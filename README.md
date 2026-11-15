# discourse-of-course

A first-principles framework for discourse about art: a critic's **orientation** is kept apart from the **form** and **task** of what they write. Begun by the owner in the Perplexity project `discourse-of-course` (2026-11-07); this repository is its first home outside Perplexity.

> "Define. Literary criticism. Define a review. Define peer feedback." (owner, 2026-11-07)
>
> "Expand the legitimation direction from the uploaded research into a concrete next step" (owner, 2026-11-14)

The Perplexity project holds a seven-slot model, an 18-persona matrix across eight aesthetic families and three vantages, a design proposal for a protocol-bound generator with world and receiver components, a Minotaur poem panel trial ("THE WALLS"), and a commissioning package for eight critical schools. Those documents are not yet imported; only the legitimation pilot is.

## First slice: legitimation pilot

The pilot asks whether a four-field model can tell three critics apart without touching their orientation:

| field | meaning |
|---|---|
| position | where the critic sits in the field |
| authority_claim | the grounds the text gives for being heard |
| granting_receiver | the audience that accepts, ignores or rejects the claim |
| recognition_outcome | what was granted, by whom, when (immediate / later / posthumous) |

Rules: claimed and granted authority are separate values (`gap = granted - asserted`); influence is never evidence of being right; orientation is fixed input.

Verdicts (exit code): PASS (0) when, on medium/high-confidence events only, the three critics have pairwise-distinct reception signatures, at least one claimed/granted gap is nonzero, an immediate/later timing split exists, and a recorded field change follows a granted outcome of the same critic. FAIL (1) when a rule breaks or the critics look alike. INCONCLUSIVE (2) when the rules hold but a critic has fewer than two medium/high-confidence outcomes, so low-confidence rows would be carrying the result.

**Current shipped result: INCONCLUSIVE.** De Piles has one evidence-grade outcome and Richardson none; the Academie reception rows are unsourced placeholders. An independent review (2026-11-15) found the first draft passed on exactly such placeholders; this version refuses to. Fixing it means sourcing those rows, not editing the validator.

```bash
PYTHONPATH=src python3 -m discourse_of_course.legitimation
```

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

`data/pilot.json` is a transcription of the Perplexity spec (`docs/source/perplexity-2026-11-14-legitimation.md`), not a verified finding. Events with confidence `low` come from a Hogarth enthusiast site and need primary-source checks; `medium` marks general-knowledge history that still needs sourcing. Known gaps: `position` and `granting_receiver` are carried as critic/outcome attributes, not separate events; the spec's house schema (`lineage`, `reception_distribution`, `displacement`, `feedback`) and its `legitimation` block plus `timing` field are not yet mapped; Richardson's reception record is thin; the 1673-2013 timeline is not yet imported.

## Next

1. Fetch the Perplexity project files (Legitimation Pilot spec, design proposal, synthesis matrix) and import them under `docs/`.
2. Map the pilot records onto the house schema and add the `legitimation` and `timing` extensions to the design proposal.
3. Verify the low-confidence events against primary sources.
