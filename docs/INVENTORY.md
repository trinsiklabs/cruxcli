# CruxCLI Domain Inventory

**Last Updated:** 2026-03-24

This is the complete index of everything in the CruxCLI monorepo.

---

## Packages

### Core Packages

| Package | Path | Name | Description |
|---------|------|------|-------------|
| opencode | `packages/opencode/` | `cruxcli` | Core CLI, server, session engine, provider integration, tool system. The main binary. |
| app | `packages/app/` | `@cruxcli/app` | SolidJS web frontend (connects to server over HTTP/SSE) |
| ui | `packages/ui/` | `@cruxcli/ui` | Shared UI component library (SolidJS) |
| desktop | `packages/desktop/` | `@cruxcli/desktop` | Tauri desktop wrapper |
| desktop-electron | `packages/desktop-electron/` | `@cruxcli/desktop-electron` | Electron desktop wrapper |
| web | `packages/web/` | `@cruxcli/web` | Marketing site / web deployment |
| storybook | `packages/storybook/` | `@cruxcli/storybook` | Component storybook |

### Platform Packages

| Package | Path | Name | Description |
|---------|------|------|-------------|
| plugin | `packages/plugin/` | `@cruxcli/plugin` | Plugin API types and interfaces |
| sdk (JS) | `packages/sdk/js/` | `@cruxcli/sdk` | TypeScript SDK for the CruxCLI server API (auto-generated from OpenAPI) |
| util | `packages/util/` | `@cruxcli/util` | Shared utilities (error types, slug generation) |
| script | `packages/script/` | `@cruxcli/script` | Build and release scripts |

### Infrastructure Packages

| Package | Path | Name | Description |
|---------|------|------|-------------|
| function | `packages/function/` | `@cruxcli/function` | Serverless functions |
| enterprise | `packages/enterprise/` | `@cruxcli/enterprise` | Enterprise features |
| slack | `packages/slack/` | `@cruxcli/slack` | Slack integration |
| containers | `packages/containers/` | — | Container definitions (Docker) |
| docs | `packages/docs/` | — | Documentation site package |
| extensions | `packages/extensions/` | — | IDE extensions (parent directory) |

### Console Packages (`packages/console/*`)

| Package | Path | Description |
|---------|------|-------------|
| console/app | `packages/console/app/` | Console web application |
| console/core | `packages/console/core/` | Console business logic |
| console/function | `packages/console/function/` | Console serverless functions |
| console/mail | `packages/console/mail/` | Email templates |
| console/resource | `packages/console/resource/` | SST infrastructure resources |

**Total packages: 19** (13 top-level + 5 console + 1 SDK/JS)

---

## Extensions

| Extension | Path | Description |
|-----------|------|-------------|
| VS Code | `sdks/vscode/` | VS Code extension |
| Zed | `packages/extensions/zed/` | Zed editor extension (`extension.toml` + icon) |

---

## CI Workflows (`.github/workflows/`)

### Build & Release

| Workflow | File | Description |
|----------|------|-------------|
| Publish | `publish.yml` | Main release pipeline (npm, Homebrew, AUR, Docker) |
| Beta | `beta.yml` | Beta channel releases |
| Sign CLI | `sign-cli.yml` | Binary signing via SignPath |
| Containers | `containers.yml` | Docker image builds |
| Deploy | `deploy.yml` | Infrastructure deployment |
| Publish VS Code | `publish-vscode.yml` | VS Code extension publishing |
| Publish GitHub Action | `publish-github-action.yml` | GitHub Action release |
| Release GitHub Action | `release-github-action.yml` | GitHub Action versioning |

### Testing & Quality

| Workflow | File | Description |
|----------|------|-------------|
| Test | `test.yml` | Test suite |
| Typecheck | `typecheck.yml` | TypeScript type checking |
| Review | `review.yml` | Code review automation |
| Nix Eval | `nix-eval.yml` | Nix expression evaluation |
| Nix Hashes | `nix-hashes.yml` | Nix hash verification |
| Generate | `generate.yml` | Code generation checks |

### PR & Issue Management

| Workflow | File | Description |
|----------|------|-------------|
| PR Standards | `pr-standards.yml` | PR formatting/standards enforcement |
| PR Management | `pr-management.yml` | PR lifecycle automation |
| Close Stale PRs | `close-stale-prs.yml` | Auto-close stale PRs |
| Triage | `triage.yml` | Issue triage automation |
| Stale Issues | `stale-issues.yml` | Stale issue management |
| Duplicate Issues | `duplicate-issues.yml` | Duplicate issue detection |
| Compliance Close | `compliance-close.yml` | Compliance-related issue closing |

### Community & Notifications

| Workflow | File | Description |
|----------|------|-------------|
| Notify Discord | `notify-discord.yml` | Discord notifications |
| Daily Issues Recap | `daily-issues-recap.yml` | Daily issue summary |
| Daily PR Recap | `daily-pr-recap.yml` | Daily PR summary |
| Stats | `stats.yml` | Repository statistics |

### Vouch System

| Workflow | File | Description |
|----------|------|-------------|
| Vouch Manage by Issue | `vouch-manage-by-issue.yml` | Vouch management via issues |
| Vouch Check Issue | `vouch-check-issue.yml` | Issue vouch verification |
| Vouch Check PR | `vouch-check-pr.yml` | PR vouch verification |

### Documentation

| Workflow | File | Description |
|----------|------|-------------|
| Docs Update | `docs-update.yml` | Documentation updates |
| Docs Locale Sync | `docs-locale-sync.yml` | Documentation translation sync |
| Sync Zed Extension | `sync-zed-extension.yml` | Zed extension sync |

**Total workflows: 31**

---

## Build Plans

Build plans are referenced in COMPETITORS.md and live in the Crux repo:

| Plan | Description | Status |
|------|-------------|--------|
| BUILD_PLAN_002 | Repo/AST impact analysis | Plan written |

---

## Documentation (`docs/`)

| Document | Description |
|----------|-------------|
| `ARCHITECTURE.md` | System architecture and subsystem documentation |
| `CHARTER.md` | Domain charter — purpose, scope, ownership, boundaries |
| `COMPETITORS.md` | Competitive analysis with feature matrix |
| `DEPLOYMENT.md` | Build, release, and installation guide |
| `USER_GUIDE.md` | End-user guide |
| `MEMORY_ARCHITECTURE_REPORT.md` | Memory architecture analysis |
| `SESSION_MIGRATION_PLAN.md` | Session migration planning |
| `RECALLABLE_KNOWLEDGE_ANALYSIS.md` | Knowledge system analysis |
| `STRATEGY.md` | Strategic positioning and growth plan |
| `INVENTORY.md` | This file — domain inventory |
| `PRD.md` | Product requirements document |
| `SCHEMA.md` | Database schema documentation |
| `TROUBLESHOOTING.md` | Common issues and fixes |
| `ADR.md` | Architectural Decision Records |
| `OPERATIONS.md` | Operational runbooks |
| `MONITORING.md` | Monitoring guide |
| `PERFORMANCE.md` | Performance characteristics |
| `HEALTH_REPORT.md` | Domain health snapshot |

**Total documentation files: 18**
