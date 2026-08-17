---
id: semiconductor-gap-absorption
title: Semiconductor Gap Absorption (Band-Edge Conversion)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - mechanical-lattice
  - thermal
confidence_data: high
confidence_mapping: high
related:
  - photoconductivity
  - photoelectric-threshold
  - ionization-threshold
  - x-ray-absorption-edge
  - work-function-thermionic
  - refraction-dielectric
  - plasma-frequency-cutoff
  - blackbody-spectrum
updated: 2026-08-17
---

# Semiconductor Gap Absorption (Band-Edge Conversion)

### 4.1 Effect Name

Semiconductor gap absorption (band-edge conversion)

### 4.2 Macroscopic Observation

A semiconductor crystal that is transmitting in a long-wavelength window becomes absorbing once the photon energy crosses a material-specific edge. Silicon and germanium pass infrared and go opaque through the visible; gallium arsenide is already opaque in the red; diamond remains clear through the whole visible and begins to absorb only in the ultraviolet. The edge is a property of the intact crystal: heating shifts it slightly; melting or amorphizing the lattice destroys the sharp crystalline edge.

### 4.3 Established Quantitative Boundaries

- Room-temperature gaps (handbook, \(300\,\mathrm{K}\)): Si \(E_g \approx 1.12\,\mathrm{eV}\) (indirect); Ge \(E_g \approx 0.66\,\mathrm{eV}\) (indirect); GaAs \(E_g \approx 1.42\,\mathrm{eV}\) (direct); diamond \(E_g \sim 5.5\,\mathrm{eV}\) (indirect). Corresponding free-space wavelengths \(hc/E_g\): Si \(\sim 1.11\,\mu\mathrm{m}\), Ge \(\sim 1.88\,\mu\mathrm{m}\), GaAs \(\sim 0.87\,\mu\mathrm{m}\), diamond \(\sim 0.23\,\mu\mathrm{m}\).
- Low-temperature limits of the same gaps sit higher by a few tens to \(\sim 100\,\mathrm{meV}\) (Si \(\approx 1.17\,\mathrm{eV}\), Ge \(\approx 0.74\,\mathrm{eV}\), GaAs \(\approx 1.52\,\mathrm{eV}\) as \(T\to 0\)). The gap shrinks with heating. That is a shift of the gate, not a new channel.
- Direct-gap edges (GaAs) rise steeply once \(h\nu > E_g\). Indirect-gap edges (Si, Ge, diamond) rise more slowly: the conversion also consumes or emits a phonon and is weaker just above threshold. Both are the same gate with a different lattice-clock requirement.
- Below \(E_g\) the crystal has a transparency window (limited in practice by free-carrier absorption, impurities, and lattice vibrations). Above \(E_g\) the absorption coefficient becomes large enough that ordinary wafers are optically thick in the visible.
- Urbach tail: a measured exponential foot of absorption just below \(E_g\), with a slope energy typically of order tens of \(\mathrm{meV}\) in crystals and larger in disordered hosts. Excitons pull a small additional feature just below \(E_g\) (a few to tens of \(\mathrm{meV}\) in ordinary bulk semiconductors). Both are softness of the same gate.

**Data confidence:** High — \(E_g\) values, direct/indirect character, and the existence of a transparency window below the edge are multiply reproduced handbook measurements. The precise Urbach energy of a given sample is medium (defect- and temperature-dependent).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Interband onset: conversion requires \(h\nu \ge E_g\) (direct) or \(h\nu \ge E_g \pm \hbar\omega_{\mathrm{ph}}\) (indirect, phonon absorbed or emitted).
- Direct allowed edge (parabolic bands, descriptive):

  \[
  \alpha(h\nu) \propto \sqrt{h\nu - E_g}\qquad (h\nu > E_g)
  \]

- Indirect edge (descriptive):

  \[
  \alpha(h\nu) \propto \bigl(h\nu - E_g \pm \hbar\omega_{\mathrm{ph}}\bigr)^2
  \]

- Urbach foot below the edge:

  \[
  \alpha(h\nu) \propto \exp\!\bigl((h\nu - E_0)/E_U\bigr)
  \]

  \(E_U\) is a measured slope, not a second gap.

- Gap versus temperature (Varshni form, a fit to data):

  \[
  E_g(T) = E_g(0) - \frac{\alpha T^2}{T+\beta}
  \]

Below-threshold light is refracted and, at most, weakly attenuated by processes that are not interband conversion. That non-occurrence *is* the collapse of this effect.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The gate is a property of the periodic lattice: a filled valence band and an empty conduction band separated by \(E_g\). A single unit cell already carries the gap; macroscopic opacity is the summed conversion of a large illuminated population over an optical path of order \(1/\alpha\). Destroying crystalline order (melt, heavy damage) removes the sharp edge. That is a lattice-resource failure, not a change of family.

- **Clock rate / latency.** The optical cycle and the interband polarization response sit in the femtosecond neighbourhood of visible / near-IR light. An indirect conversion must also exchange a phonon with the lattice; the lattice clock is then a required resource just above threshold. Relative to any laboratory shutter the conversion, when allowed, is already complete.

- **Energy barriers or thresholds.** The operating gate is \(E_g\). Direct gaps open with the photon alone; indirect gaps open with photon plus phonon. Temperature moves \(E_g\); it does not replace it.

- **Dominant failure modes.**
  - Under-threshold: \(h\nu < E_g\) → interband conversion does not occur. The sample stays in its transparency window. That is the collapse of the effect.
  - Lattice: loss of crystalline order washes the sharp edge into a smeared amorphous spectrum.
  - Thermal: \(E_g(T)\) walks; the Urbach foot grows. The gate remains a gate, slightly relocated and slightly softened.
  - Free-carrier / impurity absorption can hide the window without opening the interband channel. Those are other conversions, not this one.

- **Emergent constant or stable output.** A material-typical absorption edge and the associated split between a transmitting window and an opaque band, produced whenever a photon population is presented to an intact gapped lattice.

### 4.6 Internal Consistency Notes

The mapping is the photoelectric-class energy gate moved into a bulk crystal. [Photoconductivity](photoconductivity.md) is the same gate read as current rather than as opacity; the two entries must share \(E_g\) and must not invent different collapse energies. [X-ray-absorption-edge](x-ray-absorption-edge.md) is the same pattern at inner-shell (keV) bindings; [ionization-threshold](ionization-threshold.md) is the atomic analogue.

Urbach tails and excitons are recorded as measured softness, not as extra mechanisms and not as evidence that the gate is absent. A closed mapping would say why a given crystal has the gap it has from node rules alone. QSA here *takes* the measured \(E_g\) as the specification; that is a gap in derivation, not a conflict with the collapse.

Indirect edges need a phonon. That is a real extra resource, and it explains the slower rise of \(\alpha\) in Si and Ge without opening a second family. If the lattice cannot supply the phonon (a thought-experiment frozen harmonic crystal with no occupancy), the indirect channel at threshold would starve; the phonon terms in the edge formulae already record that requirement.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(E_g\) is a sharp, handbook-grade energy gate, below-threshold transparency is the observed non-occurrence, and the QSA translation is the same conversion family as the photoelectric threshold.

## Related entries

- [photoconductivity](photoconductivity.md) — the same \(E_g\) gate, read out as a current instead of as opacity
- [photoelectric-threshold](photoelectric-threshold.md) — surface ejection gate in a metal; same family, different hardware
- [ionization-threshold](ionization-threshold.md) — atomic binding gate; the isolated-node analogue of \(E_g\)
- [x-ray-absorption-edge](x-ray-absorption-edge.md) — inner-shell version of the same pattern, at keV
- [work-function-thermionic](work-function-thermionic.md) — surface barrier opened by heat rather than by a photon
- [refraction-dielectric](refraction-dielectric.md) — below-gap response: the lattice polarizes and does not convert
- [plasma-frequency-cutoff](plasma-frequency-cutoff.md) — a collective frequency gate, not a single-electron energy gate
- [blackbody-spectrum](blackbody-spectrum.md) — thermal photon population that may sit above or below \(E_g\)
