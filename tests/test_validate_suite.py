"""Negative packaging cases: a passing suite must reject broken installs."""

from pathlib import Path
import importlib.util
import json
import shutil
import tempfile
import unittest


PROJECT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", PROJECT / "scripts/validate_suite.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class SuiteValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="suite-", dir=PROJECT / "tests")
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name)
        self.root = self.project / "skills"
        shutil.copytree(PROJECT / "skills", self.root)
        shutil.copytree(PROJECT / ".codex-plugin", self.project / ".codex-plugin")
        shutil.copytree(PROJECT / "evals", self.project / "evals")
        shutil.copy2(PROJECT / "plugin.json", self.project / "plugin.json")

    def validate(self):
        return validator.validate(self.root)

    def test_complete_suite(self):
        errors, count = self.validate()
        self.assertEqual(errors, [])
        self.assertEqual(count, 11)

    def test_missing_shared_dependency(self):
        (self.root / "pragmatic-engineering/references/working-agreement.md").unlink()
        errors, _ = self.validate()
        self.assertTrue(any("Missing shared" in error for error in errors))

    def test_missing_git_practices(self):
        (self.root / "pragmatic-engineering/references/git-practices.md").unlink()
        errors, _ = self.validate()
        self.assertTrue(any("Missing shared Git practices" in error for error in errors))

    def test_missing_development_philosophy_guide(self):
        (self.root / "pragmatic-engineering/references/development-philosophies.md").unlink()
        errors, _ = self.validate()
        self.assertTrue(any("Missing shared development philosophy" in error for error in errors))

    def test_commit_skill_must_route_to_git_practices(self):
        file = self.root / "pragmatic-commits/SKILL.md"
        file.write_text(file.read_text().replace(
            "[Git practices](../pragmatic-engineering/references/git-practices.md)",
            "Git practices",
        ))
        errors, _ = self.validate()
        self.assertTrue(any("missing Git practices link" in error for error in errors))

    def test_missing_routed_skill(self):
        shutil.rmtree(self.root / "pragmatic-testing")
        errors, _ = self.validate()
        self.assertTrue(any("Missing expected skills" in error for error in errors))

    def test_folder_name_mismatch(self):
        (self.root / "pragmatic-review").rename(self.root / "renamed-review")
        errors, _ = self.validate()
        self.assertTrue(any("folder mismatch" in error for error in errors))

    def test_escaping_reference(self):
        file = self.root / "pragmatic-testing/SKILL.md"
        file.write_text(file.read_text() + "\n[external](../../outside.md)\n")
        errors, _ = self.validate()
        self.assertTrue(any("escapes suite" in error for error in errors))

    def test_missing_description(self):
        file = self.root / "pragmatic-testing/SKILL.md"
        file.write_text("\n".join(
            line for line in file.read_text().splitlines()
            if not line.startswith("description:")
        ) + "\n")
        errors, _ = self.validate()
        self.assertTrue(any("description length" in error for error in errors))

    def test_duplicate_metadata(self):
        file = self.root / "pragmatic-testing/SKILL.md"
        text = file.read_text().replace(
            "name: pragmatic-testing\n",
            "name: pragmatic-testing\nname: pragmatic-review\n",
        )
        file.write_text(text)
        errors, _ = self.validate()
        self.assertTrue(any("duplicate field" in error for error in errors))

    def test_non_english_public_skill(self):
        file = self.root / "pragmatic-testing/SKILL.md"
        file.write_text(file.read_text() + "\n\u4e2d\u6587 content\n")
        errors, _ = self.validate()
        self.assertTrue(any("must be English" in error for error in errors))

    def test_missing_openai_metadata(self):
        (self.root / "pragmatic-testing/agents/openai.yaml").unlink()
        errors, _ = self.validate()
        self.assertTrue(any("missing agents/openai.yaml" in error for error in errors))

    def test_manifest_version_mismatch(self):
        path = self.project / "plugin.json"
        data = json.loads(path.read_text())
        data["version"] = "0.2.0"
        path.write_text(json.dumps(data))
        errors, _ = self.validate()
        self.assertIn("Plugin manifest versions do not match.", errors)

    def test_unknown_eval_skill(self):
        path = self.project / "evals/cases.json"
        data = json.loads(path.read_text())
        data["cases"][0]["skills"] = ["unknown-skill"]
        path.write_text(json.dumps(data))
        errors, _ = self.validate()
        self.assertTrue(any("uses unknown skills" in error for error in errors))

    def test_fixture_drift(self):
        path = self.project / "evals/runs/review-only/fixture/accounts.py"
        path.write_text(path.read_text() + "\n# drift\n")
        errors, _ = self.validate()
        self.assertTrue(any("fixture drift" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
