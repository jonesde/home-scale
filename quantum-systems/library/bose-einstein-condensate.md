---
id: bose-einstein-condensate
title: Bose–Einstein Condensate (Density-Set Coherence Cliff)
status: formal
family: gapped-coherence
constraints:
  - thermal
  - spatial-buffer
confidence_data: high
confidence_mapping: medium
related:
  - superfluid-helium-4
  - superconductivity
  - thermal-equilibrium-temperature
  - ideal-gas-pressure
  - flux-quantization
  - quantum-hall-effect
updated: 2026-08-17
---

# Bose–Einstein Condensate (Density-Set Coherence Cliff)

### 4.1 Effect Name

Bose–Einstein condensate (density-set coherence cliff)

### 4.2 Macroscopic Observation

A dilute gas of alkali atoms, confined in a magnetic or optical trap and cooled, develops a macroscopic occupation of the lowest trap mode once a density- and temperature-dependent threshold is crossed. After release, the velocity distribution is bimodal: a narrow peak sits on a broader thermal cloud. Two independent condensates released into each other produce interference fringes. Warming the sample, or letting the density drop, removes the peak and the fringes; the cloud is then an ordinary thermal gas.

### 4.3 Established Quantitative Boundaries

- Ideal-gas threshold, written as a phase-space density (handbook form used to locate \(T_c\)):

  \[
  n\lambda_{\mathrm{th}}^3 \simeq 2.612, \qquad \lambda_{\mathrm{th}} = \frac{h}{\sqrt{2\pi m kT}}
  \]

  \(2.612\) is \(\zeta(3/2)\). In a harmonic trap the same condition is evaluated at the peak density and gives a \(T_c\) that scales as \(N^{1/3}\) times the trap frequency. Both statements are fits to where the condensate fraction appears, not a derivation of the nodes.

- Laboratory alkali condensates sit at nanokelvin to microkelvin temperatures with typical atom numbers \(10^3\)–\(10^7\). Those ranges are the working envelope of the existing apparatus class, not a single universal cliff.
- The condensate fraction \(N_0/N\) falls to zero as \(T \to T_c^-\) or as the density is lowered through the threshold at fixed \(T\). Either route destroys the bimodal peak and the interference contrast.
- The trapped condensate is not a self-bound droplet: when the trap is switched off the cloud expands. Loss of atoms (background-gas collisions, three-body recombination) lowers \(n\) and can drop the sample back through \(T_c(n)\).

**Data confidence:** High — the phase-space condition, the nK–\(\mu\)K / \(10^3\)–\(10^7\) working envelope, bimodal time-of-flight, and interference contrast are multiply reproduced. Species-by-species scattering lengths and exact \(T_c\) shifts from interactions are medium and are not required here.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Thermal wavelength and ideal-gas critical line:

  \[
  n\lambda_{\mathrm{th}}^3 = \zeta(3/2) \approx 2.612
  \]

  Condensate present for \(n\lambda_{\mathrm{th}}^3\) above that value; absent below it.

- Condensate fraction of a uniform ideal Bose gas (descriptive \(T\)-dependence):

  \[
  \frac{N_0}{N} = 1 - \left(\frac{T}{T_c}\right)^{3/2} \qquad (T \le T_c)
  \]

  Harmonic-trap exponents differ; the load-bearing fact is \(N_0 \to 0\) at \(T_c\), not the exponent.

- Interacting-gas bookkeeping (Gross–Pitaevskii / chemical-potential form) introduces a healing length and a sound speed set by density and scattering length. Those lengths describe the *already condensed* cloud. They are not used here to invent a pairing gap or to relocate \(T_c\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A trapped cloud whose phase-space density crosses \(n\lambda_{\mathrm{th}}^3 \simeq 2.612\). The “nodes” are the atoms; the buffer is the combination of number, volume, and temperature that puts enough of them in one mode. There is no measured few-nanometre continuity cliff of the [reflection](reflection.md) kind, and no single minimum \(N\) at which the effect switches on. \(10^3\)–\(10^7\) is the envelope in which a stable condensate fraction is routinely read out, not a derived node-count threshold.

- **Clock rate / latency.** Trap frequencies set the sloshing / expansion clocks of the cloud; they are apparatus scales, not a universal condensate clock. There is no Josephson \(2e/h\) lock and no cyclotron clock. Interaction-driven sound in the condensed cloud is a hydrodynamic response of an already-formed condensate, analogous to second sound on [superfluid-helium-4](superfluid-helium-4.md).

- **Energy barriers or thresholds.** The load-bearing threshold is thermal / density: \(T > T_c(n)\), or \(n\) dropped at fixed \(T\), removes macroscopic occupation and phase coherence. This is not a latched anisotropy barrier and not a measured superconducting gap. Holding the condensate requires continuous cooling and trapping resources; it is not a zero-power latch.

- **Dominant failure modes.**
  - Thermal: \(T > T_c(n)\) \(\to\) condensate fraction \(\to 0\) \(\to\) no bimodal peak, no interference.
  - Spatial / density: expansion, atom loss, or a weaker trap drops \(n\) through the critical line at fixed \(T\) \(\to\) same collapse.
  - Trap loss: without confinement the cloud is not a stable laboratory condensate.
  - Heating / three-body loss: practical routes to the two collapses above, not a third machine class.

- **Emergent constant or stable output.** A macroscopic occupation of one mode — read as a condensate fraction, a narrow velocity peak, and interference contrast — only while the cloud stays above the critical phase-space density.

### 4.6 Internal Consistency Notes

The thermal / density cliff is clean and maps onto a failure envelope. That is as much as this entry can claim tightly.

The mapping does not close at the same level as [josephson-effect](josephson-effect.md) or [superfluid-helium-4](superfluid-helium-4.md), for three recorded reasons.

1. **Family tension.** The file sits in `gapped-coherence` because the taxonomy groups protected collective modes that die at a critical temperature. An ideal-gas BEC has no measured pairing gap. Collapse is loss of macroscopic occupation and of phase coherence, not gap closure of the superconducting kind. Forcing a gap onto the alkali cloud would be an interpretive overlay. The tension is left visible.
2. **No sharp hardware cliff.** \(N \sim 10^3\)–\(10^7\) is a working envelope, not a derived minimum node count. QSA here *takes* the measured phase-space condition as the specification; it does not obtain \(2.612\) from node rules.
3. **Continuous resources.** Unlike a permanent magnet or a trapped fluxoid, the laboratory condensate is not held at zero continuous power. That does not eject it from the family, but it means this is not a latch.

Relation to [superfluid-helium-4](superfluid-helium-4.md) is analogical. Liquid helium is dense and strongly interacting and has a sharp \(T_\lambda\) at \(2.17\,\mathrm{K}\); alkali BECs are dilute and have a \(T_c\) set by \(n\). They share a thermal coherence cliff and quantized winding; they are not the same hardware. No claim is made about “what the condensate is.”

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the \(T_c(n)\) cliff, the working envelope, and the loss of interference contrast are solid measured boundaries, but the family assignment is looser than a pairing gap, the minimum node count is not sharp, and the phase-space threshold is taken from the ideal-gas condition rather than derived.

## Related entries

- [superfluid-helium-4](superfluid-helium-4.md) — dense, chargeless analog with a fixed \(T_\lambda\); not the same hardware
- [superconductivity](superconductivity.md) — charged gapped coherence; contrast case for a real gap and a zero-power persistent current
- [thermal-equilibrium-temperature](thermal-equilibrium-temperature.md) — \(T\) itself is an ensemble reading; \(T_c\) is a cliff on that reading
- [ideal-gas-pressure](ideal-gas-pressure.md) — the same cloud below the critical phase-space density is an ordinary thermal gas
- [flux-quantization](flux-quantization.md) — integer winding in a charged condensate; the analog here is phase winding of the atomic cloud
- [quantum-hall-effect](quantum-hall-effect.md) — another collective state whose mapping is limited by an underived quantized output
