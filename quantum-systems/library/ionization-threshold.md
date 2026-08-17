---
id: ionization-threshold
title: Ionization Threshold (Single-Particle Binding Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - thermal
confidence_data: high
confidence_mapping: high
related:
  - photoelectric-threshold
  - work-function-thermionic
  - x-ray-absorption-edge
  - semiconductor-gap-absorption
  - pair-production
  - dielectric-breakdown
  - plasma-frequency-cutoff
  - blackbody-spectrum
updated: 2026-08-17
---

# Ionization Threshold (Single-Particle Binding Gate)

### 4.1 Effect Name

Ionization threshold (single-particle binding gate)

### 4.2 Macroscopic Observation

A dilute gas remains electrically neutral under illumination or electron bombardment until the supplied energy crosses a species-specific ionization energy. Below that energy the gas does not furnish a standing population of free charges from this channel; above it, ions and electrons appear (photoionization continuum, discharge precursors, spectroscopic series limits). A cold atomic hydrogen cell does not conduct; the same atoms, presented with photons above the Lyman limit or with electrons above \(13.6\,\mathrm{eV}\), do.

### 4.3 Established Quantitative Boundaries

- Atomic first ionization energies (handbook): H \(I = 13.598\,\mathrm{eV}\); He \(I = 24.587\,\mathrm{eV}\) (\(\approx 24.6\,\mathrm{eV}\)). The one-electron ion He II sits at \(54.418\,\mathrm{eV}\). Molecular first ionization energies of the common gases are of the same order (H\(_2\) \(I \approx 15.43\,\mathrm{eV}\) is the evaluated handbook value).
- Spectroscopic mark of the atomic gate: the Rydberg series of the species converges to \(I\); the photoionization continuum opens at that limit. For H the Lyman limit is \(hc/I \approx 91.2\,\mathrm{nm}\).
- Collisional opening of the same gate: an incident electron (or other projectile) with kinetic energy below \(I\) does not ionize in the first inelastic channel; above \(I\) it can. Thermal opening of the same gate becomes appreciable only when \(kT\) is no longer negligible compared with \(I\) (Saha equilibrium in hot gases and stellar atmospheres). At room temperature \(kT \approx 0.026\,\mathrm{eV}\), so \(I/kT \sim 500\) for hydrogen: the thermal tail does not ionize a cold gas.
- Multi-electron atoms present a ladder of gates (first, second, … ionization energies), each closing or opening a specific charge state. Inner-shell ionization at keV is the same ladder continued; it is filed as [x-ray-absorption-edge](x-ray-absorption-edge.md).

**Data confidence:** High — \(I\) values for H, He, and the common atoms and molecules are among the most precise numbers in the library (optical series limits, photoelectron thresholds).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Photoionization onset:

  \[
  h\nu \ge I,\qquad \mathrm{KE}_{e} = h\nu - I
  \]

- Electron-impact onset: projectile kinetic energy \(\ge I\) (neglecting recoil and excited residual states, which shift the observed appearance potential by known spectroscopic intervals).
- Rydberg convergence (hydrogen-like, descriptive):

  \[
  E_n = I\bigl(1 - 1/n^2\bigr) \;\longrightarrow\; I \quad (n\to\infty)
  \]

- Saha ionization equilibrium for a hot dilute gas (descriptive of the *thermal* opening of the same gate):

  \[
  \frac{n_i n_e}{n_n}
  \propto T^{3/2}\exp\!\left(-\frac{I}{kT}\right)
  \]

Below \(I\), this conversion does not occur. Residual conductivity of a real gas is then from impurities, cosmic-ray seeds, or other channels — not from opening \(I\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One atom or molecule is the hardware for one conversion. A macroscopic ionized gas (a measurable charge density, a discharge, a nebular emission measure) is the summed output of a large population. There is no collective buffer that must be filled before a *single* ionization can happen. Density enters later: recombination, screening, and breakdown avalanches are many-body sequels, not the gate itself.

- **Clock rate / latency.** Optical / UV photoionization tracks the electromagnetic cycle of the ionizing photon. Electron-impact ionization is set by the collision duration. Neither is a laboratory-scale latency. Recombination times in a dilute gas can be long; that is the *closing* clock of the ionized state, not the opening of \(I\).

- **Energy barriers or thresholds.** The operating gate is the ionization energy \(I\) of the species and charge state. Photons, projectiles, or a thermal tail are interchangeable opening resources for that one barrier.

- **Dominant failure modes.**
  - Under-threshold: \(E < I\) (whether \(E = h\nu\), projectile KE, or the relevant scale of \(kT\)) → the conversion does not occur. Neutral gas remains neutral in this channel. That is the collapse of the effect.
  - Missing species: the atom is already stripped of that electron → that particular gate is gone; a deeper gate may remain.
  - Recombination / attachment: the ionized population is not a latched state. Remove the drive and the charges return. That is decay of the output, not a denial of the gate.

- **Emergent constant or stable output.** A species-specific series limit and a free-charge yield that turns on at \(I\), together with whatever subsequent plasma or chemical sequels the newly freed charges support.

### 4.6 Internal Consistency Notes

The mapping is the cleanest single-node member of the photoelectric-class family: one bound electron, one number, one cliff. [Photoelectric-threshold](photoelectric-threshold.md) and [work-function-thermionic](work-function-thermionic.md) are the same unbinding, with the solid’s work function in place of \(I\). [Semiconductor-gap-absorption](semiconductor-gap-absorption.md) is unbinding into a crystal band rather than into vacuum. [X-ray-absorption-edge](x-ray-absorption-edge.md) is the inner-shell rung of this ladder. [Pair-production](pair-production.md) is *not* unbinding; it is rest-mass creation and must not be folded into \(I\).

[Dielectric-breakdown](dielectric-breakdown.md) uses ionization as a microscopic step inside a field-driven avalanche. The present entry owns the single-particle gate; breakdown owns the many-body field cliff, which is messier and is filed separately.

A remaining gap: QSA takes \(I\) from the handbook. For hydrogen the Rydberg formula already *is* the closed description of the ladder; for many-electron atoms the number is measured. That is not a conflict. Appearance potentials in molecules can sit above the adiabatic \(I\) when the Franck–Condon factor at threshold is small — a softness of the observed onset, not a second gate.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(I\) is a precisely measured single-particle energy gate, below-threshold neutrality is the observed non-occurrence, and the family mapping is the same conversion as the photoelectric and X-ray edges.

## Related entries

- [photoelectric-threshold](photoelectric-threshold.md) — unbinding from a metal surface; \(\varphi\) in place of \(I\)
- [work-function-thermionic](work-function-thermionic.md) — the same surface unbinding, opened by heat
- [x-ray-absorption-edge](x-ray-absorption-edge.md) — inner-shell rung of the same ionization ladder
- [semiconductor-gap-absorption](semiconductor-gap-absorption.md) — unbinding into a crystal band at \(E_g\)
- [pair-production](pair-production.md) — rest-mass creation, not ionization of a pre-existing electron
- [dielectric-breakdown](dielectric-breakdown.md) — field-driven avalanche that *uses* this gate as a step
- [plasma-frequency-cutoff](plasma-frequency-cutoff.md) — collective response of the charge population *after* ionization
- [blackbody-spectrum](blackbody-spectrum.md) — thermal photon bath that may or may not sit above \(I\)
