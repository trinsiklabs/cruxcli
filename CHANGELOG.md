# Changelog

All notable changes to CruxCLI are documented in this file.

## [Unreleased]

### Added
- **Workspace Checkpoints** — `cruxcli checkpoint` command with create/list/restore/remove/diff. Auto-checkpoint before destructive tool calls (edit, write, bash, apply_patch). Configurable via `CRUXCLI_DISABLE_AUTO_CHECKPOINT`.
- **VS Code Extension** — Status bar integration, send selection/file to CruxCLI, right-click context menus, explorer "Open in CruxCLI", binary detection with install link, `cruxcli.binaryPath` setting.
- **Competitor tracking** — `docs/COMPETITORS.md` with 4 official competitors and feature matrix.
- **Architecture documentation** — `docs/ARCHITECTURE.md` covering all subsystems.

### Fixed
- Binary build failing silently due to bunfs path resolving through `.bun` cache — `realpathSync` produced `../../` paths that Bun's JSON parser treated as comments.
- Added build error reporting — `Bun.build()` failures now logged and exit non-zero.
- Tool registry gracefully handles failed custom tool imports (try/catch + warning log).
- Token budget division by zero guard when budget is 0.
- Postinstall script `main()` now properly awaited.

### Changed
- Complete org rebrand: `anomalyco` → `trinsiklabs` across 159+ files.
- CI/CD workflows updated: 4 repo guard conditions, removed obsolete `opencode.yml`.
- Install script, postinstall, and bin wrapper rebranded to CruxCLI.
- VS Code extension: publisher `trinsiklabs`, category `AI`, ESLint aligned to no-semicolons.

## [0.1.0] — 2026-03-18

### Added
- Hard fork from OpenCode — clean break, fresh git history.
- Rebrand: opencode → cruxcli (binary, config, env vars, package names).
- Crux mode prompt injection native in `prompt.ts`.
- Mode→model tier mapping for automatic model selection.
- Bridge plugin absorbed into native source (temperature/topP per mode, session context).
- Token budget system replacing step-count limits.
- Binary compilation verified across all platforms.

## [0.0.1] — 2026-03-06

### Added
- Initial commit: CruxCLI bridge plugin and config-layer distribution.
