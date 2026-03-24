# Recallable Knowledge Analysis: How Learning Would Transform Agent Quality

**Date:** 2026-03-24
**Scope:** Seven-dimension analysis of what the Crux ecosystem loses by not closing the knowledge loop, and what it gains by closing it
**Basis for:** Build plan to make recallable knowledge operational

---

## Executive Summary

The Crux ecosystem captures 9,949 interactions, 1,122 conversations, and 6 corrections across active projects. It uses almost none of this data. Digests produce 129-byte empty files. The corrections system has captured 6 entries in weeks of use, none of which are actual agent self-corrections -- they are user messages misclassified as corrections. The knowledge store has 3 manual entries. The conversation logs contain hundreds of architectural decisions, user preferences, and error patterns that are never extracted.

The system is a write-only database. Every dimension of agent quality -- code, decisions, errors, convergence, UX, cross-project learning -- degrades because of this. Below is the dimension-by-dimension analysis of what changes when recallable knowledge works.

---

## Dimension 1: Code Quality

### Current State

The agent writes code from scratch every session. It has no access to:
- Past corrections ("no, use async" -- an actual correction entry from 2026-03-06)
- Code review patterns from previous convergence passes
- Common bugs in this codebase (e.g., the token-budget division-by-zero edge case mentioned in the memory report)
- Style preferences the user has expressed across sessions

The 3 knowledge entries that exist (`crux-architecture.md`, `session-switching.md`, `tdd-workflow.md`) are architecture-level. None encode code-level patterns.

### Concrete Value Lost

1. **Repeated style violations.** If the user corrects "use async/await, not callbacks" in session 1, session 2 has no memory of this. The correction was logged to `corrections.jsonl` as a user-correction category but never extracted into a knowledge entry that future sessions would read.

2. **No codebase-specific patterns.** The crux codebase uses specific patterns: `secure_makedirs()` and `secure_write_file()` for all filesystem writes (PLAN-166 security). `_validate_string_field()` for all user input. `_sanitize_error()` for all error messages. A new session working on crux code has no knowledge of these patterns unless the mode prompt happens to mention them.

3. **Test patterns lost.** The crux test suite has 1,561+ tests with a consistent structure. The agent rediscovers this structure every session instead of knowing "crux tests use pytest, fixtures in conftest.py, parametrize for edge cases, coverage enforced at 100%."

4. **Import conventions lost.** The crux codebase has a specific import pattern: `from scripts.lib.crux_<module> import <function>`. The `_ALLOWED_PROCESSOR_MODULES` allowlist in `crux_background_processor.py` enforces which modules can be dynamically imported. An agent without this knowledge could write code that passes lint but fails the security allowlist.

### What Changes With Recallable Knowledge

- **Correction-derived style rules.** Every correction tagged "style" or "pattern" auto-elevates to a mode-specific knowledge entry after 2 occurrences. The `build-py` mode prompt gets: "In this codebase: use `secure_write_file()` for all file writes; use `_validate_string_field()` for user input; use async/await not callbacks."
- **Codebase fingerprint.** At project registration, a one-time scan produces a "codebase conventions" knowledge entry: import patterns, test framework, coverage requirements, security patterns. Updated when conventions change.
- **Review pattern memory.** After each convergence pass, the audit findings that led to code changes are extracted: "Division by zero in token budget calculation" becomes a knowledge entry tagged `edge-case, token-budget`. Next time any token math is written, this surfaces.

### Implementation Ideas

1. **Auto-extract from corrections.** The `extract_corrections.py` pipeline exists but only fires when 10+ corrections accumulate (threshold in `ProcessorConfig.correction_queue_size`). Problem: only 6 entries exist, and they are misclassified. Fix: lower threshold to 2, fix detection regex in `crux_hooks.py` to distinguish actual corrections from general conversation, and wire `crux_knowledge_clustering.py`'s `auto_elevate()` into the processor pipeline.

2. **Codebase convention scanner.** New MCP tool `scan_conventions` that reads the project's test runner config, linting config, import patterns, and security patterns. Produces a `conventions.md` knowledge entry. Runs once at `crux init` and on-demand.

3. **Post-review extraction.** After any convergence pass that produces findings, extract the finding categories into knowledge entries tagged by file/module pattern. The `convergence_submit_result` MCP tool already accepts findings JSON -- add a post-processing step.

---

## Dimension 2: Decision Continuity

### Current State

Architectural decisions live in three places:
1. `session state.json` `key_decisions` array (4 entries currently: "Crux adopted with 60 security fixes", "Phase 1: read-only MCP tools only", etc.)
2. Conversation logs (1,122 entries containing hundreds of decisions buried in natural language)
3. The user's head

Session state survives within a session. Conversation logs are never read. When a new session starts, the agent gets the mode prompt and whatever is in `state.json` -- which is overwritten each session.

### Concrete Value Lost

1. **Re-debating settled questions.** The decision "Crux venv created at ~/.crux/.venv" is in the current session state. But what about the reasoning? Why not a project-local venv? Why not system Python? That reasoning exists in a conversation from March 6 but is inaccessible. If someone asks "should we move the venv?" next week, the agent will reason from scratch.

2. **Build plan amnesia.** CruxCLI's BUILD_PLAN_001 had 6 phases, each with decisions. Phase 3 decided to "replace 6 prompt injection points with Crux mode-driven prompts." Phase 5 decided "token budgets replace step-count limits." These are in the build plan document, but the agent in a new session doesn't know which decisions were contested, which had alternatives considered, which were user preferences vs. technical necessities.

3. **Cross-session drift.** The roadmap states "NEVER maintain a rebase relationship with OpenCode." This is a strategic decision. But it's in a markdown file the agent may or may not read. If it's in recallable knowledge tagged `strategy, opencode, fork`, it surfaces automatically whenever OpenCode-related work begins.

### What Changes With Recallable Knowledge

- **Decision log with rationale.** Every session that produces architectural decisions auto-extracts them with rationale. Not just "use async" but "use async because the file I/O in the background processor blocks the event loop; sync approach caused 30s hangs in testing."
- **Decision search at session start.** When a session begins in a mode, `lookup_knowledge` is called with the `working_on` context. Relevant past decisions surface in the system prompt.
- **Contradiction detection.** If a new session's direction contradicts a stored decision, the agent flags it: "Note: previous decision was X because of Y. Proceeding with Z contradicts this. Confirm?"

### Implementation Ideas

1. **Session-end decision extraction.** At session archive (the `archive_session()` call that currently deletes handoff.md), scan the conversation log for decision indicators: "we decided", "the approach is", "going with", user confirmations after deliberation. Write each as a knowledge entry with `decision` tag and the conversation context as rationale.

2. **Handoff preservation.** The report identified that `archive_session()` deletes `handoff.md`. One-line fix: copy to `.crux/sessions/history/handoff-{timestamp}.md` before deletion. This preserves the context that was important enough to write down during a mode switch.

3. **Decision index.** A `decisions.jsonl` file in `.crux/knowledge/` that indexes all decision entries with their tags, date, and a one-line summary. The `lookup_knowledge` tool searches this index first for fast retrieval.

---

## Dimension 3: Error Prevention

### Current State

The agent has no memory of past failures. The corrections system has 6 entries, none of which capture "I tried X and it failed because Y." The conversation logs contain many such failure patterns, but they are never read back.

The `extract_corrections.py` module can parse corrections, cluster them, and generate knowledge candidates. The `crux_knowledge_clustering.py` module can auto-elevate clusters. Neither runs because the corrections system is not capturing real corrections.

### Concrete Value Lost

1. **Repeated type errors.** The most recent commit on the CruxCLI repo is `fix: resolve typecheck errors in llm.ts and token-budget.ts`. If this is the kind of error that recurs (TypeScript type mismatches in specific modules), it should be in knowledge. Instead, the next person (or agent) working on those files will hit the same type issues.

2. **Build failures from known causes.** The CruxCLI build plan phase 6 was "build verified, all phases complete." The path to "verified" likely involved build failures. What broke? What was the fix? Those are in conversation logs but will never be recalled.

3. **Security patterns rediscovered.** Crux had a PLAN-166 security audit that fixed 60 vulnerabilities. The patterns of those vulnerabilities (path traversal, unsanitized error messages, unbounded file reads) are encoded in the code but not in knowledge. A new module written without this context could reintroduce the same vulnerability classes.

4. **Edge cases in the convergence engine.** The memory report mentions "token budget code always has a division-by-zero edge case." If this is a recurring pattern, it should be a knowledge entry: "When writing token budget arithmetic, always guard against zero denominators." Without it, every convergence pass that touches token math re-discovers this.

### What Changes With Recallable Knowledge

- **"Mistakes learned" database.** Every error that required manual intervention gets a knowledge entry: the error, the root cause, the fix, and the prevention pattern. Tagged by module, error type, and mode.
- **Pre-flight error checks.** Before writing code in a module with known error patterns, the agent checks knowledge for that module. "This module has 2 known error patterns: type mismatches in the LLM response parsing, and division-by-zero in budget calculation."
- **Convergence acceleration.** The convergence engine's audit phase checks knowledge for known issues in the files being audited. First-pass audits catch known patterns immediately instead of rediscovering them.

### Implementation Ideas

1. **Error extraction from git history.** Scan commit messages for patterns: "fix:", "resolve", "patch", "workaround". For each, extract the file(s) changed and the error description. Write as knowledge entries tagged `error-pattern, {module}`.

2. **Post-mortem hook.** When the user reports a bug or the agent fixes an error, auto-create a knowledge entry: `{error_description, root_cause, fix, prevention_rule, affected_files}`. This is a new hook event: `ErrorResolved`.

3. **Security pattern library.** Extract the PLAN-166 security patterns into a `security-patterns.md` knowledge entry that every mode's prompt references. The patterns are already in the code (the `_is_safe_path`, `_validate_string_field`, `_sanitize_error`, `_MAX_FIELD_SIZE` constants) -- they just need to be documented as recallable knowledge.

---

## Dimension 4: Convergence Speed

### Current State

CruxDev's convergence engine runs audit-fix-re-audit loops. The MCP tools (`start_convergence`, `convergence_next_task`, `convergence_submit_result`) drive the loop. Each convergence run starts from zero knowledge of previous runs.

The `.cruxdev/` directory in the crux project is empty. No convergence state has been persisted between sessions despite 12 completed convergence runs mentioned in the memory report.

### Concrete Value Lost

1. **Rediscovering audit dimensions.** Each convergence run audits across 8 code dimensions and 5 doc dimensions. The findings from previous runs (e.g., "160 stale org references found in doc alignment") are not available to new runs. A new convergence on the same codebase starts from scratch.

2. **No pattern transfer between convergence targets.** If converging project A revealed that "all JSONL append operations need atomic writes," this pattern is not available when converging project B. The same finding gets rediscovered.

3. **Audit false positive accumulation.** Convergence uses a two-consecutive-clean-pass rule. If certain audit findings are repeatedly flagged and then marked as acceptable (false positives), that judgment is lost. The next convergence re-flags and re-evaluates the same false positives.

4. **Fix pattern duplication.** When the convergence engine finds an issue and generates a fix, the fix approach is not stored. If the same class of issue appears in another file or project, the fix is re-derived instead of recalled.

### What Changes With Recallable Knowledge

- **Convergence memory.** Each completed convergence writes a post-mortem: findings count by dimension, fix patterns applied, false positives identified, time to convergence. Tagged `convergence, {project}, {plan}`.
- **Pre-seeded audit context.** When a new convergence starts on a project that has previous convergence history, the audit phase begins with known patterns: "Previous convergence found 160 stale org references. Check if this class of issue persists."
- **Fix pattern library.** Convergence fixes (atomic writes, input validation, error sanitization) accumulate in knowledge. The engine's fix generation can reference these instead of deriving from first principles.
- **Estimated convergence time.** With history, the engine can estimate: "Based on 12 previous convergences, a project of this size typically converges in 3-5 passes."

### Implementation Ideas

1. **Post-convergence extraction.** After `convergence_status` returns `done`, auto-generate a knowledge entry from the convergence state: dimensions audited, findings per dimension, passes to convergence, false positives flagged. Store in `.crux/knowledge/convergence/`.

2. **False positive registry.** A `false_positives.jsonl` that records findings explicitly marked acceptable. The audit phase checks this registry before flagging. Reduces noise in subsequent convergences.

3. **Fix pattern index.** When a convergence fix is applied, record `{finding_type, fix_approach, files_affected}`. The engine queries this index when generating fixes for similar findings.

4. **Cross-project convergence patterns.** The `crux_cross_project.py` module already scans projects. Extend it to aggregate convergence post-mortems and surface patterns: "Across 3 projects, the most common finding is missing input validation (47 instances)."

---

## Dimension 5: User Experience

### Current State

The user must manually tell the agent to remember things. The memory report's trust assessment shows 5 of 7 trust questions answered "NO." The user has to:
- Say "remember this" for Claude Code memory
- Call `promote_knowledge` MCP tool for Crux knowledge
- Manually verify that what they said was actually saved
- Re-state preferences and context at the start of every new session
- Accept that corrections are not being learned from

The session state JSON shows `key_decisions` and `pending` arrays that were manually curated. None of this happened automatically.

### Concrete Value Lost

1. **Cognitive tax on the user.** Every time the user thinks "the agent should know this," they face a choice: spend time telling the agent to save it, or accept it will be lost. This is a constant low-grade friction that erodes trust. The user eventually stops trying to teach the agent because the effort-to-reliability ratio is too low.

2. **Lost corrections.** Looking at the actual corrections.jsonl: the 6 entries include what appear to be normal conversation messages misclassified as corrections. Entry 2 is a massive product spec paste. Entry 6 is a task notification. The correction detection regex in `crux_hooks.py` is not distinguishing corrections from general input. The user has no visibility into this -- they assume the system is learning.

3. **Session start overhead.** Every new session, the user re-establishes context: "We're working on X, last time we decided Y, the approach is Z." This is exactly what recallable knowledge should provide. The 4 entries in `state.json` `key_decisions` cover some of this, but they are session-specific and overwritten.

4. **Trust decay.** The competitive analysis positions Crux's unique advantage as "correction detection + organic knowledge generation + cross-session memory." These are listed as features no competitor has. But in practice, correction detection captures noise, knowledge generation requires manual intervention, and cross-session memory is fragile. The marketed differentiator is not working.

### What Changes With Recallable Knowledge

- **Zero-effort knowledge capture.** The user never has to say "remember this." The system detects decisions, preferences, corrections, and patterns automatically. The user's mental model shifts from "I have to manage the agent's memory" to "the agent remembers."
- **Session start context injection.** New sessions begin with a synthesized context block: recent decisions, active preferences, known error patterns, pending work. The user validates instead of reconstructing.
- **Visible learning.** When the agent applies a recalled correction, it says so: "Using async per your preference from March 6." The user sees the system working. Trust compounds.
- **Correction quality feedback.** The agent can periodically ask: "I've captured these as corrections. Are they accurate?" This closes the feedback loop on correction detection quality.

### Implementation Ideas

1. **Fix correction detection.** The `UserPromptSubmit` handler in `crux_hooks.py` needs a rewrite of its correction detection logic. Current approach likely matches too broadly. New approach: score prompts on a correction-likelihood scale using multiple signals (negation + reference to agent output, imperative mood + topic change, explicit "no/wrong/actually"). Threshold at high confidence only.

2. **Active memory prompts.** At session end, the agent evaluates: "Did I learn anything this session that should persist?" Generates candidate knowledge entries. In auto mode, writes them. In confirm mode, asks the user to approve. Configurable per mode.

3. **Context synthesis at session start.** New MCP tool `synthesize_context` that reads recent conversations, knowledge entries, and session history to produce a 500-word context block injected into the system prompt. Replaces the current approach of loading raw `state.json`.

4. **Learning transparency log.** A `.crux/learning.jsonl` that records every auto-created knowledge entry with its source (correction, conversation extraction, convergence post-mortem). The user can audit what the system has learned and correct misunderstandings.

---

## Dimension 6: Cross-Project Learning

### Current State

The user works across at least 6 projects visible in `~/.claude/projects/`: crux, cruxcli, cruxdev, local-llm, sb/pp (self-assessment app), and several trinsik collaboration projects. The Crux cross-project system (`crux_cross_project.py`) can discover projects and aggregate data, but:
- The project registry (`~/.crux/projects.json`) must be manually populated via `register_project` MCP tool
- Cross-project knowledge promotion requires a pattern to appear in 2+ projects (`check_cross_project_promotion`)
- The digest aggregation (`get_cross_project_digest` MCP tool) exists but produces empty digests

The knowledge store has a two-scope model: project (`.crux/knowledge/`) and user (`~/.crux/knowledge/`). User-scope is meant for cross-project patterns. It appears empty or unused.

### Concrete Value Lost

1. **Security patterns not shared.** The PLAN-166 security audit produced patterns (path validation, input sanitization, atomic writes, bounded reads) in the crux project. The cruxcli project (a TypeScript hard fork) would benefit from the same patterns translated to TypeScript. Currently no mechanism transfers this knowledge.

2. **Testing philosophy not shared.** Crux enforces 100% test coverage. If the user adopts this philosophy across projects, each project's agent has to be told independently. Knowledge like "this user requires 100% coverage, uses pytest/vitest, wants TDD" should be user-scope.

3. **Workflow patterns not shared.** The user's workflow patterns (convergence-driven development, build plans with numbered phases, mode-specific prompts) are consistent across projects but not encoded as shared knowledge.

4. **Common dependency patterns.** The user works with Python (crux), TypeScript/Bun (cruxcli), and Elixir (trueassess, visible in interaction logs). Cross-language patterns (error handling strategies, CI setup, project structure) transfer between projects but are not captured.

### What Changes With Recallable Knowledge

- **User-scope preferences.** Preferences expressed once ("I want 100% coverage", "use async", "positive framing not STRICTLY FORBIDDEN blocks") propagate to all projects automatically.
- **Pattern transfer.** Security patterns learned in Python auto-generate TypeScript equivalents in knowledge. The knowledge entry includes language-specific implementation guidance.
- **Project-aware context.** When starting work on cruxcli, the agent knows: "This is part of the Crux ecosystem. Related projects: crux (platform, Python), cruxdev (methodology). Key decisions from crux that affect cruxcli: [list]."
- **Methodology consistency.** CruxDev methodology patterns (convergence, audit dimensions, TDD) encoded as user-scope knowledge apply consistently across every project.

### Implementation Ideas

1. **Auto-register projects.** When Crux MCP tools are called from a new project directory, auto-register it. The `crux_hooks.py` session start handler already knows the project directory -- add a `register_if_new()` call.

2. **User-scope knowledge promotion.** When a knowledge entry exists in 2+ projects, auto-promote to `~/.crux/knowledge/`. The `check_cross_project_promotion` function exists -- wire it into the background processor.

3. **Ecosystem graph.** A knowledge entry that maps the Crux ecosystem: which projects exist, how they relate, what languages they use. Auto-updated when projects are registered. Injected into system prompt when working on any ecosystem project.

4. **Cross-language pattern translation.** When a knowledge entry is tagged with a language (e.g., `python, security`), generate a companion entry for other languages in the ecosystem. "In Python: `secure_write_file()`. In TypeScript: use `fs.writeFileSync()` with `{ flag: 'wx' }` + rename pattern."

---

## Dimension 7: Competitive Advantage

### Current State

The competitive analysis (`competitive-analysis.md`) identifies 6 unique Crux capabilities that no competitor has:
1. Automatic correction detection
2. Organic knowledge generation and cross-project promotion
3. Daily self-assessment digest with cross-tool analytics
4. Cross-tool session continuity
5. Autonomous convergence (CruxDev)
6. Build-in-public pipeline

Of these, capabilities 1-3 are the learning-related differentiators. The feature matrix in `COMPETITORS.md` lists "Correction detection," "Organic knowledge generation," and "Cross-session memory" as CruxCLI advantages.

**The problem:** These are listed as shipped features, but they do not work.

- Correction detection: 6 misclassified entries
- Organic knowledge generation: 3 manual entries
- Daily digest: 9 files, all 129 bytes (empty templates)
- Cross-session memory: depends on manual memory creation

### Concrete Value Lost

1. **Differentiator is vaporware.** The competitive matrix shows green checkmarks for capabilities that produce no actual value. If a potential user evaluates Crux by trying these features, they will find them non-functional. This is worse than not claiming the capability -- it creates a trust deficit.

2. **No empirical data for marketing.** The build-in-public pipeline (`crux bip`) is designed to generate content from real usage data. With no working knowledge loop, there is no data to publish. "Our agent learned 47 correction patterns and reduced repeat errors by 30%" is the kind of claim that would drive adoption. It requires a working system.

3. **Window closing.** The risk map identifies "OpenCode ships native memory/learning" as medium likelihood, high impact. Superpowers adding a convergence engine as low likelihood, high impact. The longer the learning system stays broken, the more likely a competitor builds it first. The competitive analysis notes: "Defensible because it requires architectural decisions (structured logging, knowledge promotion, correction detection) that are hard to retrofit." This is true -- but only if Crux actually uses these architectural decisions, not just logs data into dead ends.

### What Changes With Recallable Knowledge

- **First mover becomes real.** The "no competitor has closed-loop learning" claim becomes empirically verifiable. The agent demonstrably improves over time. This is not a feature checkbox -- it is a behavior that users experience.
- **Content pipeline activates.** `crux bip` can generate posts like: "Week 3: Crux learned 12 new patterns. Error repeat rate dropped from 40% to 15%. Most common correction: style preferences." Real data, real improvement, real content.
- **Moat deepens with usage.** Every user's Crux installation becomes more valuable over time as knowledge accumulates. Switching costs increase. No competitor can offer "bring your learning history with you" because no competitor has the history.
- **Enterprise story.** "Our AI coding agent has a verifiable learning audit trail" is a compliance and quality story that no competitor can tell. The `learning.jsonl` transparency log becomes an enterprise feature.

### Implementation Ideas

1. **Fix the basics first.** Correction detection, digest generation, and knowledge extraction must work before any competitive advantage claim is credible. This is the foundation.

2. **Learning metrics dashboard.** New MCP tool `get_learning_stats`: knowledge entries created (auto vs manual), corrections captured, patterns transferred cross-project, convergence acceleration metrics. Feeds `crux bip` and user-facing transparency.

3. **Before/after benchmarks.** Instrument the convergence engine to track: time-to-convergence on projects with learning history vs without. This produces the empirical data needed to market the capability.

4. **Competitive demo scenario.** Build a demo that runs the same task in Crux (with learning) and a competitor (without). Show the Crux agent avoiding a known error on the second attempt. Publish the comparison.

---

## Recommended Build Order

### Phase 0: Fix What's Broken (1-2 days)

**Goal:** Make existing systems functional before building new ones.

| Task | Why | Effort |
|------|-----|--------|
| Fix correction detection regex in `crux_hooks.py` | The 6 entries are misclassified noise. Detection must distinguish corrections from general conversation. Score on multiple signals: negation + agent reference, imperative + topic change, explicit rejection words. | 4 hours |
| Fix digest generation | 9 files at 129 bytes each. The `generate_digest` module is producing template headers with zero data. Diagnose: is it not reading interaction files, or not producing summaries? The interaction files have data (9,949 entries). | 4 hours |
| Archive handoffs before deletion | One-line fix in `archive_session()`: copy `handoff.md` to `sessions/history/` before delete. | 30 minutes |
| Lower correction processing threshold | `ProcessorConfig.correction_queue_size` is 10. With a working correction detector, lower to 3 to get faster feedback. | 15 minutes |

### Phase 1: Conversation-to-Knowledge Pipeline (3-5 days)

**Goal:** Extract decisions, preferences, and patterns from the 1,122 conversation entries sitting unused.

| Task | Why | Effort |
|------|-----|--------|
| Build conversation decision extractor | Scan conversation JSONL for decision indicators. Extract structured entries: `{decision, rationale, context, date, mode}`. | 1 day |
| Build session-end evaluator | At session end (Stop hook), evaluate: "Did the user correct me? Express a preference? Make a decision?" Auto-generate candidate knowledge entries. | 1 day |
| Wire extraction into background processor | Add as Processor 6 in `crux_background_processor.py`. Runs when conversation count exceeds threshold or at session end. | 4 hours |
| Build context synthesizer | New MCP tool `synthesize_context` that reads recent knowledge, decisions, and session state to produce a context block for session start injection. | 1 day |
| Test with real data | Run the extraction pipeline against the existing 1,122 conversation entries. Validate quality. Tune thresholds. | 1 day |

### Phase 2: Error and Pattern Memory (2-3 days)

**Goal:** Build the "mistakes learned" database.

| Task | Why | Effort |
|------|-----|--------|
| Git history error extractor | Scan commit messages for "fix:", "resolve", "patch" patterns. Extract error descriptions and affected files into knowledge entries. | 4 hours |
| Post-error knowledge creation | When the agent fixes an error during a session, auto-create a knowledge entry: error, root cause, fix, prevention rule. | 1 day |
| Security pattern library | Extract PLAN-166 patterns from crux codebase into a `security-patterns.md` knowledge entry. Reference from all mode prompts. | 4 hours |
| Module-level error index | Index which modules have known error patterns. Surface at session start when those modules are in scope. | 4 hours |

### Phase 3: Convergence Memory (2-3 days)

**Goal:** Make each convergence run faster than the last.

| Task | Why | Effort |
|------|-----|--------|
| Post-convergence knowledge extraction | After `convergence_status` returns done, auto-extract findings into knowledge entries. | 1 day |
| False positive registry | Record explicitly-accepted audit findings. Check before re-flagging. | 4 hours |
| Fix pattern library | Record convergence fixes with finding type and approach. Query when generating fixes for similar findings. | 4 hours |
| Pre-seeded audit context | When starting convergence on a project with history, inject known patterns into the first audit pass. | 4 hours |

### Phase 4: Cross-Project and Cross-Tool Sync (2-3 days)

**Goal:** Knowledge flows between projects and between Crux and Claude Code memory.

| Task | Why | Effort |
|------|-----|--------|
| Auto-register projects | On first MCP call from a new project dir, auto-register in `~/.crux/projects.json`. | 2 hours |
| Wire cross-project promotion | Call `check_cross_project_promotion` in background processor when new knowledge entries are created. | 4 hours |
| Bidirectional Crux-Claude sync | When Crux creates a knowledge entry, create a corresponding Claude Code memory file. When Claude memory is created, create a Crux knowledge entry. | 1 day |
| Ecosystem graph | Auto-generated knowledge entry mapping all registered projects, their relationships, and languages. | 4 hours |

### Phase 5: Metrics and Competitive Proof (1-2 days)

**Goal:** Prove the system works with data.

| Task | Why | Effort |
|------|-----|--------|
| Learning stats MCP tool | `get_learning_stats`: entries created, corrections captured, patterns transferred, convergence acceleration. | 4 hours |
| Before/after instrumentation | Track convergence time and error rates with and without learning history. | 4 hours |
| Wire to BIP pipeline | Feed learning metrics into `crux bip` for automated content generation. | 4 hours |
| Update competitive matrix | Replace aspirational checkmarks with empirical results. | 2 hours |

---

## Total Estimated Effort

| Phase | Days | Dependencies |
|-------|------|-------------|
| Phase 0: Fix What's Broken | 1-2 | None |
| Phase 1: Conversation-to-Knowledge | 3-5 | Phase 0 |
| Phase 2: Error and Pattern Memory | 2-3 | Phase 0 |
| Phase 3: Convergence Memory | 2-3 | Phase 1 |
| Phase 4: Cross-Project Sync | 2-3 | Phase 1 |
| Phase 5: Metrics and Proof | 1-2 | Phases 1-4 |
| **Total** | **11-18** | |

Phases 1 and 2 can run in parallel after Phase 0. Phases 3 and 4 can run in parallel after Phase 1.

---

## The Core Insight

The data capture architecture is already built. 9,949 interactions, 1,122 conversations, session states, corrections infrastructure, knowledge stores, cross-project aggregation, background processors, and MCP tools all exist. The code for extraction (`extract_corrections.py`), clustering (`crux_knowledge_clustering.py`), cross-project promotion (`crux_cross_project.py`), and background processing (`crux_background_processor.py`) is written, tested, and has security hardening.

The gap is not architectural. It is operational. The correction detector is miscalibrated. The digest generator has a bug that produces empties. The processing thresholds are too high for the current data volume. The handoff archival has a deletion bug. These are fixable in days, not weeks.

The difference between "agent that logs everything and uses nothing" and "agent that learns from every session" is approximately 15 working days of focused effort on the existing codebase. No new architecture required. Fix the broken pipelines, lower the thresholds, wire the extractors to the knowledge store, and close the loop.

Every dimension of quality -- code, decisions, errors, convergence, UX, cross-project, and competitive positioning -- improves when the loop closes. The system was designed for this. It just needs to be turned on.
