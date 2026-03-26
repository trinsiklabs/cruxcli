# CruxCLI Architecture

## System Overview

CruxCLI is an AI-powered development tool that runs as a CLI with a client/server architecture. The CLI process starts a local HTTP server (Hono-based, default port 4096) that manages project instances, sessions, and LLM interactions. Frontends (TUI, web app, desktop app) communicate with this server over HTTP and SSE.

The core loop: a user sends a message, the system constructs a prompt with system instructions and context, streams a response from an LLM provider, executes any tool calls the model requests, and repeats until the model finishes.

### Entry Point

`packages/cruxcli/src/index.ts` -- yargs-based CLI that registers all commands and runs a one-time SQLite migration on first launch. The process sets `CRUXCLI=1` and `AGENT=1` environment variables.

### Key Commands

| Command | Purpose |
|---------|---------|
| `run` | Interactive TUI session (default) |
| `serve` | Headless HTTP server mode |
| `acp` | Autonomous code pipeline |
| `agent` | Run agent programmatically |
| `mcp` | MCP server management |
| `checkpoint` | Manual snapshot management |
| `auth` | Provider authentication |
| `web` | Launch web UI |

---

## Package Structure

Bun monorepo managed with Turbo. Workspaces live under `packages/*`, `packages/console/*`, and `packages/sdk/js`.

### Core Packages

| Package | Name | Role |
|---------|------|------|
| `packages/cruxcli` | `cruxcli` | Core CLI, server, session engine, provider integration, tool system. The main binary. |
| `packages/app` | `@cruxcli/app` | SolidJS web frontend (connects to server over HTTP/SSE) |
| `packages/ui` | `@cruxcli/ui` | Shared UI component library (SolidJS) |
| `packages/desktop` | `@cruxcli/desktop` | Tauri desktop wrapper |
| `packages/desktop-electron` | `@cruxcli/desktop-electron` | Electron desktop wrapper |
| `packages/web` | `@cruxcli/web` | Web deployment package |
| `packages/storybook` | `@cruxcli/storybook` | Component storybook |

### Platform Packages

| Package | Name | Role |
|---------|------|------|
| `packages/plugin` | `@cruxcli/plugin` | Plugin API types and interfaces |
| `packages/sdk` | `@cruxcli/sdk` | TypeScript SDK for the CruxCLI server API (auto-generated from OpenAPI) |
| `packages/util` | `@cruxcli/util` | Shared utilities (error types, slug generation) |
| `packages/script` | `@cruxcli/script` | Build and release scripts |

### Infrastructure Packages

| Package | Name | Role |
|---------|------|------|
| `packages/function` | `@cruxcli/function` | Serverless functions |
| `packages/enterprise` | `@cruxcli/enterprise` | Enterprise features |
| `packages/slack` | `@cruxcli/slack` | Slack integration |
| `packages/extensions` | -- | IDE extensions (Zed) |
| `packages/containers` | -- | Container definitions |

### Console Packages (`packages/console/*`)

| Package | Role |
|---------|------|
| `console/app` | Console web application |
| `console/core` | Console business logic |
| `console/function` | Console serverless functions |
| `console/mail` | Email templates |
| `console/resource` | SST infrastructure resources |

---

## Core Subsystems

All core subsystems live under `packages/cruxcli/src/`. Most are organized as TypeScript namespaces with an `Instance.state()` pattern that scopes state per project directory.

### Instance (`project/instance.ts`)

The `Instance` module provides async context propagation per project directory. Every subsystem that holds per-project state calls `Instance.state()`, which returns a state accessor scoped to the current project. When an instance is disposed, all registered cleanup callbacks fire. The instance exposes `directory` (working directory), `worktree` (git sandbox root), and `project` (project metadata).

### Session (`session/`)

Sessions are the primary unit of user interaction. Each session belongs to a project, has a message history, and tracks cumulative token usage and cost.

Key files:
- `session/index.ts` -- CRUD operations, message management, stored in SQLite via `SessionTable` and `MessageTable`
- `session/prompt.ts` -- `SessionPrompt.prompt()` accepts user input, creates the user message, then enters the main loop; `SessionPrompt.loop()` drives the agentic step loop
- `session/llm.ts` -- `LLM.stream()` wraps the Vercel AI SDK `streamText` call with system prompt assembly, provider transforms, and plugin hooks
- `session/processor.ts` -- `SessionProcessor` consumes the LLM stream, routes events (text, reasoning, tool calls) into message parts, handles tool execution, compaction triggers, and doom-loop detection
- `session/compaction.ts` -- Context window management: detects overflow, prunes old tool call outputs, triggers summarization via a secondary LLM call
- `session/system.ts` -- Selects the system prompt based on model family (Anthropic, OpenAI/beast, Gemini, Trinity, Qwen). Reads Crux mode state from `.crux/sessions/state.json` when present
- `session/token-budget.ts` -- Token budget tracking with configurable warning (75%) and hard limit (90%) thresholds
- `session/message-v2.ts` -- Message and part schema definitions (text, tool, reasoning, compaction, subtask, file parts)
- `session/session.sql` -- Drizzle schema for `SessionTable`, `MessageTable`, `PartTable`, `PermissionTable`

### Provider (`provider/`)

Multi-provider LLM integration using the Vercel AI SDK.

- `provider/provider.ts` -- Model resolution, SDK instantiation. Bundles 20+ provider SDKs (Anthropic, OpenAI, Google, Azure, Bedrock, Vertex, OpenRouter, xAI, Mistral, Groq, DeepInfra, Cerebras, Cohere, Gateway, TogetherAI, Perplexity, Vercel, GitLab, GitHub Copilot). Custom loaders handle Bedrock credential chains and Vertex auth.
- `provider/models.ts` -- Fetches model definitions from `models.dev` at runtime; `models-snapshot.ts` is a build-time snapshot for offline fallback
- `provider/transform.ts` -- Provider-specific transforms for output tokens, system prompts, and model options
- `provider/auth.ts` -- Provider authentication resolution
- `provider/error.ts` -- Structured error types for provider failures

### Tool System (`tool/`)

Tools are defined via `Tool.define(id, init)` which returns `{ description, parameters, execute }`. The execute wrapper validates arguments via Zod, auto-creates checkpoints before destructive operations, and supports output truncation.

Built-in tools:
- **File ops**: `read`, `write`, `edit`, `multiedit`, `apply_patch`, `glob`, `grep`, `ls`
- **Execution**: `bash` (shell commands with timeout)
- **Search**: `codesearch` (LSP-based), `websearch`, `webfetch`
- **Agent**: `task` (spawn sub-agent sessions), `batch` (parallel tool calls), `skill` (load skill files)
- **Planning**: `plan` (plan mode exit), `question` (ask user), `todo` (read/write TODO lists)
- **LSP**: `lsp` (diagnostics, symbols)

`tool/registry.ts` -- Aggregates built-in tools, custom tools loaded from `.cruxcli/tool/*.{js,ts}` or `tools/*.{js,ts}`, and plugin-contributed tools.

`tool/truncation.ts` -- Handles output size limits to prevent context overflow.

### Agent (`agent/agent.ts`)

Agents define behavior profiles with a name, mode, permission ruleset, optional model override, and optional custom prompt. Built-in agents:

| Agent | Mode | Description |
|-------|------|-------------|
| `build` | primary | Default agent, full tool access |
| `plan` | primary | Read-only planning mode, disallows edits |

Agents are extensible via config and plugins. Each agent carries a `PermissionNext.Ruleset` controlling tool access (allow/deny/ask per tool per file pattern).

### Permission (`permission/next.ts`)

Rule-based permission system. Each rule has a `permission` (tool name), `pattern` (glob for file paths or `*`), and `action` (allow/deny/ask). Rules merge with precedence: agent defaults < config < session overrides. Default rules block `.env` file reads, require approval for external directories, and deny question/plan tools unless the agent explicitly allows them.

### Config (`config/config.ts`)

JSONC configuration loaded with a multi-layer precedence chain:
1. Remote `.well-known/cruxcli` (org defaults)
2. Global config (`~/.config/cruxcli/cruxcli.json{,c}`)
3. Project config (`.cruxcli/config.json{,c}`)
4. Managed config (system-level, admin-controlled: `/Library/Application Support/cruxcli` on macOS, `/etc/cruxcli` on Linux)

Supports model overrides, permission rules, plugin lists, instruction files, MCP server definitions, LSP toggle, compaction settings, and snapshot toggle.

### Checkpoint (`checkpoint/index.ts`)

Named restore points built on top of the snapshot system. Stores up to 50 entries (auto-checkpoints pruned first) in JSON storage keyed by project ID. Each checkpoint records a git tree hash. Destructive tools (`edit`, `write`, `multiedit`, `bash`, `apply_patch`) auto-create a checkpoint before execution unless `CRUXCLI_DISABLE_AUTO_CHECKPOINT` is set.

### Snapshot (`snapshot/index.ts`)

Git-based file tracking for undo/restore. Maintains a separate `.git` directory (under the CruxCLI data path, not the project's own `.git`) that tracks the project worktree. Core operations:
- `track()` -- `git add` + `git write-tree` to capture current state as a tree hash
- `restore(hash)` -- `git read-tree` + `git checkout-index` to revert files
- `diff(hash)` -- Shows changes since a given tree hash
- `cleanup()` -- Periodic `git gc --prune=7.days` via the scheduler

### Skill (`skill/skill.ts`)

Skills are markdown files (`SKILL.md`) with frontmatter (name, description) discovered from multiple directories: `.cruxcli/skills/`, `.claude/skills/`, `.agents/skills/`, and global equivalents. They are loaded as context for the LLM via the `skill` tool.

### Plugin (`plugin/index.ts`)

Plugin system supporting npm packages and internal plugins (Codex auth, Copilot auth, GitLab auth). Plugins receive a client, project info, and directory context, and can contribute tools and lifecycle hooks (`tool.execute.before`, `tool.execute.after`, etc.).

### Scheduler (`scheduler/index.ts`)

Simple interval-based task runner. Tasks can be scoped to `instance` (per-project, cleaned up on dispose) or `global` (shared). Used for periodic snapshot cleanup and other background work.

### Bus (`bus/index.ts`)

In-process event bus scoped per Instance. `Bus.publish(event, properties)` dispatches to type-specific and wildcard subscribers. Events also propagate to `GlobalBus` for cross-instance listeners (used by the SSE streaming to frontends).

---

## Data Flow

### User Message to Response

```
User Input
    |
    v
SessionPrompt.prompt(input)
    |-- Create user message (MessageV2.User) in SQLite
    |-- Resolve model from user selection or config
    |
    v
SessionPrompt.loop(sessionID)
    |-- Load message history
    |-- Resolve model, agent, check for pending subtasks
    |
    v
SessionProcessor.create(...)
    |-- process(streamInput)
    |
    v
LLM.stream(input)
    |-- Assemble system prompt (provider-specific base + Crux mode + instructions + user system)
    |-- Load config, get language model from Provider
    |-- Apply provider transforms (output tokens, headers, metadata)
    |-- Call Vercel AI SDK streamText() with tools, system, messages
    |
    v
Stream Processing (SessionProcessor)
    |-- Text chunks -> accumulate into TextPart
    |-- Reasoning chunks -> ReasoningPart
    |-- Tool calls -> ToolPart (state: pending -> running -> complete/error)
    |       |
    |       v
    |   Tool Execution
    |       |-- Permission check (PermissionNext.ask)
    |       |-- Auto-checkpoint for destructive tools
    |       |-- Execute tool, store result
    |       |-- Doom loop detection (3 consecutive identical failures)
    |
    v
Loop Decision
    |-- If finish reason is "tool-calls" -> continue loop (next LLM call with tool results)
    |-- If context overflow detected -> trigger compaction, then continue
    |-- If model signals completion -> break loop
    |
    v
Response Complete
    |-- Summarize if first step (async title generation)
    |-- Publish session events via Bus
    |-- Return final MessageV2.WithParts
```

### Context Compaction

When cumulative tokens approach the model's context limit (minus a 20K buffer), `SessionCompaction.isOverflow()` triggers. The compaction flow:
1. Prune old tool call outputs (keep last 40K tokens worth of tool results)
2. Summarize conversation history using a secondary LLM call
3. Replace pruned messages with a `CompactionPart` containing the summary
4. Continue the session loop with reduced context

---

## Storage

### SQLite (Primary Store)

Located at `~/.local/share/cruxcli/cruxcli.db` (via `Global.Path.data`). Managed by Drizzle ORM with `bun:sqlite`.

Database configuration:
- WAL journal mode
- `PRAGMA synchronous = NORMAL`
- `PRAGMA busy_timeout = 5000`

Schema files follow the `*.sql.ts` convention. Key tables:
- `SessionTable` -- Sessions with project/workspace association, title, version, summary stats
- `MessageTable` -- Messages (user/assistant) with token counts, cost, model info
- `PartTable` -- Message parts (text, tool, reasoning, compaction, file, subtask)
- `ProjectTable` -- Project metadata (VCS type, worktree path)
- `WorkspaceTable` -- Workspace/worktree tracking
- `ControlAccountTable` -- Crux platform account credentials
- `PermissionTable` -- Per-session permission overrides

Migrations live in `packages/cruxcli/migration/<timestamp>_<slug>/migration.sql`. On first run, a JSON-to-SQLite migration (`storage/json-migration.ts`) converts legacy JSON storage.

### JSON Storage (`storage/storage.ts`)

File-based key-value store under `Global.Path.data`. Used for checkpoints and other data that predates the SQLite migration. Keys map to file paths.

### Auth Storage

Provider credentials stored in `~/.local/share/cruxcli/auth.json`. Supports three auth types: OAuth (with refresh flow), API key, and well-known token.

---

## Integration Points

### MCP (Model Context Protocol) (`mcp/index.ts`)

Full MCP client implementation supporting three transport types:
- **stdio** -- Spawns a subprocess
- **SSE** -- Server-Sent Events connection
- **StreamableHTTP** -- HTTP streaming

MCP servers are configured in `cruxcli.json` or `.mcp.json`. The client discovers tools from connected servers and exposes them to the LLM alongside built-in tools. Supports OAuth authentication with browser-based authorization flow.

### LSP (Language Server Protocol) (`lsp/index.ts`)

Built-in LSP client that spawns language servers for diagnostics and symbol lookup. Used by the `codesearch` and `lsp` tools. Servers are auto-detected per language (e.g., pyright, ty for Python). Can be disabled via config (`lsp: false`). Experimental server support gated behind `CRUXCLI_EXPERIMENTAL_LSP_TY`.

### Crux Platform

Integration with the Crux AI operating system via:
- `.crux/sessions/state.json` -- Session state (active mode, working context, pending items) injected into system prompts
- `~/.crux/modes/<mode>.md` -- Mode-specific prompts loaded when a Crux mode is active
- Mode-to-model tier mapping for selecting appropriate models per task type
- MCP tools exposed by the `crux` server (session management, knowledge lookup, mode switching, design validation, security audits, TDD gates)

### CruxDev

Autonomous convergence engine accessed via MCP. Drives code through audit-fix-re-audit loops. Key flows:
- `start_convergence(plan)` -- Begin convergence on a plan file
- `convergence_next_task` / `convergence_submit_result` -- Task loop driven by the engine
- Planning via `get_methodology()` and `create_plan_template()`

### Control Plane (`control-plane/`)

Workspace management system supporting multiple adaptor types. The `Workspace` namespace handles creation, configuration, and lifecycle of isolated workspaces (git worktrees or other sandbox types). Includes SSE streaming for real-time workspace events. `Control` namespace manages Crux platform account authentication with OAuth token refresh.

### Plugin System

Plugins can hook into tool execution lifecycle, contribute custom tools, and extend provider authentication. Built-in plugins handle Codex, Copilot, and GitLab auth. External plugins are installed from npm.

### HTTP Server (`server/server.ts`)

Hono-based server with route modules:
- `routes/session.ts` -- Session CRUD and prompting
- `routes/project.ts` -- Project management
- `routes/provider.ts` -- Model listing and provider info
- `routes/config.ts` -- Configuration management
- `routes/mcp.ts` -- MCP server status
- `routes/file.ts` -- File operations
- `routes/pty.ts` -- Pseudo-terminal sessions
- `routes/permission.ts` -- Permission management
- `routes/question.ts` -- User question/answer flow
- `routes/tui.ts` -- TUI-specific endpoints
- `routes/workspace.ts` -- Workspace management
- `routes/experimental.ts` -- Experimental features
- `routes/global.ts` -- Global state endpoints

Supports CORS, basic auth (via `CRUXCLI_SERVER_PASSWORD`), SSE streaming, WebSocket, and OpenAPI spec generation.

---

## Build System

### Compilation (`packages/cruxcli/script/build.ts`)

Bun's native `Bun.build()` with `compile: true` produces self-contained single-file executables. The build process:

1. Fetches model definitions from `models.dev` and generates `models-snapshot.ts`
2. Loads SQL migration files and embeds them as `CRUXCLI_MIGRATIONS`
3. Compiles with SolidJS plugin for TUI components
4. Produces binaries for all target platforms

### Multi-Platform Targets

| OS | Architecture | Variants |
|----|-------------|----------|
| Linux | arm64 | glibc, musl |
| Linux | x64 | glibc, glibc-baseline, musl, musl-baseline |
| macOS | arm64 | -- |
| macOS | x64 | standard, baseline |
| Windows | x64 | standard, baseline |

"Baseline" variants disable AVX2 for older CPU compatibility.

### Monorepo Tooling

- **Bun** (`1.3.10`) -- Package manager, runtime, test runner, and compiler
- **Turbo** (`2.8.13`) -- Task orchestration (`typecheck`, `build`)
- **SST** (`3.18.10`) -- Infrastructure deployment (Cloudflare home, Stripe, PlanetScale providers)
- **TypeScript** -- `tsgo` (native TypeScript 7.0 preview) for typechecking in the core package
- **Drizzle Kit** -- Database migration generation
- **Husky** -- Git hooks
- **Prettier** -- Code formatting (no semicolons, 120 char width)
