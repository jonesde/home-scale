---
id: type-ii-critical-field
title: Type-II Critical Field (Mixed-State Vortex Lattice)
status: formal
family: gapped-coherence
constraints:
  - field-threshold
  - spatial-buffer
  - thermal
  - energy-barrier
confidence_data: high
confidence_mapping: high
related:
  - superconductivity
  - meissner
  - flux-quantization
  - josephson-effect
  - magnetic-domains
  - ferroelectric-domains
  - superfluid-helium-4
updated: 2026-08-20
---

# Type-II Critical Field (Mixed-State Vortex Lattice)

### 4.1 Effect Name

Type-II critical field (mixed-state vortex lattice)

### 4.2 Macroscopic Observation

A type-II superconductor (commercial NbTi, \(\mathrm{Nb_3Sn}\), YBCO and related cuprates) continues to show a superconducting response in applied fields far above the thermodynamic critical field of a type-I element such as lead or tin. Below a lower critical field \(H_{c1}\) the sample still expels flux. Between \(H_{c1}\) and an upper field \(H_{c2}\) flux enters as a lattice of discrete tubes, each carrying one flux quantum. Above \(H_{c2}\) the mixed state is gone and the sample is normal. If the tubes can move, transport becomes dissipative even though the gap has not yet closed.

### 4.3 Established Quantitative Boundaries

- Classification boundary (Ginzburg–Landau parameter):

  \[
  \kappa = \frac{\lambda}{\xi}, \qquad \text{type II when }\kappa > \frac{1}{\sqrt{2}}
  \]

  \(\lambda\) is the London screening depth; \(\xi\) is the coherence length. Type-I elements sit below this line and have a single thermodynamic \(H_c\), typically tens of millitesla (lead is the high end of that class, \(\mu_0 H_c \sim 80\,\mathrm{mT}\)).

- Two field thresholds in type II, both temperature-dependent and both collapsing to zero at \(T_c\):
  - \(H_{c1}\): first flux entry. Below \(H_{c1}\) the Meissner expulsion of [meissner](meissner.md) still holds.
  - \(H_{c2}\): gap destroyed; mixed state gone.
- Technical conductor classes, as classes not as single-sample certificates: NbTi and \(\mathrm{Nb_3Sn}\) remain superconducting in tesla-scale fields at liquid-helium temperature; YBCO does so at liquid-nitrogen temperature, with a strongly anisotropic \(H_{c2}\).
- Each vortex carries \(\Phi_0 = h/2e = 2.0678\times 10^{-15}\,\mathrm{Wb}\). The areal density of vortices is \(B / \Phi_0\); the lattice spacing is of order \(\sqrt{\Phi_0 / B}\) (tens of nanometres at tesla-scale induction).
- A moving vortex lattice produces a dissipative electric field. Zero-resistance transport in the mixed state therefore requires pinning. That is a different collapse from \(H_{c2}\) and is owned jointly with [superconductivity](superconductivity.md).

**Data confidence:** High — the \(\kappa\) line, the existence of \(H_{c1}\) and \(H_{c2}\), \(\Phi_0\) per vortex, and the vortex lattice (decoration, neutron diffraction, STM) are standard. Material-specific \(H_{c2}(T)\) curves are high as a class and medium for any one commercial wire.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Upper critical field set by the coherence-length buffer:

  \[
  \mu_0 H_{c2} = \frac{\Phi_0}{2\pi\xi^2}
  \]

- Lower critical field, large-\(\kappa\) form:

  \[
  \mu_0 H_{c1} \approx \frac{\Phi_0}{4\pi\lambda^2}\ln\kappa
  \]

- Vortex density and characteristic spacing:

  \[
  n_v = \frac{B}{\Phi_0}, \qquad a \sim \sqrt{\frac{\Phi_0}{B}}
  \]

- Flux-flow bookkeeping when the lattice is free to move: \(\mathbf{E} = \mathbf{B}\times\mathbf{v}_L\). Pinning introduces a barrier against \(\mathbf{v}_L \neq 0\). Those relations describe the extra dissipative channel; they are not a mechanism claim for the gap.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Three nested spatial scales, all required before this artifact exists as something other than a type-I Meissner state. (1) Coherence length \(\xi\): the core size of a phase defect and the length that closes at \(H_{c2}\). (2) Penetration depth \(\lambda\): the screening cloud around each core, the same \(\lambda\) as on [meissner](meissner.md). Type II is the regime \(\lambda > \xi / \sqrt{2}\). (3) Vortex lattice spacing \(\sim\sqrt{\Phi_0 / B}\): an extra, field-tuned buffer that has no type-I counterpart. The mixed state is a synchronized array of these defects, not a uniform condensate.

- **Clock rate / latency.** Screening and core adjustment follow the parent-condensate electromagnetic / gap clocks (London / plasma scales; gap frequency). Flux-flow voltages, when present, sit on a much slower, geometry- and drive-dependent scale set by vortex velocity. This entry is not a voltage-standard clock; that lock lives on [josephson-effect](josephson-effect.md).

- **Energy barriers or thresholds.** \(H_{c1}\) is the field threshold for first entry of a \(\Phi_0\) defect. \(H_{c2}\) is the field threshold that closes the gap. Pinning sites supply an additional barrier against vortex motion; that barrier protects the *zero-resistance* reading in the mixed state and is not the same threshold as \(H_{c2}\).

- **Dominant failure modes.**
  - Field, lower: \(H\) crosses \(H_{c1}\) \(\to\) first penetration \(\to\) Meissner expulsion fails, mixed state begins. This is a collapse of [meissner](meissner.md), not of the gap.
  - Field, upper: \(H > H_{c2}\) \(\to\) \(\xi\)-buffer destroyed \(\to\) gap gone \(\to\) normal metal.
  - Thermal: \(T \to T_c\) sends both \(H_{c1}\) and \(H_{c2}\) to zero.
  - Pinning: free vortex motion \(\to\) flux-flow voltage \(\to\) the \(R = 0\) artifact fails while the gap and the lattice are still present.

- **Emergent constant or stable output.** A mixed state whose field scale is set by \(\xi\) and \(\lambda\), whose flux is packaged as an integer number of \(\Phi_0\) tubes, and whose lattice spacing tracks \(\sqrt{\Phi_0 / B}\), for as long as \(H_{c1} < H < H_{c2}\) and \(T < T_c\).

### 4.6 Internal Consistency Notes

The split among three files is load-bearing and internally consistent. [superconductivity](superconductivity.md) owns \(R = 0\). [meissner](meissner.md) owns expulsion below \(H_{c1}\). This file owns the mixed-state window and the extra spatial scale. Collapse at \(H_{c1}\) is not collapse at \(H_{c2}\); treating them as one “critical field” would hide the vortex-lattice buffer.

\(\Phi_0\) per vortex is the same quantum as on [flux-quantization](flux-quantization.md). A vortex is a phase defect that plays the role of the hole; the surrounding condensate is the closed path. That is a consistency check.

A remaining gap, of the same kind as mesoscale coercivity on [permanent-magnet-latch](permanent-magnet-latch.md): pinning — the barrier that decides whether the mixed state is dissipationless — is set by microstructure (precipitates, grain boundaries, irradiation defects) and is not a universal function of \(\lambda\) and \(\xi\). QSA does not yet have a clean buffer / barrier specification for that mesoscale step. The \(H_{c1}\) / \(H_{c2}\) / \(\kappa\) collapses do not depend on closing it.

No pairing mechanism is used or required. \(\xi\) and the gap are taken as measured lengths / energy scales of the parent condensate.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(\kappa\), \(H_{c1}\), \(H_{c2}\), and the \(\Phi_0\) lattice are sharp measured boundaries and translate directly into field thresholds and nested spatial buffers; the open item is the pinning landscape, not the mixed-state classification.

## Related entries

- [superconductivity](superconductivity.md) — \(R = 0\); in type II that reading further requires pinning
- [meissner](meissner.md) — expulsion below \(H_{c1}\); \(\lambda\) is shared
- [flux-quantization](flux-quantization.md) — one \(\Phi_0\) per vortex; the hole is now a core
- [josephson-effect](josephson-effect.md) — same \(\Phi_0\); junction-scale field response is Fraunhofer modulation, not \(H_{c2}\)
- [magnetic-domains](magnetic-domains.md) — another macroscopic partition into real-space cells; different family, useful contrast
- [ferroelectric-domains](ferroelectric-domains.md) — polar partition, same contrast: topology is not a seventh family
- [superfluid-helium-4](superfluid-helium-4.md) — chargeless vortices; circulation quantum rather than \(\Phi_0\)
