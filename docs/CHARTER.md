# CruxCLI Domain Charter

**Domain type:** Key
**Owner:** trinsiklabs
**Created:** 2026-03-24

---

## 1. Purpose

CruxCLI is an open-source, provider-agnostic AI coding agent for the terminal. It exists to give developers a single CLI tool that works with any LLM provider while delivering intelligence features (mode-driven prompts, token budgets, correction detection) that generic agents lack.

## 2. Scope

### In scope

- Terminal UI and client/server architecture for AI-assisted coding
- Mode system: 24 task-specific modes with model tier mapping and token budgets
- Provider-agnostic LLM integration (Anthropic, OpenAI, Google, local models)
- LSP integration (30+ language servers)
- Plugin API and MCP tool integration
- Desktop app (Tauri/Electron) and VS Code extension
- Workspace checkpoints (git worktree-based snapshotting)
- Bun-compiled standalone binary distribution
- Marketing site (`packages/web/`)

### Out of scope

- The Crux intelligence platform itself (modes, knowledge, sessions, correction detection) — lives in the Crux repo
- The CruxDev convergence engine (autonomous audit-fix loops) — lives in the CruxDev repo
- Browser automation, linting, formatting — integrated via MCP servers, not built in
- Upstream OpenCode maintenance or rebase relationship

## 3. Ownership

| Role | Entity |
|------|--------|
| Organization | trinsiklabs |
| Repository | github.com/trinsiklabs/cruxcli |
| Structure | Monorepo, 19 packages |
| Core package | `packages/opencode/` |

## 4. Relationship to Crux Ecosystem

The Crux ecosystem has three components:

| Component | Role | Repo |
|-----------|------|------|
| **Crux** | Intelligence platform — modes, knowledge base, sessions, correction detection, safety pipeline | Separate repo |
| **CruxDev** | Convergence engine — autonomous audit-fix loops driving code to verified completion | Separate repo |
| **CruxCLI** | Terminal agent — the user-facing surface that consumes Crux intelligence and can be driven by CruxDev | This repo |

CruxCLI consumes Crux via MCP. The Crux intelligence layer (mode prompts, model tier mapping, token budgets) is baked into the CruxCLI binary at build time. CruxDev orchestrates CruxCLI sessions but does not live in this repo.

## 5. Key Decisions

| Decision | Rationale |
|----------|-----------|
| **Hard fork from OpenCode** | Clean break. No rebase relationship maintained. Monitor upstream for ideas, integrate selectively. |
| **Provider-agnostic** | Not coupled to any single LLM vendor. Models converge in capability over time; lock-in is a liability. |
| **Bun runtime (Bun-only)** | Faster compilation, smaller binaries. Intentionally does not support Node.js alongside Bun. |
| **Mode system with model tier mapping** | 24 modes map tasks to appropriate model tiers automatically. Replaces generic prompting with task-optimized intelligence. |
| **Token budgets over step-count limits** | Per-mode token budgets give finer cost control than counting tool-call steps. |
| **Client/server architecture** | Enables remote driving (e.g., mobile app controlling a local CruxCLI session). TUI is one client among many. |
| **Integrate, don't rebuild** | Browser automation, linting, formatting use existing MCP servers. Crux modes point agents at the right tools. |

## 6. Success Criteria

| Metric | Target |
|--------|--------|
| Binary ships and works end-to-end | Gate for all other work |
| Provider coverage | Works with Anthropic, OpenAI, Google, and at least one local model runtime |
| Mode system active | All 24 modes functional with correct model tier mapping |
| Token budget enforcement | Per-mode budgets enforced, replacing step-count limits |
| Competitive parity | Close "should-close" gaps from COMPETITORS.md (repo map, cost visibility, image input) |
| Community adoption | Public launch, growing user base, active Discord |
| CruxDev integration | CruxDev can drive CruxCLI sessions through convergence loops |

## 7. Domain Boundaries

| Belongs in CruxCLI | Belongs in Crux | Belongs in CruxDev |
|---------------------|-----------------|---------------------|
| TUI rendering, keybindings, terminal I/O | Mode definitions and prompt content | Convergence engine logic |
| LLM provider adapters and routing | Knowledge base and correction detection | Audit-fix loop orchestration |
| Tool execution (file, bash, LSP) | Safety pipeline (5-gate system) | Plan validation and template system |
| Token budget enforcement | Session state and context management | Multi-agent workflow coordination |
| Plugin API and MCP client | Model tier recommendations | Rollback and checkpoint policies |
| Desktop app and VS Code extension | Cross-project digest and analytics | Termination criteria |
| Build, packaging, distribution | — | — |
