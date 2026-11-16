# Stress Test: The Seven-Slot Category System
## Twenty-Two Adversarial Cases Against the v1.0 Taxonomy

**Document type:** Adversarial test log and patch register
**Date:** November 2026
**Target:** *The Category System: Discourse About Art, Built From First Principles* (v1.0)
**Method:** Three passes — boundary objects (can the system classify the strange cases?), slot mechanics (do the seven slots behave as claimed?), system-level tests (do the floor, the legitimacy test, and the completeness promise survive?). Each case receives a verdict:

- **HOLDS** — the system survives unchanged
- **BENDS** — survives with a clarification or refinement
- **BREAKS** — fails as written; requires a patch

**Result: 9 HOLDS, 8 BENDS, 5 BREAKS.** All five breaks are patchable without touching the floor. The floor itself survived every attack — including the three aimed directly at it.

---

## Part 1 — Boundary Objects

### Case 1: The adaptation, cover, and fan work (object that is also discourse)

**Challenge.** Johnny Cash's "Hurt" is simultaneously a work and an act of discourse about Nine Inch Nails' song. The system's acts are speech acts — describe, interpret, evaluate — but a cover version performs interpret and evaluate acts without sentences. The system classifies discourse; here the discourse is a song.

**Verdict: BENDS.**

**Resolution.** Two patches, both small. First, the acts are defined functionally and medium-independently: what the discourse does to its receiver, performable in any medium — a ranking guides, a cover interprets, a parody evaluates, a manifesto describes a program. Second, the recursion rule (Case 2) makes the double nature well-formed: as a work, "Hurt" has coordinates as an object of criticism; as an act, it is participant-vantage, interpret + evaluate, in the medium of song. Two readings, two questions, no contradiction.

### Case 2: Meta-discourse — criticism of criticism

**Challenge.** A review of a biography, a critique of deconstruction, this very stress test — all are discourse about discourse. The Object slot's poles are elements of a literary work's circuit. What is the pole of a piece whose object is a critical text?

**Verdict: BENDS.**

**Resolution.** The recursion rule: every act of discourse is itself a made object with its own circuit; coordinates always apply to the immediate object. The biography review is encounter-vantage discourse about a work (the biography as artifact). The critique of deconstruction is discourse about a family of discourse-works at canon granularity. Second-order discourse is first-order discourse about a discourse-work. No infinite regress in practice, because each level classifies against its immediate object only. The rule was missing from v1.0; it is now Rule 4.5.

### Case 3: Anonymous and AI-generated works vs. the maker pole

**Challenge.** The floor claims the maker is a necessary element ("a work made by no one is not a work"). Folk songs have no identifiable author; AI-generated text has no author in the traditional sense at all. Does the maker pole fail?

**Verdict: HOLDS.**

**Resolution.** The maker element is defined as "the person and conditions of making." For anonymous works, the role is occupied by an unknown — the pole exists, biographical criticism is merely harder in practice. For AI-generated works, the conditions of making include the model, the training corpus, and the prompt — all documented, all analyzable. Maker-pole discourse tracks the conditions, which are always populated. The pole is a role with content even when the person is missing.

### Case 4: The private diary vs. the receiver pole

**Challenge.** The floor says "a work for no one is not communication — it is a private symptom." But diaries are published, read, and treated as literature. A text written for no audience became a work — did the receiver pole fail at the moment of writing?

**Verdict: HOLDS.**

**Resolution.** The floor already contained its own answer; the stress test sharpens it. The circuit completes at reception, not at making. An unreceived text is a document; it becomes a work at the moment it gets a reader. The diary's coordinates as discourse-about-art are undefined until reception — and reception history is exactly receiver-pole discourse, which the system already holds. The attack confirms the floor rather than breaking it: the receiver is not the person the maker had in mind, but the reception that makes the text a work at all.

### Case 5: Performance — text, production, performance

**Challenge.** A review of *Hamlet* may be about the play-text, this production, or last night's performance — three different objects, and theater criticism routinely distinguishes them. The Object slot has granularity (work) but no way to say *which work-identity*. The system was built by a prose-shaped eye.

**Verdict: BREAKS.**

**Resolution.** Patch: an optional **layer** sub-slot under Object, for performed and versioned forms — text / production / performance (extensible to edition, cut, draft). The layer specifies which identity of the work is the object. Without it, a production review and a text analysis collide in the same cell; with it, they are distinct coordinates at the same pole.

### Case 6: Interactive works — the player as co-maker

**Challenge.** In games and interactive fiction, the receiver is part of the making. The receiver and maker poles collapse into one person; the circuit seems to short-circuit.

**Verdict: HOLDS.**

**Resolution.** The poles are circuit positions, not persons. One person can occupy several — the poet-performer, the player who completes the work by playing it, the novelist who reviews their own book. Reader-response theory already implied this (the reader "completes" the work); interactive art only makes the overlap literal. The clarification this case forces — roles, not persons — turns out to be load-bearing (see Cases 17 and 3), so it is promoted to a floor clause in v1.1.

---

## Part 2 — Slot Mechanics

### Case 7: The work/medium pole boundary

**Challenge.** Formalist and deconstructionist criticism both attend to language — diction, syntax, figure. Brooks reads paradox; Derrida reads différance; both are staring at the same sentences. If the two poles cannot be told apart at the sentence level, the primary cut is fuzzy where it matters most.

**Verdict: BENDS.**

**Resolution.** The boundary is a question, not a wall: **is the device an achievement of the work's design (work pole) or a behavior of the material that outruns any design (medium pole)?** Brooks reads the same devices as achieved design; Derrida reads them as language's self-subversion. Jakobson sits on the line — which is why structuralism kept getting claimed by both sides. A reading that does both is a region, not a contradiction. The patch adds the boundary question to the slot definition.

### Case 8: Mode single-valuedness vs. Žižek

**Challenge.** v1.0 presents mode as single-valued: surface, hidden, or unstable. Žižek's symptomatic readings are latent-mode (the symptom beneath ideology), and his Lacanian premise — the symptom is a failed signifier, meaning that subverts itself — is unstable-mode. One living, canonical critic systematically does both. Single-valued mode cannot classify him.

**Verdict: BREAKS.**

**Resolution.** Patch: mode is multi-select with a primary — latent/unstable is Žižek's coordinate. The three values remain a closed set (the floor holds); only single-valuedness fails. The same patch absorbs psychoanalytic-deconstructive hybrids generally, and Marxist-feminist symptom readings that track both the latent and the unstable.

### Case 9: "One pole per discourse" vs. Bonaparte

**Challenge.** v1.0 §2.1 claims "every critical discourse in history is a commitment to one pole as the site of meaning." Marie Bonaparte's Poe study — canonical psychoanalytic criticism — locates meaning in the work *and* the maker's life simultaneously. Freud's own Dostoevsky essay does the same. The claim is falsified by the tradition's founding cases.

**Verdict: BREAKS** (internal contradiction: §2.1's claim conflicts with §4.3's region rule, which permits multi-pole regions).

**Resolution.** Patch: poles are **prioritized, not exclusive** — a discourse commits to a primary pole and may carry secondary ones. This is what the region rule already implied; the prose claim in §2.1 was stronger than the system's own rules. Fixed by aligning the prose with the rules.

### Case 10: Structure-requires-axis vs. New Historicism

**Challenge.** v1.0 says structural attention to the world pole "requires an axis." But New Historicism — Greenblatt's "Invisible Bullets" is the canonical case — is structural attention to power *in general*, diffused across class, gender, and sovereignty without naming one axis. The requirement excludes a founding discourse of the structure reading.

**Verdict: BENDS** (internal inconsistency: the classification procedure already allowed "axis: unspecified"; the prose claim was too strong).

**Resolution.** Patch: the axis slot takes values from the open axis set, multiple values, or **general** (power as such). The procedure and the prose now agree.

### Case 11: The closed/open count

**Challenge.** v1.0's Part 2 introduction says "five slots are closed; two are open." Its own table says otherwise: Object is mixed (closed poles, open axis), Standard is a "slowly growing menu," Format is open. The system miscounts its own openings.

**Verdict: BREAKS** (internal inconsistency, no substantive damage).

**Resolution.** Patch: the closed slots are the floor-derived ones (pole, mode, aims, vantage, posture); three slots are open by design (axis, format, standard). The count now matches the table.

### Case 12: Vantage and posture as continua

**Challenge.** A biographer who interviews their living subject for twenty years is not cleanly "reconstructive." A review can affirm a work's reputation while testing its individual claims. The three vantage values and three posture values present continua as partitions.

**Verdict: BENDS.**

**Resolution.** Patch: vantage and posture are **anchor points** on continua; classification assigns the nearest anchor, and mixed cases state their mixture. The distinction that emerges from the stress test: floor items (poles, acts, modes) are categorical because they are claims about the object; the speaker-side slots (vantage, posture) are graded because they are positions of a person. The closed sets survive as the anchor values.

### Case 13: Aim overlap — "I loved it"

**Challenge.** "I loved it" expresses, evaluates, and — in a review — guides, in three words. The five acts overlap so heavily in natural speech that sentence-level classification is often ambiguous.

**Verdict: HOLDS.**

**Resolution.** The system never promised sentence-level classification. Aims are assigned function-in-context (what work the sentence does in this recipe) and matter at piece level, where the proportions dominate. The overlap is real but harmless: the acts are distinguishable at the poles of the spectrum (a plot summary describes; a star rating guides; "I wept" expresses), and mixtures are what the proportions are for.

### Case 14: Mode naming — "surface" is misleading

**Challenge.** Brooks's readings of paradox are deep — arguably deeper than many psychoanalytic readings — yet formalism is filed under "surface" mode. "Surface" connotes shallowness and misdescribes the claim, which is that meaning is *constituted by what is manifest in the work*, not that it is shallow.

**Verdict: BENDS.**

**Resolution.** Patch: rename the modes **manifest / latent / unstable** — Freud's own manifest/latent pair, which is precise, plain, and carries no shallowness connotation. Founding discourses re-map unchanged: formalist = manifest, psychoanalytic and Marxist = latent, deconstruction = unstable.

### Case 15: The Standard slot — circularity and implicit evaluation

**Challenge.** Two problems. First, "significance — what the work reveals and withholds about its world" is near-circular: significant by what measure? Second, every piece of discourse evaluates implicitly (selecting what to discuss is an evaluation); if the Standard slot fired on every implicit evaluation, every text would need a named standard, which is unworkable.

**Verdict: BENDS.**

**Resolution.** Two-part patch. Standards must be **operationalized** — state what would count as meeting them ("the work must make its social world legible in its form," not "significant"). And the slot fires only on **explicit** evaluation — a verdict section, a ranking, a grade. Implicit evaluation (emphasis, selection, inclusion) is handled by aim proportions, not by the Standard slot.

### Case 16: Evaluating an unstable object

**Challenge.** If mode = unstable (meaning undoes itself), how can the discourse evaluate? The evaluate aim seems to presuppose a stable object. Yet Barbara Johnson's deconstructive readings judge constantly.

**Verdict: HOLDS.**

**Resolution.** The standard adapts to the mode: for a latent reading, success is depth; for an unstable reading, success is productive undecidability — the impasse that opens interpretation rather than closing it. The Standard slot names what counts as success, and success is mode-relative. No contradiction; a fact about how standards work.

---

## Part 3 — System-Level Tests

### Case 17: The legitimacy test admits gossip

**Challenge.** The test says legitimate discourse directs attention at the circuit — the work, its making, or its audience's experience. The maker is on the circuit. Therefore, by the letter of the test, a gossip column about an author's divorce is legitimate discourse about art. The commissioning package flagged gossip as a red flag; the system's own admission rule waves it through.

**Verdict: BREAKS.**

**Resolution.** Patch: the roles-not-persons clause (forced independently by Case 6) closes the hole. The circuit elements are roles: attention must land on the **maker as maker** (the conditions and choices of the making), not the maker as celebrity; on the **receiver as receiver** (the experience of the work), not the receiver as a demographic to be mocked. Gossip attends to the person occupying the role, not the role — and fails the test. One clause, three holes closed (gossip, celebrity coverage, fandom mockery).

### Case 18: The counterfeit line is fuzzy — everyone is paid

**Challenge.** The test says counterfeits redirect payoff to the speaker. But every reviewer is paid, builds reputation, and benefits from attention. The payoff criterion, taken literally, indicts the whole profession.

**Verdict: BENDS.**

**Resolution.** Patch: the **substitutability test**. Payoff redirection explains the motive; substitutability detects the counterfeit. If the object could be swapped for another without the discourse losing its function, the attention is counterfeit: rage bait works with any target, sycophancy with any patron, trend-following with any trend. Legitimate discourse is non-substitutable — it could only have been written about this work. A sincere reviewer's reputation rides on the specificity of the attention; the counterfeiter's rides on the volume.

### Case 19: Silence, refusal, and canon-by-omission

**Challenge.** A publisher's refusal to print, a critic's cone of silence, a canon built by exclusion — these shape discourse about art as powerfully as any review. Can the system classify acts that consist of not-acting?

**Verdict: HOLDS.**

**Resolution.** The system classifies acts; silence is not an act, and the system is not required to give it coordinates. What the system does instead is better: silence shows up as **empty cells**. Canon-formation-by-omission is the pattern of unoccupied coordinates across the field — which authors are reviewed, which axes are ever examined, which vantages never publish. The grid doesn't need a coordinate for silence; the grid *is* the instrument for seeing it.

### Case 20: The algorithm's aims — acts without an agent

**Challenge.** The recommendation algorithm ranks, and ranking is a guide act — but the algorithm has no intentions, no audience-awareness, no communicative purpose. The Aim slot attributes speech acts; can it attribute them to a non-agent?

**Verdict: HOLDS.**

**Resolution.** The acts are defined functionally — what the discourse does to its receiver — not intentionally. v1.0's own phrasing ("what the writing is doing to its reader") was already functional; the stress test promotes it to a rule. The algorithm performs a guide act without a guiding mind, just as a trap performs a directive act without a speaker. Classification attaches to the act, not the act's author.

### Case 21: Self-application — the system classifying itself

**Challenge.** Any system claiming to classify all discourse about art must classify the discourse about the system — including this stress test — without contradiction or infinite regress.

**Verdict: HOLDS.**

**Resolution.** By the recursion rule (Case 2), this stress test is encounter-vantage discourse whose object is a work (the category system as artifact), aims: interpret + evaluate, posture: testing, standard: completeness and coherence, operationalized as "can the floor be attacked successfully." The document you are reading is a coordinate in the system it attacks. A system that survives being applied to its own attack — and to the document recording the attack — passes the self-reference check that sinks most taxonomies.

### Case 22: The system vs. the commissioning package's author-diagnosis ban

**Challenge.** The commissioning package makes "any diagnosis of the author" an automatic-fail check in psychoanalytic reviews. But Marie Bonaparte's author-diagnosis is canonical psychoanalytic criticism. Either the field's canon is mostly counterfeit, or the package's ban is not a law of criticism.

**Verdict: HOLDS** (and clarifies the relationship between the two documents).

**Resolution.** The system exposes the ban as a **house editorial policy, not a taxonomy fact**. Maker-pole, latent-mode reading of a work is a legal coordinate — the system classifies Bonaparte without strain. The desk remains free to keep the policy (many will: author-diagnosis is the mode's most-abused cell), but the system makes visible that this is a choice about which legal coordinates to commission, not a boundary of the field. Policies should be known as policies.

---

## Part 4 — Patch Register (v1.0 → v1.1)

All patches have been applied to *The Category System*. The floor is untouched; every patch operates above it.

| # | Patch | Cases resolved | Where |
|---|---|---|---|
| P1 | Roles-not-persons clause: circuit elements are roles; attention must land on the role, not its occupant | 3, 6, 17 | §1.3, §1.6 |
| P2 | Substitutability test added to the legitimacy test | 18 | §1.6 |
| P3 | Acts defined functionally and medium-independently | 1, 20 | §1.4 |
| P4 | Modes renamed manifest / latent / unstable; mode multi-select with a primary | 8, 14 | §1.5, §2.2, tables |
| P5 | Layer sub-slot under Object (text / production / performance) for performed and versioned forms | 5 | §2.1 |
| P6 | Poles prioritized, not exclusive (primary + secondary) | 9 | §2.1 |
| P7 | Axis value "general" (power as such) permitted | 10 | §2.1 |
| P8 | Closed/open count corrected: five closed (pole, mode, aims, vantage, posture), three open (axis, format, standard) | 11 | Part 2 intro |
| P9 | Vantage and posture declared anchor points on continua | 12 | §2.5, §2.6 |
| P10 | Standards must be operationalized; slot fires on explicit evaluation only | 15, 16 | §2.4 |
| P11 | Recursion rule added: every discourse act is itself a made object; coordinates apply to the immediate object | 1, 2, 21 | §4.5 |

## Verdict Summary

| Verdict | Cases |
|---|---|
| HOLDS (9) | 3 diary-adjacent maker pole, 4 receiver pole, 6 interactivity, 13 aim overlap, 16 unstable evaluation, 19 silence, 20 agentless acts, 21 self-application, 22 policy vs. law |
| BENDS (8) | 1 adaptation, 2 meta-discourse, 7 work/medium boundary, 10 axis requirement, 12 continua, 14 mode naming, 15 standard circularity, 18 counterfeit line |
| BREAKS (5) | 5 performance layer, 8 mode single-valuedness, 9 one-pole claim, 11 closed/open count, 17 gossip hole |

**The pattern in the damage:** every break was in the *derived machinery* — slot definitions, prose claims, the admission rule's letter. The floor itself (five poles, five acts, three modes) survived direct attack at its three weakest points (the makerless work, the receiverless work, the self-referential work). The system's center of gravity is sound; its edges needed filing. That is the correct failure order for a taxonomy: if the floor had broken, the system would need rebuilding; as it stands, v1.1 is the same system with sharper teeth.

*Stress test complete. Patches applied to The Category System v1.1, same date.*
