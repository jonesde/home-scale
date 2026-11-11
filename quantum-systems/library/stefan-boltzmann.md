---
id: stefan-boltzmann
title: Stefan–Boltzmann Law (Integrated Thermal Radiance)
status: formal
family: ensemble-averages
constraints:
  - thermal
  - spatial-buffer
confidence_data: high
confidence_mapping: medium
review_depth: light
related:
  - blackbody-spectrum
  - thermal-equilibrium-temperature
  - reflection
  - work-function-thermionic
  - photoelectric-threshold
updated: 2026-11-11
---

# Stefan–Boltzmann Law (Integrated Thermal Radiance)

### 4.1 Effect Name

Stefan–Boltzmann law (integrated thermal radiance)

### 4.2 Macroscopic Observation

A hot black surface radiates a power per unit area that rises as the fourth power of its temperature: doubling \(T\) multiplies the exitance by sixteen. A polished metal at the same \(T\) radiates much less. A grey surface (emissivity constant in frequency and below one) follows \(T^{4}\) with a reduced prefactor; a selective surface does not. An emitter thinner than the thermal wavelength does not follow \(T^4\).

### 4.3 Established Quantitative Boundaries

- **Convention.** Stefan–Boltzmann constant \(\sigma = 5.670374419\times 10^{-8}\,\mathrm{W\,m^{-2}\,K^{-4}}\), exact, since it is fixed by the defined \(h\), \(k\) and \(c\) [S1].
- **Model (Planck distribution).** Integrating the Planck law over wavelength gives the total hemispherical emissive power of a black body, \(\sigma T^4\) [S2][S3]. A real surface emits \(\varepsilon\sigma T^4\), where the total emissivity \(\varepsilon\) is the ratio of its emissive power to the black body's; the black body is a perfect emitter and absorber [S3].
- **Computed here.** At 300 K, \(\sigma T^{4} = 459\,\mathrm{W\,m^{-2}}\). Net black-body exchange from 300 K to 77 K, \(\sigma(T_1^4-T_2^4) = 457\,\mathrm{W\,m^{-2}}\), matching the figure in [S3].
- **Measured.** Total emissivity at 300 K: black paint on copper 0.94; polished aluminium 0.05; polished copper 0.10; polished stainless steel 0.17. Emissivity falls with temperature (polished aluminium 0.018 at 4.2 K) and rises with oxidation and dirt [S3].
- **Computed here.** Polished aluminium at 300 K with \(\varepsilon=0.05\) emits \(23\,\mathrm{W\,m^{-2}}\).
- **Convention.** The band that carries the energy is located by \(\lambda_{\max}T = 2.897772\times10^{-3}\,\mathrm{m\,K}\) [S5].
- **Computed here.** \(\lambda_{\max} = 9.66\,\mu\mathrm{m}\) at 300 K.
- **Measured.** Small emitter. A silica fibre of diameter \(500\pm50\,\mathrm{nm}\), thinner than the thermal wavelength, radiates with a power that rises more slowly than \(T^3\); the \(T^4\) surface law fails for it and a fluctuational-electrodynamics model that treats emission as a volume effect agrees with the data [S4].

**Data confidence:** High for \(\sigma\) and the \(T^4\) law. Medium for emissivities, which are one table for particular finishes. Kirchhoff's equality of spectral emissivity and absorptivity, stated in the first version, was not opened as such; only the black body as perfect emitter and absorber is cited.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- \(\sigma\) as the integral of the [Planck](blackbody-spectrum.md) function:

  \[
  \sigma = \frac{2\pi^{5}k^{4}}{15 c^{2}h^{3}}
  \]

  equivalent to the energy-density constant \(a=\pi^2k^4/15\hbar^3c^3\) of [S2] through \(\sigma = ac/4\).
- Real surface: \(j=\varepsilon\sigma T^{4}\) [S3]. With \(\varepsilon\) independent of frequency this is the grey body.
- Exchange between two surfaces: \(q_{12}=\sigma(T_1^4-T_2^4)\) divided by a sum of surface and view-factor resistances; for black surfaces that face only each other it reduces to \(\sigma(T_1^4-T_2^4)\) per unit area [S3].

These relations describe the integrated output of a thermal electromagnetic population. They fix no radiating area.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The same statistical electromagnetic population as the [blackbody spectrum](blackbody-spectrum.md), read as one integrated current. Two buffers, neither a universal number:
  1. The surface must have \(\varepsilon\approx1\) across the band that carries the energy.
  2. The object must be large compared with \(\lambda_{\max}(T)\), about 10 µm at 300 K.

- **Clock rate / latency.** No clock beyond the wall's own exchange window and the spectral content set by \(kT/h\). The \(T^4\) law is a time-averaged power.

- **Energy barriers or thresholds.** None. A high-[reflectivity](reflection.md) metal fails the black boundary condition; it stores nothing.

- **Dominant failure modes.**
  - **Crossover** — surface: output scales with \(\varepsilon\), from 0.94 (black paint) to 0.05 (polished aluminium) at 300 K; if \(\varepsilon\) varies across the band the temperature law is no longer \(T^4\).
  - **Crossover** — size: below \(\lambda_{\max}(T)\) emission becomes a volume effect and the exponent falls (500 nm silica fibre: below 3). Scale \(\lambda_{\max}T=2898\,\mu\mathrm{m\,K}\).
  - **Crossover** — thermal: \(j\propto T^4\) falls continuously to zero with \(T\); the cut is the instrument floor.
  - **Crossover** — undefined wall \(T\): inherited from the temperature entry.

- **Emergent constant or stable output.** The exitance \(j=\varepsilon\sigma T^{4}\) of a thermal surface.

### 4.6 Internal Consistency Notes

This entry is the integral of [blackbody spectrum](blackbody-spectrum.md) and shares its buffer, clock and failure class. The extra failure, a surface that is not black, is a boundary condition on the same population. [Reflection](reflection.md) and [plasma-frequency cutoff](plasma-frequency-cutoff.md) explain why a metal fails it.

Sourcing changed no numbers beyond precision. The metal emissivity range "a few percent" is now 0.05–0.17 for the polished finishes opened, and the small-object failure rests on one measured case with a stated exponent.

\(\sigma\) is a combination of defined constants. Treating it as an independent machine constant would double-count \(k\) and \(h\).

Thermionic emission from the same hot surface is a charged-particle gate ([work-function / thermionic](work-function-thermionic.md)), not a photon-current integral.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the \(T^{4}\) law, the exact \(\sigma\) and the non-black and small-object departures are established; the translation inherits the spectrum entry's lack of a universal size.

## Related entries

- [Blackbody spectrum](blackbody-spectrum.md) — the curve whose integral is this law
- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the wall average that \(T^{4}\) reports
- [Reflection](reflection.md) — high reflectance, low emissivity
- [Work function / thermionic emission](work-function-thermionic.md) — charged-particle output of a hot surface
- [Photoelectric threshold](photoelectric-threshold.md) — single-electron optical gate on the same metals

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [NIST, CODATA 2022 recommended values: Stefan–Boltzmann constant](https://physics.nist.gov/cgi-bin/cuu/Value?sigma) | full-text | σ = 5.670374419e-8 W m⁻² K⁻⁴, exact. |
| S2 | [Merhav, "Statistical Physics: a Short Course for Electrical Engineering Students", arXiv:1307.5137, §5.4](https://arxiv.org/abs/1307.5137) | full-text | Energy density aT⁴ with a = π²k⁴/15ħ³c³ from the Planck law. Lecture notes, secondary. |
| S3 | [Baudouy, "Heat Transfer and Cooling Techniques at Low Temperature", arXiv:1501.07153, §2.2](https://arxiv.org/abs/1501.07153) | full-text | σT⁴ as the integral of Planck's law; definition of emissivity; Table 4 emissivities; two-surface exchange formula; 457 W/m² from 300 K to 77 K. Lecture, secondary. |
| S4 | [Wuttke and Rauschenbeutel, *Phys. Rev. Lett.* 111, 024301 (2013), arXiv:1209.0536](https://arxiv.org/abs/1209.0536) | full-text | 500 nm silica fibre: radiated power scaling below T³, failure of the Stefan–Boltzmann surface law. |
| S5 | [NIST, CODATA 2022 recommended values: Wien wavelength displacement law constant](https://physics.nist.gov/cgi-bin/cuu/Value?bwien) | full-text | b = 2.897771955e-3 m K, exact. |
