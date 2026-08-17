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
related:
  - semiconductor-gap-absorption
  - photoelectric-threshold
  - work-function-thermionic
  - ionization-threshold
  - dielectric-breakdown
  - refraction-dielectric
  - johnson-nyquist-noise
  - x-ray-absorption-edge
updated: 2026-08-17
---

# Photoconductivity (Gap Gate, Current Readout)

### 4.1 Effect Name

Photoconductivity (gap gate, current readout)

### 4.2 Macroscopic Observation

A semiconductor or insulator that carries only a small dark current becomes a better conductor while it is illuminated with light above a material-specific edge, and reverts when the light is removed. The sample does not have to eject electrons into vacuum and does not have to become opaque to be counted: the readout is a current (or a conductance) between contacts. Below the edge, extra light of that colour does not raise the current through this channel. The same crystal’s absorption edge and its photoconductive edge sit at the same gap, or at a shallower trap depth if the conversion is extrinsic.

### 4.3 Established Quantitative Boundaries

- Intrinsic photoconductivity is gated by the same gaps as [semiconductor-gap-absorption](semiconductor-gap-absorption.md): Si \(E_g \approx 1.12\,\mathrm{eV}\), Ge \(\approx 0.66\,\mathrm{eV}\), GaAs \(\approx 1.42\,\mathrm{eV}\), diamond \(\sim 5.5\,\mathrm{eV}\) (all \(300\,\mathrm{K}\)). The photocurrent turns on with \(h\nu > E_g\) (direct) or with the phonon-assisted indirect onset.
- Extrinsic photoconductivity is gated by a trap or impurity depth \(E_t < E_g\). Infrared response of doped Ge, Si, and similar hosts is this shallower gate, not a second family.
- Excess conductance tracks generation and recombination:

  \[
  \Delta n = G\tau,\qquad
  \Delta\sigma = e\,(\Delta n\,\mu_n + \Delta p\,\mu_p)
  \]

  with \(G\) the pair-generation rate and \(\tau\) the recombination lifetime. \(\tau\) is a performance metric, not a threshold: it spans nanoseconds in many direct-gap or dirty samples to milliseconds in high-purity Si. No single universal \(\tau\) is claimed.
- Photoconductive gain (descriptive performance metric):

  \[
  \Gamma = \tau / t_{\mathrm{tr}} = \tau\mu V / L^2
  \]

  Large \(\Gamma\) means a carrier lives through many transits. It multiplies the current; it does not move \(E_g\).
- Dark current is the below-threshold (or thermal-across-the-gap) baseline. Raising \(T\) raises dark current and can bury the photocurrent; that is a thermal failure of *readout*, not a shift of the optical gate to zero.

**Data confidence:** High — the identity of the optical gate with \(E_g\) (or \(E_t\)) is multiply reproduced. Gain and lifetime are high as a class and sample-specific as numbers.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Onset:

  \[
  h\nu \ge E_g \quad\text{(intrinsic)}\qquad\text{or}\qquad h\nu \ge E_t \quad\text{(extrinsic)}
  \]

- Generation in a layer of absorption coefficient \(\alpha\) and quantum yield \(\eta\), incident flux \(\Phi\):

  \[
  G(x) = \eta\alpha\Phi\,\mathrm{e}^{-\alpha x}
  \]

- Steady-state excess density \(\Delta n = G\tau\) when monomolecular recombination at lifetime \(\tau\) dominates. Other recombination laws change the *shape* of the light–current curve; they do not open a below-gap channel.
- Measured current under bias \(V\) is the contact-to-contact integral of \(\sigma E\). Without a readout field or a junction, the generated carriers still exist and still recombine; the *photoconductive* observable is the current.

Below \(E_g\) (or \(E_t\)) this conversion does not occur. That non-occurrence is the collapse of the effect. Sub-gap current, if any, is thermal, two-photon, or defect-assisted — other channels.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The conversion event is one absorbed photon promoting one electron (and a hole) across \(E_g\) or \(E_t\). A measurable current is the summed drift of a large generated population between contacts. The crystal must be intact enough to support bands or defined traps, and contacted. There is no collective optical-buffer analogue of the 10–20 nm mirror; thinning the absorber reduces the generation volume in proportion to \(1-\mathrm{e}^{-\alpha L}\).

- **Clock rate / latency.** Generation follows the optical cycle (femtoseconds). The *readout* clock is the recombination lifetime \(\tau\) and the transit time \(t_{\mathrm{tr}}\). Chopping faster than \(1/\tau\) rolls off the photocurrent. Gain \(\Gamma = \tau/t_{\mathrm{tr}}\) is exactly this pair of clocks written as a performance number.

- **Energy barriers or thresholds.** The operating gate is \(E_g\) (intrinsic) or \(E_t\) (extrinsic). It is the same energetic lock as gap absorption. Bias does not replace the gate; it only reads the carriers. Thermal generation across the same gate produces dark current.

- **Dominant failure modes.**
  - Under-threshold: \(h\nu < E_g\) (or \(< E_t\)) → this conversion does not occur. Conductance stays at the dark baseline.
  - Clock: \(\tau\) too short → generated carriers vanish before they contribute a measurable \(\Delta\sigma\). The gate opened; the output did not last.
  - Thermal: \(kT\) comparable to the gate, or a large dark population, buries \(\Delta\sigma\) in baseline and noise.
  - Contacts / geometry: blocking contacts or a vanished bias remove the current *readout* without closing \(E_g\). That failure belongs to observation, not to the conversion.
  - Over-field: approaching [dielectric-breakdown](dielectric-breakdown.md) destroys the lattice. That is a different, usually irreversible, conversion.

- **Emergent constant or stable output.** A light-dependent conductance whose spectral onset tracks \(E_g\) or \(E_t\), with a magnitude set by \(\eta\), \(\alpha\), \(\tau\), and \(\mu\), reverting when generation stops.

### 4.6 Internal Consistency Notes

The mapping is [semiconductor-gap-absorption](semiconductor-gap-absorption.md) with a different output channel. The two files must share the same collapse energy. They differ in what is counted: opacity vs. current. Absorption without photocurrent (very short \(\tau\), bad contacts) and photocurrent without strong opacity (thin, weakly absorbing extrinsic layers) are both allowed and are not contradictions.

[Photoelectric-threshold](photoelectric-threshold.md) and [work-function-thermionic](work-function-thermionic.md) eject the carrier into vacuum; this entry keeps it inside the solid. [Ionization-threshold](ionization-threshold.md) is the gas-phase analogue. [Johnson–Nyquist-noise](johnson-nyquist-noise.md) is the thermal electrical baseline against which a small photocurrent has to be read.

A remaining gap: QSA does not here derive \(\tau\) from a primitive node count. Lifetime is taken as a measured recombination resource. Gain figures of a given detector are therefore performance data, not predicted constants. The threshold mapping does not depend on closing that derivation.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the current turns on at a measured \(E_g\) or trap depth, below-threshold darkness is the observed non-occurrence, and the gate is the same photoelectric-class conversion as gap absorption.

## Related entries

- [semiconductor-gap-absorption](semiconductor-gap-absorption.md) — the same \(E_g\) gate, read as opacity rather than as current
- [photoelectric-threshold](photoelectric-threshold.md) — ejection into vacuum over a work function, not internal conduction
- [work-function-thermionic](work-function-thermionic.md) — heat-opened surface ejection; contrast case
- [ionization-threshold](ionization-threshold.md) — gas-phase unbinding; no lattice band structure required
- [dielectric-breakdown](dielectric-breakdown.md) — field-opened, often destructive conversion of the same insulator
- [refraction-dielectric](refraction-dielectric.md) — below-gap polarization without free-carrier generation
- [johnson-nyquist-noise](johnson-nyquist-noise.md) — thermal electrical floor of the readout
- [x-ray-absorption-edge](x-ray-absorption-edge.md) — inner-shell conversion; X-ray photoconductivity is this readout on that gate
