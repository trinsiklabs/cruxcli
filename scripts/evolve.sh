#!/bin/bash
set -e
PROJECT_DIR="/Users/user/personal/cruxcli"
LOG_DIR="${PROJECT_DIR}/.cruxdev/evolution"
STOP_FILE="${LOG_DIR}/STOP"

mkdir -p "${LOG_DIR}"

if [ -f "${STOP_FILE}" ]; then
    echo "[$(date)] STOP file detected." >> "${LOG_DIR}/cron.log"
    exit 0
fi

echo "[$(date)] Evolution cycle starting." >> "${LOG_DIR}/cron.log"
/Users/user/personal/cruxdev/rust/target/release/cruxdev evolve "${PROJECT_DIR}" \
    --repo trinsiklabs/cruxcli --continuous >> "${LOG_DIR}/cron.log" 2>&1
echo "[$(date)] Evolution cycle complete." >> "${LOG_DIR}/cron.log"
