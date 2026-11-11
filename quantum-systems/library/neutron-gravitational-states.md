---
id: neutron-gravitational-states
title: Neutron Gravitational Quantum States (UCN Mirror Well)
status: formal
family: gapped-coherence
constraints:
  - spatial-buffer
  - energy-barrier
  - field-threshold
confidence_data: high
confidence_mapping: medium
review_depth: light
related:
  - bose-einstein-condensate
  - quantum-hall-effect
  - total-internal-reflection
updated: 2026-11-11
---

# Neutron Gravitational Quantum States (UCN Mirror Well)

### 4.1 Effect Name

Neutron gravitational quantum states (UCN mirror well)

### 4.2 Macroscopic Observation

Ultracold neutrons moving above a horizontal mirror in the Earth's gravitational field occupy discrete vertical states. The transmission through a slit between the mirror and an absorber above it is zero until the slit height clears the lowest state, and then rises. Faster neutrons, or a slit with no mirror, do not show this.

### 4.3 Established Quantitative Boundaries

- **Model (Airy solution, hard mirror plus \(mgz\)).** Energies of the four lowest states: 1.4, 2.5, 3.3 and 4.1 peV. Only \(g\), the neutron mass and Planck's constant enter [S1].
- **Computed here.** Length scale \(z_0 = (\hbar^2/2m^2g)^{1/3} = 5.87\) µm with the neutron mass [S3] and standard gravity. Classical turning heights \(z_n = a_n z_0\) with the Airy zeros 2.338, 4.088, 5.521, 6.787: 13.7, 24.0, 32.4 and 39.8 µm. Energies \(mgz_n\): 1.41, 2.46, 3.32, 4.08 peV, matching [S1]. \(E_1/k_B = 16\) nK.
- **Measured.** A slit lower than about 15 µm is not transparent to neutrons: the count rate through it is zero while visible light passes. The result was reproduced 11 times with different mirror configurations [S1]. First reported in 2002 [S2]; that paper was not opened.
- **Measured.** The fitted heights lie above the ideal values by a constant offset of about 3 µm, because the wave function must overlap the absorber sufficiently to be absorbed; the fit is smoothed with a resolution of at least 2 µm [S1].
- **Measured.** Apparatus: horizontal velocity 5–15 m s⁻¹, vertical velocity below 5 cm s⁻¹; bottom mirrors 6 cm and 10 cm long; absorber positioned to a few micrometres [S1].
- **Computed here.** A neutron confined to the lowest state has a peak vertical speed \(\sqrt{2gz_1} = 1.6\) cm s⁻¹ and a classical bounce period of 3.3 ms; a 10 cm mirror at 10 m s⁻¹ is crossed in 10 ms, about three periods.

**Data confidence:** High for the existence of the lowest state and its height class, from the full experimental paper. Heights are resolved to a few micrometres, comparable to the offset correction.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms. The vertical Schrödinger problem with a wall at \(z = 0\) and potential \(mgz\) has Airy-function states with

\[
E_n = mg\,a_n\left(\frac{\hbar^2}{2m^2g}\right)^{1/3}
\]

and the source uses the equivalent semiclassical form \(E_n \propto (n - \tfrac14)^{2/3}\), accurate even for \(n = 1\) [S1]. These describe the observed steps. They do not derive \(g\) or the neutron mass.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One ultracold neutron, a horizontal mirror and a gravitational potential over about 14 µm. The buffer is the height of the well. The state is a single-particle one; the beam supplies statistics, not a collective.

- **Clock rate / latency.** The bounce period, 3.3 ms in the lowest state. The mirror must be long enough for several periods at the horizontal speed.

- **Energy barriers or thresholds.** The level spacing, about 1 peV (16 nK). Room-temperature \(k_BT\) is larger by ten orders of magnitude; the neutrons are selected by their vertical velocity, not thermalized into the well.

- **Dominant failure modes.**
  - **Threshold** — slit height: below about 15 µm (ideal value 13.7 µm plus a 3 µm offset) the lowest state does not pass. Resolved to a few micrometres; the edge is softened by tunnelling into the absorber.
  - **Threshold** — vertical velocity: above a few centimetres per second the neutron is not in the lowest states.
  - **Threshold** — mirror: no reflecting floor, no well.
  - **Crossover** — mirror length: too few bounce periods and the states are not resolved.

- **Emergent constant or stable output.** Zero transmission below the lowest state and a stepwise rise above it, with the first step near 14–15 µm.

### 4.6 Internal Consistency Notes

The family name "gapped" is loose: the spacing is gravitational, not a pairing gap. This entry is not a member of `gapped-condensate` (no charge, no screening length, no critical temperature), and it is a one-node state.

Sourcing changed no numbers: 13.7 µm and 1.4 peV are confirmed, the first by computation and the second by the paper. Two things were added: the measured threshold is about 15 µm, above the ideal turning height by a 3 µm absorber offset, and the vertical speed that defines "ultracold enough" is centimetres per second, where the first version quoted the total speed class.

\(z_1\) and \(E_1\) follow from the Airy problem with the measured neutron mass and \(g\). No new constant is involved.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the micrometre height threshold and the hardware are measured; the family fit is loose and the heights are resolution-limited.

## Related entries

- [bose-einstein-condensate](bose-einstein-condensate.md) — another ultracold bound population; different well
- [quantum-hall-effect](quantum-hall-effect.md) — another discrete ladder
- [total-internal-reflection](total-internal-reflection.md) — the neutron mirror is a material-optical analogue

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Nesvizhevsky et al., *Phys. Rev. D* 67, 102002 (2003), arXiv:hep-ph/0306198](https://arxiv.org/abs/hep-ph/0306198) | full-text | Full account of the experiment: level energies, non-transparency below about 15 µm, 11 repeats, velocity components, mirror lengths, 3 µm offset. |
| S2 | [Nesvizhevsky et al., *Nature* 415, 297 (2002)](https://doi.org/10.1038/415297a) | cited-only | First report. Publisher page not reachable. |
| S3 | [CODATA 2022, neutron mass (NIST)](https://physics.nist.gov/cgi-bin/cuu/Value?mn) | full-text | Neutron mass used in the computed heights and energies. |
