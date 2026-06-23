import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "openclaw" / "agentnomos-governance-preflight"
SKILL_PATH = SKILL_DIR / "SKILL.md"
MANIFEST_PATH = SKILL_DIR / "ARTIFACT_MANIFEST.json"
EXPECTED_SKILL_SHA256 = "fb42f45dd1994c1ae62bc543cc2227c552074c2681a51f75980b1815942b430e"
EXPECTED_SKILL_BYTES = 7586
EXPECTED_SKILL_LINES = 251


class RepositoryIntegrityTest(unittest.TestCase):
    def test_published_skill_matches_sealed_artifact(self) -> None:
        data = SKILL_PATH.read_bytes()
        self.assertEqual(hashlib.sha256(data).hexdigest(), EXPECTED_SKILL_SHA256)
        self.assertEqual(len(data), EXPECTED_SKILL_BYTES)
        self.assertEqual(data.count(b"\n"), EXPECTED_SKILL_LINES)

    def test_manifest_matches_skill(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        published = manifest["published_files"]
        self.assertEqual(len(published), 1)
        artifact = published[0]
        self.assertEqual(artifact["path"], "SKILL.md")
        self.assertEqual(artifact["sha256"], EXPECTED_SKILL_SHA256)
        self.assertEqual(artifact["bytes"], EXPECTED_SKILL_BYTES)
        self.assertEqual(artifact["lines"], EXPECTED_SKILL_LINES)
        self.assertEqual(artifact["content_import_status"], "verified_exact")
        self.assertIs(artifact["byte_identical_to_published_clawhub_version"], True)
        self.assertIs(manifest["execution_enabled"], False)

    def test_all_json_files_are_valid(self) -> None:
        json_files = sorted(
            list((ROOT / "schemas").glob("*.json"))
            + list((ROOT / "examples").glob("*.json"))
            + [MANIFEST_PATH]
        )
        self.assertGreater(len(json_files), 0)
        for path in json_files:
            with self.subTest(path=path.relative_to(ROOT)):
                json.loads(path.read_text(encoding="utf-8"))

    def test_every_example_preserves_public_invariants(self) -> None:
        valid_decisions = {"ADVISORY_ALLOW", "HOLD_FOR_REVIEW", "BLOCK"}
        for path in sorted((ROOT / "examples").glob("*.json")):
            with self.subTest(path=path.name):
                document = json.loads(path.read_text(encoding="utf-8"))
                result = document["expected_result"]
                self.assertIn(result["decision"], valid_decisions)
                self.assertIs(result["not_executed"], True)
                self.assertGreater(len(result["reasons"]), 0)

    def test_readme_uses_official_clawhub_install_form(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(
            "clawhub install @agentnomos/agentnomos-governance-preflight",
            readme,
        )
        self.assertNotIn("openclaw skills install", readme)

    def test_public_files_do_not_contain_high_confidence_secret_markers(self) -> None:
        forbidden = (
            "-----BEGIN PRIVATE KEY-----",
            "sk_live_",
            "sk-ant-",
            "ghp_",
            "xoxb-",
            "/root/ops/",
        )
        suffixes = {".md", ".json", ".py", ".yml", ".yaml"}
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in suffixes:
                continue
            text = path.read_text(encoding="utf-8")
            for marker in forbidden:
                with self.subTest(path=path.relative_to(ROOT), marker=marker):
                    self.assertNotIn(marker, text)


if __name__ == "__main__":
    unittest.main()
