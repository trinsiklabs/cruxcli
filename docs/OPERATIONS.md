# CruxCLI Operations

**Last Updated:** 2026-03-24

---

## Snapshot Cleanup

**System:** Scheduler (`scheduler/index.ts`)
**Scope:** Per-project (instance-scoped)

The snapshot system maintains a separate `.git` directory (under `~/.local/share/cruxcli/`) that tracks file state for checkpoint/restore. Without periodic cleanup, git objects accumulate indefinitely.

**Schedule:** Runs on a periodic interval via the built-in scheduler.
**Operation:** `git gc --prune=7.days` on the snapshot git directory.
**Effect:** Removes unreachable git objects older than 7 days. Checkpoints referencing pruned tree hashes become unrestorable.
**Lifecycle:** Registered as an instance-scoped task — cleanup stops when the project instance is disposed.

---

## Database Migrations

**System:** Drizzle ORM with `bun:sqlite`
**Location:** `packages/opencode/migration/<timestamp>_<slug>/migration.sql`

Migrations are **embedded in the compiled binary** at build time. The build script reads all migration SQL files and bundles them as `CRUXCLI_MIGRATIONS`. In development, migrations are read from the filesystem.

**Execution:** Auto-applied on startup when `Database.Client()` is first accessed. Drizzle's migrator handles tracking which migrations have been applied.
**Rollback:** No automatic rollback. Migrations are forward-only. To undo a migration, a new migration must be created.
**Development:** New migrations are generated via `drizzle-kit`.

### JSON-to-SQLite Migration

On first database creation, if legacy JSON storage exists at `~/.local/share/cruxcli/storage/`, the `JsonMigration.run()` function bulk-migrates all data into SQLite tables. This is a one-time operation that runs inside a single transaction with optimized PRAGMA settings (`synchronous = OFF`, `cache_size = 10000`, `temp_store = MEMORY`).

Migrated entities: projects, sessions, messages, parts, todos, permissions, session shares.
Orphaned records (e.g., sessions referencing non-existent projects) are skipped with warnings.

---

## Checkpoint Storage and Limits

**System:** Checkpoint (`checkpoint/index.ts`) + Snapshot (`snapshot/index.ts`)
**Storage:** JSON storage keyed by `["checkpoint", projectId]`

**Maximum checkpoints:** 50 per project.
**Auto-pruning:** When the limit is reached, the oldest auto-created checkpoints are pruned first. User-created (named) checkpoints have priority.
**Checkpoint data:** Each entry stores a git tree hash, a name, a timestamp, and whether it was auto-created.

**Auto-checkpoint triggers:** Destructive tool calls — `edit`, `write`, `multiedit`, `bash`, `apply_patch`. Before execution, the tool wrapper calls `Snapshot.track()` to capture a tree hash, then stores it as a checkpoint.

**Restore operation:** `Snapshot.restore(hash)` runs `git read-tree` + `git checkout-index` to revert the worktree to the captured state.

**Disable:** Set `CRUXCLI_DISABLE_AUTO_CHECKPOINT=1` or configure `snapshot: false` in `cruxcli.json`.

---

## Scheduler

The built-in scheduler (`scheduler/index.ts`) runs background tasks at fixed intervals. Tasks are scoped:

- **Instance-scoped:** Tied to a project instance. Cleaned up when the instance is disposed. Used for snapshot cleanup.
- **Global-scoped:** Shared across all instances. Used for cross-cutting background work.

The scheduler is a simple `setInterval` wrapper — no persistence, no queue, no retry. Tasks that fail are logged but do not block other tasks.

---

## Configuration Precedence

Configuration is loaded from multiple sources with the following precedence (highest to lowest):

1. **Managed config** — System-level, admin-controlled (`/Library/Application Support/cruxcli` on macOS, `/etc/cruxcli` on Linux)
2. **Project config** — `.cruxcli/config.json{,c}` in the project directory
3. **Global config** — `~/.config/cruxcli/cruxcli.json{,c}`
4. **Remote config** — `.well-known/cruxcli` (organization defaults)

Changes to configuration files are picked up on next session start — no hot-reload.

---

## Data Directories

| Path | Content |
|------|---------|
| `~/.local/share/cruxcli/cruxcli.db` | SQLite database (WAL mode) |
| `~/.local/share/cruxcli/auth.json` | Provider credentials |
| `~/.local/share/cruxcli/storage/` | Legacy JSON storage + checkpoint data |
| `~/.config/cruxcli/` | Global configuration |
| `.cruxcli/` | Project-level configuration, tools, skills |
