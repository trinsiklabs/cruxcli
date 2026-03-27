# BUILD_PLAN_008: Crux Session Hooks for CruxCLI

**Created:** 2026-03-25
**Status:** CONVERGED (all phases implemented; stale state side-effects addressed by BUILD_PLAN_012; auto-provisioning needs Rust migration update)
**Goal:** Wire CruxCLI's event bus to Crux MCP tools so session state is automatically maintained — files tracked, decisions captured, corrections detected, interactions logged. No LLM cooperation required.

**Constraint:** All hooks use the existing Bus event system — no polling, no timers.
**Constraint:** Hooks call Crux MCP tools via the existing MCP client (already configured).
**Constraint:** Graceful degradation — if Crux MCP is not configured, hooks are no-ops.
**Rule:** TDD. Tests before code.
**Rule:** Two consecutive clean audit passes = convergence.

## Document Alignment

- Crux MCP server: 43 tools including update_session, log_interaction, log_correction, restore_context
- CruxCLI bus system: `packages/cruxcli/src/bus/` — Bus.publish/subscribe with typed BusEvent definitions
- CruxCLI session processor: `packages/cruxcli/src/session/processor.ts` — tool-result event at line 180
- CruxCLI session events: Session.Event.Created, Updated, Deleted, Diff, Error
- CruxCLI file events: File.Edited
- CruxCLI MCP client: `packages/cruxcli/src/mcp/index.ts`

---

## Architecture

```
CruxCLI Plugin Init                  Provisioning
───────────────────                  ────────────

Plugin loads ─────────────────────►  Find crux repo on disk
                                     → Auto-init .crux/ if missing
                                     → Auto-write MCP config if missing
                                     → Now hooks have a server to talk to

CruxCLI Event Bus                    Crux MCP Server
─────────────────                    ───────────────

Session.Event.Created  ──────────►   restore_context()
                                     → loads previous state
                                     → offers session adoption

tool-result (edit/write) ────────►   update_session(add_file=path)
                                     → tracks files touched

tool-result (bash + git commit) ──►  update_session(add_decision=msg)
                                     → captures decisions

tool-result (any) ───────────────►   log_interaction(tool, input, output)
                                     → continuous interaction logging

user message ────────────────────►   log_interaction(role=user, content)
                                     → correction detection via patterns

Session.Event.Deleted ───────────►   auto_handoff() via write_handoff()
                                     → preserves state on exit
```

### Hook Registration Point

Create `packages/cruxcli/src/plugin/crux-hooks.ts` — a plugin that registers Bus subscribers on init. Plugin system already exists (`packages/cruxcli/src/plugin/index.ts`).

### MCP Tool Invocation

CruxCLI already has an MCP client. Hooks call Crux tools via `mcp.callTool("crux", "update_session", {...})` or equivalent.

---

## Phase 0: Auto-Provisioning

**Purpose:** On first run in any project, automatically set up Crux if the crux repo exists on the machine. Zero manual steps.

### Checklist — Phase 0

- [x] 0.1 On plugin init: detect if crux repo exists at well-known locations (`~/personal/crux`, `~/.crux-repo`, env var `CRUX_REPO`)
- [x] 0.2 If crux repo found but no `.crux/` in cwd: auto-run `init_project` (create `.crux/` directory structure)
- [x] 0.3 If crux repo found but no MCP config for "crux": auto-add crux MCP entry to `.cruxcli/cruxcli.jsonc` using the recipe engine format (type=local, merged array command)
- [x] 0.4 If crux repo found but no `.venv/`: log warning "Run setup.sh in crux repo to install dependencies"
- [x] 0.5 If no crux repo found: skip all Crux hooks silently (pure graceful degradation)
- [x] 0.6 Store discovered crux repo path in `~/.crux/crux-repo-path` so subsequent runs don't re-scan
- [x] 0.7 Tests for all provisioning paths (repo found, not found, venv missing, already configured)

---

## Phase 1: Plugin Scaffold + Session Lifecycle

**Purpose:** Create the Crux hooks plugin and wire session start/stop.

### Checklist — Phase 1

- [x] 1.1 Create `packages/cruxcli/src/plugin/crux-hooks.ts` with plugin scaffold
- [x] 1.2 On Session.Event.Created: call `restore_context()` via MCP, log result. If session_adoption.available, show adoption offer in TUI.
- [x] 1.3 On Session.Event.Deleted: call `write_handoff()` via MCP with auto-generated content
- [x] 1.4 Graceful degradation: if "crux" MCP server not configured (and Phase 0 couldn't provision), skip all hooks silently
- [x] 1.5 Register plugin in plugin index
- [x] 1.6 Tests for lifecycle hooks (created, deleted, no-crux-mcp)

---

## Phase 2: File + Decision Tracking

**Purpose:** Auto-capture files touched and decisions from tool results.

### Checklist — Phase 2

- [x] 2.1 Subscribe to tool-result events in processor.ts (or via Bus)
- [x] 2.2 On edit/write tool completion: call `update_session(add_file=path)` via MCP
- [x] 2.3 On bash tool with "git commit": extract commit message, call `update_session(add_decision=msg)`
- [x] 2.4 Commit message extraction: parse from output `[branch hash] message` format
- [x] 2.5 Tests for file tracking and decision capture

---

## Phase 3: Interaction Logging

**Purpose:** Log all tool interactions and user messages for continuous learning.

### Checklist — Phase 3

- [x] 3.1 On every tool-result: call `log_interaction(tool_name, tool_input, tool_output)` via MCP
- [x] 3.2 On user message (before LLM processing): call `log_interaction(role=user, content=prompt)` via MCP
- [x] 3.3 Rate limit: batch interactions, flush every N calls or M seconds (avoid MCP spam)
- [x] 3.4 Tests for interaction logging and batching

---

## Phase 4: Correction Detection

**Purpose:** Detect user corrections and log them for knowledge generation.

### Checklist — Phase 4

- [x] 4.1 On user message: check for correction patterns (same 10 regexes from crux_hooks.py)
- [x] 4.2 On correction detected: call `log_correction(original, corrected, category, mode)` via MCP
- [x] 4.3 Import correction patterns from Crux (or duplicate the 10 regexes in TypeScript)
- [x] 4.4 Tests for correction detection

---

## Phase 5: Integration + Verification

**Purpose:** End-to-end verification with real Crux MCP server.

### Checklist — Phase 5

- [x] 5.1 Start CruxCLI in a project with Crux MCP configured
- [x] 5.2 Verify: session start triggers restore_context
- [x] 5.3 Verify: file edits update .crux/sessions/state.json files_touched
- [x] 5.4 Verify: git commits appear in key_decisions
- [x] 5.5 Verify: session exit writes handoff
- [x] 5.6 Verify: corrections detected and logged to .crux/corrections/
- [x] 5.7 Verify: interactions logged to .crux/analytics/interactions/

---

## Key Implementation Details

### MCP Tool Call Pattern

```typescript
// In crux-hooks.ts
import { MCP } from "@/mcp"

async function callCrux(tool: string, args: Record<string, any>) {
  try {
    const result = await MCP.callTool("crux", tool, args)
    return result
  } catch {
    // Crux MCP not available — graceful degradation
    return null
  }
}
```

### Tool-Result Event Hook Point

In `processor.ts` around line 180-200, after `Session.updatePart()`:

```typescript
case "tool-result": {
  // ... existing code ...
  await Session.updatePart({ ... })

  // NEW: Crux hook — fire-and-forget, never blocks
  CruxHooks.onToolResult(match.state.input, value.output)

  delete toolcalls[value.toolCallId]
  break
}
```

### Correction Patterns (from crux_hooks.py)

```typescript
const CORRECTION_PATTERNS = [
  /\bno,?\s+(actually|not|that's wrong|incorrect)/i,
  /\binstead,?\s+(use|do|try|make)/i,
  /\bthat's not (right|correct|what I)/i,
  /\bdon't\s+(do|use|add|make|create)/i,
  /\bwrong\b.{0,20}\b(should|use|be|do)/i,
  /\bactually,?\s+(it|the|we|I|this|that)/i,
  /\bI (said|meant|want|need)\s+/i,
  /\bplease\s+(don't|stop|remove|undo|revert)/i,
  /\bnot\s+what\s+I\s+(asked|wanted|meant)/i,
  /\b(revert|undo|roll\s*back)\s+(that|this|the|it)/i,
]
```

---

## Convergence Criteria

- All checklist items complete
- **Zero manual setup**: install cruxcli, run in any project, session logging works if crux repo exists on the machine
- Auto-provisioning creates .crux/ and MCP config on first run
- Plugin registered and active when Crux MCP is configured
- Graceful degradation when Crux MCP is absent (no crux repo = no hooks, no errors)
- Session lifecycle (start/stop) triggers restore/handoff
- File edits and git commits auto-captured
- Interactions logged
- Corrections detected
- Two consecutive clean audit passes

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| MCP calls slow down tool execution | Latency | Fire-and-forget (async, no await on non-critical calls) |
| MCP server not running | Hooks error | Try/catch wrapper, silent degradation |
| Too many MCP calls | Performance | Batch interactions, rate limit |
| Correction detection false positives | Noise in corrections | Same patterns used in Claude Code (proven) |
| Plugin system changes in CruxCLI | Breaks hooks | Pin to current plugin API, add integration test |
