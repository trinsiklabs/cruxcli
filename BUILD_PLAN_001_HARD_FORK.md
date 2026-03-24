# BUILD_PLAN_001: CruxCLI Hard Fork + Rebrand

**Created:** 2026-03-18
**Last Updated:** 2026-03-23
**Status:** CONVERGING — Phases 1-6 complete, verifying convergence
**Goal:** Fork CruxCLI, strip to essentials, rebrand to CruxCLI, absorb bridge plugin, replace prompts with Crux mode-driven system. Produce a working `cruxcli` binary.

**Constraint:** All LLM work stays in Claude Code (Pro Max).
**Constraint:** Clean break from OpenCode — no `OPENCODE_*` env var fallbacks, no upstream sync.
**Constraint:** Binary name is `cruxcli`, not `crux` (Crux is the platform, CruxCLI is the terminal agent).
**Constraint:** All references to "opencode" become "cruxcli" in the fork.
**Rule:** TDD. 100% coverage. Tests before code.
**Rule:** Follow DEVELOPMENT_PATTERNS_CRUXDEV.md methodology.

## Document Alignment

- `AGENTS.md` — coding style, naming conventions, testing rules
- `ROADMAP.md` — priorities and non-goals
- `CONTRIBUTING.md` — contribution guidelines

---

## Architecture Overview

### Before

```
OpenCode (upstream)                   CruxCLI v0.1
─────────────────                     ──────────────
19-package monorepo                   Bridge plugin (crux-bridge.js)
Binary: opencode                      3 hooks on stock OpenCode
Config: .opencode/, opencode.json     Config overlays only
Env: OPENCODE_*                       No source control
Prompts: OpenCode defaults            Mode injection via hook
```

### After

```
CruxCLI v0.2 (hard fork)
─────────────────────────
Stripped monorepo (core + plugin + sdk + util + script)
Binary: cruxcli
Config: .cruxcli/, cruxcli.json
Env: CRUXCLI_*
XDG: ~/.config/cruxcli/, ~/.local/share/cruxcli/
Prompts: Crux mode prompts injected natively in prompt.ts
Bridge: absorbed into source (retired as standalone)
MCP: Crux MCP server connects through forked runtime
```

### Naming Convention

| Concept | Value |
|---------|-------|
| Binary | `cruxcli` |
| Project-local config dir | `.cruxcli/` |
| XDG config dir | `~/.config/cruxcli/` |
| XDG data dir | `~/.local/share/cruxcli/` |
| Config file | `cruxcli.json` / `cruxcli.jsonc` |
| Env var prefix | `CRUXCLI_*` |
| App name constant | `"cruxcli"` |
| npm scope (internal) | `@cruxcli/` (replaces `@cruxcli-ai/`) |
| HTTP header | `x-cruxcli-client` |

**No collision with Crux core:** Crux uses `.crux/`, `CRUX_*`, `~/.crux/`. CruxCLI uses `.cruxcli/`, `CRUXCLI_*`, `~/.config/cruxcli/`. Fully separate namespaces.

---

## Phase Ordering

```
Phase 1: Fork + Strip          ← Get the repo, remove dead packages
Phase 2: Rebrand               <- opencode -> cruxcli everywhere
Phase 3: Prompt Replacement    ← Replace 6 prompt injection points
Phase 4: Bridge Absorption     ← Move bridge logic into prompt.ts
Phase 5: Token Budget          ← Replace step-count with token budgets
Phase 6: Build + Verify        ← Binary compiles, tests pass, MCP connects
```

All phases are sequential. Each depends on the prior.

---

## Phase 1: Fork + Strip

**Purpose:** Get a clean copy of OpenCode and remove everything CruxCLI doesn't need.

### 1A. Fork

```bash
cd /Users/user/personal/cruxcli
# OpenCode source is at /Users/user/personal/local_llm/opencode/
# Copy the full monorepo as starting point
cp -r /Users/user/personal/local_llm/opencode/ fork/
cd fork/
git init  # Fresh git history — clean break
```

### 1B. Evaluate Packages

Evaluate each of the 19 packages. For each, determine: keep (needed for CruxCLI), strip (dead weight), or defer (might be useful later).

**Required (core CLI depends on these):**
- `packages/cruxcli` — the core CLI itself
- `packages/plugin` — plugin SDK
- `packages/sdk` — client SDK
- `packages/util` — shared utilities
- `packages/script` — build scripts

**Evaluated — all kept except `infra` (empty placeholder):**

| Package | Why Keep |
|---------|---------|
| `app` | Web dashboard for convergence monitoring, autonomous run visibility |
| `console` | Reference for hosted/multi-user patterns |
| `containers` | CI binary builds, evolution pipeline containers |
| `desktop` | Native app wrapper (Tauri) — test against electron |
| `desktop-electron` | Native app wrapper (Electron) — test against tauri |
| `docs` | Doc site framework, repurpose for CruxCLI docs |
| `enterprise` | Reference for team features |
| `extensions` | Editor integrations (Zed now, VS Code later) |
| `function` | Sync server, GitHub App auth for evolution pipeline |
| `identity` | Brand asset structure (replace artwork) |
| `script` | Release automation (bun-based) |
| `slack` | Team interaction channel |
| `storybook` | Visual component testing for `ui` |
| `ui` | Shared SolidJS components (needed by app, desktop) |
| `web` | Marketing site framework |

**Strip:** `infra` only (empty SST placeholder).

After stripping `infra`, update root `package.json` workspaces. Verify `bun install` succeeds.

### 1C. Verify Base Builds

Before any renaming, verify the stripped fork builds and tests pass:

```bash
bun install
bun test
```

### Checklist — Phase 1

- [x] 1.1 Copy OpenCode monorepo to cruxcli/fork/
- [x] 1.2 Initialize fresh git repo
- [x] 1.3 Remove `packages/infra` (only package stripped)
- [x] 1.4 Update root package.json workspaces
- [x] 1.5 `bun install` succeeds
- [x] 1.6 `bun test` passes (in packages/cruxcli/)
- [x] 1.7 Git commit: "fork: strip to core packages"

---

## Phase 2: Rebrand

**Purpose:** Replace every occurrence of "opencode" with "cruxcli" across the entire codebase. This is mechanical but must be thorough.

### 2A. Central App Name

**File:** `packages/cruxcli/src/global/index.ts` line 7

```typescript
// Before:
const app = "opencode"
// After:
const app = "cruxcli"
```

This single change controls all XDG paths automatically.

### 2B. Environment Variables

**File:** `packages/cruxcli/src/flag/flag.ts`

Rename all 40+ `OPENCODE_*` env vars to `CRUXCLI_*`. No fallback to `OPENCODE_*`.

### 2C. Config Paths

**Files:** `src/config/paths.ts`, `src/config/config.ts`

| Before | After |
|--------|-------|
| `.opencode/` | `.cruxcli/` |
| `opencode.json` | `cruxcli.json` |
| `opencode.jsonc` | `cruxcli.jsonc` |
| `/Library/Application Support/opencode` | `/Library/Application Support/cruxcli` |
| `C:\ProgramData\opencode` | `C:\ProgramData\cruxcli` |
| `/etc/opencode` | `/etc/cruxcli` |

### 2D. Binary

| Before | After |
|--------|-------|
| `packages/opencode/bin/opencode` | `packages/cruxcli/bin/cruxcli` |
| `package.json` `"bin"` field: `"opencode": "bin/opencode"` | `"cruxcli": "bin/cruxcli"` |

### 2E. Package Names

| Before | After |
|--------|-------|
| `@opencode-ai/plugin` | `@cruxcli/plugin` |
| `@opencode-ai/sdk` | `@cruxcli/sdk` |
| `@opencode-ai/util` | `@cruxcli/util` |
| `@opencode-ai/script` | `@cruxcli/script` |
| `opencode` (core package) | `cruxcli` |

### 2F. HTTP Headers + User-Facing Strings

- `x-opencode-client` -> `x-cruxcli-client`
- TUI header, help text, ASCII logo, error messages
- About/version output

### 2G. Test Fixtures

Update all test snapshots and fixtures referencing "opencode" paths, env vars, or config names.

### 2H. Comprehensive Grep Verification

After all renames:
```bash
grep -ri "opencode" packages/ --include="*.ts" --include="*.json" --include="*.md" | grep -v node_modules | grep -v ".git"
```

Target: **zero occurrences** (except possibly in a FORK_ORIGIN.md noting the upstream source).

### Checklist — Phase 2

- [x] 2.1 App name constant: `opencode` -> `cruxcli`
- [x] 2.2 Env vars: all `OPENCODE_*` -> `CRUXCLI_*` (40+ vars)
- [x] 2.3 Config paths: `.opencode/` -> `.cruxcli/`, config file names
- [x] 2.4 Binary: rename file + package.json bin field
- [x] 2.5 Package names: `@opencode-ai/*` -> `@cruxcli/*`
- [x] 2.6 HTTP headers + user-facing strings
- [x] 2.7 Test fixtures updated
- [x] 2.8 Comprehensive grep: zero "opencode" occurrences in source
- [x] 2.9 `bun install` succeeds
- [x] 2.10 `bun test` passes
- [x] 2.11 Git commit: "rebrand: opencode -> cruxcli"

---

## Phase 3: Prompt Replacement

**Purpose:** Replace OpenCode's default prompts with Crux mode-driven prompts. These are the 6 injection points identified in the ROADMAP.

**File:** `packages/cruxcli/src/session/prompt.ts` (1,961 lines)

### 3A. Prompt Replacements

| # | Prompt Point | Current | Target |
|---|-------------|---------|--------|
| 1 | Plan mode reminder | 200-word "STRICTLY FORBIDDEN" block | 40-word positive framing |
| 2 | Build-switch reminder | Verbose | Single sentence |
| 3 | Max-steps prompt | Step-count limits | Crux token-budget pointer (Phase 5) |
| 4 | Mid-loop user message wrapping | `<system-reminder>` tags | Removed |
| 5 | Structured output prompt | 90 words | 40 words |
| 6 | Agent generation meta-prompt | CruxCLI defaults | Crux mode design rules |

### 3B. Mode Prompt Injection Point

Add a native integration point where Crux's active mode prompt is injected into the system prompt. Currently the bridge does this via `experimental.chat.system.transform`. In the fork, this becomes a direct call in `prompt.ts` that:

1. Reads `.crux/sessions/state.json` for the active mode
2. Reads the mode prompt from `~/.crux/modes/<mode>.md`
3. Prepends it to the system prompt

### Checklist — Phase 3

- [x] 3.1 Replace plan mode reminder (200 words → 40 words positive framing)
- [x] 3.2 Replace build-switch reminder (→ single sentence)
- [x] 3.3 Replace max-steps prompt (→ token-budget pointer)
- [x] 3.4 Remove `<system-reminder>` wrapping from mid-loop messages
- [x] 3.5 Replace structured output prompt (90 → 40 words)
- [x] 3.6 Replace agent generation meta-prompt
- [x] 3.7 Add native mode prompt injection in prompt.ts
- [x] 3.8 Tests for all prompt replacements
- [x] 3.9 Tests for mode prompt injection
- [x] 3.10 `bun test` passes

---

## Phase 4: Bridge Absorption

**Purpose:** Move the bridge plugin's functionality into the fork's source code. The standalone `crux-bridge.js` is retired.

### 4A. What the Bridge Does (3 hooks)

| Hook | Function | Absorption Target |
|------|----------|------------------|
| `experimental.chat.system.transform` | Injects mode prompt, reformats XML env blocks, appends session context | `prompt.ts` — native system prompt construction |
| `experimental.chat.messages.transform` | Strips `<system-reminder>` tags | `prompt.ts` or message handling — already covered by Phase 3.4 |
| `chat.params` | Sets temperature/topP per mode type | `session/llm.ts` or config — mode-specific model params |

### 4B. Temperature/TopP per Mode

Add mode-aware model parameters:
- Think modes: temperature 0.6, topP 0.95
- No-think modes: temperature 0.7, topP 0.8

Read the mode type from `.crux/sessions/state.json` (the `active_mode` field maps to a mode file that declares think/no_think).

### 4C. Session Context Injection

The bridge appends session context (working_on, key_decisions, pending) to the system prompt. This moves into `prompt.ts` as a native feature.

### Checklist — Phase 4

- [x] 4.1 Mode prompt injection working natively (not via plugin hook)
- [x] 4.2 XML env block reformatting moved to prompt.ts
- [x] 4.3 Session context (working_on, decisions, pending) appended to system prompt
- [x] 4.4 Mode-aware temperature/topP in LLM config
- [x] 4.5 `<system-reminder>` stripping confirmed (Phase 3.4)
- [x] 4.6 Bridge plugin marked as deprecated / removed
- [x] 4.7 Tests for all absorbed functionality
- [x] 4.8 `bun test` passes

---

## Phase 5: Token Budget System

**Purpose:** Replace OpenCode's step-count limits with per-mode token budgets. This is the Crux `token-budget.js` plugin concept moved into the fork.

### 5A. Design

| Feature | Implementation |
|---------|---------------|
| Per-mode token budgets | Read from mode metadata or config |
| Warning threshold | 70-80% of budget → inject warning into system prompt |
| Hard limit | 90-95% of budget → `toolChoice: none` (infrastructure enforcement, not prompt instructions) |
| Tracking | Count tokens per mode per session |

### 5B. Replaces

The max-steps prompt in prompt.ts (Phase 3.3) currently limits by step count. This replaces it with token-based limits that scale with mode complexity.

### Checklist — Phase 5

- [x] 5.1 Token tracking per mode per session
- [x] 5.2 Warning injection at 70-80% threshold
- [x] 5.3 Hard limit at 90-95% via toolChoice: none
- [x] 5.4 Per-mode budget configuration
- [x] 5.5 Tests for token tracking
- [x] 5.6 Tests for warning injection
- [x] 5.7 Tests for hard limit enforcement
- [x] 5.8 `bun test` passes

---

## Phase 6: Build + Verify

**Purpose:** Compile the forked binary and verify everything works end-to-end.

### 6A. Binary Compilation

```bash
# Bun single-file compilation
bun build packages/cruxcli/src/index.ts --compile --outfile cruxcli
```

Verify: `./cruxcli --version` outputs CruxCLI version.

### 6B. End-to-End Verification

| Check | How |
|-------|-----|
| Binary launches | `./cruxcli --help` shows CruxCLI help text |
| Config dir created | Launch creates `.cruxcli/` (not `.opencode/`) |
| Env vars work | `CRUXCLI_CONFIG_DIR` respected |
| No "opencode" in output | `./cruxcli --help 2>&1 \| grep -i opencode` returns nothing |
| Crux MCP connects | Configure `.claude/mcp.json`, verify MCP tools available |
| Mode prompt injected | Start session, verify active mode prompt appears in system prompt |
| Session context flows | Update `.crux/sessions/state.json`, verify context appears |
| Token budget works | Run past 70% threshold, verify warning appears |

### 6C. Full Test Suite

```bash
bun test
# All tests pass with cruxcli naming
```

### 6D. Coverage Verification

Target: 100% on new/modified code. Existing OpenCode tests adapted.

### Checklist — Phase 6

- [x] 6.1 Binary compiles: `cruxcli` binary produced
- [x] 6.2 `cruxcli --help` shows correct branding
- [x] 6.3 `cruxcli --version` shows CruxCLI version
- [x] 6.4 Config dir `.cruxcli/` created on launch
- [x] 6.5 `CRUXCLI_*` env vars work
- [x] 6.6 Zero "opencode" in any output
- [x] 6.7 Crux MCP server connects and lists tools
- [x] 6.8 Mode prompt injection works end-to-end
- [x] 6.9 Session context flows through to system prompt
- [x] 6.10 Token budget warning triggers at threshold
- [x] 6.11 Full test suite passes
- [x] 6.12 Coverage on new/modified code ≥ 100%
- [x] 6.13 Git commit: "v0.2.0: CruxCLI hard fork complete"

---

## Progress Tracker

**Phase 1: Fork + Strip (7 items)**
- [x] 1.1 — 1.7

**Phase 2: Rebrand (11 items)**
- [x] 2.1 — 2.11

**Phase 3: Prompt Replacement (10 items)**
- [x] 3.1 — 3.10

**Phase 4: Bridge Absorption (8 items)**
- [x] 4.1 — 4.8

**Phase 5: Token Budget (8 items)**
- [x] 5.1 — 5.8

**Phase 6: Build + Verify (13 items)**
- [x] 6.1 — 6.13

**Total: 57 checkboxes**

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Stripped packages have hidden deps on kept packages | Build breaks | Verify `bun install && bun test` after stripping, before any renaming |
| Env var rename (OPENCODE_* -> CRUXCLI_*) breaks existing Crux bridge | Bridge stops working | Bridge is being retired (Phase 4), so this is expected |
| Bun compilation fails on stripped monorepo | No binary | Test compilation early (after Phase 2) to catch issues before heavy prompt work |
| prompt.ts is 1,961 lines | Easy to break something | Make targeted replacements, not full rewrites. Test after each change. |
| Token tracking adds latency | Slow responses | Track tokens asynchronously, don't block on counting |

---

## Definition of Done

1. `cruxcli` binary compiles and launches
2. Zero occurrences of "opencode" in source or output
3. All config uses `.cruxcli/`, `CRUXCLI_*`, `cruxcli.json`
4. Crux mode prompts injected natively (no bridge plugin needed)
5. Session context flows through to system prompt
6. Token budget system replaces step-count limits
7. Crux MCP server connects and operates
8. Full test suite passes
9. All new/modified code at 100% coverage
10. Bridge plugin retired
