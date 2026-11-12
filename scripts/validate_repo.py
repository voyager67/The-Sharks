#!/usr/bin/env python3
"""Validate The Sharks skills, specialist prompts, native agents and README assets."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = {
    "mint": "mint-revenue-shark",
    "magnet": "magnet-customer-shark",
    "ledger": "ledger-numbers-shark",
    "razor": "razor-competition-shark",
    "forge": "forge-founder-shark",
}

def read(path: Path) -> str:
    if not path.is_file():
        raise ValueError(f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")

def metadata(path: Path) -> dict[str, str]:
    content = read(path)
    if not content.startswith("---\n"):
        raise ValueError(f"Missing YAML frontmatter: {path.relative_to(ROOT)}")
    try:
        _, raw, _ = content.split("---", 2)
    except ValueError as exc:
        raise ValueError(f"Malformed frontmatter: {path.relative_to(ROOT)}") from exc
    result: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip("\"'")
    for key in ("name", "description"):
        if not result.get(key):
            raise ValueError(f"Missing {key} in {path.relative_to(ROOT)}")
    return result

def validate() -> list[str]:
    errors: list[str] = []
    skill_root = ROOT / ".agents" / "skills"
    skill_names = {"the-sharks": "the-sharks", **AGENTS}
    # The five specialist folders use descriptive skill slugs.
    skill_names = {"the-sharks": "the-sharks", **{slug: slug for slug in AGENTS.values()}}
    for folder, expected_name in skill_names.items():
        path = skill_root / folder / "SKILL.md"
        try:
            meta = metadata(path)
            if meta["name"] != expected_name:
                errors.append(f"Skill name mismatch in {path.relative_to(ROOT)}")
        except ValueError as exc:
            errors.append(str(exc))

    for agent, slug in AGENTS.items():
        try:
            canonical = read(skill_root / slug / "SKILL.md")
            mirrored = read(ROOT / ".claude" / "skills" / slug / "SKILL.md")
            if canonical != mirrored:
                errors.append(f"Claude skill mirror is out of sync: {slug}")
            for relative in (f"agents/{agent}.md", f".claude/agents/{agent}.md"):
                body = read(ROOT / relative)
                if len(body.strip()) < 250 or agent.upper() not in body:
                    errors.append(f"Agent prompt is incomplete: {relative}")
            native = metadata(ROOT / ".claude" / "agents" / f"{agent}.md")
            if native.get("name") != agent:
                errors.append(f"Claude agent name mismatch: {agent}")
        except ValueError as exc:
            errors.append(str(exc))

    required = [
        "README.md", "PROMPT.md", "manifest.yaml", "LICENSE", "AGENTS.md", "GEMINI.md",
        "install.sh", ".cursor/rules/the-sharks.mdc",
        "assets/readme/hero-the-sharks.svg", "assets/readme/agents-lineup.svg",
        "assets/readme/architecture.svg",
        "docs/architecture.md", "docs/compatibility.md", "examples/example-session.md",
        "templates/pitch-brief.md", "templates/scorecard.md",
        "agents/README.md", ".claude/README.md", ".claude/skills/README.md",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    master = skill_root / "the-sharks" / "SKILL.md"
    try:
        text = read(master).lower()
        for token in ("mint", "magnet", "ledger", "razor", "forge", "pitch again", "deal meter", "fix list", "kill shot"):
            if token not in text:
                errors.append(f"Master skill missing workflow token: {token}")
    except ValueError as exc:
        errors.append(str(exc))

    return errors

if __name__ == "__main__":
    problems = validate()
    if problems:
        print("The Sharks validation FAILED:")
        for problem in problems:
            print(f" - {problem}")
        sys.exit(1)
    print("The Sharks validation PASSED: 6 skills, 5 specialist prompts, 5 native subagents, adapters and examples are present.")
