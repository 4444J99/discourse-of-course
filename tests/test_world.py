import copy
import unittest
from pathlib import Path

from discourse_of_course import world as W

ROOT = Path(__file__).resolve().parents[1]
DATA = W.load(ROOT / "data" / "world-field-state-paris-london-1708-1765.json")


def fresh():
    return copy.deepcopy(DATA)


class WorldTest(unittest.TestCase):
    def test_shipped_field_state_is_valid_house_format(self):
        self.assertEqual(W.validate_field_state(fresh()), [])

    def test_w4_is_split_not_plain(self):
        ids = [a["id"] for a in DATA["axioms"]]
        self.assertIn("W4a", ids)
        self.assertIn("W4b", ids)
        self.assertNotIn("W4", ids)
        d = fresh()
        d["axioms"].append({"id": "W4", "statement": "Discourse systems overlap rather than replace."})
        self.assertTrue(any("must be split" in e for e in W.validate_field_state(d)))

    def test_each_half_must_be_present_and_say_its_content(self):
        for drop in ("W4a", "W4b"):
            d = fresh()
            d["axioms"] = [a for a in d["axioms"] if a["id"] != drop]
            self.assertTrue(any(drop in e for e in W.validate_field_state(d)), drop)
        d = fresh()
        next(a for a in d["axioms"] if a["id"] == "W4b")["statement"] = "Authority is stable."
        self.assertTrue(any("W4b" in e for e in W.validate_field_state(d)))

    def test_house_keys_required(self):
        for k in W.HOUSE_TOP:
            d = fresh()
            del d[k]
            self.assertTrue(W.validate_field_state(d), k)
        for k in W.FIELD_STATE_KEYS:
            d = fresh()
            del d["field_state"][k]
            self.assertTrue(W.validate_field_state(d), k)
        d = fresh()
        d["component"] = "receiver"
        self.assertTrue(W.validate_field_state(d))
        d = fresh()
        d["field_state"]["authority_map"]["gatekeepers"] = []
        self.assertTrue(W.validate_field_state(d))
        self.assertTrue(W.validate_field_state([]))

    def test_w4a_channels_additive(self):
        later = fresh()
        later["field_state"]["channels"] = later["field_state"]["channels"] + ["platform feeds"]
        self.assertEqual(W.channels_additive(DATA, later), [])
        later["field_state"]["channels"].remove("academies")
        self.assertEqual(len(W.channels_additive(DATA, later)), 1)

    def test_w4b_consecrator_migrates(self):
        later = fresh()
        later["field_state"]["authority_map"]["whose_judgments_count"].append("critics' press")
        self.assertEqual(len(W.consecrator_migrates(DATA, later)), 1)  # added, none displaced
        later["field_state"]["authority_map"]["whose_judgments_count"].remove("the court's taste")
        self.assertEqual(W.consecrator_migrates(DATA, later), [])  # one displaced
        same = fresh()
        self.assertEqual(W.consecrator_migrates(DATA, same), [])  # nothing added

    def test_malformed_input_reports_instead_of_crashing(self):
        d = fresh()
        d["axioms"][0]["statement"] = 5
        self.assertTrue(W.validate_field_state(d))
        self.assertTrue(W.channels_additive({}, DATA))
        self.assertTrue(W.consecrator_migrates(DATA, {"field_state": {}}))

    def test_field_state_is_transcribed_from_the_spec(self):
        spec = (ROOT / "docs" / "perplexity" / "legitimation-pilot-spec.md").read_text(encoding="utf-8")
        for s in DATA["field_state"]["channels"] + DATA["field_state"]["authority_map"]["gatekeepers"]:
            self.assertIn(s, spec)


if __name__ == "__main__":
    unittest.main()
