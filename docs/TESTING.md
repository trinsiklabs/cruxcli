# CruxCLI Testing Guide

## Prerequisites

- **Bun 1.3+** is required (the test runner is `bun:test`)
- Run tests from `packages/cruxcli/`, **not** from the repo root

## Running Tests

```bash
# From the correct directory
cd packages/cruxcli
bun test

# Run a specific test file
bun test test/session/prompt.test.ts

# Run tests matching a pattern
bun test --filter "token budget"
```

### Do Not Run From Root

The test suite includes a guard (`test/bun.test.ts`) that validates the working directory. Tests that depend on relative paths or the fixture system will fail if run from the repo root. Always `cd packages/cruxcli` first.

## Test Organization

Tests live in `packages/cruxcli/test/` and mirror the source tree structure:

```
test/
  preload.ts              # Test environment setup (runs before all tests)
  fixture/
    fixture.ts            # tmpdir helper and test fixture utilities
    fixture.test.ts       # Tests for the fixture system itself
    db.ts                 # Database fixture helpers
  session/
    prompt.test.ts        # System prompt construction
    llm.test.ts           # LLM integration
    session.test.ts       # Session CRUD
    compaction.test.ts    # Context compaction
    structured-output.test.ts
    retry.test.ts
    message-v2.test.ts
    instruction.test.ts
    revert-compact.test.ts
  tool/
    read.test.ts          # File read tool
    write.test.ts         # File write tool
    edit.test.ts          # File edit tool
    bash.test.ts          # Shell execution tool
    grep.test.ts          # Search tool
    apply_patch.test.ts   # Patch application
    truncation.test.ts    # Output truncation
    question.test.ts      # Question tool
    skill.test.ts         # Skill tool
    webfetch.test.ts      # Web fetch tool
    external-directory.test.ts
    registry.test.ts      # Tool registry
  config/
    config.test.ts        # Config loading and merging
    tui.test.ts           # TUI config
    markdown.test.ts      # Markdown config parsing
    agent-color.test.ts   # Agent color configuration
  provider/
    provider.test.ts      # Provider loading
    transform.test.ts     # Message transforms
    amazon-bedrock.test.ts
    gitlab-duo.test.ts
    copilot/              # GitHub Copilot provider tests
  server/
    session-list.test.ts  # API endpoint tests
    session-select.test.ts
    global-session-list.test.ts
  file/
    index.test.ts         # File operations
    ignore.test.ts        # Gitignore handling
    ripgrep.test.ts       # Ripgrep integration
    fsmonitor.test.ts     # Filesystem monitoring
    path-traversal.test.ts
    time.test.ts          # File time tracking
  util/
    glob.test.ts          # Glob matching
    process.test.ts       # Process utilities
    format.test.ts        # Output formatting
    lock.test.ts          # Lock utilities
    wildcard.test.ts      # Wildcard matching
    lazy.test.ts          # Lazy evaluation
    which.test.ts         # Binary lookup
    filesystem.test.ts    # Filesystem helpers
    iife.test.ts          # IIFE utility
    timeout.test.ts       # Timeout utility
  project/
    project.test.ts       # Project management
    worktree-remove.test.ts
  plugin/
    auth-override.test.ts # Plugin auth
    codex.test.ts         # Codex plugin
  auth/
    auth.test.ts          # Authentication
  lsp/
    client.test.ts        # LSP client
  mcp/
    oauth-browser.test.ts # MCP OAuth
    headers.test.ts       # MCP headers
  cli/
    github-action.test.ts # CI integration
    github-remote.test.ts
    plugin-auth-picker.test.ts
    import.test.ts
    tui/
      transcript.test.ts  # TUI transcript
  pty/
    pty-output-isolation.test.ts
  control-plane/
    workspace-sync.test.ts
    session-proxy-middleware.test.ts
    workspace-server-sse.test.ts
    sse.test.ts
  storage/
    json-migration.test.ts
  question/
    question.test.ts
  permission/
    arity.test.ts
    next.test.ts
  permission-task.test.ts
  patch/
    patch.test.ts
  skill/
    discovery.test.ts
    skill.test.ts
  agent/
    agent.test.ts
  acp/
    event-subscription.test.ts
    agent-interface.test.ts
  snapshot/
    snapshot.test.ts
  memory/
    abort-leak.test.ts
  ide/
    ide.test.ts
  keybind.test.ts
  scheduler.test.ts
  checkpoint/
    checkpoint.test.ts
```

## Test Preload (`test/preload.ts`)

The preload script runs before every test file and handles critical setup:

1. **XDG isolation** -- Sets `XDG_DATA_HOME`, `XDG_CACHE_HOME`, `XDG_CONFIG_HOME`, and `XDG_STATE_HOME` to temporary directories. This prevents tests from reading or writing your real user config.

2. **Home directory isolation** -- Sets `CRUXCLI_TEST_HOME` to a temp directory so tests don't pick up real skills from `~/.claude/skills`.

3. **Managed config isolation** -- Sets `CRUXCLI_TEST_MANAGED_CONFIG_DIR` to prevent tests from reading system-level managed config.

4. **Cache version file** -- Writes a version file to prevent `global/index.ts` from clearing the test cache directory.

5. **Provider key cleanup** -- Deletes all provider API key environment variables (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, etc.) to ensure clean test state.

6. **Models path** -- Sets `CRUXCLI_MODELS_PATH` to a local fixture file instead of fetching from models.dev.

7. **Logging** -- Initializes logging in dev mode with printing disabled.

8. **Cleanup** -- An `afterAll` hook closes the database, runs GC, and removes the temp directory. On Windows, retries removal up to 30 times to handle EBUSY from SQLite WAL handles.

**Important:** XDG variables must be set *before* any `src/` imports because `xdg-basedir` reads them at import time. The preload file handles this ordering.

## The Fixture System (`test/fixture/fixture.ts`)

### `tmpdir(options?)`

Creates an isolated temporary directory for a test. Returns an object with:

- `path` -- Absolute path to the temp directory
- `extra` -- Return value of the `init` callback (if provided)
- `[Symbol.asyncDispose]` -- Cleanup function (stops git fsmonitor, removes directory)

**Options:**

| Option | Type | Description |
|--------|------|-------------|
| `git` | boolean | Initialize a git repo with fsmonitor disabled |
| `config` | Partial<Config.Info> | Write a `cruxcli.json` config file |
| `init` | (dir: string) => Promise<T> | Setup callback |
| `dispose` | (dir: string) => Promise<T> | Teardown callback |

**Usage with `await using` (recommended):**

```typescript
import { tmpdir } from "../fixture/fixture"

test("my test", async () => {
  await using tmp = await tmpdir({ git: true })
  // tmp.path is an isolated git repo
  // Automatically cleaned up when the block exits
})
```

**Usage with manual cleanup:**

```typescript
test("my test", async () => {
  const tmp = await tmpdir({
    git: true,
    config: { model: "anthropic/claude-sonnet-4-20250514" },
  })
  try {
    // test logic
  } finally {
    await tmp[Symbol.asyncDispose]()
  }
})
```

### Key behaviors

- Temp directories are named `cruxcli-test-<random>` in `os.tmpdir()`
- Path sanitization strips null bytes (defensive fix for CI environments)
- Git fixtures disable `core.fsmonitor` to prevent fsmonitor daemon interference
- Git fixtures create an initial empty commit
- Config fixtures write `cruxcli.json` with the provided partial config plus a `$schema` field
- Cleanup stops any running git fsmonitor daemon before removing the directory

### Database Fixture (`test/fixture/db.ts`)

Database fixture helpers for tests that need SQLite state. Imported separately from the main fixture module.

## Writing Tests

### Pattern

Tests follow a consistent pattern:

```typescript
import { describe, expect, test } from "bun:test"
import { tmpdir } from "../fixture/fixture"

describe("feature under test", () => {
  test("specific behavior", async () => {
    await using tmp = await tmpdir({ git: true })
    // Arrange: set up state
    // Act: call the function
    // Assert: verify results
    expect(result).toBe(expected)
  })
})
```

### Guidelines

- Use `await using` for automatic temp directory cleanup
- Always use `tmpdir({ git: true })` when testing features that need a git repo
- Use `tmpdir({ config: {...} })` to test config-dependent behavior
- Do not depend on real API keys or network access in unit tests
- Test files that read `src/` code should import after the preload has set up the environment
- Keep tests focused -- one behavior per test case
