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
OUTCOMES = ("granted", "ignored", "rejected", "pending")
TIMINGS = ("immediate", "later", "posthumous")
CONFIDENCE = ("high", "medium", "low")
# Ordinal ladder shared by claims (asserted) and outcomes (granted).
LEVELS = {"none": 0, "coterie": 1, "field": 2, "canon": 3}
# Keys that would smuggle in an orientation rewrite or a correctness verdict.
FORBIDDEN_EVENT_KEYS = ("orientation", "correct", "is_correct", "true", "valid")


@dataclass
class Result:
    passed: bool = True
    errors: list[str] = field(default_factory=list)
    findings: list[str] = field(default_factory=list)

    def fail(self, msg: str) -> None:
        self.passed = False
        self.errors.append(msg)


def load(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _structural(data: dict[str, Any], res: Result) -> dict[str, dict[str, Any]]:
    critics = {c["id"]: c for c in data.get("critics", [])}
    if len(critics) != len(data.get("critics", [])):
        res.fail("duplicate critic id")
    receivers = {r["id"] for r in data.get("receivers", [])}
    claims: dict[str, dict[str, Any]] = {}
    for c in critics.values():
        if not isinstance(c.get("orientation"), str) or not c["orientation"]:
            res.fail(f"{c['id']}: orientation must be a fixed non-empty string")
        for cl in c.get("claims", []):
            if cl["asserted"] not in LEVELS:
                res.fail(f"claim {cl['id']}: asserted level {cl['asserted']!r} not in {sorted(LEVELS)}")
            claims[cl["id"]] = {**cl, "critic": c["id"]}
    seen: set[str] = set()
    for ev in data.get("events", []):
        eid = ev.get("id", "?")
        if eid in seen:
            res.fail(f"{eid}: duplicate event id")
        seen.add(eid)
        if ev.get("critic") not in critics:
            res.fail(f"{eid}: unknown critic {ev.get('critic')!r}")
        if ev.get("field") not in FIELDS:
            res.fail(f"{eid}: field {ev.get('field')!r} not one of {FIELDS}")
        if ev.get("confidence") not in CONFIDENCE:
            res.fail(f"{eid}: confidence {ev.get('confidence')!r} not one of {CONFIDENCE}")
        if not ev.get("source"):
            res.fail(f"{eid}: every event needs a source")
        if not isinstance(ev.get("year"), int):
            res.fail(f"{eid}: year must be an integer")
        for k in FORBIDDEN_EVENT_KEYS:
            if k in ev:
                res.fail(f"{eid}: key {k!r} is forbidden (orientation is fixed input; influence is not correctness)")
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
            elif ev.get("outcome") in ("ignored", "rejected") and ev["granted"] != "none":
                res.fail(f"{eid}: outcome {ev['outcome']} must grant level 'none'")
    return claims


def signature(data: dict[str, Any], critic_id: str) -> tuple[tuple[str, str, str], ...]:
    """Reception signature: ordered (year-sorted) (timing, receiver, outcome) triples."""
    evs = [
        e for e in data["events"]
        if e["critic"] == critic_id and e["field"] == "recognition_outcome"
    ]
    evs.sort(key=lambda e: (e["year"], e["id"]))
    return tuple((e["timing"], e["receiver"], e["outcome"]) for e in evs)


def gaps(data: dict[str, Any]) -> list[dict[str, Any]]:
    claims = {cl["id"]: cl for c in data["critics"] for cl in c.get("claims", [])}
    out = []
    for e in data["events"]:
        if e["field"] != "recognition_outcome" or e.get("claim") not in claims:
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
    res = Result()
    _structural(data, res)
    if not res.errors:
        ids = [c["id"] for c in data["critics"]]
        if len(ids) < 3:
            res.fail("pilot needs at least three critics")
        sigs = {i: signature(data, i) for i in ids}
        for a, b in combinations(ids, 2):
            if sigs[a] == sigs[b]:
                res.fail(f"critics {a} and {b} have identical reception signatures: revise the model")
        for i in ids:
            if not sigs[i]:
                res.fail(f"{i}: no recognition_outcome events")
        g = gaps(data)
        nonzero = [x for x in g if x["gap"] != 0]
        if not nonzero:
            res.fail("no claimed/granted gap anywhere: the model has not separated the two values")
        else:
            res.findings.append(
                "gaps: " + ", ".join(f"{x['event']}({x['gap']:+d},{x['timing']})" for x in nonzero))
        if not data.get("field_changes"):
            res.fail("no recorded change of the field made by a critic")
        else:
            ev_ids = {e["id"] for e in data["events"]}
            for fc in data["field_changes"]:
                if fc.get("critic") not in ids:
                    res.fail(f"field change {fc.get('id')}: unknown critic")
                if fc.get("because") not in ev_ids:
                    res.fail(f"field change {fc.get('id')}: 'because' must name an event id")
        # timing split: at least one critic shows a different outcome immediate vs later/posthumous
        split = []
        for i in ids:
            now = {o for t, _, o in sigs[i] if t == "immediate"}
            later = {o for t, _, o in sigs[i] if t != "immediate"}
            if now and later and now != later:
                split.append(i)
        if split:
            res.findings.append("timing split (immediate differs from later/posthumous): " + ", ".join(split))
        else:
            res.fail("no critic shows an immediate/later reception split; timing field adds nothing")
        for i in ids:
            res.findings.append(f"signature {i}: {sigs[i]}")
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
    print("PASS" if res.passed else "FAIL")
    return 0 if res.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
