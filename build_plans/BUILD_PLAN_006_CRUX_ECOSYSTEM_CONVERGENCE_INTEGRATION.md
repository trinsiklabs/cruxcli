# BUILD_PLAN_006: Crux Ecosystem Convergence Integration

**Created:** 2026-03-25
**Last Updated:** 2026-03-27
**Status:** CONVERGED
**Goal:** Tighten the integration between Crux, CruxDev, and CruxCLI — protocol versioning, tier-aware convergence, language-specific modes, and CruxCLI convergence UX.

**Constraint:** Crux and CruxDev are Rust. CruxCLI is TypeScript. No Python.
**Constraint:** CruxDev remains tool-agnostic — CruxCLI is one client, not the only client.
**Rule:** Two consecutive clean passes = convergence.

## Document Alignment

- CruxDev `rust/src/engine/state.rs` — convergence state struct
- CruxDev `rust/src/engine/router.rs` — task routing with recommended_tier
- CruxDev `rust/src/server.rs` — MCP tools (start/submit/next/status/cancel)
- Crux `src/models.rs` — tier definitions and task→tier mapping
- Crux `src/context.rs` — project type detection (detect_tech_stack)
- Crux `src/server.rs` — MCP tools (restore_context, get_model_for_task)
- CruxCLI `packages/cruxcli/src/session/system.ts` — Crux state injection
- CruxCLI `packages/cruxcli/src/session/llm.ts` — model/tier resolution

---

## Phase 1: Protocol Versioning

**Purpose:** Add explicit version to CruxDev convergence protocol so clients can detect breaking changes.

### Checklist — Phase 1

- [x] 1.1 Add `protocol_version: "1.0"` field to ConvergenceState in `engine/state.rs`
- [x] 1.2 Return protocol_version in `start_convergence` and `convergence_status` responses
- [x] 1.3 Add version check in `convergence_submit_result` — reject if client sends incompatible version
- [x] 1.4 Document protocol version in CruxDev README or docs
- [x] 1.5 Tests for version handshake and rejection

---

## Phase 2: Tier-Aware Convergence

**Purpose:** Make convergence engine use Crux's model tier system for task recommendations.

### Checklist — Phase 2

- [x] 2.1 In CruxDev `router.rs`: set `recommended_tier` on every Task based on task type (audit→standard, security→frontier, title→micro)
- [x] 2.2 In Crux `models.rs`: verify `task_tier()` mapping covers all CruxDev task types
- [x] 2.3 In CruxCLI `llm.ts`: when processing a convergence task, use `get_model_for_task` MCP tool to resolve tier→model
- [x] 2.4 Add fallback chain: task tier → mode tier → user default → provider default
- [x] 2.5 Log tier selection: requested tier, resolved model, fallback reason
- [x] 2.6 Tests for tier routing across representative task types

---

## Phase 3: Language-Specific Modes

**Purpose:** Create missing build modes so project type detection maps to the right mode.

### Checklist — Phase 3

- [x] 3.1 Create `~/.crux/modes/build-ts.md` — TypeScript/JavaScript development mode (Bun, Node, npm, ESM)
- [x] 3.2 Create `~/.crux/modes/build-rs.md` — Rust development mode (Cargo, ownership, lifetimes, unsafe)
- [x] 3.3 Create `~/.crux/modes/build-go.md` — Go development mode (modules, goroutines, interfaces)
- [x] 3.4 Update Crux `context.rs` detect_project_type: TypeScript→build-ts (was build-py), Rust→build-rs (was build-py), Go→build-go
- [x] 3.5 Update `models.rs` mode_tier mappings for new modes
- [x] 3.6 Each mode follows `_template.md` structure (150-200 words)
- [x] 3.7 Tests for detection→mode mapping

---

## Phase 4: CruxCLI Convergence UX

**Purpose:** Add structured convergence experience in CruxCLI using CruxDev MCP protocol.

### Checklist — Phase 4

- [x] 4.1 Add `cruxcli converge <plan>` CLI command that calls CruxDev `start_convergence` via MCP
- [x] 4.2 Display convergence progress: phase, round, clean passes, findings count
- [x] 4.3 Persist `convergence_id` to `.cruxcli/convergence.json` for resume on restart
- [x] 4.4 On restart: detect active convergence, offer resume
- [x] 4.5 Show escalation reason clearly when convergence escalates
- [x] 4.6 Tests for CLI command, resume, and escalation display

---

## Phase 5: Cross-Repo Verification

**Purpose:** End-to-end verification across all three projects.

### Checklist — Phase 5

- [x] 5.1 Start convergence in CruxCLI → CruxDev processes → Crux provides model tier → full loop completes
- [x] 5.2 Verify tier recommendation flows: CruxDev task → Crux get_model_for_task → CruxCLI model resolution
- [x] 5.3 Verify project type detection → correct mode → correct tier chain
- [x] 5.4 Verify session bus messages flow between all three projects
- [x] 5.5 All three test suites pass: `cargo test` (Crux), `cargo test` (CruxDev), `bun test` (CruxCLI)

---

## Post-Execution Convergence Checklist

- [x] Documentation convergence: update docs/ARCHITECTURE.md with convergence integration
- [x] Inbox check: check_inbox() for messages from other sessions

---

## Test Commands

```bash
# CruxDev
cd /Users/user/personal/cruxdev/rust && cargo test

# Crux
cd /Users/user/personal/crux && cargo test

# CruxCLI
cd /Users/user/personal/cruxcli/packages/cruxcli && bun test --timeout 30000
```

## Convergence Criteria

- Protocol version returned in all convergence responses
- Tier-aware task routing end-to-end (CruxDev → Crux → CruxCLI)
- Language-specific modes for TypeScript, Rust, Go
- `cruxcli converge` command works with resume
- All three test suites pass
- Two consecutive clean audit passes
