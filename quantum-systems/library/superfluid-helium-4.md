---
id: superfluid-helium-4
title: Superfluid Helium-4 (Chargeless Superflow)
status: formal
family: gapped-coherence
constraints:
  - thermal
  - spatial-buffer
  - energy-barrier
confidence_data: high
confidence_mapping: high
review_depth: light
related:
  - bose-einstein-condensate
  - superconductivity
  - flux-quantization
  - josephson-effect
  - type-ii-critical-field
  - thermal-equilibrium-temperature
updated: 2026-11-11
---

# Superfluid Helium-4 (Chargeless Superflow)

### 4.1 Effect Name

Superfluid helium-4 (chargeless superflow)

### 4.2 Macroscopic Observation

Liquid \(^4\mathrm{He}\) below the \(\lambda\)-point flows through packed powder and fine capillaries without measurable viscosity, creeps over the walls of an open vessel as a film, and produces a fountain when one side of a superleak is heated. Currents persist in a closed path. Above the \(\lambda\)-point the same liquid is an ordinary viscous fluid. These qualitative observations are standard; the numbers below are the sourced part.

### 4.3 Established Quantitative Boundaries

- **Measured.** \(\lambda\)-point at saturated vapour pressure: \(T_\lambda = 2.1768\) K; liquid density there 0.1461 g cm⁻³ [S1].
- **Measured.** Superfluid fraction. Near the transition the recommended fit is \(\rho_s/\rho = k_0(1 + k_1\epsilon)\,\epsilon^{\zeta}\) with \(\epsilon = 1 - T/T_\lambda\), \(k_0 = 2.403\) and \(\zeta = 0.6717\) [S1]. The fraction goes continuously to zero at \(T_\lambda\).
- **Computed here.** Leading term of that fit at \(\epsilon = 0.01\) (22 mK below \(T_\lambda\)): \(\rho_s/\rho \approx 0.11\).
- **Measured.** Landau critical velocity for roton creation, from ion drift: about 60 m s⁻¹ at saturated vapour pressure, falling to 46 m s⁻¹ at 24 bar. The speed of sound is 220 m s⁻¹ [S2].
- **Measured.** Critical velocities in apertures and channels lie below the Landau value. Two regimes appear: a faster one in small apertures, where single \(2\pi\) phase slips are resolved, and a slower one in larger channels. Values are not reproducible from one experiment to the next, and in small apertures the vortices are nucleated by thermal activation [S2].
- **Computed here.** Circulation quantum \(\kappa = h/m_4 = 9.97\times10^{-8}\) m² s⁻¹, with \(m_4\) the atomic mass (alpha-particle mass plus two electron masses, \(6.6465\times10^{-27}\) kg) [S3]. Single quanta of circulation are observed building up in aperture flow [S2].
- **Computed here.** The ideal-gas condensation temperature \(T_c = (2\pi\hbar^2/mk_B)(n/2.612)^{2/3}\) [S4] at the liquid's number density (\(2.20\times10^{28}\) m⁻³) is 3.15 K, 45 % above the measured \(T_\lambda\).
- **Convention.** Holding a persistent current costs zero continuous power below \(T_\lambda\) and below the critical velocity.

**Data confidence:** High for \(T_\lambda\), the density and \(\rho_s(T)\), read from the standard reference tables (a scanned document read by character recognition). Critical velocities are Medium by the source's own account. The pressure dependence of \(T_\lambda\) and the fountain relation have no opened source and are not quoted.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Two-fluid decomposition: \(\rho = \rho_n(T) + \rho_s(T)\), \(\mathbf{j} = \rho_n\mathbf{v}_n + \rho_s\mathbf{v}_s\), with \(\rho_s(T_\lambda) = 0\). This is bookkeeping of the measured density, not a statement that two liquids are present.
- Quantized circulation on a closed path in the superfluid:

  \[
  \oint \mathbf{v}_s\cdot d\mathbf{l} = n\,\frac{h}{m_4}, \qquad n \in \mathbb{Z}
  \]

- Landau criterion: \(v_L = \min(\epsilon/p)\) over the excitation spectrum, close to the roton minimum [S2].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A connected volume of liquid \(^4\mathrm{He}\) below \(T_\lambda\). Showing zero viscosity needs a filter (superleak or film) that passes the superfluid fraction only; that is apparatus. Quantized circulation needs a closed path, as in [flux-quantization](flux-quantization.md). There is no charge, no London \(\lambda\) and no Meissner expulsion.

- **Clock rate / latency.** No voltage–frequency lock (no charge). Micro-apertures show the analogous phase-slip dynamics. Second sound is a hydrodynamic clock of the formed superfluid.

- **Energy barriers or thresholds.** \(T_\lambda\) is the thermal threshold. The velocity limit has two parts: a sharp Landau bound of 60 m s⁻¹ for roton emission, and a lower, geometry-dependent limit set by vortex nucleation over an energy barrier.

- **Dominant failure modes.**
  - **Threshold** — thermal: \(T > T_\lambda = 2.1768\) K; a phase transition, approached continuously as \(\rho_s/\rho \propto (1 - T/T_\lambda)^{0.6717}\).
  - **Threshold** — velocity, upper bound: 60 m s⁻¹ (46 m s⁻¹ at 24 bar), roton creation.
  - **Crossover** — velocity, in channels and apertures: thermally activated vortex nucleation; statistical, not reproducible between experiments, below the Landau value.
  - **Threshold** — topology: an open path holds no circulating integer.
  - **Threshold** — solidification: crossing the melting curve removes the liquid. No opened source for the pressure.

- **Emergent constant or stable output.** Chargeless superflow and a circulation quantum \(h/m_4\), while \(T < T_\lambda\) and the flow stays below the critical velocity.

### 4.6 Internal Consistency Notes

This is the chargeless member of the family. The thermal threshold, the circulation integer and the phase slip are the same kinds of specification as \(T_c\), \(\Phi_0\) and the phase slip of a superconducting loop, without electromagnetic screening.

Sourcing changed two things. \(T_\lambda\) is 2.1768 K (the first version rounded to 2.17 K). The critical velocity is split: the Landau bound is sharp and measured with ions, and the lower limits seen in channels are a statistical nucleation process, a crossover.

\(T_\lambda\) is not obtained from node rules. The ideal-gas formula at the liquid density gives 3.15 K, so the dilute-gas condition does not locate it either.

The family name "gapped" is loose here: the collapse is loss of \(\rho_s\) at \(T_\lambda\), not closure of a pairing gap. Relation to [bose-einstein-condensate](bose-einstein-condensate.md) is analogy, not identity of hardware.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(T_\lambda\), \(\rho_s(T)\), the Landau bound and \(h/m_4\) are measured boundaries that translate into thermal, velocity and topology specifications; the open items are the origin of \(T_\lambda\) and the channel-dependent critical velocity.

## Related entries

- [bose-einstein-condensate](bose-einstein-condensate.md) — dilute analogue with a density-set threshold
- [superconductivity](superconductivity.md) — charged analogue
- [flux-quantization](flux-quantization.md) — charged counterpart of the circulation integer
- [josephson-effect](josephson-effect.md) — weak-link analogue
- [type-ii-critical-field](type-ii-critical-field.md) — vortices carrying \(\Phi_0\) in place of \(h/m_4\)
- [thermal-equilibrium-temperature](thermal-equilibrium-temperature.md) — the temperature reading on which \(T_\lambda\) sits

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Donnelly and Barenghi, *J. Phys. Chem. Ref. Data* 27, 1217 (1998)](https://srd.nist.gov/JPCRD/jpcrd551.pdf) | full-text | Reference tables for liquid helium at saturated vapour pressure: lambda point 2.1768 K, density there, superfluid-fraction fit with exponent 0.6717. Scanned; read by character recognition. |
| S2 | [Varoquaux, "Critical velocities in superfluids and the nucleation of vortices", arXiv:cond-mat/0611405 (2006)](https://arxiv.org/abs/cond-mat/0611405) | full-text | Review of critical velocities: Landau value 60 m/s, 46 m/s at 24 bar, sound 220 m/s; two regimes; poor reproducibility; thermally activated nucleation; phase slips and circulation quanta in apertures. |
| S3 | [CODATA 2022, alpha particle mass (NIST)](https://physics.nist.gov/cgi-bin/cuu/Value?mal) | full-text | Alpha-particle mass; with the electron mass and the exact Planck constant gives the circulation quantum. |
| S4 | [Dalfovo, Giorgini, Pitaevskii and Stringari, *Rev. Mod. Phys.* 71, 463 (1999), arXiv:cond-mat/9806038](https://arxiv.org/abs/cond-mat/9806038) | full-text | Ideal-gas condensation temperature of a uniform Bose gas. |
