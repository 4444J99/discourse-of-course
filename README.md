# discourse-of-course

A first-principles framework for discourse about art: a critic's **orientation** is kept apart from the **form** and **task** of what they write. Begun by the owner in the Perplexity project `discourse-of-course` (2026-11-07); this repository is its first home outside Perplexity.

> "Define. Literary criticism. Define a review. Define peer feedback." (owner, 2026-11-07)
>
> "Expand the legitimation direction from the uploaded research into a concrete next step" (owner, 2026-11-14)

The Perplexity project holds a seven-slot model, an 18-persona matrix across eight aesthetic families and three vantages, a design proposal for a protocol-bound generator with world and receiver components, a Minotaur poem panel trial ("THE WALLS"), and a commissioning package for eight critical schools. Two of the project files are now imported under `docs/perplexity/` (the legitimation pilot spec and the Minotaur poem panel; provenance in `docs/perplexity/PROVENANCE.md`); nine others are listed there and not yet fetched.

## First slice: legitimation pilot

The pilot asks whether a four-field model can tell three critics apart without touching their orientation:

| field | meaning |
|---|---|
| position | where the critic sits in the field |
| authority_claim | the grounds the text gives for being heard |
| granting_receiver | the audience that accepts, ignores or rejects the claim |
| recognition_outcome | what was granted, by whom, when (immediate / delayed / posthumous) |

Outcomes: `granted`, `contested` (taken up and corrected; v0.3), `ignored`, `rejected`, `pending` (a placeholder, never a reception).

Rules: claimed and granted authority are separate values (`gap = granted - asserted`); influence is never evidence of being right; orientation is fixed input.

Verdicts (exit code): PASS (0) when, on medium/high-confidence events only, the three critics have pairwise-distinct reception signatures, at least one claimed/granted gap is nonzero, an immediate/delayed timing split exists, and a recorded field change follows a granted outcome of the same critic. FAIL (1) when a rule breaks or the critics look alike. INCONCLUSIVE (2) when the rules hold but a critic has fewer than two medium/high-confidence outcomes, so low-confidence rows would be carrying the result.

**Current shipped result (v0.3): PASS (exit 0).** Earlier sourced result (v0.2): FAIL (exit 1). Both are reported because v0.3 is a revision made after seeing the FAIL, so its PASS is not an independent confirmation.

- v0.2 coded every sourced reception `granted`. The three reception signatures were distinct and claimed and granted authority differed, but no critic showed an immediate/delayed split, so the timing rule failed.
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

## Differences from the original spec (`docs/perplexity/legitimation-pilot-spec.md`, checked 2026-11-15)

Corrected here: the timing value is `delayed`, as in the spec (it had been `later`).

Kept, with reasons:

- **De Piles's position.** The spec says "Academie member since 1699" and "Rubeniste theorist". The Procès-verbaux give Conseiller honoraire (listed "Conseiller-Amateur" in 1709), an honorary seat for an amateur, so the pilot records that.
- **Richardson 1715 and Mairan 1755.** The spec marks both low confidence, "verify", and tags Mairan as a rejection (rejection: high). The primary texts read for PR 2 and PR 3 show Richardson taking the scale up with corrections and Mairan praising the idea and correcting the execution, so both are coded `contested`, not rejected.
- **`contested`.** The spec's timeline uses "contested" for later critics who dispute a claim (Ruskin, Schlosser). v0.3 uses it for a receiver who takes a claim up and corrects it. The two senses differ; the spec's rejected-by-Schlosser reception is not coded.
- **Immediate reception of the Balance.** The spec says contemporaries read it as a "clever way to characterize genius" (medium). No primary record of that was found; the Procès-verbaux only record thanks for the book. Not coded.
- **Diderot.** The spec's rows rest on the research PDF and Starobinski; the pilot only has secondary web sources (medium) and keeps the "canon" row low.

Also kept, and now listed:

- **Timing labels.** The spec tags Mairan 1755 `delayed`; the pilot uses `posthumous` for Richardson 1715, Mairan 1755 and all later rows because De Piles had died in 1709. Only Richardson's 1728 translation (Richardson alive) is `delayed`.
- **Orientation labels** now use the spec's (`taxonomic-quantitative`, `empirical-judicial`, `embodied-dialogic`); v0.1 had free text. Diderot's position follows spec section 5.3.
- **Diderot's authority-claim date.** The spec dates the claim event to the 1765 Greuze Salon; the pilot dates the claim to 1759, the start of the Salons.
- **Richardson's receivers.** The spec's immediate receiver is a projected Grand Tour gentry, "projected, not attested"; the pilot records only attested receptions (1728 translation, Northcote 1813) and has no immediate row for him.
- **The Mairan item.** The spec places it under De Piles. The v0.1 pilot transcription had put it under Richardson; that was the transcription's error, fixed in PR 2.

Not yet implemented from the spec:

- The house-schema mapping (section 5: `lineage`, `saturation`, `reception_distribution`, `displacement`, `feedback`, plus the `legitimation` block and a `timing` key on receptions), and the W4 split into W4a (channels are additive) and W4b (consecrating authority migrates) before encoding.
- Pilot test item 2 (hold the field fixed, swap position, and show orientation stays put). The validator only enforces that orientation is fixed input and distinct across critics.
- The 1673-2013 timeline (section 4), the 1722 Account, and the Ruskin, Schlosser and Proust receptions.
- Spec section 8 scholarship beyond Graddy 2013 and Ginsburgh and Weyers 2002; the 2008 chapter (41 painters, 525 sales) is not read.

## Next

1. Test v0.3 on a second period before trusting it (the spec says to apply the model to other periods only after the pilot holds).
2. Fetch the remaining Perplexity project files (design proposal, synthesis matrix and the nine files listed in `docs/perplexity/PROVENANCE.md`), then do the spec's section 5 mapping and W4 split.
3. Diderot: read the primary Salons and a scholarly edition (Naigeon 1800 vs the conflicting 1795 date).

## Review dispositions (independent review, 2 rounds, 2026-11-15)

Fixed: placeholder-driven pass, correctness/orientation rules, outcome/level consistency, missing-key crashes, `pending` counted as a reception. Deferred, filed here as work: free-text and nested forbidden-key scan; requiring a citation shape (not just non-empty) in `source`; checking the evidence grade of a field change's `because` event; date sanity (posthumous vs death year); modelling `position` and `granting_receiver` as events.
