---
id: ideal-gas-pressure
title: Ideal-Gas Pressure (Averaged Momentum Transfer)
status: formal
family: ensemble-averages
constraints:
  - thermal
  - spatial-buffer
  - clock-latency
confidence_data: high
confidence_mapping: medium
review_depth: light
related:
  - thermal-equilibrium-temperature
  - brownian-motion
  - speed-of-sound
  - ionization-threshold
  - thermal-conductivity-phonon
updated: 2026-11-11
---

# Ideal-Gas Pressure (Averaged Momentum Transfer)

### 4.1 Effect Name

Ideal-gas pressure (averaged momentum transfer)

### 4.2 Macroscopic Observation

A dilute gas in a closed vessel exerts a steady, uniform force per unit area on the walls. A gauge reports one number \(P\) that rises in proportion to density at fixed temperature and in proportion to temperature at fixed density. In a vessel much larger than the molecular mean free path the gas also supports continuum hydrodynamics: a local pressure field, sound and viscous flow. As the vessel shrinks toward the mean free path, or the gas is pumped down until that path is comparable with the apparatus, the continuum description degrades through slip and transitional flow to free-molecular flow, where molecules cross the vessel without colliding with each other.

### 4.3 Established Quantitative Boundaries

- **Measured.** Ideal-gas equation of state in the dilute limit, \(P = nkT\) (taken as an experimental fact in [S3]).
- **Convention.** \(k = 1.380649\times 10^{-23}\,\mathrm{J\,K^{-1}}\), exact [S1]. Loschmidt constant at 273.15 K and 101.325 kPa: \(n_0 = 2.686780\times 10^{25}\,\mathrm{m^{-3}}\), exact since it is \(P/kT\) with exact inputs [S2].
- **Computed here.** At 300 K, \(kT = 25.85\,\mathrm{meV}\). At 293.15 K and 101.325 kPa, \(n = 2.50\times 10^{25}\,\mathrm{m^{-3}}\).
- **Model (hard-sphere kinetic theory).** Mean free path \(\lambda = 1/(\sqrt{2}\,n\sigma) = kT/(\sqrt{2}\,P\sigma)\), with \(\sigma=\pi d^2\) the collision cross-section [S3]. It scales as \(1/n\).
- **Model (kinetic theory).** Air at ambient pressure: \(\lambda\) = 64–68 nm [S4].
- **Computed here.** Scaling 66 nm by \(1/P\): \(\lambda = 67\,\mu\mathrm{m}\) at 100 Pa and 6.7 mm at 1 Pa.
- **Computed here.** Collision time \(\lambda/\bar v\) with \(\bar v = 471\,\mathrm{m\,s^{-1}}\) (\(\mathrm{N_2}\) at 293.15 K, atomic weight 14.007 [S6]): \(1.4\times10^{-10}\,\mathrm{s}\) at ambient pressure.
- **Convention.** Knudsen number \(\mathrm{Kn}=\lambda/L\). The usual bands: continuum flow for \(\mathrm{Kn}<0.01\); slip flow for 0.01–0.1; transitional flow for 0.1–10; free-molecular flow for \(\mathrm{Kn}>10\). The classification is empirical and problem-dependent [S5].
- **Computed here.** Count in a sub-volume: a cubic micrometre of gas at \(n_0\) holds \(2.7\times10^{7}\) molecules; a cube of side \(\lambda\) at ambient conditions holds about \(7\times10^{3}\) (\(6.6\times10^{3}\) to \(7.9\times10^{3}\) over 64–68 nm). The Poisson scatter of a count \(N\) is \(N^{-1/2}\): 0.02 % and 1.2 % respectively. Count scatter and the Knudsen crossover are separate limits.

**Data confidence:** High for \(P=nkT\), the exact constants and the \(1/n\) scaling of \(\lambda\). Medium for the air mean free path and the Knudsen bands, which rest on tertiary pages; the bands are a convention in any case.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Equation of state in the dilute, non-interacting limit: \(P = nkT\). Virial corrections appear as density rises; that is a different departure (correlations).
- Momentum flux on a wall from a Maxwellian population gives \(P=nkT\) after averaging, with \(\langle v_x^2\rangle = kT/m\) [S3]. A single impact is not \(P\).
- Mean free path as above; collision time \(\tau = \lambda/\bar v\), \(\bar v=\sqrt{8kT/\pi m}\).
- Navier–Stokes hydrodynamics, including a local \(P(\mathbf{r},t)\) and the [speed of sound](speed-of-sound.md), presupposes \(\mathrm{Kn}\ll 1\).

These relations describe the averaged wall load and the continuum field built from it. They do not derive \(k\) and fix no vessel size.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two statistical buffers, neither a universal length:
  1. **Count.** A stable \(P\) needs enough independent impacts in the gauge window that \(N^{-1/2}\) scatter is below the required resolution.
  2. **Path against apparatus.** A continuum \(P(\mathbf{r})\) needs \(L\gg\lambda\). \(\lambda\) tracks density: tens of nanometres in ambient air, millimetres at 1 Pa.

- **Clock rate / latency.** Wall impacts and collisions arrive on the collision clock, \(1.4\times10^{-10}\,\mathrm{s}\) in ambient air and longer as \(1/P\). A gauge that resolves single hits sees a sequence of impacts, not \(P\).

- **Energy barriers or thresholds.** None. The resources are density, an equilibration window and an apparatus larger than \(\lambda\). Ionization removes the neutral population ([ionization threshold](ionization-threshold.md)).

- **Dominant failure modes.**
  - **Crossover** — rarefaction: the continuum field degrades with \(\mathrm{Kn}=\lambda/L\) through slip (0.01–0.1) and transitional flow (0.1–10) to free-molecular flow (above 10). The band edges are conventions.
  - **Crossover** — population: reading scatter \(\sim N^{-1/2}\) in the sampled count.
  - **Crossover** — temporal: observation shorter than the collision time (\(1.4\times10^{-10}\,\mathrm{s}\) in ambient air) gives an incomplete average.
  - **Crossover** — density: virial corrections grow with \(n\); no scale filed here.

- **Emergent constant or stable output.** A steady wall pressure \(P=nkT\) and, at small \(\mathrm{Kn}\), a continuum hydrodynamic field built from that average.

### 4.6 Internal Consistency Notes

The Knudsen condition is a spatial-buffer statement in which the buffer is relative (\(\lambda/L\)) and moves with density. The \(N^{-1/2}\) count buffer is the gap already recorded on [thermal equilibrium temperature](thermal-equilibrium-temperature.md).

Sourcing changed the failure label. The first version put the collapse at \(\mathrm{Kn}\gtrsim1\) and called free-molecular flow the regime above 1. The standard bands put transitional flow from 0.1 to 10 and free-molecular flow above 10, so the loss of the continuum field is a crossover spanning three decades of \(\mathrm{Kn}\). The rough-vacuum length "centimetres to metres" was replaced by computed values (6.7 mm at 1 Pa). Other numbers are unchanged within rounding.

\(P=nkT\) and continuum hydrodynamics are different outputs. A free-molecular gas still delivers a time-averaged wall force; it does not support sound as a local mode. This entry owns the wall load and the Knudsen crossover; [speed of sound](speed-of-sound.md) owns the mode.

QSA does not derive \(k\) or the molecular cross-section.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — \(P=nkT\) and the Knudsen crossover translate into a statistical buffer and an averaging window; there is no universal \(N\) or \(L\).

## Related entries

- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the \(T\) in \(P=nkT\)
- [Brownian motion](brownian-motion.md) — the same impacts, averaged incompletely on a suspended particle
- [Speed of sound](speed-of-sound.md) — continuum mode that needs \(\mathrm{Kn}\ll1\)
- [Ionization threshold](ionization-threshold.md) — removes the neutral population
- [Phonon thermal conductivity](thermal-conductivity-phonon.md) — another transport coefficient set by a mean free path

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [NIST, CODATA 2022 recommended values: Boltzmann constant](https://physics.nist.gov/cgi-bin/cuu/Value?k) | full-text | k, exact. |
| S2 | [NIST, CODATA 2022 recommended values: Loschmidt constant (273.15 K, 101.325 kPa)](https://physics.nist.gov/cgi-bin/cuu/Value?n0std) | full-text | n0 = 2.686780111e25 per cubic metre, exact. |
| S3 | [Merhav, "Statistical Physics: a Short Course for Electrical Engineering Students", arXiv:1307.5137, ch. 2](https://arxiv.org/abs/1307.5137) | full-text | Ideal-gas equation of state, Maxwell velocity moments, hard-sphere mean free path formula. Lecture notes, secondary. |
| S4 | [Wikipedia, "Mean free path"](https://en.wikipedia.org/wiki/Mean_free_path) | full-text | Tertiary: 64–68 nm for air at ambient pressure, citing Jennings, *J. Aerosol Sci.* 19, 159 (1988), which was not opened. |
| S5 | [Wikipedia, "Knudsen number"](https://en.wikipedia.org/wiki/Knudsen_number) | full-text | Tertiary: flow-regime bands 0.01, 0.1, 10 and the note that the classification is empirical. |
| S6 | [NIST, Atomic Weights and Isotopic Compositions: nitrogen](https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=N) | full-text | Standard atomic weight of nitrogen, used for the mean molecular speed. |
