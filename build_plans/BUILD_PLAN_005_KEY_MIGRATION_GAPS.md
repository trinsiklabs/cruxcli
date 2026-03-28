# BUILD_PLAN_005: Close Documentation Gaps for Key Migration

**Created:** 2026-03-24
**Status:** CONVERGED
**Goal:** Close all remaining MEDIUM and LOW documentation gaps from GAPS.md, fix known deficiencies in existing docs, and audit to convergence — ready for Key domain migration.

**Constraint:** Every doc must be verified against actual code/state — no aspirational claims.
**Constraint:** At maturity level 2, only R (required) and P (production) docs are mandatory. M (mature) docs are optional.
**Rule:** Two consecutive clean audit passes = convergence.

## Document Alignment

- `GAPS.md` — the authoritative gap list
- `intake-inventory.md` — what exists today
- `intake-classification.md` — project type and maturity
- `AGENTS.md` — coding style for any code examples in docs
- MIGRATE_TO_KEY.md — migration methodology

---

## Phase 1: Fix Known Deficiencies

**Purpose:** Existing docs have stale or inaccurate content. Fix before creating new docs.

### Checklist — Phase 1

- [x] 1.1 README.md — rewrite to be CruxCLI-specific (not upstream OpenCode boilerplate)
- [x] 1.2 SECURITY.md — customize for CruxCLI (security contact, vulnerability reporting)
- [x] 1.3 ROADMAP.md — update to reflect competitive gaps 1-3 now closed, add new priorities
- [x] 1.4 CONTRIBUTING.md — fix models.dev reference, verify all URLs
- [x] 1.5 BUILD_PLAN_001 — fix before/after naming inconsistencies
- [x] 1.6 Verify all docs have no stale `anomalyco` or `opencode` references

---

## Phase 2: Medium Priority — Code Documentation

**Purpose:** Fill the 3 missing code docs (API, CONFIGURATION, TESTING).

### Checklist — Phase 2

- [x] 2.1 Create `docs/API.md` — document CruxCLI's HTTP server API (routes from `src/server/`, Hono endpoints)
- [x] 2.2 Create `docs/CONFIGURATION.md` — document `cruxcli.json` schema (all config fields from `src/config/config.ts`), provider setup, env vars
- [x] 2.3 Create `docs/TESTING.md` — document test strategy, how to run tests, fixture system, coverage expectations
- [x] 2.4 Verify each doc against actual code — no aspirational claims

---

## Phase 3: Medium Priority — Domain & Product Documentation

**Purpose:** Fill the 3 missing domain/product docs (STRATEGY, INVENTORY, PRD).

### Checklist — Phase 3

- [x] 3.1 Create `docs/STRATEGY.md` — CruxCLI's strategic position, differentiation vs competitors, growth strategy
- [x] 3.2 Create `docs/INVENTORY.md` — domain inventory listing all packages, extensions, tools, integrations
- [x] 3.3 Create `docs/PRD.md` — product requirements document for CruxCLI (features, target users, success metrics)
- [x] 3.4 Cross-reference with COMPETITORS.md and ROADMAP.md for consistency

---

## Phase 4: Low Priority — Operational Documentation

**Purpose:** Fill remaining LOW-priority gaps. These are maturity-3+ docs but useful to have.

### Checklist — Phase 4

- [x] 4.1 Create `docs/SCHEMA.md` — document SQLite schema (session, message, part tables from Drizzle migrations)
- [x] 4.2 Create `docs/TROUBLESHOOTING.md` — common issues and fixes (provider auth, build failures, MCP connection)
- [x] 4.3 Create `docs/ADR.md` — index of architectural decision records (hard fork, Bun-only, provider-agnostic, mode system, token budgets)
- [x] 4.4 Create `docs/OPERATIONS.md` — operational concerns (snapshot cleanup, database migration, log management)
- [x] 4.5 Create `docs/MONITORING.md` — what to monitor (session health, token usage, error rates)
- [x] 4.6 Create `docs/PERFORMANCE.md` — performance characteristics (build time, binary size, startup time, checkpoint overhead)
- [x] 4.7 Create `docs/HEALTH_REPORT.md` — current domain health assessment

---

## Phase 5: Audit to Convergence

**Purpose:** Two consecutive clean passes verifying all documentation against ground truth.

### Checklist — Phase 5

- [x] 5.1 Pass 1: Read every doc, verify every factual claim against code/state
- [x] 5.2 Fix all discrepancies found in Pass 1
- [x] 5.3 Pass 2: Re-read all docs, verify fixes, fresh attention on previously clean docs
- [x] 5.4 Zero discrepancies in Pass 2 → convergence achieved
- [x] 5.5 Update GAPS.md — all gaps marked DONE or justified as Not Applicable
- [x] 5.6 Update intake-inventory.md with all new documents
- [x] 5.7 Set GAPS.md migration status to `complete`

---

## Test Commands

```bash
# Verify no broken internal links
grep -r '\[.*\](.*\.md)' docs/ | while read line; do
  file=$(echo "$line" | sed 's/.*(\(.*\.md\)).*/\1/')
  [ -f "docs/$file" ] || [ -f "$file" ] || echo "BROKEN: $line"
done

# Verify no stale references
grep -ri "anomalyco\|opencode\|sst-dev" docs/ README.md CONTRIBUTING.md SECURITY.md ROADMAP.md
```

## Convergence Criteria

- All 14 remaining gaps closed (6 MEDIUM + 8 LOW) or justified as N/A
- All 6 known deficiencies fixed
- GAPS.md migration status = complete
- Two consecutive clean audit passes (zero discrepancies)
- intake-inventory.md updated with all new documents
