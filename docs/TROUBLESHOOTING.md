# CruxCLI Troubleshooting

**Last Updated:** 2026-03-24

---

## Provider Authentication Failures

### Symptom: "API key not found" or 401 errors

**Cause:** Missing or misconfigured provider API key.

**Fix:**
```bash
# Verify your key is set
echo $ANTHROPIC_API_KEY
echo $OPENROUTER_API_KEY
echo $OPENAI_API_KEY

# Set the appropriate key
export OPENROUTER_API_KEY="sk-or-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
```

Provider credentials are stored in `~/.local/share/cruxcli/auth.json`. If using OAuth-based providers, re-authenticate with `cruxcli auth`.

### Symptom: "Model not found" errors

**Cause:** The selected model is not available from your configured provider, or the models.dev snapshot is stale.

**Fix:**
- Verify the model ID matches what the provider offers.
- CruxCLI fetches model definitions from `models.dev` at runtime with an offline fallback snapshot. If running offline, the snapshot may not include newer models.
- Check provider-specific model availability (some models require waitlist access).

### Symptom: Bedrock/Vertex credential errors

**Cause:** AWS or GCP credential chains are complex and can fail silently.

**Fix:**
- For Bedrock: Ensure `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_REGION` are set, or that your AWS credential chain is properly configured.
- For Vertex: Ensure `GOOGLE_APPLICATION_CREDENTIALS` points to a valid service account JSON, or that Application Default Credentials are configured.

---

## Build Failures

### Symptom: `bunfs` path error during build

```
error: FileNotFound opening "bunfs://root/solid-refresh.js"
```

**Cause:** Bun's internal filesystem resolution fails when the SolidJS plugin tries to load its refresh module during compilation. This can happen when `bun install` was not run cleanly or when node_modules are in an inconsistent state.

**Fix:**
```bash
cd packages/cruxcli
rm -rf node_modules
bun install
bun run build --single
```

### Symptom: TypeScript errors during `bun turbo typecheck`

**Cause:** Type definitions may be out of sync after dependency updates or branch switches.

**Fix:**
```bash
# Clean turbo cache and reinstall
rm -rf .turbo
bun install
bun turbo typecheck
```

The project uses `tsgo` (TypeScript 7.0 native preview) for the core package typecheck. Ensure `@typescript/native-preview` is installed.

### Symptom: Build produces oversized binary

**Cause:** Debug symbols or unoptimized compilation settings.

**Fix:** The production build (`bun run build`) should produce binaries around ~110MB. If significantly larger, check that you are not including development dependencies. The build script at `packages/cruxcli/script/build.ts` handles optimization.

---

## MCP Connection Issues

### Symptom: MCP server fails to connect or tools not appearing

**Cause:** MCP server configuration is incorrect, the server process fails to start, or transport mismatch.

**Fix:**
1. Check configuration in `.mcp.json` or `cruxcli.json`:
   ```json
   {
     "mcpServers": {
       "server-name": {
         "command": "path/to/server",
         "args": ["--flag"],
         "transport": "stdio"
       }
     }
   }
   ```
2. Verify the server binary exists and is executable.
3. For SSE/StreamableHTTP transports, verify the server is running and the URL is reachable.
4. Check logs for MCP handshake errors — the MCP client logs at the `mcp` service namespace.

### Symptom: MCP OAuth flow fails

**Cause:** Browser-based OAuth authorization did not complete, or the callback URL is misconfigured.

**Fix:** Ensure your system can open a browser for the OAuth flow. Check that no firewall or proxy is blocking the localhost callback.

---

## Test Failures

### Symptom: Tests fail when run from the repo root

```
$ bun test
Error: do not run tests from root
```

**Cause:** Tests must be run from the `packages/cruxcli` directory, not the monorepo root. The root `package.json` explicitly blocks this.

**Fix:**
```bash
cd packages/cruxcli
bun test
```

### Symptom: Individual test files fail with module resolution errors

**Cause:** Tests depend on monorepo workspace resolution which requires `bun install` at the root first.

**Fix:**
```bash
# From repo root
bun install

# Then run tests
cd packages/cruxcli
bun test
```

### Symptom: Snapshot tests fail after code changes

**Cause:** Test snapshots are stale after intentional changes.

**Fix:**
```bash
cd packages/cruxcli
bun test --update-snapshots
```

---

## Session Issues

### Symptom: "Context overflow" or compaction errors

**Cause:** The conversation has exceeded the model's context window and compaction failed.

**Fix:**
- Start a new session for long-running tasks.
- Use a model with a larger context window.
- Compaction is automatic (triggers when tokens approach model limit minus 20K buffer). If it fails, check that the configured compaction model is accessible.

### Symptom: Checkpoint restore fails

**Cause:** The checkpoint's git tree hash no longer exists (pruned by garbage collection) or the checkpoint JSON is corrupted.

**Fix:**
- Checkpoints are pruned after 7 days by the snapshot cleanup scheduler.
- Check available checkpoints: `cruxcli checkpoint list`
- If the tree hash was garbage collected, the checkpoint cannot be restored.

---

## Database Issues

### Symptom: Database locked errors

**Cause:** Multiple CruxCLI processes competing for the SQLite database.

**Fix:**
- CruxCLI uses WAL mode with `busy_timeout = 5000`. If timeouts persist, ensure only one primary CruxCLI server is running per data directory.
- Check for zombie processes: `ps aux | grep cruxcli`

### Symptom: JSON-to-SQLite migration fails

**Cause:** Corrupt or unexpected JSON data in the legacy storage directory.

**Fix:**
- Migration errors are logged but non-fatal — the migration continues, skipping corrupt entries.
- Check logs for specific errors (logged at `json-migration` service).
- If needed, the legacy JSON storage is at `~/.local/share/cruxcli/storage/`. Back it up before retrying.

---

## Environment Issues

### Symptom: CruxCLI command not found after installation

**Fix:**
```bash
# Check if the binary is in PATH
which cruxcli

# If installed via npm, ensure global bin is in PATH
npm bin -g

# If installed via curl, the default location is ~/.local/bin/cruxcli
export PATH="$HOME/.local/bin:$PATH"
```

### Symptom: LSP features not working

**Cause:** Language servers are not installed or LSP is disabled in config.

**Fix:**
- Ensure the language server for your language is installed (e.g., `pyright` for Python).
- Check that LSP is not disabled in config: `"lsp": false` in `cruxcli.json` disables it.
- Experimental LSP servers may require feature flags (e.g., `CRUXCLI_EXPERIMENTAL_LSP_TY`).
