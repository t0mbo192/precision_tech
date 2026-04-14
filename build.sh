#!/usr/bin/env bash

set -euo pipefail

requested_basepath="${1:-$(basename "$(git rev-parse --show-toplevel)")}"

python3 src/main.py "$requested_basepath"
