#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_ROOT="$HOME/.agents/skills"

if [[ "${1:-}" == "--claude" ]]; then
  TARGET_ROOT="$HOME/.claude/skills"
fi

TARGET="$TARGET_ROOT/fisher-company-analysis"
mkdir -p "$TARGET_ROOT"
rm -rf "$TARGET"
mkdir -p "$TARGET"

for item in SKILL.md README.md VERSION CHANGELOG.md references templates docs; do
  if [[ -e "$SOURCE_DIR/$item" ]]; then
    cp -R "$SOURCE_DIR/$item" "$TARGET/"
  fi
done

echo "Installed Fisher Company Analysis to: $TARGET"
echo "Version: $(cat "$SOURCE_DIR/VERSION")"
