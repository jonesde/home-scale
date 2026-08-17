---
id: pyroelectric-fusion
title: Pyroelectric Fusion (Polar-Field Beam Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - field-threshold
  - thermal
confidence_data: medium
confidence_mapping: high
related:
  - muon-catalyzed-fusion
  - ferroelectric-remanence
  - dielectric-breakdown
  - deuteron-photodisintegration
updated: 2026-08-17
---

# Pyroelectric Fusion (Polar-Field Beam Gate)

### 4.1 Effect Name

Pyroelectric fusion (polar-field beam gate)

### 4.2 Macroscopic Observation

A pyroelectric crystal (typically \(\mathrm{LiTaO_3}\)) heated or cooled in a deuterium environment develops a large surface potential, ionizes D, and accelerates ions into a deuterated target. The D–D fusion channel then produces \(2.45\,\mathrm{MeV}\) neutrons (and the charged branch). Without the temperature ramp there is no accelerating field from this crystal and no such neutron pulse. Without deuterium there are no D–D neutrons. Naranjo, Gimzewski, and Putterman (2005) reported the process; later groups reproduced a neutron signal with a range of yields.

### 4.3 Established Quantitative Boundaries

- Pyroelectric surface potentials on millimetre-scale \(\mathrm{LiTaO_3}\) sit in the \(\sim 100\,\mathrm{kV}\) class for tens-of-kelvin ramps. That is a field / voltage *class*, not a universal set point.
- D–D fusion neutrons at \(2.45\,\mathrm{MeV}\) are the macroscopic witness. The D–D beam-target cross section is a steep function of ion energy in the tens-of-keV window; dropping the accelerating potential closes the useful channel.
- Reported neutrons per thermal cycle span a wide class (\(\sim 10^{3}\)–\(10^{5}\)). Part of that scatter is ion-species mix (\(\mathrm{D}^{+}\) versus \(\mathrm{D}_2^{+}\), which halves energy per nucleon). Treat yield as a class, not a constant.
- The crystal’s ferroelectric / pyroelectric response dies at its own \(T_C\) (\(\mathrm{LiTaO_3}\) \(T_C \sim 890\,\mathrm{K}\)). Ordinary ramps stay far below that. That thermal cliff belongs to the polar latch; this file owns the nuclear channel the field opens.

**Data confidence:** Medium — the existence of a D–D neutron signal from a pyroelectric accelerator is reproduced; absolute yield and the \(\mathrm{D}^{+}/\mathrm{D}_2^{+}\) mix are apparatus-dependent.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms. Pyroelectric bound charge \(\Delta P = \gamma_p\Delta T\) on an isolated face builds \(V\sim \Delta P\,d/\varepsilon\) until ionization, leakage, or breakdown limits it. Beam-target D–D fusion then follows the ordinary accelerator cross section at that ion energy. These describe the observed neutrons. They do not derive \(\gamma_p\) and they do not make this a net-energy source.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One polar crystal that can stand a pyroelectric field, plus deuterium (gas and/or deuterated target). The nuclear event is beam-target D–D, \(N\) small. Crystal area and D inventory are capacity.

- **Clock rate / latency.** The thermal ramp of the crystal (seconds). Fusion itself is prompt. This is not \(\tau_\mu\).

- **Energy barriers or thresholds.** Two stacked gates: (1) the pyroelectric field must reach the tens-of-keV ion-energy window; (2) the D–D fusion barrier is the ordinary beam-target Coulomb barrier, opened by that kinetic energy. Neither is a latch of the fused state.

- **Dominant failure modes.**
  - No ramp / no \(\Delta T\) \(\to\) no pyro field \(\to\) channel closed.
  - No deuterium \(\to\) no D–D neutrons.
  - Potential too low (leakage, breakdown, small \(\Delta T\)) \(\to\) cross section collapses.
  - \(T\to T_C\) of the polar host \(\to\) the field engine is gone (owned by [ferroelectric remanence](ferroelectric-remanence.md)).

- **Emergent constant or stable output.** A burst of \(2.45\,\mathrm{MeV}\) neutrons per thermal cycle, in a wide yield class, only while the field and the deuterium remain provisioned.

### 4.6 Internal Consistency Notes

This is **not** [muon-catalyzed fusion](muon-catalyzed-fusion.md). No muon is required. The nuclear gate is ordinary beam-target D–D; the uncommon piece is the polar crystal as a compact high-voltage engine. Do not file a pulsed-coil hydride as this machine: there is no pyroelectric accelerator in that cell.

The polar latch is a *supporting resource* (it writes the field). The fusion yield is an `energy-gate` output. Stacking them does not mint a tenth design.

Yield scatter is recorded as Medium data, not patched with a nuclear story. SAFETY: this file is a mapping of a handbook neutron channel, not a generator protocol.

### 4.7 Overall Confidence in the QSA Mapping

**High** on the machine class (pyro field + D \(\to\) D–D neutrons; no field or no D \(\to\) closed); **Medium** on any one yield number.

## Related entries

- [muon-catalyzed-fusion](muon-catalyzed-fusion.md) — the other uncommon hydrogen nuclear gate; different extra node
- [ferroelectric-remanence](ferroelectric-remanence.md) — the polar engine
- [dielectric-breakdown](dielectric-breakdown.md) — a field-opened channel that *destroys* the insulator; here the field is used as an accelerator
- [deuteron-photodisintegration](deuteron-photodisintegration.md) — photon unbinds \(d\); this file fuses two D
