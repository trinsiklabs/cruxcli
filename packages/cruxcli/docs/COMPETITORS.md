# CruxCLI - Competitive Analysis

This analysis tracks direct terminal-agent competitors plus watch-list tools that shape user expectations in coding-assistant workflows.

## Official Competitors

### OpenCode

- URL: https://opencode.ai
- Category: official
- Pricing: Open-source; hosted options via ecosystem
- Strengths: large open-source adoption, fast release cadence, rich provider ecosystem
- Weaknesses: no convergence methodology, no correction detection layer, less opinionated completion guardrails

### Claude Code

- URL: https://claude.ai/claude-code
- Category: official
- Pricing: Subscription and usage-based
- Strengths: first-party model access, strong UX polish, enterprise adoption
- Weaknesses: model lock-in, proprietary stack, no plugin API

### Gemini CLI

- URL: https://github.com/google-gemini/gemini-cli
- Category: official
- Pricing: Free tier plus paid usage
- Strengths: strong free tier, Google ecosystem integration, rapid adoption
- Weaknesses: provider lock-in, newer ecosystem, limited extension model

### Codex CLI

- URL: https://github.com/openai/codex
- Category: official
- Pricing: Usage-based API
- Strengths: backed by OpenAI, strong model quality, agent workflow primitives
- Weaknesses: provider lock-in, early ecosystem maturity, limited plugin surface

## Watch Competitors

### Aider

- URL: https://github.com/Aider-AI/aider
- Category: watch
- Pricing: Open-source

### Continue

- URL: https://continue.dev
- Category: watch
- Pricing: Open-source with enterprise options

## Gap Analysis

| Feature                    | CruxCLI | Aider | Claude Code | Codex CLI | Continue | Gemini CLI | OpenCode |
| -------------------------- | ------- | ----- | ----------- | --------- | -------- | ---------- | -------- |
| Auto-commits               | N       | Y     | N           | N         | N        | N          | N        |
| Autocomplete               | N       | N     | N           | N         | Y        | N          | N        |
| Client/server architecture | Y       | N     | N           | N         | N        | N          | Y        |
| Context providers          | N       | N     | N           | N         | Y        | N          | N        |
| Convergence engine         | Y       | N     | N           | N         | N        | N          | N        |
| Correction detection       | Y       | N     | N           | N         | N        | N          | N        |
| Cost visibility            | N       | N     | Y           | N         | N        | N          | N        |
| Custom models              | N       | N     | N           | N         | Y        | N          | N        |
| Custom modes               | N       | N     | N           | N         | N        | N          | Y        |
| Desktop app                | Y       | N     | N           | N         | N        | N          | Y        |
| Git integration            | N       | Y     | N           | N         | N        | N          | N        |
| IDE integration            | N       | N     | N           | N         | Y        | N          | N        |
| Image input                | N       | N     | N           | Y         | N        | N          | N        |
| Inline edits               | N       | N     | N           | N         | Y        | N          | N        |
| Large context windows      | N       | N     | Y           | N         | N        | Y          | N        |
| LSP integration            | Y       | N     | N           | N         | N        | N          | Y        |
| MCP support                | N       | N     | N           | N         | N        | Y          | N        |
| Mode-to-model tier mapping | Y       | N     | N           | N         | N        | N          | N        |
| Multi-agent workflows      | N       | N     | N           | Y         | N        | N          | N        |
| Open-source core           | N       | N     | N           | Y         | N        | N          | Y        |
| Plan mode                  | N       | N     | N           | N         | N        | Y          | N        |
| Plugin API                 | Y       | N     | N           | N         | N        | N          | Y        |
| Provider-agnostic models   | Y       | N     | N           | N         | N        | N          | Y        |
| Repo map                   | N       | Y     | N           | N         | N        | N          | N        |
| Token budget system        | Y       | N     | N           | N         | N        | N          | N        |
| TUI interface              | Y       | N     | Y           | Y         | N        | Y          | Y        |
| Voice input                | N       | Y     | N           | N         | N        | N          | N        |
| VS Code extension          | Y       | N     | N           | N         | N        | N          | Y        |
| Workspace checkpoints      | Y       | N     | N           | N         | N        | N          | N        |
| Worktree workflows         | N       | N     | Y           | N         | N        | N          | N        |

### Must-Close

- Large context windows - has: Claude Code, Gemini CLI
- Open-source core - has: OpenCode, Codex CLI

### Should-Close

- Cost visibility - has: Claude Code
- Custom modes - has: OpenCode
- Image input - has: Codex CLI
- MCP support - has: Gemini CLI
- Multi-agent workflows - has: Codex CLI
- Plan mode - has: Gemini CLI
- Worktree workflows - has: Claude Code

### Nice-To-Have

- Auto-commits - has: Aider
- Autocomplete - has: Continue
- Context providers - has: Continue
- Custom models - has: Continue
- Git integration - has: Aider
- IDE integration - has: Continue
- Inline edits - has: Continue
- Repo map - has: Aider
- Voice input - has: Aider
