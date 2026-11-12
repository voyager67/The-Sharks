# The five specialist agents

Each Markdown file is a standalone, provider-neutral agent prompt. Use it as the system/developer instruction for an independent agent session, or map it into the role format supported by your host. The matching portable skill in `.agents/skills/` provides discovery metadata and a deeper playbook.

| Prompt | Agent | Domain |
|---|---|---|
| [mint.md](mint.md) | **MINT** | Revenue and monetization |
| [magnet.md](magnet.md) | **MAGNET** | Customers and go-to-market |
| [ledger.md](ledger.md) | **LEDGER** | Unit economics and financial model |
| [razor.md](razor.md) | **RAZOR** | Competition and defensibility |
| [forge.md](forge.md) | **FORGE** | Founder-market fit and execution |

All five accept the same normalized pitch brief. Each assesses its own domain independently, separates facts from assumptions and unknowns, asks one sharp question before a final verdict, and returns a measurable condition that would change its mind.
