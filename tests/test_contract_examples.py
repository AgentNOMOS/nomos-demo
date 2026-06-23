import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"


class PublicContractExamplesTest(unittest.TestCase):
    def load(self, filename: str) -> dict:
        with (EXAMPLES / filename).open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def assert_common_invariants(self, result: dict) -> None:
        self.assertEqual(result["system"], "AgentNOMOS Governance Preflight")
        self.assertIn(result["decision"], {"ADVISORY_ALLOW", "HOLD_FOR_REVIEW", "BLOCK"})
        self.assertIs(result["not_executed"], True)
        self.assertIsInstance(result["reasons"], list)
        self.assertGreater(len(result["reasons"]), 0)

    def test_payment_requires_review(self) -> None:
        result = self.load("payment-hold.json")["expected_result"]
        self.assert_common_invariants(result)
        self.assertEqual(result["decision"], "HOLD_FOR_REVIEW")
        self.assertIs(result["human_review_required"], True)
        self.assertNotEqual(result["authority_status"], "verified")

    def test_secret_exposure_blocks(self) -> None:
        result = self.load("secret-block.json")["expected_result"]
        self.assert_common_invariants(result)
        self.assertEqual(result["decision"], "BLOCK")
        self.assertIs(result["secret_exposure_detected"], True)

    def test_bounded_read_only_action_can_be_advisory_allow(self) -> None:
        result = self.load("read-only-allow.json")["expected_result"]
        self.assert_common_invariants(result)
        self.assertEqual(result["decision"], "ADVISORY_ALLOW")
        self.assertEqual(result["authority_status"], "verified")
        self.assertEqual(result["risk_level"], "low")
        self.assertIs(result["human_review_required"], False)
        self.assertIs(result["secret_exposure_detected"], False)


if __name__ == "__main__":
    unittest.main()
