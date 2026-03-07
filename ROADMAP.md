# CruxCLI Roadmap

## Vision

CruxCLI is a config-layer distribution of [OpenCode](https://github.com/anomalyco/opencode) powered by the Crux prompt engine. It replaces OpenCode's default prompt system with Crux's mode-driven architecture — dynamic mode prompts, session state, knowledge injection, and safety infrastructure — without modifying OpenCode's source.

The end goal is a branded, Crux-native coding CLI that ships as a standalone binary with full control over prompts, branding, and behavior.

---

## Completed

### Prompt Analysis and Decisions
- Audited all 11 OpenCode prompt injection points
- Decided per-point: REPLACE (via config), ACCEPT (for now), or BUILD (bridge plugin)
- Designed universal base prompt (~130 words, 90% reduction from OpenCode defaults)
- Salvaged valuable content from OpenCode prompts into Crux knowledge entries

### Bridge Plugin (`crux-bridge.js`)
- Built with TDD — 28 tests, 100% line coverage, 97.5% branch, 92.3% function
- Three hooks:
  - `experimental.chat.system.transform` — injects active Crux mode prompt, reformats XML env blocks, appends session context
  - `experimental.chat.messages.transform` — strips `<system-reminder>` tags
  - `chat.params` — sets temperature/topP per mode type (think vs no-think)
- Dependency-injected IO for testability (no mocking needed)
- Zero runtime dependencies (pure JS, Node built-in test runner)

### OpenCode Configuration
- Agent prompt overrides for `build`, `plan`, `explore`, `compaction`, `title`
- Crux MCP server registered with Ollama provider
- Bridge plugin auto-discovered via symlink chain into OpenCode's plugins directory
- Interaction rules: numbered lists, sequential review with user confirmation

### Architecture Decision: v1 Scope
- Bridge reads filesystem only (same source as Crux MCP internals)
- Knowledge injection and session write-back handled by LLM calling MCP tools directly
- System prompt injection is the only capability impossible via MCP — bridge handles it

---

## Current Phase: Dogfooding

Running CruxCLI (stock OpenCode + config overrides + bridge plugin) against the `local_llm` project to validate:

1. Bridge plugin loads and transforms prompts correctly
2. Mode switching works end-to-end (Crux MCP sets mode, bridge injects prompt)
3. Agent prompt overrides produce good results with local models (Ollama)
4. Session state flows through: Crux hooks -> state.json -> bridge -> system prompt
5. No regressions from reduced prompt sizes

---

## Planned: Approach 2 (Source Fork)

Config-layer (Approach 1) has hard limits. A maintained fork unlocks:

### Branding
- Binary name: `crux` instead of `opencode`
- Launch banner, TUI header, status bar
- Custom about/help text

### Prompt Replacements (currently "ACCEPT, replace on hard fork")
- Plan mode reminder — replace 200-word "STRICTLY FORBIDDEN" block with 40-word positive framing
- Build-switch reminder — replace with single sentence
- Max-steps prompt — replace with Crux token-budget system
- Mid-loop user message wrapping — remove `<system-reminder>` tags
- Structured output prompt — reduce from 90 to 40 words
- Agent generation meta-prompt — incorporate Crux mode design rules

### Token-Budget System
- Replace step-count limits with per-mode token budgets
- Warning at threshold (70-80%), hard limit at 90-95%
- Infrastructure enforcement via `toolChoice: none` (not prompt instructions)
- Crux `token-budget.js` plugin already tracks per-mode usage

### Deeper Integration
- Bridge plugin calls MCP directly instead of filesystem reads (if dogfooding reveals need)
- System-prompt-level knowledge injection (if LLM fails to call `lookup_knowledge()` reliably)
- Automatic session write-back through bridge (if MCP-based write-back is unreliable)

---

## Release Plan

1. **v0.1** (current) — Config-layer distribution. Dogfooding phase. No commits until validated.
2. **v0.2** — Approach 2 fork. Branding + synthetic message replacements.
3. **v0.3** — Token-budget integration. Per-mode budget enforcement.
4. **v1.0** — Standalone `crux` binary. Full prompt authority. Published distribution.
