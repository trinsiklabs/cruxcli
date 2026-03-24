# CruxCLI Server API Reference

The CruxCLI server exposes a REST API built with [Hono](https://hono.dev/). Start the server with `cruxcli serve` (default port 4096) or `bun dev serve` during development.

## Authentication

When `CRUXCLI_SERVER_PASSWORD` is set, all requests require HTTP Basic Auth. Username defaults to `cruxcli` unless `CRUXCLI_SERVER_USERNAME` is also set.

## Common Headers

| Header | Purpose |
|--------|---------|
| `x-cruxcli-workspace` | Workspace ID (alternative to `?workspace=` query param) |
| `x-cruxcli-directory` | Working directory (alternative to `?directory=` query param) |

## Common Query Parameters

Most routes under the workspace context accept:

| Parameter | Type | Description |
|-----------|------|-------------|
| `directory` | string | Working directory for the request |
| `workspace` | string | Workspace ID |

---

## Global Routes

These routes are available **before** workspace initialization (no `directory` required).

### `GET /global/health`

Health check. Returns server version.

**Response:** `{ healthy: true, version: string }`

### `GET /global/event`

SSE stream of global events across all workspaces. Emits `server.connected` on connection and `server.heartbeat` every 10 seconds.

**Response:** `text/event-stream` with `{ directory: string, payload: BusEvent }` messages.

### `GET /global/config`

Get the global (user-level) configuration.

**Response:** `Config.Info` object.

### `PATCH /global/config`

Update the global configuration.

**Body:** `Config.Info` (partial).
**Response:** Updated `Config.Info`.

### `POST /global/dispose`

Dispose all CruxCLI instances, releasing resources.

**Response:** `true`

---

## Auth Routes

### `PUT /auth/:providerID`

Set authentication credentials for a provider.

**Body:** `Auth.Info` object.
**Response:** `true`

### `DELETE /auth/:providerID`

Remove authentication credentials for a provider.

**Response:** `true`

---

## OpenAPI Spec

### `GET /doc`

Returns the full OpenAPI 3.1.1 specification for the server.

---

## Project Routes

### `GET /project`

List all projects that have been opened with CruxCLI.

**Response:** `Project.Info[]`

### `GET /project/current`

Get the currently active project.

**Response:** `Project.Info`

### `PATCH /project/:projectID`

Update project properties (name, icon, commands).

**Body:** Project update fields.
**Response:** Updated `Project.Info`.

---

## Session Routes

### `GET /session`

List all sessions, sorted by most recently updated.

**Query Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `directory` | string? | Filter by project directory |
| `roots` | boolean? | Only return root sessions (no parentID) |
| `start` | number? | Filter sessions updated on or after this timestamp (ms) |
| `search` | string? | Filter by title (case-insensitive) |
| `limit` | number? | Max sessions to return |

**Response:** `Session.Info[]`

### `GET /session/status`

Get status of all sessions (active, idle, completed).

**Response:** `Record<string, SessionStatus.Info>`

### `GET /session/:sessionID`

Get a specific session.

**Response:** `Session.Info`

### `POST /session`

Create a new session.

**Body (optional):** `Session.create.schema`
**Response:** `Session.Info`

### `PATCH /session/:sessionID`

Update session properties.

**Body:** `{ title?: string, time?: { archived?: number } }`
**Response:** Updated `Session.Info`.

### `DELETE /session/:sessionID`

Delete a session and all associated data.

**Response:** `true`

### `GET /session/:sessionID/children`

Get all child sessions forked from this session.

**Response:** `Session.Info[]`

### `GET /session/:sessionID/todo`

Get the todo list for a session.

**Response:** `Todo.Info[]`

### `POST /session/:sessionID/init`

Initialize a session (analyzes the project, creates AGENTS.md).

**Body:** Session initialization options.
**Response:** `true`

### `POST /session/:sessionID/fork`

Fork a session at a specific message point.

**Body:** Fork options (messageID, etc.).
**Response:** New `Session.Info`.

### `POST /session/:sessionID/abort`

Abort an active session, stopping AI processing.

**Response:** `true`

### `POST /session/:sessionID/share`

Create a shareable link for a session.

**Response:** `Session.Info` with share URL.

### `DELETE /session/:sessionID/share`

Remove the shareable link (make session private again).

**Response:** `Session.Info`

### `GET /session/:sessionID/diff`

Get file changes from a specific user message.

**Query:** `messageID=<id>`
**Response:** `Snapshot.FileDiff[]`

### `POST /session/:sessionID/summarize`

Summarize a session using AI compaction.

**Body:** `{ providerID: string, modelID: string, auto?: boolean }`
**Response:** `true`

### `GET /session/:sessionID/message`

Get all messages in a session.

**Query:** `limit?: number`
**Response:** `MessageV2.WithParts[]`

### `GET /session/:sessionID/message/:messageID`

Get a specific message.

**Response:** `{ info: MessageV2.Info, parts: MessageV2.Part[] }`

### `DELETE /session/:sessionID/message/:messageID`

Delete a specific message.

**Response:** `true`

### `DELETE /session/:sessionID/message/:messageID/part/:partID`

Delete a part from a message.

**Response:** `true`

### `PATCH /session/:sessionID/message/:messageID/part/:partID`

Update a part in a message.

**Body:** `MessageV2.Part`
**Response:** Updated `MessageV2.Part`.

### `POST /session/:sessionID/message`

Send a new message to a session. Streams the AI response.

**Body:** `SessionPrompt.PromptInput` (minus sessionID).
**Response:** `{ info: MessageV2.Assistant, parts: MessageV2.Part[] }` (streamed).

### `POST /session/:sessionID/prompt_async`

Send a message asynchronously (returns immediately).

**Body:** `SessionPrompt.PromptInput` (minus sessionID).
**Response:** 204 No Content.

### `POST /session/:sessionID/command`

Send a command to a session.

**Body:** `SessionPrompt.CommandInput` (minus sessionID).
**Response:** `{ info: MessageV2.Assistant, parts: MessageV2.Part[] }`

### `POST /session/:sessionID/shell`

Execute a shell command within the session context.

**Body:** `SessionPrompt.ShellInput` (minus sessionID).
**Response:** `MessageV2.Assistant`

### `POST /session/:sessionID/revert`

Revert a specific message, undoing its effects.

**Body:** `SessionRevert.RevertInput` (minus sessionID).
**Response:** `Session.Info`

### `POST /session/:sessionID/unrevert`

Restore all previously reverted messages.

**Response:** `Session.Info`

### `POST /session/:sessionID/permissions/:permissionID` (deprecated)

Respond to a permission request. Use `/permission/:requestID/reply` instead.

**Body:** `{ response: PermissionNext.Reply }`
**Response:** `true`

---

## Permission Routes

### `GET /permission`

List all pending permission requests across sessions.

**Response:** `PermissionNext.Request[]`

### `POST /permission/:requestID/reply`

Respond to a permission request.

**Body:** `{ reply: PermissionNext.Reply, message?: string }`
**Response:** `true`

---

## Question Routes

### `GET /question`

List all pending question requests across sessions.

**Response:** `Question.Request[]`

### `POST /question/:requestID/reply`

Provide answers to a question request.

**Body:** `Question.Reply`
**Response:** `true`

### `POST /question/:requestID/reject`

Reject a question request.

**Response:** `true`

---

## Config Routes

### `GET /config`

Get the merged (project + global) configuration.

**Response:** `Config.Info`

### `PATCH /config`

Update the project-level configuration.

**Body:** `Config.Info`
**Response:** Updated `Config.Info`.

### `GET /config/providers`

List configured providers and their default models.

**Response:** `{ providers: Provider.Info[], default: Record<string, string> }`

---

## Provider Routes

### `GET /provider`

List all available providers (including unconfigured ones from models.dev).

**Response:** `{ all: ModelsDev.Provider[], default: Record<string, string>, connected: string[] }`

### `GET /provider/auth`

Get available authentication methods for all providers.

**Response:** `Record<string, ProviderAuth.Method[]>`

### `POST /provider/:providerID/oauth/authorize`

Start OAuth flow for a provider.

**Body:** `{ method: number }`
**Response:** `ProviderAuth.Authorization`

### `POST /provider/:providerID/oauth/callback`

Complete OAuth for a provider.

**Body:** `{ method: number, code?: string }`
**Response:** `true`

---

## MCP Routes

### `GET /mcp`

Get status of all MCP servers.

**Response:** `Record<string, MCP.Status>`

### `POST /mcp`

Add a new MCP server.

**Body:** `{ name: string, config: Config.Mcp }`
**Response:** `Record<string, MCP.Status>`

### `POST /mcp/:name/auth`

Start OAuth for an MCP server.

**Response:** `{ authorizationUrl: string }`

### `POST /mcp/:name/auth/callback`

Complete OAuth for an MCP server.

**Body:** `{ code: string }`
**Response:** `MCP.Status`

### `POST /mcp/:name/auth/authenticate`

Start OAuth flow and wait for callback (opens browser).

**Response:** `MCP.Status`

### `DELETE /mcp/:name/auth`

Remove OAuth credentials for an MCP server.

**Response:** `{ success: true }`

### `POST /mcp/:name/connect`

Connect an MCP server.

**Response:** `true`

### `POST /mcp/:name/disconnect`

Disconnect an MCP server.

**Response:** `true`

---

## PTY Routes

### `GET /pty`

List all active PTY sessions.

**Response:** `Pty.Info[]`

### `POST /pty`

Create a new PTY session.

**Body:** `Pty.CreateInput`
**Response:** `Pty.Info`

### `GET /pty/:ptyID`

Get a specific PTY session.

**Response:** `Pty.Info`

### `PUT /pty/:ptyID`

Update a PTY session.

**Body:** `Pty.UpdateInput`
**Response:** `Pty.Info`

### `DELETE /pty/:ptyID`

Remove and terminate a PTY session.

**Response:** `true`

### `GET /pty/:ptyID/connect`

WebSocket endpoint. Connect to a PTY session for real-time interaction.

---

## File Routes

### `GET /find`

Search for text patterns across project files using ripgrep.

**Query:** `pattern=<regex>`
**Response:** Ripgrep match data array.

### `GET /find/file`

Search for files by name/pattern.

**Query:** `query=<pattern>`, `dirs=true|false`, `type=file|directory`, `limit=<n>`
**Response:** `string[]` of file paths.

### `GET /find/symbol`

Search for workspace symbols via LSP.

**Query:** `query=<name>`
**Response:** `LSP.Symbol[]`

### `GET /file`

List files and directories at a path.

**Query:** `path=<dir>`
**Response:** `File.Node[]`

### `GET /file/content`

Read file content.

**Query:** `path=<filepath>`
**Response:** `File.Content`

### `GET /file/status`

Get git status of all files.

**Response:** `File.Info[]`

---

## Experimental Routes

### `GET /experimental/tool/ids`

List all available tool IDs.

**Response:** `string[]`

### `GET /experimental/tool`

List tools with JSON schema parameters for a provider/model.

**Query:** `provider=<id>`, `model=<id>`
**Response:** `{ id: string, description: string, parameters: object }[]`

### `POST /experimental/worktree`

Create a new git worktree.

**Body:** `Worktree.create.schema`
**Response:** `Worktree.Info`

### `GET /experimental/worktree`

List all sandbox worktrees.

**Response:** `string[]`

### `DELETE /experimental/worktree`

Remove a git worktree.

**Body:** `Worktree.remove.schema`
**Response:** `true`

### `POST /experimental/worktree/reset`

Reset a worktree to the primary branch.

**Body:** `Worktree.reset.schema`
**Response:** `true`

### `GET /experimental/session`

List sessions across all projects (global). Supports pagination via `x-next-cursor` header.

**Query:** `directory?`, `roots?`, `start?`, `cursor?`, `search?`, `limit?`, `archived?`
**Response:** `Session.GlobalInfo[]`

### `GET /experimental/resource`

Get all available MCP resources.

**Response:** `Record<string, MCP.Resource>`

### Experimental Workspace Routes

#### `POST /experimental/workspace`

Create a workspace for the current project.

**Body:** Workspace create options.
**Response:** `Workspace.Info`

#### `GET /experimental/workspace`

List all workspaces.

**Response:** `Workspace.Info[]`

#### `DELETE /experimental/workspace/:id`

Remove a workspace.

**Response:** `Workspace.Info` or null.

---

## Utility Routes

### `GET /path`

Get path information for the CruxCLI instance.

**Response:** `{ home: string, state: string, config: string, worktree: string, directory: string }`

### `GET /vcs`

Get VCS (git) info for the current project.

**Response:** `{ branch: string }`

### `GET /command`

List all available commands.

**Response:** `Command.Info[]`

### `POST /log`

Write a log entry.

**Body:** `{ service: string, level: "debug"|"info"|"error"|"warn", message: string, extra?: Record<string, any> }`
**Response:** `true`

### `GET /agent`

List all available agents.

**Response:** `Agent.Info[]`

### `GET /skill`

List all available skills.

**Response:** `Skill.Info[]`

### `GET /lsp`

Get LSP server status.

**Response:** `LSP.Status[]`

### `GET /formatter`

Get formatter status.

**Response:** `Format.Status[]`

### `GET /event`

SSE stream of workspace-scoped events. Emits `server.connected` on connection and `server.heartbeat` every 10 seconds.

**Response:** `text/event-stream` with `BusEvent` messages.

### `POST /instance/dispose`

Dispose the current CruxCLI instance.

**Response:** `true`

---

## TUI Routes

These routes control the Terminal User Interface when CruxCLI is running in TUI mode.

### `POST /tui/append-prompt`

Append text to the TUI prompt input.

### `POST /tui/submit-prompt`

Submit the current prompt.

### `POST /tui/clear-prompt`

Clear the prompt input.

### `POST /tui/open-help`

Open the help dialog.

### `POST /tui/open-sessions`

Open the session picker dialog.

### `POST /tui/open-themes`

Open the theme picker dialog.

### `POST /tui/open-models`

Open the model picker dialog.

### `POST /tui/execute-command`

Execute a TUI command by name.

**Body:** `{ command: string }`

### `POST /tui/show-toast`

Show a toast notification.

### `POST /tui/publish`

Publish an arbitrary TUI event.

### `POST /tui/select-session`

Navigate to a specific session.

**Body:** `{ sessionID: string }`

### TUI Control (internal)

#### `GET /tui/control/next`

Get the next queued TUI request (used by the TUI frontend).

#### `POST /tui/control/response`

Submit a response to a TUI request.

---

## Fallback

### `ALL /*`

Any unmatched route proxies to `https://app.cruxcli.dev` (the hosted web dashboard).
