# CruxCLI

A config-layer distribution of [OpenCode](https://github.com/anomalyco/opencode) powered by the [Crux](https://github.com/trinsiklabs/crux) prompt engine.

CruxCLI replaces OpenCode's default prompt system with Crux's mode-driven architecture — dynamic mode prompts, session state tracking, knowledge injection, and safety infrastructure — without modifying OpenCode's source code.

## How It Works

```
Stock OpenCode (unmodified)
    + opencode.json (agent prompt overrides)
    + crux-bridge.js (plugin: mode injection, env reformatting, param tuning)
    + Crux MCP server (34 tools: modes, knowledge, session state, safety)
    = CruxCLI
```

### Bridge Plugin

The bridge plugin (`src/crux-bridge.js`) intercepts OpenCode's prompt pipeline on every LLM call:

- **System transform** — reads Crux session state, injects the active mode prompt, reformats environment blocks, appends session context
- **Message transform** — strips `<system-reminder>` XML tags from synthetic messages
- **Params** — sets temperature and topP based on the active Crux mode (think modes get higher temperature for reasoning)

### Prompt Overrides

Agent prompts in `opencode.json` replace OpenCode's ~1,250-word provider prompts with a ~130-word universal base prompt — 90% token reduction per request.

## Setup

1. Install [OpenCode](https://opencode.ai)
2. Install [Crux MCP server](https://github.com/trinsiklabs/crux)
3. Symlink the bridge plugin into OpenCode's plugin directory:
   ```sh
   ln -s /path/to/cruxcli/src/crux-bridge.js ~/.config/opencode/plugins/crux-bridge.js
   ```
4. Copy or merge the agent overrides from this repo's config into your `~/.config/opencode/opencode.json`
5. Run `opencode`

## Testing

```sh
npm test                # run tests
npm run test:coverage   # run tests with coverage
```

28 tests, 100% line coverage. Zero dependencies — uses Node's built-in test runner.

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the full plan, including the transition from config-layer (Approach 1) to a branded source fork (Approach 2).

## License

MIT
