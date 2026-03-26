# CruxCLI Domain Health Report

**Snapshot Date:** 2026-03-24

---

## Summary

CruxCLI is in a healthy state. The binary compiles, all tests pass, all packages typecheck, and the five critical gaps identified during domain setup have been closed.

---

## Test Suite

| Metric | Value |
|--------|-------|
| Total tests passing | 1,204 |
| Test runner | Bun test |
| Test location | `packages/cruxcli/` |
| Known flaky tests | None identified |

Tests must be run from `packages/cruxcli/`, not the monorepo root.

---

## Type Checking

| Metric | Value |
|--------|-------|
| Packages checked | 13 / 13 |
| Tool | Turbo (`bun turbo typecheck`) |
| Core package checker | `tsgo` (TypeScript 7.0 native preview) |
| Status | All passing |

---

## Build

| Metric | Value |
|--------|-------|
| Binary compiles | Yes |
| Platform targets | 10 |
| Binary size | ~110 MB |
| Build tool | `Bun.build()` with `compile: true` |

---

## Critical Gaps Closed

Five critical gaps were identified and resolved during domain setup:

| # | Gap | Resolution |
|---|-----|-----------|
| 1 | Typecheck errors in `llm.ts` | Fixed token budget type imports and stream option types |
| 2 | Typecheck errors in `token-budget.ts` | Fixed type definitions for budget tracking |
| 3 | Mode-to-model tier mapping | Implemented in phase 3 — 24 modes with automatic tier selection |
| 4 | Bridge code absorption | Phase 4 — bridge module absorbed into native source |
| 5 | Token budget system | Phase 5 — replaced step-count limits with per-mode token budgets |

**Status: 5/5 closed**

---

## Documentation

| Metric | Value |
|--------|-------|
| Total documentation files | 18 |
| Location | `docs/` |

| Document | Status |
|----------|--------|
| ARCHITECTURE.md | Complete |
| CHARTER.md | Complete |
| COMPETITORS.md | Complete |
| DEPLOYMENT.md | Complete |
| USER_GUIDE.md | Complete |
| MEMORY_ARCHITECTURE_REPORT.md | Complete |
| SESSION_MIGRATION_PLAN.md | Complete |
| RECALLABLE_KNOWLEDGE_ANALYSIS.md | Complete |
| STRATEGY.md | Complete |
| INVENTORY.md | Complete |
| PRD.md | Complete |
| SCHEMA.md | Complete |
| TROUBLESHOOTING.md | Complete |
| ADR.md | Complete |
| OPERATIONS.md | Complete |
| MONITORING.md | Complete |
| PERFORMANCE.md | Complete |
| HEALTH_REPORT.md | This file |

---

## Competitive Position

| Metric | Value |
|--------|-------|
| Official competitors tracked | 4 (OpenCode, Claude Code, Gemini CLI, Codex CLI) |
| Watch list | 4 (Aider, Cline, Roo Code, Goose) |
| Unique moats | 6 (mode/tier mapping, token budgets, CruxDev convergence, Crux intelligence layer, workspace checkpoints, client/server + LSP) |
| "Should close" gaps remaining | 5 (repo map, cost visibility, free tier, image input, multi-agent) |
| "Must close" gaps | 1 (community adoption) |

---

## Repository Stats

| Metric | Value |
|--------|-------|
| Monorepo packages | 19 |
| CI workflows | 31 |
| Extensions | 2 (VS Code, Zed) |
| LLM providers supported | 20+ |
| Built-in tools | 18 |
| Modes | 24 |
| SQL migrations | 6 |
| Platform targets | 10 |

---

## Risk Areas

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Zero community adoption (pre-launch) | High | Launch planning needed — marketing site, Discord, documentation ready |
| Upstream OpenCode divergence | Medium | Monitor upstream selectively; hard fork means no rebase pressure |
| Provider SDK churn | Medium | Vercel AI SDK abstracts most changes; pin versions |
| Bun runtime stability | Low | Pinned to `bun@1.3.10`; Bun is stable for this use case |
| Token budget calibration | Low | Initial thresholds are estimates; will need tuning with real usage data |
