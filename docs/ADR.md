# CruxCLI Architectural Decision Records

**Last Updated:** 2026-03-24

---

## ADR-001: Hard Fork from OpenCode

**Status:** Accepted
**Date:** 2026-03 (project inception)

**Context:** OpenCode is the most community-adopted open-source terminal coding agent (129k stars, 800+ contributors, MIT license). CruxCLI needed a mature terminal agent codebase to build intelligence features on top of.

**Decision:** Hard fork from OpenCode. No rebase relationship maintained. Monitor upstream for ideas, integrate selectively.

**Rationale:**
- OpenCode provides a battle-tested client/server architecture, provider integration (20+ providers), LSP support, plugin API, and TUI.
- A hard fork gives freedom to make breaking changes (mode system, token budgets, Bun-only runtime) without upstream coordination.
- Maintaining a rebase relationship with a project releasing near-daily (737+ releases) would be unsustainable and create constant merge conflicts.
- The value CruxCLI adds (intelligence layer, modes, convergence) requires deep structural changes incompatible with a patch-on-top approach.

**Consequences:**
- Must independently maintain and update the forked codebase.
- Cannot automatically benefit from upstream bug fixes or features — must port selectively.
- Competitive risk: OpenCode could implement similar features, reducing differentiation.

---

## ADR-002: Bun-Only Runtime

**Status:** Accepted
**Date:** 2026-03

**Context:** OpenCode supports both Bun and Node.js. CruxCLI needed to decide whether to maintain dual runtime support.

**Decision:** Bun-only. Drop Node.js runtime support entirely.

**Rationale:**
- Bun compiles to standalone single-file executables, simplifying distribution.
- Bun's built-in SQLite (`bun:sqlite`) eliminates native module dependencies.
- Faster startup and compilation than Node.js equivalents.
- Maintaining dual runtime support adds testing burden and constrains which APIs can be used.
- The `packageManager` field is pinned to `bun@1.3.10`.

**Consequences:**
- Users cannot run CruxCLI from source with Node.js — must use Bun or the compiled binary.
- Excludes environments where Bun is not available (rare, given binary distribution).
- OpenCode's Node.js-compatible code paths can be removed, reducing maintenance burden.

---

## ADR-003: Provider-Agnostic Design

**Status:** Accepted
**Date:** 2026-03

**Context:** Competing terminal agents are coupled to single vendors: Claude Code (Anthropic), Gemini CLI (Google), Codex CLI (OpenAI). CruxCLI needed a provider strategy.

**Decision:** Provider-agnostic. Support every major LLM provider. No first-party model preference.

**Rationale:**
- LLM providers are converging in capability. Today's best model is tomorrow's commodity.
- Vendor lock-in is a liability for users and for the project's longevity.
- Provider-agnostic design means CruxCLI benefits from every model improvement, regardless of vendor.
- The Vercel AI SDK provides a unified interface across providers, reducing integration cost.
- Runtime model definitions from models.dev allow new models to work without code changes.

**Consequences:**
- Cannot optimize for provider-specific features (e.g., Anthropic's extended thinking, Google Search grounding).
- Provider-specific transforms (`provider/transform.ts`) are needed for edge cases.
- Must test across multiple providers to ensure quality.

---

## ADR-004: Mode-to-Model Tier Mapping

**Status:** Accepted
**Date:** 2026-03

**Context:** Generic terminal agents send the same prompt to whatever model the user selects, regardless of task complexity. This wastes expensive model capacity on routine tasks and under-serves complex tasks with cheap models.

**Decision:** Implement a mode system with 24 task-specific modes. Each mode maps to a model tier (e.g., "flagship", "standard", "fast") that automatically selects an appropriate model.

**Rationale:**
- Different tasks have different model requirements. Code review needs strong reasoning; file renaming does not.
- Automatic tier mapping removes the burden of model selection from the user.
- Mode-specific prompts are more effective than generic prompts — each mode carries task-optimized instructions.
- No competitor has this feature (see COMPETITORS.md feature matrix).
- Mode prompts are maintained in the Crux intelligence platform and baked into the binary at build time.

**Consequences:**
- Mode definitions live in the Crux repo, not CruxCLI — creates a cross-repo dependency.
- Users must understand the mode concept (mitigated by automatic mode selection).
- Model tier recommendations must be maintained as new models release.

---

## ADR-005: Token Budgets Over Step Counts

**Status:** Accepted
**Date:** 2026-03

**Context:** OpenCode and other agents use step-count limits (maximum number of tool calls) to prevent runaway sessions. This is a coarse proxy for cost.

**Decision:** Replace step-count limits with per-mode token budgets. Each mode has a configurable token budget with warning (75%) and hard limit (90%) thresholds.

**Rationale:**
- Token usage is directly proportional to cost. Step counts are not — a single step can use 100K tokens or 100 tokens.
- Per-mode budgets allow expensive modes (deep analysis) to have higher budgets than cheap modes (simple edits).
- Warning thresholds give the agent a chance to wrap up before hitting the hard limit, producing better outcomes than abrupt termination.
- Implemented in `session/token-budget.ts`.

**Consequences:**
- Requires accurate token counting per provider (some providers report tokens differently).
- Budget tuning is an ongoing process — initial thresholds are estimates.
- Users accustomed to step-count limits need to understand the new model.

---

## ADR-006: Workspace Checkpoints

**Status:** Accepted
**Date:** 2026-03

**Context:** AI agents executing file modifications and shell commands can cause unintended damage. Users need a safety net.

**Decision:** Implement automatic workspace checkpoints using git tree hashing. Before any destructive tool operation (edit, write, multiedit, bash, apply_patch), auto-create a named checkpoint. Store up to 50 checkpoints per project with auto-pruning of oldest auto-checkpoints.

**Rationale:**
- Git tree hashing is fast (sub-100ms target) and space-efficient — only stores tree objects, not full file copies.
- Automatic checkpoints require zero user effort — safety is the default.
- 50-checkpoint limit prevents unbounded storage growth.
- Separate from the project's own `.git` — uses a CruxCLI-managed git directory under the data path.
- Can be disabled via `CRUXCLI_DISABLE_AUTO_CHECKPOINT` for users who prefer git worktrees or other approaches.

**Consequences:**
- Snapshot cleanup must run periodically (`git gc --prune=7.days` via scheduler).
- Checkpoint storage adds disk usage (mitigated by git's object deduplication).
- Checkpoints older than 7 days are garbage collected and cannot be restored.

---

## ADR-007: Client/Server Architecture

**Status:** Accepted (inherited from OpenCode)
**Date:** Pre-fork (OpenCode design)

**Context:** A terminal agent could be a monolithic CLI process or a client/server system.

**Decision:** Client/server architecture. The CLI starts a local HTTP server (Hono-based, default port 4096). Frontends (TUI, web app, desktop app, VS Code extension) are clients that communicate over HTTP, SSE, and WebSocket.

**Rationale:**
- Decouples the agent engine from the presentation layer. The TUI is one client among many.
- Enables remote-drivable sessions (e.g., mobile app controlling a local CruxCLI session).
- Enables CruxDev to drive CruxCLI sessions programmatically via the HTTP API.
- SSE streaming provides real-time updates to all connected clients.
- OpenAPI spec generation enables auto-generated SDKs.
- Headless mode (`cruxcli serve`) allows running without a TUI.

**Consequences:**
- Adds complexity: HTTP server, routing, CORS, authentication (`CRUXCLI_SERVER_PASSWORD`).
- Port conflicts possible on port 4096.
- All state changes must be published via the event bus to keep clients in sync.
