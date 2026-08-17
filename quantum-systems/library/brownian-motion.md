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
related:
  - thermal-equilibrium-temperature
  - ideal-gas-pressure
  - johnson-nyquist-noise
  - speed-of-sound
updated: 2026-08-17
---

# Brownian Motion (Incomplete Impact Average)

### 4.1 Effect Name

Brownian motion (incomplete impact average)

### 4.2 Macroscopic Observation

A micrometre-scale particle suspended in a still fluid jitters continuously when watched under a microscope. The path is irregular; the mean-square displacement grows linearly with time. Larger grains at the same \(T\) jitter less. Everyday objects — a pebble in a glass of water, a hanging mirror at rest — present no visible wander on the same window: the molecular impacts are still there, but they have already averaged to a force too small, and a displacement too slow, to resolve. Cooling the bath reduces the wander. In vacuum there is no fluid bath and this particular jitter is absent.

### 4.3 Established Quantitative Boundaries

- Einstein–Smoluchowski displacement (after the momentum has been forgotten):

  \[
  \langle x^{2}\rangle = 2d\,Dt
  \]

  with \(d=1,2,3\) the number of observed axes.
- Einstein relation between diffusivity and drag:

  \[
  D = \frac{kT}{\gamma}
  \]

  For a sphere in a viscous fluid the Stokes drag is \(\gamma = 6\pi\eta a\). \(k = 1.380649\times 10^{-23}\,\mathrm{J\,K^{-1}}\) (defined); \(kT\approx 25.9\,\mathrm{meV}\) at \(300\,\mathrm{K}\).
- In water near room temperature a micrometre-scale sphere has \(D\) of order \(10^{-13}\,\mathrm{m^{2}\,s^{-1}}\), so the root-mean-square displacement in one second is of order a micrometre. That is the classical microscope-visible window (Perrin).
- Drag scales with radius; \(D\) therefore falls as \(1/a\). A millimetre-scale body in the same bath has \(D\) a thousand times smaller than a micrometre body; a centimetre-scale body is another factor of ten down. Combined with the larger mass, the object looks still on laboratory time and optical resolution. There is no single universal radius at which jitter “switches off.”
- Momentum relaxation time \(\tau_p = m/\gamma\) is tens of nanoseconds for a micrometre sphere in water. Observation windows longer than \(\tau_p\) see the overdamped random walk above. Windows shorter than \(\tau_p\) resolve ballistic segments (measured in optical-tweezer experiments). The overdamped envelope is a clock constraint, not a different effect.

**Data confidence:** High — the linear-in-\(t\) MSD, the Einstein relation, Perrin’s determination of \(k\) (historically \(N_A\)), and the ballistic-to-diffusive crossover are multiply reproduced. Stokes \(\gamma=6\pi\eta a\) is medium at boundaries and in non-Newtonian fluids; the \(D=kT/\gamma\) relation is not.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Langevin equation for the particle momentum, with a fluctuating force whose correlator is set by the same \(\gamma\) and \(T\) (fluctuation–dissipation). After averaging,

  \[
  D = \frac{kT}{\gamma},\qquad \langle x^{2}\rangle = 2d\,Dt\quad (t\gg\tau_p)
  \]

- Equipartition on the particle itself: \(\frac{1}{2}m\langle v^{2}\rangle = \frac{1}{2}kT\) per axis. A heavier body has a smaller thermal velocity; the overdamped drag then erases that velocity on the \(\tau_p\) clock.
- The fluid’s own continuum description (viscosity, [sound](speed-of-sound.md)) presupposes a molecular mean free path short compared with the particle and the container — the same Knudsen resource as [ideal-gas pressure](ideal-gas-pressure.md), now on the liquid or gas bath.

These relations describe the incomplete average of molecular impacts on a finite body. They do not derive \(k\) and they do not fix a universal particle size.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two nested statistical scales, neither a single cliff:
  1. **Bath.** The fluid must itself be a large thermal population with a stable [temperature](thermal-equilibrium-temperature.md) and, for Stokes drag, a continuum mean free path short compared with the particle.
  2. **Tracer.** Visible jitter is the *failure* of the impact average to finish on the observation window. Making the tracer larger, heavier, or more strongly damped *completes* the average and the macro wander disappears. Everyday stillness is the averaged output; Brownian motion is the under-averaged remainder. There is no universal radius: “visible” tracks optical resolution, \(T\), \(\eta\), and the chosen window.

- **Clock rate / latency.** Two clocks. Molecular impacts arrive on the collision time of the bath. The tracer forgets its velocity on \(\tau_p=m/\gamma\) (tens of nanoseconds for a micrometre sphere in water; much longer in air or at larger mass). Observation faster than \(\tau_p\) resolves ballistic segments; observation much slower sees only the random walk. A still-longer window does not cancel the walk — \(\langle x^{2}\rangle\) keeps growing — but the *rate* of wander falls with \(\sqrt{D}\) and becomes unresolvable for large bodies.

- **Energy barriers or thresholds.** None holding a latched state. The operating resource is \(kT\) against the drag. \(T\to 0\) sends \(D\to 0\). Removing the bath (vacuum) removes the impact rain.

- **Dominant failure modes.**
  - Spatial / mass: particle so large (or so heavy, or so overdamped) that the kicks average below the resolution of the window → the object looks still. This is completion of the average, i.e. collapse of the *visible* effect.
  - Thermal: \(T\to 0\) → \(D\to 0\).
  - Temporal: window \(\ll\tau_p\) → the overdamped \(\langle x^{2}\rangle=2dDt\) envelope does not apply (ballistic segment, not a different machine).
  - Bath: Knudsen or vacuum conditions → Stokes \(\gamma\) and the Einstein relation in the form above fail.

- **Emergent constant or stable output.** A diffusivity \(D=kT/\gamma\) and a linearly growing mean-square displacement, as the still-visible remainder of an incomplete impact average. For large bodies the emergent output is stillness on the same window.

### 4.6 Internal Consistency Notes

This is the family definition run in reverse: the named macroscopic effect is the incomplete average; the completed average is the still object. That is internally consistent and must be kept explicit, or the collapse statement (“particle so large the kicks average to zero”) looks like a missing machine rather than a finished one.

[Johnson–Nyquist noise](johnson-nyquist-noise.md) is the electrical fluctuation–dissipation twin: \(4kTR\Delta f\) is to a resistor what \(D=kT/\gamma\) is to a drag. The two entries should share \(kT\) and should fail together as \(T\to 0\). They do not share a geometric buffer.

QSA does not derive \(k\) or Stokes’ \(6\pi\) from node rules. The mapping takes \(D=kT/\gamma\) and the measured \(\tau_p\) crossover as the specifications. The missing universal radius is the same honest statistical gap as the missing \(N\) on the temperature entry; faking a micrometre “cliff” because that is where a microscope happens to work would be a convention, not a hardware threshold.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the Einstein relation, the MSD law, and the large-body / low-\(T\) / short-window failures are solid and translate directly into an averaging-window statement; there is no single particle-size cliff, and the mapping is written so as not to invent one.

## Related entries

- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the bath average whose incomplete mechanical readout is the jitter
- [Ideal-gas pressure](ideal-gas-pressure.md) — the same impact rain, fully averaged on a wall
- [Johnson–Nyquist noise](johnson-nyquist-noise.md) — fluctuation–dissipation twin in a resistor
- [Speed of sound](speed-of-sound.md) — continuum mode of the bath that Stokes drag already assumes
