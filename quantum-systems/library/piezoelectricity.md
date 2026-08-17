---
id: piezoelectricity
title: Piezoelectricity (Strain–Polarization Coupling)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
  - field-threshold
  - thermal
confidence_data: high
confidence_mapping: medium
related:
  - ferroelectric-remanence
  - elasticity
  - magnetostriction
  - melting
  - phonon-dispersion
  - refraction-dielectric
  - dielectric-breakdown
updated: 2026-08-17
---

# Piezoelectricity (Strain–Polarization Coupling)

### 4.1 Effect Name

Piezoelectricity (strain–polarization coupling)

### 4.2 Macroscopic Observation

Compressing a quartz plate, a PZT ceramic, or an AlN film produces a charge on the electrodes. Applying a voltage produces a proportional strain. The effect is linear at ordinary drive and reverses with the sign of the stress or field. It is absent in ordinary salt, silicon, and most metals. In ferroelectric piezoelectrics (PZT, BaTiO\(_3\)) the large coupling disappears on heating through the ferroelectric Curie point. Quartz is not a ferroelectric latch; its coupling tracks the non-centrosymmetric lattice, not a switchable remnant polarization.

### 4.3 Established Quantitative Boundaries

- Symmetry gate: linear piezoelectricity requires a lattice without an inversion center. Twenty of the 32 crystal classes meet that condition. Centrosymmetric crystals have \(d_{ij} = 0\) for the linear effect (they may still show quadratic electrostriction, which is not this entry).
- Handbook coupling class, piezoelectric charge constants \(d\) in \(\mathrm{pC\,N^{-1}}\) (\(\equiv \mathrm{pm\,V^{-1}}\)): quartz and AlN sit in the single-digit to \(\sim 10\) class (quartz \(d_{11} \approx 2.3\,\mathrm{pC\,N^{-1}}\) is a standard cut number); PZT ceramics sit in the \(10^2\,\mathrm{pC\,N^{-1}}\) class. Specific commercial PZT grades are not a single pin.
- Ferroelectric collapse: the large polar \(d_{ij}\) of PZT / BaTiO\(_3\) vanishes with the polar phase above \(T_C\) (BaTiO\(_3\) \(T_C \approx 393\,\mathrm{K}\); PZT \(T_C\) is composition-dependent, typically a few hundred °C). The remnant polarization itself is owned by `ferroelectric-remanence`.
- Quartz \(\alpha\)–\(\beta\) transition at \(573^\circ\mathrm{C}\) changes the coefficients; \(\beta\)-quartz remains non-centrosymmetric. Quartz does not die at a ferroelectric \(T_C\).
- Lattice destruction (`melting`) removes the coupling with the grid. Dielectric breakdown at high \(E\) destroys the capacitor; that is a different cliff (`dielectric-breakdown`).

**Data confidence:** High — the inversion-center rule, the quartz / AlN / PZT coupling classes, and the ferroelectric \(T_C\) collapse are multiply reproduced. A particular ceramic’s \(d_{33}\) is medium (process- and composition-dependent).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Linear constitutive pair (direct and inverse), in the usual condensed notation:

  \[
  P_i = d_{ijk}\,\sigma_{jk}, \qquad \varepsilon_{jk} = d_{ijk}\,E_i
  \]

  \(d_{ijk}\) is a measured material tensor. It is identically zero when inversion is a symmetry of the lattice.

- Electrostriction (all dielectrics, quadratic, not this effect): \(\varepsilon \propto E^2\). It survives in centrosymmetric crystals and is a different, weaker machine at ordinary fields.

- In a ferroelectric, \(d_{ij}\) is large only inside the polar phase and is tied to the remnant \(P\) and to how \(P\) moves with stress. Above \(T_C\) that polar hardware is gone.

These relations describe the measured coupling. They do not compute \(d_{33}\) from a node-spring rule, and they do not replace the latch mapping of remnant \(P\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A crystalline (or poled ceramic) lattice that lacks inversion, large enough for a macroscopic stress and a macroscopic polarization to be defined. A centrosymmetric crystal of any size does not provision the linear coupling. A poled ferroelectric ceramic additionally needs grains that hold a polar direction — that polar *memory* is the latch of `ferroelectric-remanence`; this file owns only the strain–polarization link.

- **Clock rate / latency.** The mechanical side tracks the acoustic clocks of `elasticity` / `speed-of-sound` (transit across the plate). The electrical side tracks the dielectric response of the bound-charge population (`refraction-dielectric`). Laboratory piezo devices are usually limited by the plate resonance, not by an atomic period.

- **Energy barriers or thresholds.** The existence gate is inversion-free lattice symmetry, not an energy barrier. In ferroelectrics an additional thermal threshold \(T_C\) destroys the polar phase and with it the large \(d_{ij}\). Coercive field writes the polar latch; it is not the piezo coupling itself.

- **Dominant failure modes.**
  - Symmetry: inversion present (Si, NaCl, most metals; or a phase that restored inversion) → \(d_{ij} = 0\).
  - Thermal, ferroelectric: \(T > T_C\) → polar phase gone → large piezo gone.
  - Thermal / mechanical: melting or cracking of the grid → coupling gone with the lattice.
  - Field: \(E\) past breakdown → the dielectric is destroyed (`dielectric-breakdown`), which is not the symmetry gate.
  - Amplitude: drive out of the linear window → harmonics and, in ferroelectrics, depoling.

- **Emergent constant or stable output.** A linear, reversible strain \(\leftrightarrow\) polarization conversion with a material-typical \(d_{ij}\) (pC/N class), present only while the inversion-free (and, if ferroelectric, polar) lattice holds.

### 4.6 Internal Consistency Notes

The inversion-center gate is as sharp a hardware condition as the plasma-frequency clock on `reflection`: if the symmetry is present, the linear output is forbidden, independent of field strength short of breakdown. That clause is tight.

Two collapse routes must not be collapsed into one sentence. Quartz fails by losing the non-centrosymmetric grid (or by being replaced with a centrosymmetric material). PZT fails, as a *large* piezo, at ferroelectric \(T_C\) even while a solid remains. The latch entry owns remnant \(P\); this entry owns \(d_{ij}\). Shock-depoling or cracking is lattice damage tagged `mechanical-lattice` on the latch, not a second copy of melting.

The mapping takes handbook \(d_{ij}\) as the coupling strength. QSA does not yet derive why quartz is \(\sim 2\,\mathrm{pC\,N^{-1}}\) and PZT is \(10^2\) class from node rules. That is the principal reason the mapping is medium rather than high.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the symmetry gate and the ferroelectric \(T_C\) collapse are sharp and correctly placed, but the coupling magnitude is taken from handbook \(d_{ij}\) and the polar latch is a different machine sharing the same crystal.

## Related entries

- [ferroelectric-remanence](ferroelectric-remanence.md) — the polar latch; this file owns strain \(\leftrightarrow\) \(P\), not remnant \(P\)
- [elasticity](elasticity.md) — the strain hardware
- [magnetostriction](magnetostriction.md) — the magnetic analogue (moment \(\leftrightarrow\) strain)
- [melting](melting.md) — destruction of the coupling lattice
- [phonon-dispersion](phonon-dispersion.md) — the living grid whose symmetry is the gate
- [refraction-dielectric](refraction-dielectric.md) — bound-charge polarization without the strain gate
- [dielectric-breakdown](dielectric-breakdown.md) — high-\(E\) destruction of the dielectric, not the symmetry cliff
