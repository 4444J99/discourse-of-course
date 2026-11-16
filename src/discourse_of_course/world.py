"""World field state in the house format, with the W4 split.

The design proposal (docs/perplexity/world-and-receiver-organ-designs.md, section 2.3) gives the
house JSON format for the world component. The legitimation pilot spec (section 3 and 5.2) asks
that axiom W4 ("discourse systems overlap rather than replace; the field is additive") be split
into two axioms before any period is encoded:

* W4a  channels are additive: new distribution channels join old ones.
* W4b  consecrating authority migrates: a new consecrator displaces the prior one.

``validate_field_state`` checks the house format and the split. ``channels_additive`` and
``consecrator_migrates`` are the two splits as checks between an earlier and a later field state.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

HOUSE_TOP = ("id", "component", "axioms", "field_state", "core_algorithms", "diagnostic_questions")
FIELD_STATE_KEYS = ("period", "authority_map", "channels", "visibility_regime", "sayable_set")
AUTHORITY_KEYS = ("who_can_speak", "whose_judgments_count", "gatekeepers")


def load(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_field_state(d: dict[str, Any]) -> list[str]:
    errs: list[str] = []
    if not isinstance(d, dict):
        return ["field state must be an object"]
    for k in HOUSE_TOP:
        if k not in d:
            errs.append(f"missing house key {k!r}")
    if errs:
        return errs
    if d["component"] != "world":
        errs.append("component must be 'world'")
    if not str(d["id"]).startswith("world-field-state-"):
        errs.append("id must start with 'world-field-state-'")
    axioms = d["axioms"]
    if not isinstance(axioms, list) or not all(
        isinstance(a, dict) and a.get("id") and isinstance(a.get("statement"), str) and a["statement"] for a in axioms
    ):
        errs.append("axioms must be a list of {id, statement}")
        return errs
    ids = [a["id"] for a in axioms]
    if len(set(ids)) != len(ids):
        errs.append("duplicate axiom id")
    if "W4" in ids:
        errs.append("axiom W4 must be split into W4a and W4b")
    by = {a["id"]: a["statement"].lower() for a in axioms}
    for need, words in (("W4a", ("additive",)), ("W4b", ("displace",))):
        if need not in by:
            errs.append(f"missing axiom {need}")
        elif not all(w in by[need] for w in words):
            errs.append(f"axiom {need} must say {words[0]!r}")
    fs = d["field_state"]
    if not isinstance(fs, dict):
        errs.append("field_state must be an object")
        return errs
    for k in FIELD_STATE_KEYS:
        if k not in fs:
            errs.append(f"field_state missing {k!r}")
    am = fs.get("authority_map")
    if isinstance(am, dict):
        for k in AUTHORITY_KEYS:
            if not isinstance(am.get(k), list) or not am.get(k):
                errs.append(f"authority_map.{k} must be a non-empty list")
    elif "authority_map" in fs:
        errs.append("authority_map must be an object")
    if not isinstance(fs.get("channels"), list) or not fs.get("channels"):
        errs.append("channels must be a non-empty list")
    if not isinstance(d["core_algorithms"], list):
        errs.append("core_algorithms must be a list")
    dq = d["diagnostic_questions"]
    if not isinstance(dq, list) or not all(isinstance(q, dict) and {"id", "question", "valid_if"} <= set(q) for q in dq):
        errs.append("diagnostic_questions must be a list of {id, question, valid_if}")
    return errs


def channels_additive(earlier: dict[str, Any], later: dict[str, Any]) -> list[str]:
    """W4a: every channel of the earlier state is still present in the later one."""
    try:
        gone = [c for c in earlier["field_state"]["channels"] if c not in later["field_state"]["channels"]]
    except (KeyError, TypeError):
        return ["malformed field state: channels missing"]
    return [f"channel {c!r} disappeared; W4a says channels are additive" for c in gone]


def consecrator_migrates(earlier: dict[str, Any], later: dict[str, Any]) -> list[str]:
    """W4b: if the later state adds a consecrator (whose_judgments_count), at least one earlier
    consecrator must be gone, because a new consecrator displaces the prior one."""
    try:
        a = set(earlier["field_state"]["authority_map"]["whose_judgments_count"])
        b = set(later["field_state"]["authority_map"]["whose_judgments_count"])
    except (KeyError, TypeError):
        return ["malformed field state: whose_judgments_count missing"]
    if b - a and a <= b:
        return ["a consecrator was added and none was displaced; W4b says consecrating authority migrates"]
    return []
