# The Sharks 🦈

**Build with conviction. Validate with evidence. Survive the market.**

Five specialist AI agents. One orchestrator. A startup reality-check panel that challenges your idea before the market does.

## The panel

| Agent | Focus | Core question |
|---|---|---|
| **MINT** | Revenue & monetization | Who pays, how much, why now—and why again? |
| **MAGNET** | Customers & growth | Can you reach your first 100 customers at a viable cost? |
| **LEDGER** | Unit economics & financials | Does each sale make money after every real cost? |
| **RAZOR** | Competition & defensibility | Why switch to you—and what stops others copying you? |
| **FORGE** | Founder-market fit & execution | Why is this team equipped to win this market? |

## What is included

- One master **THE SHARKS** orchestrator skill.
- Five specialist skills, one for each agent.
- Five provider-neutral agent prompts.
- Native Claude Code subagent definitions and skill adapters.
- Portable Agent Skills format, plus Cursor and Gemini guidance.
- Universal prompt for chat-based AI systems.
- Pitch brief, scorecard, worked example, installer, validation tests and documentation.

## Get started

1. Download [The-Sharks-v1.1.0.zip](The-Sharks-v1.1.0.zip) from the repository root.
2. Extract it.
3. Open the extracted `the-sharks` directory as your project.
4. Follow [QUICKSTART.md](QUICKSTART.md).

For a quick test with any chat-based AI, start with [PROMPT.md](PROMPT.md).

## Modes

- `PITCH TO THE SHARKS` — full five-agent evaluation.
- `SPEED ROUND` — concise verdicts and top fixes.
- `ASK MINT`, `ASK MAGNET`, `ASK LEDGER`, `ASK RAZOR`, `ASK FORGE` — specialist reviews.
- `PITCH AGAIN` — reassess using new evidence.

## Quality

Run:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
bash -n install.sh
```

## Design principle

The Sharks are not cheerleaders. Each objection should be specific, evidence-aware and paired with a concrete experiment. Unknowns are labelled—not invented. The panel is a practice and decision-support tool, not financial, legal, tax or investment advice.

## Credits

The concept is inspired by the free Shark Panel prompt by [@aiwithakshh](https://instagram.com/aiwithakshh). This is an independent, substantially rewritten implementation. See `CREDITS.md` in the package.

**Built by Harsh Singh.** Released under the MIT License.
