#!/bin/bash
set -euo pipefail

###############################################################################
# Script Header
# Name: competitive-safe-apply
# Risk: medium
# Created: 2026-03-27
# Status: active
# Description: Atomically apply generated competitors markdown with backup
###############################################################################

DRY_RUN="${DRY_RUN:-0}"

main() {
    local src="${1:-}"
    local dst="${2:-packages/cruxcli/docs/COMPETITORS.md}"

    if [[ -z "$src" ]]; then
        echo "usage: .opencode/scripts/competitive-safe-apply.sh <source-md> [target-md]" >&2
        exit 1
    fi

    if [[ ! -f "$src" ]]; then
        echo "[competitive-safe-apply] source not found: $src" >&2
        exit 1
    fi

    if [[ ! -s "$src" ]]; then
        echo "[competitive-safe-apply] source is empty: $src" >&2
        exit 1
    fi

    if ! grep -q '^## Gap Analysis' "$src"; then
        echo "[competitive-safe-apply] source missing gap analysis: $src" >&2
        exit 1
    fi

    local dir
    dir="$(dirname "$dst")"
    mkdir -p "$dir"

    local bak
    bak=".crux/backups/competitors/$(date +%Y%m%d-%H%M%S)-$(basename "$dst")"
    mkdir -p "$(dirname "$bak")"

    if [[ "$DRY_RUN" == "1" ]]; then
        echo "[competitive-safe-apply] dry-run source: $src"
        echo "[competitive-safe-apply] dry-run target: $dst"
        if [[ -f "$dst" ]]; then
            echo "[competitive-safe-apply] dry-run backup: $bak"
        fi
        return
    fi

    if [[ -f "$dst" ]]; then
        cp "$dst" "$bak"
        echo "[competitive-safe-apply] backup: $bak"
    fi

    cp "$src" "$dst.tmp"
    mv "$dst.tmp" "$dst"

    if [[ ! -s "$dst" ]]; then
        echo "[competitive-safe-apply] target became empty: $dst" >&2
        if [[ -f "$bak" ]]; then
            cp "$bak" "$dst"
            echo "[competitive-safe-apply] rollback applied from backup" >&2
        fi
        exit 1
    fi

    echo "[competitive-safe-apply] applied: $dst"
}

main "$@"
