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
review_depth: light
related:
  - superconductivity
  - meissner
  - josephson-effect
  - type-ii-critical-field
  - superfluid-helium-4
  - quantum-hall-effect
updated: 2026-11-11
---

# Flux Quantization (Closed-Loop Fluxoid)

### 4.1 Effect Name

Flux quantization (closed-loop fluxoid)

### 4.2 Macroscopic Observation

A closed superconducting ring cooled through its critical temperature in a magnetic field, then left isolated, holds a trapped flux that is an integer multiple of one quantum. The value does not decay on laboratory timescales while the ring stays superconducting. Opening the ring, driving a section normal, or warming through \(T_c\) releases the constraint. A SQUID, the same loop interrupted by Josephson junctions, converts the discrete flux into a periodic current or voltage.

### 4.3 Established Quantitative Boundaries

- **Convention.** \(\Phi_0 = h/2e = 2.067\,833\,848\ldots\times10^{-15}\) Wb, exact since the 2019 SI [S1].
- **Measured.** The flux through a superconducting ring is quantized, with \(\Phi_0 = h/2e\) as the smallest unit [S2]. First observed in 1961 on hollow cylinders [S4]; those letters were not opened.
- **Measured.** Each flux tube in the mixed state of a type-II superconductor carries one \(\Phi_0\) [S2].
- **Measured.** The transition temperature of a thin-walled cylinder is periodic in the applied flux [S5]. The letter was not opened; the period \(\Phi_0\) is quoted here with no opened source.
- **Model (Ginzburg–Landau phase slip).** The stored integer changes when the order parameter is driven to zero at one point of the path and the phase jumps by \(2\pi n\); each event produces a voltage pulse through \(V = \hbar\dot\varphi/2e\) [S3].
- **Measured.** Narrow paths. Wires with cross-sections from about 100 nm down to below 10 nm, far thinner than the bulk coherence length of aluminium (1.6 µm), still superconduct. Below about 50 nm quantum phase slips give a resistance at low temperature, and near 10 nm the wire crosses over to normal behaviour [S3].
- **Model (quantum phase slips in rings).** In nanorings, quantum phase slips modify the persistent current and suppress it exponentially for a sufficiently large ring perimeter [S3].
- **Computed here.** One flux quantum through a ring of 10 µm diameter corresponds to a field of 26 µT.
- **Convention.** Holding the trapped integer costs zero continuous power.

**Data confidence:** High for \(\Phi_0\) and for integer trapped flux. The 1961 and 1962 letters were not opened; the quantization statement rests on a lecture text and the Little–Parks period on no opened source. Phase-slip numbers are from one review.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Single-valuedness of the condensate phase around a closed path fixes the fluxoid:

  \[
  \Phi' = \oint\!\left(\mathbf{A} + \frac{m}{q}\mathbf{v}_s\right)\cdot d\mathbf{l} = n\Phi_0, \qquad n \in \mathbb{Z}
  \]

  with \(q = 2e\) the measured charge increment.
- Thick wall (path deep inside the metal, where the supercurrent vanishes; the screening of [meissner](meissner.md)): \(\Phi = n\Phi_0\). A wall thinner than the penetration depth still fixes the fluxoid, and the flux itself then differs from \(n\Phi_0\) by the supercurrent term.
- Phase slip: \(\Delta\varphi = 2\pi n\) at a point where \(|\Psi| \to 0\) [S3].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A closed superconducting path. For the trapped flux to equal \(n\Phi_0\) the wall must be several penetration depths thick; a thinner wall holds the fluxoid integer. The path need not be wider than the coherence length: wires far thinner than \(\xi_0\) superconduct, and the integer becomes unstable through a rising phase-slip rate near 10 nm cross-section.

- **Clock rate / latency.** No voltage–frequency lock on a loop at rest (\(V = 0\)). A SQUID reads the integer against the Josephson clock of its junctions.

- **Energy barriers or thresholds.** Changing \(n\) by one needs a phase slip, a local suppression of the order parameter on the loop. That barrier keeps \(n\) fixed. It falls as the cross-section shrinks and as \(T \to T_c\).

- **Dominant failure modes.**
  - **Threshold** — topology: a break or a normal section; the fluxoid is not conserved.
  - **Threshold** — thermal: \(T > T_c\).
  - **Crossover** — phase slips: the rate of \(2\pi\) slips rises as the cross-section falls (measurable below about 50 nm, dominant near 10 nm) and as \(T \to T_c\). Each slip rewrites \(n\); \(\Phi_0\) is unchanged.
  - **Threshold** — field: \(H > H_c\) or \(H_{c2}\) destroys the path.

- **Emergent constant or stable output.** A trapped fluxoid \(n\Phi_0\) held at zero continuous power while the loop, the gap and the phase-slip barrier remain.

### 4.6 Internal Consistency Notes

The mapping closes on a closed superconducting path and one constant shared with [josephson-effect](josephson-effect.md).

Sourcing changed one thing: the path has no minimum width of order the coherence length. Stability of the integer against cross-section is a crossover in phase-slip rate, measured in wires at 10–50 nm. No numbers changed; \(\Phi_0\) is now quoted to the CODATA digits.

The \(2e\) in \(h/2e\) is taken from the measured quantum, not derived. No pairing story is added.

The chargeless analogue is quantized circulation \(h/m_4\) in [superfluid-helium-4](superfluid-helium-4.md).

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(\Phi_0\), the closed-loop requirement and the phase-slip route translate directly into buffer, barrier and failure specifications; the open item is the origin of the \(2e\) increment.

## Related entries

- [superconductivity](superconductivity.md) — the path must be superconducting
- [meissner](meissner.md) — \(\lambda\) is the wall depth that turns fluxoid integers into flux integers
- [josephson-effect](josephson-effect.md) — same \(\Phi_0\), read as a voltage–frequency lock
- [type-ii-critical-field](type-ii-critical-field.md) — one \(\Phi_0\) per vortex
- [superfluid-helium-4](superfluid-helium-4.md) — chargeless circulation quantum
- [quantum-hall-effect](quantum-hall-effect.md) — another integer built from \(h\) and \(e\)

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [CODATA 2022, magnetic flux quantum (NIST)](https://physics.nist.gov/cgi-bin/cuu/Value?flxquhs2e) | full-text | Flux quantum, exact. |
| S2 | [Schmüser, Proc. 11th Workshop on RF Superconductivity (2003), paper MOT01](https://jacow.org/SRF2003/papers/MOT01.pdf) | full-text | Secondary (lecture). Flux through a ring is quantized in units of h/2e; one quantum per flux tube. |
| S3 | [Arutyunov, Golubev and Zaikin, "Superconductivity in one dimension", arXiv:0805.2118 (2008)](https://arxiv.org/abs/0805.2118) | full-text | Phase slips of 2π and their voltage; wires from 100 nm to below 10 nm; quantum phase slips below about 50 nm and crossover near 10 nm; persistent currents in nanorings; Al coherence length. |
| S4 | [Deaver and Fairbank, *Phys. Rev. Lett.* 7, 43 (1961)](https://doi.org/10.1103/PhysRevLett.7.43) | cited-only | First observation of quantized trapped flux; the companion letter is Doll and Näbauer, *Phys. Rev. Lett.* 7, 51 (1961). |
| S5 | [Little and Parks, *Phys. Rev. Lett.* 9, 9 (1962)](https://doi.org/10.1103/PhysRevLett.9.9) | cited-only | Periodic transition temperature of a thin-walled cylinder in applied flux. Landing page opened; it carries no abstract. |
