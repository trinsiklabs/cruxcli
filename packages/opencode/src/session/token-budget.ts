import { Session } from "."
import { SystemPrompt } from "./system"
import { Log } from "../util/log"

const log = Log.create({ service: "token-budget" })

const DEFAULT_BUDGET = 1_000_000
const WARNING_THRESHOLD = 0.75
const HARD_LIMIT_THRESHOLD = 0.90

export namespace TokenBudget {
  export interface BudgetConfig {
    budget: number
    warningThreshold: number
    hardLimitThreshold: number
  }

  /**
   * Get the token budget for the current mode.
   * Reads from Crux mode metadata if available, otherwise uses default.
   */
  export async function getConfig(): Promise<BudgetConfig> {
    const state = await SystemPrompt.cruxState()
    // Future: read budget from mode metadata file
    // For now, use a sensible default
    return {
      budget: DEFAULT_BUDGET,
      warningThreshold: WARNING_THRESHOLD,
      hardLimitThreshold: HARD_LIMIT_THRESHOLD,
    }
  }

  /**
   * Get cumulative token usage for a session.
   */
  export async function sessionTokens(sessionID: string): Promise<number> {
    const messages = await Session.messages(sessionID)
    let total = 0
    for (const msg of messages) {
      if (msg.tokens?.input) total += msg.tokens.input
      if (msg.tokens?.output) total += msg.tokens.output
      if (msg.tokens?.cache?.read) total += msg.tokens.cache.read
    }
    return total
  }

  export type BudgetStatus = "ok" | "warning" | "exceeded"

  export interface BudgetCheck {
    status: BudgetStatus
    used: number
    budget: number
    percentage: number
  }

  /**
   * Check token budget status for a session.
   */
  export async function check(sessionID: string): Promise<BudgetCheck> {
    const config = await getConfig()
    const used = await sessionTokens(sessionID)
    const percentage = used / config.budget

    let status: BudgetStatus = "ok"
    if (percentage >= config.hardLimitThreshold) {
      status = "exceeded"
      log.info("token budget exceeded", { sessionID, used, budget: config.budget, percentage })
    } else if (percentage >= config.warningThreshold) {
      status = "warning"
      log.info("token budget warning", { sessionID, used, budget: config.budget, percentage })
    }

    return { status, used, budget: config.budget, percentage }
  }

  /**
   * Get a warning message to inject into the system prompt.
   */
  export function warningMessage(check: BudgetCheck): string {
    const pct = Math.round(check.percentage * 100)
    const remaining = check.budget - check.used
    return `Token budget: ${pct}% used (${remaining.toLocaleString()} tokens remaining). Prioritize completing your current task efficiently.`
  }
}
