# CruxCLI Roadmap

**Last Updated:** 2026-03-24

## Completed: Ship the Binary

CruxCLI Phases 1-6 from BUILD_PLAN_001_HARD_FORK.md are complete. The `cruxcli` binary compiles and runs.

| Phase | What | Status |
|-------|------|--------|
| Phase 1: Fork + Strip | Copy OpenCode, remove dead packages | Done |
| Phase 2: Rebrand | opencode -> cruxcli everywhere | Done |
| Phase 3: Prompt Replacement | Replace 6 prompt injection points with Crux mode-driven prompts | Done |
| Phase 4: Bridge Absorption | Move crux-bridge.js hooks into native source | Done |
| Phase 5: Token Budget | Replace step-count limits with per-mode token budgets | Done |
| Phase 6: Build + Verify | Binary compiles, tests pass, E2E verified | Done |

## Completed: Competitive Gaps 1-3

| Gap | What | Status |
|-----|------|--------|
| 1. Repo/AST Impact Analysis | `analyze_impact` MCP tool using LSP + git history to rank files by relevance | Done |
| 2. Workspace Checkpoints | Automatic snapshotting before convergence rounds, `cruxcli checkpoint` command | Done |
| 3. VS Code Native Experience | Extension in `sdks/vscode/` with keybindings, inline diff, marketplace distribution | Done |

## Next: Key Migration

Priority work now that the binary ships and competitive gaps 1-3 are closed.

### API Key Migration

Migrate from environment variable-based API key management to a secure credential store. Current state requires users to set `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, etc. in their shell profile. Target: `cruxcli auth` command that stores credentials in the OS keychain (macOS Keychain, Linux libsecret, Windows Credential Manager).

### Plugin Ecosystem

Formalize the plugin API. The `@cruxcli/plugin` package exists but the contract is underdocumented. Publish plugin authoring guide, register plugins via `cruxcli plugin add`, and support discovery through a plugin registry.

### CruxDev Integration Hardening

The CruxDev convergence engine connects via MCP. Harden the integration: structured error reporting, convergence state persistence across restarts, and progress visualization in the TUI.

## Open Competitive Gaps

### 4. Browser Automation

**Gap:** No Playwright/Puppeteer integration for testing UIs or scraping docs.

**Approach:** Don't build -- integrate. Playwright MCP servers already exist. Add a Crux "frontend" mode that knows to suggest connecting browser MCP tools. Crux's mode system is the integration point, not custom browser code.

**Effort:** Low. Mode definition + documentation only.

### 5. Enterprise Compliance Tier

**Gap:** No audit trail export, SSO/SAML, role-based mode restrictions, approved-model-only policies.

**Approach:** Building blocks exist (Crux 5-gate safety pipeline, correction logging, mode-based guardrails). Enterprise tier adds config/policy layers on top: audit trail export, SSO integration, role-based mode access, model allowlists. Don't build until enterprise demand exists.

**Effort:** High. Business decision, not just engineering.

## Later: CruxDev Engine

The deterministic convergence engine (BUILD_PLAN_001_DETERMINISTIC_ENGINE.md, 80 checkboxes across 7 phases). This is the product that replaces "human says do it again" with "code drives convergence to termination." Tracked separately in the CruxDev repo.

## Non-Goals

- **Upstream sync with OpenCode.** Clean break. Monitor for good ideas, integrate selectively, never maintain a rebase relationship.
- **Building what can be integrated.** Browser automation, linting, formatting -- these have MCP servers. Crux's mode system points agents at the right tools. Don't rebuild.
- **Features before shipping.** Every gap above is a distraction until the binary works end-to-end.
