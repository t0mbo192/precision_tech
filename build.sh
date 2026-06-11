#!/usr/bin/env bash

set -euo pipefail

# Pick a working Python. On Windows, `python3` is usually a Microsoft Store
# stub that exits non-zero, so test by actually running it rather than
# trusting PATH order.
if python3 -c '' >/dev/null 2>&1; then
  python_bin=python3
elif python -c '' >/dev/null 2>&1; then
  python_bin=python
else
  echo "Error: no working Python interpreter found (tried python3, python)." >&2
  exit 1
fi

requested_basepath="${1:-$(basename "$(git rev-parse --show-toplevel)")}"

# MSYS_NO_PATHCONV keeps Git Bash on Windows from rewriting a leading-slash
# basepath into a Windows path; harmless on Linux/macOS.
MSYS_NO_PATHCONV=1 "$python_bin" src/main.py "$requested_basepath" docs
