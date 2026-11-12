import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_repo", ROOT / "scripts" / "validate_repo.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class RepositoryValidationTests(unittest.TestCase):
    def test_repository_inventory_is_valid(self):
        self.assertEqual(MODULE.validate(), [])

    def test_all_five_specialist_skills_exist(self):
        for slug in MODULE.AGENTS.values():
            with self.subTest(slug=slug):
                self.assertTrue((ROOT / ".agents" / "skills" / slug / "SKILL.md").is_file())

    def test_portable_prompt_includes_all_specialists_and_modes(self):
        content = (ROOT / "PROMPT.md").read_text(encoding="utf-8").lower()
        for token in ("mint", "magnet", "ledger", "razor", "forge", "pitch again", "deal meter", "kill shot", "fix list"):
            with self.subTest(token=token):
                self.assertIn(token, content)

    def test_claude_native_agents_load_their_matching_skills(self):
        for agent, slug in MODULE.AGENTS.items():
            text = (ROOT / ".claude" / "agents" / f"{agent}.md").read_text(encoding="utf-8")
            with self.subTest(agent=agent):
                self.assertIn(f"- {slug}", text)


if __name__ == "__main__":
    unittest.main()
