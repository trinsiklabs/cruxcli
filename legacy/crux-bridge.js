import path from "node:path"

const DEFAULT_THINK_MODES = ["plan", "review", "debug", "explain", "strategist", "legal", "psych"]

// ---------------------------------------------------------------------------
// Filesystem helpers
// ---------------------------------------------------------------------------

async function readState(config, io) {
  try {
    const statePath = path.join(config.cruxDir, "sessions", "state.json")
    const raw = await io.readFile(statePath)
    return JSON.parse(raw)
  } catch {
    return null
  }
}

async function readModePrompt(mode, config, io) {
  try {
    const modePath = path.join(config.modesDir, `${mode}.md`)
    return await io.readFile(modePath)
  } catch {
    return null
  }
}

// ---------------------------------------------------------------------------
// Environment block reformatting
// ---------------------------------------------------------------------------

function isXmlEnvBlock(text) {
  return text.includes("<env>") && text.includes("</env>")
}

function reformatEnvBlock(text) {
  const fields = []

  const modelMatch = text.match(/<model>(.*?)<\/model>/)
  if (modelMatch) fields.push(`Model: ${modelMatch[1]}`)

  const cwdMatch = text.match(/<cwd>(.*?)<\/cwd>/)
  if (cwdMatch) fields.push(`Working directory: ${cwdMatch[1]}`)

  const gitMatch = text.match(/<is_git>(.*?)<\/is_git>/)
  if (gitMatch) fields.push(`Git repo: ${gitMatch[1]}`)

  const platformMatch = text.match(/<platform>(.*?)<\/platform>/)
  if (platformMatch) fields.push(`Platform: ${platformMatch[1]}`)

  const dateMatch = text.match(/<date>(.*?)<\/date>/)
  if (dateMatch) fields.push(`Date: ${dateMatch[1]}`)

  return fields.join("\n")
}

// ---------------------------------------------------------------------------
// System-reminder tag stripping
// ---------------------------------------------------------------------------

function stripSystemReminders(text) {
  return text.replace(/<system-reminder>([\s\S]*?)<\/system-reminder>/g, "$1")
}

// ---------------------------------------------------------------------------
// Session context formatting
// ---------------------------------------------------------------------------

function formatSessionContext(state) {
  const parts = []

  if (state.working_on) {
    parts.push(`Working on: ${state.working_on}`)
  }

  if (state.context_summary) {
    parts.push(state.context_summary)
  }

  if (state.pending && state.pending.length > 0) {
    parts.push(`Pending: ${state.pending.join(", ")}`)
  }

  return parts.length > 0 ? parts.join("\n") : null
}

// ---------------------------------------------------------------------------
// Main export
// ---------------------------------------------------------------------------

/**
 * Create the Crux bridge hooks.
 *
 * @param {object} config - { cruxDir, modesDir, thinkModes? }
 * @param {object} io - { readFile(path): Promise<string>, fileExists(path): Promise<boolean> }
 * @returns {Promise<object>} OpenCode Hooks object
 */
export async function createBridge(config, io) {
  const thinkModes = new Set(config.thinkModes ?? DEFAULT_THINK_MODES)

  return {
    "experimental.chat.system.transform": async (_input, output) => {
      const state = await readState(config, io)
      if (!state || !state.active_mode) return

      const modePrompt = await readModePrompt(state.active_mode, config, io)
      if (!modePrompt) return

      // Prepend mode prompt to system[0], or create it
      if (output.system.length > 0) {
        output.system[0] = modePrompt + "\n\n" + output.system[0]
      } else {
        output.system.push(modePrompt)
      }

      // Reformat XML environment blocks
      for (let i = 0; i < output.system.length; i++) {
        if (isXmlEnvBlock(output.system[i])) {
          output.system[i] = reformatEnvBlock(output.system[i])
        }
      }

      // Inject session context
      const context = formatSessionContext(state)
      if (context) {
        output.system.push(context)
      }
    },

    "experimental.chat.messages.transform": async (_input, output) => {
      for (const message of output.messages) {
        for (const part of message.parts) {
          if ("text" in part && typeof part.text === "string") {
            part.text = stripSystemReminders(part.text)
          }
        }
      }
    },

    "chat.params": async (_input, output) => {
      const state = await readState(config, io)
      if (!state || !state.active_mode) return

      if (thinkModes.has(state.active_mode)) {
        output.temperature = 0.6
        output.topP = 0.95
      } else {
        output.topP = 0.8
      }
    },
  }
}

// ---------------------------------------------------------------------------
// OpenCode plugin entry point
// ---------------------------------------------------------------------------

/**
 * OpenCode plugin factory. Reads CRUX_PROJECT and CRUX_HOME from env
 * to locate the .crux directory and modes.
 */
export default async function CruxBridgePlugin(input) {
  const { readFile } = await import("node:fs/promises")
  const { existsSync } = await import("node:fs")

  const cruxDir = path.join(input.directory, ".crux")
  const modesDir = path.join(process.env.CRUX_HOME || "", "personal", "crux", "modes")

  return createBridge(
    { cruxDir, modesDir },
    {
      readFile: (p) => readFile(p, "utf-8"),
      fileExists: async (p) => existsSync(p),
    },
  )
}
