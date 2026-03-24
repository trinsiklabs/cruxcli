import * as vscode from "vscode"
import { execSync } from "child_process"

const TERMINAL_NAME = "cruxcli"

let status: vscode.StatusBarItem | undefined

export function deactivate() {
  status?.dispose()
}

export function activate(context: vscode.ExtensionContext) {
  // Check if cruxcli binary is available
  const bin = findBinary()
  if (!bin) {
    vscode.window
      .showInformationMessage("CruxCLI is not installed. Install it to use this extension.", "Install")
      .then((choice) => {
        if (choice === "Install") vscode.env.openExternal(vscode.Uri.parse("https://cruxcli.ai"))
      })
  }

  // Status bar
  status = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 0)
  status.command = "cruxcli.openTerminal"
  status.text = "$(terminal) CruxCLI"
  status.tooltip = "Open CruxCLI"
  context.subscriptions.push(status)
  updateStatus()

  context.subscriptions.push(
    vscode.window.onDidOpenTerminal(updateStatus),
    vscode.window.onDidCloseTerminal(updateStatus),
  )

  // Commands
  context.subscriptions.push(
    vscode.commands.registerCommand("cruxcli.openTerminal", async () => {
      const existing = vscode.window.terminals.find((t) => t.name === TERMINAL_NAME)
      if (existing) {
        existing.show()
        return
      }
      await openTerminal(context, bin)
    }),

    vscode.commands.registerCommand("cruxcli.openNewTerminal", async () => {
      await openTerminal(context, bin)
    }),

    vscode.commands.registerCommand("cruxcli.addFilepathToTerminal", async () => {
      const ref = getActiveFile()
      if (!ref) return
      const terminal = vscode.window.activeTerminal
      if (!terminal || terminal.name !== TERMINAL_NAME) return
      // @ts-ignore
      const port = terminal.creationOptions.env?.["_EXTENSION_CRUXCLI_PORT"]
      port ? await appendPrompt(parseInt(port), ref) : terminal.sendText(ref, false)
      terminal.show()
    }),

    vscode.commands.registerCommand("cruxcli.sendSelection", async () => {
      const editor = vscode.window.activeTextEditor
      if (!editor) return
      const text = editor.document.getText(editor.selection)
      if (!text) return
      const terminal = vscode.window.terminals.find((t) => t.name === TERMINAL_NAME)
      if (!terminal) {
        await openTerminal(context, bin)
        return
      }
      // @ts-ignore
      const port = terminal.creationOptions.env?.["_EXTENSION_CRUXCLI_PORT"]
      if (port) {
        const ref = getActiveFile()
        await appendPrompt(parseInt(port), `${ref}\n\`\`\`\n${text}\n\`\`\``)
      }
      terminal.show()
    }),

    vscode.commands.registerCommand("cruxcli.sendFile", async () => {
      const editor = vscode.window.activeTextEditor
      if (!editor) return
      const ref = getActiveFile()
      if (!ref) return
      const terminal = vscode.window.terminals.find((t) => t.name === TERMINAL_NAME)
      if (!terminal) {
        await openTerminal(context, bin)
        return
      }
      // @ts-ignore
      const port = terminal.creationOptions.env?.["_EXTENSION_CRUXCLI_PORT"]
      if (port) await appendPrompt(parseInt(port), `Look at ${ref}`)
      terminal.show()
    }),

    vscode.commands.registerCommand("cruxcli.openInFolder", async (uri: vscode.Uri) => {
      if (!uri) return
      const terminal = vscode.window.createTerminal({
        name: TERMINAL_NAME,
        cwd: uri.fsPath,
        iconPath: {
          light: vscode.Uri.file(context.asAbsolutePath("images/button-dark.svg")),
          dark: vscode.Uri.file(context.asAbsolutePath("images/button-light.svg")),
        },
        env: { CRUXCLI_CALLER: "vscode" },
      })
      terminal.show()
      terminal.sendText(bin || "cruxcli")
    }),
  )
}

function updateStatus() {
  if (!status) return
  const active = vscode.window.terminals.some((t) => t.name === TERMINAL_NAME)
  if (active) {
    status.text = "$(terminal) CruxCLI"
    status.backgroundColor = new vscode.ThemeColor("statusBarItem.prominentBackground")
    status.show()
  } else {
    status.text = "$(terminal) CruxCLI"
    status.backgroundColor = undefined
    status.show()
  }
}

function findBinary(): string | undefined {
  const configured = vscode.workspace.getConfiguration("cruxcli").get<string>("binaryPath")
  if (configured) return configured
  try {
    execSync("which cruxcli", { stdio: "pipe" })
    return "cruxcli"
  } catch {
    return undefined
  }
}

async function openTerminal(context: vscode.ExtensionContext, bin: string | undefined) {
  const cmd = bin || "cruxcli"
  const port = Math.floor(Math.random() * (65535 - 16384 + 1)) + 16384
  const terminal = vscode.window.createTerminal({
    name: TERMINAL_NAME,
    iconPath: {
      light: vscode.Uri.file(context.asAbsolutePath("images/button-dark.svg")),
      dark: vscode.Uri.file(context.asAbsolutePath("images/button-light.svg")),
    },
    location: { viewColumn: vscode.ViewColumn.Beside, preserveFocus: false },
    env: {
      _EXTENSION_CRUXCLI_PORT: port.toString(),
      CRUXCLI_CALLER: "vscode",
    },
  })

  terminal.show()
  terminal.sendText(`${cmd} --port ${port}`)

  const ref = getActiveFile()
  if (!ref) return

  let tries = 10
  while (tries-- > 0) {
    await new Promise((r) => setTimeout(r, 200))
    try {
      await fetch(`http://localhost:${port}/app`)
      await appendPrompt(port, `In ${ref}`)
      terminal.show()
      return
    } catch {}
  }
}

async function appendPrompt(port: number, text: string) {
  try {
    await fetch(`http://localhost:${port}/tui/append-prompt`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    })
  } catch {}
}

function getActiveFile() {
  const editor = vscode.window.activeTextEditor
  if (!editor) return
  const doc = editor.document
  if (!vscode.workspace.getWorkspaceFolder(doc.uri)) return

  let ref = `@${vscode.workspace.asRelativePath(doc.uri)}`
  const sel = editor.selection
  if (!sel.isEmpty) {
    const start = sel.start.line + 1
    const end = sel.end.line + 1
    ref += start === end ? `#L${start}` : `#L${start}-${end}`
  }
  return ref
}
