---
id: superfluid-helium-4
title: Superfluid Helium-4 (Chargeless Superflow)
status: formal
family: gapped-coherence
constraints:
  - thermal
  - spatial-buffer
  - energy-barrier
confidence_data: high
confidence_mapping: high
related:
  - bose-einstein-condensate
  - superconductivity
  - flux-quantization
  - josephson-effect
  - type-ii-critical-field
  - thermal-equilibrium-temperature
updated: 2026-08-17
---

# Superfluid Helium-4 (Chargeless Superflow)

### 4.1 Effect Name

Superfluid helium-4 (chargeless superflow)

### 4.2 Macroscopic Observation

Liquid \(^4\mathrm{He}\) below the \(\lambda\)-point flows through packed powder and fine capillaries without measurable viscosity, climbs the walls of an open vessel as a film, and, when one side of a superleak is heated, produces a fountain of liquid (the thermomechanical / fountain effect). Persistent currents circulate in a closed torus on laboratory timescales. Above the \(\lambda\)-point the same liquid is an ordinary (if cryogenic) fluid: the superleak clogs, the fountain stops, and a finite viscosity returns.

### 4.3 Established Quantitative Boundaries

- \(\lambda\)-point at saturated vapour pressure:

  \[
  T_\lambda = 2.17\,\mathrm{K}
  \]

  The heat capacity has a \(\lambda\)-shaped singularity there. Under pressure the \(\lambda\)-line moves; it ends when the liquid freezes. Those are measured phase-boundary facts, not used here as a mechanism.

- Superfluid fraction \(\rho_s(T)\): \(\rho_s \to 0\) as \(T \to T_\lambda^-\), and \(\rho_s / \rho \to 1\) as \(T \to 0\). The complementary normal fraction \(\rho_n = \rho - \rho_s\) is what a torsion-pendulum (Andronikashvili) stack continues to drag. This two-fluid bookkeeping is *data* — a decomposition of the observed density into a fraction that flows through a superleak and a fraction that does not — not an axiom that two liquids occupy the same volume.
- Viscosity through a fine channel \(\to 0\) for the superfluid fraction below \(T_\lambda\). The same channel shows a finite viscosity above \(T_\lambda\).
- Superflow collapses above a critical velocity \(v_c\). Observed \(v_c\) is geometry-dependent (channel size, film thickness, wall condition) and typically lies far below the Landau estimate taken from the roton minimum. The existence of a velocity cliff is high confidence; any one numerical \(v_c\) is medium.
- Circulation around a closed superfluid path is quantized:

  \[
  \kappa = \frac{h}{m_4} \approx 9.97\times 10^{-8}\,\mathrm{m^2\,s^{-1}}
  \]

  Quantized vortices in the rotating liquid carry this increment. That is the chargeless counterpart of \(\Phi_0\) on [flux-quantization](flux-quantization.md).

**Data confidence:** High — \(T_\lambda\), the fountain and superleak responses, \(\rho_s(T)\), and the circulation quantum are handbook measurements. Channel-specific \(v_c\) is medium.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Two-fluid decomposition of the observed mass density:

  \[
  \rho = \rho_n(T) + \rho_s(T), \qquad \mathbf{j} = \rho_n\mathbf{v}_n + \rho_s\mathbf{v}_s
  \]

  \(\rho_s(T_\lambda) = 0\). The fountain / thermomechanical relation \(\Delta P = \rho s\,\Delta T\) (London form) fits the pressure head across a superleak; it is a fit to the fountain data.

- Quantized circulation on a closed path that stays in the superfluid:

  \[
  \oint \mathbf{v}_s\cdot d\mathbf{l} = n\,\frac{h}{m_4}, \qquad n \in \mathbb{Z}
  \]

- Superflow is lost for \(T > T_\lambda\) or for \(|\mathbf{v}_s| > v_c\) (channel-dependent). Those are the operating inequalities, not a derived \(v_c(d)\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A connected volume of liquid \(^4\mathrm{He}\) below \(T_\lambda\), large enough to support a nonzero \(\rho_s\). The *demonstration* of vanishing viscosity further requires a spatial filter — a superleak or film — that the normal fraction cannot pass and the superfluid fraction can. That filter is apparatus, not the condensate buffer. Quantized circulation requires a closed path, as in [flux-quantization](flux-quantization.md), with vortex cores as the chargeless analog of mixed-state defects on [type-ii-critical-field](type-ii-critical-field.md). There is no charge, no London \(\lambda\), and no Meissner expulsion.

- **Clock rate / latency.** There is no Josephson voltage–frequency lock (no \(e\)). Weak-link apertures in helium do produce an analogous current–phase oscillation; that is a related observation, not the primary artifact here. Second sound (a temperature wave in the two-fluid bookkeeping) is a hydrodynamic clock of the *already formed* superfluid, not the clock that opens the \(\lambda\)-point.

- **Energy barriers or thresholds.** \(T_\lambda\) is the thermal cliff: \(\rho_s\) vanishes and the superleak / fountain / persistent-current responses go with it. \(v_c\) is a velocity threshold that dumps superflow into a dissipative channel (vortex nucleation / coupling to the normal fraction). Neither is a static anisotropy barrier of the [permanent-magnet-latch](permanent-magnet-latch.md) kind; holding a persistent current still costs no continuous power while \(T < T_\lambda\) and \(v < v_c\).

- **Dominant failure modes.**
  - Thermal: \(T > T_\lambda\) \(\to \rho_s = 0\) \(\to\) ordinary viscous liquid.
  - Velocity: \(v > v_c\) \(\to\) dissipation, even though \(T < T_\lambda\).
  - Topology: an open path cannot hold a persistent circulating integer; a blocked superleak cannot demonstrate the viscosity collapse.
  - Solidification: crossing the melting curve removes the liquid hardware.

- **Emergent constant or stable output.** A chargeless superflow (vanishing viscosity through a superleak, fountain head, persistent current) together with a circulation quantum \(h/m_4\), produced only while \(T < T_\lambda\) and \(v < v_c\).

### 4.6 Internal Consistency Notes

This is the clean chargeless member of the gapped-coherence family. The thermal cliff, the superleak filter, the fountain, and the circulation integer are the same *kind* of specification as \(T_c\), \(R = 0\), and \(\Phi_0\), without electromagnetic screening. That is a consistency check on the family: charge is not required for the machine class.

Two-fluid language is kept as bookkeeping of \(\rho_s(T)\) and \(\rho_n(T)\). It is not promoted to a claim that two substances are present, and it is not used to derive \(T_\lambda = 2.17\,\mathrm{K}\) from node rules. Why the \(\lambda\)-point sits at that temperature is a gap.

The family name “gapped” is slightly loose here: the load-bearing collapse is loss of \(\rho_s\) at \(T_\lambda\) (and of superflow at \(v_c\)), not a measured charge gap of the superconducting kind. The assignment follows the taxonomy rule — protected collective mode with a critical temperature — not a pairing-gap identification.

Relation to [bose-einstein-condensate](bose-einstein-condensate.md) is analogical (thermal / density cliff, phase coherence, quantized winding), not identity of hardware. Liquid helium is dense and strongly interacting; alkali BECs are dilute. The two entries must not be collapsed into one machine.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(T_\lambda\), \(\rho_s(T)\), the superleak / fountain collapses, and \(h/m_4\) are sharp measured boundaries and translate directly into thermal, spatial, and velocity-threshold specifications; the open items are the numerical origin of \(T_\lambda\) and channel-by-channel \(v_c\), not the existence of the envelope.

## Related entries

- [bose-einstein-condensate](bose-einstein-condensate.md) — dilute, density-set thermal cliff; analog, not the same hardware
- [superconductivity](superconductivity.md) — charged analog: dissipationless flow below a critical temperature
- [flux-quantization](flux-quantization.md) — charged counterpart of the circulation integer
- [josephson-effect](josephson-effect.md) — weak-link / aperture analog once a voltage (or its helium counterpart) is present
- [type-ii-critical-field](type-ii-critical-field.md) — vortex lattice as an array of phase defects; here the quantum is \(h/m_4\)
- [thermal-equilibrium-temperature](thermal-equilibrium-temperature.md) — \(T_\lambda\) is a thermal cliff sitting on top of an ordinary temperature reading
