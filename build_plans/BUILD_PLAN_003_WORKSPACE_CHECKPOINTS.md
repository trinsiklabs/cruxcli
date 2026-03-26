# BUILD_PLAN_003: Workspace Checkpoints

**Created:** 2026-03-23
**Status:** NOT STARTED
**Goal:** Add automatic and manual workspace checkpointing so users can snapshot and restore file state before risky operations. Builds on the existing `Snapshot` system.

**Constraint:** Reuse existing `Snapshot.track()` / `Snapshot.restore()` — no new git plumbing.
**Constraint:** Zero overhead when checkpoints are not used.
**Rule:** TDD. Tests before code.
**Rule:** 100% coverage enforced.
**Rule:** Two consecutive clean passes = convergence.

## Document Alignment

- `AGENTS.md` — coding style, naming conventions, testing rules
- `ROADMAP.md` — defines this as competitive gap #2, "low effort"

---

## Architecture

The existing `Snapshot` module (`src/snapshot/index.ts`) already:
- Creates git tree snapshots via `track()` → returns hash
- Restores files via `restore(snapshot)`
- Generates diffs via `diff(hash)` and `patch(hash)`
- Stores snapshots in `~/.local/share/cruxcli/snapshot/{projectID}/`
- Auto-cleans via `git gc --prune=7.days`

Checkpoints add a **named layer** on top:

```
Snapshot (low-level)          Checkpoint (user-facing)
────────────────────          ──────────────────────────
track() → hash                create(label?) → {id, hash, label, time}
restore(hash)                 restore(id)
diff(hash)                    list() → Checkpoint[]
                              auto-create before destructive tools
```

### Storage

Checkpoint metadata stored via the existing `Storage` module:
```typescript
Storage.write(["checkpoint", projectID], checkpoints)
// checkpoints: Array<{id, hash, label, time, sessionID?}>
```

---

## Phase 1: Checkpoint Module

**Purpose:** Create the checkpoint abstraction on top of Snapshot.

### Checklist — Phase 1

- [x] 1.1 Create `src/checkpoint/index.ts` with `Checkpoint` namespace
- [x] 1.2 `Checkpoint.create(label?)` → creates snapshot via `Snapshot.track()`, stores metadata with id/hash/label/timestamp
- [x] 1.3 `Checkpoint.list()` → returns all checkpoints for current project, sorted by time desc
- [x] 1.4 `Checkpoint.restore(id)` → calls `Snapshot.restore()` with stored hash
- [x] 1.5 `Checkpoint.remove(id)` → deletes checkpoint metadata (snapshot data auto-gc'd)
- [x] 1.6 `Checkpoint.diff(id)` → returns diff between checkpoint and current state
- [x] 1.7 Max 50 checkpoints per project (oldest auto-pruned on create)
- [x] 1.8 Tests for create, list, restore, remove, diff, auto-prune
- [x] 1.9 Tests pass, coverage ≥ 100%

---

## Phase 2: CLI Command

**Purpose:** Expose checkpoints via `cruxcli checkpoint` subcommand.

### Checklist — Phase 2

- [x] 2.1 Create `src/cli/cmd/checkpoint.ts` with subcommands: create, list, restore, remove
- [x] 2.2 `cruxcli checkpoint create [label]` — creates checkpoint, prints id and file count
- [x] 2.3 `cruxcli checkpoint list` — table of id, label, time, file count
- [x] 2.4 `cruxcli checkpoint restore <id>` — restores and prints diff summary
- [x] 2.5 `cruxcli checkpoint remove <id>` — deletes checkpoint
- [x] 2.6 `cruxcli checkpoint diff <id>` — shows what changed since checkpoint
- [x] 2.7 Register command in `src/cli/cmd/index.ts`
- [x] 2.8 Tests for CLI argument parsing and output
- [x] 2.9 Tests pass, coverage ≥ 100%

---

## Phase 3: Auto-Checkpoint on Destructive Tools

**Purpose:** Automatically create checkpoints before tools that modify files.

### Checklist — Phase 3

- [x] 3.1 Identify destructive tools: Edit, Write, Bash (when modifying files), ApplyPatch
- [x] 3.2 Add pre-execution hook in `Tool.define()` that calls `Checkpoint.create("auto")` before destructive tool calls
- [x] 3.3 Deduplicate: only create one auto-checkpoint per message (not per tool call)
- [x] 3.4 Auto-checkpoints labeled "auto-{toolName}-{timestamp}" for identification
- [x] 3.5 Auto-checkpoints count toward the 50-max limit but are pruned first (before manual ones)
- [x] 3.6 Config flag `CRUXCLI_AUTO_CHECKPOINT` (default: true) to disable
- [x] 3.7 Tests for auto-checkpoint creation, deduplication, pruning priority
- [x] 3.8 Tests pass, coverage ≥ 100%

---

## Phase 4: Build + Verify

**Purpose:** End-to-end verification.

### Checklist — Phase 4

- [x] 4.1 Binary compiles with checkpoint feature
- [x] 4.2 `cruxcli checkpoint create "before refactor"` works in a real repo
- [x] 4.3 Make file changes, `cruxcli checkpoint restore <id>` reverts them
- [x] 4.4 `cruxcli checkpoint list` shows correct entries
- [x] 4.5 Auto-checkpoint fires before Edit tool in a session
- [x] 4.6 `cruxcli checkpoint diff <id>` shows accurate changes
- [x] 4.7 Full test suite passes (existing + new)
- [x] 4.8 No performance regression (checkpoint create <100ms)

---

## Test Commands

```bash
cd packages/cruxcli && bun test --timeout 30000
```

## Convergence Criteria

- All checklist items complete
- All tests pass
- Coverage ≥ 100% on new code
- Two consecutive clean audit passes
- Binary compiles and checkpoint commands work end-to-end

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Snapshot.track() slow on large repos | Auto-checkpoint adds latency | Measure; skip auto-checkpoint if >100ms |
| 50-checkpoint limit too low for long sessions | User loses old checkpoints | Configurable limit; manual checkpoints survive longer than auto |
| Restoring checkpoint in dirty working tree | Conflicts | Warn user; require --force or stash first |

## Definition of Done

1. `cruxcli checkpoint create/list/restore/remove/diff` all work
2. Auto-checkpoint fires before destructive tool calls
3. Checkpoint data persists across sessions
4. <100ms overhead for auto-checkpoint
5. 100% test coverage on new code
6. Two consecutive clean audit passes
