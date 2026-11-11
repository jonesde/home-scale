---
id: quantum-hall-effect
title: Quantum Hall Effect (Landau-Gap Plateaus)
status: formal
family: gapped-coherence
constraints:
  - field-threshold
  - spatial-buffer
  - thermal
  - energy-barrier
  - clock-latency
confidence_data: high
confidence_mapping: medium
review_depth: light
related:
  - cyclotron-resonance
  - superconductivity
  - flux-quantization
  - josephson-effect
  - electron-heat-capacity
  - faraday-rotation
updated: 2026-11-11
---

# Quantum Hall Effect (Landau-Gap Plateaus)

### 4.1 Effect Name

Quantum Hall effect (Landau-gap plateaus)

### 4.2 Macroscopic Observation

A two-dimensional electron gas at low temperature in a strong magnetic field shows flat plateaus in the Hall resistance at a universal set of values, while the longitudinal resistance falls toward zero. Moving the field off a plateau, raising the temperature or raising the current restores a finite longitudinal resistance. The primary artifact is the integer sequence. Fractional plateaus are a related, harder case.

### 4.3 Established Quantitative Boundaries

- **Convention.** Von Klitzing constant \(R_K = h/e^2 = 25\,812.807\,45\ldots\,\Omega\), exact since the 2019 SI [S1]. Plateaus sit at \(R_H = R_K/i\) for integer \(i\).
- **Measured.** Discovery in a silicon MOSFET: the Hall resistance takes fixed values at well-defined carrier concentrations, insensitive to device geometry [S2]. The first plateaus matched \(h/ie^2\) to 10 parts in \(10^6\) [S3].
- **Measured.** Universality. The quantized resistance is independent of host material, device and plateau number to a few parts in \(10^{10}\), and of mobility between 13 and 135 T⁻¹ to 3 parts in \(10^{10}\) [S3].
- **Measured.** Hardware: a two-dimensional electron gas at low temperature and high field; the reference trace is a GaAs/AlGaAs heterostructure at 0.1 K [S3].
- **Measured.** Loss of quantization. A high current or a raised temperature gives a finite longitudinal resistivity, and the deviation of the Hall resistance from its quantized value is linear in that resistivity [S3].
- **Measured.** Tilted field. In silicon inversion layers with the field tilted up to 90° from the normal, the magneto-oscillations depend solely on the normal component of the field; the parallel component has a negligible effect on the orbital quantization. The spin splitting follows the total field [S5].
- **Measured.** Graphene at room temperature: Hall plateaus at \(2e^2/h\) with longitudinal resistance below 10 Ω, measured at 29 T and 45 T, quantized to about 0.2 %, with an activation energy of about 600 K. Plateaus begin to develop below 20 T at 300 K. Conventional semiconductors had not shown the effect above 30 K [S4].
- **Computed here.** Graphene Landau gap \(v_F\sqrt{2e\hbar B}\) with \(v_F = 10^6\) m s⁻¹ [S4]: 2820 K at 45 T, 9.4 times \(k_BT\) at 300 K (the source quotes 2800 K and a factor of 10).
- **Computed here.** Magnetic length \(\ell_B = \sqrt{\hbar/eB}\): 25.7 nm at 1 T and 8.1 nm at 10 T. A sheet density of \(3\times10^{15}\) m⁻² reaches filling factor 2 at 6.2 T.
- **Measured.** Fractional plateaus appear in higher-mobility samples at lower temperature [S6]; the letter was not opened.

**Data confidence:** High. \(R_K\) is exact by definition, and universality is established to parts in \(10^{10}\) in a metrology review read in full. The current and temperature at which a given sample leaves quantization are sample-dependent and not filed as numbers.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- On an integer plateau: \(R_H = h/ie^2\), \(R_{xx} \to 0\).
- Cyclotron frequency and magnetic length, with the normal component of the field: \(\omega_c = eB_\perp/m\), \(\ell_B = \sqrt{\hbar/eB_\perp}\), \(B_\perp = B\cos\theta\) [S5].
- Filling factor \(\nu = n_s h/(eB_\perp)\) locates the plateaus. It is bookkeeping, not a derivation of \(h/ie^2\).
- Thermally activated longitudinal resistance on a plateau, \(\rho_{xx} \propto e^{-\Delta E/k_BT}\), defines the activation energy quoted above [S4].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A two-dimensional electron system and a field component normal to it. A single atomic layer (graphene) is enough. Once the field opens a gap in the bulk of the sheet, the remaining current path is along the edges. The magnetic length is the in-plane scale. QSA records this layered hardware as measured; it does not derive the edge path.

- **Clock rate / latency.** The cyclotron frequency \(eB_\perp/m\), the same combination read as an absorption line on [cyclotron-resonance](cyclotron-resonance.md). The plateau is a DC resistance, not a radiated frequency.

- **Energy barriers or thresholds.** The Landau or mobility gap protects a plateau. The normal field component opens it.

- **Dominant failure modes.**
  - **Crossover** — thermal: longitudinal resistance is activated, \(e^{-\Delta E/k_BT}\); the Hall deviation is linear in it. Activation energy 600 K in graphene at 29–45 T.
  - **Crossover** — current: a high current gives finite longitudinal resistance and a proportional Hall deviation. No breakdown current filed.
  - **Crossover** — orientation: the orbital quantization follows \(B\cos\theta\). Tilting lowers the gap continuously; with the field in the plane the normal component and the gap are zero.
  - **Crossover** — filling: off a plateau the Hall resistance is not flat. Plateau width is set by disorder and temperature.
  - **Threshold** — buffer: no two-dimensional electron system, no plateau sequence.

- **Emergent constant or stable output.** A Hall resistance equal to \(R_K/i\) to parts in \(10^{10}\), with vanishing longitudinal resistance, inside the envelope above.

### 4.6 Internal Consistency Notes

The failure envelope is consistent with a gapped two-dimensional machine whose remaining transport path is an edge channel. Graphene's room-temperature plateaus sit on the same gap-against-\(k_BT\) clause.

Sourcing changed two things. The orientation clause is a crossover: the plateaus follow the normal field component, measured in 1968, so an in-plane field is the zero of a continuous \(\cos\theta\) dependence and not a separate switch. The thermal and current failures are crossovers with a measured linear relation between Hall deviation and longitudinal resistance. No numbers changed; \(R_K\) is quoted to the CODATA digits.

The mapping does not close, for three reasons.

1. **Underived output.** QSA takes \(R_H = h/ie^2\) from metrology. Because the output is a universal constant, the missing derivation is load-bearing.
2. **Architecture recorded, not derived.** Bulk gap plus edge path is the measured hardware.
3. **Fractional effect out of scope.**

The stack is draft `edge-channel` in the analysis layer. A 1D constriction ([quantum-point-contact](quantum-point-contact.md)) is contrast, not a member. Disorder widens a plateau without changing its value, as the mobility-independence above shows.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the plateaus, \(R_K\) and the collapses are metrological, but the quantized value is taken, the edge architecture is recorded and not specified from node rules, and the fractional case is unmapped.

## Related entries

- [cyclotron-resonance](cyclotron-resonance.md) — same \(eB/m\) clock, read as absorption
- [superconductivity](superconductivity.md) — another dissipationless channel protected by a gap
- [flux-quantization](flux-quantization.md) — another integer built from \(h\) and \(e\)
- [josephson-effect](josephson-effect.md) — the complementary metrological constant \(2e/h\)
- [electron-heat-capacity](electron-heat-capacity.md) — density of states of the same electrons
- [faraday-rotation](faraday-rotation.md) — electrons in a field; not quantized, not 2D

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [CODATA 2022, von Klitzing constant (NIST)](https://physics.nist.gov/cgi-bin/cuu/Value?rk) | full-text | Von Klitzing constant, exact. |
| S2 | [von Klitzing, Dorda and Pepper, *Phys. Rev. Lett.* 45, 494 (1980)](https://doi.org/10.1103/PhysRevLett.45.494) | abstract | Fixed Hall resistance values in a silicon MOSFET, insensitive to geometry. |
| S3 | [Jeckelmann and Jeanneret, *Séminaire Poincaré* 2, 39 (2004)](https://seminaire-poincare.pages.math.cnrs.fr/jeanneret.pdf) | full-text | Metrology review: 2DEG at low temperature and high field; 0.1 K GaAs trace; universality to parts in 1e10; mobility independence; effect of current and temperature; linear relation to longitudinal resistivity. |
| S4 | [Novoselov et al., "Room-temperature quantum Hall effect in graphene", arXiv:cond-mat/0702408 (2007)](https://arxiv.org/abs/cond-mat/0702408) | full-text | Graphene plateaus at 300 K, 29 T and 45 T; activation energy 600 K; gap 2800 K at 45 T; earlier limit of 30 K. |
| S5 | [Fang and Stiles, *Phys. Rev.* 174, 823 (1968)](https://doi.org/10.1103/PhysRev.174.823) | abstract | Tilted field on a silicon inversion layer: orbital quantization depends only on the normal component; spin splitting separable. |
| S6 | [Tsui, Stormer and Gossard, *Phys. Rev. Lett.* 48, 1559 (1982)](https://doi.org/10.1103/PhysRevLett.48.1559) | cited-only | Fractional plateaus. |
