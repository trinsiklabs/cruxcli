# CruxCLI Strategy

**Last Updated:** 2026-03-24

---

## Market Positioning

CruxCLI is a **provider-agnostic terminal AI coding agent with an intelligence layer**. It occupies a unique position in the terminal agent space: it combines the open-source, multi-provider flexibility of OpenCode with a proprietary intelligence layer (Crux modes, model tier mapping, token budgets, correction detection) that no competitor offers.

The core thesis: LLM providers are converging in capability. Coupling to a single vendor (as Claude Code, Gemini CLI, and Codex CLI do) is a liability. The durable value is in the intelligence layer that sits above the model — the modes that select the right model for the right task, the token budgets that control cost, and the convergence engine that drives code to verified completion.

---

## Differentiation

### vs OpenCode (upstream fork source)
OpenCode is the most community-adopted terminal agent (129k stars, 800+ contributors). CruxCLI hard-forked from OpenCode and adds what it lacks:
- **Mode system with model tier mapping** — 24 task-specific modes that automatically select model tiers. OpenCode uses generic prompts.
- **Token budget system** — Per-mode token budgets replacing step-count limits.
- **Workspace checkpoints** — Auto-snapshot before destructive operations.
- **CruxDev convergence integration** — Autonomous audit-fix loops to verified completion.
- **Correction detection** — Native in binary, not addon.

### vs Claude Code (Anthropic)
Claude Code has first-party Opus 4.6 access and 1M context. CruxCLI counters with:
- **Open source and self-hostable** — Not locked to a vendor.
- **Provider-agnostic** — Use Anthropic, OpenAI, Google, or local models.
- **Plugin API and MCP integration** — Extensible tool ecosystem.
- **Mode system** — Task-specific intelligence vs single personality.

### vs Gemini CLI (Google)
Gemini CLI has massive adoption (98k stars) and a free tier. CruxCLI counters with:
- **Any model, any provider** — Not limited to Gemini.
- **Deep mode system** — 24 modes vs Gemini CLI's single Plan Mode.
- **Plugin API and custom tools** — Extensibility beyond MCP.
- **Client/server architecture** — Remote-drivable sessions.

### vs Codex CLI (OpenAI)
Codex CLI is Rust-based with multi-agent workflows. CruxCLI counters with:
- **Provider-agnostic** — Not limited to OpenAI models.
- **LSP integration** — 30+ language servers for code intelligence.
- **Plugin API and custom modes** — Deeper extensibility.
- **Client/server architecture** — TUI is one client among many.

---

## Growth Strategy

### Phase 1: Open Source Adoption
- Public launch with clear differentiation messaging.
- Target developers frustrated by vendor lock-in (Claude Code, Gemini CLI users).
- Target OpenCode power users who want smarter mode/model selection.
- Ship with comprehensive documentation and easy installation (curl, npm, Homebrew, AUR, Docker).

### Phase 2: Mode Ecosystem
- Expand the mode library beyond the initial 24 modes.
- Enable community mode contributions (similar to Roo Code's Mode Gallery).
- Mode marketplace for sharing task-specific configurations.
- Each mode is a distribution channel — developers discover CruxCLI through the mode that solves their specific problem.

### Phase 3: CruxDev Integration
- CruxDev convergence engine as the premium differentiator.
- Autonomous audit-fix loops that drive code to verified completion.
- Position CruxCLI as the agent surface, CruxDev as the autonomy engine.
- Enterprise customers get CruxDev; open source users get CruxCLI with manual convergence.

### Phase 4: Platform Effects
- Plugin ecosystem grows tool coverage without core team effort.
- SDK enables third-party integrations (VS Code, Zed, custom clients).
- Console platform for team management, analytics, and shared configurations.

---

## Near-Term Priorities

| Priority | Description | Status |
|----------|-------------|--------|
| Binary stability | Shipping, compiling, end-to-end functional | Done |
| Mode system | 24 modes with model tier mapping and token budgets | Done |
| Workspace checkpoints | Auto-snapshot before destructive operations | Done |
| Gap closure: repo/AST impact analysis | Aider-style repo map for better context selection | Plan written |
| Gap closure: cost visibility | Real-time token/cost display (parity with Claude Code) | Not started |
| Gap closure: free model tier | Support free-tier models (parity with OpenCode/Gemini CLI) | Not started |
| Gap closure: image/screenshot input | Visual input support (parity with Codex CLI) | Not started |
| Community launch | Public repo, Discord, marketing site | Pending |
| Documentation | Complete domain documentation suite | In progress |
