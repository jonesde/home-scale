---
id: quantum-point-contact
title: Quantum Point Contact (1D Conductance Steps)
status: formal
family: gapped-coherence
constraints:
  - spatial-buffer
  - thermal
  - field-threshold
confidence_data: high
confidence_mapping: medium
review_depth: light
related:
  - quantum-hall-effect
  - cyclotron-resonance
  - coulomb-blockade
updated: 2026-11-11
---

# Quantum Point Contact (1D Conductance Steps)

### 4.1 Effect Name

Quantum point contact (1D conductance steps)

### 4.2 Macroscopic Observation

A short, narrow constriction in a two-dimensional electron gas, defined by a split gate, shows steps in its conductance at integer multiples of one conductance quantum as the gate voltage widens the channel. Pinch-off gives near-zero conductance. Raising the temperature or adding scattering smears the steps. No magnetic field is needed.

### 4.3 Established Quantitative Boundaries

- **Convention.** Conductance quantum \(G_0 = 2e^2/h = 7.748\,091\,729\ldots\times10^{-5}\) S, exact since the 2019 SI [S1].
- **Computed here.** \(1/G_0 = 12\,906\,\Omega\) (the review rounds to 1/13 kΩ [S3]).
- **Measured.** Ballistic point contacts in a GaAs–AlGaAs two-dimensional electron gas, with no magnetic field applied, change conductance in steps of \(e^2/\pi\hbar\) (equal to \(2e^2/h\)) as the gate widens the contact; up to sixteen steps appear as the width goes from 0 to 360 nm [S2]. The Cambridge group reported the same in 1988 [S5]; that paper was not opened.
- **Model (waveguide, \(N \approx 2W/\lambda_F\)).** The constriction passes \(N\) transverse modes [S3]. **Computed here:** sixteen modes at 360 nm give \(\lambda_F \approx 45\) nm.
- **Measured.** The Fermi wavelength in this electron gas is a hundred times that of a metal (0.5 nm), so the opening can be comparable to the wavelength and much smaller than the impurity mean free path [S3].
- **Measured.** Accuracy and limits. Deviations from exact quantization in a real geometry are about 1 %, against better than 1 part in \(10^7\) for the Hall resistance. The causes are the series resistance of the wide regions and backscattering at the entrance and exit. A magnetic field suppresses the backscattering [S3].
- **Measured.** The steps smear out when the thermal energy becomes comparable to the energy separation of the modes [S3]. No temperature is quoted in the opened sources for the split-gate device.
- **Measured.** Metal contacts of atomic size, with \(\lambda_F \approx 0.5\) nm, show conductance steps near \(2e^2/h\) at room temperature [S3].
- **Measured.** A further feature at \(0.7\times 2e^2/h\) is attributed to electron–electron interaction and indicates spin polarization at zero field [S4]. It is not the primary artifact.

**Data confidence:** High for the steps, their value and the zero-field condition (original abstract and a review by the discoverers, read in full). Flatness in one device is Medium.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms. Landauer formula [S3]:

\[
G = \frac{2e^2}{h}\sum_n t_n, \qquad 0 \le t_n \le 1
\]

An ideal contact has \(N\) transmission eigenvalues equal to 1 and the rest 0. The gate voltage changes \(N \approx 2W/\lambda_F\). These relations describe the staircase; they do not derive \(h/e^2\) from a node count.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A ballistic constriction with an opening comparable to the Fermi wavelength (about 45 nm in GaAs; atomic in a metal) and shorter than the mean free path, between two wide reservoirs.

- **Clock rate / latency.** Transit through the constriction at the Fermi velocity. The DC staircase is not a radiated frequency.

- **Energy barriers or thresholds.** The transverse-mode edges open one at a time. Pinch-off is the last one closing. There is no pairing gap and no Landau gap.

- **Dominant failure modes.**
  - **Threshold** — gate: pinch-off, \(G \to 0\).
  - **Crossover** — thermal: steps smear when \(k_BT\) approaches the mode spacing. The spacing grows as the wavelength shrinks, which is why atomic metal contacts show steps at room temperature.
  - **Crossover** — scattering and length: each \(t_n\) falls below 1 continuously with backscattering; about 1 % deviation in a clean device.
  - **Threshold** — buffer: no electron gas, no reservoirs.

- **Emergent constant or stable output.** A conductance near \(N\times 2e^2/h\), accurate to about 1 %, inside the envelope.

### 4.6 Internal Consistency Notes

This is not [quantum-hall-effect](quantum-hall-effect.md). The Hall plateau needs a normal field component, a bulk gap and an edge path, and is exact to parts in \(10^{10}\). The constriction needs no field and is good to about 1 %. The two share \(h\) and \(e\) and differ as machines.

Sourcing changed one thing and added one. The "tens of nanometres" width is a 45 nm Fermi wavelength, with sixteen steps resolved up to 360 nm, so a wider contact adds steps and does not end the staircase. The 1 % accuracy is new: it separates this output from a metrological constant. No numbers were contradicted.

The stack is draft `landauer-channel`. The contrast with `edge-channel` stays. The quantized value is taken from the Landauer description and metrology, the same class of underived output as \(R_K\).

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the steps, pinch-off and zero-field hardware are measured; \(2e^2/h\) is taken, and the 0.7 feature is unmapped.

## Related entries

- [quantum-hall-effect](quantum-hall-effect.md) — the other \(h,e\) transport leftover; needs a normal field
- [cyclotron-resonance](cyclotron-resonance.md) — same electron gas, different output
- [coulomb-blockade](coulomb-blockade.md) — another small-structure electron gate; charging, not modes

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [CODATA 2022, conductance quantum (NIST)](https://physics.nist.gov/cgi-bin/cuu/Value?conqu2e2sh) | full-text | Conductance quantum, exact. |
| S2 | [van Wees et al., *Phys. Rev. Lett.* 60, 848 (1988)](https://doi.org/10.1103/PhysRevLett.60.848) | abstract | Steps of e²/πħ with no magnetic field; sixteen steps from 0 to 360 nm. |
| S3 | [van Houten and Beenakker, *Physics Today* 49(7), 22 (1996), arXiv:cond-mat/0512609](https://arxiv.org/abs/cond-mat/0512609) | full-text | Review by the discoverers: mode count, Landauer formula, Fermi wavelength against a metal, mean free path, 1 % accuracy against 1 in 1e7, thermal smearing, field suppresses backscattering, atomic contacts at room temperature. |
| S4 | [Thomas et al., *Phys. Rev. Lett.* 77, 135 (1996)](https://doi.org/10.1103/PhysRevLett.77.135) | abstract | The 0.7 structure: interaction-induced, spin polarization at zero field. |
| S5 | [Wharam et al., *J. Phys. C* 21, L209 (1988)](https://doi.org/10.1088/0022-3719/21/8/002) | cited-only | Independent first observation; cited through the review. |
