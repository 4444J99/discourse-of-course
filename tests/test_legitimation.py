import copy
import unittest
from pathlib import Path

from discourse_of_course import legitimation as L

DATA = L.load(Path(__file__).resolve().parents[1] / "data" / "pilot.json")


def fresh():
    return copy.deepcopy(DATA)


class PilotTest(unittest.TestCase):
    def test_shipped_pilot_passes(self):
        res = L.evaluate(fresh())
        self.assertTrue(res.passed, res.errors)

    def test_signatures_are_pairwise_distinct(self):
        sigs = {c["id"]: L.signature(DATA, c["id"]) for c in DATA["critics"]}
        self.assertEqual(len(set(sigs.values())), 3)

    def test_claimed_and_granted_are_separate_and_gap_exists(self):
        gaps = {g["event"]: g["gap"] for g in L.gaps(DATA)}
        self.assertEqual(gaps["e_dp_now"], -1)  # claimed coterie, ignored
        self.assertEqual(gaps["e_dp_later"], 2)  # claimed coterie, canon later
        self.assertEqual(gaps["e_di_now"], 0)

    def test_identical_critics_fail(self):
        d = fresh()
        for e in d["events"]:
            if e["critic"] == "richardson" and e["field"] == "recognition_outcome":
                e["critic"] = "diderot"
                e["claim"] = "di_salon"
        d["events"] = [e for e in d["events"] if e["critic"] != "richardson"]
        res = L.evaluate(d)
        self.assertFalse(res.passed)

    def test_same_signature_fails(self):
        d = fresh()
        by = {e["id"]: e for e in d["events"]}
        for src, dst in (("e_dp_now", "e_ri_now"), ("e_dp_later", "e_ri_rej")):
            for k in ("timing", "receiver", "outcome", "granted"):
                by[dst][k] = by[src][k]
        res = L.evaluate(d)
        self.assertFalse(res.passed)
        self.assertTrue(any("identical reception" in e for e in res.errors))

    def test_no_gap_fails(self):
        d = fresh()
        for c in d["critics"]:
            for cl in c["claims"]:
                cl["asserted"] = "coterie"
        for e in d["events"]:
            if e["field"] == "recognition_outcome":
                e["outcome"], e["granted"] = "granted", "coterie"
        res = L.evaluate(d)
        self.assertFalse(res.passed)
        self.assertTrue(any("no claimed/granted gap" in x for x in res.errors))

    def test_orientation_rewrite_rejected(self):
        d = fresh()
        d["events"][0]["orientation"] = "new"
        res = L.evaluate(d)
        self.assertFalse(res.passed)
        self.assertTrue(any("forbidden" in e for e in res.errors))

    def test_influence_is_not_correctness(self):
        d = fresh()
        d["events"][2]["correct"] = True
        self.assertFalse(L.evaluate(d).passed)

    def test_every_event_needs_source(self):
        d = fresh()
        d["events"][0]["source"] = ""
        self.assertFalse(L.evaluate(d).passed)

    def test_ignored_cannot_grant(self):
        d = fresh()
        for e in d["events"]:
            if e["id"] == "e_dp_now":
                e["granted"] = "field"
        self.assertFalse(L.evaluate(d).passed)

    def test_claim_must_belong_to_critic(self):
        d = fresh()
        for e in d["events"]:
            if e["id"] == "e_ri_now":
                e["claim"] = "dp_scales"
        self.assertFalse(L.evaluate(d).passed)

    def test_field_change_needs_real_event(self):
        d = fresh()
        d["field_changes"][0]["because"] = "nope"
        self.assertFalse(L.evaluate(d).passed)
        d["field_changes"] = []
        self.assertFalse(L.evaluate(d).passed)

    def test_cli_exit_code(self):
        self.assertEqual(L.main([]), 0)


if __name__ == "__main__":
    unittest.main()
