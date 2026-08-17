---
id: speed-of-sound
title: Speed of Sound (Long-Wave Acoustic Slope)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
  - clock-latency
confidence_data: high
confidence_mapping: high
related:
  - phonon-dispersion
  - debye-cutoff
  - elasticity
  - melting
  - thermal-conductivity-phonon
  - ideal-gas-pressure
updated: 2026-08-17
---

# Speed of Sound (Long-Wave Acoustic Slope)

### 4.1 Effect Name

Speed of sound (long-wave acoustic slope)

### 4.2 Macroscopic Observation

A pressure or shear disturbance launched in air, water, or a solid arrives at a distant detector after a finite delay. The implied speed is a material-typical number, far below the speed of light, and is independent of frequency through the ordinary audible and ultrasonic window. Solids carry a faster longitudinal wave and a slower shear wave. Liquids and gases carry only a compressional wave. A vacuum carries no sound.

### 4.3 Established Quantitative Boundaries

- Measured long-wave structure: \(v_s = \sqrt{C/\rho}\), with \(C\) the appropriate adiabatic elastic modulus and \(\rho\) the mass density.
- Dry air at \(20^\circ\mathrm{C}\), 1 atm: \(v_s \approx 343\,\mathrm{m\,s^{-1}}\).
- Liquid water near \(20^\circ\mathrm{C}\): \(v_s \approx 1480\,\mathrm{m\,s^{-1}}\).
- Common steels, longitudinal: \(\approx 5000\)–\(6000\,\mathrm{m\,s^{-1}}\). Crystalline solids as a class sit in the kilometres-per-second range.
- Shear (transverse) sound exists in solids. It is absent as a propagating mode in liquids and gases at ordinary acoustic frequencies, where the shear modulus \(G = 0\). A vacuum has no coupled mechanical medium: \(v_s\) is undefined there, not a small number.
- The same number is the slope \(d\omega/dq\) of an acoustic branch as \(q\to 0\). That slope is no longer the group velocity once the wavelength approaches the inter-node spacing. The full \(\omega(q)\) belongs to `phonon-dispersion`.
- Ideal-gas air tracks \(v_s = \sqrt{\gamma P/\rho} = \sqrt{\gamma RT/M}\) (\(\gamma \approx 1.4\)), rising as \(\sqrt{T}\). Liquid water does not follow that gas law.

**Data confidence:** High — speeds in air, water, and engineering solids are multiply reproduced handbook and metrology values. Absence of a fluid shear wave is equally well established. Anisotropy and temperature coefficients are high as a class and medium for any one unstated alloy.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Longitudinal / compressional speed:

  \[
  v_L = \sqrt{\frac{K + 4G/3}{\rho}}
  \]

  In a fluid \(G = 0\), so \(v_L = \sqrt{K_s/\rho}\) with \(K_s\) the adiabatic bulk modulus.

- Shear speed (solid only):

  \[
  v_T = \sqrt{\frac{G}{\rho}}
  \]

- Long-wave acoustic dispersion:

  \[
  \omega = v_s |q| \qquad (qa \ll 1)
  \]

- Transit time on a path \(L\): \(t = L/v_s\).

The moduli \(C\) are the small-strain numbers recorded under `elasticity`. This entry does not derive \(C\) or \(\rho\); it records the measured long-wave slope they produce.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A coupled mechanical medium — an ion grid in a solid, or a colliding density field in a fluid — with many nodes per wavelength. The continuum slope is a stable output only for \(\lambda \gg a\) (lattice constant or mean spacing). A vacuum has no such nodes and produces no wave. A fluid has compressional couplings and no shear restoring couplings, so the shear branch is not provisioned. There is no single nanometre-scale thickness cliff analogous to the optical mirror; the sharp hardware condition is the presence of the medium and of the relevant restoring modulus.

- **Clock rate / latency.** The macroscopic clock is the transit time \(L/v_s\) and the period \(\lambda/v_s\). That clock is orders of magnitude slower than the zone-boundary / Debye clock of the same solid (terahertz class; `debye-cutoff`). Relative to a human clock a laboratory path is still delayed: milliseconds in air across a room, microseconds in a metal bar of similar length.

- **Energy barriers or thresholds.** No latched barrier. The operating condition is a finite restoring modulus (bulk, and shear if a shear wave is claimed) plus a density. The wave is a launched collective oscillation of the coupled nodes, not a memory.

- **Dominant failure modes.**
  - Medium: vacuum, or a density so low that couplings do not form a collective wave on the path → no sound.
  - Restoring force: \(G = 0\) (liquids, gases) → no propagating shear mode. Melting of a crystal is the same shear-branch collapse (`melting`).
  - Wavelength: \(qa \sim 1\) → \(v_s\) is no longer the group velocity; the mode still exists on the `phonon-dispersion` curve until the zone-boundary / Debye ceiling.
  - Dissipative: viscosity, grain scattering, and relaxation attenuate the amplitude. That is not the same cliff as a missing modulus.

- **Emergent constant or stable output.** A material-typical, frequency-independent (long-wave) pair \(\{v_L, v_T\}\) in a solid, or a single \(v_L\) in a fluid, as the synchronized long-wavelength output of the coupled mechanical population.

### 4.6 Internal Consistency Notes

The vacuum / fluid-shear / solid-both-waves split maps onto which restoring couplings are present. Reading \(v_s\) as the \(q\to 0\) slope of the same grid that `phonon-dispersion` maps at finite \(q\) is internally consistent: one machine, two windows.

A closed mapping would also say why a given solid has the \(C\) it has, from node-spring rules, rather than taking handbook moduli as input. That derivation is not done here; it is the same gap carried by `elasticity`. The speed measurement does not depend on closing it.

Ideal-gas air and condensed water share a Newton–Laplace form and not a common microscopic clock. They are the same QSA class (long-wave mechanical slope) on different hardware. `ideal-gas-pressure` owns the averaged wall force, not this slope.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the measured speeds, the \(v_s=\sqrt{C/\rho}\) structure, and the vacuum / no-shear failures translate directly into a medium-plus-modulus hardware condition and a long-wave clock; remaining gaps are about deriving \(C\), not about the existence or location of the slope.

## Related entries

- [phonon-dispersion](phonon-dispersion.md) — full \(\omega(q)\); this entry is only the acoustic \(q\to 0\) slope
- [debye-cutoff](debye-cutoff.md) — the short-wave clock ceiling on the same grid
- [elasticity](elasticity.md) — the moduli \(C\) that enter \(v_s=\sqrt{C/\rho}\)
- [melting](melting.md) — shear restoring force and Bragg order collapse together
- [thermal-conductivity-phonon](thermal-conductivity-phonon.md) — uses \(v_s\) as the carrier speed
- [ideal-gas-pressure](ideal-gas-pressure.md) — gas as a different mechanical medium; \(v_s=\sqrt{\gamma P/\rho}\)
