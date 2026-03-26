# CruxCLI Performance

**Last Updated:** 2026-03-24

---

## Known Measurements

### Binary Size

| Target | Approximate Size | Notes |
|--------|-----------------|-------|
| All platforms | ~110 MB | Single-file compiled Bun executable including embedded migrations and model snapshot |

The binary bundles: the full application, SolidJS TUI components, 20+ provider SDKs, Drizzle ORM, SQL migrations, and a models.dev snapshot. The size is dominated by the Bun runtime and bundled dependencies.

**Baseline variants** (no AVX2) are approximately the same size — the AVX2 difference is in CPU instruction selection, not binary content.

### Checkpoint Create Overhead

| Operation | Target | Notes |
|-----------|--------|-------|
| `Snapshot.track()` (git add + write-tree) | < 100 ms | Depends on worktree size and number of changed files |

Auto-checkpoints run before every destructive tool call. The target is sub-100ms to avoid perceptible delay. This has not been formally benchmarked across project sizes.

### Database Operations

| Operation | Expected | Notes |
|-----------|----------|-------|
| SQLite WAL mode writes | Fast (no fsync per write) | `synchronous = NORMAL` trades durability for speed |
| JSON-to-SQLite migration | Depends on data volume | Runs in a single transaction with optimized PRAGMAs (`synchronous = OFF`, `cache_size = 10000`) |
| `busy_timeout` | 5000 ms | Maximum wait for database lock before failing |

---

## Unmeasured (Needs Benchmarking)

The following performance characteristics should be measured but have not been formally benchmarked yet:

| Metric | What to measure | How |
|--------|----------------|-----|
| **Startup time** | Time from `cruxcli` invocation to TUI ready | `time cruxcli --help` for cold start; instrument `Instance.state()` for warm start |
| **Build time** | Time to compile single-platform binary | `time bun run build --single` in `packages/cruxcli` |
| **Full build time** | Time to compile all 10 platform targets | `time bun run build` in `packages/cruxcli` |
| **LLM first-token latency** | Time from prompt submission to first streamed token | Instrument `LLM.stream()` — this is mostly provider-dependent |
| **Tool execution overhead** | CruxCLI overhead per tool call (excluding tool runtime) | Instrument `Tool.execute` wrapper: permission check + checkpoint + validation |
| **Compaction duration** | Time to summarize and prune context | Instrument `SessionCompaction` — depends on context size and summarization model speed |
| **Snapshot restore time** | Time to restore worktree from tree hash | `time cruxcli checkpoint restore <name>` — depends on file count |
| **Memory usage** | Peak RSS during a typical session | `CRUXCLI_DEBUG=1 cruxcli run` with memory profiling |
| **Server response latency** | HTTP API response times under load | Load test the Hono server with concurrent clients |
| **Typecheck time** | `bun turbo typecheck` wall time | Currently uses `tsgo` (native TypeScript 7.0 preview) for the core package |

---

## Performance-Relevant Architecture Decisions

| Decision | Performance impact |
|----------|-------------------|
| Bun runtime | Faster startup and compilation than Node.js. Native SQLite eliminates native module overhead. |
| WAL journal mode | Concurrent reads during writes. Better throughput for the client/server model. |
| Embedded migrations | No filesystem reads at startup for migration SQL — they are compiled into the binary. |
| Git-based snapshots | Tree hashing is O(changed files), not O(total files). Space-efficient via git object deduplication. |
| Batch JSON migration | Single-transaction bulk insert with relaxed PRAGMAs for the one-time JSON-to-SQLite migration. |
| Stream processing | LLM responses are processed as streams (SSE), not buffered — first output appears immediately. |
| Context compaction | Prevents context window overflow but adds a secondary LLM call. Trades latency for session continuity. |

---

## Optimization Opportunities

| Area | Opportunity | Effort |
|------|------------|--------|
| Binary size | Tree-shake unused provider SDKs for users who only use 1-2 providers | High |
| Startup time | Lazy-load provider SDKs (only initialize the selected provider) | Medium |
| Checkpoint overhead | Skip checkpoint for read-only tool calls that were misclassified as destructive | Low |
| Build time | Parallelize multi-target compilation | Medium |
| Memory | Stream large file reads instead of loading entirely into memory | Medium |
