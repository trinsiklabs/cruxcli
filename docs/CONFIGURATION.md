# CruxCLI Configuration Reference

CruxCLI is configured through `cruxcli.json` (or `cruxcli.jsonc`) files and environment variables.

## Config File Locations

Configuration is loaded in order of increasing precedence. Later sources override earlier ones.

| Priority | Source | Description |
|----------|--------|-------------|
| 1 (lowest) | Remote `.well-known/cruxcli` | Organization defaults via wellknown auth |
| 2 | `~/.config/cruxcli/cruxcli.json` | Global user config |
| 3 | `CRUXCLI_CONFIG` env var | Custom config file path |
| 4 | `cruxcli.json` in project root | Project-level config |
| 5 | `.cruxcli/cruxcli.json` | Project .cruxcli directory config |
| 6 | `CRUXCLI_CONFIG_CONTENT` env var | Inline JSON config string |
| 7 (highest) | Managed config directory | Enterprise admin-controlled (see below) |

### Managed Config Directory (Enterprise)

Admin-controlled settings that override all user and project config:

| Platform | Path |
|----------|------|
| macOS | `/Library/Application Support/cruxcli` |
| Windows | `C:\ProgramData\cruxcli` |
| Linux | `/etc/cruxcli` |

### .cruxcli Directory

The `.cruxcli/` directory (in your project root or `CRUXCLI_CONFIG_DIR`) can contain:

| Path | Purpose |
|------|---------|
| `.cruxcli/cruxcli.json` | Config overrides |
| `.cruxcli/agents/*.md` | Agent definitions (Markdown with frontmatter) |
| `.cruxcli/commands/*.md` | Custom command templates |
| `.cruxcli/plugins/*.{ts,js}` | Local plugins |

The global `~/.config/cruxcli/` directory supports the same structure.

---

## Config Schema

All fields are optional. The `$schema` field enables IDE autocomplete.

```jsonc
{
  "$schema": "https://cruxcli.dev/config.json"
}
```

### Top-Level Fields

| Field | Type | Description |
|-------|------|-------------|
| `$schema` | string | JSON schema URL for validation |
| `logLevel` | `"DEBUG"` \| `"INFO"` \| `"WARN"` \| `"ERROR"` | Log level |
| `model` | string | Default model in `provider/model` format (e.g., `"anthropic/claude-sonnet-4-20250514"`) |
| `small_model` | string | Model for lightweight tasks (title generation, etc.) |
| `default_agent` | string | Default primary agent. Falls back to `"build"` if unset or invalid |
| `username` | string | Display name in conversations (defaults to OS username) |
| `snapshot` | boolean | Enable snapshots |
| `share` | `"manual"` \| `"auto"` \| `"disabled"` | Session sharing behavior |
| `autoshare` | boolean | **Deprecated.** Use `share` instead |
| `autoupdate` | boolean \| `"notify"` | Auto-update behavior |
| `disabled_providers` | string[] | Providers to exclude from auto-loading |
| `enabled_providers` | string[] | When set, ONLY these providers are enabled |
| `instructions` | string[] | Additional instruction file paths or patterns |
| `layout` | `"auto"` \| `"stretch"` | **Deprecated.** Always uses stretch layout |
| `plugin` | string[] | Plugin specifiers (npm packages or `file://` URLs) |
| `tools` | Record<string, boolean> | **Deprecated.** Use `permission` instead |

### `server`

Configuration for `cruxcli serve` and `cruxcli web`.

| Field | Type | Description |
|-------|------|-------------|
| `port` | number | Port to listen on |
| `hostname` | string | Hostname to bind to |
| `mdns` | boolean | Enable mDNS service discovery |
| `mdnsDomain` | string | Custom mDNS domain (default: `cruxcli.local`) |
| `cors` | string[] | Additional CORS-allowed origins |

### `agent`

Agent configuration. Built-in agents: `build`, `plan` (primary), `general`, `explore` (subagent), `title`, `summary`, `compaction` (specialized). You can add custom agents.

Each agent supports:

| Field | Type | Description |
|-------|------|-------------|
| `model` | string | Model ID in `provider/model` format |
| `variant` | string | Default model variant for this agent |
| `temperature` | number | Temperature parameter |
| `top_p` | number | Top-p parameter |
| `prompt` | string | System prompt (appended to base prompt) |
| `description` | string | When to use this agent |
| `mode` | `"subagent"` \| `"primary"` \| `"all"` | Agent mode |
| `hidden` | boolean | Hide from `@` autocomplete (subagents only) |
| `color` | string | Hex color (`#FF5733`) or theme color (`primary`, `secondary`, etc.) |
| `steps` | number | Max agentic iterations before forcing text-only response |
| `maxSteps` | number | **Deprecated.** Use `steps` |
| `disable` | boolean | Disable this agent |
| `permission` | Permission | Per-agent permission overrides |
| `tools` | Record<string, boolean> | **Deprecated.** Use `permission` |
| `options` | Record<string, any> | Additional agent-specific options |

### `mode`

**Deprecated.** Use `agent` instead. Mode definitions are automatically migrated to agents with `mode: "primary"`.

### `provider`

Custom provider configurations and model overrides. Keyed by provider ID.

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Display name |
| `api` | string | API type (e.g., `"openai"`, `"anthropic"`) |
| `models` | Record<string, ModelConfig> | Model-specific overrides |
| `whitelist` | string[] | Only allow these models |
| `blacklist` | string[] | Exclude these models |
| `options.apiKey` | string | API key |
| `options.baseURL` | string | Custom API base URL |
| `options.enterpriseUrl` | string | GitHub Enterprise URL (for Copilot) |
| `options.setCacheKey` | boolean | Enable promptCacheKey |
| `options.timeout` | number \| false | Request timeout in ms (default 300000). Set `false` to disable |

Example:

```jsonc
{
  "provider": {
    "anthropic": {
      "options": { "apiKey": "sk-ant-..." }
    },
    "custom-ollama": {
      "name": "Local Ollama",
      "api": "openai",
      "options": { "baseURL": "http://localhost:11434/v1" },
      "models": {
        "llama3": { "name": "Llama 3" }
      }
    }
  }
}
```

### `mcp`

MCP (Model Context Protocol) server configurations. Keyed by server name.

#### Local MCP Server

```jsonc
{
  "mcp": {
    "my-server": {
      "type": "local",
      "command": ["node", "server.js"],
      "environment": { "API_KEY": "..." },
      "enabled": true,
      "timeout": 5000
    }
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"local"` | Local process |
| `command` | string[] | Command and arguments |
| `environment` | Record<string, string> | Environment variables |
| `enabled` | boolean | Enable on startup |
| `timeout` | number | Request timeout in ms (default 5000) |

#### Remote MCP Server

```jsonc
{
  "mcp": {
    "remote-server": {
      "type": "remote",
      "url": "https://mcp.example.com",
      "headers": { "Authorization": "Bearer ..." },
      "oauth": { "clientId": "...", "scope": "read write" }
    }
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"remote"` | Remote URL |
| `url` | string | Server URL |
| `headers` | Record<string, string> | Request headers |
| `oauth` | object \| false | OAuth config (or `false` to disable auto-detection) |
| `oauth.clientId` | string | OAuth client ID |
| `oauth.clientSecret` | string | OAuth client secret |
| `oauth.scope` | string | OAuth scopes |
| `enabled` | boolean | Enable on startup |
| `timeout` | number | Request timeout in ms |

### `permission`

Permission configuration for tools. Can be set globally or per-agent.

**Actions:** `"ask"` (prompt user), `"allow"` (auto-approve), `"deny"` (auto-reject).

Built-in tool permissions:

| Tool | Description |
|------|-------------|
| `read` | File reading |
| `edit` | File editing (covers write, edit, patch, multiedit) |
| `glob` | File globbing |
| `grep` | Text search |
| `list` | Directory listing |
| `bash` | Shell command execution |
| `task` | Task execution |
| `external_directory` | Access files outside project |
| `todowrite` | Write todo items |
| `todoread` | Read todo items |
| `question` | Ask questions |
| `webfetch` | Fetch web content |
| `websearch` | Web search |
| `codesearch` | Code search |
| `lsp` | LSP operations |
| `doom_loop` | Doom loop detection |
| `skill` | Skill execution |

Permissions can use glob patterns for bash commands:

```jsonc
{
  "permission": {
    "bash": {
      "npm test": "allow",
      "rm -rf *": "deny",
      "*": "ask"
    }
  }
}
```

### `command`

Custom command definitions. Commands can also be defined as Markdown files in `.cruxcli/commands/`.

```jsonc
{
  "command": {
    "review": {
      "template": "Review this pull request: $ARGUMENTS",
      "description": "Code review",
      "agent": "plan",
      "model": "anthropic/claude-sonnet-4-20250514",
      "subtask": false
    }
  }
}
```

### `skills`

Additional skill configuration.

| Field | Type | Description |
|-------|------|-------------|
| `paths` | string[] | Additional skill folder paths |
| `urls` | string[] | URLs to fetch skills from |

### `keybinds`

Full TUI keybinding customization. All fields have defaults. Use `"none"` to disable a binding.

Key format: `ctrl+x`, `shift+return`, `alt+f`, etc. Multiple bindings separated by commas.

The `leader` key (default: `ctrl+x`) is referenced as `<leader>` in other bindings.

### `formatter`

Formatter configuration. Set to `false` to disable all formatters.

```jsonc
{
  "formatter": {
    "prettier": {
      "command": ["prettier", "--write"],
      "extensions": [".ts", ".js", ".json"]
    }
  }
}
```

### `lsp`

LSP server configuration. Set to `false` to disable all LSP servers. Custom servers require `extensions`.

```jsonc
{
  "lsp": {
    "custom-lsp": {
      "command": ["my-lsp", "--stdio"],
      "extensions": [".myext"],
      "env": { "DEBUG": "true" },
      "initialization": {}
    }
  }
}
```

### `compaction`

Context compaction settings.

| Field | Type | Description |
|-------|------|-------------|
| `auto` | boolean | Auto-compact when context is full (default: true) |
| `prune` | boolean | Prune old tool outputs (default: true) |
| `reserved` | number | Token buffer to avoid overflow during compaction |

### `watcher`

File watcher configuration.

| Field | Type | Description |
|-------|------|-------------|
| `ignore` | string[] | Additional file patterns to ignore |

### `enterprise`

Enterprise configuration.

| Field | Type | Description |
|-------|------|-------------|
| `url` | string | Enterprise server URL |

### `experimental`

Experimental features (may change without notice).

| Field | Type | Description |
|-------|------|-------------|
| `disable_paste_summary` | boolean | Disable paste summary |
| `batch_tool` | boolean | Enable batch tool |
| `openTelemetry` | boolean | Enable OpenTelemetry for AI SDK calls |
| `primary_tools` | string[] | Tools only available to primary agents |
| `continue_loop_on_deny` | boolean | Continue agent loop when tool call is denied |
| `mcp_timeout` | number | MCP request timeout in ms |

---

## Environment Variables

All CruxCLI environment variables use the `CRUXCLI_` prefix. These are read from `packages/opencode/src/flag/flag.ts`.

### Core

| Variable | Type | Description |
|----------|------|-------------|
| `CRUXCLI_CONFIG` | string | Path to a custom config file |
| `CRUXCLI_CONFIG_DIR` | string | Custom `.cruxcli` directory path |
| `CRUXCLI_CONFIG_CONTENT` | string | Inline JSON config (highest non-managed precedence) |
| `CRUXCLI_TUI_CONFIG` | string | Path to TUI-specific config |
| `CRUXCLI_CLIENT` | string | Client identifier (default: `"cli"`) |
| `CRUXCLI_PERMISSION` | JSON string | Permission overrides as JSON |
| `CRUXCLI_FAKE_VCS` | string | Fake VCS info for testing |

### Server

| Variable | Type | Description |
|----------|------|-------------|
| `CRUXCLI_SERVER_PASSWORD` | string | HTTP Basic Auth password for server mode |
| `CRUXCLI_SERVER_USERNAME` | string | HTTP Basic Auth username (default: `"cruxcli"`) |

### Feature Flags

| Variable | Type | Description |
|----------|------|-------------|
| `CRUXCLI_AUTO_SHARE` | boolean | Auto-share sessions |
| `CRUXCLI_DISABLE_AUTOUPDATE` | boolean | Disable auto-update |
| `CRUXCLI_DISABLE_PRUNE` | boolean | Disable pruning in compaction |
| `CRUXCLI_DISABLE_TERMINAL_TITLE` | boolean | Don't set terminal title |
| `CRUXCLI_DISABLE_DEFAULT_PLUGINS` | boolean | Don't load default plugins |
| `CRUXCLI_DISABLE_LSP_DOWNLOAD` | boolean | Don't auto-download LSP servers |
| `CRUXCLI_ENABLE_EXPERIMENTAL_MODELS` | boolean | Show experimental models |
| `CRUXCLI_DISABLE_AUTO_CHECKPOINT` | boolean | Disable automatic checkpoints |
| `CRUXCLI_DISABLE_AUTOCOMPACT` | boolean | Disable automatic compaction |
| `CRUXCLI_DISABLE_MODELS_FETCH` | boolean | Don't fetch models from models.dev |
| `CRUXCLI_DISABLE_CLAUDE_CODE` | boolean | Disable Claude Code integration entirely |
| `CRUXCLI_DISABLE_CLAUDE_CODE_PROMPT` | boolean | Disable Claude Code prompt injection |
| `CRUXCLI_DISABLE_CLAUDE_CODE_SKILLS` | boolean | Disable Claude Code skills |
| `CRUXCLI_DISABLE_EXTERNAL_SKILLS` | boolean | Disable external skill loading |
| `CRUXCLI_DISABLE_PROJECT_CONFIG` | boolean | Ignore project-level config files |
| `CRUXCLI_DISABLE_FILETIME_CHECK` | boolean | Disable file modification time checks |
| `CRUXCLI_ENABLE_QUESTION_TOOL` | boolean | Enable the question tool |
| `CRUXCLI_ENABLE_EXA` | boolean | Enable Exa search integration |
| `CRUXCLI_GIT_BASH_PATH` | string | Custom git bash path (Windows) |

### Models

| Variable | Type | Description |
|----------|------|-------------|
| `CRUXCLI_MODELS_URL` | string | Custom URL for models.dev data |
| `CRUXCLI_MODELS_PATH` | string | Local path to models JSON file |

### Experimental

| Variable | Type | Description |
|----------|------|-------------|
| `CRUXCLI_EXPERIMENTAL` | boolean | Enable all experimental features |
| `CRUXCLI_EXPERIMENTAL_FILEWATCHER` | boolean | Enable experimental file watcher |
| `CRUXCLI_EXPERIMENTAL_DISABLE_FILEWATCHER` | boolean | Disable experimental file watcher |
| `CRUXCLI_EXPERIMENTAL_ICON_DISCOVERY` | boolean | Enable icon discovery |
| `CRUXCLI_EXPERIMENTAL_DISABLE_COPY_ON_SELECT` | boolean | Disable copy-on-select (default true on Windows) |
| `CRUXCLI_EXPERIMENTAL_BASH_DEFAULT_TIMEOUT_MS` | number | Default bash command timeout |
| `CRUXCLI_EXPERIMENTAL_OUTPUT_TOKEN_MAX` | number | Max output tokens |
| `CRUXCLI_EXPERIMENTAL_OXFMT` | boolean | Enable oxfmt formatter |
| `CRUXCLI_EXPERIMENTAL_LSP_TY` | boolean | Enable ty LSP |
| `CRUXCLI_EXPERIMENTAL_LSP_TOOL` | boolean | Enable LSP tool |
| `CRUXCLI_EXPERIMENTAL_PLAN_MODE` | boolean | Enable plan mode |
| `CRUXCLI_EXPERIMENTAL_MARKDOWN` | boolean | Enable markdown rendering (default true) |

### Test-Only

| Variable | Type | Description |
|----------|------|-------------|
| `CRUXCLI_TEST_HOME` | string | Isolated home directory for tests |
| `CRUXCLI_TEST_MANAGED_CONFIG_DIR` | string | Isolated managed config dir for tests |

---

## Boolean Environment Variables

Boolean env vars accept `"true"` or `"1"` for truthy, `"false"` or `"0"` for falsy (case-insensitive).
