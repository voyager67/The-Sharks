# Agent instructions — The Sharks

This repository contains a model-agnostic startup evaluation framework.

## Source of truth
- Portable skills: `.agents/skills/`
- Specialist prompts: `agents/`
- Claude Code adapter: `.claude/`
- Universal prompt: `PROMPT.md`

## Core roles
- THE SHARKS coordinates the panel.
- MINT evaluates revenue and monetization.
- MAGNET evaluates customer acquisition and retention.
- LEDGER audits unit economics and financials.
- RAZOR evaluates competition and defensibility.
- FORGE evaluates founder-market fit and execution.

## Quality bar
Use evidence, not hype. Mark inputs FACT, FOUNDER ESTIMATE, ASSUMPTION or UNKNOWN. Never fabricate numbers or market facts. Ask one sharp question before issuing a specialist verdict. Be tough on the idea and respectful to the founder. Every material objection needs a measurable test and pass/fail threshold.

When modifying a skill, keep equivalent host adapters aligned and update tests or documentation when behavior changes.
