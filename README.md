<p align="center">
  <a href="https://github.com/trinsiklabs/cruxcli">
    <picture>
      <source srcset="packages/console/app/src/asset/logo-ornate-dark.svg" media="(prefers-color-scheme: dark)">
      <source srcset="packages/console/app/src/asset/logo-ornate-light.svg" media="(prefers-color-scheme: light)">
      <img src="packages/console/app/src/asset/logo-ornate-light.svg" alt="CruxCLI logo">
    </picture>
  </a>
</p>
<p align="center">The intelligent terminal agent. Provider-agnostic AI coding with the Crux intelligence layer.</p>
<p align="center">
  <a href="https://www.npmjs.com/package/cruxcli"><img alt="npm" src="https://img.shields.io/npm/v/cruxcli?style=flat-square" /></a>
  <a href="https://github.com/trinsiklabs/cruxcli/actions/workflows/publish.yml"><img alt="Build status" src="https://img.shields.io/github/actions/workflow/status/trinsiklabs/cruxcli/publish.yml?style=flat-square&branch=main" /></a>
  <a href="https://github.com/trinsiklabs/cruxcli/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/trinsiklabs/cruxcli?style=flat-square" /></a>
</p>

---

## What is CruxCLI?

CruxCLI is a hard fork of OpenCode, rebuilt around the **Crux intelligence layer**. It replaces static prompt templates with a mode-driven system that adapts behavior, token budgets, and model parameters per task. The result is a terminal-native AI coding agent that is provider-agnostic, context-aware, and designed for convergence-driven development.

**Key differences from stock OpenCode:**

- **Crux Mode System** -- Active modes drive system prompts, temperature/topP tuning, and token budgets. Modes are defined as Markdown files, not hardcoded strings.
- **Token Budget System** -- Per-mode token budgets replace step-count limits. Warnings at 70-80%, hard enforcement at 90-95% via `toolChoice: none`. No more arbitrary step caps.
- **Workspace Checkpoints** -- Automatic snapshotting before risky operations via git worktree integration. Roll back to known-good states.
- **Session Context Injection** -- Working state, key decisions, and pending items flow from `.crux/sessions/state.json` into every system prompt.
- **CruxDev Convergence Engine** -- Drive code through audit-fix-re-audit loops until two consecutive clean passes. Replaces "human says do it again" with deterministic convergence.
- **Provider-Agnostic** -- Works with Anthropic, OpenAI, Google, Amazon Bedrock, Azure, Copilot, local models, or any provider supported by models.dev.

---

### Installation

```bash
# npm (recommended)
npm i -g cruxcli@latest

# Other package managers
bun add -g cruxcli@latest
pnpm add -g cruxcli@latest
```

### Building from Source

```bash
git clone https://github.com/trinsiklabs/cruxcli.git
cd cruxcli
bun install
bun dev
```

To compile a standalone binary:

```bash
./packages/cruxcli/script/build.ts --single
./packages/cruxcli/dist/cruxcli-$(uname -s | tr A-Z a-z)-$(uname -m)/bin/cruxcli --version
```

---

### Features

#### Crux Mode System

CruxCLI ships with two built-in agents, switchable with `Tab`:

- **build** -- Default, full-access agent for development work
- **plan** -- Read-only agent for analysis and code exploration (denies file edits, asks before running commands)

Modes are defined as Markdown files in `.cruxcli/agents/` or `~/.config/cruxcli/agents/`. Each mode can specify its own model, temperature, top_p, prompt, steps limit, and permission set.

A **general** subagent handles complex searches and multistep tasks internally, invocable via `@general` in messages.

#### Token Budget System

Each mode has a configurable token budget. CruxCLI tracks token usage per mode per session and enforces limits through infrastructure, not prompt instructions:

- **Warning** at 70-80% of budget: a reminder is injected into the system prompt
- **Hard limit** at 90-95%: `toolChoice` is set to `none`, forcing a text-only response

#### Workspace Checkpoints

CruxCLI integrates with git worktrees to create lightweight checkpoints before convergence rounds. Roll back with `cruxcli checkpoint` commands.

#### Provider-Agnostic Design

Configure any provider via `cruxcli.json`:

```jsonc
{
  "$schema": "https://cruxcli.dev/config.json",
  "provider": {
    "anthropic": {
      "options": { "apiKey": "sk-..." }
    }
  },
  "model": "anthropic/claude-sonnet-4-20250514"
}
```

All providers from [models.dev](https://models.dev) are supported. CruxCLI's mode system applies per-mode temperature and topP tuning regardless of which provider you use.

#### Client/Server Architecture

CruxCLI runs a headless API server that the TUI connects to. This means:

- Run `cruxcli serve` on your machine, drive it from a mobile app or web UI
- The TUI is just one of many possible frontends
- Full REST API documented in [docs/API.md](docs/API.md)

#### LSP Integration

Out-of-the-box LSP support for 30+ language servers. Provides workspace symbol search, diagnostics, and formatting without additional configuration.

---

### Documentation

- [Configuration Reference](docs/CONFIGURATION.md)
- [Server API Reference](docs/API.md)
- [Testing Guide](docs/TESTING.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Contributing](CONTRIBUTING.md)
- [Roadmap](ROADMAP.md)

---

### Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for development setup, PR expectations, and style guidelines.

---

### FAQ

#### How is this different from Claude Code?

- 100% open source
- Not coupled to any provider. CruxCLI works with Claude, OpenAI, Google, local models, or any models.dev provider. As models evolve, being provider-agnostic matters.
- The Crux intelligence layer adds mode-driven prompts, token budgets, and session context that adapt behavior per task -- not just per conversation.
- Out-of-the-box LSP support
- Client/server architecture enables remote and multi-frontend operation
- Built for convergence-driven development via CruxDev

#### How is this different from OpenCode?

CruxCLI is a hard fork of OpenCode (clean break, no upstream sync). The differences:

- Crux mode system replaces hardcoded prompts
- Token budget system replaces step-count limits
- Bridge plugin absorbed into native source
- Workspace checkpoint integration
- Session context injection from Crux platform
- All config/env/paths use `cruxcli` namespace (`.cruxcli/`, `CRUXCLI_*`, `cruxcli.json`)

#### What is the CruxDev convergence engine?

CruxDev drives code through deterministic audit-fix-re-audit loops until two consecutive independent clean passes are achieved. It replaces manual "run it again" cycles with a structured convergence process. See the [Roadmap](ROADMAP.md) for status.

---

**GitHub:** [trinsiklabs/cruxcli](https://github.com/trinsiklabs/cruxcli)
