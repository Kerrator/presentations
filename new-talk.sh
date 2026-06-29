#!/usr/bin/env bash
# Scaffold a new, self-contained talk from template/.
# Usage: ./new-talk.sh 2026-mrs-fall-zr-alloys
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
slug="${1:-}"

if [ -z "$slug" ]; then
  echo "usage: ./new-talk.sh <slug>"
  echo "  e.g. ./new-talk.sh 2026-mrs-fall-zr-alloys"
  exit 1
fi

if [ ! -d "$ROOT/template/lib" ]; then
  echo "template/lib is missing — run ./setup.sh first."
  exit 1
fi

dest="$ROOT/talks/$slug"
if [ -e "$dest" ]; then
  echo "talks/$slug already exists."
  exit 1
fi

cp -r "$ROOT/template" "$dest"
echo "Created talks/$slug"
echo "Preview:  (cd talks/$slug && python3 -m http.server 8000)  ->  http://localhost:8000"
echo "PDF:      http://localhost:8000/?print-pdf  ->  Print  ->  Save as PDF"
