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
review_depth: light
related:
  - superconductivity
  - meissner
  - flux-quantization
  - josephson-effect
  - magnetic-domains
  - ferroelectric-domains
  - superfluid-helium-4
updated: 2026-11-11
---

# Type-II Critical Field (Mixed-State Vortex Lattice)

### 4.1 Effect Name

Type-II critical field (mixed-state vortex lattice)

### 4.2 Macroscopic Observation

A type-II superconductor (niobium, NbTi, \(\mathrm{Nb_3Sn}\), the cuprates) stays superconducting in fields far above the critical field of a type-I element such as lead. Below a lower critical field \(H_{c1}\) it expels flux. Between \(H_{c1}\) and an upper field \(H_{c2}\) flux enters as a lattice of tubes, each carrying one flux quantum. Above \(H_{c2}\) the sample is normal. If the tubes move, transport is dissipative although the gap has not closed.

### 4.3 Established Quantitative Boundaries

- **Model (Ginzburg–Landau).** \(\kappa = \lambda/\xi\); type I for \(\kappa < 1/\sqrt{2}\), type II above [S1].
- **Computed here.** \(\kappa\) from tabulated lengths [S2]: Al 0.010, Sn 0.22, Pb 0.44, Nb 2.8. A second table [S1] gives Nb 32 nm and 39 nm, \(\kappa = 0.82\). Both place niobium on the type-II side; the source describes it as close to the border [S1].
- **Measured.** Type I critical fields are usually below 0.1 T (Pb 80 mT) [S1]. Niobium at 2 K: \(B_{c1} \approx 160\) mT, \(B_c \approx 190\) mT, \(B_{c2} \approx 300\) mT [S1]. NbTi: \(B_{c2} = 14\) T; many alloys remain superconducting to 10 T or more [S1].
- **Model (Ginzburg–Landau and WHH extrapolation).** YBCO films: \(\mu_0 H_{c2}(0) = 153\) T (field along *c*) and 638 T (field in the *ab* plane), an anisotropy of 4.2 [S3].
- **Measured.** The flux tubes form a triangular lattice, imaged by decorating a niobium surface with iron particles; each carries one \(\Phi_0\) and has a normal core of area about \(\pi\xi^2\) [S1]. \(\Phi_0 = 2.067\,833\,848\ldots\times10^{-15}\) Wb [S4].
- **Computed here.** Triangular-lattice spacing \(d = \sqrt{2\Phi_0/(\sqrt{3}B)}\): 49 nm at 1 T and 20 nm at 6 T (the source quotes 20 nm at 6 T [S1]). Areal density \(B/\Phi_0 = 4.8\times10^{14}\) m⁻² at 1 T.
- **Computed here.** \(\xi\) from \(B_{c2} = \Phi_0/2\pi\xi^2\): 14 T gives 4.8 nm (source: 5 nm [S1]). The same formula with the tabulated Nb \(\xi\) of 30 and 39 nm gives 0.37 and 0.22 T, bracketing the measured 0.30 T.
- **Measured.** A transport current through an unpinned type-II conductor in a field moves the flux tubes and produces a flux-flow resistance. Pinning centres prevent it; in NbTi they are normal titanium precipitates whose size is in the range of the tube spacing. A pinned conductor carries 3700 A mm⁻² at 5 T and 4.2 K, and its magnetization is hysteretic above \(H_{c1}\) [S1].

**Data confidence:** High for the classification, the two fields, one \(\Phi_0\) per tube and the lattice. Tabulated \(\lambda\) and \(\xi\) for niobium differ between the two opened tables. YBCO \(H_{c2}\) is an extrapolation far above any applied field.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Upper critical field [S1]:

  \[
  B_{c2} = \sqrt{2}\,\kappa\,B_c = \frac{\Phi_0}{2\pi\xi^2}
  \]

- Lower critical field, large-\(\kappa\) form (standard; no opened source): \(\mu_0 H_{c1} \approx (\Phi_0/4\pi\lambda^2)\ln\kappa\).
- Vortex density \(n_v = B/\Phi_0\); triangular spacing \(d = \sqrt{2\Phi_0/(\sqrt{3}B)}\) [S1].
- Flux flow: \(\mathbf{E} = \mathbf{B}\times\mathbf{v}_L\) when the lattice moves at \(\mathbf{v}_L\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Three nested lengths. (1) \(\xi\): the core size of a flux tube, and the length that sets \(H_{c2}\). (2) \(\lambda\): the screening cloud around each core, shared with [meissner](meissner.md). (3) The lattice spacing, 49 nm at 1 T, tuned by the field. The mixed state is an ordered array of these defects.

- **Clock rate / latency.** Screening follows the parent-condensate clocks. Flux-flow voltages sit on a slower, drive-dependent scale set by vortex velocity. The voltage-standard lock lives on [josephson-effect](josephson-effect.md).

- **Energy barriers or thresholds.** \(H_{c1}\) is the field for first entry of a flux tube. \(H_{c2}\) closes the gap. Pinning sites add a barrier against vortex motion, which protects zero resistance in the mixed state and is a separate quantity from \(H_{c2}\).

- **Dominant failure modes.**
  - **Threshold** — field, lower: \(H > H_{c1}\); first penetration. This ends [meissner](meissner.md) expulsion, not the gap.
  - **Threshold** — field, upper: \(H > H_{c2}\); cores overlap and the sample is normal.
  - **Threshold** — thermal: \(T \to T_c\) sends both fields to zero.
  - **Crossover** — pinning: flux-flow resistance grows with vortex velocity once the driving force exceeds the pinning force. The critical current is set by microstructure; no universal scale.

- **Emergent constant or stable output.** A mixed state with flux packaged in tubes of one \(\Phi_0\) on a triangular lattice of spacing \(\sqrt{2\Phi_0/(\sqrt{3}B)}\), for \(H_{c1} < H < H_{c2}\) and \(T < T_c\).

### 4.6 Internal Consistency Notes

The split among three files is required. [superconductivity](superconductivity.md) owns zero resistance, [meissner](meissner.md) owns expulsion below \(H_{c1}\), and this file owns the mixed-state window. \(\Phi_0\) per tube is the quantum of [flux-quantization](flux-quantization.md).

Sourcing changed little: no numbers were contradicted. The lattice spacing is now computed for the triangular lattice (49 nm at 1 T, where the first version said "tens of nanometres"), niobium's fields and the NbTi upper field are quoted from a source, and the pinning clause has a measured example. The \(\mathrm{Nb_3Sn}\) field was dropped for lack of an opened source.

A remaining gap, of the same kind as mesoscale coercivity on [permanent-magnet-latch](permanent-magnet-latch.md): pinning is set by precipitates, grain boundaries and defects and is not a function of \(\lambda\) and \(\xi\) alone. The one sourced regularity is that the effective pinning centres in NbTi are comparable in size to the tube spacing.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(\kappa\), \(H_{c1}\), \(H_{c2}\) and the \(\Phi_0\) lattice are measured boundaries that translate into field thresholds and nested lengths; the open item is the pinning landscape.

## Related entries

- [superconductivity](superconductivity.md) — zero resistance; in type II it needs pinning
- [meissner](meissner.md) — expulsion below \(H_{c1}\); \(\lambda\) is shared
- [flux-quantization](flux-quantization.md) — one \(\Phi_0\) per vortex
- [josephson-effect](josephson-effect.md) — same \(\Phi_0\); junction-scale field response
- [magnetic-domains](magnetic-domains.md) — another partition into real-space cells; contrast
- [ferroelectric-domains](ferroelectric-domains.md) — polar partition; contrast
- [superfluid-helium-4](superfluid-helium-4.md) — chargeless vortices with circulation quantum

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Schmüser, Proc. 11th Workshop on RF Superconductivity (2003), paper MOT01](https://jacow.org/SRF2003/papers/MOT01.pdf) | full-text | Secondary (lecture). Type I and II criterion; Nb fields at 2 K; NbTi 14 T and 5 nm; triangular lattice, 20 nm at 6 T; decoration image; flux flow, pinning by precipitates sized to the tube spacing, 3700 A/mm², hysteresis. |
| S2 | [Arutyunov, Golubev and Zaikin, "Superconductivity in one dimension", arXiv:0805.2118 (2008)](https://arxiv.org/abs/0805.2118) | full-text | Table I: penetration depth and coherence length of Al, Sn, Pb, Nb. |
| S3 | [Petrenko et al., *Low Temp. Phys.* 48, 856 (2022), arXiv:2209.14668](https://arxiv.org/abs/2209.14668) | full-text | YBCO films: extrapolated upper critical fields 153 T and 638 T. |
| S4 | [CODATA 2022, magnetic flux quantum (NIST)](https://physics.nist.gov/cgi-bin/cuu/Value?flxquhs2e) | full-text | Flux quantum, exact. |
