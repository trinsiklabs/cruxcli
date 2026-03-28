# BUILD_PLAN_012: Crux State Injection Resilience

**Created:** 2026-03-27
**Status:** CONVERGED
**Goal:** Make CruxCLI resilient to stale, missing, or mismatched Crux session state. Prevent wrong mode prompts, stale decisions, and bad temperature overrides from degrading agent performance.

**Context:** CruxCLI injects Crux session state (mode prompt, decisions, pending, temperature/topP) into every LLM system prompt. When state is stale or mismatched (e.g., Python mode in a TypeScript project), models perform worse — especially GPT-5.x which is sensitive to system prompt token pressure.

**Rule:** TDD. Tests before code.
**Rule:** Two consecutive clean passes = convergence.

## Document Alignment

- `packages/cruxcli/src/session/system.ts` — Crux state injection
- `packages/cruxcli/src/session/llm.ts` — temperature/topP overrides
- `packages/cruxcli/src/session/prompt.ts` — system prompt assembly
- `docs/MEMORY_ARCHITECTURE_REPORT.md` — documents the write-everything-use-nothing problem
- Crux `BUILD_PLAN_015_SESSION_STALENESS.md` — server-side fixes (complementary)

---

## Phase 1: State Validation Before Injection

**Purpose:** Validate Crux state before injecting it. Skip injection if state is stale, mismatched, or likely harmful.

### Checklist — Phase 1

- [x] 1.1 Add `isStateStale(state)` check in `system.ts`: if `updated_at` is >24h old, treat state as stale
- [x] 1.2 When state is stale: skip mode prompt injection, skip decision injection, skip pending tasks. Only inject session context if `working_on` is set.
- [x] 1.3 Add `detectProjectType(dir)` in `system.ts`: check for `tsconfig.json` (TS), `package.json` (JS/TS), `pyproject.toml` (Python), `mix.exs` (Elixir), `Cargo.toml` (Rust), `go.mod` (Go)
- [x] 1.4 When detected project type doesn't match active mode (e.g., TS project + `build-py` mode): skip mode prompt, log warning
- [x] 1.5 Tests for stale detection, project type detection, mismatch handling

---

## Phase 2: Temperature/topP Safety

**Purpose:** Don't let stale mode overrides degrade model performance.

### Checklist — Phase 2

- [x] 2.1 In `llm.ts`: only apply Crux temperature/topP overrides if state is fresh AND mode matches project type
- [x] 2.2 If state is stale or mismatched: use model defaults (don't override)
- [x] 2.3 Log when Crux overrides are skipped (for debugging)
- [x] 2.4 Tests for temperature fallback behavior

---

## Phase 3: Decision and Context Filtering

**Purpose:** Don't inject irrelevant decisions or stale pending tasks.

### Checklist — Phase 3

- [x] 3.1 In `cruxSessionContext()`: filter `key_decisions` to only recent ones (if timestamps available from Crux BUILD_PLAN_015)
- [x] 3.2 If decisions have no timestamps (legacy format): only inject last 3 instead of last 5
- [x] 3.3 Cap total injected context to 500 tokens (~200 words) — prevent context bloat
- [x] 3.4 If `pending` tasks exist but `working_on` is empty: skip pending (likely stale)
- [x] 3.5 Tests for filtering and token cap

---

## Phase 4: Graceful Degradation Flag

**Purpose:** Allow users to disable Crux injection entirely if it causes problems.

### Checklist — Phase 4

- [x] 4.1 Add `CRUXCLI_DISABLE_CRUX_INJECTION` flag in `flag.ts`
- [x] 4.2 When set: skip all Crux state reading, mode injection, temperature overrides
- [x] 4.3 Document in `docs/CONFIGURATION.md`
- [x] 4.4 Tests for flag behavior

---

## Post-Execution Convergence Checklist

- [x] Documentation convergence: update CONFIGURATION.md with new flag
- [x] Inbox check: check_inbox() for messages from other sessions

---

## Test Commands

```bash
cd packages/cruxcli && bun test --timeout 30000
```

## Convergence Criteria

- Stale state (>24h) not injected into system prompt
- Project type mismatch detected and mode prompt skipped
- Temperature/topP defaults used when state is stale/mismatched
- Decision injection capped at 500 tokens
- `CRUXCLI_DISABLE_CRUX_INJECTION` flag works
- Two consecutive clean audit passes

## Convergence Record

- Implemented in:
  - `packages/cruxcli/src/session/system.ts`
  - `packages/cruxcli/src/session/llm.ts`
  - `packages/cruxcli/src/flag/flag.ts`
  - `packages/cruxcli/test/session/system.test.ts`
  - `docs/CONFIGURATION.md`
- Test pass #1: `cd packages/cruxcli && bun test test/session/system.test.ts`
- Test pass #2: `cd packages/cruxcli && bun test test/session/system.test.ts`
- Additional spot-check: `cd packages/cruxcli && bun test test/session/llm.test.ts -t hasToolCalls`
