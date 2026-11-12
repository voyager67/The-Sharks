# Platform compatibility

The Sharks separates portable role instructions from host-specific execution.

## Portable core
Each role is described in a `SKILL.md` file using the Agent Skills convention. The six canonical skills live in `.agents/skills/`. The provider-neutral agent prompts live in `agents/`.

## Host integrations
- **OpenAI Codex:** Use skills from `.agents/skills/`; subagent delegation depends on the active Codex runtime and configuration.
- **ChatGPT:** Skill availability and agent orchestration depend on the ChatGPT surface, workspace and connected capabilities. Use the portable prompt when importing a skill is unavailable.
- **Claude Code:** The repository includes native skill mirrors in `.claude/skills/` and specialist agent definitions in `.claude/agents/`.
- **Gemini CLI:** Use `GEMINI.md` and the portable skills/prompts. Independent agent execution depends on the installed Gemini CLI capabilities.
- **Cursor:** A project rule is supplied in `.cursor/rules/`; use the portable specialist prompts when separately delegated agents are unavailable.
- **Other model hosts:** Feed the relevant prompt as system/developer instructions or adapt the SKILL.md content to the host's supported role mechanism.

## Important distinction
A model can understand a skill without its host supporting autonomous delegation. When native subagents are unavailable, run the five roles as separate sequential analyses and disclose that this is a simulated panel rather than five independent model runs.
