import copy
import json
import unittest
from pathlib import Path

from discourse_of_course import house_schema as H
from discourse_of_course import legitimation as L
from discourse_of_course import world as W

ROOT = Path(__file__).resolve().parents[1]
PILOT = H.load_json(ROOT / "data" / "pilot.json")
FS = W.load(ROOT / "data" / "world-field-state-paris-london-1708-1765.json")
EXTRAS = H.load_json(ROOT / "data" / "spec-event-extras.json")
EVENTS = H.build_events(PILOT, FS, EXTRAS)


def one(i=0):
    return copy.deepcopy(EVENTS[i])


class MappingTest(unittest.TestCase):
    def test_every_event_is_valid(self):
        for e in EVENTS:
            self.assertEqual(H.validate_event(e, FS), [], e["id"])

    def test_shipped_file_matches_the_generator(self):
        self.assertEqual(json.loads((ROOT / "data" / "field-events.json").read_text(encoding="utf-8")), EVENTS)
        self.assertEqual(H.main(["--check"]), 0)

    def test_orientation_and_position_are_carried_unchanged(self):
        for c in PILOT["critics"]:
            e = next(x for x in EVENTS if x["speaker"] == c["name"])
            self.assertEqual(e["orientation"], c["orientation"])
            self.assertEqual(e["position"], c["position"])

    def test_every_pilot_outcome_row_appears_once_with_timing(self):
        rows = [r["event_ref"] for e in EVENTS for r in e["reception_distribution"]]
        want = [e["id"] for e in PILOT["events"] if e["field"] == "recognition_outcome"]
        self.assertEqual(sorted(rows), sorted(want))
        for e in EVENTS:
            for r in e["reception_distribution"]:
                self.assertIn(r["timing"], L.TIMINGS)

    def test_claimed_vs_granted_keeps_both_values(self):
        for e in EVENTS:
            text = e["legitimation"]["claimed_vs_granted"]
            self.assertIn("claimed", text)
            self.assertIn("granted", text)
        dp = EVENTS[0]["legitimation"]["claimed_vs_granted"]
        self.assertIn("dp_scales: claimed coterie", dp)
        self.assertIn("contested", dp)

    def test_spec_only_fields_equal_the_spec(self):
        spec = (ROOT / "docs" / "perplexity" / "legitimation-pilot-spec.md").read_text(encoding="utf-8")
        i = spec.index("### 5.3")
        j = spec.index("```json", i) + 7
        spec_events = {e["id"]: e for e in json.loads(spec[j:spec.index("```", j)])}
        for e in EVENTS:
            s = spec_events[e["id"]]
            for k in e["evidence"]["spec_only_fields"]:
                self.assertEqual(e[k], s[k], (e["id"], k))
            self.assertIn(e["speaker"], s["speaker"])

    def test_derived_fields_come_from_the_pilot_and_copied_ones_say_why(self):
        outcomes = {e["id"]: e for e in PILOT["events"]}
        dp = EVENTS[0]
        self.assertEqual([m["event_ref"] for m in dp["lineage"]["mutations"]], ["e_dp_richardson", "e_dp_mairan"])
        for m in dp["lineage"]["mutations"]:
            self.assertEqual(outcomes[m["event_ref"]]["outcome"], "contested")
            self.assertEqual(m["year"], outcomes[m["event_ref"]]["year"])
        # No contested row, no mutation: nothing is invented for the other critics.
        self.assertEqual(EVENTS[1]["lineage"]["mutations"], [])
        self.assertEqual(EVENTS[2]["lineage"]["mutations"], [])
        fcs = {fc["critic"]: fc for fc in PILOT["field_changes"]}
        for e, cid in zip(EVENTS, ("de_piles", "richardson", "diderot")):
            deltas = e["feedback"]["world_state_deltas"]
            if cid in fcs:
                self.assertEqual([d["field_change_ref"] for d in deltas], [fcs[cid]["id"]])
                self.assertEqual(deltas[0]["because_confidence"], outcomes[fcs[cid]["because"]]["confidence"])
            else:
                self.assertEqual(deltas, [])  # Richardson has no recorded field change
            self.assertTrue(e["saturation"]["basis"].startswith("spec, not derivable"))
            self.assertTrue(e["displacement"]["basis"].startswith("spec, not derivable"))
            self.assertTrue(e["lineage"]["unverified_spec_mutations"])
            self.assertTrue(e["feedback"]["unverified_spec_world_state_deltas"])

    def test_the_spec_rejection_of_mairan_is_not_carried(self):
        # The spec codes Mairan 1755 as high rejection; the primary text read for the pilot shows a correction.
        r = next(r for r in EVENTS[0]["reception_distribution"] if r["event_ref"] == "e_dp_mairan")
        self.assertEqual((r["outcome"], r["rejection"]), ("contested", "partial"))

    def test_missing_and_malformed_parts_are_reported(self):
        for k in H.EVENT_KEYS:
            e = one()
            del e[k]
            self.assertTrue(H.validate_event(e, FS), k)
        e = one()
        e["field_state_ref"] = "elsewhere"
        self.assertTrue(H.validate_event(e, FS))
        e = one()
        e["legitimation"]["claimed_vs_granted"] = ""
        self.assertTrue(any("L-1" in m for m in H.validate_event(e, FS)))
        e = one()
        e["reception_distribution"] = e["reception_distribution"][:1]
        self.assertTrue(any("RD-1" in m for m in H.validate_event(e, FS)))
        e = one()
        for r in e["reception_distribution"]:
            r["community"] = "same"
        self.assertTrue(any("RD-1" in m for m in H.validate_event(e, FS)))
        e = one()
        e["reception_distribution"][0]["timing"] = "later"
        self.assertTrue(any("timing" in m for m in H.validate_event(e, FS)))
        self.assertTrue(H.validate_event([], FS))
        e = one()
        e["reception_distribution"][0]["community"] = ["a"]
        e["reception_distribution"][1]["community"] = {"b": 1}
        H.validate_event(e, FS)  # must not raise
        self.assertTrue(H.validate_event(one(), []))
        e = one()
        e["reception_distribution"] = [5, 6]
        self.assertTrue(H.validate_event(e, FS))

    def test_recognition_is_not_correctness(self):
        e = one()
        e["verdict"] = "right"
        self.assertTrue(any("forbidden" in m for m in H.validate_event(e, FS)))
        e = one()
        e["legitimation"]["is_correct"] = True
        self.assertTrue(any("forbidden" in m for m in H.validate_event(e, FS)))

    def test_uncertainty_rule(self):
        rows = [{"confidence": "high", "outcome": "granted", "timing": "immediate"}] * 2
        self.assertEqual(H._uncertainty(rows), "low")
        self.assertEqual(H._uncertainty(rows[:1]), "high")
        self.assertEqual(H._uncertainty([{"confidence": "high", "outcome": "granted", "timing": "delayed"}] * 2), "medium")
        self.assertEqual(H._uncertainty([{"confidence": "medium", "outcome": "granted", "timing": "immediate"}] * 2), "medium")


if __name__ == "__main__":
    unittest.main()
