# CruxCLI Monitoring

**Last Updated:** 2026-03-24

---

## What to Monitor

### Session Health

| Signal | What to watch | Why |
|--------|--------------|-----|
| Session completion rate | Sessions that end normally vs error/timeout | Indicates provider reliability and prompt quality |
| Compaction frequency | How often context compaction triggers per session | High frequency suggests prompts are too verbose or tasks too long |
| Doom loop detection | Consecutive identical tool call failures (3+ triggers doom loop) | Indicates the agent is stuck — mode prompt or tool may need adjustment |
| Subtask depth | Nested sub-agent sessions | Deep nesting suggests the primary prompt is not scoping tasks well |

### Token Budget Usage

| Signal | What to watch | Why |
|--------|--------------|-----|
| Budget utilization per mode | Percentage of token budget consumed per session | Modes consistently hitting 90% hard limit need budget increases |
| Warning threshold hits | Sessions reaching 75% warning | Normal if sessions complete shortly after; concerning if they then hit hard limit |
| Cost per session | Total token cost across all LLM calls in a session | Track for budget planning and mode optimization |
| Token count accuracy | Reported tokens vs provider billing | Ensures budget enforcement is calibrated correctly |

### Checkpoint Creation Rate

| Signal | What to watch | Why |
|--------|--------------|-----|
| Checkpoints per session | Number of auto-checkpoints created | High counts indicate many destructive operations — normal for edit-heavy sessions |
| Checkpoint storage size | Disk usage of snapshot git directories | Unbounded growth indicates cleanup is not running |
| Restore success rate | Percentage of restore operations that succeed | Failures indicate tree hashes were garbage collected prematurely |
| Checkpoint pruning events | Auto-pruning when 50-limit is reached | Frequent pruning in short sessions suggests the limit may need adjustment |

### Build Pipeline Status

| Signal | What to watch | Why |
|--------|--------------|-----|
| `publish.yml` success rate | Release pipeline completion | Failed releases block distribution |
| `test.yml` pass rate | Test suite on PR/merge | Regressions caught before merge |
| `typecheck.yml` status | TypeScript type checking (13 packages) | Type errors indicate API contract violations |
| Binary size trend | Output binary size over releases | Unexpected growth indicates bundling issues |
| Build duration | Time from trigger to binary output | Regressions indicate build system issues |

### Test Suite Pass Rate

| Signal | What to watch | Why |
|--------|--------------|-----|
| Total tests passing | Current: 1204 | Declining count indicates removed or broken tests |
| Test duration | Time to run full suite | Slow tests indicate performance regressions |
| Flaky test rate | Tests that pass/fail non-deterministically | Flaky tests erode confidence in the suite |
| Coverage per subsystem | Test coverage of core subsystems (session, provider, tool) | Gaps indicate under-tested areas |

---

## Logging

CruxCLI uses structured logging via the `Log` utility. Each subsystem creates a named logger:

| Service | Subsystem |
|---------|-----------|
| `storage` | JSON file storage operations |
| `json-migration` | Legacy JSON to SQLite migration |
| `db` | SQLite database operations |
| `mcp` | MCP client connections and tool discovery |
| `lsp` | Language server lifecycle |
| `snapshot` | Git-based snapshot operations |
| `checkpoint` | Checkpoint create/restore/prune |
| `scheduler` | Background task execution |

---

## Health Checks

**Server health:** The Hono HTTP server exposes endpoints that clients use to verify connectivity. If the server is unresponsive, all connected frontends (TUI, web, desktop) lose access.

**Provider health:** Provider errors are surfaced in session logs. Common failure modes: 401 (auth), 429 (rate limit), 500 (provider outage).

**Database health:** SQLite WAL mode with `busy_timeout = 5000`. If the database is locked for more than 5 seconds, operations fail. Monitor for `SQLITE_BUSY` errors.

---

## Alerts Worth Setting Up

For production/team deployments:

1. **Build pipeline failure** — Any `publish.yml` failure blocks releases.
2. **Test count regression** — Total tests dropping below 1200 indicates removed coverage.
3. **Typecheck failure** — Any of the 13 packages failing typecheck.
4. **Binary size anomaly** — Binary size deviating more than 10% from baseline (~110MB).
5. **Provider error spike** — Elevated 401/429/500 rates from LLM providers.
