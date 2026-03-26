# BUILD_PLAN_006_CRUX_ECOSYSTEM_CONVERGENCE_INTEGRATION

**Created:** 2026-03-25  
**Status:** NOT STARTED  
**Goal:** Tightly weave Crux, CruxDev, and CruxCLI with CruxDev-first protocol guarantees, cross-tool parity, and unified model-tier routing.  
**Scope:** Cross-repo changes in `/Users/user/personal/crux`, `/Users/user/personal/cruxdev`, `/Users/user/personal/cruxcli`.
**Rule:** Contract-first. CruxDev remains tool-agnostic and first-class for Claude Code, OpenCode, CruxCLI, and future clients.  
**Rule:** No client-specific hidden behavior in core convergence protocol.  
**Rule:** Two consecutive clean passes per convergence phase.

---

## Architecture Overview

### Current (Observed)

- CruxDev convergence protocol exists, but some permissive behavior can cause silent false-clean outcomes.
- Crux mode validation includes legacy static mode set drift.
- CruxCLI consumes Crux state/modes and MCP tools, but does not fully route model choice from shared tier policy.
- Cross-client parity guidance and conformance artifacts are incomplete.

### Target

- CruxDev publishes strict, versioned, client-agnostic convergence protocol.
- Crux enforces dynamic mode validation and shared model-tier policy.
- CruxCLI acts as reference client by consuming public contracts only.
- Any external client can reach parity with documented lifecycle + conformance kit.

---

## Phase 1: Contract Hardening (Cross-Repo)

**Purpose:** Remove ambiguous or permissive behavior that can corrupt convergence integrity.

### Checklist — Phase 1

- [ ] 1.1 Harden CruxDev submit-result parsing: malformed findings payloads fail loudly and do not mutate convergence state.
- [ ] 1.2 Add explicit checklist completion contract in CruxDev execution phase (API-level, not implicit file-side behavior).
- [ ] 1.3 Update Crux mode validation to dynamic discovery from installed mode files (remove legacy static drift behavior).
- [ ] 1.4 Promote CruxCLI to first-class tool support in Crux tool sync/switch contract (not recipe-only fallback).
- [ ] 1.5 Add regression tests for all above contract behaviors.
- [ ] 1.6 Confirm no existing convergence run can advance on malformed payloads.
- [ ] 1.7 Add append-only convergence event log (WAL) with atomic append and fsync before any snapshot mutation.
- [ ] 1.8 Add snapshot checkpoint fields (`last_applied_event_id`, `last_seq`) and deterministic replay-on-load recovery.
- [ ] 1.9 Enforce idempotency keys + monotonic sequence validation for `start`, `next`, and `submit`.
- [ ] 1.10 Add replay/duplicate-submit regression tests proving no double-advance of phase, round, or clean-pass counters.

---

## Phase 2: CruxDev Protocol Canonicalization

**Purpose:** Make CruxDev the authoritative, versioned protocol owner for convergence clients.

### Checklist — Phase 2

- [ ] 2.1 Define protocol version + capabilities handshake for convergence clients.
- [ ] 2.2 Publish strict schema for start/next/submit/status/cancel request+response payloads.
- [ ] 2.3 Publish explicit error codes and terminal reason taxonomy.
- [ ] 2.4 Document canonical client lifecycle state machine (start -> next -> execute -> submit -> terminal).
- [ ] 2.5 Add protocol invariant tests (server-side) independent of any single client.
- [ ] 2.6 Add golden fixtures for transitions (happy path, malformed payload, timeout, max rounds, net-negative).
- [ ] 2.7 Publish durability contract: WAL ordering, fsync boundary, snapshot checkpoint semantics, and replay guarantees.
- [ ] 2.8 Publish run-history contract for plan-level visibility (`in_progress`, `converged`, `escalated`, `cancelled`) including phase/round/timestamps.

---

## Phase 3: Cross-Tool Conformance Kit

**Purpose:** Ensure parity is practical for non-CruxCLI clients.

### Checklist — Phase 3

- [ ] 3.1 Create “Convergence Client Guide” with minimum required call sequence and retry rules.
- [ ] 3.2 Provide reference pseudocode for CLI client, chat-loop client, and API runner client.
- [ ] 3.3 Create conformance checklist + fixture runner instructions.
- [ ] 3.4 Define feature levels (manual loop, automated loop+resume, full telemetry/escalation UX).
- [ ] 3.5 Validate guide against current Claude Code/OpenCode style usage assumptions.

---

## Phase 4: CruxCLI Reference Client Adapter

**Purpose:** Implement first-class convergence UX in CruxCLI by consuming public CruxDev protocol only.

### Checklist — Phase 4

- [ ] 4.1 Add convergence adapter module in CruxCLI that uses validate/start/next/submit/status/cancel.
- [ ] 4.2 Persist convergence_id for interruption-safe resume.
- [ ] 4.3 Add structured loop UX: phase, round, clean passes, recommended tier, escalation reason.
- [ ] 4.4 Add strict payload validation before acting on server responses.
- [ ] 4.5 Add retry/backoff for transient protocol call failures.
- [ ] 4.6 Add adapter conformance tests using CruxDev golden fixtures.
- [ ] 4.7 Persist idempotency metadata for retried protocol calls so client retries are crash-safe and replay-safe.

---

## Phase 5: Model-Tier Unification (Crux -> CruxDev -> Clients)

**Purpose:** Ensure deterministic model routing across modes and convergence tasks.

### Checklist — Phase 5

- [ ] 5.1 Make Crux the single source of truth for tier vocabulary and precedence.
- [ ] 5.2 Align CruxDev task recommended_tier outputs to shared tier taxonomy.
- [ ] 5.3 Update CruxCLI model resolver to honor tier precedence: user override -> task tier -> mode tier -> default.
- [ ] 5.4 Add deterministic fallback chain with explicit logged downgrade reason.
- [ ] 5.5 Add telemetry fields: requested tier, selected tier, fallback reason, outcome class.
- [ ] 5.6 Add integration tests proving consistent tier behavior across representative providers.

---

## Phase 6: Full-System Convergence + Documentation

**Purpose:** Converge code, docs, and operational guidance with no drift.

### Checklist — Phase 6

- [ ] 6.1 Run full convergence for code auditing with two consecutive clean passes.
- [ ] 6.2 Run documentation convergence for all changed docs with two consecutive clean passes.
- [ ] 6.3 Verify cross-repo contract alignment (Crux, CruxDev, CruxCLI docs and APIs).
- [ ] 6.4 Update ecosystem docs with final protocol and integration guidance.
- [ ] 6.5 Capture novel patterns in methodology docs (only behavior-changing learnings).
- [ ] 6.6 Final verification report with known gaps = none or explicitly tracked.

---

## Phase Ordering and Dependencies

1. Phase 1 must complete before Phase 2/4/5.
2. Phase 2 must complete before Phase 4 and Phase 3 finalization.
3. Phase 3 can begin during Phase 2 but must finalize after protocol freeze.
4. Phase 5 can start after Phase 1 and must complete before final system convergence.
5. Phase 6 begins after Phases 1-5 are complete.

---

## File Inventory (Planned Touch Points)

- `/Users/user/personal/cruxdev/src/mcp_server.py`
- `/Users/user/personal/cruxdev/src/engine/task_router.py`
- `/Users/user/personal/cruxdev/src/engine/convergence.py`
- `/Users/user/personal/cruxdev/docs/DEVELOPMENT_PATTERNS_CRUXDEV.md` (if novel learnings qualify)
- `/Users/user/personal/cruxdev/docs/` (new protocol + conformance docs)
- `/Users/user/personal/crux/scripts/lib/crux_mcp_handlers.py`
- `/Users/user/personal/crux/scripts/lib/crux_sync.py`
- `/Users/user/personal/crux/scripts/lib/crux_switch.py`
- `/Users/user/personal/cruxcli/packages/cruxcli/src/session/system.ts`
- `/Users/user/personal/cruxcli/packages/cruxcli/src/session/llm.ts`
- `/Users/user/personal/cruxcli/packages/cruxcli/src/mcp/index.ts`
- `/Users/user/personal/cruxcli/packages/cruxcli/src/...` (new convergence adapter + tests)

---

## Document Alignment

### Product Docs (this plan must conform to)

- `/Users/user/personal/cruxdev/docs/DEVELOPMENT_PATTERNS_CRUXDEV.md` — convergence lifecycle and safety gates.
- `/Users/user/personal/cruxdev/docs/ADOPTION_PROCESS.md` — adoption and orchestration principles.
- `/Users/user/personal/crux/docs/API.md` — Crux MCP contract expectations.
- `/Users/user/personal/crux/docs/safety-pipeline.md` — gate expectations.
- `/Users/user/personal/cruxcli/AGENTS.md` — project-level coding constraints.
- `/Users/user/personal/crux/templates/AGENTS.md` — ecosystem integration constraints.

### Memory/Decision Files

- `/Users/user/personal/cruxcli/.crux/sessions/state.json` — active decisions and current direction (when present).

---

## Test Commands

### CruxDev

```bash
cd /Users/user/personal/cruxdev && python3 -m pytest
```

### Crux

```bash
cd /Users/user/personal/crux && python3 -m pytest
```

### CruxCLI

```bash
cd /Users/user/personal/cruxcli/packages/cruxcli && bun test
```

### Cross-Repo Contract/Conformance

```bash
# CruxDev convergence protocol + engine invariants
cd /Users/user/personal/cruxdev && python3 -m pytest tests/engine/test_convergence.py

# Crux model-tier policy parity
cd /Users/user/personal/crux && python3 -m pytest tests/test_crux_model_tiers.py tests/test_audit_modes.py

# CruxCLI client adapter + MCP integration coverage
cd /Users/user/personal/cruxcli/packages/cruxcli && bun test
```

Pass criteria:

- All three commands exit 0.
- Any newly added fixture/conformance suites in this plan are appended to this section before Phase 6 closure.

---

## E2E Test Plan

### Journey Matrix

- J1 New convergence run: validate -> start -> next -> submit loop reaches terminal `done` with two clean passes.
- J2 Interrupted session resume: persisted `convergence_id` restores and continues from the last non-terminal task.
- J3 Malformed submit payload: server returns explicit error code; convergence counters and phase state remain unchanged.
- J4 Escalation path: timeout/max-rounds/net-negative transitions produce deterministic terminal reason and user-visible guidance.
- J5 Tier routing parity: representative tasks resolve tiers consistently in Crux, CruxDev recommended tier, and CruxCLI resolver.
- J6 Crash/replay recovery: interrupted run resumes from persisted checkpoint, and replayed duplicate calls are idempotent.

### E2E Commands (Phase 6 Gate)

```bash
# CruxDev protocol lifecycle + error handling
cd /Users/user/personal/cruxdev && python3 -m pytest tests/engine/test_convergence.py

# Crux model tier policy parity
cd /Users/user/personal/crux && python3 -m pytest tests/test_crux_model_tiers.py tests/test_audit_modes.py

# CruxCLI adapter flow + resume behavior
cd /Users/user/personal/cruxcli/packages/cruxcli && bun test
```

### E2E Pass Criteria

- All journeys J1-J5 have explicit tests or scripted fixture assertions.
- All journeys J1-J6 have explicit tests or scripted fixture assertions.
- Resume and escalation outputs include phase, round, clean pass count, and terminal reason.
- No journey depends on tool-specific hidden behavior outside the published CruxDev protocol.
- Run history query can list completed and in-progress convergences per plan with deterministic status.

---

## Post-Execution Convergence (Mandatory)

- [ ] Documentation convergence: audit all touched docs against final code, two clean passes.
- [ ] Website convergence (if applicable): update any integration/metrics pages and verify accuracy.
- [ ] Deployment convergence (if applicable): follow each repo’s deployment process.
- [ ] Patterns update: capture only genuinely novel, behavior-changing learnings.
- [ ] Inbox/session coordination check across ecosystem sessions.

---

Risks and Mitigations

- Risk: Breaking existing loose clients with stricter protocol validation.  
  Mitigation: clear error codes + migration notes + conformance kit.
- Risk: Cross-repo drift during implementation.  
  Mitigation: protocol freeze milestone + fixture-based contract tests.
- Risk: Tier policy conflicts with provider availability.  
  Mitigation: deterministic fallback + explicit downgrade telemetry.

---

Convergence Criteria

- All checklist items complete.
- CruxDev protocol is strict, versioned, and documented.
- Conformance fixtures pass for server invariants.
- CruxCLI reference adapter passes conformance against public protocol only.
- Model-tier routing follows shared precedence and deterministic fallback rules.
- Two consecutive clean passes for code and docs in final convergence.
- No unresolved high/medium contract defects.
- Convergence persistence is crash-safe, resumable, and idempotent via WAL + checkpoint replay semantics.
