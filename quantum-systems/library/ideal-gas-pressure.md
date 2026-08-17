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
related:
  - thermal-equilibrium-temperature
  - brownian-motion
  - speed-of-sound
  - ionization-threshold
  - thermal-conductivity-phonon
updated: 2026-08-17
---

# Ideal-Gas Pressure (Averaged Momentum Transfer)

### 4.1 Effect Name

Ideal-gas pressure (averaged momentum transfer)

### 4.2 Macroscopic Observation

A dilute gas in a closed vessel exerts a steady, uniform force per unit area on the walls. A bourdon gauge, a piston, or a capacitance manometer reports a single number \(P\) that is stable on laboratory time and that rises in proportion to density at fixed thermometer reading, and in proportion to that reading at fixed density. In a vessel much larger than the molecular mean free path the gas also supports continuum hydrodynamics: a well-defined local pressure field, sound, and viscous flow. When the vessel or the obstacle shrinks toward the mean free path, or when the gas is pumped down so that path becomes the largest length in the apparatus, the continuum reading fails: transport becomes ballistic, the wall load is a rain of independent impacts, and \(P = nkT\) is no longer a stable local field.

### 4.3 Established Quantitative Boundaries

- Ideal-gas envelope, dilute limit:

  \[
  P = nkT \qquad\text{or}\qquad PV = NkT
  \]

  with \(k = 1.380649\times 10^{-23}\,\mathrm{J\,K^{-1}}\) (defined). At \(300\,\mathrm{K}\), \(kT \approx 25.9\,\mathrm{meV}\).

- Standard atmosphere \(101325\,\mathrm{Pa}\) at \(273.15\,\mathrm{K}\) corresponds to a number density \(n = P/kT \approx 2.69\times 10^{25}\,\mathrm{m^{-3}}\).
- Hard-sphere mean free path used in kinetic theory:

  \[
  \lambda = \frac{1}{\sqrt{2}\,\pi d^{2} n}
  \]

  For air-like molecular diameters at standard density this gives \(\lambda\) of order \(65\,\mathrm{nm}\). The numerical prefactor depends on the chosen collision model; the \(1/n\) scaling does not.
- Continuum hydrodynamics fails when the Knudsen number

  \[
  \mathrm{Kn} = \frac{\lambda}{L}
  \]

  is no longer small. The conventional engineering bands are slip around \(\mathrm{Kn}\sim 10^{-2}\)–\(10^{-1}\) and free-molecular flow for \(\mathrm{Kn}\gtrsim 1\). The load-bearing QSA cliff is the latter: \(L\) has dropped through \(\lambda\), or \(n\) has been lowered until \(\lambda\) exceeds \(L\).
- Relative fluctuation of the count in a sub-volume scales as \(N^{-1/2}\). A cubic micrometre of standard-density air still holds \(\sim 10^{7}\) molecules; a cube of side \(\sim\lambda\) still holds of order \(10^{3}\)–\(10^{4}\). Count scatter and the Knudsen failure are therefore not the same cliff. There is no single universal \(N\) at which “pressure begins.”

**Data confidence:** High — \(P = nkT\), the \(\lambda(n)\) scaling, and the Knudsen failure of continuum hydro are handbook kinetic theory, reproduced in rarefied-gas and vacuum apparatus. The exact \(\mathrm{Kn}\) at which a given gauge or CFD scheme is declared invalid is a convention (medium); the existence of the \(\lambda/L\sim 1\) collapse is not.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Equation of state in the dilute, non-interacting envelope: \(P = nkT\). Virial corrections appear as density rises; they are a different failure of this envelope (correlations), not the Knudsen failure.
- Momentum flux on a wall from a Maxwellian population recovers \(P = nkT\) after averaging. A single impact is not \(P\).
- Mean free path as above; collision time \(\tau \sim \lambda/\bar v\) with \(\bar v \sim \sqrt{kT/m}\). In standard-density air \(\tau\) is of order \(10^{-10}\,\mathrm{s}\).
- Navier–Stokes hydrodynamics, including a local scalar \(P(\mathbf{r},t)\) and the [speed of sound](speed-of-sound.md), presupposes \(\mathrm{Kn}\ll 1\).

These relations describe the averaged wall load and the continuum field built from it. They do not derive \(k\) and they do not fix a universal vessel size.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two nested statistical buffers, neither of them a single universal length:
  1. **Count.** \(P\) as a stable reading requires enough independent impacts in the gauge window that the mean is not dominated by \(N^{-1/2}\) scatter.
  2. **Path versus apparatus.** Continuum \(P(\mathbf{r})\) further requires \(L\gtrsim\lambda\) (\(\mathrm{Kn}\lesssim 1\)). That length tracks density: it is tens of nanometres in standard air and centimetres to metres in a rough vacuum. The cliff moves with \(n\); it is not a material constant.

- **Clock rate / latency.** Wall impacts arrive on the collision clock (\(\sim 10^{-10}\,\mathrm{s}\) in standard air; much longer once the gas is rarefied). A gauge that resolves individual hits, or a drive faster than local equilibration, sees a shot sequence rather than \(P\). Ordinary mechanical gauges sit far above this clock.

- **Energy barriers or thresholds.** None holding a latched state. The operating resources are density, an equilibration window, and an apparatus larger than \(\lambda\). Ionization of the gas is a different family ([ionization threshold](ionization-threshold.md)) and removes the neutral-molecule population this envelope assumes.

- **Dominant failure modes.**
  - Spatial / rarefaction: \(\mathrm{Kn}\gtrsim 1\) → continuum hydro and a local \(P\) field collapse; the wall load is a ballistic rain.
  - Population: \(N\) too small in the sampled volume or window → the manometer reading jitters and \(P = nkT\) is not a stable output.
  - Temporal: observation faster than the impact / collision window → incomplete average.
  - Density (other direction): the gas is no longer dilute → virial / liquid corrections, a different envelope, not this one.

- **Emergent constant or stable output.** A steady wall pressure \(P = nkT\) and, when \(\mathrm{Kn}\) is small, a continuum hydrodynamic field built from that average.

### 4.6 Internal Consistency Notes

The Knudsen condition is a clean spatial-buffer statement, but the buffer is *relative* (\(\lambda/L\)), not a fixed nanometre stack. That is consistent with a statistical family and must not be rewritten as a universal node-count cliff. The \(N^{-1/2}\) count buffer is the same gap already recorded on [thermal equilibrium temperature](thermal-equilibrium-temperature.md).

Ideal-gas \(P = nkT\) and continuum hydro are not the same artifact. A free-molecular beam still delivers a time-averaged force; it does not support sound as a local mode. This entry owns the averaged wall load and the \(\mathrm{Kn}\) failure of the continuum reading. [Speed of sound](speed-of-sound.md) owns the long-wavelength lattice/gas mode that requires the continuum envelope.

QSA does not derive \(k\) or the hard-sphere \(d\) from node rules. Both are taken from the descriptive relations and from molecular sizes measured elsewhere.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — \(P = nkT\) and the \(\mathrm{Kn}\gtrsim 1\) collapse are solid, reproducible boundaries and translate directly into a statistical buffer plus an averaging window; there is no single universal \(N\) or \(L\), and the mapping should not pretend otherwise.

## Related entries

- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the \(T\) that enters \(P = nkT\)
- [Brownian motion](brownian-motion.md) — the same impact rain, averaged incompletely on a suspended particle
- [Speed of sound](speed-of-sound.md) — continuum mode that requires \(\mathrm{Kn}\ll 1\)
- [Ionization threshold](ionization-threshold.md) — removes the neutral population this envelope assumes
- [Phonon thermal conductivity](thermal-conductivity-phonon.md) — another transport coefficient set by a mean free path
