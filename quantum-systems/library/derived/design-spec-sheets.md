---
origin: logically-derived
not_an_effect_entry: true
updated: 2026-08-20
---

# Design spec sheets

Pulled from `design` rows and from `design_implication` where `relation = entails`.  
These are assembly commitments, not new measurements. The inside of each cliff is restated in [operating-envelopes.md](operating-envelopes.md). Constituents are in [node-types.md](node-types.md).

Each sheet is one reverse-engineered machine: the smallest hardware that still produces the macro output, the clock it must keep, any barrier that protects a written state, what it costs to hold, and the erase that kills the output. Shared *kinds* of demand (a thermal cliff, a spatial buffer, a true 0 W hold) are audited in [requirement-audit.md](requirement-audit.md). Do not copy one sheet’s number onto another machine.

---

## collective-screening

A connected charged population that screens an incoming field and re-radiates it. That is a visible mirror, an RF skin, a plasma-edge cutoff, and the conducting faces of a Casimir gap. The machine is **driven**, not a memory: there is no stored bit when the incident field is gone. Starve the connected thickness (island film, ≲ 5–10 nm continuous Ag/Al) or drive faster than the plasma / interband clock and the collective output dies. One electron leaving a surface is a different machine (`energy-gate`).

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | Connected metal / polarizable volume of order the optical penetration or RF skin depth | 10–20 nm Ag/Al optical; classical δ = √(2/ωμσ) at low ω |
| Clock | Plasma period / ωp (or Ag interband-shifted optical edge) | Al ~15 eV; Ag edge ~3.9 eV; period ~0.3–0.5 fs |
| Barrier | None that stores a state. Operating window: ω < ωp and a continuous film ≳ δ | Driven, not latched |
| Hold-power | Zero *extra* watts beyond the incident field | Mirror is not a lamp |
| Dominant erase | Thickness / percolation ≲ 5–10 nm, or drive above the plasma / interband edge | Two routes, one machine |
| Open | δ and √(2/ωμσ) are taken, not derived from a node count | `underived-penetration-depth` |

Incompatible with “this hardware is N = 1 electron” (that is `energy-gate` / photoelectric). Island or plasma-transparent faces also starve conducting-plate Casimir contrast.

---

## anisotropy-latch

A grain that keeps a direction of magnetization after the writing field is removed, at **zero continuous power**. The cliff is the grain’s anisotropy energy versus thermal kicks (*KV* above a timescale contour), not the size of the part in the hand. Sample envelope is capacity. Heat through Curie, shrink through the superparamagnetic line, or destroy the lattice and the held direction is gone. Unlocked Curie *χ* is the population this latch *replaces*, not its barrier.

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

The electrical twin of the anisotropy latch: remnant polarization at *E* = 0, still 0 W hold. The barrier is a lattice-locked double well below the ferroelectric Curie point. There is not yet a portable grain-size number analogous to NdFeB’s ~30 nm. A large polar body partitions; walls are a measured nm-class buffer, and a field can expel the pattern while remanent *P* remains. Charged walls need screening (the electrostatic extra vs magnetism). A pyroelectric temperature ramp on this crystal can write a high face voltage; that field engine dies at the host *T*<sub>C</sub> even if deuterium is still present.

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | Polar grain / film thick enough to stand depolarization; a large body partitions (nm-class walls) | Process-dependent; no portable ferroelectric *KV* yet |
| Clock | Ionic / soft-mode class (THz), write is *P*–*E* sweep / wall motion | Not a hold clock |
| Barrier | Lattice-locked double well below *T*<sub>C</sub> | Write at *E*<sub>c</sub> |
| Hold-power | 0 W at *E* = 0 | Remanent *P*; static domain pattern |
| Dominant erase | *T* > *T*<sub>C</sub>; *E* > *E*<sub>c</sub>; volume too small; *E* can also expel walls without killing *P<sub>r</sub>* | BaTiO₃ *T*<sub>C</sub> ≈ 393 K; LiTaO₃ ~890 K |
| Open | *E*<sub>c</sub> / dead layer | Electrical twin of mesoscale coercivity |

A pyroelectric D–D neutron burst dies with the host *T*<sub>C</sub> even if deuterium remains. Filing ferroelectric domains does not close `polar-depolarization-buffer`.

---

## gapped-condensate

A charged superconducting condensate. Zero resistance and complete field expulsion are related artifacts of one machine with **different erase lines**: in type II, *R* = 0 can outlive *χ* = −1 if vortices are pinned. The spectroscopic gap closes at a material *T*<sub>c</sub>. This is not a dilute alkali cloud and not an integer Hall plateau.

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

Liquid ⁴He below the λ-point: superflow and a fountain / superleak without electric charge. No London depth, no Meissner expulsion, no Josephson voltage–frequency lock. Circulation is quantized as *h*/*m*₄, not *h*/2*e*. The 2.17 K cliff is not the density-set *T<sub>c</sub>* of a trapped alkali cloud.

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | Connected ⁴He with nonzero *ρ*<sub>s</sub> | Superleak / film as apparatus filter |
| Clock | No *e*, no *V*–*ν* lock | Circulation quantum *h*/*m*₄ ≈ 9.97×10⁻⁸ m²/s |
| Barrier | *T*λ = 2.17 K; geometry-dependent *v*<sub>c</sub> | Loss of *ρ*<sub>s</sub>, not a pairing gap |
| Hold-power | Persistent circulation, 0 W | |
| Dominant erase | *T* > *T*λ; *v* > *v*<sub>c</sub>; solidification | |
| Open | Family name “gapped” is loose | `gapped-name-loose` |

No London *λ*. No *χ* = −1. *T*<sub>λ</sub> is not a dilute-cloud *T<sub>c</sub>(n)*.

---

## energy-gate

One discrete conversion at a time (*N* = 1): a photon above the work function, a crystal above *E<sub>g</sub>*, a pair above 2*m<sub>e</sub>c*², a muon opening a hydrogen well. The product leaves; this is not a latch. Under-threshold input is simply non-occurrence. Named gates are not interchangeable: *φ* is not *ω<sub>p</sub>*, charging *E<sub>c</sub>* is not *φ*, a 2.224 MeV *γ* is not a muon, and pyroelectric neutrons do not die with *τ<sub>μ</sub>*.

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | **N = 1** for one conversion | Escape depth / avalanche path are sequels |
| Clock | Attosecond to optical-cycle opening | Rate ≠ latency |
| Barrier | *φ*, *E*<sub>g</sub>, *I*, shell *E*<sub>b</sub>, 2*mₑc*², or the muon-rescaled hydrogen well | *φ* ~ 2–6 eV; Si *E*<sub>g</sub> ≈ 1.12 eV; H *I* = 13.598 eV; pair 1.022 MeV; μCF needs a muon |
| Hold-power | Not a latch; the product leaves | |
| Dominant erase | Under-threshold input (non-occurrence) | Pair production also needs a recoil partner; μCF also needs a muon |
| Open | Most gate energies taken, not derived | Pair 2*mₑc*² is the clean identity |

*φ* is not *ω*<sub>p</sub>. Same face should share *φ* for photo and thermionic. *E<sub>c</sub>* is not *φ*. A photodisintegration photon is not a muon. Pyroelectric neutrons do not die with *τ<sub>μ</sub>*. *R<sub>Q</sub>* is not *R<sub>K</sub>*.

---

## oscillator-grid

The crystal as a finite set of coupled mechanical oscillators (3*N* modes, a Debye ceiling). Allowed clocks are the measured phonon branches. There is no stored configuration unless some other machine latches on this grid. Melting takes the grid away: shear sound, crystal phonon heat current, and Mössbauer recoilless fraction fail together. A liquid still carries a longitudinal speed.

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | Ordered ion grid; 3*N* modes | No single nm cliff for *ω*(**q**) |
| Clock | Measured phonon branches, few–tens of THz | Long-wave *v*<sub>s</sub> = √(*C*/*ρ*) |
| Barrier | None that stores a configuration (except as host to a latch) | |
| Hold-power | n/a | |
| Dominant erase | *T* → *T*<sub>m</sub> (Bragg gone, *G* → 0); yield / fracture; *ω* > *ω*<sub>D</sub> | Ice 273 K; Al 933 K; W 3695 K |
| Open | *T*<sub>m</sub> and moduli / *λ*<sub>s</sub> / *d* / *α* taken | Lindemann is a criterion |

Shear sound, crystal phonon *κ*, and Mössbauer *f* die together at melt; a liquid still carries a longitudinal speed. The 14.4 keV line is the payload, not an under-threshold gate.

---

## ensemble-average

A stable macroscopic number or spectrum that exists only as the average of a large population: temperature, ideal-gas pressure, the Planck curve, *γT* electronic heat, Johnson noise, Curie *χ*. The buffer is statistical (1/√*N*, a Knudsen number, a Fermi-surface slice). There is **no** universal node-count cliff. A latch or a gap does not sit on this average; it *replaces* the contributing population.

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

A second latch that pins the first: an antiferromagnet at an interface writes a unidirectional loop shift *H*<sub>ex</sub> on a ferromagnet and holds that shift at 0 W. Collapse is the pin’s blocking temperature *T*<sub>B</sub> (≤ *T<sub>N</sub>*), not the FM Curie point — remanence of the parent latch can remain. A superparamagnetic FM grain has nothing to pin. Draft until more bilayer implications exist.

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

A two-dimensional electron system in a perpendicular field. Once the field opens a gap in the bulk, surviving current runs on the edge and the Hall resistance locks to *R<sub>K</sub>/ν*. That lock is a driven DC plateau, not a 0 W latch. Rotate *B* in-plane, walk off a filling, overrun the gap, or lose the 2DEG and the plateau is gone. A ballistic 1D constriction with no field (`landauer-channel`) is contrast, not a member. *R<sub>K</sub>* is taken. Draft until a second core effect (QSHE / QAHE) is filed.

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | 2DEG; after the bulk is gapped, current lives on the edge | 3D metal is the wrong buffer; *ℓ_B* = √(ℏ/*eB*) |
| Clock | Cyclotron *ω_c = eB/m* | Same combination as cyclotron resonance; output is DC |
| Barrier | Landau / mobility gap | Perpendicular *B* opens the ladder |
| Hold-power | n/a — driven DC plateau, not a latch | Do not attach `zero-hold-power` |
| Dominant erase | Off-plateau *ν*; in-plane *B*; *kT* or Hall field vs gap; lost 2DEG | Graphene high-*T* integer plateaus sit on the same gap-vs-*kT* clause |
| Open | *R_K = h/e²* taken; why the edge path forces *R_H* is not derived | `underived-hall-quantum` |

Integer QHE is the core artifact. A 1D constriction (`2e²/h`, no *B*) is contrast (`landauer-channel`). The cyclotron *m\** line is the same *eB/m* combination, not this plateau. *R<sub>Q</sub>* as a tunnel floor is not *R<sub>K</sub>*. Fractional plateaus stay out. Draft until a second core effect (QSHE / QAHE) is filed.

---

## phase-space-condensate

A dilute trapped atomic cloud that macroscopically occupies one mode once the phase-space density crosses the taken ideal-gas line *nλ*<sub>th</sub>³ ≃ 2.612. Holding it needs continuous cooling and trapping — the opposite of a 0 W latch. Turn the trap off and the laboratory condensate is gone. This is not helium-4 superflow (no fountain / superleak), not a pairing condensate, and not Meissner. *T<sub>λ</sub>* is not *T<sub>c</sub>(n)*. Draft.

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | Phase-space density \(n\lambda_{\mathrm{th}}^3 \simeq 2.612\) | Taken ideal-gas line; \(N\sim 10^3\)–\(10^7\) is a working envelope |
| Clock | Trap frequencies (apparatus) | No \(2e/h\) lock |
| Barrier | \(T_c(n)\) / critical density | Not a pairing gap; not *KV* |
| Hold-power | Continuous trap + cool | `not-zero-hold-power` |
| Dominant erase | \(T > T_c(n)\); density drop; trap loss | Same cliff two ways |
| Open | \(2.612\) taken; family name still loose | `phase-space-threshold-taken` |

Contrast: pairing condensate, He-4 fountain/superleak, 0 W latch, Meissner / London *λ*. Trap off ⇒ laboratory condensate gone. *T<sub>λ</sub>* is not *T<sub>c</sub>(n)*. Draft.

---

## landauer-channel

A short, clean constriction in a 2DEG reservoir, about a Fermi wavelength wide. Each occupied 1D mode contributes a taken 2*e*²/*h*. No perpendicular field is required; pinch-off, thermal smear, or a dirty/long channel kills the staircase. This is not a Hall plateau and not a Coulomb-blockade diamond pattern. Draft because one constriction file owns it.

| Spec | Commitment | Source class |
|---|---|---|
| Buffer | Ballistic constriction, width \(\sim\lambda_F\), \(L <\) mfp | 2DEG is the reservoir, not the Hall buffer |
| Clock | Fermi transit through the saddle | DC staircase |
| Barrier | 1D subband edges | Pinch-off closes the last mode |
| Hold-power | n/a — driven conductance | Not a latch |
| Dominant erase | Pinch-off; \(kT\) smears subbands; dirty / long channel | No *B* required |
| Open | \(2e^2/h\) taken; 0.7 feature out of scope | `underived-conductance-quantum` |

Contrast: `edge-channel` Hall plateau. Steps persist at *B* = 0. Charging diamonds are a different machine. Draft.
