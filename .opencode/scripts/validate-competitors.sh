#!/bin/bash
set -euo pipefail

###############################################################################
# Script Header
# Name: validate-competitors
# Risk: low
# Created: 2026-03-27
# Status: active
# Description: Validate competitors docs are non-empty and structured
###############################################################################

DRY_RUN="${DRY_RUN:-0}"

main() {
    local files=(
        "docs/COMPETITORS.md"
        "packages/cruxcli/docs/COMPETITORS.md"
    )

    for file in "${files[@]}"; do
        if [[ ! -f "$file" ]]; then
            echo "[validate-competitors] missing file: $file" >&2
            exit 1
        fi

        if [[ ! -s "$file" ]]; then
            echo "[validate-competitors] empty file: $file" >&2
            exit 1
        fi

        if ! grep -qE '^# .*Competitors|^# .*Competitive Analysis' "$file"; then
            echo "[validate-competitors] missing title heading: $file" >&2
            exit 1
        fi

        if ! grep -qE '^## Gap Analysis|^## Feature Matrix' "$file"; then
            echo "[validate-competitors] missing analysis section: $file" >&2
            exit 1
        fi
    done

    if [[ "$DRY_RUN" == "1" ]]; then
        echo "[validate-competitors] dry-run ok"
        return
    fi

    echo "[validate-competitors] ok"
}

main "$@"
