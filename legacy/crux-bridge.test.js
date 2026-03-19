import { describe, it } from "node:test"
import assert from "node:assert/strict"
import { createBridge } from "../src/crux-bridge.js"
import CruxBridgePlugin from "../src/crux-bridge.js"

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function makeConfig(overrides = {}) {
  return {
    cruxDir: "/tmp/test-crux",
    modesDir: "/tmp/test-modes",
    ...overrides,
  }
}

function makeSessionState(overrides = {}) {
  return {
    active_mode: "build-py",
    active_tool: "claude-code",
    started_at: "2026-03-07T00:00:00Z",
    updated_at: "2026-03-07T00:00:00Z",
    working_on: "building things",
    key_decisions: [],
    files_touched: [],
    pending: [],
    context_summary: "",
    ...overrides,
  }
}

function makeModePrompt(mode = "build-py") {
  return `# Mode: ${mode}\n\nYou are a Python developer.\n\n## Core Rules\n- Type hints required\n- Security first`
}

function failIO() {
  return {
    readFile: async () => { throw new Error("ENOENT") },
    fileExists: async () => false,
  }
}

function stateOnlyIO(state) {
  const stateJson = JSON.stringify(state)
  return {
    readFile: async (p) => {
      if (p.includes("state.json")) return stateJson
      throw new Error("ENOENT")
    },
    fileExists: async (p) => p.includes("state.json"),
  }
}

function fullIO(state, modePrompt) {
  const stateJson = JSON.stringify(state)
  return {
    readFile: async (p) => {
      if (p.includes("state.json")) return stateJson
      if (p.endsWith(".md")) return modePrompt
      throw new Error("ENOENT")
    },
    fileExists: async () => true,
  }
}

// ---------------------------------------------------------------------------
// 1. Hook Registration
// ---------------------------------------------------------------------------

describe("Hook Registration", () => {
  it("plugin registers all 3 hooks", async () => {
    const hooks = await createBridge(makeConfig(), fullIO(makeSessionState(), makeModePrompt()))
    assert.ok(hooks["experimental.chat.system.transform"])
    assert.ok(hooks["experimental.chat.messages.transform"])
    assert.ok(hooks["chat.params"])
  })

  it("hook functions are async (return promises)", async () => {
    const hooks = await createBridge(makeConfig(), fullIO(makeSessionState(), makeModePrompt()))
    const result = hooks["experimental.chat.system.transform"](
      { model: {} },
      { system: ["base prompt"] },
    )
    assert.ok(result instanceof Promise)
  })
})

// ---------------------------------------------------------------------------
// 2. System Transform — No Crux State
// ---------------------------------------------------------------------------

describe("System Transform — No Crux State", () => {
  it("passes through unchanged when state file missing", async () => {
    const hooks = await createBridge(makeConfig(), failIO())
    const output = { system: ["base prompt", "env block"] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)
    assert.deepStrictEqual(output.system, ["base prompt", "env block"])
  })

  it("passes through unchanged when active_mode is empty", async () => {
    const hooks = await createBridge(makeConfig(), stateOnlyIO(makeSessionState({ active_mode: "" })))
    const output = { system: ["base prompt", "env block"] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)
    assert.deepStrictEqual(output.system, ["base prompt", "env block"])
  })
})

// ---------------------------------------------------------------------------
// 3. System Transform — Active Mode
// ---------------------------------------------------------------------------

describe("System Transform — Active Mode", () => {
  it("injects mode prompt before system[0]", async () => {
    const hooks = await createBridge(
      makeConfig(),
      fullIO(makeSessionState({ active_mode: "build-py" }), makeModePrompt("build-py")),
    )
    const output = { system: ["base prompt"] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)

    assert.ok(output.system[0].includes("# Mode: build-py"))
    assert.ok(output.system[0].includes("base prompt"))
  })

  it("reformats XML environment block to plain key-value", async () => {
    const envBlock = `<env>
<model>anthropic/claude-sonnet-4-5-20250929</model>
<cwd>/Users/user/project</cwd>
<platform>darwin</platform>
<date>2026-03-07</date>
<directories>
</directories>
</env>`

    const hooks = await createBridge(
      makeConfig(),
      fullIO(makeSessionState(), makeModePrompt()),
    )
    const output = { system: ["base prompt", envBlock] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)

    const envEntry = output.system.find((s) => s.includes("Model:"))
    assert.ok(envEntry, "should have reformatted env entry")
    assert.ok(envEntry.includes("Model: anthropic/claude-sonnet-4-5-20250929"))
    assert.ok(envEntry.includes("Working directory: /Users/user/project"))
    assert.ok(envEntry.includes("Platform: darwin"))
    assert.ok(!envEntry.includes("<env>"))
    assert.ok(!envEntry.includes("<directories>"))
  })

  it("passes through non-XML environment blocks unchanged", async () => {
    const hooks = await createBridge(
      makeConfig(),
      fullIO(makeSessionState(), makeModePrompt()),
    )
    const plainEnv = "Model: foo\nWorking directory: /bar"
    const output = { system: ["base prompt", plainEnv] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)

    assert.ok(output.system.includes(plainEnv))
  })

  it("injects session context summary when available", async () => {
    const state = makeSessionState({
      context_summary: "Working on bridge plugin. All 11 injection points reviewed.",
      working_on: "crux-bridge.js TDD",
      pending: ["Build bridge plugin", "Init repo"],
    })
    const hooks = await createBridge(makeConfig(), fullIO(state, makeModePrompt()))

    const output = { system: ["base prompt"] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)

    const joined = output.system.join("\n")
    assert.ok(joined.includes("Working on bridge plugin"))
  })
})

// ---------------------------------------------------------------------------
// 4. System Transform — Filesystem Unavailable
// ---------------------------------------------------------------------------

describe("System Transform — Filesystem Unavailable", () => {
  it("does not crash when state file read throws", async () => {
    const hooks = await createBridge(makeConfig(), {
      readFile: async () => { throw new Error("Permission denied") },
      fileExists: async () => true,
    })
    const output = { system: ["base prompt"] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)
    assert.deepStrictEqual(output.system, ["base prompt"])
  })

  it("does not crash when mode file read throws", async () => {
    const hooks = await createBridge(makeConfig(), stateOnlyIO(makeSessionState()))
    const output = { system: ["base prompt"] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)
    assert.deepStrictEqual(output.system, ["base prompt"])
  })

  it("does not crash when state file contains invalid JSON", async () => {
    const hooks = await createBridge(makeConfig(), {
      readFile: async () => "not json {{{",
      fileExists: async () => true,
    })
    const output = { system: ["base prompt"] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)
    assert.deepStrictEqual(output.system, ["base prompt"])
  })
})

// ---------------------------------------------------------------------------
// 5. Message Transform — Synthetic Messages
// ---------------------------------------------------------------------------

describe("Message Transform — Synthetic Messages", () => {
  it("strips <system-reminder> XML tags from message parts", async () => {
    const hooks = await createBridge(makeConfig(), fullIO(makeSessionState(), makeModePrompt()))
    const output = {
      messages: [{
        info: { role: "user" },
        parts: [{
          type: "text",
          text: "<system-reminder>Plan mode is active. Do not edit files.</system-reminder>",
        }],
      }],
    }
    await hooks["experimental.chat.messages.transform"]({}, output)
    assert.strictEqual(output.messages[0].parts[0].text, "Plan mode is active. Do not edit files.")
  })

  it("strips nested system-reminder tags", async () => {
    const hooks = await createBridge(makeConfig(), fullIO(makeSessionState(), makeModePrompt()))
    const output = {
      messages: [{
        info: { role: "user" },
        parts: [{
          type: "text",
          text: "User said something\n<system-reminder>injected context</system-reminder>\nmore text",
        }],
      }],
    }
    await hooks["experimental.chat.messages.transform"]({}, output)
    assert.strictEqual(
      output.messages[0].parts[0].text,
      "User said something\ninjected context\nmore text",
    )
  })
})

// ---------------------------------------------------------------------------
// 6. Message Transform — Normal Messages
// ---------------------------------------------------------------------------

describe("Message Transform — Normal Messages", () => {
  it("leaves messages without system-reminder tags untouched", async () => {
    const hooks = await createBridge(makeConfig(), fullIO(makeSessionState(), makeModePrompt()))
    const original = "Hello, can you help me with this code?"
    const output = {
      messages: [{
        info: { role: "user" },
        parts: [{ type: "text", text: original }],
      }],
    }
    await hooks["experimental.chat.messages.transform"]({}, output)
    assert.strictEqual(output.messages[0].parts[0].text, original)
  })

  it("leaves non-text parts untouched", async () => {
    const hooks = await createBridge(makeConfig(), fullIO(makeSessionState(), makeModePrompt()))
    const toolPart = { type: "tool_use", id: "123", name: "read", input: {} }
    const output = {
      messages: [{
        info: { role: "user" },
        parts: [toolPart],
      }],
    }
    await hooks["experimental.chat.messages.transform"]({}, output)
    assert.deepStrictEqual(output.messages[0].parts[0], toolPart)
  })
})

// ---------------------------------------------------------------------------
// 7. Params Transform — Think Mode
// ---------------------------------------------------------------------------

describe("Params Transform — Think Mode", () => {
  it("sets temperature 0.6 and topP 0.95 for think modes", async () => {
    const hooks = await createBridge(
      makeConfig({ thinkModes: ["plan", "review", "debug"] }),
      stateOnlyIO(makeSessionState({ active_mode: "plan" })),
    )
    const output = { temperature: 1.0, topP: 1.0, topK: 0, options: {} }
    await hooks["chat.params"](
      { sessionID: "s1", agent: "build", model: {}, provider: {}, message: {} },
      output,
    )
    assert.strictEqual(output.temperature, 0.6)
    assert.strictEqual(output.topP, 0.95)
  })
})

// ---------------------------------------------------------------------------
// 8. Params Transform — No-Think Mode
// ---------------------------------------------------------------------------

describe("Params Transform — No-Think Mode", () => {
  it("sets topP 0.8 for build modes", async () => {
    const hooks = await createBridge(
      makeConfig({ thinkModes: ["plan", "review", "debug"] }),
      stateOnlyIO(makeSessionState({ active_mode: "build-py" })),
    )
    const output = { temperature: 1.0, topP: 1.0, topK: 0, options: {} }
    await hooks["chat.params"](
      { sessionID: "s1", agent: "build", model: {}, provider: {}, message: {} },
      output,
    )
    assert.strictEqual(output.topP, 0.8)
  })

  it("does not change temperature for no-think modes", async () => {
    const hooks = await createBridge(
      makeConfig({ thinkModes: ["plan", "review", "debug"] }),
      stateOnlyIO(makeSessionState({ active_mode: "build-py" })),
    )
    const output = { temperature: 1.0, topP: 1.0, topK: 0, options: {} }
    await hooks["chat.params"](
      { sessionID: "s1", agent: "build", model: {}, provider: {}, message: {} },
      output,
    )
    assert.strictEqual(output.temperature, 1.0)
  })
})

// ---------------------------------------------------------------------------
// 9. Params Transform — No Crux State
// ---------------------------------------------------------------------------

describe("Params Transform — No Crux State", () => {
  it("leaves params unchanged when state unavailable", async () => {
    const hooks = await createBridge(makeConfig(), failIO())
    const output = { temperature: 1.0, topP: 1.0, topK: 0, options: {} }
    await hooks["chat.params"](
      { sessionID: "s1", agent: "build", model: {}, provider: {}, message: {} },
      output,
    )
    assert.strictEqual(output.temperature, 1.0)
    assert.strictEqual(output.topP, 1.0)
  })

  it("leaves params unchanged when active_mode is empty", async () => {
    const hooks = await createBridge(
      makeConfig(),
      stateOnlyIO(makeSessionState({ active_mode: "" })),
    )
    const output = { temperature: 0.7, topP: 0.9, topK: 0, options: {} }
    await hooks["chat.params"](
      { sessionID: "s1", agent: "build", model: {}, provider: {}, message: {} },
      output,
    )
    assert.strictEqual(output.temperature, 0.7)
    assert.strictEqual(output.topP, 0.9)
  })
})

// ---------------------------------------------------------------------------
// 10. Integration: Full Prompt Assembly
// ---------------------------------------------------------------------------

describe("Integration — Full Prompt Assembly", () => {
  it("complete flow: mode prompt + reformatted env + session context", async () => {
    const state = makeSessionState({
      active_mode: "build-py",
      working_on: "crux-bridge plugin",
      context_summary: "Building the bridge plugin with TDD.",
      pending: ["Finish tests", "Push to repo"],
    })
    const modePrompt = makeModePrompt("build-py")
    const envBlock = `<env>
<model>anthropic/claude-sonnet-4-5-20250929</model>
<cwd>/Users/user/project</cwd>
<platform>darwin</platform>
<date>2026-03-07</date>
<directories>
</directories>
</env>`

    const hooks = await createBridge(makeConfig(), fullIO(state, modePrompt))

    const output = { system: ["base prompt", envBlock, "AGENTS.md content"] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)

    // system[0] should have mode prompt prepended
    assert.ok(output.system[0].includes("# Mode: build-py"))
    assert.ok(output.system[0].includes("base prompt"))

    // env block should be reformatted
    const envEntry = output.system.find((s) => s.includes("Model:"))
    assert.ok(envEntry)
    assert.ok(!envEntry.includes("<env>"))

    // AGENTS.md should be preserved
    assert.ok(output.system.includes("AGENTS.md content"))

    // Session context should be present
    const joined = output.system.join("\n")
    assert.ok(joined.includes("crux-bridge plugin"))
    assert.ok(joined.includes("Building the bridge plugin with TDD."))
    assert.ok(joined.includes("Finish tests"))
  })
})

// ---------------------------------------------------------------------------
// 11. Integration: Fallback Chain
// ---------------------------------------------------------------------------

describe("Integration — Fallback Chain", () => {
  it("opencode.json overrides work when bridge has no Crux state", async () => {
    const hooks = await createBridge(makeConfig(), failIO())

    // System: base prompt from opencode.json should be untouched
    const basePrompt = "You are a partner working alongside the user in a CLI terminal."
    const envBlock = "<env><model>test</model></env>"
    const systemOutput = { system: [basePrompt, envBlock] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, systemOutput)
    assert.strictEqual(systemOutput.system[0], basePrompt)
    assert.strictEqual(systemOutput.system[1], envBlock)

    // Messages: should still strip XML tags even without Crux state
    const msgOutput = {
      messages: [{
        info: { role: "user" },
        parts: [{ type: "text", text: "<system-reminder>test</system-reminder>" }],
      }],
    }
    await hooks["experimental.chat.messages.transform"]({}, msgOutput)
    assert.strictEqual(msgOutput.messages[0].parts[0].text, "test")

    // Params: should be unchanged
    const paramsOutput = { temperature: 1.0, topP: 1.0, topK: 0, options: {} }
    await hooks["chat.params"](
      { sessionID: "s1", agent: "build", model: {}, provider: {}, message: {} },
      paramsOutput,
    )
    assert.strictEqual(paramsOutput.temperature, 1.0)
    assert.strictEqual(paramsOutput.topP, 1.0)
  })
})

// ---------------------------------------------------------------------------
// Edge Cases
// ---------------------------------------------------------------------------

describe("Edge Cases", () => {
  it("handles empty system array", async () => {
    const hooks = await createBridge(
      makeConfig(),
      fullIO(makeSessionState(), makeModePrompt()),
    )
    const output = { system: [] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)

    assert.ok(output.system.length > 0)
    assert.ok(output.system[0].includes("# Mode: build-py"))
  })

  it("handles empty messages array", async () => {
    const hooks = await createBridge(makeConfig(), fullIO(makeSessionState(), makeModePrompt()))
    const output = { messages: [] }
    await hooks["experimental.chat.messages.transform"]({}, output)
    assert.deepStrictEqual(output.messages, [])
  })

  it("reformats env block with git repo field", async () => {
    const envBlock = `<env>
<model>anthropic/claude-sonnet-4-5-20250929</model>
<cwd>/Users/user/project</cwd>
<is_git>true</is_git>
<platform>darwin</platform>
<date>2026-03-07</date>
<directories>
</directories>
</env>`

    const hooks = await createBridge(
      makeConfig(),
      fullIO(makeSessionState(), makeModePrompt()),
    )
    const output = { system: ["base prompt", envBlock] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)

    const envEntry = output.system.find((s) => s.includes("Model:"))
    assert.ok(envEntry.includes("Git repo: true"))
  })

  it("handles multiple system-reminder tags in one part", async () => {
    const hooks = await createBridge(makeConfig(), fullIO(makeSessionState(), makeModePrompt()))
    const output = {
      messages: [{
        info: { role: "user" },
        parts: [{
          type: "text",
          text: "<system-reminder>first</system-reminder> and <system-reminder>second</system-reminder>",
        }],
      }],
    }
    await hooks["experimental.chat.messages.transform"]({}, output)
    assert.strictEqual(output.messages[0].parts[0].text, "first and second")
  })
})

// ---------------------------------------------------------------------------
// Plugin Entry Point (default export)
// ---------------------------------------------------------------------------

describe("CruxBridgePlugin Entry Point", () => {
  it("returns hooks object from default export", async () => {
    const hooks = await CruxBridgePlugin({
      directory: "/tmp/nonexistent-project",
      project: {},
      worktree: "/tmp",
      serverUrl: new URL("http://localhost:4096"),
    })

    assert.ok(hooks["experimental.chat.system.transform"])
    assert.ok(hooks["experimental.chat.messages.transform"])
    assert.ok(hooks["chat.params"])
  })

  it("gracefully handles missing .crux directory", async () => {
    const hooks = await CruxBridgePlugin({
      directory: "/tmp/nonexistent-project",
      project: {},
      worktree: "/tmp",
      serverUrl: new URL("http://localhost:4096"),
    })

    // Should not crash — falls through gracefully
    const output = { system: ["base prompt"] }
    await hooks["experimental.chat.system.transform"]({ model: {} }, output)
    assert.deepStrictEqual(output.system, ["base prompt"])
  })
})
