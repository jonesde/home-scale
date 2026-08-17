---
id: magnetostriction
title: Magnetostriction (Moment–Strain Coupling)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
  - thermal
  - field-threshold
confidence_data: high
confidence_mapping: medium
related:
  - permanent-magnet-latch
  - ferromagnetic-hysteresis
  - elasticity
  - piezoelectricity
  - thermal-expansion
  - melting
  - magnetic-domains
updated: 2026-08-17
---

# Magnetostriction (Moment–Strain Coupling)

### 4.1 Effect Name

Magnetostriction (moment–strain coupling)

### 4.2 Macroscopic Observation

A ferromagnetic rod changes length when it is magnetized. Nickel shortens slightly; Terfenol-D lengthens by a much larger fraction. The length saturates with the magnetization and returns, with hysteresis, as the field is cycled. The effect is gone above the Curie point, where there is no ordered moment to couple to the lattice, and is gone if the lattice itself is destroyed. Applying a stress changes the magnetization (Villari / inverse effect): this is the mechanical path that can write or scramble a magnet without reaching \(T_C\).

### 4.3 Established Quantitative Boundaries

- Saturation magnetostriction \(\lambda_s = \Delta L/L\) at technical saturation, handbook class: Ni \(\lambda_s \sim 10^{-5}\) (negative); Fe is anisotropic (single-crystal \(\lambda_{100}\) and \(\lambda_{111}\) of opposite sign) with a small polycrystalline average, also \(10^{-5}\) class or smaller; Terfenol-D (Tb–Dy–Fe) \(\lambda_s\) in the \(10^{-3}\) class.
- Thermal collapse: \(\lambda \to 0\) as \(T\to T_C^-\) of the ordered magnet. Fe \(T_C \approx 1043\,\mathrm{K}\). Ni and Terfenol-D fail at their own, lower, Curie points. This is the same thermal cliff that erases net \(M\) on `permanent-magnet-latch`; this file owns the length change, not the latch.
- Mechanical collapse: plastic deformation, cracking, or melting removes the lattice that carries \(\Delta L\). Severe shock can also scramble the latch via this coupling without a bulk melt.
- Field: \(\lambda\) follows \(M(H)\) and saturates once the domain population is aligned (`magnetic-domains`, `ferromagnetic-hysteresis`). A small field on a hard magnet produces little \(\lambda\) until the write field is reached.
- Contrast: piezoelectric \(d_{ij}\) needs an inversion-free lattice and a charge; magnetostriction needs an ordered moment and a spin–lattice coupling. Centrosymmetric iron is magnetostrictive and not piezoelectric.

**Data confidence:** High — the Ni vs Terfenol-D class, the \(T_C\) collapse, and the existence of the inverse (stress–\(M\)) effect are multiply reproduced. A particular polycrystal’s \(\lambda_s\) is medium (texture- and stress-dependent).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Saturated linear strain along the magnetization, isotropic polycrystal form:

  \[
  \frac{\Delta L}{L} = \frac32 \lambda_s\bigl(\cos^2\theta - \tfrac13\bigr)
  \]

  \(\lambda_s\) is a measured material number. Single crystals need a \(\lambda_{100}\), \(\lambda_{111}\) (or full magnetoelastic tensor) instead of one \(\lambda_s\).

- Inverse (Villari) statement: stress enters the effective anisotropy and shifts \(M(H)\). That is a write / read channel on the magnetic latch, not a second independent latch.

- \(\lambda(T)\) tracks the magnetic order parameter and vanishes at \(T_C\). Mean-field exponents are fits, not used here as a mechanism claim.

- Volume magnetostriction (isotropic \(\Delta V/V\)) is a separate, usually smaller, channel. It is the term that can cancel ordinary thermal expansion in Invar (`thermal-expansion`).

These relations describe the measured length change. They do not compute why Terfenol-D is \(10^{-3}\) and Ni is \(10^{-5}\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** An ordered magnetic population sitting in a deformable lattice, large enough for a macroscopic \(\Delta L\) and a macroscopic \(M\). A paramagnetic crystal has the lattice and not the ordered moment. A liquid magnet (if any) has no static shear grid to register a linear \(\lambda_s\) of this kind. Grain-scale latching of \(M\) is owned by `permanent-magnet-latch` / `superparamagnetism`; this file owns the strain that follows \(M\).

- **Clock rate / latency.** Magnetic side: precession / domain-wall clocks of the magnet entries. Mechanical side: acoustic transit of `elasticity`. Laboratory \(\lambda(H)\) loops are limited by the field sweep and by eddy currents / walls, not by the 28 GHz/T carrier.

- **Energy barriers or thresholds.** No separate magnetostrictive latch. The thresholds are the host magnet’s: \(T_C\), the anisotropy / coercivity write field, and the mechanical integrity of the grid. Magnetoelastic energy is an extra term in the anisotropy budget; it can raise or lower the latch barrier but is not the barrier’s origin in NdFeB-class \(K_1\).

- **Dominant failure modes.**
  - Thermal: \(T > T_C\) → ordered moment gone → \(\lambda = 0\).
  - Mechanical: lattice plastic / cracked / melted → no grid to carry \(\Delta L\); the latch may also be erased (owned by the latch entry).
  - Field / domain: \(M\) not aligned (soft loop not driven, or hard magnet below coercivity) → macroscopic \(\Delta L\) small even though \(\lambda_s\) is finite.
  - Material: vanishing spin–lattice coupling (\(\lambda_s \to 0\)) → moment remains, length does not change.

- **Emergent constant or stable output.** A saturation strain \(\lambda_s\) locked to the aligned moment, plus the inverse stress–\(M\) channel, while the ordered magnet and the lattice both remain inside the envelope above.

### 4.6 Internal Consistency Notes

Filing magnetostriction under lattice-modes, with `mechanical-lattice` and `thermal` tags, matches the taxonomy: the output is a strain, and it dies when either the grid or the ordered moment fails. The latch entry continues to own remanence, \(T_C\), and \(KV\). This file must not re-specify the magnet.

The mechanical failure path named on `permanent-magnet-latch` is this coupling plus ordinary plasticity: shock couples into \(M\) and into the grain structure. That is a cross-link, not a second magnet entry.

Why \(\lambda_s\) spans \(10^{-5}\) (Ni) to \(10^{-3}\) (Terfenol-D) is not extracted from a node rule here. Crystal-field and magnetoelastic coefficients are taken as data, the same way \(d_{33}\) is taken as data on `piezoelectricity`. Mapping confidence is therefore medium.

Invar’s near-zero expansion is a compensation between this (volume) channel and ordinary anharmonic expansion. `thermal-expansion` owns that statement.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the \(T_C\) and lattice-destruction collapses, and the lock of \(\Delta L\) to \(M\), are sharp and consistent with the magnet latch, but \(\lambda_s\) is a handbook coupling and is not derived from a stated node-level spring.

## Related entries

- [permanent-magnet-latch](permanent-magnet-latch.md) — the directional latch; this file is the mechanical length change locked to that moment
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — \(M(H)\) that \(\lambda\) follows
- [elasticity](elasticity.md) — the strain hardware
- [piezoelectricity](piezoelectricity.md) — charge analogue (strain \(\leftrightarrow\) \(P\))
- [thermal-expansion](thermal-expansion.md) — Invar compensation by volume magnetostriction
- [melting](melting.md) — grid-loss collapse shared with every lattice mode
- [magnetic-domains](magnetic-domains.md) — domain population that must align before macroscopic \(\lambda\) appears
