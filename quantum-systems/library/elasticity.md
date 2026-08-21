---
id: elasticity
title: Elasticity (Small-Strain Restoring Output)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
confidence_data: high
confidence_mapping: medium
related:
  - speed-of-sound
  - phonon-dispersion
  - melting
  - piezoelectricity
  - magnetostriction
  - thermal-expansion
  - ferromagnetic-hysteresis
  - ferroelectric-domains
updated: 2026-08-20
---

# Elasticity (Small-Strain Restoring Output)

### 4.1 Effect Name

Elasticity (small-strain restoring output)

### 4.2 Macroscopic Observation

A solid loaded below its yield point changes length or angle in proportion to the load and returns to the original shape when the load is removed. The constants of proportionality — Young’s, shear, and bulk moduli — are material handbook numbers. Above a yield stress the same solid flows plastically or fractures and does not recover. A liquid has a bulk modulus but no static shear modulus: it supports compression and not a lasting shear stress.

### 4.3 Established Quantitative Boundaries

- Hooke’s law holds only at small strain. In ordinary metals the reversible window is a strain of order \(10^{-3}\) or less; polymers and elastomers are a different, large-strain machine and are not this lattice-spring entry.
- Handbook class, room temperature: steels \(E \approx 200\,\mathrm{GPa}\); aluminum \(E \approx 70\,\mathrm{GPa}\); diamond \(E \sim 10^3\,\mathrm{GPa}\). Shear and bulk moduli are the same class of measured stiffnesses. Water’s bulk modulus is the \(C\) that gives \(v_s \approx 1480\,\mathrm{m\,s^{-1}}\) at \(\rho \approx 10^3\,\mathrm{kg\,m^{-3}}\) (`speed-of-sound`).
- Yield / fracture: mild steels yield at hundreds of MPa, far below \(E\). The conventional ideal-strength estimate \(E/10\) therefore sits one to two orders of magnitude above real metallic yield. That gap is the mesoscale dislocation / microstructure step — the mechanical analogue of coercivity versus anisotropy field in `ferromagnetic-hysteresis`.
- Static shear modulus \(G\to 0\) on melting (`melting`). The liquid keeps a bulk modulus.
- The long-wave speeds are \(v = \sqrt{C/\rho}\) for the appropriate \(C\). Elasticity and `speed-of-sound` are the same springs read as a modulus or as a slope.

**Data confidence:** High — moduli of common crystals and the existence of a yield / fracture envelope are handbook. A particular alloy’s yield stress is medium (processing-dependent). The \(E/10\) ideal-strength figure is a conventional estimate, not a measured cliff.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Small-strain Hooke (isotropic form shown; crystals are tensors):

  \[
  \sigma_{ij} = C_{ijkl}\,\varepsilon_{kl}
  \]

  Young’s modulus \(E\), shear modulus \(G\), bulk modulus \(K\), and Poisson ratio \(\nu\) are contractions of \(C_{ijkl}\) used as engineering coordinates.

- Wave speeds from the same \(C\):

  \[
  v_L = \sqrt{\frac{K+4G/3}{\rho}}, \qquad v_T = \sqrt{\frac{G}{\rho}}
  \]

- Failure envelope (descriptive, not derived here): plastic yield when the resolved shear stress on a slip system exceeds a microstructure-set threshold; brittle fracture when a crack-tip field exceeds a toughness. Neither threshold equals the ideal \(E/10\) bond-breaking stress in real metals.

- Harmonic lattice: \(C\) independent of strain amplitude and of volume to first order. Real \(C(T)\) and thermal expansion require anharmonicity (`thermal-expansion`).

This description records the linear output and names the yield envelope. It does not compute a yield stress from the unit cell.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A mechanically coupled grid (or, for \(K\) only, a fluid density field). The *linear* modulus is already a bulk average of the same springs whose long-wave slope is \(v_s\). The *yield* envelope is not set by that unit-cell spring: it requires a mesoscale population of dislocations, grain boundaries, or cracks. There is no single nanometre cliff for \(E\) itself; the sharp additional buffer is the defect structure that writes plasticity.

- **Clock rate / latency.** Reversible elastic response tracks the acoustic / Debye clocks of the grid (`speed-of-sound`, `debye-cutoff`): microscopic restoration is fast compared with ordinary mechanical tests. Plastic flow is slower and rate-dependent; that latency belongs to defect motion, not to the harmonic spring.

- **Energy barriers or thresholds.** Small-strain elasticity is a restoring well, not a latch: stored energy \(\frac12 C\varepsilon^2\) is returned on unload. Yield is a threshold on that well’s useful range. In crystals the microscopic barrier being crossed is a dislocation Peierls / pinning barrier — measured as a yield stress, not yet specified here as a \(KV\)-style node number.

- **Dominant failure modes.**
  - Stress: load above yield → plastic set; above fracture toughness → separation. The linear emergent output is gone.
  - Thermal / grid: \(T\to T_m\) → \(G\to 0\); the solid elastic machine is gone (`melting`).
  - Medium: no shear couplings (fluid, vacuum) → no static shear modulus.
  - Amplitude: strain large enough that anharmonicity and geometric change leave the Hooke window → nonlinear elasticity, still reversible until yield.

- **Emergent constant or stable output.** Handbook moduli \(\{E, G, K\}\) as the synchronized small-amplitude restoring output of the coupled nodes, together with a material- and history-dependent yield / fracture envelope.

### 4.6 Internal Consistency Notes

Reading \(C\) and \(v_s\) as two coordinates on the same grid is tight. Filing yield with this entry is correct as a failure envelope and incomplete as a mapping: the mesoscale gap is the same kind of unfinished step noted for coercivity on `permanent-magnet-latch` / `ferromagnetic-hysteresis`. QSA does not yet have a clean buffer / barrier specification for dislocation nucleation and pinning. The Hookean output does not depend on closing it.

Elastomers (entropy-elastic, large reversible strain) share the word “elastic” and not this ion-grid machine. They should not be forced into the same \(C_{ijkl}\).

`piezoelectricity` and `magnetostriction` are couplings of this strain to polarization or to a magnetic moment. They inherit the small-strain window and the melting collapse; they do not replace this file.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the small-strain moduli and their identity with \(v_s=\sqrt{C/\rho}\) map cleanly onto the ion grid, but the load-bearing failure (yield / fracture) is set by a mesoscale defect population that is not yet reduced to a node-level barrier.

## Related entries

- [speed-of-sound](speed-of-sound.md) — the same \(C\) read as a long-wave slope
- [phonon-dispersion](phonon-dispersion.md) — finite-\(q\) extension of the same springs
- [melting](melting.md) — \(G\to 0\); the grid stops being a grid
- [piezoelectricity](piezoelectricity.md) — strain coupled to polarization
- [ferroelectric-domains](ferroelectric-domains.md) — 90° walls switch this strain with the polar partition
- [magnetostriction](magnetostriction.md) — strain coupled to ordered moment
- [thermal-expansion](thermal-expansion.md) — anharmonic correction to these wells
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — analog of the mesoscale write threshold (coercivity vs \(H_a\))
