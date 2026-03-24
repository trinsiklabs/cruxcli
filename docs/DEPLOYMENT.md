# Deployment

**Last Updated:** 2026-03-24

## Overview

CruxCLI is distributed as a compiled Bun binary across 10 platform targets. Distribution channels include GitHub Releases, npm, Homebrew, AUR, Docker, and a curl installer.

## Build

```bash
cd packages/opencode
bun run build --single          # Current platform only
bun run build                   # All 10 targets
bun run build --single --skip-install  # Skip dependency install (faster rebuild)
```

The build script (`script/build.ts`):
1. Fetches model snapshot from models.dev
2. Loads SQL migrations from `migration/` directory
3. Compiles via `Bun.build()` with SolidJS plugin, embedded migrations, and model data
4. Produces binaries in `dist/<target>/bin/cruxcli`

### Platform Targets

| Target | OS | Arch | Variant |
|--------|-----|------|---------|
| cruxcli-linux-arm64 | Linux | arm64 | glibc |
| cruxcli-linux-x64 | Linux | x64 | glibc |
| cruxcli-linux-x64-baseline | Linux | x64 | no AVX2 |
| cruxcli-linux-arm64-musl | Linux | arm64 | musl |
| cruxcli-linux-x64-musl | Linux | x64 | musl |
| cruxcli-linux-x64-musl-baseline | Linux | x64 | musl, no AVX2 |
| cruxcli-darwin-arm64 | macOS | arm64 | Apple Silicon |
| cruxcli-darwin-x64 | macOS | x64 | Intel |
| cruxcli-darwin-x64-baseline | macOS | x64 | no AVX2 |
| cruxcli-windows-x64 | Windows | x64 | — |

## Release Process

Releases are triggered by the `publish.yml` workflow on push to `dev` or `beta` branches, or manual dispatch.

1. `script/version.ts` determines version from git tags
2. `script/build.ts` compiles all targets, uploads to GitHub Release
3. `script/publish.ts` publishes to:
   - **npm** — `cruxcli` package + platform-specific binary packages
   - **Homebrew** — updates `trinsiklabs/homebrew-tap` formula
   - **AUR** — updates `cruxcli-bin` PKGBUILD
   - **Docker** — `ghcr.io/trinsiklabs/cruxcli` (multi-arch)
4. `sign-cli.yml` signs binaries via SignPath

## Installation Channels

| Channel | Command |
|---------|---------|
| curl | `curl -fsSL https://cruxcli.ai/install \| bash` |
| npm | `npm i -g cruxcli@latest` |
| Homebrew | `brew install trinsiklabs/tap/cruxcli` |
| AUR | `paru -S cruxcli-bin` |
| Docker | `docker pull ghcr.io/trinsiklabs/cruxcli` |
| Scoop | `scoop install cruxcli` |

## Environment

Required:
- At least one LLM provider API key (e.g., `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`)

Optional:
- `CRUXCLI_CONFIG_DIR` — custom config directory
- `CRUXCLI_DISABLE_AUTO_CHECKPOINT` — disable auto-checkpoints
- See `src/flag/flag.ts` for all 40+ environment variables
