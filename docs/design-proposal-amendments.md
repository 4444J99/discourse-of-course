# Amendments to the design proposal that the legitimation pilot needs

The design proposal is `docs/perplexity/world-and-receiver-organ-designs.md`, kept verbatim. The legitimation pilot spec (`docs/perplexity/legitimation-pilot-spec.md`, sections 3 and 5) asks for the changes below. They live here, not in the verbatim copy.

## W4 split (spec section 3, "required before encoding")

The proposal's W4 reads: "Discourse systems overlap rather than replace: salons persist inside platform feeds; the field is additive." It becomes two axioms:

- **W4a** Channels are additive: new distribution channels join old ones.
- **W4b** Consecrating authority migrates: a new consecrator displaces the prior one rather than joining it.

Why: the spec requires the split before encoding and cites `literature-synthesis-matrix-v2.md` section 6.5 for it. That matrix is not in the project files fetched, so the rationale is second-hand. `src/discourse_of_course/world.py` holds the two halves as checks (`channels_additive`, `consecrator_migrates`) and refuses a field state that still carries a plain `W4`.

The field state `data/world-field-state-paris-london-1708-1765.json` carries W1, W4a and W4b only, as the spec's section 5.2 does; it does not restate W0, W2, W3 or W5.

## Schema extensions (spec section 5, "Two schema findings")

1. A `legitimation` block on event records: `authority_claim` and `claimed_vs_granted` (the proposal's `authority_map` describes the field, not a speaker's claim).
2. A `timing` key on `reception_distribution` entries (`immediate`, `delayed`, `posthumous`), so a critic's immediate and posthumous receptions do not collapse into one profile (diagnostic RD-1 forbids a single verdict).

Both are implemented in `src/discourse_of_course/house_schema.py` and `data/field-events.json` (generated; `python -m discourse_of_course.house_schema --check` fails if the file drifts from `data/pilot.json`). Neither is folded into the proposal itself.

## What the event mapping derives and what it copies

Derived from the sourced pilot: speaker, orientation (carried unchanged), position, `legitimation`, `reception_distribution` (one entry per pilot outcome row, with `timing`, outcome, granted level, a coarse `resonance`/`rejection` read only from level and outcome, `misreading` left null), `evidence`, and, since PR 9:

- `lineage.mutations`: one entry per outcome row coded `contested` (a later receiver took the claim up and corrected it), with the row id. De Piles gets two (Richardson 1715, Mairan 1755); Richardson and Diderot get none, because the pilot records no such row for them.
- `feedback.world_state_deltas`: one entry per recorded field change, with the event it follows and that event's confidence. De Piles and Diderot get one each; Richardson gets none (no field change recorded).

Still copied unchanged from the spec section 5.3 because the pilot cannot produce them (`data/spec-event-extras.json`): `id`, `text`, `lineage.origin`, `saturation` and `displacement`. Each carries a `basis` string saying why: saturation compares a critic with other speakers in the same slot (the pilot has three critics in three slots), and displacement needs a before/after measure of taste or belief (the pilot's field changes are channel and instrument changes). `lineage.origin` for De Piles (Dialogue sur le coloris, 1673) is also given by the research PDF, a secondary source. The spec's own mutations and deltas the pilot does not support (for example Ruskin inverting Richardson, Proust domesticating Diderot) are kept under `unverified_spec_mutations` and `unverified_spec_world_state_deltas`, never merged into the derived lists. `evidence.derived_fields`, `evidence.partly_spec_fields` and `evidence.spec_only_fields` list which is which.

Not carried: the spec's own `reception_distribution` entries (they include Mairan as a high rejection, Schlosser and Ruskin rows, and high/low levels the sourced record does not support).
