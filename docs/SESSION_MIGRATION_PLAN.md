# Session Migration Plan: Claude Code <-> CruxCLI Seamless Handoff

**Date:** 2026-03-24
**Author:** Key + Claude Opus 4.6
**Status:** Design Phase
**Depends on:** MEMORY_ARCHITECTURE_REPORT.md recommendations

---

## The Problem

A session in Claude Code (Opus 4.6, Pro Max, 1M context) accumulates value: decisions made, corrections applied, files understood, context built up over dozens of turns. When switching to CruxCLI (OpenRouter, any model), all of that is lost. The user has to re-explain everything. The same problem exists in reverse.

The two tools share a project directory. They share Crux as an MCP server. But they don't share session state in any meaningful way.

**Goal:** Make switching between Claude Code and CruxCLI feel like switching browser tabs, not starting over.

---

## Architecture Overview

```
                        CLAUDE CODE                          CRUXCLI
                   ┌─────────────────────┐            ┌─────────────────────┐
                   │  ~/.claude/projects/ │            │  SQLite DB          │
                   │    <hash>/<sid>.jsonl│            │  session/message/   │
                   │                     │            │  part tables        │
                   │  Format: JSONL      │            │  Format: Drizzle ORM│
                   │  (user/assistant/   │            │  (MessageV2 schema) │
                   │   tool-use/result/  │            │                     │
                   │   file-history)     │            │                     │
                   └────────┬────────────┘            └────────┬────────────┘
                            │                                  │
                            │         CRUX BRIDGE              │
                            │   ┌─────────────────────┐        │
                            └──>│  .crux/sessions/     │<──────┘
                                │    state.json        │
                                │    migration/        │  <-- NEW
                                │      manifest.json   │
                                │      context.md      │
                                │      decisions.json   │
                                │      files.json      │
                                │                      │
                                │  .crux/knowledge/    │
                                │    (persistent)      │
                                │                      │
                                │  MCP Tools:          │
                                │    write_handoff     │
                                │    read_handoff      │
                                │    restore_context   │
                                │    get_session_state │
                                └──────────────────────┘
```

**Flow:**
1. Exiting tool writes migration snapshot to `.crux/sessions/migration/`
2. Crux MCP tools mediate the format
3. Entering tool reads migration snapshot and reconstitutes context

---

## Data Mapping: What Exists in Each Tool

### Claude Code Session Data (~/.claude/projects/<hash>/<session>.jsonl)

Each line is one of these types:

| Type | Fields | Migration Value |
|------|--------|----------------|
| `user` | `message.content`, `cwd`, `gitBranch`, `permissionMode`, `timestamp`, `parentUuid` | HIGH -- conversation history |
| `assistant` | `message.content` (thinking, text, tool_use), `message.usage`, `model` | HIGH -- decisions, reasoning |
| `file-history-snapshot` | `snapshot.trackedFileBackups`, `timestamp` | MEDIUM -- file state at points in time |
| Tool results | Embedded in assistant content blocks as `tool_result` | MEDIUM -- what was discovered |

Key structural details:
- Messages are linked via `parentUuid` (tree structure, supports sidechains)
- Session ID is a UUID stored in each message and as the filename
- Model info: `message.model` field (e.g., `claude-opus-4-6`)
- Token usage: `message.usage` with `input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`
- Subagent sessions stored in `<session>/subagents/agent-<id>.jsonl`

### CruxCLI Session Data (SQLite via Drizzle ORM)

| Table | Key Fields | Migration Value |
|-------|-----------|----------------|
| `session` | `id`, `project_id`, `title`, `directory`, `version`, `summary_*`, `permission` | HIGH -- session metadata |
| `message` | `id`, `session_id`, `data` (JSON: User or Assistant info) | HIGH -- conversation |
| `part` | `id`, `message_id`, `session_id`, `data` (JSON: Part union type) | HIGH -- tool calls, text, reasoning |
| `todo` | `session_id`, `content`, `status`, `priority` | MEDIUM -- task tracking |

CruxCLI MessageV2 part types:
- `text` -- assistant text output
- `reasoning` -- chain-of-thought
- `tool` -- tool call with state machine (pending -> running -> completed/error)
- `file` -- attached files
- `step-start` / `step-finish` -- LLM call boundaries with token counts
- `compaction` -- context window management markers
- `subtask` -- delegated agent tasks
- `snapshot` / `patch` -- file state tracking

CruxCLI Assistant message metadata:
- `modelID`, `providerID`, `agent`, `mode`
- `tokens`: `{ input, output, reasoning, cache: { read, write } }`
- `cost`: computed cost
- `path`: `{ cwd, root }`

### Crux Bridge Layer (.crux/)

Already exists and partially bridges both tools:

| Component | What It Provides | Migration Role |
|-----------|-----------------|----------------|
| `sessions/state.json` | active_mode, working_on, key_decisions, pending, files_touched | **PRIMARY BRIDGE** -- shared state |
| `knowledge/*.md` | Promoted knowledge entries | Persistent across all sessions |
| `knowledge/by-mode/` | Mode-specific knowledge | Carries mode context |
| `modes/*.md` | Mode prompts (plan, debug, build-py, etc.) | Ensures consistent behavior |
| `corrections/` | Logged corrections (broken, but fixable) | Learning persistence |
| `config.json` | default_mode, digest_cadence | Shared configuration |
| MCP: `write_handoff` / `read_handoff` | Ephemeral context passing | **KEY MECHANISM** for migration |
| MCP: `restore_context` | Full context recovery at session start | **Existing entry point** for migration |
| MCP: `update_session` | Write decisions, files, pending tasks | Keep Crux state current |
| MCP: `get_session_state` | Read current Crux state | Bootstrap new session |

---

## Model Capability Differences

### Opus 4.6 (Claude Code, Pro Max)
- Context: 1,000,000 tokens
- Output: 128,000 tokens
- Extended thinking: Yes (signed)
- Tool use: Native Anthropic format
- Caching: ephemeral 5m + ephemeral 1h tiers
- Cost: $5/$25 per M tokens (under 200k), $10/$37.50 (over 200k)

### OpenRouter Models (CruxCLI)
- Opus 4.6 via OpenRouter: 1M context, 128k output, $5/$25
- Sonnet 4.6: 200k context, lower cost
- Gemini models: up to 1M context
- Grok models: up to 2M context
- Open-weight models: 128k-256k context, very low cost

### Migration Implications

| Concern | Solution |
|---------|----------|
| Context window shrinks (1M -> 200k) | Compact context before migration; prioritize recent + decisions |
| Extended thinking format differs | Strip thinking signatures; convert to text summaries |
| Tool schemas differ | Map tool names; Claude Code tools vs CruxCLI tools |
| Caching doesn't transfer | Cold start on new tool; pre-fill system prompt cache |
| Token counting differs | Re-count on target; token budget system adapts |
| Provider metadata format | Normalize through Crux bridge layer |

---

## The Migration System Design

### Phase 1: Migration Snapshot Format

A new directory `.crux/sessions/migration/` holds the transfer state:

```
.crux/sessions/migration/
  manifest.json          # Migration metadata
  context-summary.md     # LLM-generated session summary
  decisions.json         # Extracted key decisions
  file-state.json        # Files touched + their relevance
  conversation-tail.json # Last N turns in normalized format
  pending-tasks.json     # Unfinished work
```

**manifest.json:**
```json
{
  "version": 1,
  "created": "2026-03-24T12:00:00Z",
  "source": {
    "tool": "claude-code",
    "model": "claude-opus-4-6",
    "sessionId": "59bd2e90-43f2-4ef8-a22c-486744476568",
    "project": "/Users/user/personal/cruxcli",
    "totalTokens": 450000,
    "messageCount": 87
  },
  "target": {
    "tool": "cruxcli",
    "suggestedModel": "anthropic/claude-opus-4.6",
    "contextBudget": 200000
  },
  "cruxState": {
    "active_mode": "build-py",
    "working_on": "session migration system",
    "key_decisions": ["..."],
    "pending": ["..."],
    "files_touched": ["..."]
  }
}
```

**context-summary.md:**
LLM-generated summary of the session, structured for injection into a new system prompt. This is the critical piece -- it's not raw conversation history, it's distilled context. Sections:
- What we're building and why
- Key decisions made and their rationale
- Current state of the work
- What's been tried and didn't work
- Open questions and blockers
- Files that matter and why

**conversation-tail.json:**
The last N turns in a normalized format that either tool can ingest:
```json
[
  {
    "role": "user",
    "content": "the user's message",
    "timestamp": 1711234567890
  },
  {
    "role": "assistant",
    "content": "the assistant's response (text only, tools summarized)",
    "model": "claude-opus-4-6",
    "toolsUsed": ["Read", "Edit", "Bash"],
    "filesModified": ["src/session/system.ts"],
    "timestamp": 1711234567900
  }
]
```

### Phase 2: Export Adapters

#### Claude Code -> Crux Migration Snapshot

The exporter reads `~/.claude/projects/<hash>/<session>.jsonl` and produces the migration snapshot.

**Implementation:** A Crux MCP tool `export_session` that:
1. Finds the active Claude Code session (from `~/.claude/sessions/*.json` -- PID-based)
2. Reads the session JSONL
3. Parses the parent-child UUID chain to reconstruct conversation order
4. Extracts:
   - All user messages (text content)
   - All assistant text responses (stripping thinking blocks)
   - Tool call summaries (tool name + input summary + output summary)
   - File modifications (from file-history-snapshot entries)
5. Generates context-summary.md using the current LLM (or a summarization prompt)
6. Writes to `.crux/sessions/migration/`

Key parsing logic for Claude Code JSONL:
```
For each line:
  if type == "user":
    extract message.content (string or content array)
    track parentUuid chain
  if type == "assistant":
    extract message.content blocks:
      - type "thinking" -> skip (or summarize)
      - type "text" -> include as text
      - type "tool_use" -> record tool name + input
      - type "tool_result" -> record output summary
  if type == "file-history-snapshot":
    record tracked files at this point
```

#### CruxCLI -> Crux Migration Snapshot

The exporter reads CruxCLI's SQLite database.

**Implementation:** A Crux MCP tool or CruxCLI command that:
1. Reads current session from SQLite (Session + Message + Part tables)
2. Walks messages in order (by `time_created`)
3. Extracts:
   - User message text (from text parts)
   - Assistant text (from text parts, excluding compaction markers)
   - Tool summaries (from tool parts with completed state)
   - Token usage (from step-finish parts)
   - File diffs (from snapshot/patch parts)
4. Generates context-summary.md
5. Writes to `.crux/sessions/migration/`

### Phase 3: Import Adapters

#### Crux Migration Snapshot -> CruxCLI

On CruxCLI session start, if migration snapshot exists:

1. Read `manifest.json` to understand source context
2. Read `context-summary.md`
3. Inject summary as a system prompt addition (via `SystemPrompt.environment()` extension)
4. Optionally: create synthetic message history from `conversation-tail.json`
   - Insert as messages in the SQLite DB with a `migrated: true` flag
   - These appear in the conversation but are marked as coming from the prior tool
5. Read `decisions.json` and merge into Crux session state
6. Read `pending-tasks.json` and create todos
7. Update token budget to account for injected context size
8. Archive the migration snapshot (move to `.crux/sessions/migration/history/`)

#### Crux Migration Snapshot -> Claude Code

This is trickier because Claude Code's session format is append-only JSONL.

Options:
1. **System prompt injection (recommended):** Use Claude Code's `MEMORY.md` or `CLAUDE.md` to inject the context summary. The `restore_context` MCP tool already provides this pathway.
2. **JSONL synthesis:** Write synthetic JSONL entries that Claude Code will read as prior conversation. Risky -- format may change between versions.
3. **Handoff-only:** Use `write_handoff` to store the context summary, then `restore_context` picks it up. This is the safest approach and uses existing infrastructure.

**Recommended approach:** Option 3 (handoff) + Option 1 (CLAUDE.md append) for persistent decisions.

### Phase 4: Automatic Export Triggers

The migration snapshot should be written automatically, not manually triggered:

| Trigger | Mechanism |
|---------|-----------|
| Claude Code session end | Hook into `session-env/*.json` PID monitoring -- when process exits, export |
| CruxCLI session end | Hook into Session archive/close event |
| Explicit user command | `/migrate` or `/handoff` slash command |
| Mode switch (via Crux) | `switch_tool_to` MCP tool triggers export before switch |
| Periodic checkpoint | Every N turns, update the migration snapshot silently |

The `switch_tool_to` MCP tool is the most natural trigger. When the user says "switch to CruxCLI," Crux should:
1. Export current Claude Code session -> migration snapshot
2. Write handoff context
3. Update session state
4. Signal CruxCLI to start (or tell user to start it)

### Phase 5: Context Compression for Smaller Windows

When migrating from a 1M-context session to a 200k-context model:

1. **Tiered summarization:**
   - Last 5 turns: verbatim (recent context is most valuable)
   - Turns 6-20: tool calls summarized, text preserved
   - Turns 21+: LLM-generated summary only

2. **Decision preservation:** All key decisions transfer regardless of compression level. These are small and high-value.

3. **File state over file history:** Don't transfer "we read file X and saw Y." Transfer "file X is relevant because Z" and let the new session re-read if needed.

4. **Token budget integration:** The `TokenBudget` system (token-budget.ts) already tracks usage. On import, set the budget baseline to account for injected context:
   ```
   effective_budget = model_context_limit - injected_context_size - output_reserve
   ```

5. **Progressive disclosure:** Don't dump everything into the system prompt. Inject a compact summary, and make the full migration data available via a tool call (`restore_full_context` or `get_migration_detail`).

---

## What Crux Already Provides

Crux is already 60% of the bridge. Here's what works today:

| Capability | Tool | Status |
|-----------|------|--------|
| Session state tracking | `update_session` / `get_session_state` | Working |
| Handoff context writing | `write_handoff` | Working (but ephemeral) |
| Handoff context reading | `read_handoff` | Working |
| Full context restoration | `restore_context` | Working |
| Knowledge persistence | `promote_knowledge` / `lookup_knowledge` | Working |
| Mode-specific prompts | Modes in `.crux/modes/*.md` | Working |
| Mode-aware model params | `cruxModelParams()` in system.ts | Working |
| Session context injection | `cruxSessionContext()` in system.ts | Working |
| Tool switching | `switch_tool_to` | Working |
| Model tier mapping | `model_tiers.json` + system.ts | Framework exists, no config file yet |

**What Crux doesn't provide yet:**
1. No session export/import tools
2. No conversation history extraction
3. No LLM-powered summarization pipeline
4. Handoff context is deleted on `archive_session()` (known bug from MEMORY_ARCHITECTURE_REPORT)
5. No normalized conversation format
6. No automatic migration triggers
7. No context compression for smaller models
8. No migration history/audit trail

---

## What Needs to Be Built

### New Crux MCP Tools

1. **`export_session`** -- Export current tool's session to migration snapshot
   - Input: `source_tool` ("claude-code" | "cruxcli"), `session_id` (optional, defaults to active)
   - Output: Path to migration snapshot
   - Reads tool-specific session data, writes normalized snapshot

2. **`import_session`** -- Import migration snapshot into current tool
   - Input: `target_tool`, `compression_level` ("full" | "summary" | "minimal")
   - Output: Imported context summary
   - Reads snapshot, adapts to target format, injects

3. **`migrate_session`** -- One-shot: export + import
   - Input: `from_tool`, `to_tool`, `compression_level`
   - Combines export and import in one call

4. **`get_migration_status`** -- Check if a migration snapshot exists
   - Output: Manifest info or "no pending migration"

### New Crux Infrastructure

5. **Session history archiver** -- Fix the handoff deletion bug
   - Before `archive_session()` deletes handoff.md, copy to `.crux/sessions/history/`
   - This is a one-line fix identified in MEMORY_ARCHITECTURE_REPORT

6. **Conversation normalizer** -- Transform tool-specific formats to/from the normalized format
   - Claude Code JSONL parser
   - CruxCLI SQLite reader
   - Normalized JSON writer

7. **Context compressor** -- LLM-powered summarization for cross-model migration
   - Uses the current model to summarize before migration
   - Tiered: verbatim recent + summarized older + decisions

### CruxCLI Changes

8. **Migration import on session start** -- Check for pending migration in `SystemPrompt.environment()`
   - If `.crux/sessions/migration/manifest.json` exists, inject context
   - Add migration context to the system prompt parts array

9. **Migration-aware token budget** -- Adjust budget for injected context
   - `TokenBudget.getConfig()` checks for active migration and reserves space

10. **`/migrate` command** -- User-facing command to trigger migration
    - Surfaces in the TUI as a command

### Claude Code Integration

11. **Auto-export hook** -- Write migration snapshot on session end
    - Crux hooks (`ToolCallFinish`, `SessionStart`) can trigger periodic snapshots
    - Or: a background watcher on the session JSONL file

12. **CLAUDE.md integration** -- Persistent decisions written to project CLAUDE.md
    - Decisions promoted through Crux knowledge also appear in CLAUDE.md
    - Claude Code reads CLAUDE.md at session start automatically

---

## Phased Build Plan

### Phase 1: Foundation (Fix What's Broken)
- [ ] Fix handoff deletion bug in `archive_session()` -- archive before delete
- [ ] Create `.crux/sessions/migration/` directory structure
- [ ] Define migration manifest JSON schema (version 1)
- [ ] Define normalized conversation format schema
- [ ] Create `model_tiers.json` for the cruxcli project with sensible defaults

### Phase 2: Export Adapters
- [ ] Build Claude Code JSONL parser (read `~/.claude/projects/<hash>/<sid>.jsonl`)
- [ ] Build conversation chain reconstructor (follow `parentUuid` links)
- [ ] Build CruxCLI SQLite session reader
- [ ] Build normalized conversation writer
- [ ] Implement `export_session` MCP tool
- [ ] Test: export a real Claude Code session, verify manifest + conversation-tail

### Phase 3: Import Adapters
- [ ] Build CruxCLI import adapter (system prompt injection path)
- [ ] Build Claude Code import adapter (handoff + CLAUDE.md path)
- [ ] Implement `import_session` MCP tool
- [ ] Add migration detection to `SystemPrompt.environment()` in CruxCLI
- [ ] Test: import a snapshot into CruxCLI, verify context is available

### Phase 4: Context Compression
- [ ] Build tiered summarization (verbatim / summarized / decisions-only)
- [ ] Integrate with token budget system
- [ ] Add `compression_level` parameter to import
- [ ] Test: migrate 1M-context session to 200k-context model
- [ ] Verify no critical context is lost at each compression level

### Phase 5: Automatic Triggers
- [ ] Hook `switch_tool_to` to trigger export before switch
- [ ] Add periodic checkpoint (every 10 turns, update migration snapshot)
- [ ] Hook CruxCLI session close to export
- [ ] Implement `/migrate` slash command in CruxCLI
- [ ] Add migration status to session UI

### Phase 6: Bidirectional Sync
- [ ] CruxCLI -> Claude Code migration path (via handoff + CLAUDE.md)
- [ ] Test full round-trip: Claude Code -> CruxCLI -> Claude Code
- [ ] Verify decisions persist across round-trips
- [ ] Add migration history audit trail in `.crux/sessions/migration/history/`

---

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Claude Code JSONL format changes between versions | HIGH | Version-check in parser; fail gracefully; keep adapter thin |
| Context summary loses critical nuance | MEDIUM | Always preserve raw decisions.json; summary is additive, not replacement |
| Token budget miscalculation after import | MEDIUM | Conservative estimate; re-count on first LLM call |
| SQLite DB locked during CruxCLI export | LOW | Read-only connection; retry with backoff |
| Migration snapshot grows unbounded | LOW | Rotate to history/ on import; cap conversation-tail at 20 turns |
| User confusion about which tool is "active" | MEDIUM | Crux session state always shows active tool; migration status in prompt |
| Handoff still deleted before archive (if fix not applied) | HIGH | Phase 1 prerequisite; block migration on unfixed handoff |
| LLM summarization hallucinates decisions | MEDIUM | Include raw decisions alongside summary; user can verify |
| OpenRouter rate limits during migration | LOW | Migration is local file operations; no API calls except optional summarization |
| Subagent sessions not captured | MEDIUM | Phase 2 should also parse subagent JSONL files in `<session>/subagents/` |

---

## Connection to Memory Architecture Improvements

This plan directly addresses several gaps identified in MEMORY_ARCHITECTURE_REPORT.md:

| Report Gap | How Migration Addresses It |
|-----------|---------------------------|
| Gap 3: No Cross-Tool Synchronization | Migration snapshot IS the sync mechanism |
| Gap 1: No Conversation -> Knowledge Pipeline | Export adapter extracts decisions -> migration -> knowledge promotion |
| Gap 4: Handoff Context Is Ephemeral | Phase 1 fixes the deletion bug; migration adds persistent handoff |
| Gap 2: No Cross-Session Pattern Detection | Migration history enables "you worked on this before" detection |
| Recommendation 5: Active memory at session end | Export trigger at session end auto-creates memory |
| Recommendation 6: Sync Crux <-> Claude Code memory | Bidirectional migration handles this |

**The migration system IS the missing pipeline.** It forces the ecosystem to:
1. Read session data (which nothing does today)
2. Extract structured information (decisions, files, context)
3. Write it in a format that the next tool can consume
4. Persist it for future reference

Once this pipeline exists, the same extraction logic can feed the digest system, the corrections system, and the knowledge promotion system. Migration is the forcing function for the entire memory architecture.

---

## Implementation Priority

**Build order optimized for immediate value:**

1. **Manual export/import** (Phases 1-3) -- gets the core working, even if triggered manually
2. **Handoff fix** (Phase 1) -- one-line fix, unblocks everything
3. **Context compression** (Phase 4) -- needed as soon as you use a smaller model
4. **Automatic triggers** (Phase 5) -- removes friction
5. **Bidirectional + history** (Phase 6) -- polish

The first usable version is Phases 1-3: you can manually trigger a migration, and it works. Everything after that is automation and polish.
