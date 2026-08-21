---
origin: logically-derived
not_an_effect_entry: true
updated: 2026-08-20
---

# Shared-requirement audit

Which designs share a requirement, and whether they share a **number** or only a **kind**.  
Derived from `design_requirement` ⋈ `requirement`. Status is curated, not computed.

The tables below are the structural join. Plain-language descriptions of every requirement, in the same grouping, are at the end under [What these requirements are saying](#what-these-requirements-are-saying).

---

## Same kind, not the same number

### `thermal-cliff` — spec, satisfied, 7 designs

anisotropy-latch · polar-latch · gapped-condensate · chargeless-superflow · oscillator-grid · exchange-pin · phase-space-condensate (should)

| Design | The actual cliff |
|---|---|
| anisotropy-latch | Host *T*<sub>C</sub> (Fe 1043 K; Nd₂Fe₁₄B ~585 K) |
| polar-latch | Ferroelectric *T*<sub>C</sub> (BaTiO₃ ~393 K) |
| gapped-condensate | Superconducting *T*<sub>c</sub> (Nb 9.25 K … YBCO ~92 K) |
| chargeless-superflow | *T*λ = 2.17 K |
| oscillator-grid | *T*<sub>m</sub> (ice 273 K … W 3695 K) |
| exchange-pin | *T*<sub>B</sub> of the pin, **not** FM *T*<sub>C</sub> |
| phase-space-condensate | *T<sub>c</sub>(n)* — density-set, not *T<sub>λ</sub>* or Curie |

**Audit.** Kinship is real (a thermal resource destroys the ordered / coherent / crystalline population). Equating the numbers is a mapping error. EM-LENR “blocking line” is this *kind*; it is not NdFeB’s 585 K.

### `connected-spatial-buffer` — spec, satisfied, 2 designs

collective-screening · gapped-condensate

| Design | Length class |
|---|---|
| collective-screening | Optical δ ~ 10–20 nm; RF skin can be µm–mm |
| gapped-condensate | London *λ* ~ 40–50 nm (elements) |

**Audit.** Same failure class (starve the responding depth). Not the same formula. Do not quote 10 nm as London *λ*.

### `latch-cell-is-the-cliff` — consistency, satisfied, 2 designs

anisotropy-latch · polar-latch

**Audit.** Shared logic: grain / polar volume is the cliff, sample envelope is capacity. Polar side has **no portable *KV*** yet. Using 30 nm NdFeB as a ferroelectric number is over-claim.

---

## Shared number (or a true zero)

### `zero-hold-power` — spec, satisfied, 6 designs

anisotropy-latch · polar-latch · gapped-condensate · chargeless-superflow · collective-screening · exchange-pin

**Audit.** The number is actually the same: **0 W** (or 0 extra W for the mirror; 0 V for a persistent current). That is the cleanest join in the layer. “Hold-power test” in applications means: does the signature survive after the drive is dark? `phase-space-condensate` imposes the opposite spec (`not-zero-hold-power`). Do not quote 0 W as a BEC number.

### `gate-is-single-particle` — spec, satisfied, 2 designs

energy-gate (must) · collective-screening (should, as contrast)

**Audit.** *N* = 1 is a positive spec of the gate and a **negative** spec of screening. Same row, opposite machines. Photoelectric *N* = 1 is `incompatible` with collective-screening and `entails` for energy-gate.

---

## Closures (open on purpose)

A number or mesoscale step is **located and taken**, not derived. Shared or single-design — same honesty.

| Requirement | Designs | What is still taken |
|---|---|---|
| `underived-penetration-depth` | screening (must), condensate (should) | δ, skin √, London *λ* |
| `mesoscale-coercivity` | anisotropy-latch (must), exchange-pin (should) | *H*<sub>c</sub> ≪ *H*<sub>a</sub>; Hex |
| `polar-depolarization-buffer` | polar-latch | *E<sub>c</sub>* / dead layer. Ferroelectric domains fill the *partition* slot; they do not close this buffer. |
| `pinning-after-hc1` | gapped-condensate | pinning landscape after first penetration |
| `fluxoid-increment-2e` | gapped-condensate | *Φ*<sub>0</sub> = *h*/2*e* |
| `gapped-name-loose` | chargeless-superflow | *ρ<sub>s</sub>(*T<sub>λ</sub>*)*, not 2Δ |
| `underived-gate-energy` | energy-gate | *φ*, *E<sub>g</sub>*, *I*, *E<sub>b</sub>* taken; 2*m<sub>e</sub>c*² is the identity |
| `melting-not-derived` | oscillator-grid | *T<sub>m</sub>*; Lindemann is a criterion |
| `underived-grid-couplings` | oscillator-grid | *C*, *λ<sub>s</sub>*, *d<sub>ij</sub>*, *α* |
| `no-universal-n` | ensemble-average | Statistical buffer only |
| `interface-exchange-underived` | exchange-pin | *J<sub>ex</sub>*, *T<sub>B</sub>*/*T<sub>N</sub>* |
| `underived-hall-quantum` | edge-channel | *R_K = h/e²* |
| `underived-conductance-quantum` | landauer-channel | \(2e^2/h\) |
| `phase-space-threshold-taken` | phase-space-condensate | \(n\lambda^3\simeq 2.612\) |

**Audit.** These are honest. Do not fill them with a guessed node count to make an application look closed.

---

## Tension, not a failed spec

### `bec-not-this-condensate` — consistency, **tension**, 3 designs

gapped-condensate (must) · chargeless-superflow (should) · phase-space-condensate (must)

**Audit.** Status `tension` stays: the leftover now has a home (`phase-space-condensate`) and still must not be folded into the pairing condensate or He-4. Do not “fix” the tension by inventing a gap or a 0 W hold.

---

## Predictions that are already library-true

| Requirement | Meaning for applications |
|---|---|
| `coupled-screening-failure` | A starved Ag film should lose *R*, SPR, go plasma-transparent, and lose conducting-plate Casimir contrast together |
| `average-replaced-by-order` | When a latch or gap opens, *χ* ~ 1/*T* and *γT* are the wrong readout |
| `split-r0-and-expulsion` | Type-II mixed state: *R* = 0 can outlive *χ* = −1 |
| `qpc-is-not-this-edge` | A 1D constriction’s `2e²/h` steps are not a Hall plateau |
| `hall-gap-not-pairing` | Landau / mobility gap is not 2Δ |
| `coupled-grid-loss` | Shear speed, crystal *κ*, and Mössbauer *f* fail together at *T*<sub>m</sub> |

Use these as **coupled tests**, not as extra knobs.

`coupled-grid-loss` is imposed only by `oscillator-grid`. The number is each host’s *T*<sub>m</sub> (ice 273 K … W 3695 K). It is the same *kind* as `thermal-cliff`, not Curie, *T*<sub>λ</sub>, or *T<sub>c</sub>(n)*.

---

## Single-design specs

Satisfied specs that sit on one machine (or on one machine plus a contrast). Not a shared number.

| Requirement | Design | Idea |
|---|---|---|
| `chargeless-no-london-lambda` | chargeless-superflow | No *λ*, no *χ* = −1 in ⁴He |
| `finite-mode-count` | oscillator-grid | 3*N* modes; nothing above *ω<sub>D</sub>* |
| `pair-needs-recoil-partner` | energy-gate | Pair channel closed in empty space |
| `not-zero-hold-power` | phase-space-condensate | Trap + cool; opposite of 0 W |
| `two-dimensional-electron-buffer` | edge-channel | 3D metal is the wrong buffer |
| `edge-path-after-bulk-gap` | edge-channel | Bulk gapped ⇒ current on the edge |
| `no-perpendicular-b-required` | landauer-channel | 2*e*²/*h* steps need no Landau ladder |

---

## Other consistencies

Satisfied consistency rows that are not the latch-cell or BEC-tension items above.

| Requirement | Design | Idea |
|---|---|---|
| `one-plasma-clock` | collective-screening | One *ω<sub>p</sub>* class per metal for *R*, skin, and the plasma edge |
| `shared-surface-phi` | energy-gate | Photoelectric and thermionic *φ* are one gate |
| `shared-crystal-eg` | energy-gate | Absorption and photocurrent share *E<sub>g</sub>* |
| `defined-constants-not-extracted` | ensemble-average | *k* and *σ* are defined SI constants |
| `nested-pin-not-parent-latch` | exchange-pin | Collapse is *T<sub>B</sub>*, not FM *T<sub>C</sub>* |

---

## What this audit forbids in application files

- Quoting one thermal number across latch, superfluid, melt, and pin.
- Treating H/M or sample mass as a latch-cell cliff.
- Calling London *λ* the optical skin.
- Filing QHE or BEC as `gapped-condensate` members.
- Filing a quantum point contact as `edge-channel` (or quoting `2e²/h` as *R_K*).
- Closing *R_K* or \(2e^2/h\) with a Chern-number / Landauer derivation story.
- Quoting \(T_c(n)\) as \(T_\lambda\) or as a 0 W latch number.
- Treating defined *k* or *σ* as extracted machine constants.
- Identifying *E<sub>c</sub>* with *φ*, or *R<sub>Q</sub>* with *R<sub>K</sub>*.
- Quoting *T<sub>m</sub>* as Curie or as *T<sub>λ</sub>*.
- Filing pyroelectric D–D neutrons or a 2.224 MeV *γ* as a muon-catalyzed cycle.

---

## What these requirements are saying

The tables above are the join. This section spells out the idea of each requirement in the same grouping. A requirement is a demand visible only at **design** grain — not a restatement of one library sentence. Status is curated: `satisfied` means the demand is located; `open` means a number or step is still taken; `tension` is an honest leftover.

Single-design specs and the remaining consistencies have their own tables and matching subsections below.

### Same kind, not the same number

#### `thermal-cliff`

Several machines die when a critical temperature destroys the ordered, coherent, or crystalline population they use. That kinship is real. The **numbers** are not: Curie of NdFeB, ferroelectric *T<sub>C</sub>*, superconducting *T<sub>c</sub>*, the λ-point, melting, and a pin’s *T<sub>B</sub>* are different cliffs. Applications may speak of “a thermal cliff”; they may not quote 585 K as a helium or melt figure.

#### `connected-spatial-buffer`

The machine needs a connected responding depth of order its own screening or coherence length. Starve that depth and the collective output collapses. Optical *δ* (~10–20 nm) and London *λ* (~40–50 nm in elements) are the same *failure class*, not the same formula. Do not call 10 nm a London depth.

#### `latch-cell-is-the-cliff`

For a latch, the sharp hardware cliff is the grain or polar volume that can hold the barrier against *kT*. The sample envelope (the magnet in the hand, the ceramic disk) is capacity. The magnetic side has a portable ~30 nm / 25 *kT* contour (timescale, not a universal energy). The polar side does not yet have an equivalent *KV*. Using NdFeB’s 30 nm as a ferroelectric number is over-claim.

### Shared number (or a true zero)

#### `zero-hold-power`

Once written, expelled, or circulating, the state costs **0 W** (0 extra W for a mirror; 0 V for a persistent current) to keep. Energy is spent on write/erase or on the incident drive. This is the cleanest shared number in the layer. A “hold-power test” asks whether the signature survives after the drive is dark. The dilute BEC is the opposite spec (`not-zero-hold-power`).

#### `gate-is-single-particle`

One conversion event needs one node. No collective film is required for the gate to open. That is a positive spec of `energy-gate` and a negative spec of `collective-screening`. Photoelectric *N* = 1 is incompatible with the screening machine.

### Closures (open on purpose)

These name a number or step that is **located and taken**, not derived from a more primitive node rule. Do not invent a node count to make an application look closed.

#### `underived-penetration-depth`

Optical *δ* = *λ*/4*πk*, classical skin √(2/*ωμσ*), and London *λ* are how the screening / expulsion buffer is located. The formulas are taken. Same honesty on the mirror and on Meissner.

#### `mesoscale-coercivity`

Technical *H<sub>c</sub>* is not the anisotropy field *H<sub>a</sub>*. Nucleation, grain boundaries, and dipolar coupling sit between the unit-cell barrier and the bulk force. *H*<sub>ex</sub> lives in the same mesoscale band. The latch is located; the write-field spec is not.

#### `polar-depolarization-buffer`

*E<sub>c</sub>* and the depolarization field of a thin ferroelectric are mesoscale. Electrical twin of `mesoscale-coercivity`. The polar latch is located; the write-field / dead-layer spec is not. [`ferroelectric-domains`](../ferroelectric-domains.md) fills the partition slot (nm-class walls, field-expelled pattern); it does not close this buffer.

#### `pinning-after-hc1`

Why *R* = 0 survives between *H<sub>c1</sub>* and *H<sub>c2</sub>* is a pinning landscape. The condensate machine does not yet have a buffer/barrier spec for that step.

#### `fluxoid-increment-2e`

The measured increment in *Φ*<sub>0</sub> = *h*/2*e* and in the Josephson lock is 2*e*. Taken as data. Origin of 2*e* versus *e* is not derived here.

#### `gapped-name-loose`

⁴He collapse is loss of *ρ<sub>s</sub>* at *T<sub>λ</sub>* (and of superflow at *v<sub>c</sub>*), not a spectroscopic pairing gap. The family assignment is by a critical-temperature protected mode, not by identifying a gap.

#### `underived-gate-energy`

*φ*, *E<sub>g</sub>*, *I*, and shell binding energies are located as gates and are taken. Pair production’s 2*m<sub>e</sub>c*² is the clean rest-mass identity in this family.

#### `melting-not-derived`

*T<sub>m</sub>* and the loss of Bragg / shear order are located. Lindemann is a criterion, not a derivation of *T<sub>m</sub>* from node rules.

#### `underived-grid-couplings`

Moduli, magnetostriction *λ<sub>s</sub>*, piezo *d<sub>ij</sub>*, and thermal expansion *α* are taken handbook couplings of the same grid. The grid and its collapses are located; the coupling magnitudes are not derived.

#### `no-universal-n`

The ensemble-average machine names a statistical buffer (1/√*N*, Kn, a Fermi-surface slice) and refuses a single node-count cliff analogous to a 10 nm film. That refusal *is* the family-wide Medium mapping.

#### `underived-hall-quantum`

*R<sub>H</sub>* = *h*/*νe*² is taken from metrology. QSA does not obtain *R<sub>K</sub>* from a buffer or node-count rule. Do not close it with a Chern-number story.

#### `underived-conductance-quantum`

*G* = *n* × 2*e*²/*h* is taken from Landauer / metrology. Twin of `underived-hall-quantum`. Do not equate 2*e*²/*h* with *R<sub>K</sub>*.

#### `phase-space-threshold-taken`

The BEC critical line *nλ*<sub>th</sub>³ ≃ 2.612 is taken from the ideal-gas condition. Same honesty as the penetration-depth closure.

#### `interface-exchange-underived`

*H<sub>ex</sub>* and *T<sub>B</sub>*/*T<sub>N</sub>* remain interface- and grain-level data. The two-latch topology is located; *J<sub>ex</sub>* is not derived. Draft-design honesty.

### Tension, not a failed spec

#### `bec-not-this-condensate`

A dilute alkali BEC has a thermal/density cliff and quantized winding but no measured pairing gap and is not held at 0 W. It must not be folded into `gapped-condensate`. It now has a home (`phase-space-condensate`) and still must not be folded into ⁴He either. Status stays `tension`: the leftover is named; the family word “gapped” is still loose. Do not “fix” it by inventing a gap or a 0 W hold.

### Predictions that are already library-true

Use these as **coupled tests**, not as extra knobs.

#### `coupled-screening-failure`

A film starved in connected thickness should lose ordinary reflectivity, go transmitting toward and above the plasma edge, lose a Kretschmann SPR dip, and lose conducting-plate Casimir contrast in the same window. If one artifact dies and a sibling in that list survives, the “one screening population” assembly is wrong.

#### `average-replaced-by-order`

When a latch or a gap opens, the original contributing population is no longer the one being averaged. Curie *χ* ~ 1/*T* and electronic *γT* are then the wrong readout.

#### `split-r0-and-expulsion`

Zero resistance and complete field expulsion are related artifacts with different failure envelopes. A type-II mixed state can keep *R* = 0 after *χ* = −1 has failed, if vortices are pinned.

#### `qpc-is-not-this-edge`

A ballistic 1D constriction with 2*e*²/*h* steps and no perpendicular *B* is not the gapped-2D edge that outputs *R<sub>H</sub>* = *h*/*νe*². Same *h*, *e* bricks; different machine.

#### `hall-gap-not-pairing`

The Landau / mobility gap that protects a Hall plateau is not a superconducting pairing gap and is not Meissner expulsion.

#### `coupled-grid-loss`

Shear speed, crystal phonon *κ*, and Mössbauer recoilless *f* fail together at *T<sub>m</sub>* when the grid stops being a grid. Liquid longitudinal sound and liquid heat transport are different channels. Imposed only by `oscillator-grid`. The number is each host’s melt point — same *kind* as `thermal-cliff`, not Curie or *T<sub>λ</sub>*.

### Single-design specs

#### `chargeless-no-london-lambda`

Chargeless superflow has no electromagnetic screening length and no Meissner expulsion. Demanding London *λ* of ⁴He is a category error.

#### `finite-mode-count`

A grid of *N* ions has 3*N* mechanical modes and a spectral ceiling. There is no oscillator above *ω<sub>D</sub>*.

#### `pair-needs-recoil-partner`

Above 1.022 MeV, pair production still fails without a nearby nucleus (or other momentum sink). Second hardware clause, twin of “no muon ⇒ μCF closed.”

#### `not-zero-hold-power`

Holding a dilute condensate requires continuous cooling and trapping. Treating it as a 0 W latch is a category error. Positive negative of `zero-hold-power`; imposed only by `phase-space-condensate`.

#### `two-dimensional-electron-buffer`

Integer Hall plateaus need a 2D electron system. A bulk 3D metal in the same *B* is the wrong buffer. Graphene integer plateaus sit on the same 2D plus gap-versus-*kT* clause.

#### `edge-path-after-bulk-gap`

Once the field opens a gap in the bulk of the 2DEG, the surviving current path is along the edges. That architecture is recorded. Why current is expelled to the edge, and why that forces *R<sub>H</sub>* onto *R<sub>K</sub>/ν*, is the companion closure `underived-hall-quantum`.

#### `no-perpendicular-b-required`

Integer 2*e*²/*h* steps persist at zero or in-plane *B*. Demanding a Landau ladder or a Hall geometry of a quantum point contact is a category error. The split from `edge-channel`.

### Other consistencies

#### `one-plasma-clock`

Reflection, skin effect, and plasma-frequency cutoff share one *ω<sub>p</sub>* (or interband-shifted optical edge) class for a given metal. A later mapping that needs a second independent clock for the same film puts this row in tension.

#### `shared-surface-phi`

Photoelectric and thermionic conversion on the same crystal face, in the same contamination state, share one work-function class. Do not identify *φ* with the optical plasma edge.

#### `shared-crystal-eg`

Semiconductor gap absorption and photoconductivity in the same crystal share one *E<sub>g</sub>*, read as opacity or as current.

#### `defined-constants-not-extracted`

*k* and *σ* are defined SI constants. Treating them as QSA-extracted machine numbers over-claims.

#### `nested-pin-not-parent-latch`

Exchange-bias collapse is *T<sub>B</sub>* of the AFM pin, not the FM Curie point. Treating *H<sub>ex</sub>* as just another name for *H<sub>a</sub>* hides the bilayer hardware. This is why `exchange-pin` is its own design.
