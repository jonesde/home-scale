---
id: aharonov-bohm
title: Aharonov–Bohm Effect (Enclosed-Flux Phase)
status: formal
family: collective-field-response
constraints:
  - spatial-buffer
  - clock-latency
  - field-threshold
confidence_data: high
confidence_mapping: high
review_depth: light
related:
  - flux-quantization
  - josephson-effect
  - cyclotron-resonance
  - faraday-rotation
  - quantum-hall-effect
updated: 2026-11-11
---

# Aharonov–Bohm Effect (Enclosed-Flux Phase)

### 4.1 Effect Name

Aharonov–Bohm effect (enclosed-flux phase)

### 4.2 Macroscopic Observation

An electron interferometer whose two arms enclose a magnetic flux shows a shift of its interference fringes as the enclosed flux is changed, including when the field is shielded from the electron paths. The pattern is periodic in a flux quantum built from \(h\) and a single \(e\). A path that does not encircle the flux, or loss of phase coherence across the interferometer, removes the shift. Small normal-metal rings show the same period as oscillations of their resistance with applied field.

### 4.3 Established Quantitative Boundaries

- **Convention.** Single-charge flux period. With \(h\) and \(e\) exact in the SI, \(h/e\) is twice the tabulated magnetic flux quantum \(h/2e = 2.067\,833\,848\times10^{-15}\) Wb [S1]:

  \[
  \Phi_{\mathrm{AB}} = \frac{h}{e} = 4.135\,667\,696\times 10^{-15}\,\mathrm{Wb}
  \]

- **Model (quantum mechanics).** Phase difference between the two paths, set by the enclosed flux and not by the field along the paths [S4]:

  \[
  \Delta\varphi = \frac{q\Phi}{\hbar} = 2\pi\,\frac{\Phi}{\Phi_{\mathrm{AB}}}\quad (q = e)
  \]

- **Measured.** Electron-beam tests. The first claimed confirmation used a thin iron whisker (Chambers, 1960) [S4][S5]; several early results were later questioned because the electrons may not have been completely shielded from the field [S4]. In 1986 a toroidal magnet covered with a superconducting layer and then copper, so that the field was shielded from the electron wave, gave a measured phase shift between a beam through the hole and a beam outside; the same experiment gave direct evidence of flux quantization in the superconductor [S2].
- **Measured.** Solid-state rings. The magnetoresistance of submicron-diameter gold rings oscillates with period \(h/e\) in the enclosed flux, with a weaker \(h/2e\) component, and the oscillations persist to very large fields. Their amplitude depends on temperature [S3].
- **Computed here.** One period for a loop 1 µm in diameter is a field change of 5.3 mT.

**Data confidence:** High — the \(h/e\) value is exact and the shielded-toroid and metal-ring results were read in the primary abstracts. The 1960 letter was not opened beyond its title page, and the account of the early objections is from a tertiary page.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms. The line integral of \(\mathbf{A}\) around a closed path equals the enclosed flux, so \(\Delta\varphi = (e/\hbar)\oint\mathbf{A}\cdot d\mathbf{l}\). The interference intensity is periodic in \(\Phi/\Phi_{\mathrm{AB}}\). These describe the observed shift. They do not derive \(h/e\) from a node count.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two coherent paths that together enclose a flux, and a charge-\(e\) carrier whose coherence spans the loop. The loop is the buffer; the flux region inside it is not. A simply connected path is under-provisioned. Demonstrated loops run from electron-beam interferometers around a toroid to submicron metal rings.

- **Clock rate / latency.** The carrier's transit of the interferometer. Decoherence faster than that transit erases the shift.

- **Energy barriers or thresholds.** No latch. Enclosed flux is a field resource that sets a phase; it stores no directional moment.

- **Dominant failure modes.**
  - **Threshold** — topology: a path that does not enclose the flux shows no shift.
  - **Crossover** — field: the phase is linear in \(\Phi\) and the pattern periodic in \(h/e\); \(\Phi \to 0\) gives the unshifted pattern.
  - **Crossover** — coherence: the oscillation amplitude falls with temperature in metal rings; no scale filed.
  - **Threshold** — charge: \(\Delta\varphi = q\Phi/\hbar\) vanishes for \(q = 0\). A neutral interferometer does not acquire this phase.

- **Emergent constant or stable output.** A fringe shift, or a resistance oscillation, periodic in \(h/e\) while the loop, the coherence and the enclosed flux are maintained.

### 4.6 Internal Consistency Notes

The \(h/e\) period against the superconducting \(h/2e\) is a load-bearing distinction. This file owns the single-charge phase. [Flux quantization](flux-quantization.md) owns the pair increment.

Sourcing changed two statements; the \(h/e\) value did not change. The first version said the 1960 whisker experiment and the 1986 shielded toroid together established the field-free case; the early experiments were disputed on shielding, and the 1986 experiment is the one that excluded the field. The first version also treated "\(h/e\), not \(h/2e\)" as a clean split by hardware. Normal-metal rings show a weaker \(h/2e\) component alongside \(h/e\), and the shielded toroid used a superconductor whose own flux is quantized, so both periods can appear in one apparatus. The single-charge period is still the fundamental one in a normal conductor.

In a metal ring the field also passes through the metal, so the field-free condition belongs to the electron-beam experiments only.

Family assignment is by loss of collective phase or an under-provisioned loop, not by a pairing gap. This entry is not folded into `gapped-condensate`.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the \(h/e\) period, the enclosing-path hardware and the topology and coherence failure modes are measured and translate into buffer and failure specifications. The coherence scale is not filed.

## Related entries

- [flux-quantization](flux-quantization.md) — \(h/2e\) on a superconducting loop; different charge increment
- [josephson-effect](josephson-effect.md) — same \(h/2e\), read as a voltage–frequency lock
- [cyclotron-resonance](cyclotron-resonance.md) — electrons in a local \(B\), not around an enclosed flux
- [quantum-hall-effect](quantum-hall-effect.md) — another \(h, e\) combination; a two-dimensional sheet in perpendicular \(B\)

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [NIST, CODATA 2022 recommended values: magnetic flux quantum](https://physics.nist.gov/cgi-bin/cuu/Value?flxquhs2e) | full-text | h/2e = 2.067 833 848 × 10⁻¹⁵ Wb, exact; h/e is twice this. |
| S2 | [Tonomura et al., *Phys. Rev. Lett.* 56, 792 (1986)](https://doi.org/10.1103/PhysRevLett.56.792) | abstract | Toroidal magnet shielded by superconductor and copper; phase shift measured by electron holography; evidence of flux quantization. |
| S3 | [Webb, Washburn, Umbach and Laibowitz, *Phys. Rev. Lett.* 54, 2696 (1985)](https://doi.org/10.1103/PhysRevLett.54.2696) | abstract | h/e magnetoresistance oscillations in submicron Au rings, weaker h/2e component, persistence to large fields, temperature-dependent amplitude. |
| S4 | [Wikipedia, "Aharonov–Bohm effect"](https://en.wikipedia.org/wiki/Aharonov%E2%80%93Bohm_effect) | full-text | Tertiary: phase = qΦ/ħ; Chambers as first claimed confirmation; early results questioned on shielding; the 1986 experiment as unambiguous. |
| S5 | [Chambers, *Phys. Rev. Lett.* 5, 3 (1960)](https://doi.org/10.1103/PhysRevLett.5.3) | cited-only | "Shift of an Electron Interference Pattern by Enclosed Magnetic Flux"; title page only, text paywalled. |
