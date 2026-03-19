import { Ripgrep } from "../file/ripgrep"
import fs from "fs/promises"
import path from "path"
import os from "os"

import { Instance } from "../project/instance"

import PROMPT_ANTHROPIC from "./prompt/anthropic.txt"
import PROMPT_ANTHROPIC_WITHOUT_TODO from "./prompt/qwen.txt"
import PROMPT_BEAST from "./prompt/beast.txt"
import PROMPT_GEMINI from "./prompt/gemini.txt"

import PROMPT_CODEX from "./prompt/codex_header.txt"
import PROMPT_TRINITY from "./prompt/trinity.txt"
import type { Provider } from "@/provider/provider"
import { Log } from "../util/log"

export namespace SystemPrompt {
  const log = Log.create({ service: "system-prompt" })
  export function instructions() {
    return PROMPT_CODEX.trim()
  }

  export function provider(model: Provider.Model) {
    if (model.api.id.includes("gpt-5")) return [PROMPT_CODEX]
    if (model.api.id.includes("gpt-") || model.api.id.includes("o1") || model.api.id.includes("o3"))
      return [PROMPT_BEAST]
    if (model.api.id.includes("gemini-")) return [PROMPT_GEMINI]
    if (model.api.id.includes("claude")) return [PROMPT_ANTHROPIC]
    if (model.api.id.toLowerCase().includes("trinity")) return [PROMPT_TRINITY]
    return [PROMPT_ANTHROPIC_WITHOUT_TODO]
  }

  /**
   * Read the active Crux mode prompt, if Crux is installed.
   * Looks for .crux/sessions/state.json in the project directory,
   * then loads the mode prompt from ~/.crux/modes/<mode>.md.
   */
  export async function cruxModePrompt(): Promise<string | undefined> {
    try {
      const stateFile = path.join(Instance.directory, ".crux", "sessions", "state.json")
      const raw = await fs.readFile(stateFile, "utf-8")
      const state = JSON.parse(raw)
      const activeMode = state?.active_mode
      if (!activeMode) return undefined

      const home = os.homedir()
      const modeFile = path.join(home, ".crux", "modes", `${activeMode}.md`)
      const prompt = await fs.readFile(modeFile, "utf-8")
      log.info("injecting crux mode prompt", { mode: activeMode })
      return prompt.trim()
    } catch {
      return undefined
    }
  }

  export async function environment(model: Provider.Model) {
    const project = Instance.project
    const modePrompt = await cruxModePrompt()
    const parts = [
      [
        `You are powered by the model named ${model.api.id}. The exact model ID is ${model.providerID}/${model.api.id}`,
        `Here is some useful information about the environment you are running in:`,
        `<env>`,
        `  Working directory: ${Instance.directory}`,
        `  Is directory a git repo: ${project.vcs === "git" ? "yes" : "no"}`,
        `  Platform: ${process.platform}`,
        `  Today's date: ${new Date().toDateString()}`,
        `</env>`,
        `<directories>`,
        `  ${
          project.vcs === "git" && false
            ? await Ripgrep.tree({
                cwd: Instance.directory,
                limit: 50,
              })
            : ""
        }`,
        `</directories>`,
      ].join("\n"),
    ]
    if (modePrompt) {
      parts.unshift(modePrompt)
    }
    return parts
  }
}
