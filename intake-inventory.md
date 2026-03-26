# Intake Inventory

> **Project:** CruxCLI
> **Date:** 2026-03-24
> **Inventoried by:** Claude Opus 4.6

## Documentation

| # | File/Document | Location | Format | Template Match | Quality |
|---|---|---|---|---|---|
| 1 | README.md | /README.md | markdown | projects/code README | usable |
| 2 | AGENTS.md | /AGENTS.md | markdown | projects/code DEVELOPMENT.md | usable |
| 3 | CONTRIBUTING.md | /CONTRIBUTING.md | markdown | projects/code CONTRIBUTING.md | usable |
| 4 | SECURITY.md | /SECURITY.md | markdown | projects/code SECURITY.md | usable |
| 5 | ROADMAP.md | /ROADMAP.md | markdown | product ROADMAP | usable |
| 6 | COMPETITORS.md | /docs/COMPETITORS.md | markdown | projects/business COMPETITIVE_ANALYSIS | usable |
| 7 | MEMORY_ARCHITECTURE_REPORT.md | /docs/ | markdown | research (analysis report) | usable |
| 8 | RECALLABLE_KNOWLEDGE_ANALYSIS.md | /docs/ | markdown | research (analysis report) | usable |
| 9 | SESSION_MIGRATION_PLAN.md | /docs/ | markdown | projects/code MIGRATION.md | usable |
| 10 | BUILD_PLAN_001_HARD_FORK.md | / | markdown | plans/ (build plan) | usable |
| 11 | BUILD_PLAN_003_WORKSPACE_CHECKPOINTS.md | / | markdown | plans/ (build plan) | usable |
| 12 | BUILD_PLAN_004_VSCODE_EXTENSION.md | / | markdown | plans/ (build plan) | usable |
| 13 | SYSTEM_PROMPT_GUIDE.md | / | markdown | projects/code CONFIGURATION.md | reference-only |
| 14 | LIGHTWEIGHT_PROMPT_PLAN.md | / | markdown | plans/ (build plan) | reference-only |
| 15 | STATS.md | / | markdown | -- | reference-only |
| 16 | specs/project.md | /specs/ | markdown | product PRD | reference-only |
| 17 | PR template | /.github/pull_request_template.md | markdown | projects/code CONTRIBUTING | usable |
| 18 | GitHub Action README | /github/README.md | markdown | projects/code docs | usable |
| 19 | LICENSE | /LICENSE | text | legal LICENSE | usable |

## Source Code (not documents — just noting existence)

| # | Package | Path | Purpose |
|---|---|---|---|
| 1 | opencode (core CLI) | packages/cruxcli/ | Core CLI engine |
| 2 | plugin | packages/plugin/ | Plugin SDK |
| 3 | sdk | packages/sdk/ | Client SDK |
| 4 | util | packages/util/ | Shared utilities |
| 5 | script | packages/script/ | Build scripts |
| 6 | app | packages/app/ | Web dashboard |
| 7 | web | packages/web/ | Marketing site |
| 8 | desktop | packages/desktop/ | Tauri desktop app |
| 9 | desktop-electron | packages/desktop-electron/ | Electron desktop app |
| 10 | ui | packages/ui/ | Shared SolidJS components |
| 11 | vscode extension | sdks/vscode/ | VS Code extension |

## CI/CD

| # | Workflow | Path | Status |
|---|---|---|---|
| 1 | publish.yml | .github/workflows/ | Rebranded, functional |
| 2 | test.yml | .github/workflows/ | Functional |
| 3 | typecheck.yml | .github/workflows/ | Functional |
| 4 | publish-vscode.yml | .github/workflows/ | Rebranded, needs secrets |
| 5 | sign-cli.yml | .github/workflows/ | Rebranded |
| 6 | 27 other workflows | .github/workflows/ | Inherited from upstream, need review |

## Configuration

| # | File | Purpose |
|---|---|---|
| 1 | package.json | Root monorepo config |
| 2 | turbo.json | Turborepo pipeline |
| 3 | tsconfig.json | TypeScript config |
| 4 | sst.config.ts | SST infrastructure |
| 5 | .mcp.json | MCP server config (crux + cruxdev) |

## Missing (to be captured in GAPS.md)

- No ARCHITECTURE.md
- No API.md
- No CONFIGURATION.md (for end users)
- No DEPLOYMENT.md
- No TESTING.md
- No CHANGELOG.md
- No USER_GUIDE.md
- No CHARTER.md (domain level)
- No STRATEGY.md (domain level)
- No product PRD (specs/project.md is reference-only)
