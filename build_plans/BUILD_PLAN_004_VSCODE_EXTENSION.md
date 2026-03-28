# BUILD_PLAN_004: VS Code Extension Polish + Publish

**Created:** 2026-03-23
**Status:** CONVERGED
**Goal:** Fix branding, add status bar + UX improvements, and publish the CruxCLI VS Code extension to the marketplace.

**Constraint:** Keep the thin terminal-based architecture — no webviews or heavy UI.
**Constraint:** Must work without CruxCLI installed (graceful error message).
**Rule:** TDD. Tests before code.
**Rule:** Two consecutive clean passes = convergence.

## Document Alignment

- `AGENTS.md` — coding style
- `ROADMAP.md` — defines this as competitive gap #3

---

## Phase 1: Branding + Config Fixes

**Purpose:** Fix all OpenCode/SST references, update publisher, fix publish script.

### Checklist — Phase 1

- [x] 1.1 Update `package.json`: publisher from `sst-dev` to `trinsiklabs`
- [x] 1.2 Update `package.json`: displayName to `CruxCLI`
- [x] 1.3 Update `package.json`: description to something compelling
- [x] 1.4 Update `package.json`: category from `Other` to `AI`
- [x] 1.5 Fix `script/publish`: output filename from `opencode.vsix` to `cruxcli.vsix`
- [x] 1.6 Verify image symlinks resolve (icon.png, button SVGs)
- [x] 1.7 Update README with CruxCLI branding, screenshots placeholder
- [x] 1.8 No remaining `opencode` or `sst-dev` references in sdks/vscode/

---

## Phase 2: Status Bar Integration

**Purpose:** Show CruxCLI status in VS Code's status bar.

### Checklist — Phase 2

- [x] 2.1 Add status bar item that shows when CruxCLI terminal is active
- [x] 2.2 Status bar shows "CruxCLI" with icon, click opens/focuses terminal
- [x] 2.3 Status bar hides when no CruxCLI terminal exists
- [x] 2.4 Track terminal lifecycle (onDidOpenTerminal, onDidCloseTerminal)

---

## Phase 3: Enhanced Context Sharing

**Purpose:** Make it easier to share context from VS Code to CruxCLI.

### Checklist — Phase 3

- [x] 3.1 "Send Selection to CruxCLI" command — sends selected code as a message
- [x] 3.2 "Send File to CruxCLI" command — sends full file content as context
- [x] 3.3 Right-click context menu entries for both commands
- [x] 3.4 Explorer context menu: "Open in CruxCLI" for folders
- [x] 3.5 Keybinding for send selection: `Cmd+Shift+K` / `Ctrl+Shift+K`

---

## Phase 4: Graceful Binary Detection

**Purpose:** Handle the case where CruxCLI binary isn't installed.

### Checklist — Phase 4

- [x] 4.1 On activation, check if `cruxcli` is in PATH
- [x] 4.2 If not found, show info message with install link
- [x] 4.3 Add `cruxcli.binaryPath` setting for custom binary location
- [x] 4.4 Respect setting when launching terminal

---

## Phase 5: Publish Pipeline

**Purpose:** Get the extension publishable to VS Code Marketplace and Open VSX.

### Checklist — Phase 5

- [x] 5.1 `bun run package` produces valid .vsix
- [x] 5.2 Extension installs and activates in clean VS Code
- [x] 5.3 All 3 commands work (open, new tab, file reference)
- [x] 5.4 Status bar appears when terminal is active
- [x] 5.5 Publish script uses correct filename and tokens
- [x] 5.6 CI workflow (`publish-vscode.yml`) has correct paths

---

## Test Commands

```bash
cd sdks/vscode && bun run compile && bun run lint
```

## Convergence Criteria

- All checklist items complete
- Extension compiles without errors
- Extension installs in VS Code
- Two consecutive clean audit passes
