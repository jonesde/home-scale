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
review_depth: light
related:
  - ionization-threshold
  - photoelectric-threshold
  - semiconductor-gap-absorption
  - pair-production
  - reflection
  - plasma-frequency-cutoff
  - photoconductivity
updated: 2026-11-11
---

# X-ray Absorption Edge (Inner-Shell Gate)

### 4.1 Effect Name

X-ray absorption edge (inner-shell gate)

### 4.2 Macroscopic Observation

The X-ray attenuation of a material falls smoothly with photon energy and then rises abruptly at certain energies. Each rise marks the binding energy of an inner electron shell of one element, so its position identifies the element and the shell. Tuning a source across the edge makes the same foil several times more absorbing. Fine structure above the edge depends on the chemical state and the neighbouring atoms.

### 4.3 Established Quantitative Boundaries

- **Measured.** Copper, from the NIST attenuation table [S1]. K edge at 8.9789 keV: the mass attenuation coefficient \(\mu/\rho\) goes from 38.29 to 278.4 cm² g⁻¹. L₁ edge at 1.0961 keV: from 8242 to 9347 cm² g⁻¹.
- **Computed here.** The jump ratio is 7.27 at the K edge and 1.13 at the L₁ edge. The K-edge photon has a wavelength of 0.138 nm.
- **Convention.** The table places each edge at a single energy with a sawtooth shape; cross sections near edges are assumed to have that form and the edge energies are taken from a separate compilation [S5].
- **Model (empirical scaling).** Away from edges the absorption coefficient is a smooth function that goes roughly as \(\rho Z^4/(A E^3)\) [S3].
- **Model (semi-empirical level widths).** The natural width of the copper K level is 1.55 eV [S2].
- **Computed here.** That width corresponds to a core-hole lifetime \(\hbar/\Gamma\) of 0.42 fs and is 1.7 × 10⁻⁴ of the edge energy. The period \(h/E\) of the X-ray is 4.1 × 10⁻¹⁹ s at 10 keV [S4]. The first version put the hole lifetime in the femtosecond range; for copper K it is below a femtosecond.
- **Measured.** The edge position and shape are sensitive to formal valence, ligand type and coordination [S3]. No opened source gives the size of the shift for copper.
- **Convention.** Shell labels: K for \(n = 1\); L₁, L₂, L₃ for \(n = 2\).

**Data confidence:** High — the edge energy and the tabulated jump were read in the NIST table. The table is an evaluated compilation with idealized edge shapes, and the level width is a semi-empirical tabulation. No number is filed for chemical shifts.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Onset for a shell \(s\) with binding energy \(E_b^{(s)}\): \(h\nu \ge E_b^{(s)}\).
- Transmission through a thickness \(t\) [S3]:

  \[
  I = I_0\,e^{-\mu t}
  \]

- Between edges, \(\mu \approx \rho Z^4/(A E^3)\) [S3].
- Lifetime broadening: a level of width \(\Gamma\) has lifetime \(\hbar/\Gamma\).
- Fluorescence and Auger decay of the core hole follow the absorption. Oscillations above the edge come from scattering of the photoelectron by neighbouring atoms [S3].

Below \(E_b^{(s)}\) that shell does not convert. Shallower shells and scattering still attenuate the beam.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One atom with one occupied inner shell. Opacity is the summed output of the atoms along the beam, \(e^{-\mu t}\); thinning the sample reduces it in proportion and does not move the edge. Removing the element removes the edge.

- **Clock rate / latency.** The X-ray period is 4.1 × 10⁻¹⁹ s at 10 keV. The core hole of copper K lives 0.42 fs, and that lifetime sets the 1.55 eV width of the step.

- **Energy barriers or thresholds.** The operating gates are the shell binding energies, 8.9789 keV for copper K and 1.0961 keV for copper L₁. They are the same kind of energy gate as the work function and the semiconductor gap, at keV.

- **Dominant failure modes.**
  - **Threshold** — photon energy below \(E_b^{(s)}\): that shell does not convert and its step is absent. The step is rounded by the lifetime width (1.55 eV, 1.7 × 10⁻⁴ of the copper K energy) and by instrument resolution.
  - **Threshold** — missing hardware: without the element there is no edge. No opened source covers an emptied shell.
  - **Crossover** — sample thickness: the transmitted fraction is \(e^{-\mu t}\), continuous in \(t\).
  - **Crossover** — competing channels: between edges this channel fades as roughly \(E^{-3}\); at MeV energies [pair-production](pair-production.md) takes over the attenuation.

- **Emergent constant or stable output.** An element-specific step in \(\mu(E)\) at \(E_b^{(s)}\), a factor of 7.27 for copper K, which identifies the element and, through its fine structure, the chemical environment.

### 4.6 Internal Consistency Notes

This is the photoelectric-class gate at inner-shell energies. [Photoelectric-threshold](photoelectric-threshold.md), [semiconductor-gap-absorption](semiconductor-gap-absorption.md), [ionization-threshold](ionization-threshold.md) and this entry share the under-threshold clause: below the binding energy that conversion does not occur.

Sourcing changed no headline number: the edge energy and the 38 to 278 cm² g⁻¹ jump were confirmed. The copper K hole lifetime is 0.42 fs, shorter than the femtosecond range first stated. The first version's "eV-level" chemical shift and its statement that the jump exists in atomic vapours are dropped for lack of an opened source. Unlike the optical gap of silicon, this edge is a step in the output as well as a threshold in energy, because the newly opened shell adds a large cross section at once; its width is about 10⁻⁴ of its energy.

QSA takes \(E_b^{(s)}\) from tables and does not derive it. The fine structure above the edge is modulation of an open channel by the surroundings of the atom and needs no second gate.

### 4.7 Overall Confidence in the QSA Mapping

**High** — edge energies and attenuation jumps are tabulated thresholds that translate directly into a discrete inner-shell energy gate whose collapse is under-threshold drive.

## Related entries

- [ionization-threshold](ionization-threshold.md) — valence ionization of an isolated atom; the same pattern at tens of eV
- [photoelectric-threshold](photoelectric-threshold.md) — surface work-function gate in the optical / UV
- [semiconductor-gap-absorption](semiconductor-gap-absorption.md) — bulk valence-to-conduction gate at \(E_g\)
- [pair-production](pair-production.md) — the next conversion to open at still higher photon energy (\(2mc^2\))
- [photoconductivity](photoconductivity.md) — valence-band analogue read as current
- [reflection](reflection.md) — collective below-plasma response; not an inner-shell conversion
- [plasma-frequency-cutoff](plasma-frequency-cutoff.md) — collective frequency gate of a free-electron population

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Hubbell and Seltzer, NIST X-Ray Mass Attenuation Coefficients (NISTIR 5632), table for copper, Z = 29](https://physics.nist.gov/PhysRefData/XrayMassCoef/ElemTab/z29.html) | full-text | Cu K edge 8.9789 keV with 38.29 to 278.4 cm²/g; L1 edge 1.0961 keV with 8242 to 9347 cm²/g. Evaluated compilation. |
| S2 | [Krause and Oliver, "Natural widths of atomic K and L levels, Kα X-ray lines and several KLL Auger lines", *J. Phys. Chem. Ref. Data* 8, 329 (1979)](https://srd.nist.gov/jpcrdreprint/1.555595.pdf) | full-text | Cu K level width 1.55 eV. Semi-empirical tabulation. |
| S3 | [Newville, "Fundamentals of XAFS", Consortium for Advanced Radiation Sources, University of Chicago](https://www.lehigh.edu/imi/teched/GlassCSC/SuppReading/Tutorials.pdf) | full-text | Tutorial, secondary: transmission law; smooth dependence roughly as ρZ⁴/(AE³); sensitivity of the edge to valence, ligand and coordination; origin of the fine structure. |
| S4 | [NIST, CODATA 2022 recommended values: Planck constant in eV/Hz (with the page for the reduced constant in eV s)](https://physics.nist.gov/cgi-bin/cuu/Value?hev) | full-text | Constants for the X-ray period, the wavelength and the lifetime from the width. |
| S5 | [Hubbell and Seltzer, NIST X-Ray Mass Attenuation Coefficients, section 2, "X-ray interactions with matter"](https://physics.nist.gov/PhysRefData/XrayMassCoef/chap2.html) | full-text | Cross sections near absorption edges assumed to have sawtooth shapes; edge energies from Bearden and Burr. |
