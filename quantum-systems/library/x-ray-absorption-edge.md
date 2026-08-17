---
id: x-ray-absorption-edge
title: X-ray Absorption Edge (Inner-Shell Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - clock-latency
confidence_data: high
confidence_mapping: high
related:
  - ionization-threshold
  - photoelectric-threshold
  - semiconductor-gap-absorption
  - pair-production
  - reflection
  - plasma-frequency-cutoff
  - photoconductivity
updated: 2026-08-17
---

# X-ray Absorption Edge (Inner-Shell Gate)

### 4.1 Effect Name

X-ray absorption edge (inner-shell gate)

### 4.2 Macroscopic Observation

A thin metal foil or a solution that is relatively transmitting just below a characteristic X-ray energy becomes abruptly more absorbing once that energy is crossed. The location of the jump is an elemental fingerprint: copper is not iron, and a K-edge is not an L-edge. Tuning a synchrotron or a filtered tube source across the jump turns the same sample from a window into a stopper. Fine structure immediately above the edge (near-edge shape, EXAFS wiggles) rides on the open channel; it does not create a second jump.

### 4.3 Established Quantitative Boundaries

- Each occupied inner shell is a distinct gate. Shell labels: K (\(n=1\)), L (\(n=2\), split into L\(_1\), L\(_2\), L\(_3\)), M, … Binding energies run from tens of eV (shallow cores) to tens of keV (deep K shells of heavy elements).
- Copper as the type case (NIST mass-attenuation tables): Cu K-edge at \(8.9789\,\mathrm{keV}\) (\(\sim 8.98\,\mathrm{keV}\) class); Cu L\(_1\) at \(1.096\,\mathrm{keV}\). At the Cu K-edge the mass attenuation coefficient \(\mu/\rho\) jumps from \(\approx 38\,\mathrm{cm^2\,g^{-1}}\) to \(\approx 278\,\mathrm{cm^2\,g^{-1}}\). That order-of-magnitude step is the macroscopic signature of the newly opened K channel.
- Between edges, photoelectric absorption falls rapidly with energy (empirically a steep inverse power of \(E\), often quoted near \(E^{-3}\)). Crossing the next shell binding energy re-opens a channel and \(\mu\) jumps again.
- Edge position is element-specific and, at the eV level, slightly chemically shifted (oxidation state, ligands). The shift is a relocation of the same gate, used as a spectroscopic coordinate, not a new conversion family.
- Edges are not infinitely sharp. Core-hole lifetime and instrumental resolution give a finite width (eV-scale for typical metal K-edges). That width is a clock/latency smear of one gate.

**Data confidence:** High — edge energies and tabulated \(\mu/\rho\) jumps are standard X-ray optical data (NIST and equivalent tables). Chemical shifts and the exact near-edge lineshape of a given compound are high as a class and sample-specific in detail.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Onset condition for a named shell \(s\):

  \[
  h\nu \ge E_b^{(s)}
  \]

  where \(E_b^{(s)}\) is the measured binding energy of that shell.

- Photoelectric channel open above the edge, closed below it. The isolated-atom photoelectric cross section above an edge falls with energy; tabulated \(\mu/\rho\) record that fall plus scattering.
- Fluorescence and Auger decay of the core hole are the relaxation channels *after* the gate has opened. They are not additional thresholds for the absorption jump itself.
- XANES / EXAFS oscillations modulate \(\mu(E)\) above the edge through the local scattering environment. They are structure on an open gate.

Below \(E_b^{(s)}\) that shell does not convert. That non-occurrence is the collapse of *this* edge. Other open channels (shallower shells, scattering) may still attenuate the beam; they are other effects.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The conversion event is one atom, one occupied inner shell. Macroscopic opacity is the summed output of a large atomic population (foil, crystal, solution). There is no collective coherence length analogous to optical reflection; thinning the sample reduces optical depth in proportion and does not close the atomic gate. Removing the element removes the edge.

- **Clock rate / latency.** The absorption step itself tracks the X-ray cycle (\(\sim 10^{-19}\,\mathrm{s}\) at 10 keV). The observed edge width is set in part by the core-hole lifetime (femtosecond neighbourhood for many deep holes), which is a latency smear of the gate, not a second threshold. EXAFS is a spatial interference pattern written by the outgoing photoelectron on that same open channel.

- **Energy barriers or thresholds.** The operating gates are the shell binding energies \(E_b^{(K)}, E_b^{(L)}, \ldots\). They are the same kind of discrete energetic lock as the work function and the semiconductor gap, relocated from eV to keV.

- **Dominant failure modes.**
  - Under-threshold: \(h\nu < E_b^{(s)}\) → that shell does not convert. The K-edge (or L-edge, …) is absent from the spectrum.
  - Missing hardware: the element is not present, or the shell is already empty (highly ionized species) → no jump.
  - Clock smear: a short hole lifetime plus instrument resolution rounds the step. The gate is still there.
  - At still higher energy, [pair-production](pair-production.md) opens a different conversion and eventually dominates attenuation. That is another family member, not the failure of this one.

- **Emergent constant or stable output.** An element-specific step in \(\mu(E)\) at \(E_b^{(s)}\), reproducible enough to identify the element and, with finer structure, its local chemistry.

### 4.6 Internal Consistency Notes

This is the photoelectric-class gate at inner-shell energies. [Photoelectric-threshold](photoelectric-threshold.md) (surface, eV), [semiconductor-gap-absorption](semiconductor-gap-absorption.md) (valence band, eV), [ionization-threshold](ionization-threshold.md) (valence electron on an isolated atom, tens of eV), and this entry (core shell, keV) are one machine class. They must share the under-threshold clause: below the binding, that conversion does not occur.

Near-edge fine structure is a temptation to invent extra gates. It is not required by the data: the jump exists in atomic vapours; the wiggles are environmental modulation of an already-open channel.

A remaining gap: QSA takes \(E_b^{(s)}\) from tables. It does not here derive the 8.98 keV of copper’s K shell from a more primitive node rule. The collapse \(h\nu < E_b\) does not depend on that derivation. Chemical shifts of a few eV on a 9 keV gate are consistent with a small environmental correction to the same barrier.

### 4.7 Overall Confidence in the QSA Mapping

**High** — edge energies and attenuation jumps are among the sharpest tabulated thresholds in the library, and they translate directly into a discrete inner-shell energy gate whose collapse is simply under-threshold drive.

## Related entries

- [ionization-threshold](ionization-threshold.md) — valence ionization of an isolated atom; the same pattern at tens of eV
- [photoelectric-threshold](photoelectric-threshold.md) — surface work-function gate in the optical / UV
- [semiconductor-gap-absorption](semiconductor-gap-absorption.md) — bulk valence-to-conduction gate at \(E_g\)
- [pair-production](pair-production.md) — the next conversion to open at still higher photon energy (\(2mc^2\))
- [photoconductivity](photoconductivity.md) — valence-band analogue read as current
- [reflection](reflection.md) — collective below-plasma response; not an inner-shell conversion
- [plasma-frequency-cutoff](plasma-frequency-cutoff.md) — collective frequency gate of a free-electron population
