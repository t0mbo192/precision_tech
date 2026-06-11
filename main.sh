#!/usr/bin/env bash

set -euo pipefail

# Pick a working Python (see note in build.sh).
if python3 -c '' >/dev/null 2>&1; then
  python_bin=python3
elif python -c '' >/dev/null 2>&1; then
  python_bin=python
else
  echo "Error: no working Python interpreter found (tried python3, python)." >&2
  exit 1
fi

# MSYS_NO_PATHCONV stops Git Bash on Windows from rewriting the "/" basepath
# into a Windows path (e.g. C:/Program Files/Git/); harmless on Linux/macOS.
MSYS_NO_PATHCONV=1 "$python_bin" src/main.py / .preview
cd .preview && "$python_bin" -m http.server 8888
