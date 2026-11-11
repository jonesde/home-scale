---
id: photoconductivity
title: Photoconductivity (Gap Gate, Current Readout)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - clock-latency
  - thermal
confidence_data: high
confidence_mapping: high
review_depth: light
related:
  - semiconductor-gap-absorption
  - photoelectric-threshold
  - work-function-thermionic
  - ionization-threshold
  - dielectric-breakdown
  - refraction-dielectric
  - johnson-nyquist-noise
  - x-ray-absorption-edge
updated: 2026-11-11
---

# Photoconductivity (Gap Gate, Current Readout)

### 4.1 Effect Name

Photoconductivity (gap gate, current readout)

### 4.2 Macroscopic Observation

A semiconductor or insulator that carries a small dark current conducts better while it is illuminated with light above a material-specific edge, and reverts when the light is removed. The readout is a current between contacts; no electron leaves the solid. The long-wavelength limit of the response follows the absorption edge of the crystal, or lies far beyond it when a shallow impurity level supplies the carriers.

### 4.3 Established Quantitative Boundaries

- **Measured.** Gaps at 300 K, as in [semiconductor-gap-absorption](semiconductor-gap-absorption.md): Si 1.12 eV [S1], Ge 0.661 eV [S2], GaAs 1.424 eV [S3].
- **Measured.** Absorption of photons with energy above the gap generates electron–hole pairs, which the bias separates. The gap sets the absorption edge, and for detectors that rely on pair generation the absorption edge defines the longest detectable wavelength [S5]. Intrinsic germanium, with a 0.67 eV gap, cuts off at 1.8 µm [S4].
- **Computed here.** \(hc/E_g\) for Ge at 0.661 eV is 1876 nm, 4 % from the quoted 1.8 µm cutoff.
- **Measured.** Extrinsic response. Doping with shallow levels extends the response: gallium-doped germanium cuts off near 115 µm and is operated at 1.8 K; uniaxial stress extends the cutoff further [S4].
- **Computed here.** A 115 µm cutoff is a gate of 10.8 meV, 1.6 % of the germanium gap. That energy equals \(k_BT\) at 125 K, and is 70 \(k_BT\) at the 1.8 K operating temperature.
- **Measured.** Carrier lifetimes span six orders of magnitude: about 5 × 10⁻⁹ s for electrons in p-type GaAs and about 3 × 10⁻⁶ s for holes in GaAs [S3]; at least 10⁻³ s in pure Ge [S2].
- **Model (lifetime over transit time).** Photoconductive gain is the ratio of the photocarrier lifetime to the transit time, with transit time \(L^2/(\mu V)\) for contact spacing \(L\), mobility \(\mu\) and bias \(V\) [S5].
- **Model (thermal carriers).** The intrinsic carrier density, the source of dark current, varies as \(e^{-E_g/2k_BT}\) [S1].
- **Computed here.** For silicon at 300 K, \(E_g/2k_BT\) is 21.7.

**Data confidence:** High that the optical gate is \(E_g\) or an impurity depth; the statement is a working rule of detector practice and was read in a review [S5] and a detector summary [S4]. Lifetimes are sample-specific; the figures are compilation values [S2][S3]. No measured photocurrent spectrum was opened.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Onset: \(h\nu \ge E_g\) (intrinsic) or \(h\nu \ge E_t\) (extrinsic, impurity depth \(E_t\)).
- Excess density and conductivity for generation rate \(G\) and lifetime \(\tau\):

  \[
  \Delta n = G\tau,\qquad \Delta\sigma = e\,(\Delta n\,\mu_n + \Delta p\,\mu_p)
  \]

- Gain [S5]:

  \[
  \Gamma = \frac{\tau}{t_\mathrm{tr}} = \frac{\tau\mu V}{L^2}
  \]

- Generation in a layer follows the absorbed flux, \(1 - e^{-\alpha L}\) of the incident light.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One absorbed photon promotes one electron and leaves a hole. A measurable current is the summed drift of the generated population between contacts. The crystal must support bands or defined impurity levels and must be contacted. Thinning the absorber reduces the generation in proportion to \(1 - e^{-\alpha L}\).

- **Clock rate / latency.** The readout clocks are the lifetime \(\tau\) (5 ns to more than 1 ms in the materials listed) and the transit time. Modulation faster than \(1/\tau\) rolls off the photocurrent. Gain is the ratio of the two clocks.

- **Energy barriers or thresholds.** The operating gate is \(E_g\), or the impurity depth \(E_t\) (10.8 meV for Ge:Ga). Bias reads the carriers and does not replace the gate. Thermal generation across the same gate produces the dark current.

- **Dominant failure modes.**
  - **Threshold** — photon energy below \(E_g\) or \(E_t\): no pair generation in this channel. The gate inherits the rounding of the absorption edge recorded in [semiconductor-gap-absorption](semiconductor-gap-absorption.md).
  - **Crossover** — lifetime: the signal scales with \(\tau\) through \(\Delta n = G\tau\) and through the gain \(\tau/t_\mathrm{tr}\).
  - **Crossover** — temperature: thermal carriers grow as \(e^{-E_g/2k_BT}\) (or with \(E_t\) in place of \(E_g\)) and bury the photocurrent. A 10.8 meV gate is operated at 1.8 K.
  - **Crossover** — contacts and bias: the current is proportional to the bias through the transit time; with no field the carriers recombine unread.

- **Emergent constant or stable output.** A light-dependent conductance whose spectral limit follows \(E_g\) or \(E_t\), with a size set by absorption, lifetime and mobility, which reverts when generation stops.

### 4.6 Internal Consistency Notes

The mapping is [semiconductor-gap-absorption](semiconductor-gap-absorption.md) with a different output channel, and the two files share the gate energy. They differ in what is counted. Absorption with no photocurrent (short lifetime, blocking contacts) and photocurrent with little opacity (a thin extrinsic layer) are both allowed.

Sourcing changed no gap beyond the third digit. It added the extrinsic case as a number (115 µm, 10.8 meV for Ge:Ga) and measured lifetimes, and it replaced the first version's "nanoseconds to milliseconds in high-purity Si" with compilation values for GaAs and Ge; no silicon lifetime was opened. The diamond gap is left to the absorption entry. The contrast with a thickness floor for mirrors is removed; [reflection](reflection.md) has no such floor.

[Photoelectric-threshold](photoelectric-threshold.md) and [work-function-thermionic](work-function-thermionic.md) eject the carrier into vacuum; this entry keeps it in the solid. [Johnson–Nyquist-noise](johnson-nyquist-noise.md) is the thermal electrical baseline against which a small photocurrent is read.

QSA does not derive \(\tau\). Lifetime and gain are performance data of a sample. The threshold mapping does not depend on them.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the response limit is \(E_g\) or an impurity depth, and the gate is the same conversion as gap absorption. Lifetime, gain and dark current are crossovers that set the size of the output, not its threshold.

## Related entries

- [semiconductor-gap-absorption](semiconductor-gap-absorption.md) — the same \(E_g\) gate, read as opacity rather than as current
- [photoelectric-threshold](photoelectric-threshold.md) — ejection into vacuum over a work function, not internal conduction
- [work-function-thermionic](work-function-thermionic.md) — heat-opened surface ejection; contrast case
- [ionization-threshold](ionization-threshold.md) — gas-phase unbinding; no lattice band structure required
- [dielectric-breakdown](dielectric-breakdown.md) — field-opened, often destructive conversion of the same insulator
- [refraction-dielectric](refraction-dielectric.md) — below-gap polarization without free-carrier generation
- [johnson-nyquist-noise](johnson-nyquist-noise.md) — thermal electrical floor of the readout
- [x-ray-absorption-edge](x-ray-absorption-edge.md) — inner-shell conversion; X-ray photoconductivity is this readout on that gate

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Ioffe Institute, "NSM Archive: Silicon, band structure and carrier concentration"](http://www.ioffe.ru/SVA/NSM/Semicond/Si/bandstr.html) | full-text | Secondary compilation: Si gap 1.12 eV; intrinsic carrier density proportional to exp(−Eg/2kT). |
| S2 | [Ioffe Institute, "NSM Archive: Germanium" (band structure and electrical properties pages)](http://www.ioffe.ru/SVA/NSM/Semicond/Ge/electric.html) | full-text | Secondary compilation: Ge gap 0.661 eV; longest carrier lifetimes of at least 1 ms. |
| S3 | [Ioffe Institute, "NSM Archive: Gallium arsenide" (band structure and electrical properties pages)](http://www.ioffe.ru/SVA/NSM/Semicond/GaAs/electric.html) | full-text | Secondary compilation: GaAs gap 1.424 eV; longest lifetimes about 5 ns (electrons, p-type) and 3 µs (holes). |
| S4 | [Young, "Germanium Detectors for the Far-Infrared", Steward Observatory, STScI space-detectors meeting](https://www.stsci.edu/stsci/meetings/space_detectors/gdfi.htm) | full-text | Intrinsic Ge gap 0.67 eV with a 1.8 µm cutoff; Ge:Ga cutoff near 115 µm, operated at 1.8 K; stress extends the cutoff. The page prints micrometres as "mm". |
| S5 | [Buscema et al., "Photocurrent generation with two-dimensional van der Waals semiconductors", *Chem. Soc. Rev.* 44, 3691 (2015), arXiv:1506.00679](https://arxiv.org/pdf/1506.00679) | full-text | Review: photons above the gap generate pairs separated by the bias; the absorption edge defines the longest detectable wavelength; gain as lifetime over transit time, with transit time L²/(μV). Journal reference not re-opened. |
