import copy
import unittest
from pathlib import Path

from discourse_of_course import legitimation as L

DATA = L.load(Path(__file__).resolve().parents[1] / "data" / "pilot.json")


def fresh():
    return copy.deepcopy(DATA)


def passing():
    """The shipped v0.3 record (it passes on its own)."""
    return fresh()


def v02_coding():
    """The v0.2 coding: the two corrected receptions recorded as plain grants."""
    d = fresh()
    for eid in ("e_dp_richardson", "e_dp_mairan"):
        ev(d, eid)["outcome"] = "granted"
    return d


sourced = passing  # older test name


def ev(d, eid):
    return next(e for e in d["events"] if e["id"] == eid)


class PilotTest(unittest.TestCase):
    def test_shipped_pilot_passes_on_v03(self):
        res = L.evaluate(fresh())
        self.assertTrue(res.passed, res.errors)
        self.assertIn("timing split: de_piles", res.findings)
        self.assertEqual(L.main([]), 0)

    def test_v02_coding_failed_the_timing_rule(self):
        res = L.evaluate(v02_coding())
        self.assertFalse(res.passed)
        self.assertFalse(res.inconclusive)
        self.assertEqual(res.errors, ["no critic shows an immediate/delayed reception split; timing field adds nothing"])

    def test_contested_must_grant_a_level(self):
        d = fresh()
        ev(d, "e_dp_mairan").update(outcome="contested", granted="none")
        self.assertFalse(L.evaluate(d).passed)

    def test_contested_rows_quote_a_reservation(self):
        for e in DATA["events"]:
            if e.get("outcome") == "contested":
                self.assertRegex(e["source"], r"(?i)not a just idea|n'en est pas de m[eê]me", e["id"])

    def test_contested_is_not_a_pending_placeholder(self):
        # contested counts as a reception on the evidence-grade pass
        sig = L.signature(DATA, "de_piles", evidence_only=True)
        self.assertEqual(sum(1 for _, _, o in sig if o == "contested"), 2)

    def test_every_high_confidence_source_cites_a_place_in_a_text(self):
        for e in DATA["events"]:
            if e["confidence"] == "high":
                self.assertRegex(e["source"], r"\bpp?\. \d|title page|archive\.org|doi", e["id"])

    def test_every_critic_has_two_evidence_grade_outcomes(self):
        for c in DATA["critics"]:
            self.assertGreaterEqual(len(L.signature(DATA, c["id"], evidence_only=True)), 2, c["id"])

    def test_low_confidence_cannot_carry_the_pass(self):
        d = sourced()
        for e in d["events"]:
            if e["critic"] == "richardson":
                e["confidence"] = "low"
        res = L.evaluate(d)
        self.assertFalse(res.passed)
        self.assertTrue(res.inconclusive)

    def test_claimed_and_granted_gap_values(self):
        gaps = {g["event"]: g["gap"] for g in L.gaps(DATA)}
        self.assertEqual(gaps["e_dp_acad_1699"], 0)  # claimed field, field granted
        self.assertEqual(gaps["e_dp_later"], 1)  # claimed coterie, field later
        self.assertEqual(gaps["e_ri_fr1728"], -1)  # claimed field, coterie granted
        self.assertEqual(gaps["e_di_now"], 0)

    def test_identical_signature_fails(self):
        d = sourced()
        d["events"] = [e for e in d["events"] if e["id"] != "e_di_canon"]
        for src, dst in (("e_di_now", "e_ri_fr1728"), ("e_di_pub", "e_ri_northcote")):
            for k in ("timing", "receiver", "outcome", "granted"):
                ev(d, dst)[k] = ev(d, src)[k]
        res = L.evaluate(d)
        self.assertFalse(res.passed)
        self.assertTrue(any("identical reception" in e for e in res.errors))

    def test_no_gap_fails(self):
        d = sourced()
        for c in d["critics"]:
            for cl in c["claims"]:
                cl["asserted"] = "coterie"
        for e in d["events"]:
            if e["field"] == "recognition_outcome":
                e["outcome"], e["granted"] = "granted", "coterie"
        res = L.evaluate(d)
        self.assertFalse(res.passed)
        self.assertTrue(any("no evidence-grade claimed/granted gap" in x for x in res.errors))

    def test_forbidden_keys_everywhere(self):
        for where in ("event", "claim", "field_change", "critic"):
            d = sourced()
            target = {"event": d["events"][0], "claim": d["critics"][0]["claims"][0],
                      "field_change": d["field_changes"][0], "critic": d["critics"][1]}[where]
            target["verdict"] = "right"
            res = L.evaluate(d)
            self.assertFalse(res.passed, where)
            self.assertTrue(any("forbidden" in e for e in res.errors), where)

    def test_orientation_rewrite_on_event_rejected(self):
        d = sourced()
        d["events"][0]["orientation"] = "new"
        self.assertFalse(L.evaluate(d).passed)

    def test_shared_orientation_fails(self):
        d = sourced()
        for c in d["critics"]:
            c["orientation"] = "same"
        res = L.evaluate(d)
        self.assertFalse(res.passed)
        self.assertTrue(any("share an orientation" in e for e in res.errors))

    def test_outcome_and_level_must_agree(self):
        for outcome, level in (("granted", "none"), ("pending", "canon"), ("ignored", "field")):
            d = sourced()
            e = ev(d, "e_dp_acad_1699")
            e["outcome"], e["granted"] = outcome, level
            self.assertFalse(L.evaluate(d).passed, (outcome, level))

    def test_every_event_needs_source_and_valid_year(self):
        d = sourced()
        d["events"][0]["source"] = ""
        self.assertFalse(L.evaluate(d).passed)
        for bad in (True, 1, 3000, "1708"):
            d = sourced()
            d["events"][0]["year"] = bad
            self.assertFalse(L.evaluate(d).passed, bad)

    def test_claim_must_belong_to_critic(self):
        d = sourced()
        ev(d, "e_ri_fr1728")["claim"] = "dp_scales"
        self.assertFalse(L.evaluate(d).passed)

    def test_authority_claim_event_required_and_checked(self):
        d = sourced()
        d["events"] = [e for e in d["events"] if e["id"] != "e_di_claim"]
        self.assertFalse(L.evaluate(d).passed)
        d = sourced()
        ev(d, "e_dp_claim")["claim"] = "zzz"
        self.assertFalse(L.evaluate(d).passed)

    def test_field_change_must_follow_granted_outcome_of_same_critic(self):
        d = sourced()
        d["field_changes"][0]["because"] = "e_di_pub"
        self.assertFalse(L.evaluate(d).passed)
        d = sourced()
        d["field_changes"][0]["because"] = "e_dp_claim"
        self.assertFalse(L.evaluate(d).passed)
        d = sourced()
        d["field_changes"][0]["change"] = ""
        self.assertFalse(L.evaluate(d).passed)
        d = sourced()
        d["field_changes"] = []
        self.assertFalse(L.evaluate(d).passed)

    def test_malformed_records_fail_without_crashing(self):
        d = sourced()
        del d["critics"][0]["claims"][0]["asserted"]
        self.assertFalse(L.evaluate(d).passed)
        d = sourced()
        del d["events"][0]["id"]
        self.assertFalse(L.evaluate(d).passed)
        self.assertFalse(L.evaluate({}).passed)
        d = sourced()
        d["field_changes"] = ["x"]
        self.assertFalse(L.evaluate(d).passed)

    def test_pending_is_not_a_reception(self):
        d = sourced()
        res = L.evaluate(d)
        self.assertTrue(res.passed, res.errors)
        d = sourced()
        ev(d, "e_di_pub").update(outcome="pending", granted="none")
        self.assertFalse(L.evaluate(d).passed)

    def test_imported_perplexity_files_match_their_recorded_hashes(self):
        import hashlib, re
        d = Path(__file__).resolve().parents[1] / "docs" / "perplexity"
        prov = (d / "PROVENANCE.md").read_text(encoding="utf-8")
        for name in ("legitimation-pilot-spec.md", "minotaur-poem-critic-panel.md"):
            digest = hashlib.sha256((d / name).read_bytes()).hexdigest()
            self.assertIn(digest, prov, name)

    def test_timing_vocabulary_matches_the_spec(self):
        self.assertEqual(L.TIMINGS, ("immediate", "delayed", "posthumous"))
        spec = (Path(__file__).resolve().parents[1] / "docs" / "perplexity" / "legitimation-pilot-spec.md").read_text(encoding="utf-8")
        self.assertIn("immediate / delayed / posthumous", spec)


if __name__ == "__main__":
    unittest.main()
