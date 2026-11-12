#!/usr/bin/env bash
# Install The Sharks skills and agent prompts.
# Usage: ./install.sh [claude|project|cursor|all] [project-directory]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="${1:-claude}"

copy_contents() {
  local source="$1" destination="$2"
  mkdir -p "$destination"
  cp -R "$source"/. "$destination"/
}

install_claude_global() {
  copy_contents "$ROOT/.claude/skills" "$HOME/.claude/skills"
  copy_contents "$ROOT/.claude/agents" "$HOME/.claude/agents"
  printf 'Installed The Sharks to ~/.claude (6 skills + 5 agents). Restart Claude Code.\n'
}

install_project() {
  local project="${1:-$PWD}"
  copy_contents "$ROOT/.claude/skills" "$project/.claude/skills"
  copy_contents "$ROOT/.claude/agents" "$project/.claude/agents"
  copy_contents "$ROOT/.agents/skills" "$project/.agents/skills"
  if [[ ! -e "$project/AGENTS.md" ]]; then
    cp "$ROOT/AGENTS.md" "$project/AGENTS.md"
  else
    printf 'Kept existing %s/AGENTS.md; review The Sharks AGENTS.md and merge if needed.\n' "$project"
  fi
  printf 'Installed The Sharks into project: %s\n' "$project"
}

install_cursor() {
  local project="${1:-$PWD}"
  copy_contents "$ROOT/.cursor/rules" "$project/.cursor/rules"
  copy_contents "$ROOT/.agents/skills" "$project/.agents/skills"
  if [[ ! -e "$project/AGENTS.md" ]]; then
    cp "$ROOT/AGENTS.md" "$project/AGENTS.md"
  else
    printf 'Kept existing %s/AGENTS.md; review The Sharks AGENTS.md and merge if needed.\n' "$project"
  fi
  printf 'Installed Cursor rule and portable skills into: %s\n' "$project"
}

case "$TARGET" in
  claude)  install_claude_global ;;
  project) install_project "${2:-$PWD}" ;;
  cursor)  install_cursor "${2:-$PWD}" ;;
  all)     install_claude_global; install_project "${2:-$PWD}"; install_cursor "${2:-$PWD}" ;;
  *)
    printf 'Usage: %s [claude|project|cursor|all] [project-directory]\n' "$0" >&2
    exit 2
    ;;
esac
