---
id: josephson-effect
title: Josephson Effect (Weak-Link Phase Current)
status: formal
family: gapped-coherence
constraints:
  - spatial-buffer
  - clock-latency
  - energy-barrier
  - thermal
  - field-threshold
confidence_data: high
confidence_mapping: high
review_depth: light
related:
  - superconductivity
  - meissner
  - flux-quantization
  - type-ii-critical-field
  - superfluid-helium-4
  - quantum-hall-effect
updated: 2026-11-11
---

# Josephson Effect (Weak-Link Phase Current)

### 4.1 Effect Name

Josephson effect (weak-link phase current)

### 4.2 Macroscopic Observation

Two superconducting electrodes separated by a thin insulating barrier, a short normal bridge or a constriction pass a current at zero DC voltage up to a junction-specific critical current \(I_c\). Above \(I_c\) a DC voltage appears and the junction oscillates at a frequency fixed by that voltage; an applied microwave tone produces constant-voltage steps. Thickening the barrier reduces \(I_c\) toward zero. Warming either electrode through its critical temperature removes the effect.

### 4.3 Established Quantitative Boundaries

- **Convention.** Josephson constant \(K_J = 2e/h = 483\,597.848\,4\ldots\) GHz V⁻¹, exact since the 2019 SI [S1]. Its inverse is the flux quantum \(\Phi_0 = h/2e = 2.067\,833\,848\ldots\times10^{-15}\) Wb [S2].
- **Computed here.** A bias of 1 µV oscillates at 483.6 MHz and 1 mV at 483.6 GHz. A 10 GHz drive gives steps spaced by 20.7 µV.
- **Measured.** Under microwave irradiation at frequency \(f\) the current–voltage curve has constant-voltage steps at \(V_n = n\,hf/2e\) [S5]. The original letter was not opened; the same relation \(V = \hbar\dot\varphi/2e\) is stated in [S6].
- **Measured.** Barrier. In Al/AlO\(_x\)/Al junctions the oxide is about 1 to 2 nm thick with a Gaussian spread along the junction, and less than 10 % of the barrier area dominates the tunnelling [S3].
- **Model (Werthamer / Riedel, with simulation).** Frequency. The supercurrent response has a singularity at the gap voltage (the Riedel peak). Zero-crossing steps are used below about 100 GHz, and the calculated response lets them exist up to terahertz frequencies if the peak is not too rounded [S4].
- **Computed here.** Gap frequency \(2\Delta/h\) of the electrodes from the gaps in [S6]: Al 85 GHz, Pb 660 GHz, Nb 735 GHz; the corresponding gap voltages \(2\Delta/e\) are 0.35, 2.73 and 3.04 mV.
- **Measured.** Field. A flux of order \(\Phi_0\) through the junction area modulates \(I_c\) in a diffraction pattern [S7]. The letter was not opened; no opened source for this bullet.
- **Convention.** \(I_c\) is a property of the junction (area, barrier, electrode gap), not a constant.

**Data confidence:** High for the voltage–frequency ratio, which is exact by definition of the SI units. The step relation and the field modulation are standard results cited to letters that were not opened. The barrier thickness is from one abstract.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Current–phase and voltage–phase relations:

  \[
  I = I_c\sin\phi, \qquad \frac{d\phi}{dt} = \frac{2e}{\hbar}V
  \]

  \(\phi\) is the phase difference across the link [S6].
- Zero-voltage branch for \(|I| \le I_c\); a resistive branch with \(V \ne 0\) above.
- Uniform rectangular junction in a field:

  \[
  I_c(\Phi) = I_c(0)\left|\frac{\sin(\pi\Phi/\Phi_0)}{\pi\Phi/\Phi_0}\right|
  \]

  with zeros at integer multiples of \(\Phi_0\) [S7].
- The resistively shunted junction model fits current–voltage curves with a capacitance and a shunt resistance. It is bookkeeping, not a mechanism claim.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two superconducting electrodes ([superconductivity](superconductivity.md)) coupled through a weak link. For an oxide tunnel barrier the link is 1–2 nm thick, and the current is carried by the thinnest tenth of its area. The load-bearing variable is the phase difference \(\phi\) across the link.

- **Clock rate / latency.** The voltage–frequency lock: 483.6 MHz per microvolt. Shapiro steps are the same clock read against an external drive. The electrode gap frequency (85 GHz for Al, 735 GHz for Nb) is where the response peaks; the lock ratio itself does not change there.

- **Energy barriers or thresholds.** \(I_c\) protects the zero-voltage branch. The electrode gap vanishes at \(T_c\) and takes \(I_c\) with it. A flux of order \(\Phi_0\) through the junction suppresses \(I_c\) without destroying the electrodes.

- **Dominant failure modes.**
  - **Crossover** — barrier thickness: \(I_c\) falls steeply and continuously as the barrier thickens; the dominance of the thinnest 10 % of the area is the measured sign of that steepness. No decay length filed.
  - **Threshold** — current: \(I > I_c\) gives a DC voltage.
  - **Threshold** — thermal: \(T > T_c\) in either electrode.
  - **Crossover** — field: \(I_c\) follows \(|\sin x/x|\) in the junction flux, with zeros at multiples of \(\Phi_0\). A field above the electrode \(H_c\) or \(H_{c2}\) is a separate threshold owned by the parent entries.
  - **Crossover** — frequency: the supercurrent amplitude peaks at the gap frequency and falls above it; steps are calculated to persist into the terahertz range. The ratio \(2e/h\) is unchanged.

- **Emergent constant or stable output.** A zero-voltage current for \(|I| \le I_c\), and the lock \(V = (h/2e)\,\nu\) once a voltage is present.

### 4.6 Internal Consistency Notes

The collapses sit where a weak link with a current threshold and a voltage-locked clock should fail. The same \(\Phi_0\) appears here and in [flux-quantization](flux-quantization.md).

Sourcing changed two things. The "few nanometres" barrier is 1–2 nm in the junctions measured, and its failure is a crossover in thickness. A frequency clause was added: the gap frequency marks a peak and a roll-off in amplitude, not an end of the lock. No numbers were otherwise changed; \(K_J\) and \(\Phi_0\) are now quoted to the CODATA digits.

A remaining gap: the charge increment \(2e\) in \(h/2e\) is taken from the lock and from the flux quantum. QSA does not derive why it is \(2e\) and not \(e\).

A chargeless weak-link analogue exists in helium-4 apertures; see [superfluid-helium-4](superfluid-helium-4.md).

### 4.7 Overall Confidence in the QSA Mapping

**High** — the lock is exact, the barrier window and the \(I_c\), \(T_c\) and \(\Phi_0\) limits are measured and translate directly into buffer, clock and threshold specifications; the open item is the origin of the \(2e\) increment.

## Related entries

- [superconductivity](superconductivity.md) — parent condensate
- [meissner](meissner.md) — same condensate, field expulsion
- [flux-quantization](flux-quantization.md) — same \(\Phi_0\) in a closed loop
- [type-ii-critical-field](type-ii-critical-field.md) — electrode-scale field collapse
- [superfluid-helium-4](superfluid-helium-4.md) — chargeless aperture analogue
- [quantum-hall-effect](quantum-hall-effect.md) — the complementary metrological constant \(R_K = h/e^2\)

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [CODATA 2022, Josephson constant (NIST)](https://physics.nist.gov/cgi-bin/cuu/Value?kjos) | full-text | Josephson constant, exact. |
| S2 | [CODATA 2022, magnetic flux quantum (NIST)](https://physics.nist.gov/cgi-bin/cuu/Value?flxquhs2e) | full-text | Flux quantum, exact. |
| S3 | [Zeng et al., arXiv:1407.0173 (2014)](https://arxiv.org/abs/1407.0173) | abstract | AlOx barrier about 1 to 2 nm, Gaussian thickness distribution, under 10 % of the area dominates tunnelling. |
| S4 | [Danchi, Golightly and Sutton, *J. Appl. Phys.* 65, no. 7 (1989)](https://www.osti.gov/biblio/6203294) | abstract | Zero-crossing steps below about 100 GHz; Riedel singularity lets them exist up to terahertz frequencies (calculation and simulation). |
| S5 | [Shapiro, *Phys. Rev. Lett.* 11, 80 (1963)](https://doi.org/10.1103/PhysRevLett.11.80) | cited-only | Constant-voltage steps under microwave irradiation. |
| S6 | [Arutyunov, Golubev and Zaikin, "Superconductivity in one dimension", arXiv:0805.2118 (2008)](https://arxiv.org/abs/0805.2118) | full-text | Josephson voltage–phase relation as stated in a review; gaps of Al, Pb, Nb (Table I). |
| S7 | [Rowell, *Phys. Rev. Lett.* 11, 200 (1963)](https://doi.org/10.1103/PhysRevLett.11.200) | cited-only | Magnetic-field diffraction pattern of the critical current. |
