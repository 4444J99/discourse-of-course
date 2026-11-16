"""Legitimation pilot: four-field model and its pass/fail test.

The model separates, for each critic, four fields that must never be merged:

* position            where the critic sits in the field
* authority_claim     the grounds the text itself gives for being heard
* granting_receiver   which audience accepts, ignores or rejects the claim
* recognition_outcome what was granted, by whom, when

Rules carried over from the pilot specification (docs/source):

* claimed authority and granted authority are separate values (gap = granted - asserted)
* influence is never evidence of being right (no event may assert correctness)
* a critic's orientation is fixed input; events may not rewrite it

The test (``evaluate``) passes only when the three critics get pairwise
distinct reception signatures, at least one claimed/granted gap is nonzero,
at least one recorded change of the field follows from a critic, and no
structural rule is broken. It fails otherwise, which is the pilot's signal to
revise the four-field model before applying it to other periods.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from itertools import combinations
from pathlib import Path
from typing import Any

FIELDS = ("position", "authority_claim", "granting_receiver", "recognition_outcome")
# "contested": the receiver takes the claim up and corrects it (a grant with reservations).
# Added in v0.3 after the sourced v0.2 record failed the timing rule (see README).
OUTCOMES = ("granted", "contested", "ignored", "rejected", "pending")
TIMINGS = ("immediate", "later", "posthumous")
CONFIDENCE = ("high", "medium", "low")
# Ordinal ladder shared by claims (asserted) and outcomes (granted).
LEVELS = {"none": 0, "coterie": 1, "field": 2, "canon": 3}
# Keys that would smuggle in an orientation rewrite or a correctness verdict.
FORBIDDEN_KEY_PARTS = ("orientation", "correct", "verdict", "true", "valid", "right")
EVIDENCE = ("high", "medium")  # confidence grades that may carry the pass


@dataclass
class Result:
    passed: bool = True
    inconclusive: bool = False
    errors: list[str] = field(default_factory=list)
    findings: list[str] = field(default_factory=list)

    def fail(self, msg: str) -> None:
        self.passed = False
        self.errors.append(msg)

    def thin(self, msg: str) -> None:
        """Evidence too thin to decide: not a PASS, not a model failure."""
        self.inconclusive = True
        self.errors.append(msg)


def _forbidden(obj: dict[str, Any], where: str, res: Result, allow: tuple[str, ...] = ()) -> None:
    for k in obj:
        if k in allow:
            continue
        if any(part in k.lower() for part in FORBIDDEN_KEY_PARTS):
            res.fail(f"{where}: key {k!r} is forbidden (orientation is fixed input at critic level; influence is not correctness)")


def load(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _structural(data: dict[str, Any], res: Result) -> dict[str, dict[str, Any]]:
    critics = {c.get("id"): c for c in data.get("critics", [])}
    if len(critics) != len(data.get("critics", [])):
        res.fail("duplicate or missing critic id")
    receivers = {r.get("id") for r in data.get("receivers", [])}
    claims: dict[str, dict[str, Any]] = {}
    for cid, c in critics.items():
        _forbidden({k: v for k, v in c.items() if k != "claims"}, f"critic {cid}", res, allow=("orientation",))
        if not isinstance(c.get("orientation"), str) or not c["orientation"]:
            res.fail(f"{cid}: orientation must be a fixed non-empty string")
        if not c.get("position"):
            res.fail(f"{cid}: position is required")
        for cl in c.get("claims", []):
            _forbidden(cl, f"claim {cl.get('id')}", res)
            if cl.get("asserted") not in LEVELS:
                res.fail(f"claim {cl.get('id')}: asserted level {cl.get('asserted')!r} not in {sorted(LEVELS)}")
            claims[cl.get("id")] = {**cl, "critic": cid}
    orient = [c.get("orientation") for c in critics.values()]
    if len(set(orient)) != len(orient):
        res.fail("critics share an orientation: the pilot compares critics with different orientations")
    seen: set[Any] = set()
    claim_events: set[Any] = set()
    for ev in data.get("events", []):
        eid = ev.get("id")
        if not eid or eid in seen:
            res.fail(f"{eid!r}: missing or duplicate event id")
        seen.add(eid)
        _forbidden(ev, f"event {eid}", res)
        if ev.get("critic") not in critics:
            res.fail(f"{eid}: unknown critic {ev.get('critic')!r}")
        if ev.get("field") not in FIELDS:
            res.fail(f"{eid}: field {ev.get('field')!r} not one of {FIELDS}")
        if ev.get("confidence") not in CONFIDENCE:
            res.fail(f"{eid}: confidence {ev.get('confidence')!r} not one of {CONFIDENCE}")
        if not ev.get("source"):
            res.fail(f"{eid}: every event needs a source")
        y = ev.get("year")
        if isinstance(y, bool) or not isinstance(y, int) or not 1600 <= y <= 2100:
            res.fail(f"{eid}: year must be an integer in 1600..2100")
        if ev.get("field") == "authority_claim":
            if ev.get("claim") not in claims or claims[ev["claim"]]["critic"] != ev.get("critic"):
                res.fail(f"{eid}: authority_claim must name a claim of the same critic")
            else:
                claim_events.add(ev["critic"])
        if ev.get("field") == "recognition_outcome":
            if ev.get("outcome") not in OUTCOMES:
                res.fail(f"{eid}: outcome {ev.get('outcome')!r} not one of {OUTCOMES}")
            if ev.get("timing") not in TIMINGS:
                res.fail(f"{eid}: timing {ev.get('timing')!r} not one of {TIMINGS}")
            if ev.get("receiver") not in receivers:
                res.fail(f"{eid}: unknown receiver {ev.get('receiver')!r}")
            if ev.get("claim") not in claims:
                res.fail(f"{eid}: unknown claim {ev.get('claim')!r}")
            elif claims[ev["claim"]]["critic"] != ev.get("critic"):
                res.fail(f"{eid}: claim {ev['claim']} belongs to another critic")
            if ev.get("granted") not in LEVELS:
                res.fail(f"{eid}: granted level {ev.get('granted')!r} not in {sorted(LEVELS)}")
            else:
                if ev.get("outcome") in ("granted", "contested") and ev["granted"] == "none":
                    res.fail(f"{eid}: outcome {ev['outcome']} must grant a level above 'none'")
                if ev.get("outcome") in ("ignored", "rejected", "pending") and ev["granted"] != "none":
                    res.fail(f"{eid}: outcome {ev['outcome']} must grant level 'none'")
    for cid in critics:
        if cid not in claim_events:
            res.fail(f"{cid}: no authority_claim event")
    return claims


def signature(data: dict[str, Any], critic_id: str, evidence_only: bool = False) -> tuple[tuple[str, str, str], ...]:
    """Reception signature: ordered (year-sorted) (timing, receiver, outcome) triples."""
    evs = [
        e for e in data["events"]
        if e["critic"] == critic_id and e["field"] == "recognition_outcome"
        and (not evidence_only or (e["confidence"] in EVIDENCE and e["outcome"] != "pending"))
    ]
    evs.sort(key=lambda e: (e["year"], e["id"]))
    return tuple((e["timing"], e["receiver"], e["outcome"]) for e in evs)


def gaps(data: dict[str, Any], evidence_only: bool = False) -> list[dict[str, Any]]:
    claims = {cl["id"]: cl for c in data["critics"] for cl in c.get("claims", [])}
    out = []
    for e in data["events"]:
        if e["field"] != "recognition_outcome" or e.get("claim") not in claims:
            continue
        if evidence_only and e["confidence"] not in EVIDENCE:
            continue
        asserted = LEVELS[claims[e["claim"]]["asserted"]]
        granted = LEVELS[e["granted"]] if e.get("granted") in LEVELS else None
        if granted is None:
            continue
        out.append({"event": e["id"], "critic": e["critic"], "claim": e["claim"],
                    "asserted": asserted, "granted": granted, "gap": granted - asserted,
                    "timing": e.get("timing")})
    return out


def evaluate(data: dict[str, Any]) -> Result:
    try:
        return _evaluate(data)
    except (KeyError, TypeError, AttributeError) as exc:
        res = Result()
        res.fail(f"malformed record: {exc!r}")
        return res


def _evaluate(data: dict[str, Any]) -> Result:
    """FAIL: a rule broke or the critics look alike on the evidence.
    INCONCLUSIVE: rules hold but low-confidence rows are all that separate a critic.
    PASS: the criteria hold on medium/high-confidence events alone."""
    res = Result()
    try:
        _structural(data, res)
    except (KeyError, TypeError, AttributeError) as exc:
        res.fail(f"malformed record: {exc!r}")
    if res.errors:
        return res
    ids = [c["id"] for c in data.get("critics", [])]
    if len(ids) < 3:
        res.fail("pilot needs at least three critics")
        return res
    full = {i: signature(data, i) for i in ids}
    for a, b in combinations(ids, 2):
        if full[a] == full[b]:
            res.fail(f"critics {a} and {b} have identical reception signatures: revise the model")
    for i in ids:
        if not full[i]:
            res.fail(f"{i}: no recognition_outcome events")
    if res.errors:
        return res
    ev_ids = {e["id"]: e for e in data["events"]}
    if not data.get("field_changes"):
        res.fail("no recorded change of the field made by a critic")
    for fc in data.get("field_changes", []):
        src = ev_ids.get(fc.get("because"))
        if fc.get("critic") not in ids or src is None:
            res.fail(f"field change {fc.get('id')}: unknown critic or 'because' event")
        elif src["critic"] != fc["critic"] or src["field"] != "recognition_outcome" or src["outcome"] != "granted":
            res.fail(f"field change {fc['id']}: must follow a granted recognition_outcome of the same critic")
        if not fc.get("change"):
            res.fail(f"field change {fc.get('id')}: change text is required")
        _forbidden(fc, f"field change {fc.get('id')}", res)
    if res.errors:
        return res
    # Evidence-grade pass: same tests on medium/high events only.
    ev_sig = {i: signature(data, i, evidence_only=True) for i in ids}
    for i in ids:
        if len(ev_sig[i]) < 2:
            res.thin(f"{i}: fewer than 2 medium/high-confidence outcomes ({len(ev_sig[i])}); record too thin to decide")
    if res.inconclusive:
        res.findings.append("full-record signatures: " + "; ".join(f"{i}={full[i]}" for i in ids))
        res.passed = False
        return res
    for a, b in combinations(ids, 2):
        if ev_sig[a] == ev_sig[b]:
            res.fail(f"critics {a} and {b} look alike on evidence-grade events")
    nonzero = [x for x in gaps(data, evidence_only=True) if x["gap"] != 0]
    if not nonzero:
        res.fail("no evidence-grade claimed/granted gap: the model has not separated the two values")
    else:
        res.findings.append("gaps: " + ", ".join(f"{x['event']}({x['gap']:+d},{x['timing']})" for x in nonzero))
    split = []
    for i in ids:
        now = {o for t, _, o in ev_sig[i] if t == "immediate"}
        later = {o for t, _, o in ev_sig[i] if t != "immediate"}
        if now and later and now != later:
            split.append(i)
    if split:
        res.findings.append("timing split: " + ", ".join(split))
    else:
        res.fail("no critic shows an immediate/later reception split; timing field adds nothing")
    for i in ids:
        res.findings.append(f"signature {i}: {ev_sig[i]}")
    return res


def main(argv: list[str] | None = None) -> int:
    import sys

    argv = list(sys.argv[1:] if argv is None else argv)
    path = argv[0] if argv else str(Path(__file__).resolve().parents[2] / "data" / "pilot.json")
    res = evaluate(load(path))
    for f in res.findings:
        print("finding:", f)
    for e in res.errors:
        print("error:", e)
    if res.passed:
        print("PASS")
        return 0
    print("INCONCLUSIVE" if res.inconclusive else "FAIL")
    return 2 if res.inconclusive else 1


if __name__ == "__main__":
    raise SystemExit(main())
