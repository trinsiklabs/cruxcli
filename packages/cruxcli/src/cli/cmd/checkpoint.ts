import { Checkpoint } from "../../checkpoint"
import { bootstrap } from "../bootstrap"
import { cmd } from "./cmd"

export const CheckpointCommand = cmd({
  command: "checkpoint",
  describe: "manage workspace checkpoints",
  builder: (yargs) =>
    yargs
      .command(CreateCommand)
      .command(ListCommand)
      .command(RestoreCommand)
      .command(RemoveCommand)
      .command(DiffCommand)
      .demandCommand(),
  async handler() {},
})

const CreateCommand = cmd({
  command: "create [label]",
  describe: "create a checkpoint of the current workspace state",
  builder: (yargs) =>
    yargs.positional("label", {
      type: "string",
      description: "optional label for the checkpoint",
    }),
  async handler(args) {
    await bootstrap(process.cwd(), async () => {
      const result = await Checkpoint.create(args.label as string | undefined)
      if (!result) {
        console.error("Failed to create checkpoint (not a git project or snapshots disabled)")
        process.exit(1)
      }
      console.log(`Checkpoint created: ${result.id}`)
      if (result.label) console.log(`Label: ${result.label}`)
    })
  },
})

const ListCommand = cmd({
  command: "list",
  describe: "list all checkpoints",
  async handler() {
    await bootstrap(process.cwd(), async () => {
      const items = await Checkpoint.list()
      if (!items.length) {
        console.log("No checkpoints")
        return
      }
      for (const item of items) {
        const date = new Date(item.time).toISOString().replace("T", " ").slice(0, 19)
        const tag = item.auto ? " (auto)" : ""
        const label = item.label && !item.auto ? ` — ${item.label}` : ""
        console.log(`${item.id}  ${date}${tag}${label}`)
      }
    })
  },
})

const RestoreCommand = cmd({
  command: "restore <id>",
  describe: "restore workspace to a checkpoint",
  builder: (yargs) =>
    yargs.positional("id", {
      type: "string",
      description: "checkpoint id",
      demandOption: true,
    }),
  async handler(args) {
    await bootstrap(process.cwd(), async () => {
      const ok = await Checkpoint.restore(args.id)
      if (!ok) {
        console.error(`Checkpoint not found: ${args.id}`)
        process.exit(1)
      }
      console.log("Restored")
    })
  },
})

const RemoveCommand = cmd({
  command: "remove <id>",
  describe: "remove a checkpoint",
  builder: (yargs) =>
    yargs.positional("id", {
      type: "string",
      description: "checkpoint id",
      demandOption: true,
    }),
  async handler(args) {
    await bootstrap(process.cwd(), async () => {
      const ok = await Checkpoint.remove(args.id)
      if (!ok) {
        console.error(`Checkpoint not found: ${args.id}`)
        process.exit(1)
      }
      console.log("Removed")
    })
  },
})

const DiffCommand = cmd({
  command: "diff <id>",
  describe: "show changes since a checkpoint",
  builder: (yargs) =>
    yargs.positional("id", {
      type: "string",
      description: "checkpoint id",
      demandOption: true,
    }),
  async handler(args) {
    await bootstrap(process.cwd(), async () => {
      const result = await Checkpoint.diff(args.id)
      if (!result) {
        console.log("No changes since checkpoint")
        return
      }
      console.log(result)
    })
  },
})
