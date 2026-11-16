# World and Receiver Components — Design Proposal

Proposed designs for the two missing circuit components of the discourse system, plus the generative layer that unifies all five components. Plain taxonomy throughout: components are named for their circuit role.

---

## 0. Design Philosophy: Laws, Not Destinations

The existing components formalize three of the five circuit roles:

| Circuit role | Component | Repo | What it makes computable |
| --- | --- | --- | --- |
| Maker | Voice governance (Organ IV) | [vox--architectura-gubernatio](https://github.com/4444J99/vox--architectura-gubernatio) | Authorial voice, scored and governed |
| Work | Narratological suite | [narratological-algorithmic-lenses](https://github.com/4444J99/narratological-algorithmic-lenses) | Narrative structure, diagnosed against 141 algorithms |
| Medium | Text analysis (Organ I) | [linguistic-atomization-framework](https://github.com/4444J99/linguistic-atomization-framework) | Language itself, atomized and measured |
| **World** | **— missing —** | | Context, history, authority, visibility |
| **Receiver** | **— missing —** | | Reception, audience, effect |

This document proposes the two missing components — the **world component** and the **receiver component** — and, more importantly, the generative framework that turns all five into a system of critique generation.

### 0.1 The Rejected Model: Definitions as Blueprints

A teleological generator defines its units by what they are *for*: "this persona produces devastating takedowns," "this format produces 900-word consumer reviews." Every unit carries an end-state in its definition. This caps the system at the imagination of its author. The output space is finite because every definition encodes a destination.

### 0.2 The Adopted Model: Laws, Not Destinations

Physics does not define an electron by where it will end up. It defines the electron by intrinsic properties (mass, charge, spin) and defines *laws* that constrain how any configuration of particles evolves. Trajectories are computed, not stored. The set of possible trajectories is infinite; the set of law-violating trajectories is zero.

The equivalent move here:

- **A persona is a particle species**: a bundle of intrinsic properties (aim vector, standard field, vantage, posture) — never a target output.
- **A format is a constraint manifold**: a grammar of permitted states and transitions, not a template to fill.
- **The five components are force fields**: each applies a lawful coupling to every generated trajectory.
- **Conservation laws**: invariants that must hold along every trajectory (region fidelity, verification separation, format coherence). These replace quality goals.
- **A critique is a trajectory, not a product**: computed from initial conditions (the commission) under the laws, never retrieved from a library of endings.

Infinite results, protocol-bound: the infinity is the combinatorial space of lawful trajectories; the bound is the set of invariants no trajectory can violate.

---

## 1. The Generative Model

### 1.1 State Space

A critique instance is a point moving through the seven-slot coordinate space (Object, Mode, Aim, Standard, Vantage, Posture, Format) plus auxiliary dimensions (evidence base, register, length, medium of delivery). Formally:

```
C(t) = (object, mode, aim_vector, standard, vantage, posture, format_state, evidence, register)
```

where `aim_vector` is a weighting over the five discourse acts (describe, interpret, evaluate, guide, express) and `format_state` is a position in the format's section grammar.

### 1.2 Persona and Format Definitions (First Principles, No End-States)

Following the narratological house method — axioms, structural hierarchy, core algorithms, diagnostic questions, JSON extract — every persona and format gets a **definition**: a property bundle with zero output specifications:

```
PERSONA_DEFINITION = {
  axioms:            [premises the critic holds about art and value],      # e.g., Kael: "movies are sensual experience first"
  aim_vector:        {describe: w1, interpret: w2, evaluate: w3, guide: w4, express: w5},
  standard_field:    [value standards applied, with relative weights],
  vantage:           participant | reconstructive | encounter,
  posture:           stance toward the work, the field, and the reader,
  sensitivities:     [structural features this persona notices at low threshold],
  blind_spots:       [structural features this persona cannot register],
  couplings:         [lawful reactions to other definitions, e.g., "contests authority-claims"]
}
```

```
FORMAT_DEFINITION = {
  section_grammar:   ordered/recursive set of permitted sections and transitions,
  invariants:        constraints that hold at every state (e.g., verdict must name its standard),
  budgets:           word/time/evidence budgets as soft bounds,
  registers:         permitted register range,
  termination:       lawful end conditions (never "when it feels done")
}
```

Neither definition contains an end-state. A Kael definition is not "writes rhapsodic contrarian essays"; it is a set of axioms, thresholds, and couplings from which rhapsodic contrarian essays *emerge* under most boundary conditions — and from which other, never-written Kael essays emerge under others.

### 1.3 Equations of Motion (Draft-Level Dynamics)

A critique draft evolves section by section. At each step, the next state is computed from the lawful forces:

```
GIVEN:
  - commission = initial conditions (declared region R, object, constraints)
  - persona P, format F
  - world state W(t)      # from the world component
  - receiver model Rv     # from the receiver component

EVOLVE C(t) through F.section_grammar:
  force_aim      = P.aim_vector                # what the persona wants to do next
  force_standard = P.standard_field(object)    # evaluative pull toward/away from features
  force_world    = W.coupling(C, t)            # what the field makes visible, sayable, urgent
  force_receiver = Rv.impedance(C)             # where the receiver can actually follow
  drift          = stochastic_seed             # unbounded variation source

  C(t+1) = lawful_resolution(forces, drift)
    subject to:
      INV-1  C(t+1) ∈ R                        # region fidelity (may never leave declared region)
      INV-2  format invariants of F hold
      INV-3  posture coherence of P holds
      INV-4  every claim carries its evidence   # no claim-evidence violation
      INV-5  classification ≠ verification     # the two checks run independently, always

TERMINATE when: F.termination conditions met
```

### 1.4 Conservation Laws (The Protocol Bound)

These are the laws of the system — the constraints that make "infinite yet protocol-bound" a formal property rather than a hope:

| Law | Statement |
| --- | --- |
| **L1 (Region Conservation)** | A trajectory may not leave its declared commission region. Hybrid regions are declared unions; drift is a violation, not a style. |
| **L2 (Evidence Conservation)** | No critique may contain evaluative or factual energy beyond its evidence base. The claim-evidence ratio is bounded above. |
| **L3 (Standard Conservation)** | An evaluative verdict must name and apply its standard. Verdicts without standards are physically impossible in this system. |
| **L4 (Verification Separation)** | Region fidelity and citation verification are independent measurements. A piece can pass one and fail the other; the system never collapses them. |
| **L5 (Posture Coherence)** | A persona's posture is invariant along a single trajectory. (Multi-persona critiques are composite trajectories, explicitly stitched.) |
| **L6 (Reception Reality)** | No generated critique may assert its own reception. Effect is measured, not declared. |

### 1.5 Where the Infinity Comes From

- Combinatorial: personas × formats × objects × regions × world-states × receiver models.
- Dynamical: the stochastic drift term inside lawful bounds — no two trajectories are identical even from identical initial conditions.
- Historical: the world state W(t) never repeats; every period, every visibility configuration, is new boundary conditions.

The infinity is real but entirely lawful — exactly as the set of legal chess games is infinite while the rules are fixed.

---

## 2. Component Design: World

The world component operationalizes the cultural-discourse-history concept: discourse about art is shaped by changing systems of authority — who can speak, whose judgments count, how responses circulate, and what determines visibility. It makes the world a computable boundary condition rather than a vague backdrop.

### 2.0 Axioms

| Axiom | Formulation |
| --- | --- |
| W0 | There is no origin point of discourse about art; surviving documents mark the record, not the beginning. |
| W1 | Authority is a system, not a person: who can speak, whose judgments count, and how responses circulate are properties of a field, not of individuals. |
| W2 | Publication and visibility are distinct layers: distribution lowers barriers; discovery shapes what is encountered. |
| W3 | Engagement is not critical quality: interaction is a distribution signal, not a judgment of value or truth. |
| W4 | Discourse systems overlap rather than replace: salons persist inside platform feeds; the field is additive. |
| W5 | Every critique is an event in a field: it has a position (occupied or open region), a lineage (claims it inherits and mutates), and drag (what the field makes easy or hard to say). |

### 2.1 Core Algorithms

```
ALGORITHM field_state(t)
  PURPOSE: reconstruct the discourse field at time t
  INPUTS:  period, locale, medium ecosystem
  OUTPUTS: authority_map, circulation_channels, visibility_regime, sayable_set
  GIVEN a period:
    authority_map   = {who can speak, whose judgments count, institutional gatekeepers}
    channels        = {performance communities, learned traditions, academies, salons,
                       public print, institutional criticism, networked publishing, platform feeds}
                      # additive, overlapping — never a single replacement (W4)
    visibility      = f(distribution_layer, discovery_layer)   # separate per W2
    sayable_set     = claims the field can register without anomaly
```

```
ALGORITHM anachronism_check(critique, t_work, t_critique)
  PURPOSE: detect standards applied before they existed
  INPUTS:  critique's standard_field, world states at t_work and t_critique
  OUTPUTS: violations[]
  FOR each standard s in critique.standard_field:
    t_s = first appearance of s in field_state history
    IF t_s > t_work AND critique applies s as if timeless:
      flag {standard: s, invented: t_s, applied_to: t_work}
  # the inverse is also checked: critiques judged by standards invented after them
```

```
ALGORITHM lineage(claim)
  PURPOSE: trace a claim's ancestry through the field
  INPUTS:  claim text, field history
  OUTPUTS: provenance chain with mutation deltas
  GIVEN claim:
    find earliest articulation
    walk forward: each re-articulation is a mutation (amplified, contested, inverted, domesticated)
    output: {origin, mutations[], current_position, adoption_curve}
```

```
ALGORITHM saturation(critique_region, t)
  PURPOSE: is this critique landing in an occupied or open region?
  INPUTS:  declared region, field_state(t)
  OUTPUTS: occupancy score, nearest neighbors, differentiation requirement
  IF occupancy high:
    the trajectory must carry differentiation force (what does this add to the field?)
```

```
ALGORITHM circulation_realism(critique, t)
  PURPOSE: does the critique's imagined path match the media systems of its period?
  INPUTS:  critique, channels(t)
  OUTPUTS: feasible paths[]
  # a 1790s salon critique cannot "go viral"; a platform-feed critique can.
  # mismatches between claimed circulation and available channels are violations.
```

### 2.2 Diagnostics

| ID | Question | Valid if |
| --- | --- | --- |
| WD-1 | Does the critique apply only standards available at its moment? | anachronism_check returns no violations |
| WD-2 | Does the critique know its position in the field? | saturation computed; if occupied, differentiation present |
| WD-3 | Are authority structures of the period named or contested, never assumed? | authority_map consulted |
| WD-4 | Is visibility treated as a system outcome, not a merit outcome? | no conflation of distribution signal with judgment |
| WD-5 | Are claims in the sayable_set, or is their anomaly acknowledged? | sayability check explicit |

### 2.3 JSON Extract Schema (house format)

```json
{
  "id": "world-field-state-<period>",
  "component": "world",
  "axioms": [{"id": "W0", "statement": "..."}],
  "field_state": {
    "period": "...",
    "authority_map": {},
    "channels": [],
    "visibility_regime": "...",
    "sayable_set": []
  },
  "core_algorithms": [{"name": "...", "purpose": "...", "pseudocode": "...", "inputs": [], "outputs": []}],
  "diagnostic_questions": [{"id": "WD-1", "question": "...", "valid_if": "..."}]
}
```

### 2.4 What the World Component Is Not

It is not a history database. It is a **boundary-condition engine**: the other components query it for `W(t)` and receive lawful constraints on what a generated critique can see, say, and presume. It does not judge critiques; it conditions them.

---

## 3. Component Design: Receiver

The receiver component makes reception computable. It formalizes the least-formalized circuit role: the receiver as a co-producer of meaning, not a passive endpoint.

### 3.0 Axioms

| Axiom | Formulation |
| --- | --- |
| R0 | Reception is an act: receivers co-produce meaning; they do not receive it intact. |
| R1 | Every receiver is positioned: the coordinate system applies to receivers too (they have vantages, postures, standards of their own). |
| R2 | A work has no reception; it has a distribution over interpretive communities. |
| R3 | The implied receiver constructed by the work is never identical to actual receivers; the gap is productive, not error. |
| R4 | A work's meaning includes its reception history: meaning at time t is conditioned by all prior receptions. |
| R5 | Effect is displacement: what a discourse act measurably changes in a receiver's state — belief, attention, taste, action — or it is nothing. |

### 3.1 Core Algorithms

```
ALGORITHM horizon(community, t)
  PURPOSE: reconstruct the expectations a community brings to a work
  INPUTS:  community profile, field_state(t) from the world component
  OUTPUTS: expectation set, tolerance bands, prior commitments
  # a 1962 Cahiers du Cinéma reader and a 2026 algorithmic-feed scroller
  # bring different horizons to the same Godard film; both are lawful receivers.
```

```
ALGORITHM implied_receiver(work)
  PURPOSE: extract the receiver the work itself constructs
  INPUTS:  work features (from the narratological suite), medium signals (from the text analysis component)
  OUTPUTS: assumed knowledge, assumed taste, addressed posture
```

```
ALGORITHM reception_distribution(work, communities)
  PURPOSE: predict the resonance profile across communities
  INPUTS:  work features, community horizons
  OUTPUTS: per-community {expected resonance, expected misreading, expected rejection}
  # per R2, output is a distribution, never a single verdict
```

```
ALGORITHM displacement(critique, receiver)
  PURPOSE: compute what the critique does to a receiver state
  INPUTS:  critique trajectory, receiver model
  OUTPUTS: {belief_delta, attention_delta, taste_delta, action_delta, misfire_risk}
  # per R5: effect is measured displacement or it does not exist
  # per L6: the critique itself never gets to assert its own displacement
```

```
ALGORITHM impedance_match(critique, receiver)
  PURPOSE: where does the receiver stop following?
  INPUTS:  critique register/density trajectory, receiver capacity
  OUTPUTS: {followable_fraction, strain_points[], collapse_points[]}
  # a critique that outruns its receiver's horizon at step n loses the reader at step n;
  # this is a lawful coupling, not a style preference
```

```
ALGORITHM feedback(reception_events)
  PURPOSE: close the circuit
  INPUTS:  actual or simulated reception events
  OUTPUTS: world-state deltas → world component
  # receiver responses become new field events (new claims, new visibility, new authority)
  # the circuit is a loop: the world component conditions reception; reception updates the world
```

### 3.2 Diagnostics

| ID | Question | Valid if |
| --- | --- | --- |
| RD-1 | Is reception modeled as a distribution, not a verdict? | single-receiver fallacy absent |
| RD-2 | Is the implied/actual receiver gap acknowledged where it matters? | gap computed, not assumed zero |
| RD-3 | Does any claimed effect have a measurable displacement? | displacement computed or claim withdrawn |
| RD-4 | Does the critique stay within the receiver's followable range, or knowingly strain it? | impedance matched or strain deliberate |
| RD-5 | Are the receiver's own coordinates named (vantage, posture, standards)? | receiver positioned per R1 |

### 3.3 The Measurement Postulate

The receiver component's deepest axiom, worth stating separately: **a critique's effect exists as a distribution of possible displacements until reception collapses it.** Like measurement in physics, the act of reception converts potential effect into actual effect — and different receivers collapse it differently. This is why L6 forbids generated critiques from asserting their own reception: the outcome has not been measured yet.

---

## 4. The Generative Synthesis: Five-Component Coupling

### 4.1 The Full Circuit as a System

```
                    ┌─────────────────┐
        maker ─────► │ voice governance │
                    └────────┬────────┘
                             │ voice-conditioned text
                             ▼
        work ───────► narratological suite   structure diagnosis
                             │
                             ▼
        medium ─────► text analysis           language measurement
                             │
                             ▼
        world ──────► world component        boundary conditions W(t)
                             │
                             ▼
        receiver ───► receiver component     reception field, impedance
                             │
                             ▼
                     GENERATIVE CORE
              persona definition × format definition
                × commission (initial conditions)
                      × W(t) × Rv
                = lawful trajectory space
                             │
                             ▼
                   CONSERVATION GATES (L1–L6)
                             │
                             ▼
                   critique (one trajectory)
                             │
                             └──► reception events ──► world component (field update)
```

### 4.2 The Master Protocol

One generation run, stated as a system of laws:

```
GIVEN:
  seed s, commission K (region R, object, constraints),
  persona P, format F,
  world state W(t) [world component], receiver model Rv [receiver component]

COMPUTE:
  initial state C(0) from K
  trajectory C(0) → C(n) by equations of motion (§1.3)
  at every step: forces from P, F, W, Rv; drift from s
  at every step: invariants L1–L6 checked; violations abort the branch

OUTPUT:
  one lawful critique trajectory
  plus its full run record: forces applied, invariants checked,
  world state used, receiver coupling, trajectory hash

NOTE:
  Nothing in the pipeline optimizes for "good."
  Goodness is not a force. It is, at most, a post-hoc measurement
  performed by receivers — which is exactly L6.
```

### 4.3 Why This Satisfies the Intention

The stated goal: *not* protocols defined to achieve an end goal, but a law-based system that, combined with the other protocols, creates dynamic, infinite, yet protocol-bound results.

- **No end goals**: definitions carry properties, not targets; the generator contains zero output specifications. Nothing in P or F says what the critique should conclude.
- **Dynamic**: trajectories are computed under time-varying boundary conditions (W(t) never repeats) and stochastic drift (no two runs identical).
- **Infinite**: the lawful trajectory space is combinatorially unbounded; new personas, formats, periods, and receivers all extend it without changing the laws.
- **Protocol-bound**: L1–L6 hold on every trajectory without exception. The laws are the protocol. Anything outside them is not in this system.

### 4.4 What Emergence Buys

Because outcomes are computed rather than stored, the system can produce critiques that were never designed: a Kael definition under 1890s salon boundary conditions; a format built for television recaps applied to an oral epic with the receiver model of a Homeric audience; two incompatible persona definitions run as a composite trajectory to locate lawful disagreement (where their standards genuinely conflict) versus mere noise. The narratological suite already asks "what would two incompatible craft traditions agree on?" — this generalizes that question from craft to the entire circuit.

---

## 5. Repository and Package Structure (Proposal)

Following the narratological repo pattern (specs + packages):

```
discourse-world/  (world component)
  specs/
    01-primary-sources/        # historical criticism records, period authority maps
    02-field-studies/         # one study per period/ecosystem (salon, print, platform)
    03-structured-data/       # JSON extracts, house schema
    04-templates/
    08-protocol-framework/
  packages/
    core/    # field_state, anachronism, lineage, saturation, circulation
    cli/     # world field 1890-paris, world lineage <claim>

discourse-receiver/  (receiver component)
  specs/
    02-community-studies/     # one study per interpretive community
    03-structured-data/
  packages/
    core/    # horizon, implied_receiver, reception_distribution, displacement, impedance
    cli/     # receiver horizon <community> <t>

generative-core/  (the law layer)
  packages/
    core/    # definition loader, equations of motion, invariant gates (L1–L6), trajectory records
    cli/     # generate --persona kael --format essay-900 --world 1965-nyc --receiver cahiers --seed s
```

The law layer is deliberately the smallest package: laws should be few, exact, and rarely extended. Definitions and field studies are where the corpus grows — infinitely extensible content, fixed laws.

---

## 6. Open Questions

1. **Composite trajectories**: when two personas share a trajectory, are both postures held simultaneously (L5 requires explicit stitching) or does the format define handoff points?
2. **World-state granularity**: is W(t) discrete (period snapshots) or continuous (interpolated)? Period snapshots are tractable; interpolation risks inventing fields that never existed.
3. **Receiver ethics**: simulated receivers model real communities; displacement predictions about real people need the same epistemic honesty the text analysis component applies to its scores — pattern indicators, not psychometric truth.
4. **The drift term**: how much stochasticity before a trajectory stops being recognizable as its persona? Likely an eighth conservation law: persona recognizability (couplings and thresholds must remain detectable in the output).
5. **Where goodness lives**: the system refuses to define it (correctly, per L6 and the framework's separation of classification from verification). But users will ask. The answer should stay: goodness is a measurement performed by receivers, and the receiver component can measure it — never the generator.

---

## Sources

- [narratological-algorithmic-lenses](https://github.com/4444J99/narratological-algorithmic-lenses) — study structure (axioms, algorithms, diagnostics, JSON extracts) and the two-traditions question generalized in §4.4
- [linguistic-atomization-framework](https://github.com/4444J99/linguistic-atomization-framework) — heuristic-honesty posture applied to receiver modeling in §6.3
- [vox--architectura-gubernatio](https://github.com/4444J99/vox--architectura-gubernatio) — worksheet-to-rule pipeline as precedent for definition extraction
- The Discourse About Art framework (this project) — seven-slot coordinate space, five circuit roles, five discourse acts, region fidelity vs. citation verification separation, which become L1–L6
