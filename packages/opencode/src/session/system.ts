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

  const THINK_MODES = new Set(["plan", "review", "debug", "explain", "strategist", "legal", "psych"])

  export interface CruxState {
    active_mode?: string
    working_on?: string
    context_summary?: string
    pending?: string[]
  }

  /**
   * Read Crux session state, if Crux is installed.
   */
  export async function cruxState(): Promise<CruxState | undefined> {
    try {
      const stateFile = path.join(Instance.directory, ".crux", "sessions", "state.json")
      const raw = await fs.readFile(stateFile, "utf-8")
      return JSON.parse(raw)
    } catch {
      return undefined
    }
  }

  /**
   * Read the active Crux mode prompt.
   */
  export async function cruxModePrompt(state: CruxState): Promise<string | undefined> {
    try {
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

  /**
   * Format session context (working_on, context_summary, pending) for system prompt.
   */
  export function cruxSessionContext(state: CruxState): string | undefined {
    const parts: string[] = []
    if (state.working_on) parts.push(`Working on: ${state.working_on}`)
    if (state.context_summary) parts.push(state.context_summary)
    if (state.pending && state.pending.length > 0) parts.push(`Pending: ${state.pending.join(", ")}`)
    return parts.length > 0 ? parts.join("\n") : undefined
  }

  /**
   * Get mode-aware temperature/topP overrides.
   */
  export function cruxModelParams(state: CruxState): { temperature?: number; topP?: number } | undefined {
    if (!state.active_mode) return undefined
    if (THINK_MODES.has(state.active_mode)) {
      return { temperature: 0.6, topP: 0.95 }
    }
    return { topP: 0.8 }
  }

  export async function environment(model: Provider.Model) {
    const project = Instance.project
    const state = await cruxState()
    const modePrompt = state ? await cruxModePrompt(state) : undefined
    const sessionContext = state ? cruxSessionContext(state) : undefined
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
    if (sessionContext) {
      parts.push(sessionContext)
    }
    return parts
  }
}
