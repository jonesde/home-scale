---
origin: logically-derived
not_an_effect_entry: true
updated: 2026-08-17
---

# Design spec sheets

Pulled from `design` rows and from `design_implication` where `relation = entails`.  
These are assembly commitments, not new measurements. The inside of each cliff is restated in [operating-envelopes.md](operating-envelopes.md). Constituents are in [node-types.md](node-types.md).

---

## collective-screening

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | Connected metal / polarizable volume of order the optical penetration or RF skin depth | 10–20 nm Ag/Al optical; classical δ = √(2/ωμσ) at low ω |
| Clock | Plasma period / ωp (or Ag interband-shifted optical edge) | Al ~15 eV; Ag edge ~3.9 eV; period ~0.3–0.5 fs |
| Barrier | None that stores a state. Operating window: ω < ωp and a continuous film ≳ δ | Driven, not latched |
| Hold-power | Zero *extra* watts beyond the incident field | Mirror is not a lamp |
| Dominant erase | Thickness / percolation ≲ 5–10 nm, or drive above the plasma / interband edge | Two routes, one machine |
| Open | δ and √(2/ωμσ) are taken, not derived from a node count | `underived-penetration-depth` |

Incompatible with “this hardware is N = 1 electron” (that is `energy-gate` / photoelectric).

---

## anisotropy-latch

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | Grain / cluster with *KV* above the thermal-escape line | NdFeB ~30 nm / 2.3×10⁻²⁶ m³ at ~25 *kT* (timescale contour) |
| Clock | Precession ~28 GHz/T; write is wall motion, not that carrier | γ/2π |
| Barrier | Magnetocrystalline or shape anisotropy, *K₁V* | *K₁* ≈ 4.5 MJ/m³ (Nd₂Fe₁₄B) |
| Hold-power | 0 W | Energy is the *M*–*H* loop area |
| Dominant erase | *T* > *T*<sub>C</sub>; *KV* too small; lattice shock | Curie / superparamagnetism / mechanical |
| Open | Technical *H*<sub>c</sub> ≪ *H*<sub>a</sub> is mesoscale | `mesoscale-coercivity` |

Sample size is capacity, not a second cliff. Unlocked Curie *χ* is not this barrier.

---

## polar-latch

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | Polar grain / film thick enough to stand depolarization | Process-dependent; no portable ferroelectric *KV* yet |
| Clock | Ionic / soft-mode class (THz), write is *P*–*E* sweep | Not a hold clock |
| Barrier | Lattice-locked double well below *T*<sub>C</sub> | Write at *E*<sub>c</sub> |
| Hold-power | 0 W at *E* = 0 | Remanent *P* |
| Dominant erase | *T* > *T*<sub>C</sub>; *E* > *E*<sub>c</sub>; volume too small | BaTiO₃ *T*<sub>C</sub> ≈ 393 K |
| Open | *E*<sub>c</sub> / dead layer | Electrical twin of mesoscale coercivity |

---

## gapped-condensate

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | *ξ* (coherence) and *λ* (London) as classes | *λ*(0) ~ 40–50 nm elements; *ξ* from µm (clean Al) to nm (cuprates) |
| Clock | Gap frequency ~2Δ/*h*; Josephson 483.6 MHz/µV | BCS 2Δ/*kT*<sub>c</sub> ≈ 3.52 is a fit |
| Barrier | Spectroscopic gap that closes at *T*<sub>c</sub> | Material *T*<sub>c</sub> (Nb 9.25 K; YBCO ~92 K) |
| Hold-power | Persistent current at zero continuous voltage | 0 V hold |
| Dominant erase | *T* > *T*<sub>c</sub>; *H* > *H*<sub>c</sub> / *H*<sub>c2</sub>; *I* > *I*<sub>c</sub> | Split: expulsion dies at *H*<sub>c1</sub> while *R* = 0 can remain |
| Open | Pinning after *H*<sub>c1</sub>; origin of the 2*e* increment | `pinning-after-hc1`, `fluxoid-increment-2e` |

Not a dilute BEC. Not integer QHE.

---

## chargeless-superflow

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | Connected ⁴He with nonzero *ρ*<sub>s</sub> | Superleak / film as apparatus filter |
| Clock | No *e*, no *V*–*ν* lock | Circulation quantum *h*/*m*₄ ≈ 9.97×10⁻⁸ m²/s |
| Barrier | *T*λ = 2.17 K; geometry-dependent *v*<sub>c</sub> | Loss of *ρ*<sub>s</sub>, not a pairing gap |
| Hold-power | Persistent circulation, 0 W | |
| Dominant erase | *T* > *T*λ; *v* > *v*<sub>c</sub>; solidification | |
| Open | Family name “gapped” is loose | `gapped-name-loose` |

No London *λ*. No *χ* = −1.

---

## energy-gate

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | **N = 1** for one conversion | Escape depth / avalanche path are sequels |
| Clock | Attosecond to optical-cycle opening | Rate ≠ latency |
| Barrier | *φ*, *E*<sub>g</sub>, *I*, shell *E*<sub>b</sub>, 2*mₑc*², or the muon-rescaled hydrogen well | *φ* ~ 2–6 eV; Si *E*<sub>g</sub> ≈ 1.12 eV; H *I* = 13.598 eV; pair 1.022 MeV; μCF needs a muon |
| Hold-power | Not a latch; the product leaves | |
| Dominant erase | Under-threshold input (non-occurrence) | Pair production also needs a recoil partner; μCF also needs a muon |
| Open | Most gate energies taken, not derived | Pair 2*mₑc*² is the clean identity |

*φ* is not *ω*<sub>p</sub>. Same face should share *φ* for photo and thermionic.

---

## oscillator-grid

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | Ordered ion grid; 3*N* modes | No single nm cliff for *ω*(**q**) |
| Clock | Measured phonon branches, few–tens of THz | Long-wave *v*<sub>s</sub> = √(*C*/*ρ*) |
| Barrier | None that stores a configuration (except as host to a latch) | |
| Hold-power | n/a | |
| Dominant erase | *T* → *T*<sub>m</sub> (Bragg gone, *G* → 0); yield / fracture; *ω* > *ω*<sub>D</sub> | Ice 273 K; Al 933 K; W 3695 K |
| Open | *T*<sub>m</sub> and moduli / *λ*<sub>s</sub> / *d* / *α* taken | Lindemann is a criterion |

Shear sound dies at melt; a liquid still carries a longitudinal speed.

---

## ensemble-average

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | Statistical: 1/√*N*, Kn = *λ*/*L*, or a Fermi-surface slice | **No universal *N*** |
| Clock | Exchange / collision / *kT*/*h* window | Observation faster than the window is not *T* |
| Barrier | None | A latch or gap *replaces* this population |
| Hold-power | n/a | |
| Dominant erase | Too few contributors; *T* → 0 for thermal noise; order or gap opens | |
| Open | *k* and *σ* are defined SI constants, not extracted | `defined-constants-not-extracted` |

---

## exchange-pin

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | AFM + FM + interface; Hex often ~1/*t*<sub>FM</sub> | Nested, not a single grain |
| Clock | Field-cool / block write | Not the FM Larmor hold clock |
| Barrier | Unidirectional *J*<sub>ex</sub> at the interface | |
| Hold-power | 0 W (loop shift held) | |
| Dominant erase | *T* > *T*<sub>B</sub> of the **pin** (*T*<sub>B</sub> ≤ *T*<sub>N</sub>), not FM *T*<sub>C</sub> | FM remanence can remain |
| Open | *J*<sub>ex</sub> / *T*<sub>B</sub>/*T*<sub>N</sub> taken | Draft design |

A superparamagnetic FM grain cannot hold Hex.

---

## edge-channel

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | 2DEG; after the bulk is gapped, current lives on the edge | 3D metal is the wrong buffer; *ℓ_B* = √(ℏ/*eB*) |
| Clock | Cyclotron *ω_c = eB/m* | Same combination as cyclotron resonance; output is DC |
| Barrier | Landau / mobility gap | Perpendicular *B* opens the ladder |
| Hold-power | n/a — driven DC plateau, not a latch | Do not attach `zero-hold-power` |
| Dominant erase | Off-plateau *ν*; in-plane *B*; *kT* or Hall field vs gap; lost 2DEG | Graphene high-*T* integer plateaus sit on the same gap-vs-*kT* clause |
| Open | *R_K = h/e²* taken; why the edge path forces *R_H* is not derived | `underived-hall-quantum` |

Integer QHE is the core artifact. A 1D constriction (`2e²/h`, no *B*) is contrast. Fractional plateaus stay out. Draft until a second core effect (QSHE / QAHE) is filed.
