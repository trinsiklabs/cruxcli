import type { Hooks, PluginInput } from "@cruxcli/plugin"
import { Log } from "../util/log"
import { Bus } from "../bus"
import { Session } from "../session"
import { MCP } from "../mcp"
import type { Client } from "@modelcontextprotocol/sdk/client/index.js"
import { CallToolResultSchema } from "@modelcontextprotocol/sdk/types.js"

const log = Log.create({ service: "plugin.crux-hooks" })

const CORRECTION_PATTERNS = [
  /\bno,?\s+(actually|not|that's wrong|incorrect)/i,
  /\binstead,?\s+(use|do|try|make)/i,
  /\bthat's not (right|correct|what I)/i,
  /\bdon't\s+(do|use|add|make|create)/i,
  /\bwrong\b.{0,20}\b(should|use|be|do)/i,
  /\bactually,?\s+(it|the|we|I|this|that)/i,
  /\bI (said|meant|want|need)\s+/i,
  /\bplease\s+(don't|stop|remove|undo|revert)/i,
  /\bnot\s+what\s+I\s+(asked|wanted|meant)/i,
  /\b(revert|undo|roll\s*back)\s+(that|this|the|it)/i,
]

async function getCruxClient(): Promise<Client | null> {
  try {
    const all = await MCP.clients()
    return all["crux"] ?? null
  } catch {
    return null
  }
}

async function callCrux(tool: string, args: Record<string, unknown>): Promise<unknown> {
  const client = await getCruxClient()
  if (!client) return null
  try {
    const result = await client.callTool({ name: tool, arguments: args }, CallToolResultSchema, { timeout: 5000 })
    return result
  } catch (err) {
    log.warn("crux mcp call failed", { tool, error: err })
    return null
  }
}

// Batched interaction logging
const interactionQueue: Array<{ tool: string; input: unknown; output: unknown; time: number }> = []
let flushTimer: ReturnType<typeof setTimeout> | undefined

function queueInteraction(tool: string, input: unknown, output: unknown) {
  interactionQueue.push({ tool, input, output, time: Date.now() })
  if (interactionQueue.length >= 10) {
    flushInteractions()
  } else if (!flushTimer) {
    flushTimer = setTimeout(flushInteractions, 5000)
  }
}

async function flushInteractions() {
  if (flushTimer) {
    clearTimeout(flushTimer)
    flushTimer = undefined
  }
  if (!interactionQueue.length) return
  const batch = interactionQueue.splice(0)
  for (const item of batch) {
    await callCrux("log_interaction", {
      tool_name: item.tool,
      input_summary: typeof item.input === "string" ? item.input.slice(0, 500) : JSON.stringify(item.input).slice(0, 500),
      output_summary: typeof item.output === "string" ? item.output.slice(0, 500) : JSON.stringify(item.output).slice(0, 500),
    })
  }
}

export namespace CruxHooks {
  export function onToolResult(toolName: string, input: unknown, output: unknown) {
    // Fire-and-forget — never block tool execution
    queueInteraction(toolName, input, output)

    // Track files for edit/write tools
    if (toolName === "edit" || toolName === "write" || toolName === "multiedit" || toolName === "apply_patch") {
      const filePath = typeof input === "object" && input !== null && "file_path" in input
        ? (input as any).file_path
        : typeof input === "object" && input !== null && "path" in input
          ? (input as any).path
          : null
      if (filePath) {
        callCrux("update_session", { add_file: filePath })
      }
    }

    // Capture git commit decisions from bash
    if (toolName === "bash") {
      const out = typeof output === "string" ? output : JSON.stringify(output)
      const commitMatch = out.match(/\[[\w/-]+\s+([a-f0-9]+)\]\s+(.+)/)
      if (commitMatch) {
        callCrux("update_session", { add_decision: commitMatch[2] })
      }
    }
  }

  export function detectCorrection(text: string): boolean {
    return CORRECTION_PATTERNS.some((pattern) => pattern.test(text))
  }

  export function onUserMessage(text: string) {
    // Log user interaction
    queueInteraction("user_message", text, "")

    // Check for corrections
    if (detectCorrection(text)) {
      callCrux("log_correction", {
        original: "",
        corrected: text.slice(0, 500),
        category: "user_correction",
      })
    }
  }
}

export async function CruxHooksPlugin(input: PluginInput): Promise<Hooks> {
  // Check if crux MCP is configured
  const client = await getCruxClient()
  if (!client) {
    log.info("crux MCP not configured, hooks disabled")
    return {}
  }

  log.info("crux hooks enabled")

  // Session lifecycle hooks
  Bus.subscribe(Session.Event.Created, async (event) => {
    log.info("session created, restoring context")
    await callCrux("restore_context", {})
  })

  Bus.subscribe(Session.Event.Deleted, async (event) => {
    log.info("session deleted, writing handoff")
    const info = event.properties.info
    await flushInteractions()
    await callCrux("write_handoff", {
      content: `Auto-handoff from CruxCLI session ${info.id}.`,
    })
  })

  return {}
}
