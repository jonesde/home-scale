---
id: bose-einstein-condensate
title: Bose–Einstein Condensate (Density-Set Coherence Threshold)
status: formal
family: gapped-coherence
constraints:
  - thermal
  - spatial-buffer
confidence_data: high
confidence_mapping: medium
review_depth: light
related:
  - superfluid-helium-4
  - superconductivity
  - thermal-equilibrium-temperature
  - ideal-gas-pressure
  - flux-quantization
  - quantum-hall-effect
updated: 2026-11-11
---

# Bose–Einstein Condensate (Density-Set Coherence Threshold)

### 4.1 Effect Name

Bose–Einstein condensate (density-set coherence threshold)

### 4.2 Macroscopic Observation

A dilute gas of alkali atoms, confined in a magnetic or optical trap and cooled, develops a macroscopic occupation of the lowest trap state once a density- and temperature-dependent threshold is crossed. A sharp peak appears on the broader thermal distribution, in the trap and in the velocity distribution measured after release. Two condensates released into each other produce interference fringes. Warming the sample, or letting the density fall, removes the peak.

### 4.3 Established Quantitative Boundaries

- **Model (ideal Bose gas).** Threshold: \(n\lambda_T^3 = \zeta(3/2) \simeq 2.612\), with \(\lambda_T = h/\sqrt{2\pi m k_BT}\). In a harmonic trap the condition holds at the central density, and \(k_BT_c = \hbar\omega_{ho}(N/\zeta(3))^{1/3} = 0.94\,\hbar\omega_{ho}N^{1/3}\) [S1].
- **Measured.** The measured transition temperature is very close to the ideal-gas value, with a sudden onset of the condensate fraction at \(T/T_c \approx 1\); about 300 nK for 40,000 atoms in an early experiment [S1].
- **Measured.** Atom numbers range from a few thousand to several million [S1]. Sodium: up to \(5\times10^5\) condensed atoms at densities above \(10^{14}\) cm⁻³, below a critical temperature of about 2 µK, reached in seven seconds of evaporative cooling [S2].
- **Computed here.** Sodium at 2 µK has \(\lambda_T = 257\) nm, and \(n\lambda_T^3 = 2.612\) then requires \(n = 1.5\times10^{14}\) cm⁻³, consistent with the measured density [S2].
- **Model (ideal gas, harmonic trap).** Condensate fraction \(N_0/N = 1 - (T/T_c)^3\); in a uniform gas the exponent is 3/2 [S1].
- **Measured.** Readout. The trap is switched off and the expanded cloud is imaged by absorption; the condensate is the narrow peak. Interference between two condensates has been observed [S1][S5].
- **Measured.** Superfluid response. A laser beam stirred through a condensate heats it strongly only above a critical velocity [S3]. In a toroidal trap a flow of condensed atoms persists without decay for up to 10 s, limited by drift and trap lifetime [S4].
- **Convention.** The laboratory condensate is not a zero-power state: it exists only while the trap confines it, and its lifetime is finite.

**Data confidence:** High for the threshold condition, the atom-number range and the bimodal readout, from a standard review. The first-observation papers were not opened; their content is taken from the review. The critical-velocity and persistent-flow results are from abstracts.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Critical line: \(n\lambda_T^3 = \zeta(3/2)\); equivalently \(T_c = (2\pi\hbar^2/mk_B)(n/\zeta(3/2))^{2/3}\) for a uniform gas [S1].
- Harmonic trap: \(k_BT_c = 0.94\,\hbar\omega_{ho}N^{1/3}\), \(N_0/N = 1-(T/T_c)^3\) [S1].
- Interactions (Gross–Pitaevskii) broaden the condensate peak and shift \(T_c\) slightly; they set a healing length and a sound speed in the condensed cloud [S1].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A trapped cloud whose central phase-space density exceeds 2.612. The buffer is the combination of number, volume and temperature. There is no minimum atom number at which the effect switches on: condensates of a few thousand atoms are routine, and the transition is rounded, not absent, in a finite system.

- **Clock rate / latency.** Trap frequencies set the oscillation and expansion times; they are apparatus scales. There is no \(2e/h\) lock.

- **Energy barriers or thresholds.** The threshold is thermal and density-set: \(T > T_c(n)\), or \(n\) lowered at fixed \(T\). It is not an anisotropy barrier and not a pairing gap. Holding the condensate needs continuous trapping.

- **Dominant failure modes.**
  - **Threshold** — thermal: \(T > T_c(n)\); the condensate fraction, \(1-(T/T_c)^3\) below \(T_c\), reaches zero. Sharp in the large-\(N\) limit and rounded at finite \(N\).
  - **Threshold** — density: \(n\lambda_T^3 < 2.612\) at fixed \(T\); the same line crossed along the other axis.
  - **Crossover** — loss and heating: atom loss lowers \(n\) continuously over the sample lifetime. No opened source for a lifetime; 10 s of persistent flow was limited by the trap.
  - **Threshold** — trap removal: the cloud expands. The bimodal peak and the interference fringes are read during this expansion, so release ends the sample but is also how it is observed.
  - **Threshold** — velocity: dissipation above a critical velocity.

- **Emergent constant or stable output.** A macroscopic occupation of one state, read as a condensate fraction, a narrow velocity peak and interference contrast, while the cloud stays above the critical phase-space density.

### 4.6 Internal Consistency Notes

The thermal and density threshold is clean and maps onto a failure envelope.

Sourcing changed two things. A dilute condensate is a superfluid by direct test: it has a critical velocity and supports persistent flow, so the contrast with [superfluid-helium-4](superfluid-helium-4.md) is one of density and interaction strength, not of whether superflow exists. And the signatures are read after the trap is switched off, so "trap off" is the readout step as well as the end of the sample. The 2.612 threshold and the atom-number range were confirmed; the harmonic-trap exponent is 3, where the first version quoted only the uniform-gas 3/2.

The mapping does not close as tightly as its neighbours, for three reasons.

1. **Family tension.** The file sits in `gapped-coherence` by the taxonomy rule. An ideal-gas condensate has no pairing gap; the collapse is loss of macroscopic occupation.
2. **No size threshold.** The atom-number range is a working envelope. The 2.612 condition is taken from the ideal-gas model, not derived from node rules.
3. **Continuous resources.** The condensate is not held at zero power.

The leftover stack is draft `phase-space-condensate` in the analysis layer.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the \(T_c(n)\) threshold and the readout are solid, but the family assignment is loose, there is no minimum node count, and the threshold value is taken from the ideal-gas condition.

## Related entries

- [superfluid-helium-4](superfluid-helium-4.md) — dense analogue with a fixed \(T_\lambda\)
- [superconductivity](superconductivity.md) — charged case with a gap and a zero-power persistent current
- [thermal-equilibrium-temperature](thermal-equilibrium-temperature.md) — the temperature reading on which \(T_c\) sits
- [ideal-gas-pressure](ideal-gas-pressure.md) — the same cloud below threshold is a thermal gas
- [flux-quantization](flux-quantization.md) — integer winding in a charged condensate
- [quantum-hall-effect](quantum-hall-effect.md) — another state whose output value is taken, not derived

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Dalfovo, Giorgini, Pitaevskii and Stringari, *Rev. Mod. Phys.* 71, 463 (1999), arXiv:cond-mat/9806038](https://arxiv.org/abs/cond-mat/9806038) | full-text | Standard review: threshold 2.61, trap critical temperature and condensate fraction, 300 nK for 40,000 atoms, atom-number range, release-and-image readout, interference, interaction effects. |
| S2 | [Davis et al., *Phys. Rev. Lett.* 75, 3969 (1995)](https://doi.org/10.1103/PhysRevLett.75.3969) | abstract | Sodium: up to 5e5 atoms, density above 1e14 per cm³, critical temperature about 2 µK, seven seconds of cooling. |
| S3 | [Raman et al., *Phys. Rev. Lett.* 83, 2502 (1999)](https://doi.org/10.1103/PhysRevLett.83.2502) | abstract | Strong heating of a stirred condensate only above a critical velocity. |
| S4 | [Ryu et al., *Phys. Rev. Lett.* 99, 260401 (2007)](https://doi.org/10.1103/PhysRevLett.99.260401) | abstract | Persistent flow in a toroidal trap for up to 10 s. |
| S5 | [Andrews et al., *Science* 275, 637 (1997)](https://doi.org/10.1126/science.275.5300.637) | cited-only | Interference between two condensates; cited through the review. The first observation, Anderson et al., *Science* 269, 198 (1995), is likewise taken from the review. |
