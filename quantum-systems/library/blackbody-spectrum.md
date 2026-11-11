---
id: blackbody-spectrum
title: Blackbody Spectrum (Thermal Electromagnetic Output)
status: formal
family: ensemble-averages
constraints:
  - thermal
  - clock-latency
  - spatial-buffer
confidence_data: high
confidence_mapping: medium
review_depth: light
related:
  - stefan-boltzmann
  - thermal-equilibrium-temperature
  - photoelectric-threshold
  - work-function-thermionic
  - plasma-frequency-cutoff
updated: 2026-11-11
---

# Blackbody Spectrum (Thermal Electromagnetic Output)

### 4.1 Effect Name

Blackbody spectrum (thermal electromagnetic output)

### 4.2 Macroscopic Observation

A heated cavity with a small port, or a surface that absorbs all incident radiation, emits a smooth spectrum that depends only on the temperature of the walls. Raising \(T\) moves the peak to shorter wavelength and raises the whole curve. The same curve is recovered from different cavities at the same \(T\). A surface that is not black (polished metal, a selective coating) emits less, with a different shape. An emitter smaller than the wavelengths that carry the energy does not follow the black-body form.

### 4.3 Established Quantitative Boundaries

- **Convention.** \(h = 6.62607015\times10^{-34}\,\mathrm{J\,s}\) and \(k = 1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}\) are exact [S1]. The Wien wavelength-displacement constant follows from them: \(\lambda_{\max}T = 2.897772\times10^{-3}\,\mathrm{m\,K}\) [S2].
- **Computed here.** \(\lambda_{\max}\) is 9.66 µm at 300 K, 502 nm at the nominal solar effective temperature 5772 K [S3], and 1.06 mm at 2.725 K.
- **Computed here.** \(kT/h = 6.25\,\mathrm{THz}\) at 300 K. Mode occupancy is of order one where \(h\nu\sim kT\).
- **Model (Planck distribution).** For \(h\nu\ll kT\) the spectrum follows the Rayleigh–Jeans form \(\propto\nu^2kT\); for \(h\nu\gg kT\) it falls as \(\nu^3e^{-h\nu/kT}\). The classical form extended to all frequencies gives a divergent total (the "ultraviolet catastrophe") [S4].
- **Measured.** The cosmic microwave background spectrum measured by FIRAS deviates from a black body by less than 50 parts per million of the peak (rms) [S5]; its temperature is \(2.72548\pm0.00057\,\mathrm{K}\) [S6].
- **Measured.** Small emitter. A silica fibre 500 nm in diameter, thinner than the thermal wavelength, thermalizes by far-field radiation in agreement with a fluctuational-electrodynamics model that treats emission as a volume effect; the Planck surface law fails, and the radiated power rises more slowly than \(T^3\) where the black-body law gives \(T^4\) [S7].
- **Measured.** Non-black surfaces. Total emissivity at 300 K: black paint 0.94, polished aluminium 0.05, polished copper 0.10, polished stainless steel 0.17 [S8].

**Data confidence:** High — the constants are exact, the Planck form is textbook, and the FIRAS limit and fibre experiment were read at source. The emissivity values are one cryogenics table for particular finishes. The first version's statement that shape-dependent mode-density corrections are measured in micromachined and cryogenic resonators was not sourced and is dropped.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Planck energy density per unit frequency [S4]:

  \[
  u(\nu,T) = \frac{8\pi h\nu^{3}}{c^{3}}\frac{1}{e^{h\nu/kT}-1}
  \]

- Rayleigh–Jeans limit (\(h\nu\ll kT\)): \(u\approx 8\pi\nu^{2}kT/c^{3}\).
- Wien displacement as above, for the per-wavelength peak. The per-frequency peak sits at a different constant.
- The frequency integral gives \(u\propto T^4\), the [Stefan–Boltzmann](stefan-boltzmann.md) law [S4].

\(h\) and \(k\) are defined SI constants. The Planck function is a descriptive fit to the stable spectral output.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A thermal electromagnetic population over a dense set of modes, coupled to a wall that itself has a stable [temperature](thermal-equilibrium-temperature.md). The scale is statistical and geometric: the emitter or cavity must be large compared with the wavelengths that carry the energy (about 10 µm at 300 K, about 1 mm at 2.7 K). No universal volume exists; the scale tracks \(\lambda_{\max}(T)\).

- **Clock rate / latency.** The spectral clock is \(kT/h\) (6.25 THz at 300 K). Frequencies well below it are in the Rayleigh–Jeans range; well above it they are exponentially empty. The wall must also have finished its own exchange.

- **Energy barriers or thresholds.** No latch. A metal wall that reflects ([reflection](reflection.md), [plasma-frequency cutoff](plasma-frequency-cutoff.md)) has emissivity below 1 and does not emit the Planck spectrum. That is a failed boundary condition, not a stored state.

- **Dominant failure modes.**
  - **Crossover** — size: as the emitter falls below \(\lambda_{\max}(T)\) the spectrum and the temperature scaling leave the black-body form (500 nm fibre: slower than \(T^3\)). The scale is \(\lambda_{\max}T = 2898\,\mu\mathrm{m\,K}\).
  - **Crossover** — surface: emission scales with \(\varepsilon(\nu)\), from 0.94 for black paint to 0.05 for polished aluminium at 300 K.
  - **Crossover** — undefined wall \(T\): inherited from the temperature entry (\(N^{-1/2}\) scatter, exchange window).
  - **Crossover** — spectral range: the Rayleigh–Jeans form departs from the measured curve as \(h\nu\) approaches \(kT\).

- **Emergent constant or stable output.** The Planck curve \(u(\nu,T)\) and its Wien peak, depending only on \(T\).

### 4.6 Internal Consistency Notes

The failure class is statistical and geometric, consistent with the family and with the [Stefan–Boltzmann](stefan-boltzmann.md) integral of the same curve.

Sourcing changed no numbers beyond precision (Wien constant 2897.77 µm K; solar temperature 5772 K). The small-cavity statement is now carried by one measured case, a sub-wavelength fibre, which shows a departure from the black-body law in an emitter and not a discrete-mode cavity spectrum; the few-mode cavity picture in the first version has no opened source and is kept only as mapping language. FIRAS numbers were added.

QSA takes the measured curve and the Wien product as the output specification. It does not derive \(h\) or the Planck occupation factor.

Photoemission from the same hot wall ([photoelectric threshold](photoelectric-threshold.md), [thermionic emission](work-function-thermionic.md)) is a single-electron energy gate, not a spectral average.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the Planck and Wien data and the small-emitter and non-black departures are measured; the translation names a statistical and geometric buffer and gives no universal size or derived \(h\).

## Related entries

- [Stefan–Boltzmann law](stefan-boltzmann.md) — frequency integral of this curve
- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the wall average the spectrum reports
- [Photoelectric threshold](photoelectric-threshold.md) — single-electron gate; contrast case
- [Work function / thermionic emission](work-function-thermionic.md) — charged-particle output of the same wall
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — why a metal wall is not black
- [Reflection](reflection.md) — high reflectance means low emissivity

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [NIST, CODATA 2022 recommended values: Planck constant (and Boltzmann constant, Value?k)](https://physics.nist.gov/cgi-bin/cuu/Value?h) | full-text | h and k, exact. |
| S2 | [NIST, CODATA 2022 recommended values: Wien wavelength displacement law constant](https://physics.nist.gov/cgi-bin/cuu/Value?bwien) | full-text | b = 2.897771955e-3 m K, exact. |
| S3 | [Mamajek et al., "IAU 2015 Resolution B3 on Recommended Nominal Conversion Constants", arXiv:1510.07674](https://arxiv.org/abs/1510.07674) | full-text | Nominal solar effective temperature 5772 K. |
| S4 | [Merhav, "Statistical Physics: a Short Course for Electrical Engineering Students", arXiv:1307.5137, §5.4](https://arxiv.org/abs/1307.5137) | full-text | Planck law, Rayleigh–Jeans and Wien limits, ultraviolet catastrophe, T⁴ energy density. Lecture notes, secondary. |
| S5 | [Fixsen et al., "The Cosmic Microwave Background Spectrum from the Full COBE FIRAS Data Set", *Astrophys. J.* 473, 576 (1996), arXiv:astro-ph/9605054](https://arxiv.org/abs/astro-ph/9605054) | abstract | Rms deviation from a black body below 50 ppm of the peak. |
| S6 | [Fixsen, "The Temperature of the Cosmic Microwave Background", *Astrophys. J.* 707, 916 (2009), arXiv:0911.1955](https://arxiv.org/abs/0911.1955) | abstract | CMB temperature 2.72548 ± 0.00057 K. |
| S7 | [Wuttke and Rauschenbeutel, *Phys. Rev. Lett.* 111, 024301 (2013), arXiv:1209.0536](https://arxiv.org/abs/1209.0536) | full-text | 500 nm silica fibre: agreement with fluctuational electrodynamics, failure of the Planck prediction, power scaling below T³. |
| S8 | [Baudouy, "Heat Transfer and Cooling Techniques at Low Temperature", arXiv:1501.07153, Table 4](https://arxiv.org/abs/1501.07153) | full-text | Total emissivities of black paint and polished Al, Cu and stainless steel at 300 K, 78 K and 4.2 K. Lecture, secondary. |
