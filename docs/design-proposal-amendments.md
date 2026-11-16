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

Both are implemented in `src/discourse_of_course/house_schema.py` once the event mapping lands; they are not yet folded into the proposal itself.
