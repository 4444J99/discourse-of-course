# Legitimation Pilot — Next-Step Specification

**Status:** Proposed next deliverable · November 2026
**Builds on:** `literature-synthesis-matrix-v2.md` (§5, §6.5, §7, §8); `world-and-receiver-design-proposal.md` (W0–W5, R0–R5, §2.3 house schema)
**Research source:** *The Architecture of Aesthetic Legitimation* (project file `History of Discourse and Personas in Art Creation.pdf`)

---

## 1. The question

The framework can already build an utterance about art: orientation, form, act and the other coordinate slots. It cannot yet say **under what conditions that utterance counts**. Legitimation is the missing layer. It covers how a critique gets standing, who grants that standing, and how granting it changes the field for whatever comes next.

The research shows the mechanism repeatedly without formalizing it. Examples: Apelles silencing the shoemaker (jurisdiction), Apelles buying Protogenes' canvases (consecration by a peer), De Piles' Color scores predicting auction prices centuries later (recognition delayed and separated from the original audience), Vasari's observation that Alberti's writings gave him more fame than his betters (discourse outranking practice), and the TikTok "backtrack" workflow (the receiver scripting the speaker).

## 2. The concrete next step

Build **one pilot field study, the Paris–London art-criticism field of 1708–1765**, using a new four-part legitimation model. Run one test against it before encoding any other period.

This narrows the matrix's recommended field-study pack (§8) to a single test that can fail. If the model can't tell apart three critics who shared roughly the same field, it shouldn't be scaled to twelve episodes.

### Why this field

| Critic | Orientation | Authority claim | Who granted recognition |
|---|---|---|---|
| Roger de Piles, *Balance des peintres* (1708) | Taxonomic, quantitative | Systematic method; claims it is "for my own pleasure" (an authority claim made through disavowal) | Contemporaries treated it as serious; later scholars (Schlosser) rejected it; the market and canon vindicated the Color scores long after |
| Jonathan Richardson, *Two Discourses* (1719) | Empirical, judicial | Connoisseurship as a "science" with "dignity, certainty" | Grand Tour gentry and merchants as the projected Second Persona |
| Denis Diderot, *Salons* (1759–1781, pivot 1765) | Embodied, dialogic | Literary performance; unconventional art needs unconventional criticism | Grimm's subscriber circle at first; then literary posterity (Proust) |

There are three distinct strategies across roughly one field state, and each has a documented reception. That makes this the best natural experiment in the source.

## 3. The model: four separations

Persona has already been separated from form. Legitimation adds four fields that must stay independent of one another and of orientation:

1. **Position:** where the speaker sits in the field (academician, outsider-theorist, practising painter, philosophe-journalist).
2. **Authority claim:** the grounds the text offers for being heeded (method, expertise, experience, institutional office, independence, disavowal).
3. **Granting receiver:** the specific community that accepts, ignores or rejects the claim. A single text gets one entry per receiver.
4. **Recognition outcome:** what was granted, by whom, and when (immediate / delayed / posthumous), recorded separately from whether the claim was correct.

Two invariants:

- **L-1:** Claimed authority and recognized authority are separate values. A model that derives one from the other fails.
- **L-2:** Recognition is not correctness. Influence never flows back into an evaluation of truth.

Also required before encoding (from matrix §6.5): **split W4** into *channels are additive* (new distribution channels join old ones) and *consecrating authority migrates* (a new consecrator displaces the previous one rather than joining it).

## 4. Timeline of the four-part model

Each event is tagged with the part of the model it instantiates: **P** position, **A** authority claim, **G** granting receiver, **R** recognition outcome. The pilot field runs 1708–1765. Earlier events supply lineage, and later events supply delayed recognition, which is where claimed and granted authority diverge (L-1).

| Year | Event | Part | Source · confidence |
|---|---|---|---|
| 1673 | De Piles, *Dialogue sur le coloris*: "color is the soul of painting." Origin of the Color claim the *Balance* later quantifies | A (lineage origin) | Research PDF p. 8 · high |
| 1699 | De Piles admitted to the Académie Royale, long after Félibien. He moves from outside Rubéniste theorist to inside member | P | [Ginsburgh & Weyers 2002](https://artibusethistoriae.org/chapter439.html) · high |
| 1708 | *Balance des peintres* published as an appendix to *Cours de peinture par principes*: 56 painters scored 0–20 on four attributes; disavowed as "for my own pleasure" | A | Research PDF p. 8; [Ginsburgh & Weyers 2008](https://dipot.ulb.ac.be/dspace/bitstream/2013/152102/1/de-piles.pdf) · high |
| 1708–1709 | Contemporaries read the *Balance* as a "clever way to characterize genius"; it tracks the court's taste more closely than Félibien did | G, R (immediate) | Research PDF p. 8; [Ginsburgh & Weyers 2002](https://artibusethistoriae.org/chapter439.html) · medium |
| 1715 | Richardson, *Essay on the Theory of Painting*, endorses De Piles' method and adds Invention, Handling, and Grace and Greatness | G (a peer grants and extends) | [Hogarth scholarship site](http://www.william-hogarth.de/balance.html) · low, verify against Richardson |
| 1719 | Richardson, *Two Discourses*: connoisseurship as a "science" with "dignity, certainty"; addressed to Grand Tour gentry and merchants | P, A | Research PDF p. 9 · high |
| 1722 | Richardson and his son, *Account of … Pictures in Italy*: the method applied in the field | A | Research PDF p. 9 · high |
| 1755 | Mathematician Dortous de Mairan criticizes the *Balance*'s scoring before the Académie Royale des Sciences | G (rejects) | [Hogarth scholarship site](http://www.william-hogarth.de/balance.html) · low, verify |
| 1759 | Diderot begins reviewing the Salons for Grimm's manuscript newsletter, the *Correspondance littéraire*, with a small subscriber circle | P, G | Research PDF p. 10 · high |
| 1765 | Diderot's Salon on Greuze's *Girl Weeping Over Her Dead Bird*: authority claimed through embodied literary performance | A | Research PDF p. 10 · high |
| 1781 | Diderot's Salons end | — | Research PDF p. 10 · high |
| Later | Ruskin abandons Richardson's judicial detachment; Schlosser rejects the *Balance*; Proust's Elstir passages continue Diderot's mode | R (delayed, contested) | Research PDF pp. 8–10 · medium |
| 1977–1996 | Auction prices (1977–1993) and Turner's *Dictionary of Art* (1996) used as long-run measures of De Piles' standing | R (posthumous) | [Ginsburgh & Weyers 2008](https://dipot.ulb.ac.be/dspace/bitstream/2013/152102/1/de-piles.pdf) · high |
| 2002–2013 | Peer-reviewed econometrics find the ratings survived the "test of time" (see §8) | R (posthumous, measured) | §8 · high |

In this timeline, De Piles is the only critic with a recognition arc that is fully measured. Richardson's arc is mostly a projected audience plus one peer endorsement. Diderot's arc runs through a private channel first and literary posterity later.

## 5. Mapping onto the house schema

The design proposal (project file `world-and-receiver-design-proposal.md`) defines one JSON extract format, for the world component (§2.3). The receiver component specifies algorithms but no JSON. The mapping below keeps the world format exactly and expresses each critic as a field event whose keys use the names of existing algorithm outputs (`lineage`, `saturation`, `reception_distribution`, `displacement`, `feedback`). Where the house schema has no slot, a key under `legitimation` is added and marked as an extension.

### 5.1 How the four parts map

| Model part | House-schema home | Status |
|---|---|---|
| Position | W5 "position" → `event.position`, checked by `saturation` | Existing (W5) |
| Authority claim | None. The closest neighbour is `authority_map`, but that describes the field, not a speaker's claim (W1) | **Extension:** `legitimation.authority_claim` |
| Granting receiver | `reception_distribution` communities, each with resonance / misreading / rejection | Existing; one added `timing` key |
| Recognition outcome | `feedback` world-state deltas plus `displacement` | Existing; **extension:** `legitimation.claimed_vs_granted` to enforce L-1 |

### 5.2 Field state (house format, unchanged)

```json
{
  "id": "world-field-state-paris-london-1708-1765",
  "component": "world",
  "axioms": [
    {"id": "W1", "statement": "Authority is a system, not a person."},
    {"id": "W4a", "statement": "Channels are additive: new distribution channels join old ones."},
    {"id": "W4b", "statement": "Consecrating authority migrates: a new consecrator displaces the prior one."}
  ],
  "field_state": {
    "period": "1708-1765, Paris and London",
    "authority_map": {
      "who_can_speak": ["academicians", "learned theorists", "gentleman-connoisseurs", "philosophes writing for subscribers"],
      "whose_judgments_count": ["Académie Royale", "the court's taste", "Grand Tour collectors"],
      "gatekeepers": ["Académie Royale de Peinture et de Sculpture", "royal censors", "subscription newsletters"]
    },
    "channels": ["academies", "learned treatises", "public Salon exhibitions", "manuscript subscription newsletters", "public print"],
    "visibility_regime": "Distribution through print and the biennial Salon; discovery mediated by the Académie and private subscriber networks (W2: separate layers)",
    "sayable_set": ["disegno outranks color (orthodox)", "color is the soul of painting (contested, sayable after 1673)", "criticism as rational science", "criticism as sentimental performance (anomalous until c. 1765)"]
  },
  "core_algorithms": [],
  "diagnostic_questions": [{"id": "WD-3", "question": "Are authority structures of the period named or contested, never assumed?", "valid_if": "authority_map consulted"}]
}
```

### 5.3 The three critics as field events

```json
[
  {
    "id": "event-depiles-balance-1708",
    "field_state_ref": "world-field-state-paris-london-1708-1765",
    "speaker": "Roger de Piles",
    "text": "Balance des peintres (1708)",
    "orientation": "taxonomic-quantitative",
    "position": "Rubéniste theorist; Académie member since 1699",
    "lineage": {"origin": "Dialogue sur le coloris (1673)", "mutations": [{"year": 1708, "type": "amplified", "note": "color made a scored, independent criterion"}, {"year": 1715, "type": "domesticated", "note": "Richardson adopts the method and adds categories"}]},
    "saturation": {"occupancy": "low", "differentiation": "first numerical rating of painters"},
    "legitimation": {
      "authority_claim": ["systematic method", "disavowal: 'for my own pleasure'"],
      "claimed_vs_granted": "claimed modestly; granted widely, then contested, then vindicated"
    },
    "reception_distribution": [
      {"community": "contemporaries and court taste", "resonance": "high", "misreading": "read as a serious ranking despite the disavowal", "rejection": "low", "timing": "immediate"},
      {"community": "Académie des Sciences (Dortous de Mairan, 1755)", "resonance": "low", "rejection": "high", "timing": "delayed"},
      {"community": "traditional art historians (Schlosser)", "resonance": "low", "rejection": "high", "timing": "delayed"},
      {"community": "market and reference canon (1977–1996 measures)", "resonance": "high (Color, and overall ratings)", "rejection": "low", "timing": "posthumous"}
    ],
    "displacement": {"taste_delta": "Color legitimized as an independent criterion", "misfire_risk": "quantitative reductionism"},
    "feedback": {"world_state_deltas": ["'color is the soul of painting' moves from contested to sayable", "numerical rating enters the channel repertoire"]},
    "evidence": {"passage": "research PDF pp. 8–9", "citation": "Ginsburgh & Weyers 2002, 2008; Graddy 2013", "uncertainty": "low for the posthumous result; medium for immediate reception"}
  },
  {
    "id": "event-richardson-two-discourses-1719",
    "field_state_ref": "world-field-state-paris-london-1708-1765",
    "speaker": "Jonathan Richardson (Senior; Junior as editor)",
    "text": "Two Discourses (1719)",
    "orientation": "empirical-judicial",
    "position": "practising portraitist writing as a theorist",
    "lineage": {"origin": "De Piles' attribute method", "mutations": [{"year": 1715, "type": "amplified", "note": "Invention, Handling, Grace and Greatness added"}, {"year": 1719, "type": "amplified", "note": "connoisseurship systematized as a 'science'"}, {"year": null, "type": "inverted", "note": "Ruskin abandons judicial detachment"}]},
    "saturation": {"occupancy": "low in English", "differentiation": "first systematic English method of criticism"},
    "legitimation": {
      "authority_claim": ["method as science: 'dignity, certainty, pleasure, and advantage'", "judicial detachment"],
      "claimed_vs_granted": "granted status uncertain: the source attests only a projected audience"
    },
    "reception_distribution": [
      {"community": "Grand Tour gentry and merchant collectors (projected Second Persona)", "resonance": "projected", "rejection": "unknown", "timing": "immediate"},
      {"community": "Romantic critics (Ruskin)", "resonance": "low", "rejection": "high (of detachment)", "timing": "delayed"}
    ],
    "displacement": {"belief_delta": "attribution framed as a learnable discipline", "misfire_risk": "unmeasured"},
    "feedback": {"world_state_deltas": ["'criticism as rational science' joins the English sayable_set"]},
    "evidence": {"passage": "research PDF pp. 9–10", "citation": "Richardson 1715, 1719, 1722", "uncertainty": "high: reception is projected, not attested"}
  },
  {
    "id": "event-diderot-salon-1765",
    "field_state_ref": "world-field-state-paris-london-1708-1765",
    "speaker": "Denis Diderot",
    "text": "Salon de 1765 (Greuze passage)",
    "orientation": "embodied-dialogic",
    "position": "Encyclopédie editor writing for a private manuscript newsletter",
    "lineage": {"origin": "Salons from 1759", "mutations": [{"year": 1765, "type": "amplified", "note": "diegetic immersion: the critic speaks to the painted figure"}, {"year": null, "type": "domesticated", "note": "Proust's Elstir passages"}]},
    "saturation": {"occupancy": "open", "differentiation": "criticism as an autonomous literary performance"},
    "legitimation": {
      "authority_claim": ["unconventional art needs unconventional criticism", "literary performance", "dialogic self-contestation"],
      "claimed_vs_granted": "small immediate circle; large posthumous literary recognition"
    },
    "reception_distribution": [
      {"community": "Correspondance littéraire subscribers", "resonance": "high", "rejection": "low", "timing": "immediate"},
      {"community": "literary posterity (Proust)", "resonance": "high", "rejection": "low", "timing": "posthumous"}
    ],
    "displacement": {"taste_delta": "sentimental genre painting (Greuze) given a raison d'être", "misfire_risk": "critic overwrites the work"},
    "feedback": {"world_state_deltas": ["'criticism as sentimental performance' moves from anomalous to sayable"]},
    "evidence": {"passage": "research PDF p. 10", "citation": "Diderot, Salons; Starobinski", "uncertainty": "medium"}
  }
]
```

Two schema findings came out of this mapping. First, `circulation_realism` matters for Diderot: his authority claim was made inside a manuscript channel with a few subscribers, so his public recognition could only come later. Second, the house schema needs a `timing` key on reception entries. Without one, the immediate and posthumous verdicts on De Piles collapse into a single contradictory profile, which RD-1 forbids.

## 6. The test

**Pilot test:** Hold the field state fixed and vary only position and authority claim. The model should:

1. Produce three different reception distributions for De Piles, Richardson and Diderot that match the documented ones.
2. Keep orientation independent. For example, re-assigning Richardson's empirical orientation to a speaker in Diderot's position should change the predicted receivers, not the orientation itself.
3. Show at least one case where claimed and recognized authority diverge (De Piles' disavowal followed by delayed canonization). This exercises L-1.
4. Record a field effect for at least one critic. That is the first instance of the receiver-to-world feedback loop the design proposal lacks.

**Pass:** all four hold and every record traces back to a cited passage.
**Fail:** if the three critics collapse into one reception pattern, or if recognition can only be expressed by re-describing orientation, revise the four-field model before scaling.

## 7. Out of scope for the pilot

- The other nine episodes (Apelles through AI). They come after the pilot passes.
- Constitutive rhetoric, negation (Third Persona) and algorithmic receivers. These are logged as gaps in matrix §7 and are better tackled once the base model holds.
- Any change to persona names. The research's named masks stay descriptive; only their coordinates are imported.
- Any goal that optimizes generated critiques for legitimacy. The model explains how standing is sought and granted. It doesn't make "become legitimate" a target.

## 8. Scholarship on the De Piles econometrics

The pilot's strongest recognition evidence rests on the following work. The first and third items appeared in peer-reviewed journals. The second is a chapter in an edited Routledge volume, which is a lighter form of review.

- **Ginsburgh & Weyers (2002), "De Piles, Drawing and Color: An Essay in Quantitative Art History," *Artibus et Historiae* 23(45): 191–203.** They find that De Piles' scores are only mildly reflected in his own *Abrégé*, where Color is a weak explanation of the space he gives each painter. The *Abrégé* tracks the number of a painter's works in the royal collection more closely. De Piles agreed with the King's taste more than Félibien did and predicted better which painters would pass the test of time ([Artibus et Historiae](https://artibusethistoriae.org/chapter439.html); [EconPapers record](https://econpapers.repec.org/paper/ulbulbeco/2013_2f1685.htm)). This is the likely source of the research PDF's "7.4 lines" figure. The 2008 chapter does not report it.
- **Ginsburgh & Weyers (2008), "On the Contemporaneousness of Roger de Piles' *Balance des Peintres*," in Amariglio, Childers & Cullenberg (eds.), *Sublime Economy*, Routledge, pp. 112–123.** They regress two modern value measures on the four scores for 41 painters. One measure is entry length in Turner's 1996 *Dictionary of Art*. The other is log prices from 525 auction sales between 1977 and 1993, controlling for size, year and salesroom. A one-point Color increase adds 64.6 lines (64.644) and raises price by 11.9% (exp(0.112) − 1). Drawing is not significant in either measure (−6.754 lines; 0.007) ([working-paper version](https://dipot.ulb.ac.be/dspace/bitstream/2013/152102/1/de-piles.pdf); [Taylor & Francis chapter page](https://www.taylorfrancis.com/chapters/edit/10.4324/9780203890578-11/contemporaneousness-roger-de-piles-balance-des-peintres-victor-ginsburgh-sheila-weyers)).
- **Graddy (2013), "Taste Endures! The Rankings of Roger de Piles (†1709) and Three Centuries of Art Prices," *Journal of Economic History* 73(3): 766–791, [doi:10.1017/S0022050713000600](https://doi.org/10.1017/S0022050713000600).** This is an independent peer-reviewed test using two datasets that run from the mid-eighteenth century to the present. Works by De Piles' higher-rated artists achieved both greater returns and higher critical acclaim ([Cambridge Core](https://www.cambridge.org/core/journals/journal-of-economic-history/article/abs/taste-endures-the-rankings-of-roger-de-piles-1709-and-three-centuries-of-art-prices/60C08B95BE92118109624509764D5ED2)). Graddy's result concerns overall ratings, not Color alone.
- **Context:** Ginsburgh & Weyers (2006), "Persistence and Fashion in Art: Italian Renaissance from Vasari to Berenson and Beyond," *Poetics* 34(1): 24–44 ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0304422X05000318)). This established the encyclopedia-entry-length method. A later Low Countries study replaced their Spearman rank correlations with standardized log z-scores ([CORE](https://core.ac.uk/download/pdf/43326394.pdf)).

**What this changes in the pilot:** De Piles' posthumous recognition is supported by two independent lines of evidence, so its uncertainty drops from "medium — single econometric study" to low. The finding is also more nuanced than the research PDF suggests. Color predicts long-run standing, but it did not drive De Piles' own writing, which followed the royal collection. That gap between the claim he scored and the evidence he actually wrote from is itself a legitimation datum for the record.

## 9. Known limits

- The source is centred on visual art. Transfer to literary criticism is plausible but untested.
- The 1715 Richardson endorsement and the 1755 Dortous de Mairan critique come from a non-peer-reviewed scholarship site. Check both against primary texts before encoding.
- Richardson's reception is projected rather than attested, so his record carries high uncertainty.
- The `legitimation` block and the reception `timing` key extend the house schema. Fold them into the design proposal before scaling to other field studies.

