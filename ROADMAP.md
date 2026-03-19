# CruxCLI Roadmap

**Last Updated:** 2026-03-19

## Now: Ship the Binary

CruxCLI Phases 3-6 from BUILD_PLAN_001_HARD_FORK.md. Everything else waits until the binary ships.

| Phase | What | Status |
|-------|------|--------|
| Phase 1: Fork + Strip | Copy OpenCode, remove dead packages | Done |
| Phase 2: Rebrand | opencode → cruxcli everywhere | Done |
| Phase 3: Prompt Replacement | Replace 6 prompt injection points with Crux mode-driven prompts | Done |
| Phase 4: Bridge Absorption | Move crux-bridge.js hooks into native source | Done |
| Phase 5: Token Budget | Replace step-count limits with per-mode token budgets | Done |
| Phase 6: Build + Verify | Binary compiles, tests pass, E2E verified | Done |

## Next: Competitive Gaps

Prioritized by impact. None of these start until the binary ships.

### 1. Repo/AST Impact Analysis

**Gap:** Aider's repo map proactively selects relevant files for a task. CruxCLI has LSP (30+ servers) but no proactive "given this task, which files matter?" capability.

**Approach:** Build as a Crux MCP tool (`analyze_impact`) rather than CruxCLI-specific. Uses LSP symbol data + git history to rank files by relevance to a prompt. Works across any agent connected to Crux, not just CruxCLI.

**Effort:** Medium. LSP data is already flowing; the work is ranking and context selection.

### 2. Workspace Checkpoints

**Gap:** No automatic snapshotting before risky operations. Can't roll back to a known-good state.

**Approach:** CruxCLI already has git worktree support. Add automatic checkpoint creation before convergence rounds (CruxDev engine already specs rollback). Add a `cruxcli checkpoint` command that creates a lightweight git stash or tagged commit. Low effort, high trust signal for users.

**Effort:** Low. Plumbing exists (worktree.ts), just needs orchestration.

### 3. VS Code Native Experience

**Gap:** No polished VS Code extension. Users expect to stay in their editor.

**Approach:** `sdks/vscode/` already has an extension that launches the binary and connects to its server. The plumbing exists — the gap is polish, keybindings, inline diff display, and distribution via VS Code marketplace. Becomes relevant after the binary ships and stabilizes.

**Effort:** Medium. Mostly UX work, not infrastructure.

### 4. Browser Automation

**Gap:** No Playwright/Puppeteer integration for testing UIs or scraping docs.

**Approach:** Don't build — integrate. Playwright MCP servers already exist. Add a Crux "frontend" mode that knows to suggest connecting browser MCP tools. Crux's mode system is the integration point, not custom browser code.

**Effort:** Low. Mode definition + documentation only.

### 5. Enterprise Compliance Tier

**Gap:** No audit trail export, SSO/SAML, role-based mode restrictions, approved-model-only policies.

**Approach:** Building blocks exist (Crux 5-gate safety pipeline, correction logging, mode-based guardrails). Enterprise tier adds config/policy layers on top: audit trail export, SSO integration, role-based mode access, model allowlists. Don't build until enterprise demand exists.

**Effort:** High. Business decision, not just engineering.

## Later: CruxDev Engine

The deterministic convergence engine (BUILD_PLAN_001_DETERMINISTIC_ENGINE.md, 80 checkboxes across 7 phases). This is the product that replaces "human says do it again" with "code drives convergence to termination." Tracked separately in the CruxDev repo.

## Non-Goals

- **Upstream sync with OpenCode.** Clean break. Monitor for good ideas, integrate selectively, never maintain a rebase relationship.
- **Building what can be integrated.** Browser automation, linting, formatting — these have MCP servers. Crux's mode system points agents at the right tools. Don't rebuild.
- **Features before shipping.** Every gap above is a distraction until the binary works end-to-end.
