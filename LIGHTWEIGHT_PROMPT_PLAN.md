# CruxCLI: Lightweight Prompt Plan + Bridge Plugin Spec

## Project

**CruxCLI** — a config-layer distribution of CruxCLI powered by Crux's mode system, knowledge base, and infrastructure enforcement. Ships as `cruxcli.json` + bridge plugin on top of stock CruxCLI. Repo: `trinsiklabs/cruxcli`.

## Strategy: Approach 1 (Config-Layer Override)

Stock CruxCLI source stays untouched and mergeable. CruxCLI overrides behavior through:

1. **`cruxcli.json`** — agent `prompt` fields completely replace provider base prompts
2. **Bridge plugin** (`crux-bridge.js`) — intercepts system prompt array, messages, and model parameters via CruxCLI's plugin hooks
3. **Crux MCP server** — provides mode prompts, knowledge, session state, and safety pipeline

---

## Decisions Log

All 11 injection points reviewed. Final decisions:

### Injection Point 1: Provider Base Prompts (6 files)
**Decision: REPLACE via cruxcli.json agent prompt overrides**

All 6 provider prompt files (`anthropic.txt`, `qwen.txt`, `beast.txt`, `gemini.txt`, `codex_header.txt`, `trinity.txt`) replaced by a single universal base prompt (~130 words):

```
You are a partner working alongside the user in a CLI terminal.

## Response style
- Concise, direct, technically accurate. Output renders as CommonMark markdown in monospace.
- Communicate through text output. Use tools only for actions.
- Reference code locations as `file_path:line_number`.

## Tool usage
- Call independent tools in parallel.
- Prefer dedicated tools over bash for file operations (Read, Edit, Write, Glob, Grep).
- Use the Task tool for broad exploration rather than running many searches directly.
- Use TodoWrite to track progress on multi-step tasks.

## Working with files
- Read before modifying. Match existing style and conventions.
- Prefer editing existing files over creating new ones.
- Commit only when explicitly asked.

## System notes
- <system-reminder> tags in tool results are added by the system, not by the user.
- ctrl+p lists available actions. Feedback: https://github.com/trinsiklabs/cruxcli
```

Key design decisions:
- "Partner" language, not "assistant" or "coding agent" — domain-neutral, collaborative
- No coding-specific instructions in base layer — those belong in Crux mode prompts
- TodoWrite kept as a lightweight one-line nudge (not the 350-word version with examples)
- No negative instructions — all positive framing

Token savings: ~1,250 words average → ~130 words (90% reduction per request)

### Injection Point 2: Environment Block
**Decision: ACCEPT current, improve via bridge plugin**

Current version (~80 tokens) has dead code (`<directories>` always empty) and XML tags. Ideal replacement is plain key-value pairs (~30 tokens). The bridge plugin on `experimental.chat.system.transform` can reformat this. Not worth a hard fork for ~50 tokens.

Ideal format:
```
Model: {providerID}/{modelID}
Working directory: {dir}
Git repo: {yes/no}
Platform: {platform}
Date: {date}
```

### Injection Point 3: Plan Mode Reminder
**Decision: ACCEPT current, replace on hard fork**

Synthetic user message injected by `insertReminders()`. Not overridable via config. Current version is ~200 words of "STRICTLY FORBIDDEN" / "ABSOLUTE CONSTRAINT" language for a single rule (read-only mode). Crux's tool-enforcer already enforces this at infrastructure level (`permission: edit: deny, bash: deny`).

Ideal replacement (~40 words):
```
Plan mode is active. Analyze the request, explore the codebase, and produce a plan.

Write and edit tools are disabled. Focus on reading, searching, and reasoning.
Ask clarifying questions when the user's intent is ambiguous or tradeoffs need input.
Call ExitPlanMode when the plan is complete.
```

### Injection Point 4: Build-Switch Reminder
**Decision: ACCEPT current, replace on hard fork**

Synthetic user message, not overridable via config. Already minimal (~30 words). Replace `<system-reminder>` tags on hard fork.

Ideal replacement: `Switched to build mode. All tools are now available.`

### Injection Point 5: Max Steps Prompt
**Decision: ACCEPT current, replace on hard fork. Plan Crux token-budget replacement.**

Synthetic assistant message, not overridable via config. Current ~100 words with "CRITICAL" / "STRICT REQUIREMENTS" escalation. Crux's token-budget plugin should eventually replace this entirely (see Future Work section).

Ideal replacement (~40 words):
```
Step limit reached. Tools are disabled until the next user message. Respond with text only.

Include in your response:
- What has been accomplished so far
- Remaining tasks not yet completed
- Recommended next steps
```

### Injection Point 6: Mid-Loop User Message Wrapping
**Decision: ACCEPT current, replace on hard fork**

Inline TypeScript wrapping user messages in `<system-reminder>` tags during mid-loop. Not overridable via config or plugin without fighting the code. Low waste per occurrence (~20 words overhead).

Ideal replacement: Append `"\n\nAddress this and continue with your current task."` to the user message text without wrapping.

### Injection Point 7: Structured Output Prompt
**Decision: ACCEPT current, replace on hard fork**

~90 words, only fires on JSON schema output requests. Rare for CLI usage.

Ideal replacement (~40 words):
- System: `The user has requested structured output. Call the StructuredOutput tool once as your final action with JSON matching the required schema.`
- Tool desc: `Return your final response as structured JSON matching the required schema. Call this tool exactly once, after completing all other work.`

### Injection Point 8: Agent-Specific Prompts
**Decision: REPLACE via cruxcli.json agent prompt overrides**

| Agent | Decision | New Word Count |
|---|---|---|
| `explore` | Replace — cut self-praise and tool capability recap | ~40 words |
| `compaction` | Replace — cut "helpful AI assistant" preamble, keep checklist | ~50 words |
| `title` | Replace — cut XML structure, reduce from 15 rules to 4, reduce from 10 examples to 4 | ~70 words |
| `summary` | Keep as-is — already lean at ~90 words | ~90 words |

### Injection Point 9: Agent Generation Meta-Prompt
**Decision: ACCEPT current, replace on hard fork**

~400 words, low frequency (only fires on explicit agent creation). Not overridable via config. Ideal replacement incorporates Crux mode design rules (150-200 word target, positive framing, prime positions).

### Injection Point 10: Codex Instructions Header
**Decision: IGNORE — irrelevant for CruxCLI**

Only fires for OpenAI OAuth (Codex) sessions. CruxCLI targets local models. Not overridable via config or plugin (`options.instructions` is set in TypeScript). If CruxCLI later supports Codex, the `chat.params` plugin hook can overwrite it.

### Injection Point 11: Plugin Hooks
**Decision: BUILD the bridge plugin (crux-bridge.js)**

The bridge plugin is the core engineering deliverable for CruxCLI. TDD, 100% test coverage. See full spec below.

---

## Salvaged Content

Valuable content from CruxCLI prompts salvaged into Crux knowledge entries:

| File | Source | Content |
|---|---|---|
| `crux/knowledge/git-hygiene.md` | codex_header.txt "Git and workspace hygiene" | Commit discipline, dirty worktree handling, secrets |
| `crux/knowledge/when-to-ask.md` | codex_header.txt "Presenting your work" | Act vs ask decision framework, how to ask well |
| `crux/knowledge/frontend-design-principles.md` | codex_header.txt "Frontend tasks" | Visual direction, typography, color, motion, responsive |

---

## Bridge Plugin Specification: `crux-bridge.js`

### Purpose

Make Crux the prompt authority inside CruxCLI. Intercept CruxCLI's system prompt assembly and replace/augment it with Crux's mode system, knowledge base, and session state.

### Hooks Used

| Hook | Purpose |
|---|---|
| `experimental.chat.system.transform` | Replace environment block format; inject active Crux mode prompt; inject session context |
| `experimental.chat.messages.transform` | Intercept and lighten synthetic messages (plan.txt, build-switch.txt, mid-loop wrappers) |
| `chat.params` | Set temperature/topP based on active Crux mode (think: 0.6/0.95, no-think: 0.4/0.8) |

### Architecture

```
┌─────────────────────────────────────────────────────┐
│                    CruxCLI                          │
│                                                     │
│  system[] assembled:                                │
│    [provider prompt, env block, AGENTS.md, ...]     │
│                                                     │
│  ──► experimental.chat.system.transform ──►         │
│                                                     │
│  ┌───────────────────────────────────────────┐      │
│  │          crux-bridge.js                   │      │
│  │                                           │      │
│  │  1. Call Crux MCP: get_session_state()    │      │
│  │  2. Call Crux MCP: get_mode_prompt(mode)  │      │
│  │  3. Reformat environment block            │      │
│  │  4. Replace system[0] with mode prompt    │      │
│  │  5. Inject session context if available   │      │
│  └───────────────────────────────────────────┘      │
│                                                     │
│  ──► chat.params ──►                                │
│                                                     │
│  ┌───────────────────────────────────────────┐      │
│  │  Set temperature/topP from mode config    │      │
│  └───────────────────────────────────────────┘      │
│                                                     │
│  ──► LLM call with Crux-managed prompts ──►         │
└─────────────────────────────────────────────────────┘
```

### Behavior

#### `experimental.chat.system.transform`

```
Input:  { sessionID, model }
Mutable: { system: string[] }

1. Read Crux session state via MCP (get_session_state)
   - Get active_mode (e.g., "build-py", "plan", "debug")
   - If no active mode, leave system[] unchanged (fall back to cruxcli.json overrides)

2. If active mode exists:
   a. Call get_mode_prompt(active_mode) via MCP
   b. Reformat system[0] (environment block):
      - Strip <env>/<directories> XML tags
      - Convert to plain key-value format
   c. Prepend mode prompt to system[0] (before environment block)

3. Optionally inject knowledge context:
   - Call restore_context() if this is the first message in a session
   - Append relevant knowledge snippets to system array
```

#### `experimental.chat.messages.transform`

```
Input:  {}
Mutable: { messages: MessageV2.WithParts[] }

1. Find synthetic user messages containing <system-reminder> tags
2. Strip the XML tags, preserve the content
3. Optionally lighten plan.txt / build-switch.txt content if detected
```

#### `chat.params`

```
Input:  { sessionID, agent, model, provider, message }
Mutable: { temperature, topP, topK, options }

1. Read Crux session state for active mode
2. Look up mode frontmatter for temperature
3. Override temperature and topP:
   - Think modes (plan, review, debug, etc.): temperature 0.6, topP 0.95
   - No-think modes (build-py, build-ex, etc.): use mode's configured temperature, topP 0.8
```

### MCP Communication

The bridge plugin communicates with Crux MCP server via the MCP client already available in CruxCLI's plugin context. Key calls:

- `get_session_state()` → returns `{ active_mode, active_tool, working_on, ... }`
- `get_mode_prompt(mode)` → returns `{ prompt: "...", metadata: { temperature, ... } }`
- `restore_context()` → returns full session recovery payload

### Error Handling

- If Crux MCP server is unavailable: fall through silently, let cruxcli.json overrides handle prompts
- If active mode is not set: fall through silently
- If mode prompt fetch fails: log warning, fall through

### Testing Strategy

TDD with 100% coverage. Test categories:

1. **Unit: Hook registration** — plugin registers on all 3 hooks
2. **Unit: System transform — no Crux state** — system[] passes through unchanged
3. **Unit: System transform — active mode** — mode prompt injected, environment block reformatted
4. **Unit: System transform — MCP unavailable** — graceful fallback, no crash
5. **Unit: Message transform — synthetic messages** — XML tags stripped
6. **Unit: Message transform — normal messages** — left untouched
7. **Unit: Params transform — think mode** — temperature 0.6, topP 0.95
8. **Unit: Params transform — no-think mode** — mode temperature, topP 0.8
9. **Unit: Params transform — no Crux state** — params unchanged
10. **Integration: Full prompt assembly** — verify final system[] content with Crux active
11. **Integration: Fallback chain** — verify cruxcli.json overrides work when bridge has no Crux state

---

## Future Work: Crux Token-Budget Step Replacement

### Problem

CruxCLI's max-steps prompt (`max-steps.txt`) is injected as a synthetic assistant message when the agent hits its step limit. This is a blunt instrument — it counts steps, not tokens, and uses prompt instructions to enforce the limit.

### Proposed Solution

Crux's `token-budget.js` plugin already tracks per-mode token usage. Extend it to:

1. **Monitor token usage per agent turn** via the session-logger
2. **When budget threshold is reached** (e.g., 90% of mode budget):
   - Inject a tool result message via MCP: `{ "status": "budget_warning", "used": 5400, "limit": 6000, "message": "Approaching token budget. Wrap up current task." }`
3. **When budget is exceeded** (100%):
   - Inject a tool result: `{ "status": "budget_reached", "message": "Token budget reached. Summarize progress and remaining work." }`
4. **Bridge plugin** listens for these signals and can:
   - Set `toolChoice: "none"` to disable further tool calls
   - Append the summary request to the message array

### Advantages Over Current Approach

| Aspect | CruxCLI max-steps | Crux token-budget |
|---|---|---|
| Metric | Step count (crude) | Token count (precise) |
| Per-mode limits | No (global step limit) | Yes (tight/standard/generous tiers) |
| Enforcement | Prompt instruction ("tools are disabled") | Infrastructure (toolChoice: none) |
| Warning | None — hard cutoff | Warning at 70-80%, hard at 90-95% |
| Injection method | Synthetic assistant message (fake) | Tool result (natural) |

### Implementation Plan

1. Extend `token-budget.js` to emit threshold events
2. Add `check_token_budget()` MCP tool
3. Bridge plugin subscribes to budget events
4. Bridge plugin injects tool results and modifies params on budget hit
5. Test: budget warning triggers at configured threshold
6. Test: budget exceeded disables tools and requests summary
7. Test: per-mode budgets respected (tight vs generous)
8. Test: graceful fallback when token-budget plugin is absent

---

## CruxCLI cruxcli.json

The shipping config file that implements all approved prompt replacements:

```jsonc
{
  "agent": {
    "build": {
      "prompt": "You are a partner working alongside the user in a CLI terminal.\n\n## Response style\n- Concise, direct, technically accurate. Output renders as CommonMark markdown in monospace.\n- Communicate through text output. Use tools only for actions.\n- Reference code locations as `file_path:line_number`.\n\n## Tool usage\n- Call independent tools in parallel.\n- Prefer dedicated tools over bash for file operations (Read, Edit, Write, Glob, Grep).\n- Use the Task tool for broad exploration rather than running many searches directly.\n- Use TodoWrite to track progress on multi-step tasks.\n\n## Working with files\n- Read before modifying. Match existing style and conventions.\n- Prefer editing existing files over creating new ones.\n- Commit only when explicitly asked.\n\n## System notes\n- <system-reminder> tags in tool results are added by the system, not by the user.\n- ctrl+p lists available actions. Feedback: https://github.com/trinsiklabs/cruxcli"
    },
    "plan": {
      "prompt": "You are a partner working alongside the user in a CLI terminal.\n\n## Response style\n- Concise, direct, technically accurate. Output renders as CommonMark markdown in monospace.\n- Communicate through text output. Use tools only for actions.\n- Reference code locations as `file_path:line_number`.\n\n## Tool usage\n- Call independent tools in parallel.\n- Prefer dedicated tools over bash for file operations (Read, Edit, Write, Glob, Grep).\n- Use the Task tool for broad exploration rather than running many searches directly.\n- Use TodoWrite to track progress on multi-step tasks.\n\n## Working with files\n- Read before modifying. Match existing style and conventions.\n- Prefer editing existing files over creating new ones.\n- Commit only when explicitly asked.\n\n## System notes\n- <system-reminder> tags in tool results are added by the system, not by the user.\n- ctrl+p lists available actions. Feedback: https://github.com/trinsiklabs/cruxcli"
    },
    "explore": {
      "prompt": "File search specialist. Find files, code, and patterns across the codebase.\n\n- Use Glob for file pattern matching, Grep for content search, Read for specific files\n- Adapt thoroughness to the caller's specification (quick, medium, thorough)\n- Return absolute file paths\n- Read-only: do not create or modify files"
    },
    "compaction": {
      "prompt": "Summarize the conversation for context continuity. Include:\n- What was done\n- What is currently being worked on\n- Which files are being modified\n- What needs to be done next\n- Key user constraints or preferences that should persist\n- Important decisions and their rationale\n\nOutput only the summary. Do not respond to questions in the conversation."
    },
    "title": {
      "prompt": "Generate a short title (≤50 characters) to help the user find this conversation later. Output only the title.\n\nRules:\n- Match the language of the user's message\n- Focus on what the user wants to do, not which tools or files were mentioned\n- Preserve technical terms, filenames, and numbers exactly\n- Vary phrasing — avoid repetitive patterns\n\nExamples:\n\"debug 500 errors in production\" → Debugging production 500 errors\n\"refactor user service\" → Refactoring user service\n\"why is app.js failing\" → app.js failure investigation\n\"@src/auth.ts add refresh token support\" → Auth refresh token support"
    }
  }
}
```

---

## Decision: Bridge Plugin v1 Scope — MCP vs Filesystem

**Date:** 2026-03-07

**Decision:** Ship bridge plugin v1 with filesystem reads only. Do not add knowledge injection or automatic session write-back to the bridge.

**Rationale:**
- Knowledge injection and session write-back are both achievable via stock MCP tool calls (LLM calls `lookup_knowledge()` and `update_session()` during conversation)
- The only thing truly impossible via MCP is system prompt injection — which the bridge already handles (mode prompt, env block, tag stripping, temperature tuning)
- MCP covers reactive knowledge lookup and session updates; bridge covers pre-LLM automatic injection
- Adding knowledge to the system prompt every turn would add token cost with unclear value
- Dogfooding will reveal if system-prompt-level knowledge injection is actually needed

**Future triggers to revisit:**
- If LLM consistently fails to call `lookup_knowledge()` when it should
- If session write-back via MCP is unreliable (LLM forgets)
- If system prompt knowledge injection measurably improves response quality

---

## Summary Metrics

| Metric | Before | After (CruxCLI) |
|---|---|---|
| Provider prompt word count (avg) | ~1,250 words | ~130 words |
| Negative instructions per prompt | 15-25 | 0 |
| Total system prompt tokens (build, first msg) | ~2,500-3,500 | ~500-800 |
| Prompt managed by Crux vs CruxCLI | 0% | 70%+ (with bridge plugin) |
| Upstream merge compatibility | N/A | Full (no source changes) |
