"""Map the legitimation pilot record onto the house schema (spec section 5).

``build_events`` turns the pilot (data/pilot.json) plus the world field state into one event
record per critic, in the key format of the spec's section 5.3, which uses the names of the
design proposal's algorithm outputs (``lineage``, ``saturation``, ``reception_distribution``,
``displacement``, ``feedback``). Two extensions the spec asks for are carried:

* ``legitimation``: ``authority_claim`` and ``claimed_vs_granted`` (invariant L-1).
* ``timing`` on every ``reception_distribution`` entry.

What is derived and what is copied:

* ``evidence.uncertainty`` is "high" with fewer than two evidence-grade outcomes, "medium" when any
  row is not high confidence or the critic has no immediate row, else "low";
* derived from the pilot: speaker, orientation, position, authority_claim, claimed_vs_granted,
  reception_distribution, evidence;
* derived from the pilot (``basis: "derived"``): ``lineage.mutations`` (one entry per recorded outcome row
  where a later receiver took the scale up and corrected it, outcome ``contested``) and
  ``feedback.world_state_deltas`` (one entry per recorded field change, with the event it follows);
* copied from the spec unchanged (data/spec-event-extras.json, ``basis`` names why): id, text,
  lineage.origin (supported by the research PDF, a secondary source, for De Piles only), saturation and
  displacement. The pilot cannot produce them and they are not independently verified;
* the spec's own lineage mutations and feedback deltas that the pilot does not support are kept apart under
  ``unverified_spec_mutations`` and ``unverified_spec_world_state_deltas``, never mixed into the derived lists.

The spec's own reception_distribution entries are not used: they carry resonance, misreading
and rejection levels that the sourced pilot does not support (for example Mairan as a high
rejection; the primary text shows a correction). Entries here carry only what the pilot coded.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from . import legitimation as L

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

# Ordinal map from the pilot's granted level to a coarse resonance label. Nothing finer is coded.
RESONANCE = {"none": "none", "coterie": "low", "field": "medium", "canon": "high"}
# Rejection is read from the outcome only. "ignored" is neither resonance nor rejection, so it maps to "none"
# here and is told apart by outcome; no pilot row is ignored.
REJECTION = {"granted": "none", "contested": "partial", "ignored": "none", "rejected": "high", "pending": "unknown"}

EVENT_KEYS = ("id", "field_state_ref", "speaker", "text", "orientation", "position", "lineage", "saturation",
              "legitimation", "reception_distribution", "displacement", "feedback", "evidence")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _uncertainty(rows: list[dict[str, Any]]) -> str:
    evidence = [r for r in rows if r["confidence"] in L.EVIDENCE and r["outcome"] != "pending"]
    if len(evidence) < 2:
        return "high"
    if any(r["confidence"] != "high" for r in rows) or not any(r["timing"] == "immediate" for r in rows):
        return "medium"  # a non-primary row, or no first-reception row at all
    return "low"


# Why each copied value stays copied. "not derivable" says what evidence a derivation would need.
SATURATION_BASIS = ("spec, not derivable: occupancy and differentiation compare a critic with other speakers in "
                    "the same slot, and the pilot records three critics in three different slots")
DISPLACEMENT_BASIS = ("spec, not derivable: taste_delta, belief_delta and misfire_risk need a before/after "
                      "measure of taste or belief; the pilot's field changes are channel and instrument changes, "
                      "carried under feedback")
LINEAGE_ORIGIN_BASIS = {
    "de_piles": "spec; the research PDF (docs/research, De Piles paragraph) also gives the 1673 Dialogue sur le "
                "coloris as the source of 'color is the soul of painting' (secondary source, primary not read)",
}
LINEAGE_ORIGIN_DEFAULT = "spec only; no source in the pilot or the research PDF names an origin for this critic's text"


def _mutations(outs: list[dict[str, Any]], receivers: dict[str, str]) -> list[dict[str, Any]]:
    """A later receiver that took the claim up and corrected it changed the text it received (outcome contested)."""
    return [{
        "year": e["year"],
        "type": "corrected",
        "note": f"{receivers[e['receiver']]} takes the claim up and corrects it ({e['timing']}, {e['confidence']})",
        "event_ref": e["id"],
        "basis": "derived",
    } for e in outs if e["outcome"] == "contested"]


def _world_state_deltas(c: dict[str, Any], pilot: dict[str, Any]) -> list[dict[str, Any]]:
    by_id = {e["id"]: e for e in pilot["events"]}
    return [{
        "delta": fc["change"],
        "field_change_ref": fc["id"],
        "because": fc["because"],
        "because_confidence": by_id[fc["because"]]["confidence"],
        "basis": "derived",
    } for fc in pilot["field_changes"] if fc["critic"] == c["id"]]


def build_events(pilot: dict[str, Any], field_state: dict[str, Any], extras: dict[str, Any]) -> list[dict[str, Any]]:
    receivers = {r["id"]: r["name"] for r in pilot["receivers"]}
    claims = {cl["id"]: cl for c in pilot["critics"] for cl in c["claims"]}
    out = []
    for c in pilot["critics"]:
        ex = extras["events"][c["id"]]
        outs = sorted((e for e in pilot["events"] if e["critic"] == c["id"] and e["field"] == "recognition_outcome"),
                      key=lambda e: (e["year"], e["id"]))
        dist = [{
            "community": receivers[e["receiver"]],
            "timing": e["timing"],
            "outcome": e["outcome"],
            "granted_level": e["granted"],
            "resonance": RESONANCE[e["granted"]],
            "misreading": None,
            "rejection": REJECTION[e["outcome"]],
            "event_ref": e["id"],
            "year": e["year"],
            "confidence": e["confidence"],
        } for e in outs]
        cvg = []
        for cl in c["claims"]:
            got = [f"{e['granted']} by {receivers[e['receiver']]} ({e['timing']}, {e['outcome']}, {e['confidence']})"
                   for e in outs if e["claim"] == cl["id"]]
            cvg.append(f"{cl['id']}: claimed {cl['asserted']}; granted " + ("; ".join(got) if got else "nothing recorded"))
        evs = [e for e in pilot["events"] if e["critic"] == c["id"]]
        out.append({
            "id": ex["id"],
            "field_state_ref": field_state["id"],
            "speaker": c["name"],
            "text": ex["text"],
            "orientation": c["orientation"],
            "position": c["position"],
            "lineage": {
                "origin": ex["lineage"]["origin"],
                "origin_basis": LINEAGE_ORIGIN_BASIS.get(c["id"], LINEAGE_ORIGIN_DEFAULT),
                "mutations": _mutations(outs, receivers),
                "mutations_basis": "derived from the pilot's contested outcome rows; none recorded is an empty list",
                "unverified_spec_mutations": ex["lineage"]["mutations"],
            },
            "saturation": {**ex["saturation"], "basis": SATURATION_BASIS},
            "legitimation": {
                "authority_claim": [cl["text"] for cl in c["claims"]],
                "claimed_vs_granted": " | ".join(cvg),
            },
            "reception_distribution": dist,
            "displacement": {**ex["displacement"], "basis": DISPLACEMENT_BASIS},
            "feedback": {
                "world_state_deltas": _world_state_deltas(c, pilot),
                "world_state_deltas_basis": "derived from the pilot's field_changes; none recorded is an empty list",
                "unverified_spec_world_state_deltas": ex["feedback"]["world_state_deltas"],
            },
            "evidence": {
                "events": [e["id"] for e in evs],
                "sources": [e["source"] for e in evs],
                "uncertainty": _uncertainty(dist),
                "spec_only_fields": ["id", "text"],
                "partly_spec_fields": ["lineage.origin", "saturation", "displacement"],
                "derived_fields": ["lineage.mutations", "feedback.world_state_deltas"],
            },
        })
    return out


def validate_event(ev: dict[str, Any], field_state: dict[str, Any]) -> list[str]:
    """House-schema checks plus the spec's invariants (L-1, L-2) and diagnostic RD-1."""
    errs: list[str] = []
    if not isinstance(ev, dict):
        return ["event must be an object"]
    for k in EVENT_KEYS:
        if k not in ev:
            errs.append(f"missing key {k!r}")
    if errs:
        return errs
    if not isinstance(field_state, dict) or ev["field_state_ref"] != field_state.get("id"):
        errs.append("field_state_ref does not name the field state")
    for k in ("speaker", "text", "orientation", "position"):
        if not isinstance(ev[k], str) or not ev[k]:
            errs.append(f"{k} must be a non-empty string")
    lin = ev["lineage"]
    if not isinstance(lin, dict) or not lin.get("origin") or not isinstance(lin.get("mutations"), list):
        errs.append("lineage needs origin and a mutations list")
    sat = ev["saturation"]
    if not isinstance(sat, dict) or not {"occupancy", "differentiation"} <= set(sat):
        errs.append("saturation needs occupancy and differentiation")
    leg = ev["legitimation"]
    if not isinstance(leg, dict) or not isinstance(leg.get("authority_claim"), list) or not leg.get("authority_claim") \
            or not isinstance(leg.get("claimed_vs_granted"), str) or not leg.get("claimed_vs_granted"):
        errs.append("legitimation needs authority_claim (non-empty list) and claimed_vs_granted (L-1)")
    dist = ev["reception_distribution"]
    if not isinstance(dist, list) or len(dist) < 2:
        errs.append("reception_distribution must be a distribution over at least two entries (RD-1)")
    else:
        for i, d in enumerate(dist):
            if not isinstance(d, dict):
                errs.append(f"reception_distribution[{i}] must be an object")
                continue
            for k in ("community", "timing", "outcome", "resonance", "rejection"):
                if k not in d:
                    errs.append(f"reception_distribution[{i}] missing {k!r}")
            if d.get("timing") not in L.TIMINGS:
                errs.append(f"reception_distribution[{i}] timing {d.get('timing')!r} not in {L.TIMINGS}")
            if d.get("outcome") not in L.OUTCOMES:
                errs.append(f"reception_distribution[{i}] outcome {d.get('outcome')!r} not in {L.OUTCOMES}")
        if len({repr(d.get("community")) for d in dist if isinstance(d, dict)}) < 2:
            errs.append("reception_distribution needs at least two distinct communities (RD-1)")
    if not isinstance(ev["feedback"], dict) or not isinstance(ev["feedback"].get("world_state_deltas"), list):
        errs.append("feedback needs world_state_deltas")
    if not isinstance(ev["displacement"], dict):
        errs.append("displacement must be an object")
    evd = ev["evidence"]
    if not isinstance(evd, dict) or not evd.get("sources") or not evd.get("uncertainty"):
        errs.append("evidence needs sources and uncertainty")
    # L-2: recognition is not correctness. Same forbidden-key scan as the pilot, on event and legitimation keys.
    res = L.Result()
    L._forbidden({k: v for k, v in ev.items() if k != "orientation"}, f"event {ev.get('id')}", res)
    if isinstance(leg, dict):
        L._forbidden(leg, f"event {ev.get('id')} legitimation", res)
    errs.extend(res.errors)
    return errs


def main(argv: list[str] | None = None) -> int:
    import sys

    argv = list(sys.argv[1:] if argv is None else argv)
    pilot = load_json(DATA / "pilot.json")
    fs = load_json(DATA / "world-field-state-paris-london-1708-1765.json")
    extras = load_json(DATA / "spec-event-extras.json")
    events = build_events(pilot, fs, extras)
    errs = [f"{e['id']}: {m}" for e in events for m in validate_event(e, fs)]
    text = json.dumps(events, indent=2, ensure_ascii=False) + "\n"
    if "--check" in argv:
        current = (DATA / "field-events.json").read_text(encoding="utf-8")
        if current != text:
            errs.append("data/field-events.json is out of date; regenerate with --write")
    elif "--write" in argv:
        (DATA / "field-events.json").write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    for e in errs:
        print("error:", e, file=sys.stderr)
    return 1 if errs else 0


if __name__ == "__main__":
    raise SystemExit(main())
