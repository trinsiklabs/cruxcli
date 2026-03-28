import { bootstrap } from "../bootstrap"
import { cmd } from "./cmd"
import { MCP } from "../../mcp"
import { Log } from "../../util/log"
import { Filesystem } from "../../util/filesystem"
import path from "path"
import { Instance } from "../../project/instance"

const log = Log.create({ service: "converge" })
const STATE_FILE = ".cruxcli/convergence.json"

interface ConvergenceLocal {
  convergence_id: string
  plan_file: string
  started_at: string
}

export const ConvergeCommand = cmd({
  command: "converge <plan>",
  describe: "start or resume convergence on a build plan",
  builder: (yargs) =>
    yargs.positional("plan", {
      type: "string",
      description: "path to the build plan markdown file",
      demandOption: true,
    }),
  async handler(args) {
    await bootstrap(process.cwd(), async () => {
      const planFile = path.resolve(args.plan)

      // Check for active convergence to resume
      const stateFile = path.join(Instance.directory, STATE_FILE)
      let state: ConvergenceLocal | undefined
      try {
        state = await Filesystem.readJson<ConvergenceLocal>(stateFile)
      } catch {}

      if (state?.convergence_id) {
        // Resume existing convergence
        console.log(`Resuming convergence ${state.convergence_id} on ${state.plan_file}`)
        try {
          const status = await callCruxDev("convergence_status", {
            convergence_id: state.convergence_id,
          })
          if (status) {
            const parsed = typeof status === "string" ? JSON.parse(status) : status
            if (parsed.terminal) {
              console.log(`Previous convergence completed: ${parsed.phase}`)
              state = undefined
            } else {
              console.log(`Phase: ${parsed.phase} | Round: ${parsed.round} | Clean: ${parsed.consecutive_clean}`)
              return
            }
          }
        } catch {
          console.log("Could not reach previous convergence — starting fresh")
          state = undefined
        }
      }

      // Start new convergence
      console.log(`Starting convergence on ${planFile}`)
      const result = await callCruxDev("start_convergence", {
        plan_file: planFile,
      })

      if (!result) {
        console.error("Failed to start convergence — is CruxDev MCP configured?")
        process.exit(1)
      }

      const parsed = typeof result === "string" ? JSON.parse(result) : result
      const id = parsed.convergence_id

      // Persist for resume
      await Filesystem.writeJson(stateFile, {
        convergence_id: id,
        plan_file: planFile,
        started_at: new Date().toISOString(),
      } satisfies ConvergenceLocal)

      console.log(`Convergence started: ${id}`)
      console.log(`Phase: ${parsed.task?.task_type ?? "unknown"}`)
      if (parsed.task?.description) {
        console.log(`Task: ${parsed.task.description}`)
      }
    })
  },
})

async function callCruxDev(tool: string, args: Record<string, unknown>): Promise<unknown> {
  try {
    const tools = await MCP.tools()
    const toolName = Object.keys(tools).find((k) => k.includes("cruxdev") && k.includes(tool))
    if (!toolName) {
      log.warn("cruxdev tool not found", { tool })
      return null
    }
    const matched = tools[toolName]!
    const result = await matched.execute!(args as any, {} as any)
    return result?.output
  } catch (err) {
    log.warn("cruxdev call failed", { tool, error: err })
    return null
  }
}
