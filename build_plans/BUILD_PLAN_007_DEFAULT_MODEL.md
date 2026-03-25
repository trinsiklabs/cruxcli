# Prompt To Save Manual Model Changes As Default
## Goal
When a user manually changes models in CruxCLI, prompt them to optionally save that choice as their new default model so startup behavior matches user intent and no longer feels inconsistent with in-session model selection.
## Document Alignment
- Preserve existing CruxCLI config precedence rules
- Do not override managed/admin-controlled config
- Do not change behavior for explicit CLI `--model` overrides
- Keep current recent/favorite model behavior intact
## Phase 1 - Trace existing model selection flow
- [x] Identify all user-initiated model change entry points in the TUI and CLI
- [x] Confirm where current model changes are persisted to recent history
- [x] Confirm where configured default model is loaded at startup
- [x] Document which model changes are manual vs automatic/fallback
## Phase 2 - Define prompt behavior
- [x] Add a user-facing decision flow for manual model changes
- [x] Prompt only when the chosen model differs from the current configured default
- [x] Skip prompting for automatic fallback selections
- [x] Skip prompting for temporary CLI override sessions
- [x] Add an opt-out path such as "Never ask again"
## Phase 3 - Persist default model choice
- [x] Update user config write path to save `model: "provider/model"`
- [x] Create user config file if it does not already exist
- [x] Preserve existing config structure and formatting as much as practical
- [x] Fail safely when config is not writable or is managed by higher-precedence config
## Phase 4 - UX integration
- [x] Hook the prompt into manual model selection handlers
- [x] Ensure the prompt appears only once per explicit change event
- [x] Show clear confirmation when the default is updated
- [x] Respect a config flag to disable future prompts
## Phase 5 - Tests
- [x] Add tests for prompting after manual model change
- [x] Add tests for no prompt when selected model already matches config default
- [x] Add tests for no prompt on `--model` override sessions
- [x] Add tests for opt-out behavior
- [x] Add tests for config write failure / managed config cases
## Phase 6 - Verification
- [x] Run targeted tests for config and TUI model selection logic
- [x] Manually verify changing models prompts once
- [x] Manually verify accepting the prompt updates startup default
- [x] Manually verify declining keeps session-only behavior
- [x] Manually verify "Never ask again" suppresses future prompts
## Convergence Criteria
- Manual model changes prompt to save as default exactly when intended
- Accepting the prompt updates the startup default model
- Declining preserves current-session selection without changing config
- Temporary and automatic selections do not prompt
- Tests pass and no existing model selection flows regress
## Test Command
- [x] Run package tests from `packages/cruxcli` with the project’s standard test command
