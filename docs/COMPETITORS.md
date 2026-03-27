# CruxCLI — Competitors

**Last Updated:** 2026-03-27
**Project:** CruxCLI
**Lane:** Terminal AI coding agent

---

## Official Competitors (Actively Tracked)

### OpenCode

- **URL:** https://opencode.ai
- **GitHub:** https://github.com/anomalyco/opencode (131,408 stars)
- **Category:** Direct (upstream fork source)
- **License:** MIT
- **Latest:** v1.3.3 (2026-03-26)
- **One-line:** The most TUI-native terminal coding agent — client/server architecture, LSP support, plugin API.

**Strengths:**

- Massive community (800+ contributors, 5M+ monthly developers)
- Multi-surface: terminal, desktop app, VS Code extension
- 75+ LLM providers out of the box
- Near-daily release cadence (737+ releases)
- GitLab Agent Platform integration (v1.3.0)
- ACP (Agent Communication Protocol) emerging

**Weaknesses:**

- No intelligence layer — prompts are generic, not mode-optimized
- No correction detection or continuous learning
- No convergence methodology — relies on user judgment for "done"
- No token budget system — step-count limits only

**Our moat vs them:**

- Crux intelligence layer native in binary (not addon)
- 24 research-optimized mode prompts
- Token budget system replacing step-count limits
- Workspace checkpoints (auto-snapshot before destructive ops)
- CruxDev convergence engine integration

**Their moat vs us:**

- Community size (131k stars vs our 0) — must-close via adoption/marketing
- GitLab integration — should-close
- Desktop app polish — already have the code, needs polish
- Node.js runtime support alongside Bun — intentional gap (we're Bun-only)

---

### Claude Code

- **URL:** https://claude.ai/claude-code
- **GitHub:** https://github.com/anthropics/claude-code (83,536 stars)
- **Category:** Direct
- **License:** Proprietary
- **Latest:** v2.1.85 (2026-03-26)
- **One-line:** Anthropic's first-party CLI agent with Opus 4.6 and 1M context.

**Strengths:**

- First-party Opus 4.6 access with 1M context window
- 64k/128k output token limits
- Built-in worktree support, cron scheduling
- Real-time cost visibility
- Backed by Anthropic — updates first when new models ship

**Weaknesses:**

- Proprietary — not forkable or self-hostable
- Coupled to Anthropic models only
- No mode system — single personality
- No convergence methodology
- No plugin API

**Our moat vs them:**

- Open source, provider-agnostic
- Mode system with model tier mapping
- Plugin API + MCP integration
- CruxDev convergence engine
- Self-hostable

**Their moat vs us:**

- First-party model access — intentional gap (we're provider-agnostic)
- 1M context window — should-close (leverage via provider support)
- Cost visibility — should-close
- Brand recognition — must-close via differentiation

---

### Gemini CLI

- **URL:** https://github.com/google-gemini/gemini-cli
- **GitHub:** https://github.com/google-gemini/gemini-cli (99,282 stars)
- **Category:** Direct
- **License:** Apache-2.0
- **Latest:** v0.35.2 (2026-03-26)
- **One-line:** Google's terminal agent with Gemini 3, 1M context, Google Search grounding.

**Strengths:**

- 99k stars — massive adoption in 2 months
- Generous free tier (Gemini models)
- Google Search grounding for real-time info
- 1M context window
- Plan Mode (added 2026-03-11)
- MCP support

**Weaknesses:**

- Coupled to Google/Gemini models
- New — less mature than OpenCode or Aider
- No plugin API beyond MCP
- No custom modes system
- No convergence methodology

**Our moat vs them:**

- Provider-agnostic (any model)
- Deep mode system with 24 modes
- Plugin API + custom tools
- CruxDev convergence engine
- Workspace checkpoints

**Their moat vs us:**

- Free tier with capable models — should-close (support Gemini as provider)
- Google Search grounding — nice-to-have (browser automation mode covers this)
- Community size — must-close via adoption

---

### Codex CLI

- **URL:** https://github.com/openai/codex
- **GitHub:** https://github.com/openai/codex (67,984 stars)
- **Category:** Direct
- **License:** Apache-2.0
- **Latest:** rust-v0.117.0 (2026-03-26)
- **One-line:** OpenAI's Rust-based terminal agent with o3/o4-mini, multi-agent workflows.

**Strengths:**

- Rust-based (fast, low memory)
- Multi-agent workflows
- Screenshot/image input
- Backed by OpenAI

**Weaknesses:**

- Coupled to OpenAI models
- Newer, less ecosystem than OpenCode
- No LSP integration
- No plugin API

**Our moat vs them:**

- Provider-agnostic
- LSP integration (30+ servers)
- Plugin API, custom modes
- Client/server architecture

**Their moat vs us:**

- Rust performance — nice-to-have (Bun compilation is fast enough)
- Multi-agent workflows — should-close (subagent support exists, needs polish)
- Image input — should-close

---

## Watch List

| Name     | URL                            | Stars  | Why watching                                                                                                    |
| -------- | ------------------------------ | ------ | --------------------------------------------------------------------------------------------------------------- |
| Aider    | github.com/Aider-AI/aider      | 42,441 | Pioneer terminal agent, repo map concept. No release in 7+ months — may be stalling or preparing major version. |
| Cline    | github.com/cline/cline         | 59,506 | IDE-bound (VS Code) but influences user expectations. Plan/Act modes, MCP integration.                          |
| Roo Code | github.com/RooCodeInc/Roo-Code | 22,857 | Custom modes system closest to Crux's. Mode Gallery for community sharing.                                      |
| Goose    | github.com/block/goose         | 33,667 | Block (Square) backed. Extensible, any LLM, runs locally.                                                       |

---

## Feature Matrix

| Feature                    |      CruxCLI       | OpenCode | Claude Code  | Gemini CLI | Codex CLI |  Aider  |
| -------------------------- | :----------------: | :------: | :----------: | :--------: | :-------: | :-----: |
| Open source                |         ✓          |    ✓     |      —       |     ✓      |     ✓     |    ✓    |
| Provider-agnostic          |         ✓          |    ✓     |      —       |     —      |     —     |    ✓    |
| TUI interface              |         ✓          |    ✓     |      ✓       |     ✓      |     ✓     |    ✓    |
| Client/server arch         |         ✓          |    ✓     |      —       |     —      |     —     |    —    |
| LSP integration            |         ✓          |    ✓     |      —       |     —      |     —     |    —    |
| Plugin API                 |         ✓          |    ✓     |      —       |     —      |     —     |    —    |
| Custom modes               |         ✓          |    ✓     |      —       |     —      |     —     |    —    |
| Mode→model tier mapping    |         ✓          |    —     |      —       |     —      |     —     |    —    |
| Token budget system        |         ✓          |    —     |      —       |     —      |     —     |    —    |
| Workspace checkpoints      |         ✓          |    —     | ✓ (worktree) |     —      |     —     | ✓ (git) |
| Convergence engine         |    ✓ (CruxDev)     |    —     |      —       |     —      |     —     |    —    |
| Correction detection       |      ✓ (Crux)      |    —     |      —       |     —      |     —     |    —    |
| Repo map / impact analysis |    — (planned)     |    —     |      —       |     —      |     —     |    ✓    |
| Desktop app                | ✓ (Tauri+Electron) |    ✓     |      —       |     —      |     —     |    —    |
| VS Code extension          |         ✓          |    ✓     |      ✓       |     —      |     —     |    —    |
| Image/screenshot input     |         —          |    —     |      —       |     —      |     ✓     |    —    |
| Free model tier            |         —          | ✓ (Zen)  |      —       |     ✓      |     —     |    —    |
| Cost visibility            |         —          |    —     |      ✓       |     —      |     —     |    —    |
| Multi-agent workflows      |         —          |    —     |      ✓       |     —      |     ✓     |    —    |

---

## Gap Closure Queue

| Gap                      | Competitor(s)          | Classification | Build Plan     | Status                     |
| ------------------------ | ---------------------- | -------------- | -------------- | -------------------------- |
| Repo/AST impact analysis | Aider                  | Should close   | BUILD_PLAN_002 | Plan written, in Crux repo |
| Cost visibility          | Claude Code            | Should close   | —              | Not started                |
| Free model tier          | OpenCode, Gemini CLI   | Should close   | —              | Not started                |
| Image/screenshot input   | Codex CLI              | Should close   | —              | Not started                |
| Multi-agent workflows    | Claude Code, Codex CLI | Should close   | —              | Not started                |
| Community/adoption       | All                    | Must close     | —              | Marketing/launch needed    |

---

## Moat Inventory (Our Unique Advantages)

| Moat                       | Description                                         | Protect by                                        |
| -------------------------- | --------------------------------------------------- | ------------------------------------------------- |
| Mode→model tier mapping    | Automatic model selection per task type             | Expand mode library, improve tier recommendations |
| Token budget system        | Per-mode token budgets replacing step-count limits  | Refine thresholds, add per-session analytics      |
| CruxDev convergence engine | Autonomous audit-fix loops to verified completion   | Continue developing, showcase in docs             |
| Crux intelligence layer    | 24 modes, correction detection, continuous learning | Native in binary, not addon                       |
| Workspace checkpoints      | Auto-snapshot before destructive tool calls         | Already shipped                                   |
| Client/server + LSP        | Remote-drivable sessions with code intelligence     | Unique combination — promote heavily              |
