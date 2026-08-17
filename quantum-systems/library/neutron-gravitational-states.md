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
related:
  - bose-einstein-condensate
  - quantum-hall-effect
  - total-internal-reflection
updated: 2026-08-17
---

# Neutron Gravitational Quantum States (UCN Mirror Well)

### 4.1 Effect Name

Neutron gravitational quantum states (UCN mirror well)

### 4.2 Macroscopic Observation

Ultracold neutrons bouncing on a horizontal mirror in the Earth’s gravitational field occupy discrete vertical states. Transmission past an absorber (or scatterer) placed a height \(z\) above the mirror stays near zero until \(z\) clears the ground-state height, then rises in steps as successive states fit. Nesvizhevsky et al. (2002, ILL) first reported the ground state. Neutrons that are not ultracold, or a gap with no mirror, do not show these steps.

### 4.3 Established Quantitative Boundaries

- Characteristic height and energy of the ground state (Airy / gravitational well):

  \[
  z_1 \approx 13.7\,\mu\mathrm{m}, \qquad
  E_1 \approx 1.4\,\mathrm{peV}.
  \]

  Higher states sit at \(z_n = z_1\,\xi_n/\xi_1\) with Airy zeros \(\xi_n\).

- Hardware: ultracold neutrons (\(v\lesssim 8\,\mathrm{m\,s^{-1}}\) class) plus a horizontal neutron mirror (material optical potential) plus Earth’s \(g\). An absorber / scatterer at height \(z\) is the readout slit.
- Collapse: \(z < z_1\) \(\to\) essentially no transmission of the ground state; neutrons too fast \(\to\) not bound in this well; no mirror \(\to\) no bouncing states.

**Data confidence:** High — existence of the ground state and the \(\sim 10\,\mu\mathrm{m}\) height class are reproduced (GRANIT / qBounce). Exact \(z_n\) in any one apparatus is medium (mirror roughness, absorber resolution).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms. The vertical Schrödinger problem with a hard wall at \(z=0\) and potential \(mgz\) has Airy-function eigenstates. Transmission versus absorber height maps those turning points. These describe the observed steps. They do not derive \(g\) or \(m_n\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One ultracold neutron plus a horizontal mirror plus a gravitational potential over \(\sim 10\,\mu\mathrm{m}\). The spatial buffer is the *height of the well*, not a metal film. A thermal neutron beam is the wrong buffer.

- **Clock rate / latency.** Bounce / dwell times on the millimetre-per-second UCN scale (ms–s). This is not a nuclear lifetime.

- **Energy barriers or thresholds.** The gravitational level spacing (\(\mathrm{peV}\)) is the “gap” that protects a state. \(kT\) at 300 K is enormous compared with \(E_1\); the neutrons are *selected* as UCN, not thermalized into this well.

- **Dominant failure modes.**
  - Spatial: absorber below \(z_1\) \(\to\) ground state does not pass.
  - Buffer: neutrons not ultracold \(\to\) not bound.
  - Mirror: no reflecting floor \(\to\) no well.
  - \(g\to 0\) (free fall / orbital) \(\to\) this well vanishes. That is a thought-collapse, not a laboratory knob.

- **Emergent constant or stable output.** A stepwise transmission versus height, with the first step at the \(z_1\sim 14\,\mu\mathrm{m}\) class, while UCN, mirror, and \(g\) remain.

### 4.6 Internal Consistency Notes

The family name “gapped” is loose: the spacing is gravitational, not a pairing gap. Same honesty as the He-4 entry. Do not fold this into `gapped-condensate` as a member (no charge, no \(\lambda\), no \(T_c\)).

\(z_1\) and \(E_1\) are taken from the Airy problem with measured \(m_n\) and \(g\). That is a derived *class*, not a new fundamental constant.

Aharonov–Bohm and this file are both “phase / bound-state leftovers” that do not mint a tenth design.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the micrometre height cliff and the UCN + mirror hardware are real; the family fit is loose and \(z_n\) in any one setup is a resolution-limited class.

## Related entries

- [bose-einstein-condensate](bose-einstein-condensate.md) — another ultracold bound population; different well
- [quantum-hall-effect](quantum-hall-effect.md) — another discrete ladder with an underived / taken output
- [total-internal-reflection](total-internal-reflection.md) — the neutron mirror is a material-optical analog of TIR
