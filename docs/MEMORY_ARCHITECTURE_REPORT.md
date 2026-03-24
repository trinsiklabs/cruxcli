# Memory Architecture Report: How the Crux Ecosystem Handles Persistent Knowledge

**Date:** 2026-03-24
**Requested by:** Key
**Scope:** Full gauntlet — what works, what's broken, gaps, missed opportunities

---

## The Question

> How does the architecture handle making sure information actually gets regularly documented in a recallable way, so that you can trust information gets saved and don't have to ask the agent to save data constantly?

## The Short Answer

**You can't trust it.** The system logs everything but uses almost nothing. It's write-heavy, read-light. Data flows into five separate stores across three products, but there's no pipeline turning raw logs into actionable, recallable knowledge. The corrections system is broken. The digest generator produces empty files. Conversations are logged but never summarized. The only reliable path is manual — you have to tell the agent to save things.

---

## What Exists (Four Memory Layers)

### Layer 1: Crux Session State (WORKS)
- **What:** Current mode, working_on, key_decisions, pending tasks, files_touched
- **Trigger:** Automatic — hooks fire on every tool call and session start
- **Storage:** `.crux/sessions/state.json`
- **Recall:** Injected into system prompt at session start
- **Trust level:** HIGH — this is reliable within a session

### Layer 2: Crux Knowledge (WORKS, but manual only)
- **What:** Project knowledge entries, mode-specific knowledge
- **Trigger:** Manual — user calls `promote_knowledge` MCP tool
- **Storage:** `.crux/knowledge/*.md`, `.crux/knowledge/by-mode/<mode>/*.md`
- **Recall:** `lookup_knowledge` MCP tool searches across priority-ordered dirs
- **Trust level:** MEDIUM — works well when used, but nothing auto-promotes

### Layer 3: Claude Code Memory (WORKS, but manual only)
- **What:** User preferences, feedback, project context, references
- **Trigger:** Manual — user says "remember this" or agent decides to save
- **Storage:** `~/.claude/projects/<hash>/memory/*.md` + `MEMORY.md` index
- **Recall:** `MEMORY.md` loaded at conversation start (first 200 lines)
- **Trust level:** MEDIUM — same problem: nothing auto-creates memories

### Layer 4: Raw Logs (LOGGED, NEVER USED)
- **What:** Every interaction, correction, conversation turn
- **Trigger:** Automatic — hooks fire on every event
- **Storage:** `.crux/analytics/interactions/*.jsonl`, `.crux/analytics/conversations/*.jsonl`, `.crux/corrections/corrections.jsonl`
- **Recall:** **Nothing reads these.** 22k+ interaction entries, 1087 conversation entries, sitting unused.
- **Trust level:** ZERO for recall — data exists but is never surfaced

---

## What's Broken

### 1. Corrections System Is Dead
- Only **6 entries** in `corrections.jsonl` despite months of work
- The `UserPromptSubmit` hook is wired up but entries aren't being created
- Either the hook isn't firing or the correction detection logic isn't matching user patterns
- **Impact:** The "continuous learning" promise is not being delivered

### 2. Digest Generation Produces Empty Files
- 9 digest files exist, all exactly **129 bytes** (template headers, no content)
- The background processor claims to generate digests but produces empties
- **Impact:** No daily summaries, no weekly reviews, no "what did we work on?"

### 3. Background Processor Isn't Reliably Running
- Threshold-triggered (10 corrections, 50 interactions, 24hrs since last run)
- If the session exits before thresholds are hit, processing is skipped
- No monitoring, no retry, no guarantee of execution
- **Impact:** Pending work gets silently dropped

### 4. Handoff Context Is Ephemeral
- Mode switches write to `.crux/sessions/handoff.md`
- `archive_session()` **deletes it** — context lost forever
- Should archive before deletion
- **Impact:** Context lost on every mode switch

---

## Gaps and Missed Opportunities

### Gap 1: No Conversation → Knowledge Pipeline
The biggest missing piece. The system logs 1087 conversation entries but never asks: "What did we learn today? What decisions were made? What patterns emerged?" There's no extraction step turning conversations into searchable knowledge.

**Opportunity:** A nightly processor that reads today's conversations, extracts decisions and insights, and writes them as knowledge entries. Zero manual effort.

### Gap 2: No Cross-Session Pattern Detection
Session archives pile up in `.crux/sessions/history/` but nothing reads them. The system can't tell you:
- "This problem has come up 3 times"
- "Last time you tried X, it failed because Y"
- "You've been working on auth for 4 sessions now"

**Opportunity:** A session summarizer that indexes history and surfaces patterns.

### Gap 3: No Cross-Tool Synchronization
Crux knowledge and Claude Code memory are separate stores. If you save a correction via Crux MCP, Claude Code's memory doesn't know about it. If Claude Code learns a preference, Crux doesn't see it.

**Opportunity:** Bidirectional sync — Crux knowledge entries auto-create Claude Code memory files, and vice versa.

### Gap 4: No Automatic Memory Creation
Both Crux knowledge and Claude Code memory require manual triggers. The system never proactively says "this seems important, I should save it." Claude Code's auto-memory system (in its prompt) suggests saving feedback and user preferences, but in practice this rarely fires without user prompting.

**Opportunity:** Active memory — after each session, automatically evaluate: "Did the user correct me? Did they express a preference? Did we make a decision?" and auto-save.

### Gap 5: CruxDev Convergence Learnings Are Lost
12 convergence runs completed, but no cross-run learning. The engine doesn't know:
- "Last time we converged a build plan, the doc alignment phase found 160 stale org references"
- "Token budget code always has a division-by-zero edge case"

**Opportunity:** Post-convergence knowledge extraction — "What did this convergence teach us?"

### Gap 6: No Memory Verification
When memory IS created, there's no verification that it's still accurate. Code changes, files get renamed, patterns evolve. Stale memory is worse than no memory — it generates confident but wrong recommendations.

**Opportunity:** Memory aging + verification — flag memories older than N days for re-verification.

---

## Trust Assessment

| Question | Answer |
|----------|--------|
| Can I trust session state is saved? | YES — within a session |
| Can I trust decisions are preserved across sessions? | PARTIAL — if manually saved |
| Can I trust corrections are being learned from? | NO — system is broken |
| Can I trust the agent remembers what we worked on last week? | NO — depends on manual memory |
| Can I trust knowledge is being accumulated automatically? | NO — all manual |
| Can I trust handoff context survives mode switches? | NO — deleted on archive |
| Can I trust digests summarize activity? | NO — empty files |

---

## Recommendations (Priority Order)

1. **Fix the digest pipeline** — this is the foundation. If daily digests work, everything else can build on them. Diagnose why 129-byte empties are generated.

2. **Fix the corrections system** — verify the UserPromptSubmit hook fires, verify correction detection regex matches real user patterns, verify JSONL append works.

3. **Build conversation → knowledge extraction** — nightly processor reads conversations, extracts decisions/insights, writes knowledge entries. This is the highest-leverage gap.

4. **Archive handoffs before deletion** — one-line fix: copy handoff.md to history/ before `archive_session()` deletes it.

5. **Add active memory to session hooks** — at session end, evaluate "what should be remembered?" and auto-write to both Crux knowledge and Claude Code memory.

6. **Sync Crux ↔ Claude Code memory** — bidirectional: knowledge entries create memory files, memory files create knowledge entries.

7. **Add convergence post-mortems** — after each convergence, auto-extract "what did we learn?" into knowledge.

---

## Architecture Diagram (Current vs Target)

### Current: Write Everything, Use Nothing
```
User correction → corrections.jsonl → (dead end)
Conversation    → conversations.jsonl → (dead end)
Interaction     → interactions.jsonl → (dead end)
Session state   → state.json → system prompt ✓
Knowledge       → knowledge/*.md → lookup_knowledge ✓ (manual only)
Claude Memory   → memory/*.md → session start ✓ (manual only)
```

### Target: Closed-Loop Learning
```
User correction → corrections.jsonl → processor → knowledge entry → search
Conversation    → conversations.jsonl → processor → daily digest + insights → knowledge
Interaction     → interactions.jsonl → processor → pattern detection → corrections
Session state   → state.json → system prompt + session archive → cross-session patterns
Knowledge       → knowledge/*.md → bidirectional sync → Claude Memory
Convergence     → state.json → post-mortem → knowledge entry
```

The difference is **pipelines**. The data capture is there. The extraction and feedback loops are not.
