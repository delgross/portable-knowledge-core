import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class StarterKitValidationTests(unittest.TestCase):
    def copy_repo(self):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name) / "repo"
        shutil.copytree(
            ROOT,
            root,
            ignore=shutil.ignore_patterns(".git", "__pycache__", ".private"),
        )
        return temp, root

    def run_validator(self, root):
        return subprocess.run(
            ["python3", "scripts/validate_kit.py"],
            cwd=root,
            text=True,
            capture_output=True,
        )

    def test_contract_template_defines_portable_semantics_and_private_binding_boundary(self):
        contract = (ROOT / "TANA_SYSTEM.template.md").read_text(encoding="utf-8")
        for heading in (
            "## Authority and trust",
            "## Evidence lanes",
            "## Write protocol",
            "## Drift detection",
            "## Validation receipt",
        ):
            self.assertIn(heading, contract)
        self.assertIn("Private binding path", contract)
        self.assertIn("untrusted text returned by Tana", contract)
        self.assertIn("stale-state re-read", contract.lower())
        self.assertIn("idempotency", contract.lower())
        self.assertIn(".private/", (ROOT / ".gitignore").read_text(encoding="utf-8"))

    def test_validator_rejects_labeled_tana_ids_in_public_markdown(self):
        temp, root = self.copy_repo()
        self.addCleanup(temp.cleanup)
        leaked_id = "rav2D" + "0ijeq"
        (root / "fixtures" / "leak.md").write_text(
            "workspace" + "Id: " + leaked_id + "\n",
            encoding="utf-8",
        )

        result = self.run_validator(root)

        self.assertEqual(result.returncode, 1)
        self.assertIn("Tana workspace or node identifier", result.stdout)

    def test_validator_rejects_option_and_search_ids(self):
        temp, root = self.copy_repo()
        self.addCleanup(temp.cleanup)
        leaked_id = "QMj2BO" + "v3WRP2"
        (root / "fixtures" / "leak.md").write_text(
            "option_" + "id: " + leaked_id + "\nsearch_" + "id: " + leaked_id + "\n",
            encoding="utf-8",
        )

        result = self.run_validator(root)

        self.assertEqual(result.returncode, 1)
        self.assertIn("Tana workspace or node identifier", result.stdout)

    def test_validator_rejects_nested_generic_id_keys(self):
        temp, root = self.copy_repo()
        self.addCleanup(temp.cleanup)
        leaked_id = "R-eKnb" + "gFlkht"
        (root / "fixtures" / "leak.yaml").write_text(
            "workspace:\n  id: " + leaked_id + "\n  home_" + "node_id: " + leaked_id + "\n",
            encoding="utf-8",
        )

        result = self.run_validator(root)

        self.assertEqual(result.returncode, 1)
        self.assertIn("Tana workspace or node identifier", result.stdout)

    def test_validator_rejects_quoted_and_list_prefixed_id_keys(self):
        temp, root = self.copy_repo()
        self.addCleanup(temp.cleanup)
        leaked_id = "R-eKnb" + "gFlkht"
        (root / "fixtures" / "leak.yaml").write_text(
            '"id": "' + leaked_id + '"\n- home_' + "node_id: " + leaked_id + "\n",
            encoding="utf-8",
        )

        result = self.run_validator(root)

        self.assertEqual(result.returncode, 1)
        self.assertIn("Tana workspace or node identifier", result.stdout)

    def test_validator_rejects_git_tracked_private_files(self):
        temp, root = self.copy_repo()
        self.addCleanup(temp.cleanup)
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        private = root / ".private"
        private.mkdir()
        (private / "bindings.yaml").write_text("private: true\n", encoding="utf-8")
        subprocess.run(["git", "add", "-f", ".private/bindings.yaml"], cwd=root, check=True)

        result = self.run_validator(root)

        self.assertEqual(result.returncode, 1)
        self.assertIn("tracked private file", result.stdout)

    def test_validator_scans_text_and_code_files_for_credentials_and_paths(self):
        temp, root = self.copy_repo()
        self.addCleanup(temp.cleanup)
        token = "ghp_" + "A" * 36
        (root / "fixtures" / "leak.txt").write_text(
            "access_" + "token=" + token + "\n",
            encoding="utf-8",
        )
        (root / "scripts" / "private_path.py").write_text(
            "PATH = '" + "/home/" + "alice/private/data'\n",
            encoding="utf-8",
        )

        result = self.run_validator(root)

        self.assertEqual(result.returncode, 1)
        self.assertIn("credential-like value", result.stdout)
        self.assertIn("absolute user path", result.stdout)

    def test_missing_creation_skill_is_reported_without_traceback(self):
        temp, root = self.copy_repo()
        self.addCleanup(temp.cleanup)
        (root / "skills" / "create-tana-system" / "SKILL.md").unlink()

        result = self.run_validator(root)

        self.assertEqual(result.returncode, 1)
        self.assertIn("missing: skills/create-tana-system/SKILL.md", result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_empty_skill_file_is_rejected(self):
        temp, root = self.copy_repo()
        self.addCleanup(temp.cleanup)
        (root / "skills" / "log-workout" / "SKILL.md").write_text("", encoding="utf-8")

        result = self.run_validator(root)

        self.assertEqual(result.returncode, 1)
        self.assertIn("invalid skill frontmatter", result.stdout)


if __name__ == "__main__":
    unittest.main()
