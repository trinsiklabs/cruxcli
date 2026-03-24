# CruxCLI Product Requirements Document

**Last Updated:** 2026-03-24

---

## Target Users

**Primary:** Developers who want an AI coding agent they control — choosing their own models, providers, and workflows rather than being locked into a single vendor.

**Segments:**
- **Power users** migrating from Claude Code, Gemini CLI, or Codex CLI who want provider flexibility.
- **OpenCode users** who want smarter mode/model selection and token cost control.
- **Team leads** who need consistent, auditable AI-assisted development workflows.
- **Enterprise developers** who require self-hosted, configurable AI tooling.

---

## Key Features

### 1. Mode System
24 task-specific modes with distinct prompts, tool configurations, and model tier mappings. Each mode optimizes the agent's behavior for a specific task type (e.g., code review, refactoring, debugging, documentation). Modes map to model tiers automatically — complex tasks get stronger models, routine tasks use cheaper ones.

### 2. Workspace Checkpoints
Automatic snapshots before destructive tool operations (edit, write, bash, patch). Up to 50 checkpoints stored per project. Users can restore to any checkpoint. Built on git tree hashing, not full file copies.

### 3. Provider-Agnostic LLM Integration
Works with 20+ providers out of the box: Anthropic, OpenAI, Google, Azure, Bedrock, Vertex, OpenRouter, xAI, Mistral, Groq, DeepInfra, Cerebras, Cohere, TogetherAI, Perplexity, Vercel, GitLab, GitHub Copilot, and more. Runtime model fetching from models.dev with offline fallback.

### 4. LSP Integration
Built-in Language Server Protocol client supporting 30+ language servers. Provides diagnostics and symbol lookup via the `codesearch` and `lsp` tools. Auto-detects appropriate servers per language.

### 5. MCP (Model Context Protocol)
Full MCP client supporting stdio, SSE, and StreamableHTTP transports. Connects to external tool servers configured in `cruxcli.json` or `.mcp.json`. Supports OAuth authentication.

### 6. Client/Server Architecture
CLI starts a local HTTP server (Hono-based, port 4096). Multiple frontends connect: TUI, web app, desktop app (Tauri/Electron), VS Code extension. Enables remote-drivable sessions (e.g., mobile controlling a local agent).

### 7. Plugin API
Plugins can contribute custom tools, hook into tool execution lifecycle, and extend provider authentication. Supports npm packages and built-in plugins (Codex auth, Copilot auth, GitLab auth).

### 8. Token Budget System
Per-mode token budgets replacing step-count limits. Configurable warning threshold (75%) and hard limit (90%). Finer cost control than counting tool-call steps.

### 9. Context Compaction
Automatic context window management. Detects overflow, prunes old tool call outputs, triggers summarization via secondary LLM call. Keeps sessions productive without manual intervention.

### 10. Skill System
Markdown-based skill files (`SKILL.md`) with frontmatter. Discovered from project and global directories. Loaded as context for the LLM, enabling reusable domain knowledge.

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Binary ships end-to-end | Gate for all other work | Build compiles, tests pass, binary runs |
| Provider coverage | 4+ providers working | Anthropic, OpenAI, Google, and at least one local runtime |
| Mode system active | 24/24 modes functional | Each mode resolves to correct model tier |
| Token budgets enforced | Per-mode limits active | Warning at 75%, hard stop at 90% |
| Checkpoint reliability | Zero data loss from auto-checkpoints | Restore works for all checkpoint entries |
| Test suite health | 1200+ tests passing | CI green on every merge |
| Typecheck clean | 13/13 packages pass | Turbo typecheck succeeds |
| Community adoption | Growing user base post-launch | Stars, installs, Discord members |
| CruxDev integration | Convergence loops work end-to-end | CruxDev can drive CruxCLI sessions |

---

## Non-Goals

| Non-Goal | Rationale |
|----------|-----------|
| **Node.js runtime support** | Bun-only is an intentional decision for faster compilation and smaller binaries. |
| **Built-in browser automation** | Integrated via MCP servers (e.g., Playwright), not rebuilt in core. |
| **Built-in linting/formatting** | Integrated via MCP servers and existing tools, not rebuilt. |
| **Upstream OpenCode rebase** | Hard fork — clean break. Monitor upstream for ideas, integrate selectively. |
| **Free hosted service** | CruxCLI is a local tool. Users bring their own API keys. |
| **IDE-first experience** | Terminal-first. VS Code and Zed extensions exist but are secondary surfaces. |
| **Multi-agent orchestration in core** | CruxDev handles autonomous multi-step workflows. CruxCLI is the agent surface. |
| **Custom model training** | CruxCLI uses existing models. Intelligence comes from the mode/prompt layer, not fine-tuning. |
