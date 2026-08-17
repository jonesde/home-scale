---
id: flux-quantization
title: Flux Quantization (Closed-Loop Fluxoid)
status: formal
family: gapped-coherence
constraints:
  - spatial-buffer
  - energy-barrier
  - thermal
  - field-threshold
confidence_data: high
confidence_mapping: high
related:
  - superconductivity
  - meissner
  - josephson-effect
  - type-ii-critical-field
  - superfluid-helium-4
  - quantum-hall-effect
updated: 2026-08-17
---

# Flux Quantization (Closed-Loop Fluxoid)

### 4.1 Effect Name

Flux quantization (closed-loop fluxoid)

### 4.2 Macroscopic Observation

A closed superconducting ring, cooled through its critical temperature in an applied magnetic field and then left isolated, holds a trapped flux that is an integer multiple of a universal quantum. The trapped value does not decay on laboratory timescales while the ring remains superconducting. Opening the ring, driving a section normal, or warming the loop through \(T_c\) releases the constraint and the integer condition disappears. A SQUID — the same loop interrupted by one or two Josephson junctions — converts that discrete flux into a periodic current or voltage.

### 4.3 Established Quantitative Boundaries

- Flux quantum (measured on superconducting rings; now a defined SI combination):

  \[
  \Phi_0 = \frac{h}{2e} = 2.0678\times 10^{-15}\,\mathrm{Wb}
  \]

- In a thick ring (wall thickness large compared with the London depth \(\lambda\) of the parent condensate) the trapped *flux* itself is \(n\Phi_0\). In a thin-walled cylinder the conserved quantity is the fluxoid (flux plus a line integral of the supercurrent); the Little–Parks oscillation of \(T_c\) with applied flux still has period \(\Phi_0\).
- A SQUID loop is periodic in applied flux with the same \(\Phi_0\). Combined with the AC Josephson lock this is the same constant read in a different geometry; see [josephson-effect](josephson-effect.md).
- The loop must be a closed superconducting path. A break, a normal section, or \(T > T_c\) anywhere on the circumference removes quantization of the trapped flux.
- Phase-slip at a weak spot on an otherwise superconducting loop lets the fluxoid change by \(\Phi_0\). That is a discrete write of the stored integer, not a shift of \(\Phi_0\) itself.

**Data confidence:** High — \(\Phi_0\) is a metrological constant; trapped-flux integers, Little–Parks periodicity, and SQUID periodicity are multiply reproduced. The exact wall-thickness crossover from flux to fluxoid is medium for any one film and high as a class.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Single-valuedness of the condensate phase around a closed path forces the fluxoid to an integer:

  \[
  \Phi' = \oint_{\partial S}\!\left(\mathbf{A} + \frac{m}{q}\mathbf{v}_s\right)\cdot d\mathbf{l} = n\Phi_0, \qquad n \in \mathbb{Z}
  \]

  with \(q = 2e\) the measured charge increment and \(\Phi = \int_S \mathbf{B}\cdot d\mathbf{A}\).

- Thick-wall limit (\(\mathbf{v}_s \to 0\) in the interior of the metal, the same screening that [meissner](meissner.md) records as \(\lambda\)):

  \[
  \Phi = n\Phi_0
  \]

- Little–Parks: the transition temperature of a thin-walled cylinder is periodic in the applied flux with period \(\Phi_0\). That is the fluxoid constraint read as a \(T_c(H)\) oscillation rather than as a trapped integer.
- Each vortex in the mixed state of a type-II superconductor carries one \(\Phi_0\); see [type-ii-critical-field](type-ii-critical-field.md). That is the same quantum threaded through a phase defect rather than through a fabricated hole.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A closed superconducting path. The loop circumference must be a condensate — the hardware of [superconductivity](superconductivity.md). For the *trapped flux* (not merely the fluxoid) to sit at \(n\Phi_0\), the wall must be thick enough that screening currents live in a surface layer of depth \(\lambda\) and the interior supercurrent vanishes. A thinner wall still enforces the fluxoid integer; it does not pin the magnetic flux itself to \(n\Phi_0\). The hole (or vortex core) is the region the condensate does not fill; the load-bearing buffer is the surrounding closed path.

- **Clock rate / latency.** There is no voltage–frequency lock on a fully superconducting loop at rest (\(V = 0\) around the path). The relevant latency is the screening response of the parent condensate (London / plasma scales on [meissner](meissner.md)). A SQUID reads the same integer against the Josephson clock of the interrupting junctions.

- **Energy barriers or thresholds.** Changing the stored integer by one requires a phase slip: a local collapse of the gap on the loop, or a vortex crossing the wall. That barrier is what keeps \(n\) fixed on laboratory timescales. The barrier vanishes if any section of the loop is driven normal, or if \(T \to T_c\).

- **Dominant failure modes.**
  - Topology: loop not closed (a break, a lead, a normal gap) \(\to\) fluxoid not conserved \(\to\) no trapped integer.
  - Thermal: \(T > T_c\) \(\to\) parent condensate gone.
  - Phase-slip / current: a weak spot or a current near the loop \(I_c\) lets \(n\) step. The quantum is unchanged; the stored state is rewritten.
  - Field, electrode-scale: \(H > H_c\) or \(H_{c2}\) destroys the path itself.

- **Emergent constant or stable output.** A trapped fluxoid equal to \(n\Phi_0\), with \(\Phi_0 = h/2e = 2.0678\times 10^{-15}\,\mathrm{Wb}\), held at zero continuous power for as long as the loop, the gap, and the phase-slip barrier remain inside the envelope above.

### 4.6 Internal Consistency Notes

The mapping closes on the hardware condition (a closed superconducting path) and on a single constant \(\Phi_0\) shared with [josephson-effect](josephson-effect.md). Thick-wall flux quantization and thin-wall Little–Parks are the same constraint read in two spatial-buffer regimes, analogous to electromagnetic penetration versus morphological continuity on [reflection](reflection.md): same failure class, different experimental route.

The \(2e\) in \(h/2e\) is again taken from the measured quantum, not derived from node rules. That is the same open increment as on the Josephson entry. No pairing story is added to close it.

A remaining spatial clause: \(\lambda\) and the coherence length \(\xi\) that set how small a hole or vortex core can be are owned by [meissner](meissner.md) and [type-ii-critical-field](type-ii-critical-field.md). This entry takes those lengths as the wall / core buffers; it does not re-derive them.

The chargeless analog is quantized circulation \(h/m_4\) in [superfluid-helium-4](superfluid-helium-4.md). Cross-check is the existence of an integer winding with a measured quantum, not identity of the two constants.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(\Phi_0\), the closed-loop requirement, and the thick-wall / thin-wall / phase-slip collapses are well measured and translate directly into buffer, barrier, and failure-envelope specifications; the open item is the origin of the \(2e\) increment, not the integer condition.

## Related entries

- [superconductivity](superconductivity.md) — the path must be a zero-resistance condensate
- [meissner](meissner.md) — \(\lambda\) is the wall-thickness buffer that converts fluxoid integers into trapped-flux integers
- [josephson-effect](josephson-effect.md) — same \(\Phi_0\), read as a voltage–frequency lock and as SQUID periodicity
- [type-ii-critical-field](type-ii-critical-field.md) — one \(\Phi_0\) per vortex; the mixed-state lattice of phase defects
- [superfluid-helium-4](superfluid-helium-4.md) — chargeless circulation quantum on a closed path
- [quantum-hall-effect](quantum-hall-effect.md) — another macroscopic integer built from \(h\) and \(e\), in a 2DEG rather than a superconducting loop
