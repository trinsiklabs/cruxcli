# CruxCLI Database Schema

**Last Updated:** 2026-03-24

---

## Overview

CruxCLI uses two storage systems:
1. **SQLite** (primary) — Structured data via Drizzle ORM with `bun:sqlite`. Located at `~/.local/share/cruxcli/cruxcli.db`.
2. **JSON file storage** (legacy/supplementary) — File-based key-value store under `~/.local/share/cruxcli/storage/`. Used for checkpoints and data that predates the SQLite migration.

Database configuration: WAL journal mode, `synchronous = NORMAL`, `busy_timeout = 5000`, `cache_size = -64000`, foreign keys enabled.

Migrations are embedded in the compiled binary at build time (`CRUXCLI_MIGRATIONS`). In development, they are read from `packages/opencode/migration/`. Auto-applied on startup.

---

## SQLite Tables

### `project`

Project metadata. One row per tracked project directory.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | text | PRIMARY KEY | Project ID (git root commit hash for git projects) |
| `worktree` | text | NOT NULL | Absolute path to project worktree |
| `vcs` | text | nullable | Version control type (e.g., "git") |
| `name` | text | nullable | Display name |
| `icon_url` | text | nullable | Project icon URL |
| `icon_color` | text | nullable | Project icon color |
| `commands` | text | nullable | Custom project commands (added in migration 20260211) |
| `time_created` | integer | NOT NULL | Creation timestamp (epoch ms) |
| `time_updated` | integer | NOT NULL | Last update timestamp |
| `time_initialized` | integer | nullable | Initialization timestamp |
| `sandboxes` | text | NOT NULL | Sandbox configuration (JSON) |

### `session`

Sessions are the primary unit of user interaction. Each session belongs to a project and optionally a workspace.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | text | PRIMARY KEY | Session ID |
| `project_id` | text | NOT NULL, FK -> project.id (CASCADE) | Owning project |
| `parent_id` | text | nullable | Parent session (for subtasks) |
| `workspace_id` | text | nullable | Associated workspace (added in migration 20260227) |
| `slug` | text | NOT NULL | URL-friendly slug |
| `directory` | text | NOT NULL | Working directory |
| `title` | text | NOT NULL | Session title |
| `version` | text | NOT NULL | Schema version |
| `share_url` | text | nullable | Public share URL |
| `summary_additions` | integer | nullable | Lines added |
| `summary_deletions` | integer | nullable | Lines deleted |
| `summary_files` | integer | nullable | Files changed |
| `summary_diffs` | text | nullable | Diff summary data |
| `revert` | text | nullable | Revert information |
| `permission` | text | nullable | Permission overrides |
| `time_created` | integer | NOT NULL | Creation timestamp |
| `time_updated` | integer | NOT NULL | Last update timestamp |
| `time_compacting` | integer | nullable | Last compaction timestamp |
| `time_archived` | integer | nullable | Archive timestamp |

**Indexes:** `session_project_idx` (project_id), `session_parent_idx` (parent_id), `session_workspace_idx` (workspace_id)

### `message`

Messages within a session (user or assistant turns).

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | text | PRIMARY KEY | Message ID |
| `session_id` | text | NOT NULL, FK -> session.id (CASCADE) | Owning session |
| `time_created` | integer | NOT NULL | Creation timestamp |
| `time_updated` | integer | NOT NULL | Last update timestamp |
| `data` | text | NOT NULL | Message data (JSON: role, token counts, cost, model info) |

**Indexes:** `message_session_idx` (session_id)

### `part`

Individual parts of a message (text, tool call, reasoning, compaction, file, subtask).

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | text | PRIMARY KEY | Part ID |
| `message_id` | text | NOT NULL, FK -> message.id (CASCADE) | Owning message |
| `session_id` | text | NOT NULL | Session ID (denormalized for query efficiency) |
| `time_created` | integer | NOT NULL | Creation timestamp |
| `time_updated` | integer | NOT NULL | Last update timestamp |
| `data` | text | NOT NULL | Part data (JSON: type-specific content) |

**Indexes:** `part_message_idx` (message_id), `part_session_idx` (session_id)

### `todo`

TODO items attached to sessions.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `session_id` | text | NOT NULL, FK -> session.id (CASCADE) | Owning session |
| `content` | text | NOT NULL | TODO text |
| `status` | text | NOT NULL | Status (e.g., pending, done) |
| `priority` | text | NOT NULL | Priority level |
| `position` | integer | NOT NULL | Ordering position |
| `time_created` | integer | NOT NULL | Creation timestamp |
| `time_updated` | integer | NOT NULL | Last update timestamp |

**Primary Key:** (`session_id`, `position`) composite
**Indexes:** `todo_session_idx` (session_id)

### `permission`

Per-project permission overrides.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `project_id` | text | PRIMARY KEY, FK -> project.id (CASCADE) | Project ID |
| `time_created` | integer | NOT NULL | Creation timestamp |
| `time_updated` | integer | NOT NULL | Last update timestamp |
| `data` | text | NOT NULL | Permission rules (JSON) |

### `session_share`

Shared session links.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `session_id` | text | PRIMARY KEY, FK -> session.id (CASCADE) | Session being shared |
| `id` | text | NOT NULL | Share ID |
| `secret` | text | NOT NULL | Share secret |
| `url` | text | NOT NULL | Public share URL |
| `time_created` | integer | NOT NULL | Creation timestamp |
| `time_updated` | integer | NOT NULL | Last update timestamp |

### `workspace`

Workspace/worktree tracking for isolated development environments.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | text | PRIMARY KEY | Workspace ID |
| `branch` | text | nullable | Git branch name |
| `project_id` | text | NOT NULL, FK -> project.id (CASCADE) | Owning project |
| `type` | text | NOT NULL | Workspace type (added in migration 20260303) |
| `name` | text | nullable | Display name (added in migration 20260303) |
| `directory` | text | nullable | Workspace directory path (added in migration 20260303) |
| `extra` | text | nullable | Additional metadata (JSON, added in migration 20260303) |

### `control_account`

Crux platform account credentials.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `email` | text | NOT NULL | Account email |
| `url` | text | NOT NULL | Platform URL |
| `access_token` | text | NOT NULL | OAuth access token |
| `refresh_token` | text | NOT NULL | OAuth refresh token |
| `token_expiry` | integer | nullable | Token expiration timestamp |
| `active` | integer | NOT NULL | Whether this account is active |
| `time_created` | integer | NOT NULL | Creation timestamp |
| `time_updated` | integer | NOT NULL | Last update timestamp |

**Primary Key:** (`email`, `url`) composite

---

## Entity Relationships

```
project (1) ──< session (many)
project (1) ──< workspace (many)
project (1) ──< permission (1)
session (1) ──< message (many)
session (1) ──< todo (many)
session (1) ──< session_share (1)
session (1) ──< session (many) [parent_id self-reference]
message (1) ──< part (many)
workspace (1) ──< session (many) [workspace_id]
```

---

## Migration History

| Timestamp | Slug | Changes |
|-----------|------|---------|
| 20260127222353 | `familiar_lady_ursula` | Initial schema: project, message, part, permission, session, todo, session_share tables with indexes |
| 20260211171708 | `add_project_commands` | Added `commands` column to project table |
| 20260213144116 | `wakeful_the_professor` | Added `control_account` table |
| 20260225215848 | `workspace` | Added `workspace` table (id, branch, project_id, config) |
| 20260227213759 | `add_session_workspace_id` | Added `workspace_id` column and index to session table |
| 20260303231226 | `add_workspace_fields` | Added `type`, `name`, `directory`, `extra` to workspace; dropped `config` |

---

## JSON Storage Layer

File-based key-value store at `~/.local/share/cruxcli/storage/`. Keys map to file paths (e.g., `["checkpoint", projectId, name]` -> `storage/checkpoint/<projectId>/<name>.json`).

Operations: `read`, `write`, `update`, `remove`, `list`. All operations use file locking (`Lock.read`/`Lock.write`). Errors for missing keys throw `NotFoundError`.

The JSON storage layer includes its own migration system (separate from SQLite migrations) that handles legacy data layout changes. Two migrations exist:
1. Migrates project/session/message/part data from the old directory structure to the new layout.
2. Extracts session diff summaries into separate files and normalizes summary data.

On first SQLite database creation, `JsonMigration.run()` bulk-migrates all JSON storage data into SQLite tables.
