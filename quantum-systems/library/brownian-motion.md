---
id: brownian-motion
title: Brownian Motion (Incomplete Impact Average)
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
  - thermal-equilibrium-temperature
  - ideal-gas-pressure
  - johnson-nyquist-noise
  - speed-of-sound
updated: 2026-11-11
---

# Brownian Motion (Incomplete Impact Average)

### 4.1 Effect Name

Brownian motion (incomplete impact average)

### 4.2 Macroscopic Observation

A micrometre-scale particle suspended in a still fluid jitters continuously under a microscope. The path is irregular and the mean-square displacement grows linearly with time. Larger grains at the same temperature wander less. Everyday objects show no visible wander on the same observation window. Cooling the bath reduces the motion.

### 4.3 Established Quantitative Boundaries

- **Model (Langevin equation).** For a particle of mass \(m\) with drag coefficient \(\gamma\) in a bath at \(T\), \(\langle x^2(t)\rangle = \frac{2kT}{\gamma}\bigl[t-\frac{m}{\gamma}(1-e^{-\gamma t/m})\bigr]\) per axis. The relaxation time is \(\tau_p=m/\gamma\). For \(t\ll\tau_p\) the motion is ballistic, \(\langle x^2\rangle\approx kTt^2/m\); for \(t\gg\tau_p\), \(\langle x^2\rangle\approx 2Dt\) with the Einstein relation \(D=kT/\gamma\) [S1].
- **Model (Stokes drag).** For a small sphere of radius \(a\) in a fluid of viscosity \(\eta\), \(\gamma = 6\pi\eta a\), valid for laminar flow at Reynolds number well below 1 [S2].
- **Convention.** \(k = 1.380649\times 10^{-23}\,\mathrm{J\,K^{-1}}\), exact [S5].
- **Measured.** Viscosity of water at 20 °C: \(1.0020\,\mathrm{mPa\,s}\) [S3].
- **Computed here.** A sphere of 1 µm diameter in water at 20 °C: \(D = 4.3\times10^{-13}\,\mathrm{m^2\,s^{-1}}\); root-mean-square displacement along one axis in one second, \(\sqrt{2D\cdot1\,\mathrm{s}} = 0.93\,\mu\mathrm{m}\).
- **Computed here.** \(D\propto1/a\). A sphere of 1 mm diameter in the same water has \(D = 4.3\times10^{-16}\,\mathrm{m^2\,s^{-1}}\) and moves 29 nm rms in one second.
- **Computed here.** Momentum relaxation \(\tau_p = 2\rho a^2/9\eta = 55\,\mathrm{ns}\) for the 1 µm sphere, with an assumed particle density of \(1.0\,\mathrm{g\,cm^{-3}}\).
- **Measured.** The ballistic regime has been observed for a single particle in a liquid with an optical trap of 75 MHz bandwidth and sub-ångström precision; the velocity autocorrelation agrees with theory that includes the particle's inertia and the hydrodynamic memory of the fluid [S4].

**Data confidence:** High for the Langevin and Einstein relations and the ballistic observation. The numbers for the 1 µm sphere are arithmetic from one viscosity value and an assumed density. Perrin's determination, named in the first version, was not opened and is dropped. In a liquid the simple \(\tau_p\) is modified by hydrodynamic memory [S4].

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Langevin equation \(m\ddot x=-\gamma\dot x+F_r(t)\) with a white random force; averaging gives [S1]

  \[
  D = \frac{kT}{\gamma},\qquad \langle x^{2}\rangle = 2Dt \ \text{per axis}\quad (t\gg\tau_p)
  \]

- Equipartition on the particle: \(m\langle\dot x^{2}\rangle = kT\) per axis [S1].
- Stokes drag presupposes a continuum fluid: mean free path short compared with the particle, the Knudsen condition of [ideal-gas pressure](ideal-gas-pressure.md).

These relations describe the incomplete average of molecular impacts on a finite body. They fix no particle size.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two statistical scales, neither a single number:
  1. **Bath.** The fluid is a large thermal population with a stable [temperature](thermal-equilibrium-temperature.md) and, for Stokes drag, a mean free path short compared with the particle.
  2. **Tracer.** Visible jitter is the impact average left unfinished on the observation window. A larger tracer has smaller \(D\); stillness of everyday objects is the completed average. "Visible" depends on optical resolution, \(T\), \(\eta\) and the window.

- **Clock rate / latency.** Two clocks: the collision time of the bath, and the tracer's \(\tau_p=m/\gamma\) (55 ns for the 1 µm sphere in water). Observation faster than \(\tau_p\) resolves ballistic motion; slower observation sees the random walk.

- **Energy barriers or thresholds.** None. The resource is \(kT\) against the drag.

- **Dominant failure modes.**
  - **Crossover** — size: \(D=kT/6\pi\eta a\) falls as \(1/a\); rms displacement in 1 s goes from 0.93 µm at 1 µm diameter to 29 nm at 1 mm. The cut is the resolution of the observation.
  - **Crossover** — thermal: \(D\propto T/\eta(T)\) falls continuously with temperature.
  - **Crossover** — temporal: the linear law holds for \(t\gg\tau_p\); the full form \(t-\tau_p(1-e^{-t/\tau_p})\) joins it to the ballistic regime.
  - **Crossover** — bath: as the mean free path approaches the particle size Stokes drag fails (Knudsen number); no scale filed here.

- **Emergent constant or stable output.** A diffusivity \(D=kT/\gamma\) and a linearly growing mean-square displacement. For large bodies the output on the same window is stillness.

### 4.6 Internal Consistency Notes

This is the family definition run in reverse: the named effect is the incomplete average and the completed average is the still object.

Sourcing changed no numbers in kind: \(D\) "of order \(10^{-13}\)" is now \(4.3\times10^{-13}\,\mathrm{m^2\,s^{-1}}\) for a stated sphere and temperature, and \(\tau_p\) "tens of nanoseconds" is 55 ns for a stated density. The ballistic observation is now tied to one experiment in a liquid, which also shows that hydrodynamic memory must be included there.

[Johnson–Nyquist noise](johnson-nyquist-noise.md) is the electrical counterpart: the same Langevin equation with capacitance for mass and \(1/R\) for \(\gamma\) [S1]. Both scale with \(kT\).

QSA does not derive \(k\) or the Stokes coefficient. The missing universal radius is the same statistical gap as the missing \(N\) on the temperature entry.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the Einstein relation, the displacement law and its crossovers translate into an averaging-window statement; there is no particle-size threshold.

## Related entries

- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the bath average
- [Ideal-gas pressure](ideal-gas-pressure.md) — the same impacts, fully averaged on a wall
- [Johnson–Nyquist noise](johnson-nyquist-noise.md) — the electrical counterpart
- [Speed of sound](speed-of-sound.md) — continuum mode of the bath that Stokes drag assumes

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Merhav, "Statistical Physics: a Short Course for Electrical Engineering Students", arXiv:1307.5137, §8.2–8.3](https://arxiv.org/abs/1307.5137) | full-text | Langevin equation, mean-square displacement with relaxation time m/γ, ballistic and diffusive limits, Einstein relation, electrical analogue. Lecture notes, secondary. |
| S2 | [Wikipedia, "Stokes' law"](https://en.wikipedia.org/wiki/Stokes%27_law) | full-text | Tertiary: drag 6πηa on a small sphere; laminar flow, Reynolds number below 1. |
| S3 | [Kaye and Laby, *Tables of Physical and Chemical Constants*, §2.2.3 Viscosities (NPL, archived)](https://web.archive.org/web/2019/http://www.kayelaby.npl.co.uk/general_physics/2_2/2_2_3.html) | full-text | Viscosity of water, 1.0020 mPa s at 20 °C (Kestin, Sokolov and Wakeham 1978). |
| S4 | [Huang et al., "Direct observation of the full transition from ballistic to diffusive Brownian motion in a liquid", *Nat. Phys.* 7, 576 (2011)](https://www.nature.com/articles/nphys1953) | abstract | First measurement of ballistic Brownian motion in a liquid; 75 MHz bandwidth; inertia and hydrodynamic memory. |
| S5 | [NIST, CODATA 2022 recommended values: Boltzmann constant](https://physics.nist.gov/cgi-bin/cuu/Value?k) | full-text | k, exact. |
