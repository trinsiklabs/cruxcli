# CruxCLI System Prompt Adjustment Guide

This document catalogs every place CruxCLI injects its own system-level prompting — independent of the LLM provider — and describes how to adjust each one as a **user**, as a **fork maintainer**, and for **local/custom LLM tuning**.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Provider Base Prompts](#2-provider-base-prompts)
3. [Environment Block](#3-environment-block)
4. [Agent-Specific Prompts](#4-agent-specific-prompts)
5. [Plan Mode Reminder](#5-plan-mode-reminder)
6. [Build-Switch Reminder](#6-build-switch-reminder)
7. [Max Steps Prompt](#7-max-steps-prompt)
8. [Mid-Loop User Message Wrapping](#8-mid-loop-user-message-wrapping)
9. [Structured Output Prompt](#9-structured-output-prompt)
10. [Codex Instructions Header](#10-codex-instructions-header)
11. [Agent Generation Meta-Prompt](#11-agent-generation-meta-prompt)
12. [Plugin Hooks](#12-plugin-hooks)
13. [Environment Variables & Flags](#13-environment-variables--flags)
14. [Prompt Assembly Order](#14-prompt-assembly-order)
15. [Recipes: Common Customization Scenarios](#15-recipes-common-customization-scenarios)

---

## 1. Architecture Overview

The system prompt is assembled across three files, then sent to the LLM as one or more `system` role messages:

| File | Responsibility |
|---|---|
| `src/session/system.ts` | Selects provider prompt + builds environment block |
| `src/session/llm.ts` | Joins provider prompt, agent prompt, user system, and instructions; calls LLM |
| `src/session/prompt.ts` | Orchestrates the loop; builds the `system[]` array from environment + AGENTS.md; injects plan/build/max-steps reminders into messages |

The assembly in `llm.ts:67-79` is:

```ts
const system = []
system.push(
  [
    ...(input.agent.prompt ? [input.agent.prompt] : isCodex ? [] : SystemPrompt.provider(input.model)),
    ...input.system,          // environment + AGENTS.md + structured output
    ...(input.user.system ? [input.user.system] : []),
  ].filter(x => x).join("\n"),
)
```

**Key insight:** If an agent has a `.prompt` field, it *replaces* the provider base prompt entirely. This is the primary override mechanism.

---

## 2. Provider Base Prompts

### What it is

`SystemPrompt.provider()` in `src/session/system.ts:19-27` selects one of six `.txt` files based on the model ID string:

| Model ID contains | File | Lines | Character |
|---|---|---|---|
| `gpt-5` | `session/prompt/codex_header.txt` | ~80 | Concise, edit-focused |
| `gpt-*` / `o1` / `o3` | `session/prompt/beast.txt` | ~148 | Aggressive autonomy, web-research heavy |
| `gemini-*` | `session/prompt/gemini.txt` | ~156 | Structured workflows, security-first |
| `claude` | `session/prompt/anthropic.txt` | ~106 | TodoWrite-heavy, professional objectivity |
| `trinity` (case-insensitive) | `session/prompt/trinity.txt` | ~80 | Same content as `codex_header.txt` |
| **Everything else** (fallback) | `session/prompt/qwen.txt` | ~98 | Minimal, concise CLI style |

### As a user (cruxcli.json)

Override the entire provider prompt for any agent by setting `prompt` in your config:

```jsonc
// cruxcli.json
{
  "agent": {
    "build": {
      "prompt": "You are a helpful coding assistant. Be concise."
    }
  }
}
```

When `agent.prompt` is set, `SystemPrompt.provider()` is **completely skipped** for that agent (see `llm.ts:72`).

You can also create a new agent that inherits nothing:

```jsonc
{
  "agent": {
    "my-local": {
      "prompt": "You are a local coding assistant running on my machine...",
      "model": "ollama/codellama",
      "mode": "primary",
      "description": "My custom local agent"
    }
  },
  "default_agent": "my-local"
}
```

### As a fork maintainer (source code)

Edit the `.txt` files directly:

- `packages/cruxcli/src/session/prompt/anthropic.txt` — Claude models
- `packages/cruxcli/src/session/prompt/beast.txt` — OpenAI GPT/o-series
- `packages/cruxcli/src/session/prompt/gemini.txt` — Google Gemini
- `packages/cruxcli/src/session/prompt/qwen.txt` — Fallback for all other models
- `packages/cruxcli/src/session/prompt/codex_header.txt` — GPT-5 / Codex / Trinity
- `packages/cruxcli/src/session/prompt/trinity.txt` — Trinity models

To add a new provider-specific prompt, edit `system.ts:19-27`:

```ts
export function provider(model: Provider.Model) {
  if (model.api.id.includes("my-local-model")) return [MY_CUSTOM_PROMPT]
  // ... existing checks
}
```

### For local LLM tuning

The **fallback** prompt (`qwen.txt`) is what your local model will receive unless its ID matches one of the specific patterns. Options:

1. **Name your model** with a string that matches an existing pattern (e.g., include `claude` in the ID) to reuse that prompt
2. **Edit `qwen.txt`** to be your universal local-model prompt
3. **Add a new branch** in `system.ts:provider()` for your model family
4. **Use the config override** (`agent.build.prompt`) to bypass all of this entirely — this is the simplest approach for local models

**Recommendations for local models:**
- Strip the TodoWrite instructions (most local models handle them poorly)
- Remove references to `WebFetch` / `WebSearch` if your model can't use them
- Simplify tool usage instructions to match your model's tool-call format
- Reduce prompt length — smaller models are more sensitive to long system prompts

---

## 3. Environment Block

### What it is

`SystemPrompt.environment()` in `src/session/system.ts:29-53` generates a block like:

```
You are powered by the model named claude-sonnet-4-5-20250929. The exact model ID is anthropic/claude-sonnet-4-5-20250929
Here is some useful information about the environment you are running in:
<env>
  Working directory: /home/user/project
  Is directory a git repo: yes
  Platform: darwin
  Today's date: Thu Mar 06 2026
</env>
<directories>
</directories>
```

This is **always injected** at `prompt.ts:652` as the first element of the `system[]` array, before AGENTS.md.

### As a user

There is **no config-level override** for this block. It is always present.

### As a fork maintainer

Edit `src/session/system.ts:29-53`. Common changes:

- **Remove model self-identification** (line 33) — useful if you don't want the model to know its own name
- **Add more environment context** — shell type, language, node version, etc.
- **Enable the directory tree** — line 43-48 has a commented-out `Ripgrep.tree()` call behind `&& false`; remove `&& false` to include a directory listing
- **Strip `<env>` XML tags** — some local models handle plain text better than XML-wrapped blocks

```ts
// Example: minimal environment for local models
export async function environment(model: Provider.Model) {
  return [
    [
      `Working directory: ${Instance.directory}`,
      `Platform: ${process.platform}`,
      `Date: ${new Date().toDateString()}`,
    ].join("\n"),
  ]
}
```

### For local LLM tuning

- Many local models don't benefit from knowing their own model ID — consider removing line 33
- The `<env>` / `<directories>` XML tags may confuse models not trained on XML-style structured prompts; switch to plain Markdown headers or key-value pairs
- If you're using a model with a small context window, this block is relatively cheap (~200 tokens) and generally worth keeping

---

## 4. Agent-Specific Prompts

### What it is

Built-in agents defined in `src/agent/agent.ts` can have a `.prompt` field. When set, this prompt **replaces** the provider base prompt entirely. The following built-in agents have hardcoded prompts:

| Agent | File | Purpose | Mode |
|---|---|---|---|
| `explore` | `src/agent/prompt/explore.txt` | File search specialist | subagent |
| `compaction` | `src/agent/prompt/compaction.txt` | Conversation summarizer | primary (hidden) |
| `title` | `src/agent/prompt/title.txt` | Session title generator | primary (hidden) |
| `summary` | `src/agent/prompt/summary.txt` | PR-style summary writer | primary (hidden) |

The `build` and `plan` agents do **not** have a `.prompt` field — they use the provider base prompt.

### As a user (cruxcli.json)

Override any agent's prompt:

```jsonc
{
  "agent": {
    "explore": {
      "prompt": "You are a codebase explorer. Use grep and glob to find files. Return absolute paths. Be thorough."
    },
    "title": {
      "prompt": "Generate a 3-5 word title. Output ONLY the title, nothing else."
    },
    "compaction": {
      "prompt": "Summarize the conversation focusing on: what was done, what files changed, what's next."
    }
  }
}
```

You can also **disable** any agent entirely:

```jsonc
{
  "agent": {
    "explore": { "disable": true }
  }
}
```

Or change the model used for a specific agent:

```jsonc
{
  "agent": {
    "title": {
      "model": "ollama/llama3",
      "temperature": 0.3
    }
  }
}
```

### As a fork maintainer

Edit the `.txt` files in `src/agent/prompt/`:

- `explore.txt` — Keep focused on search tools only
- `compaction.txt` — Critical for context window management; be careful with changes
- `title.txt` — Simple; most changes here are safe
- `summary.txt` — Affects the session summary display

To add a new built-in agent with a custom prompt, add it to the `result` object in `agent.ts:76-203`:

```ts
result["my-agent"] = {
  name: "my-agent",
  description: "Does something specific",
  prompt: MY_AGENT_PROMPT,   // import from a .txt file
  permission: PermissionNext.merge(defaults, user),
  options: {},
  mode: "subagent",
  native: true,
}
```

### For local LLM tuning

- The `explore` agent is called frequently as a subagent — keep its prompt short and directive for small models
- The `compaction` agent handles context window overflow — if your local model has a small context window, you may want a more aggressive summarization prompt
- The `title` agent uses `temperature: 0.5` by default; local models may need this adjusted via config
- Consider routing `title` and `summary` to a faster/smaller model via the `model` config field

---

## 5. Plan Mode Reminder

### What it is

When the active agent is `"plan"`, a read-only constraint prompt is injected as a **synthetic user message** (not a system message). There are two variants:

**Legacy (default):** `src/session/prompt/plan.txt` — injected at `prompt.ts:1330-1337`
```
<system-reminder>
CRITICAL: Plan mode ACTIVE - you are in READ-ONLY phase. STRICTLY FORBIDDEN:
ANY file edits, modifications, or system changes...
</system-reminder>
```

**Experimental:** Inline in `prompt.ts:1385-1402` when `CRUXCLI_EXPERIMENTAL_PLAN_MODE=true` — a longer prompt that includes plan file management, phased workflow (explore → plan → synthesize → finalize), and instructions to use the `ExitPlanMode` tool.

There is also `src/session/prompt/plan-reminder-anthropic.txt` which appears to be a reference/development artifact for the experimental plan mode.

### As a user

- **Disable plan mode entirely:** set `agent.plan.disable: true` in config
- **Override the plan prompt:** set `agent.plan.prompt` in config (but note: the plan reminder is injected *in addition to* the agent prompt, as a synthetic message)
- **Enable experimental plan mode:** set env var `CRUXCLI_EXPERIMENTAL_PLAN_MODE=true`

### As a fork maintainer

- Edit `src/session/prompt/plan.txt` for the legacy variant
- Edit the inline string at `prompt.ts:1385-1402` for the experimental variant
- The injection logic is in `insertReminders()` at `prompt.ts:1323-1402`

### For local LLM tuning

- The `<system-reminder>` XML tags may confuse models not trained on them — consider replacing with plain Markdown
- The plan mode prompt is quite long in experimental mode (~60 lines); local models may benefit from a shorter version
- Many local models struggle with the concept of "read-only mode" — you may need more explicit negative examples

---

## 6. Build-Switch Reminder

### What it is

`src/session/prompt/build-switch.txt` — injected as a synthetic user message at `prompt.ts:1340-1349` when switching from plan agent to build agent:

```
<system-reminder>
Your operational mode has changed from plan to build.
You are no longer in read-only mode.
You are permitted to make file changes, run shell commands, and utilize your arsenal of tools as needed.
</system-reminder>
```

In experimental plan mode, it may also include a reference to the plan file (`prompt.ts:1367`).

### As a user

No direct config override. This is only injected when a session transitions from plan → build.

### As a fork maintainer

Edit `src/session/prompt/build-switch.txt` and/or the inline logic at `prompt.ts:1356-1373`.

### For local LLM tuning

- This prompt is small (~5 lines) and generally benign
- Replace `<system-reminder>` tags with plain text if your model doesn't handle XML well

---

## 7. Max Steps Prompt

### What it is

`src/session/prompt/max-steps.txt` — injected as a **synthetic assistant message** at `prompt.ts:666-673` when the agent reaches its configured step limit:

```
CRITICAL - MAXIMUM STEPS REACHED
The maximum number of steps allowed for this task has been reached. Tools are disabled until next user input.
...
Response must include:
- Statement that maximum steps for this agent have been reached
- Summary of what has been accomplished so far
- List of any remaining tasks that were not completed
- Recommendations for what should be done next
```

### As a user

Control the step limit per agent:

```jsonc
{
  "agent": {
    "build": { "steps": 50 },
    "general": { "steps": 20 }
  }
}
```

The default is `Infinity` (no limit) unless the agent defines one.

### As a fork maintainer

Edit `src/session/prompt/max-steps.txt`. The injection point is `prompt.ts:666-673`.

### For local LLM tuning

- Local models with smaller context windows benefit from lower `steps` values to prevent context overflow
- The max-steps prompt itself is short (~15 lines) and works well as-is
- Consider adding explicit "DO NOT call any tools" reinforcement for models that struggle with tool-call restraint

---

## 8. Mid-Loop User Message Wrapping

### What it is

At `prompt.ts:631-647`, when the agent is in step > 1 of its loop and a user sends a message mid-execution, the message text is ephemerally wrapped:

```
<system-reminder>
The user sent the following message:
{original user text}

Please address this message and continue with your tasks.
</system-reminder>
```

This is **not persisted** — it's an ephemeral transformation of the message before sending to the LLM.

### As a user

No config override. This always happens for mid-loop user messages.

### As a fork maintainer

Edit the inline template at `prompt.ts:637-644`. To disable entirely, remove the `if (step > 1 && lastFinished)` block.

### For local LLM tuning

- Replace `<system-reminder>` tags with `---` or `**Note:**` for models that don't handle XML
- Some local models interpret "continue with your tasks" as permission to ignore the user's message — consider rephrasing to "Address the user's message, then continue"

---

## 9. Structured Output Prompt

### What it is

A hardcoded constant at `prompt.ts:60`:

```
IMPORTANT: The user has requested structured output. You MUST use the StructuredOutput tool to provide your final response. Do NOT respond with plain text - you MUST call the StructuredOutput tool with your answer formatted according to the schema.
```

Injected at `prompt.ts:654-656` when `format.type === "json_schema"`. A corresponding `StructuredOutput` tool is also injected.

The tool description is at `prompt.ts:52-58`:

```
Use this tool to return your final response in the requested structured format.
IMPORTANT:
- You MUST call this tool exactly once at the end of your response
- The input must be valid JSON matching the required schema
- Complete all necessary research and tool calls BEFORE calling this tool
- This tool provides your final answer - no further actions are taken after calling it
```

### As a user

This only activates when structured output is requested via the API/SDK. No config override.

### As a fork maintainer

Edit the constants `STRUCTURED_OUTPUT_DESCRIPTION` and `STRUCTURED_OUTPUT_SYSTEM_PROMPT` at `prompt.ts:52-60`.

### For local LLM tuning

- Many local models struggle with "call this tool exactly once at the end" — consider simplifying to "Return JSON matching the schema"
- If your local model doesn't support tool calling, you may need to replace the tool-based approach with a direct JSON-in-response approach

---

## 10. Codex Instructions Header

### What it is

For OpenAI Codex (OAuth) sessions specifically, `SystemPrompt.instructions()` returns the content of `codex_header.txt` and injects it via `providerOptions.instructions` at `llm.ts:110-112`:

```ts
if (isCodex) {
  options.instructions = SystemPrompt.instructions()
}
```

This is separate from the regular system prompt — it uses OpenAI's `instructions` parameter.

### As a user

Not directly configurable unless you override the build agent prompt (which won't affect the `instructions` parameter).

### As a fork maintainer

Edit `src/session/prompt/codex_header.txt` and/or the injection logic at `llm.ts:110-112`.

### For local LLM tuning

Not relevant unless you're proxying through an OpenAI-compatible endpoint that supports the `instructions` parameter.

---

## 11. Agent Generation Meta-Prompt

### What it is

`src/agent/generate.txt` — used when dynamically generating new agent configurations via `Agent.generate()` at `agent.ts:289`. This is a meta-prompt that instructs the LLM how to create agent configs.

It defines the JSON output schema (`identifier`, `whenToUse`, `systemPrompt`) and provides detailed instructions for crafting agent personas.

### As a user

Not directly configurable. This only runs when you use the agent generation feature.

### As a fork maintainer

Edit `src/agent/generate.txt`. The function is at `agent.ts:283-338`.

### For local LLM tuning

- This prompt requires strong instruction-following and JSON output — smaller models may struggle
- Consider simplifying the output schema or providing few-shot examples
- Route this to a more capable model via the `model` parameter in the generate function

---

## 12. Plugin Hooks

### What they are

Three plugin hooks can modify the system prompt and parameters before they reach the LLM:

| Hook | Location | What it can modify |
|---|---|---|
| `experimental.chat.system.transform` | `llm.ts:83-87` | The `system[]` string array — can add, remove, or rewrite entries |
| `experimental.chat.messages.transform` | `prompt.ts:649` | The full message array before conversion |
| `chat.params` | `llm.ts:114-131` | Temperature, topP, topK, provider options |
| `chat.headers` | `llm.ts:133-145` | HTTP headers sent with the request |

### As a user

Plugins are configured in `cruxcli.json`. The plugin API allows external code to register hooks that intercept and modify prompts.

### As a fork maintainer

Create a plugin that registers these hooks. Example:

```ts
Plugin.register("my-plugin", {
  "experimental.chat.system.transform": async (input, output) => {
    // Remove the first system prompt entry (provider prompt)
    output.system.shift()
    // Add your own
    output.system.unshift("You are my custom assistant.")
  },
})
```

### For local LLM tuning

The `experimental.chat.system.transform` hook is the **most powerful single point** for customizing prompts without forking. You can use it to:

- Strip all CruxCLI-imposed prompts and replace with your own
- Add model-specific instructions based on `input.model`
- Inject few-shot examples for models that need them

---

## 13. Environment Variables & Flags

These flags (defined in `src/flag/flag.ts`) control prompt behavior:

| Variable | Default | Effect |
|---|---|---|
| `CRUXCLI_DISABLE_CLAUDE_CODE_PROMPT` | `false` | When `true`, skips loading `~/.claude/CLAUDE.md` as a global instruction file |
| `CRUXCLI_DISABLE_PROJECT_CONFIG` | `false` | When `true`, skips loading project-level `AGENTS.md` / `CLAUDE.md` / `CONTEXT.md` |
| `CRUXCLI_CONFIG_DIR` | undefined | Custom directory for global `AGENTS.md` lookup |
| `CRUXCLI_EXPERIMENTAL_PLAN_MODE` | `false` | Enables the new plan mode with plan files and phased workflow |
| `CRUXCLI_PERMISSION` | undefined | JSON string merged into permission config |
| `CRUXCLI_CLIENT` | `"cli"` | Identifies the client type in request headers |

Set them as environment variables:

```bash
CRUXCLI_DISABLE_PROJECT_CONFIG=true cruxcli
CRUXCLI_EXPERIMENTAL_PLAN_MODE=true cruxcli
CRUXCLI_CONFIG_DIR=~/.config/cruxcli cruxcli
```

---

## 14. Prompt Assembly Order

For a standard `build` agent session, the final system prompt sent to the LLM is assembled in this order:

```
┌─────────────────────────────────────────────────────┐
│  SYSTEM MESSAGE 1 (joined into one string)          │
│                                                     │
│  1. Provider base prompt (anthropic.txt, etc.)      │
│     — OR agent.prompt if set                        │
│     — OR empty if Codex (sent via options instead)  │
│                                                     │
│  2. SystemPrompt.environment()                      │
│     → model ID, working dir, platform, date         │
│                                                     │
│  3. InstructionPrompt.system()                      │
│     → AGENTS.md / CLAUDE.md / CONTEXT.md content    │
│     → config.instructions files/URLs                │
│                                                     │
│  4. STRUCTURED_OUTPUT_SYSTEM_PROMPT (if json_schema) │
│                                                     │
│  5. user.system (per-message system override)       │
│                                                     │
│  → Plugin: experimental.chat.system.transform       │
│    (can rewrite everything above)                   │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  CONVERSATION MESSAGES                              │
│                                                     │
│  - User messages (may include synthetic parts:      │
│    plan.txt, build-switch.txt, mid-loop wrappers)   │
│  - Assistant messages                               │
│  - Tool calls and results                           │
│  - max-steps.txt (as synthetic assistant message)   │
│                                                     │
│  → Plugin: experimental.chat.messages.transform     │
│    (can rewrite all messages)                       │
└─────────────────────────────────────────────────────┘
```

---

## 15. Recipes: Common Customization Scenarios

### Recipe A: Minimal prompt for a local model

```jsonc
// cruxcli.json
{
  "agent": {
    "build": {
      "model": "ollama/my-model",
      "prompt": "You are a coding assistant. You help with software engineering tasks using the tools provided. Be concise. Use tools to read, edit, and search files. Use bash for commands.",
      "steps": 25
    },
    "explore": {
      "model": "ollama/my-model",
      "prompt": "Find files matching the user's request. Use Glob for patterns, Grep for content search, Read for file contents. Return absolute paths."
    },
    "title": {
      "model": "ollama/my-small-model",
      "prompt": "Output a short title (under 50 chars) for this conversation. Output ONLY the title.",
      "temperature": 0.3
    },
    "compaction": {
      "model": "ollama/my-model",
      "prompt": "Summarize the conversation. Focus on: what was done, what files changed, what's in progress, what's next. Be detailed but concise."
    }
  },
  "default_agent": "build"
}
```

### Recipe B: Strip all CruxCLI personality, keep tool instructions

Edit the provider prompt file (e.g., `qwen.txt`) to remove:
- The "You are cruxcli" identity lines
- Tone/style instructions
- The examples
- TodoWrite instructions (if not using todo tools)

Keep:
- Tool usage policy section
- Code conventions section
- Security rules

### Recipe C: Add a custom provider prompt via source

In `src/session/system.ts`:

```ts
import PROMPT_LOCAL from "./prompt/local.txt"

export function provider(model: Provider.Model) {
  if (model.api.id.includes("llama") || model.api.id.includes("mistral"))
    return [PROMPT_LOCAL]
  // ... existing checks
}
```

Create `src/session/prompt/local.txt` with your custom prompt.

### Recipe D: Use a plugin to dynamically modify prompts

Create a plugin file and register it:

```ts
Plugin.register("local-model-adapter", {
  "experimental.chat.system.transform": async (input, output) => {
    if (input.model.providerID === "ollama") {
      // Replace all system prompts with a simplified version
      output.system.length = 0
      output.system.push("You are a helpful coding assistant. Use the provided tools to help the user.")
    }
  },
})
```

### Recipe E: Disable all instruction file loading

```bash
CRUXCLI_DISABLE_PROJECT_CONFIG=true CRUXCLI_DISABLE_CLAUDE_CODE_PROMPT=true cruxcli
```

This prevents loading of `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, and `~/.claude/CLAUDE.md`. The provider base prompt and environment block will still be present.

### Recipe F: Override only for specific agents

```jsonc
{
  "agent": {
    "build": {
      "prompt": "Custom build prompt here...",
      "temperature": 0.7,
      "top_p": 0.9
    },
    "plan": {
      "prompt": "Custom plan prompt here...",
      "temperature": 0.3
    }
  }
}
```

The `explore`, `title`, `compaction`, and `summary` agents will keep their defaults unless also overridden.

---

## File Quick Reference

| File | What to edit |
|---|---|
| `src/session/system.ts` | Provider prompt selection logic, environment block |
| `src/session/llm.ts` | System prompt assembly, plugin hooks, Codex instructions |
| `src/session/prompt.ts` | Loop logic, plan/build/max-steps injection, structured output, mid-loop wrapping |
| `src/session/instruction.ts` | AGENTS.md / CLAUDE.md discovery and loading |
| `src/agent/agent.ts` | Built-in agent definitions and their prompt assignments |
| `src/session/prompt/anthropic.txt` | Claude provider prompt |
| `src/session/prompt/beast.txt` | OpenAI GPT/o-series provider prompt |
| `src/session/prompt/gemini.txt` | Gemini provider prompt |
| `src/session/prompt/qwen.txt` | Fallback provider prompt (local models) |
| `src/session/prompt/codex_header.txt` | GPT-5 / Codex / Trinity provider prompt |
| `src/session/prompt/trinity.txt` | Trinity provider prompt |
| `src/session/prompt/plan.txt` | Plan mode read-only constraint |
| `src/session/prompt/build-switch.txt` | Plan→build transition notice |
| `src/session/prompt/max-steps.txt` | Step limit reached notice |
| `src/agent/prompt/explore.txt` | Explore subagent prompt |
| `src/agent/prompt/compaction.txt` | Compaction agent prompt |
| `src/agent/prompt/title.txt` | Title generation prompt |
| `src/agent/prompt/summary.txt` | Summary generation prompt |
| `src/agent/generate.txt` | Agent generation meta-prompt |
| `src/flag/flag.ts` | Environment variable flag definitions |
| `src/config/config.ts` | Config schema (agent, permission, instructions fields) |
