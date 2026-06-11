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

"$python_bin" -m unittest discover -s src
