#!/usr/bin/env bash
set -euo pipefail

workspace="${1:-${PWD}}"

if ! command -v tokensave >/dev/null 2>&1; then
    echo "tokensave is not installed; rebuild the devcontainer to install it." >&2
    exit 1
fi

if [ -d "${workspace}/.tokensave" ]; then
    tokensave sync "${workspace}"
else
    tokensave init "${workspace}"
fi
