function truthy(key: string) {
  const value = process.env[key]?.toLowerCase()
  return value === "true" || value === "1"
}

function falsy(key: string) {
  const value = process.env[key]?.toLowerCase()
  return value === "false" || value === "0"
}

export namespace Flag {
  export const CRUXCLI_AUTO_SHARE = truthy("CRUXCLI_AUTO_SHARE")
  export const CRUXCLI_GIT_BASH_PATH = process.env["CRUXCLI_GIT_BASH_PATH"]
  export const CRUXCLI_CONFIG = process.env["CRUXCLI_CONFIG"]
  export declare const CRUXCLI_TUI_CONFIG: string | undefined
  export declare const CRUXCLI_CONFIG_DIR: string | undefined
  export const CRUXCLI_CONFIG_CONTENT = process.env["CRUXCLI_CONFIG_CONTENT"]
  export const CRUXCLI_DISABLE_AUTOUPDATE = truthy("CRUXCLI_DISABLE_AUTOUPDATE")
  export const CRUXCLI_DISABLE_PRUNE = truthy("CRUXCLI_DISABLE_PRUNE")
  export const CRUXCLI_DISABLE_TERMINAL_TITLE = truthy("CRUXCLI_DISABLE_TERMINAL_TITLE")
  export const CRUXCLI_PERMISSION = process.env["CRUXCLI_PERMISSION"]
  export const CRUXCLI_DISABLE_DEFAULT_PLUGINS = truthy("CRUXCLI_DISABLE_DEFAULT_PLUGINS")
  export const CRUXCLI_DISABLE_LSP_DOWNLOAD = truthy("CRUXCLI_DISABLE_LSP_DOWNLOAD")
  export const CRUXCLI_ENABLE_EXPERIMENTAL_MODELS = truthy("CRUXCLI_ENABLE_EXPERIMENTAL_MODELS")
  export const CRUXCLI_DISABLE_AUTOCOMPACT = truthy("CRUXCLI_DISABLE_AUTOCOMPACT")
  export const CRUXCLI_DISABLE_MODELS_FETCH = truthy("CRUXCLI_DISABLE_MODELS_FETCH")
  export const CRUXCLI_DISABLE_CLAUDE_CODE = truthy("CRUXCLI_DISABLE_CLAUDE_CODE")
  export const CRUXCLI_DISABLE_CLAUDE_CODE_PROMPT =
    CRUXCLI_DISABLE_CLAUDE_CODE || truthy("CRUXCLI_DISABLE_CLAUDE_CODE_PROMPT")
  export const CRUXCLI_DISABLE_CLAUDE_CODE_SKILLS =
    CRUXCLI_DISABLE_CLAUDE_CODE || truthy("CRUXCLI_DISABLE_CLAUDE_CODE_SKILLS")
  export const CRUXCLI_DISABLE_EXTERNAL_SKILLS =
    CRUXCLI_DISABLE_CLAUDE_CODE_SKILLS || truthy("CRUXCLI_DISABLE_EXTERNAL_SKILLS")
  export declare const CRUXCLI_DISABLE_PROJECT_CONFIG: boolean
  export const CRUXCLI_FAKE_VCS = process.env["CRUXCLI_FAKE_VCS"]
  export declare const CRUXCLI_CLIENT: string
  export const CRUXCLI_SERVER_PASSWORD = process.env["CRUXCLI_SERVER_PASSWORD"]
  export const CRUXCLI_SERVER_USERNAME = process.env["CRUXCLI_SERVER_USERNAME"]
  export const CRUXCLI_ENABLE_QUESTION_TOOL = truthy("CRUXCLI_ENABLE_QUESTION_TOOL")

  // Experimental
  export const CRUXCLI_EXPERIMENTAL = truthy("CRUXCLI_EXPERIMENTAL")
  export const CRUXCLI_EXPERIMENTAL_FILEWATCHER = truthy("CRUXCLI_EXPERIMENTAL_FILEWATCHER")
  export const CRUXCLI_EXPERIMENTAL_DISABLE_FILEWATCHER = truthy("CRUXCLI_EXPERIMENTAL_DISABLE_FILEWATCHER")
  export const CRUXCLI_EXPERIMENTAL_ICON_DISCOVERY =
    CRUXCLI_EXPERIMENTAL || truthy("CRUXCLI_EXPERIMENTAL_ICON_DISCOVERY")

  const copy = process.env["CRUXCLI_EXPERIMENTAL_DISABLE_COPY_ON_SELECT"]
  export const CRUXCLI_EXPERIMENTAL_DISABLE_COPY_ON_SELECT =
    copy === undefined ? process.platform === "win32" : truthy("CRUXCLI_EXPERIMENTAL_DISABLE_COPY_ON_SELECT")
  export const CRUXCLI_ENABLE_EXA =
    truthy("CRUXCLI_ENABLE_EXA") || CRUXCLI_EXPERIMENTAL || truthy("CRUXCLI_EXPERIMENTAL_EXA")
  export const CRUXCLI_EXPERIMENTAL_BASH_DEFAULT_TIMEOUT_MS = number("CRUXCLI_EXPERIMENTAL_BASH_DEFAULT_TIMEOUT_MS")
  export const CRUXCLI_EXPERIMENTAL_OUTPUT_TOKEN_MAX = number("CRUXCLI_EXPERIMENTAL_OUTPUT_TOKEN_MAX")
  export const CRUXCLI_EXPERIMENTAL_OXFMT = CRUXCLI_EXPERIMENTAL || truthy("CRUXCLI_EXPERIMENTAL_OXFMT")
  export const CRUXCLI_EXPERIMENTAL_LSP_TY = truthy("CRUXCLI_EXPERIMENTAL_LSP_TY")
  export const CRUXCLI_EXPERIMENTAL_LSP_TOOL = CRUXCLI_EXPERIMENTAL || truthy("CRUXCLI_EXPERIMENTAL_LSP_TOOL")
  export const CRUXCLI_DISABLE_FILETIME_CHECK = truthy("CRUXCLI_DISABLE_FILETIME_CHECK")
  export const CRUXCLI_EXPERIMENTAL_PLAN_MODE = CRUXCLI_EXPERIMENTAL || truthy("CRUXCLI_EXPERIMENTAL_PLAN_MODE")
  export const CRUXCLI_EXPERIMENTAL_MARKDOWN = !falsy("CRUXCLI_EXPERIMENTAL_MARKDOWN")
  export const CRUXCLI_MODELS_URL = process.env["CRUXCLI_MODELS_URL"]
  export const CRUXCLI_MODELS_PATH = process.env["CRUXCLI_MODELS_PATH"]

  function number(key: string) {
    const value = process.env[key]
    if (!value) return undefined
    const parsed = Number(value)
    return Number.isInteger(parsed) && parsed > 0 ? parsed : undefined
  }
}

// Dynamic getter for CRUXCLI_DISABLE_PROJECT_CONFIG
// This must be evaluated at access time, not module load time,
// because external tooling may set this env var at runtime
Object.defineProperty(Flag, "CRUXCLI_DISABLE_PROJECT_CONFIG", {
  get() {
    return truthy("CRUXCLI_DISABLE_PROJECT_CONFIG")
  },
  enumerable: true,
  configurable: false,
})

// Dynamic getter for CRUXCLI_TUI_CONFIG
// This must be evaluated at access time, not module load time,
// because tests and external tooling may set this env var at runtime
Object.defineProperty(Flag, "CRUXCLI_TUI_CONFIG", {
  get() {
    return process.env["CRUXCLI_TUI_CONFIG"]
  },
  enumerable: true,
  configurable: false,
})

// Dynamic getter for CRUXCLI_CONFIG_DIR
// This must be evaluated at access time, not module load time,
// because external tooling may set this env var at runtime
Object.defineProperty(Flag, "CRUXCLI_CONFIG_DIR", {
  get() {
    return process.env["CRUXCLI_CONFIG_DIR"]
  },
  enumerable: true,
  configurable: false,
})

// Dynamic getter for CRUXCLI_CLIENT
// This must be evaluated at access time, not module load time,
// because some commands override the client at runtime
Object.defineProperty(Flag, "CRUXCLI_CLIENT", {
  get() {
    return process.env["CRUXCLI_CLIENT"] ?? "cli"
  },
  enumerable: true,
  configurable: false,
})
