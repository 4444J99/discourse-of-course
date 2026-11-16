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

Outcomes: `granted`, `contested` (taken up and corrected; v0.3), `ignored`, `rejected`, `pending` (a placeholder, never a reception).

Rules: claimed and granted authority are separate values (`gap = granted - asserted`); influence is never evidence of being right; orientation is fixed input.

Verdicts (exit code): PASS (0) when, on medium/high-confidence events only, the three critics have pairwise-distinct reception signatures, at least one claimed/granted gap is nonzero, an immediate/later timing split exists, and a recorded field change follows a granted outcome of the same critic. FAIL (1) when a rule breaks or the critics look alike. INCONCLUSIVE (2) when the rules hold but a critic has fewer than two medium/high-confidence outcomes, so low-confidence rows would be carrying the result.

**Current shipped result (v0.3): PASS (exit 0).** Earlier sourced result (v0.2): FAIL (exit 1). Both are reported because v0.3 is a revision made after seeing the FAIL, so its PASS is not an independent confirmation.

- v0.2 coded every sourced reception `granted`. The three reception signatures were distinct and claimed and granted authority differed, but no critic showed an immediate/later split, so the timing rule failed.
- The sources say something finer than granted: Richardson (1715, 1719) calls the Balance "Curious, and Useful" but "not a just Idea" and then adopts it with alterations; Mairan (1755) praises the idea and corrects the execution (multiply the degrees, do not add). The outcome vocabulary had no value for that, so v0.3 adds `contested` (the receiver takes the claim up and corrects it; it must grant a level above `none`). Only those two rows are recoded, each because its quoted text states the reservation.
- On v0.3, De Piles shows the split: a formal grant by the Academie in 1699, then posthumous receptions that correct the scale (Richardson, Mairan) and a field-level grant from scholars (Graddy 2013, Ginsburgh and Weyers 2002). `test_v02_coding_failed_the_timing_rule` keeps the old verdict reproducible.
- Review dispositions (independent verifier, PR 3): accepted and stated here. Either recode alone clears the timing rule; only reverting both gives the FAIL. The timing rule compares sets of outcome labels (`now != later`), so adding any label to the later set can clear it without proving a substantive timing difference; that weakness predates v0.3 and is a reason to read the PASS cautiously and to replace the rule with a level-and-label comparison before the second period. Richardson's reservation is the 1715 text (p. 230) and his adoption is the 1719 text (discourse I, p. 55).
- Limits: Diderot rests on secondary sources (medium); Richardson has no reception from 1715 to 1727; the pilot passes on a small, hand-coded record and says nothing about other periods.

What sourcing changed (v0.1 to v0.2, details in `data/pilot.json` and `docs/sources.md`):

- De Piles: the Academie "ignored" row had no source and is gone. The record shows the opposite at the institutional level in 1699 (Procès-verbaux III pp. 259 and 268) and no Academie verdict on the Balance at all (the Academie only thanked him for the book, IV p. 61). Later receivers are Richardson (1715, 1719), Mairan (1755) and Graddy (2013).
- Richardson: the "1715 granted" and "1755 critique" rows were unsourced. The 1755 Mairan critique is about De Piles, not Richardson, who died in 1745. Richardson now has a French translation revised by the author (Amsterdam, 1728) and a painter-biographer's praise (Northcote, 1813). No reception from 1715 to 1727 was found.
- Diderot: only secondary web sources were read (medium). The "canon" row stays low confidence and cannot carry the verdict.

```bash
PYTHONPATH=src python3 -m discourse_of_course.legitimation
```

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

`data/pilot.json` is a transcription of the Perplexity spec (`docs/source/perplexity-2026-11-14-legitimation.md`), not a verified finding. Confidence: `high` means the primary text was read in a scan, `medium` an authoritative secondary source or a primary with an estimated date, `low` no source. Known gaps: `position` and `granting_receiver` are carried as critic/outcome attributes, not separate events; the spec's house schema (`lineage`, `reception_distribution`, `displacement`, `feedback`) and its `legitimation` block plus `timing` field are not yet mapped; Richardson's reception record is thin (nothing found for 1715 to 1727); the 1673-2013 timeline is not yet imported.

## Next

1. Test v0.3 on a second period before trusting it (the spec says to apply the model to other periods only after the pilot holds).
2. Import the Perplexity project files (Legitimation Pilot spec, design proposal, synthesis matrix). Not retrieved: the local Perplexity app stores hold no file bodies, only pointers (see `docs/sources.md`).
3. Map the pilot records onto the house schema once the design proposal is imported.
4. Diderot: read the primary Salons and a scholarly edition (Naigeon 1800 vs the conflicting 1795 date).

## Review dispositions (independent review, 2 rounds, 2026-11-15)

Fixed: placeholder-driven pass, correctness/orientation rules, outcome/level consistency, missing-key crashes, `pending` counted as a reception. Deferred, filed here as work: free-text and nested forbidden-key scan; requiring a citation shape (not just non-empty) in `source`; checking the evidence grade of a field change's `because` event; date sanity (posthumous vs death year); modelling `position` and `granting_receiver` as events.
