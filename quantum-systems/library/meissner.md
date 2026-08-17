---
id: meissner
title: Meissner Effect (Field Expulsion)
status: formal
family: gapped-coherence
constraints:
  - spatial-buffer
  - field-threshold
  - thermal
confidence_data: high
confidence_mapping: high
related:
  - superconductivity
  - type-ii-critical-field
  - flux-quantization
  - josephson-effect
updated: 2026-08-17
---

# Meissner Effect (Field Expulsion)

### 4.1 Effect Name

Meissner effect (field expulsion)

### 4.2 Macroscopic Observation

A superconducting body cooled through \(T_c\) in a static magnetic field expels that field from its interior. In the fully expelled state the volume susceptibility is \(\chi = -1\) (SI) and the interior induction is \(B = 0\). A levitating magnet above a cooled superconductor is the everyday form of the same observation. Expulsion is not the same fact as zero resistance: a hypothetical perfect conductor would trap the flux it already contained, not expel it. Raising the field through a critical value, or warming through \(T_c\), ends the expulsion.

### 4.3 Established Quantitative Boundaries

- Complete expulsion (\(\chi = -1\), \(B=0\) in the bulk) holds for type-I superconductors at \(H < H_c\), aside from a surface layer of depth \(\lambda\) and aside from the intermediate state of a finite body with a nonzero demagnetizing factor. Type-I \(H_c(0)\): Al \(\mu_0 H_c \approx 10.5\,\mathrm{mT}\); Pb \(\approx 80\,\mathrm{mT}\); Sn \(\approx 30\,\mathrm{mT}\).
- Type II: complete expulsion only for \(H < H_{c1}\). Between \(H_{c1}\) and \(H_{c2}\) flux enters as quantized vortices (mixed state) while zero resistance can still hold if those vortices are pinned — the split recorded on [superconductivity](superconductivity.md). Above \(H_{c2}\) the condensate is gone. \(\Phi_0 = h/2e \approx 2.07\times 10^{-15}\,\mathrm{Wb}\) is the flux per vortex.
- London penetration depth \(\lambda(T)\) is the measured spatial buffer: \(B\) decays as \(e^{-x/\lambda}\) into a flat surface. Conventional elemental values of \(\lambda(0)\) sit in the \(40\)–\(50\,\mathrm{nm}\) class (Nb and Pb near \(40\,\mathrm{nm}\); Al often quoted near \(50\,\mathrm{nm}\)). YBCO \(\lambda_{ab}(0)\) sits in the \(100\)–\(160\,\mathrm{nm}\) class; \(\lambda_c\) is larger. \(\lambda(T)\) grows as \(T\to T_c^-\) and the expulsion layer thickens.
- Coherence length \(\xi\) is the second spatial scale. Type I vs type II is the measured ratio \(\kappa = \lambda/\xi\) against \(1/\sqrt{2}\). Al is deep type I (\(\xi_0 \sim 1.6\,\mu\mathrm{m}\)); Nb is near the boundary (\(\xi_0 \sim 40\,\mathrm{nm}\)); YBCO is extreme type II (\(\xi_{ab} \sim 1.5\)–\(2\,\mathrm{nm}\)).
- Thin films with thickness \(d \ll \lambda\) do not fully expel; the effective screening is incomplete. That is a buffer-starvation form of the same effect, not a different \(T_c\).

**Data confidence:** High — \(\chi = -1\), type-I \(H_c\), the \(H_{c1}/H_{c2}\) fork, and \(\lambda(0)\) as a class are handbook measurements. The precise \(\lambda(0)\) of any one film is medium (mean free path, surface quality, anisotropy).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- London screening (half-space, static field):

  \[
  B(x) = B(0)\,e^{-x/\lambda}, \qquad
  \lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}}
  \]

  The observed \(\lambda\) includes nonlocal and mean-free-path corrections; \(\lambda_L\) is the clean local limit.

- Perfect diamagnetism of the fully expelled volume:

  \[
  \mathbf{B} = 0 \quad (x \gg \lambda), \qquad \chi = -1 \quad (\mathrm{SI})
  \]

- Type-I thermodynamic critical field ends expulsion and superconductivity together. Type-II fields:

  \[
  \mu_0 H_{c2} = \frac{\Phi_0}{2\pi\xi^2}, \qquad
  \mu_0 H_{c1} \sim \frac{\Phi_0}{4\pi\lambda^2}\ln\kappa
  \]

  with \(\kappa = \lambda/\xi\) and \(\Phi_0 = h/2e\). The \(H_{c1}\) prefactor is a standard descriptive form, not used here as a derived node rule.

- Temperature: \(\lambda(T)\) and \(\xi(T)\) diverge as \(T\to T_c^-\); \(H_c\), \(H_{c1}\), and \(H_{c2}\) fall to zero there.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two nested spatial specifications:
  1. **Screening buffer.** A superconducting layer at least of order \(\lambda\) thick — tens of nanometres in conventional elements, of order \(100\,\mathrm{nm}\) in YBCO’s ab plane — before the interior field is fully expelled. Thinner films under-provision this buffer and expulsion is incomplete.
  2. **Condensate coherence.** The parent coherent state of [superconductivity](superconductivity.md), with its own length \(\xi\). Type I vs type II is which of \(\lambda\) and \(\xi\) is larger. This entry owns \(\lambda\); [type-ii-critical-field](type-ii-critical-field.md) owns the vortex lattice that appears once \(\lambda > \xi/\sqrt{2}\) and \(H > H_{c1}\).

- **Clock rate / latency.** Expulsion on cooling through \(T_c\) is limited by thermal diffusion, eddy-current transients, and (in type II) flux-line motion — laboratory times, not the gap frequency \(2\Delta/h\). The gap frequency still sets the scale on which the condensate can respond to a *changing* field; this entry’s static observation is the \(\omega = 0\) expelled state.

- **Energy barriers or thresholds.** The same gap that protects zero resistance protects the expelled state against thermal quasiparticles. The field thresholds \(H_c\) (type I) and \(H_{c1}\) (type II) are the load-bearing gates for *complete* expulsion. Holding the expelled state costs no continuous power.

- **Dominant failure modes.**
  - Field, type I: \(H > H_c\) → field floods, superconductivity itself collapses.
  - Field, type II: \(H > H_{c1}\) → complete expulsion fails (vortices enter) while \(R=0\) can persist. \(H > H_{c2}\) → condensate gone.
  - Thermal: \(T > T_c\) → \(\lambda\) diverges, gap closes, expulsion ends.
  - Spatial: \(d \ll \lambda\) → incomplete screening at any \(H < H_{c1}\).
  - Geometry (type I): a finite demagnetizing factor produces an intermediate state of mixed normal and superconducting domains below the nominal \(H_c\). That is a shape-dependent partition, not a second condensate.

- **Emergent constant or stable output.** A field-free interior behind a surface layer of depth \(\lambda\), with \(\chi = -1\) for the expelled volume, for as long as \(T\) and \(H\) remain inside the envelope above.

### 4.6 Internal Consistency Notes

\(\lambda\) as a spatial buffer is the same kind of specification as the optical penetration depth on [reflection](reflection.md): a measured screening length of a collective charged population, taken as the hardware depth rather than derived from a more primitive node count. \(\chi = -1\) is the stable output of that fully provisioned buffer. The field thresholds sit where a gapped-coherence family says they should.

The split from zero resistance is internally required. A type-II mixed state has \(B \neq 0\) in the bulk and can still carry a lossless current. Filing both facts under one artifact would hide a real difference in failure envelopes.

A remaining gap, shared with the parent entry: QSA does not derive *why* the equilibrium is expulsion rather than flux trapping from node rules alone. The data distinguish the two (cool in a field → \(B=0\), rather than freeze-in). The mapping records that equilibrium as the stable output of the gapped state; it does not yet produce it from a more primitive update rule. That is a gap, not a contradiction.

\(\xi\) and the vortex lattice are second and third spatial scales. They are flagged here and owned by [type-ii-critical-field](type-ii-critical-field.md) and [flux-quantization](flux-quantization.md), so this file is not forced to treat \(\lambda\) as the only length.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(\lambda\), \(\chi = -1\), and the \(H_c / H_{c1}\) gates are well-measured buffer and field-threshold specifications; remaining gaps are about deriving expulsion from node rules and about the type-II lengths filed next door, not about the existence of the expelled state.

## Related entries

- [Superconductivity (zero-resistance transport)](superconductivity.md) — \(R\to 0\); different artifact, same condensate
- [Type-II critical field](type-ii-critical-field.md) — mixed state as a lattice of phase defects; \(H_{c1}\) and \(H_{c2}\)
- [Flux quantization](flux-quantization.md) — \(\Phi_0 = h/2e\) in a closed loop or in one vortex
- [Josephson effect](josephson-effect.md) — weak-link current; a different use of the same phase coherence
