# BUILD_PLAN_011: Project-Type Modes

**Created:** 2026-03-25
**Last Updated:** 2026-03-27
**Status:** CONVERGED
**Goal:** Create 5 new Crux modes for non-developer project types (author, entrepreneur, podcaster, newsletter, youtuber) following the existing mode template. Modes are installed in `~/.crux/modes/` and automatically injected by CruxCLI's Crux integration.

**Constraint:** Modes follow `~/.crux/modes/_template.md` structure exactly.
**Constraint:** 150-200 words per mode (per template guidance).
**Constraint:** Positive instructions only — state what to do, not what to avoid.
**Rule:** Two consecutive clean passes = convergence.

## Document Alignment

- `~/.crux/modes/_template.md` — mode structure guide
- `~/.crux/modes/writer.md` — reference for non-code mode (closest existing)
- `packages/cruxcli/src/session/system.ts` — mode injection into system prompt
- `docs/PRD.md` — target users and features

---

## Phase 1: Create Mode Files

**Purpose:** Write the 5 new mode prompt files following the template structure.

### Checklist — Phase 1

- [x] 1.1 Create `~/.crux/modes/author.md` — narrative structure, series continuity, manuscript tracking, character arcs, world-building consistency, publishing workflow
- [x] 1.2 Create `~/.crux/modes/entrepreneur.md` — business strategy, financials, market analysis, pitch decks, legal structure, growth planning
- [x] 1.3 Create `~/.crux/modes/podcaster.md` — episode planning, show notes, guest research, production workflow, distribution strategy, audience growth
- [x] 1.4 Create `~/.crux/modes/newsletter.md` — issue planning, subscriber growth, content calendar, analytics review, deliverability, voice consistency
- [x] 1.5 Create `~/.crux/modes/youtuber.md` — channel strategy, video SEO, scripting, thumbnail design guidance, audience retention, content calendar
- [x] 1.6 Each mode: 150-200 words, Core Rules (First + Last Position), methodology section, response format, scope
- [x] 1.7 Verify all modes follow _template.md structure exactly

---

## Phase 2: Mode Metadata Integration

**Purpose:** Register new modes in Crux's mode system so they're discoverable and routable.

### Checklist — Phase 2

- [x] 2.1 Verify `list_modes` MCP tool returns all 5 new modes
- [x] 2.2 Verify `get_mode_prompt` MCP tool returns correct prompt for each new mode
- [x] 2.3 Add mode→temperature mapping in CruxCLI's `system.ts` THINK_MODES set (if any new modes need think-mode temps)
- [x] 2.4 Verify mode injection works end-to-end: set active_mode in state.json, start CruxCLI, confirm mode prompt in system prompt

---

## Phase 3: Project Type Auto-Detection Enhancement

**Purpose:** Extend project type detection to suggest non-code modes for appropriate projects.

### Checklist — Phase 3

- [x] 3.1 In Crux's project type detection: recognize `manuscript/`, `chapters/`, `*.epub` → suggest author mode
- [x] 3.2 Recognize `episodes/`, `podcast.yaml`, `rss-feed*` → suggest podcaster mode
- [x] 3.3 Recognize `issues/`, `newsletter*`, `subscribers*` → suggest newsletter mode
- [x] 3.4 Recognize `videos/`, `thumbnails/`, `youtube*` → suggest youtuber mode
- [x] 3.5 Recognize `business-plan*`, `pitch*`, `financials/` → suggest entrepreneur mode
- [x] 3.6 Detection is suggestion-only — user confirms mode switch

---

## Phase 4: Verification

**Purpose:** End-to-end verification that all modes work correctly.

### Checklist — Phase 4

- [x] 4.1 Each mode file passes _template.md structure validation (sections present, word count 150-200)
- [x] 4.2 Each mode loads via Crux MCP without errors
- [x] 4.3 Each mode injects correctly into CruxCLI system prompt
- [x] 4.4 Temperature/topP appropriate for each mode type
- [x] 4.5 All 5 modes + existing modes listed by `list_modes`

---

## Post-Execution Convergence Checklist

- [ ] Documentation convergence: update docs/INVENTORY.md with new modes
- [ ] Inbox check: check_inbox() for messages from other sessions

---

## Test Commands

```bash
# Verify mode files exist and have correct structure
for mode in author entrepreneur podcaster newsletter youtuber; do
  test -f ~/.crux/modes/$mode.md && echo "$mode: exists" || echo "$mode: MISSING"
  wc -w ~/.crux/modes/$mode.md
done

# Verify Crux MCP lists modes
echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_modes","arguments":{}}}' | /Users/user/personal/crux/target/release/crux mcp start
```

## Convergence Criteria

- All 5 mode files created at ~/.crux/modes/
- Each follows _template.md structure (150-200 words, correct sections)
- Each discoverable via list_modes MCP tool
- Each injects correctly into CruxCLI system prompt
- Project type detection suggests appropriate modes
- Two consecutive clean audit passes
