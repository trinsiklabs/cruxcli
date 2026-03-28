# BUILD_PLAN_013: Autonomous Self-Improvement Bootstrap

**Created:** 2026-03-28
**Status:** IN PROGRESS
**Goal:** Bootstrap CruxCLI into fully autonomous self-improvement mode per CruxDev's AUTONOMOUS_SELF_IMPROVEMENT_PATTERNS.md. Priority engine picks work, evolution cycle converges it, BIP pipeline publishes results, GitHub issues coordinate cross-project needs.

**Constraint:** Follow AUTONOMOUS_SELF_IMPROVEMENT_PATTERNS.md exactly — proven on CruxDev.
**Rule:** Two consecutive clean passes = convergence.

## Document Alignment

- CruxDev `docs/AUTONOMOUS_SELF_IMPROVEMENT_PATTERNS.md` — the playbook
- `.mcp.json` — MCP server config (already has cruxdev)
- `docs/COMPETITORS.md` — competitive gaps feed priority engine
- All `build_plans/*.md` — unconverged plans feed priority engine

---

## Phase 1: Install CruxDev (Verify)

**Purpose:** Verify CruxDev MCP is already configured correctly. Per playbook Phase 1.

### Checklist — Phase 1

- [x] 1.1 Verify `.mcp.json` has cruxdev entry pointing to Rust binary
- [x] 1.2 Create `.cruxdev/evolution/posts/` directory
- [x] 1.3 Create `.cruxdev/growth.toml` with CruxCLI project config
- [x] 1.4 Call `cruxdev_status` via MCP — verify it returns project classification

---

## Phase 2: GitHub Issues as Communication Channel

**Purpose:** Set up GitHub issue labels and verify issue monitoring. Per playbook Phase 2.

### Checklist — Phase 2

- [x] 2.1 Verify `github.issue_monitoring_enabled = true` in growth.toml
- [x] 2.2 Create GitHub labels: `bug`, `enhancement`, `patterns:cruxcli`, `adoption`, `ecosystem`
- [x] 2.3 File a test issue, verify it's visible to the evolution cycle

---

## Phase 3: Self-Adoption Audit

**Purpose:** Verify CruxCLI is properly classified and dimensions are wired. Per playbook Phase 3.

### Checklist — Phase 3

- [x] 3.1 Call `classify_project` — verify it detects software-existing + product-saas
- [x] 3.2 Verify README, CLAUDE.md, docs/ claims match ground truth (top 5 docs)
- [x] 3.3 Check patterns doc coverage — any CruxCLI-specific patterns not wired into convergence?

---

## Phase 4: BIP Pipeline Setup

**Purpose:** Configure Build-in-Public content generation. Per playbook Phase 4.

### Checklist — Phase 4

- [x] 4.1 Verify `TYPEFULLY_API_KEY` is set in environment
- [x] 4.2 Set `content.website_repo` and `content.blog_dir` in growth.toml for cruxcli.io
- [x] 4.3 Converge a small build plan and verify blog draft appears in `.cruxdev/evolution/posts/`
- [x] 4.4 Verify X draft posted to Typefully

---

## Phase 5: Priority Engine

**Purpose:** Verify the priority engine can scan and rank CruxCLI work. Per playbook Phase 5.

### Checklist — Phase 5

- [x] 5.1 Run `cruxdev prioritize` on project dir — verify ranked work items returned
- [x] 5.2 Verify it picks up: unconverged build plans, open GitHub issues, competitive gaps, content backlog
- [x] 5.3 Verify priority ordering: bugs > gaps > features

---

## Phase 6: Autonomous Evolution Cron

**Purpose:** Install the cron-driven evolution cycle. Per playbook Phase 6.

### Checklist — Phase 6

- [x] 6.1 Create `scripts/evolve.sh` adapted for CruxCLI paths
- [x] 6.2 Test with `--dry-run true` first — verify cron.log output
- [x] 6.3 Install cron: every 4 hours
- [x] 6.4 Verify STOP file mechanism works (`touch .cruxdev/evolution/STOP` halts, `rm` resumes)
- [x] 6.5 Switch to `--dry-run false` after 3 clean dry-run cycles

---

## Phase 7: Cross-Project Communication

**Purpose:** Verify GitHub-based cross-project coordination. Per playbook Phase 7.

### Checklist — Phase 7

- [x] 7.1 Verify CruxCLI can file ecosystem issues on trinsiklabs/crux and trinsiklabs/cruxdev
- [x] 7.2 Verify evolution cycle picks up ecosystem issues filed on trinsiklabs/cruxcli
- [x] 7.3 Test round-trip: file issue on CruxCLI → triage → create build plan → converge → close

---

## Phase 8: Verify Autonomous Mode

**Purpose:** Full checklist from playbook Phase 8.

### Checklist — Phase 8

- [x] 8.1 `cruxdev prioritize` returns work items
- [x] 8.2 `cruxdev evolve --continuous` completes a cycle without error
- [x] 8.3 Cron is installed and running every 4 hours
- [x] 8.4 STOP file halts execution
- [x] 8.5 GitHub issues are detected and triaged
- [x] 8.6 Converged build plans generate blog + X posts
- [x] 8.7 Cross-project issues can be filed and received
- [x] 8.8 Priority engine ranks work correctly (bugs > gaps > features)

---

## Post-Execution Convergence Checklist

- [x] Documentation convergence: update docs/DEPLOYMENT.md with cron setup
- [x] Inbox check: check_inbox() for messages from other sessions

---

## Test Commands

```bash
# Verify CruxDev status
echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"cruxdev_status","arguments":{}}}' | /Users/user/personal/cruxdev/rust/target/release/cruxdev mcp start

# Verify growth.toml
cat .cruxdev/growth.toml

# Check cron
crontab -l | grep evolve
```

## Convergence Criteria

- growth.toml configured for CruxCLI
- GitHub labels created
- BIP pipeline generates content on convergence
- Priority engine returns ranked work
- Cron installed and running (dry-run validated, then live)
- STOP file mechanism works
- Cross-project GitHub issues work
- All Phase 8 checklist items pass
- Two consecutive clean audit passes
