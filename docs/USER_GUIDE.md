# CruxCLI User Guide

**Last Updated:** 2026-03-24

## Getting Started

### Install

```bash
curl -fsSL https://cruxcli.ai/install | bash
# or
npm i -g cruxcli@latest
# or
brew install trinsiklabs/tap/cruxcli
```

### Configure a Provider

CruxCLI works with any LLM provider. Set an API key:

```bash
# OpenRouter (recommended — access to 100+ models)
export OPENROUTER_API_KEY="sk-or-..."

# Or Anthropic directly
export ANTHROPIC_API_KEY="sk-ant-..."

# Or OpenAI
export OPENAI_API_KEY="sk-..."
```

### Launch

```bash
cd your-project
cruxcli
```

CruxCLI opens in a split-screen TUI. Type your request and press Enter.

## Key Concepts

### Agents

CruxCLI has two built-in agents, switchable with `Tab`:

| Agent | Access | Use for |
|-------|--------|---------|
| **build** | Full (read + write + bash) | Development work — writing code, running tests, editing files |
| **plan** | Read-only | Analysis, code exploration, planning changes before making them |

### Modes (via Crux)

If Crux is installed, CruxCLI inherits 24 research-optimized modes that control prompt behavior and model selection. Each mode tunes the agent for a specific task type (coding, review, architecture, debugging, etc.).

### Checkpoints

CruxCLI automatically snapshots your workspace before destructive operations (file edits, writes, bash commands). You can also manage checkpoints manually:

```bash
cruxcli checkpoint create "before refactor"
cruxcli checkpoint list
cruxcli checkpoint restore <id>
cruxcli checkpoint diff <id>
cruxcli checkpoint remove <id>
```

Disable auto-checkpoints: `export CRUXCLI_DISABLE_AUTO_CHECKPOINT=1`

### Tools

The agent has access to these built-in tools:

| Tool | What it does |
|------|-------------|
| `bash` | Run shell commands |
| `read` | Read file contents |
| `write` | Create or overwrite files |
| `edit` | Make targeted edits to existing files |
| `glob` | Find files by pattern |
| `grep` | Search file contents |
| `webfetch` | Fetch and process web content |
| `websearch` | Search the web |
| `lsp` | Query Language Server Protocol (definitions, references, symbols) |
| `task` | Create and manage tasks |

### MCP Integration

CruxCLI connects to MCP (Model Context Protocol) servers for extended capabilities. Configure in `.mcp.json` at project root:

```json
{
  "mcpServers": {
    "my-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["my-mcp-server"]
    }
  }
}
```

## Configuration

### Config File

CruxCLI reads config from (in priority order):
1. `cruxcli.json` or `cruxcli.jsonc` in project root
2. `.cruxcli/cruxcli.json` in project root
3. `~/.config/cruxcli/cruxcli.json` (global)

### Provider Configuration

```jsonc
{
  "provider": {
    "openrouter": {
      "npm": "@openrouter/ai-sdk-provider",
      "api": "https://openrouter.ai/api/v1",
      "models": {
        "my-model": {
          "id": "anthropic/claude-opus-4"
        }
      }
    }
  },
  "model": "openrouter/my-model"
}
```

### Environment Variables

See `CRUXCLI_*` environment variables in the source (`src/flag/flag.ts`) for all options. Key ones:

| Variable | Purpose |
|----------|---------|
| `CRUXCLI_CONFIG_DIR` | Custom config directory |
| `CRUXCLI_DISABLE_AUTO_CHECKPOINT` | Disable auto-checkpoints |
| `CRUXCLI_DISABLE_AUTOUPDATE` | Disable update checks |
| `CRUXCLI_PERMISSION` | Default permission mode |

## Commands

| Command | Description |
|---------|-------------|
| `cruxcli` | Start TUI (default) |
| `cruxcli run [message]` | Run with a message (non-interactive) |
| `cruxcli checkpoint` | Manage workspace checkpoints |
| `cruxcli auth` | Manage provider credentials |
| `cruxcli models` | List available models |
| `cruxcli mcp` | Manage MCP servers |
| `cruxcli agent` | Manage agents |
| `cruxcli serve` | Start headless server |
| `cruxcli web` | Start server + open web interface |
| `cruxcli upgrade` | Upgrade to latest version |
| `cruxcli debug` | Debugging utilities |

## VS Code Extension

Install the CruxCLI extension from the VS Code marketplace (publisher: trinsiklabs).

| Shortcut | Action |
|----------|--------|
| `Cmd+Esc` | Open/focus CruxCLI terminal |
| `Cmd+Shift+Esc` | Open new CruxCLI terminal |
| `Cmd+Option+K` | Insert file reference |
| `Cmd+Shift+K` | Send selection to CruxCLI |

Right-click menus available in editor and file explorer.
