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
review_depth: light
related:
  - photoconductivity
  - photoelectric-threshold
  - ionization-threshold
  - x-ray-absorption-edge
  - work-function-thermionic
  - refraction-dielectric
  - plasma-frequency-cutoff
  - blackbody-spectrum
updated: 2026-11-11
---

# Semiconductor Gap Absorption (Band-Edge Conversion)

### 4.1 Effect Name

Semiconductor gap absorption (band-edge conversion)

### 4.2 Macroscopic Observation

A semiconductor crystal that transmits at long wavelengths absorbs once the photon energy passes a material-specific edge. Silicon and germanium pass infrared and are opaque in the visible; gallium arsenide is opaque in the red; diamond is clear through the visible and absorbs in the ultraviolet. Heating moves the edge to lower energy. In a direct-gap crystal the edge is steep; in silicon the absorption coefficient falls continuously over five orders of magnitude across the edge.

### 4.3 Established Quantitative Boundaries

- **Measured.** Gaps at 300 K: Si 1.12 eV [S1]; Ge 0.661 eV [S2]; GaAs 1.424 eV [S3]; diamond 5.46–5.6 eV [S4]. The lowest gap of Si and Ge is indirect: the direct gaps are listed separately at 3.4 eV for Si [S1] and 0.8 eV for Ge [S2].
- **Computed here.** Wavelength \(hc/E_g\): Si 1107 nm, Ge 1876 nm, GaAs 871 nm, diamond 221–227 nm.
- **Model (Varshni fit to measured gaps).** \(E_g(T)\) in eV: Si \(1.17 - 4.73 \times 10^{-4}\,T^2/(T+636)\) [S1]; Ge \(0.742 - 4.8 \times 10^{-4}\,T^2/(T+235)\) [S2]; GaAs \(1.519 - 5.405 \times 10^{-4}\,T^2/(T+204)\) [S3]. For diamond \(dE_g/dT = -5.4 \times 10^{-5}\) eV K⁻¹ [S4].
- **Computed here.** The fits give 1.125, 0.661 and 1.422 eV at 300 K. The zero-temperature gaps exceed the 300 K values by 50 meV (Si), 81 meV (Ge) and 95 meV (GaAs).
- **Measured.** Absorption coefficient of silicon at 300 K [S5]: 9.52 × 10⁴ cm⁻¹ at 400 nm, 6.39 × 10³ at 550 nm, 850 at 800 nm, 64 at 1000 nm, 3.5 at 1100 nm, 0.68 at 1150 nm and 0.022 at 1200 nm.
- **Computed here.** The absorption length \(1/\alpha\) in silicon is 1.6 µm at 550 nm, 156 µm at 1000 nm, 2.9 mm at 1100 nm and 45 cm at 1200 nm. Absorption continues below the gap: 1200 nm is 1.033 eV, 87 meV under the 1.12 eV gap. From 550 to 1200 nm the coefficient falls by a factor of 2.9 × 10⁵ with no step at \(E_g\).
- **Measured.** Urbach edge of semi-insulating GaAs: the characteristic energy of the exponential edge rises linearly from 7.5 meV at room temperature to 12.4 meV at 700 °C [S6].
- **Measured.** Disorder widens the edge. Room-temperature Urbach energies of hydrogenated amorphous silicon are typically 50–150 meV [S7], against 7.5 meV for crystalline GaAs [S6].
- **Convention.** Exciton features and the transparency limits set by free carriers and lattice absorption are not quantified here; no source was opened for them.

**Data confidence:** High for the gaps and their temperature dependence, read on the Ioffe semiconductor pages [S1]–[S4], a secondary compilation. The silicon absorption table is a secondary reproduction of Green and Keevers [S5]. The amorphous-silicon range is tertiary [S7].

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Interband onset: \(h\nu \ge E_g\) (direct), or \(h\nu \ge E_g \pm \hbar\omega_\mathrm{ph}\) (indirect, a phonon absorbed or emitted).
- Direct allowed edge, parabolic bands: \(\alpha \propto \sqrt{h\nu - E_g}\).
- Indirect edge: \(\alpha \propto (h\nu - E_g \pm \hbar\omega_\mathrm{ph})^2\).
- Urbach foot below the edge [S6]:

  \[
  \alpha(h\nu) \propto \exp\!\bigl((h\nu - E_0)/E_U\bigr)
  \]

- Gap against temperature, Varshni form [S1]:

  \[
  E_g(T) = E_g(0) - \frac{\alpha T^2}{T+\beta}
  \]

- Transmission through a thickness \(L\): \(e^{-\alpha L}\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The gate is a property of the periodic lattice: a filled valence band and an empty conduction band separated by \(E_g\). Opacity is the summed conversion over an optical path of order \(1/\alpha\), which in silicon runs from 1.6 µm at 550 nm to 2.9 mm at 1100 nm. Disorder widens the edge.

- **Clock rate / latency.** The optical cycle is in the femtosecond range for visible and near-infrared light. An indirect conversion also exchanges a phonon with the lattice, so the lattice is a required resource near the edge.

- **Energy barriers or thresholds.** The operating gate is \(E_g\). A direct gap opens with the photon alone; an indirect gap opens with a photon and a phonon. Temperature moves \(E_g\) by 50–95 meV between 0 and 300 K in Si, Ge and GaAs.

- **Dominant failure modes.**
  - **Threshold** — photon energy below \(E_g\): interband conversion without assistance does not occur. The gate is rounded by an exponential foot of 7.5 meV per e-fold in GaAs at room temperature, and in silicon by phonon-assisted absorption that is still measurable 87 meV below the gap.
  - **Crossover** — opacity of a given sample: the transmitted fraction is \(e^{-\alpha L}\), and \(\alpha\) in silicon changes by 2.9 × 10⁵ between 550 and 1200 nm. The wavelength at which a sample turns opaque depends on its thickness.
  - **Crossover** — disorder: the Urbach energy grows from 7.5 meV in a GaAs crystal to 50–150 meV in amorphous silicon. The edge widens; it does not vanish at a threshold.
  - **Crossover** — temperature: \(E_g(T)\) follows the Varshni form and the Urbach energy rises linearly with temperature.

- **Emergent constant or stable output.** A material-specific absorption edge separating a transmitting window from an opaque band in an intact gapped lattice.

### 4.6 Internal Consistency Notes

The mapping is the photoelectric-class energy gate moved into a bulk crystal. [Photoconductivity](photoconductivity.md) is the same gate read as current; the two entries share \(E_g\). [X-ray-absorption-edge](x-ray-absorption-edge.md) is the same pattern at inner-shell energies and [ionization-threshold](ionization-threshold.md) is the atomic analogue.

Sourcing changed the gaps only in the third digit (Ge 0.661 eV, GaAs 1.424 eV, diamond 5.46–5.6 eV) and changed the description of the edge. The first version called the gate sharp and said melting or amorphizing destroys it. The measured edge of silicon is a continuous fall with no step at \(E_g\), and disorder widens the edge by a measured amount. The gate energy is still a threshold for unassisted conversion; the opacity of a sample is a crossover in \(\alpha L\). The first version's exciton figures and the statement about melting are dropped for lack of an opened source.

QSA takes the measured \(E_g\) as the specification and does not derive it. Indirect edges need a phonon, which accounts for the slow rise of \(\alpha\) in Si and Ge within the same family.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(E_g\) is a handbook-grade energy gate and the translation is the same conversion family as the photoelectric threshold. The grade is for the gate energy; the observed edge is rounded and, in an indirect crystal, gradual.

## Related entries

- [photoconductivity](photoconductivity.md) — the same \(E_g\) gate, read out as a current instead of as opacity
- [photoelectric-threshold](photoelectric-threshold.md) — surface ejection gate in a metal; same family, different hardware
- [ionization-threshold](ionization-threshold.md) — atomic binding gate; the isolated-node analogue of \(E_g\)
- [x-ray-absorption-edge](x-ray-absorption-edge.md) — inner-shell version of the same pattern, at keV
- [work-function-thermionic](work-function-thermionic.md) — surface barrier opened by heat rather than by a photon
- [refraction-dielectric](refraction-dielectric.md) — below-gap response: the lattice polarizes and does not convert
- [plasma-frequency-cutoff](plasma-frequency-cutoff.md) — a collective frequency gate, not a single-electron energy gate
- [blackbody-spectrum](blackbody-spectrum.md) — thermal photon population that may sit above or below \(E_g\)

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Ioffe Institute, "NSM Archive: Silicon, band structure and carrier concentration"](http://www.ioffe.ru/SVA/NSM/Semicond/Si/bandstr.html) | full-text | Secondary compilation: Si gap 1.12 eV, direct gap 3.4 eV, Varshni fit. |
| S2 | [Ioffe Institute, "NSM Archive: Germanium, band structure and carrier concentration"](http://www.ioffe.ru/SVA/NSM/Semicond/Ge/bandstr.html) | full-text | Secondary compilation: Ge gap 0.661 eV, direct gap 0.8 eV, Varshni fit. |
| S3 | [Ioffe Institute, "NSM Archive: Gallium arsenide, band structure and carrier concentration"](http://www.ioffe.ru/SVA/NSM/Semicond/GaAs/bandstr.html) | full-text | Secondary compilation: GaAs gap 1.424 eV, Varshni fit. |
| S4 | [Ioffe Institute, "NSM Archive: Diamond, band structure and carrier concentration"](http://www.ioffe.ru/SVA/NSM/Semicond/Diamond/bandstr.html) | full-text | Secondary compilation: diamond gap 5.46–5.6 eV and its temperature coefficient. |
| S5 | [PVEducation, "Optical properties of silicon", table from Green and Keevers, *Prog. Photovolt.* 3, 189 (1995)](https://www.pveducation.org/pvcdrom/materials/optical-properties-of-silicon) | full-text | Secondary reproduction of the 300 K absorption coefficient of silicon, 400–1200 nm. |
| S6 | [Johnson and Tiedje, "Temperature dependence of the Urbach edge in GaAs", *J. Appl. Phys.* 78, 5609 (1995)](https://asu.elsevierpure.com/en/publications/temperature-dependence-of-the-urbach-edge-in-gaas) | abstract | Urbach energy 7.5 meV at room temperature rising linearly to 12.4 meV at 700 °C in semi-insulating GaAs. |
| S7 | [Wikipedia, "Urbach energy"](https://en.wikipedia.org/wiki/Urbach_energy) | full-text | Tertiary: Urbach energies of hydrogenated amorphous silicon typically 50–150 meV at room temperature. |
