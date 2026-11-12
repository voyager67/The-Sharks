# Contributing to The Sharks

Thanks for helping make startup feedback more rigorous and more useful.

## Good contributions

- Better, non-overlapping questions for one of the five Sharks.
- Evaluation cases that reveal hallucinations, shallow critique or unfair verdicts.
- Industry-specific or regional references that improve the workflow without hard-coding assumptions.
- Improved one-week experiments and measurable success/failure thresholds.
- Provider adapters that are tested and clearly label platform limitations.
- Documentation, accessibility, translation and examples.

## Before opening a pull request

1. Keep the orchestrator and five specialist mandates distinct.
2. Do not invent market facts or turn illustrative numbers into defaults.
3. Mark all synthetic examples as synthetic.
4. Do not include real founder, investor, employee or customer personal data.
5. Run `python scripts/validate_repo.py` and `python -m unittest discover -s tests -v`.
6. Explain what changed, why it helps and how you verified it.

## Agent behavior changes

When changing a specialist's core behavior, update all of the following as applicable:

- `.agents/skills/<specialist-skill>/SKILL.md`
- `agents/<specialist>.md`
- `.claude/agents/<specialist>.md`
- The matching entry in `manifest.yaml`
- The master skill and `PROMPT.md` if the orchestration contract changes

Keep compatibility claims factual. A provider's ability to read `SKILL.md` does not automatically mean it can start five independent agents.

## Pull requests

Prefer focused changes. Include a test or a clear manual verification note for behavior changes. Do not add secrets, private datasets, credentials or real pitch decks.
