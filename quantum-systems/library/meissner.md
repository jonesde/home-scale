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
review_depth: light
related:
  - superconductivity
  - type-ii-critical-field
  - flux-quantization
  - josephson-effect
updated: 2026-11-11
---

# Meissner Effect (Field Expulsion)

### 4.1 Effect Name

Meissner effect (field expulsion)

### 4.2 Macroscopic Observation

A superconducting body cooled through \(T_c\) in a weak static magnetic field expels that field from its interior. In the fully expelled state the interior induction is zero and the volume susceptibility is \(\chi = -1\) (SI). A perfect conductor would instead keep the flux it already contained, so expulsion is a separate fact from zero resistance. Raising the field through a critical value, or warming through \(T_c\), ends the expulsion.

### 4.3 Established Quantitative Boundaries

- **Measured.** Meissner and Ochsenfeld (1933): lead expels a weak field from its interior on cooling below \(T_c\) [S1].
- **Measured.** Type I (Pb, Hg, Sn, Al): no field in the bulk below a critical field that is usually under 0.1 T [S1]; Al 10 mT, Sn 30.5 mT, Pb 80.3 mT at \(T \to 0\) [S2].
- **Measured.** Type II (Nb, alloys): complete expulsion below \(H_{c1}\); between \(H_{c1}\) and \(H_{c2}\) the field enters as flux tubes, each carrying one flux quantum [S1]. Niobium at 2 K: \(B_{c1} \approx 160\) mT, \(B_{c2} \approx 300\) mT [S1]. \(\Phi_0 = 2.067\,833\,848\ldots\times10^{-15}\) Wb [S4].
- **Model (London; tabulated values).** Penetration depth: the field falls as \(e^{-x/\lambda}\) into a flat surface, with \(\lambda\) typically 20–50 nm [S1]. Tabulated \(\lambda\): Al 16 nm, Sn 50 nm, Pb 40 nm, Nb 85 nm [S2]; a second table gives Pb 32 nm, Sn about 30 nm, Nb 32 nm [S1]. The two tables differ by a factor of 2.7 for niobium.
- **Measured.** YBCO near optimal doping, \(T \to 0\): \(\lambda_a = 103 \pm 8\) nm, \(\lambda_b = 80 \pm 5\) nm, \(\lambda_c = 635 \pm 50\) nm [S3].
- **Model (tabulated).** Coherence length \(\xi_0\): Al 1.6 µm, Sn 0.23 µm, Pb 0.090 µm, Nb 0.030 µm [S2]; YBCO \(\xi_{ab} = 1.41\) nm [S3].
- **Computed here.** \(\kappa = \lambda/\xi\) from [S2]: Al 0.010, Sn 0.22, Pb 0.44, Nb 2.8; from the second table [S1] Nb 0.82. YBCO, with \(\lambda_{ab} \approx 90\) nm and \(\xi_{ab} = 1.41\) nm: about 64. The type-II condition is \(\kappa > 1/\sqrt{2} = 0.707\) [S1].
- **Measured.** Thin sheets: in a sheet thinner than \(\lambda\) the field does not fall to zero at the centre, and the critical field of the sheet can be much larger than that of a thick slab [S1]. The sheet remains superconducting. Lead and indium films one atomic layer thick on silicon are superconducting [S5].
- **Computed here.** London slab of thickness \(d\) in a parallel field: the field at mid-plane is \(B_0/\cosh(d/2\lambda)\). That is 0.89 \(B_0\) at \(d = \lambda\), 0.43 \(B_0\) at \(d = 3\lambda\) and 0.013 \(B_0\) at \(d = 10\lambda\).
- **Convention.** Holding the expelled state costs zero continuous power.

**Data confidence:** High for expulsion, the type-I fields and the \(H_{c1}/H_{c2}\) fork. Tabulated \(\lambda\) for one element differs between the two opened tables by up to a factor of 2.7. YBCO values are from a tertiary page; the monolayer result rests on a `snippet`.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- London screening of a half-space [S1]:

  \[
  B(x) = B_0\,e^{-x/\lambda_L}, \qquad
  \lambda_L = \sqrt{\frac{m_e}{\mu_0 n_s e^2}}
  \]

  A slab of thickness \(d\) with the field on both faces has \(B(x) = B_0\cosh(x/\lambda)/\cosh(d/2\lambda)\), measured from the mid-plane.
- Fully expelled volume: \(\mathbf{B} = 0\) for \(x \gg \lambda\); \(\chi = -1\).
- Type I against type II: \(\kappa = \lambda/\xi\) below or above \(1/\sqrt{2}\) [S1].
- \(\mu_0 H_{c2} = \Phi_0/(2\pi\xi^2)\) [S1]; \(\mu_0 H_{c1} \sim (\Phi_0/4\pi\lambda^2)\ln\kappa\) (standard large-\(\kappa\) form; no opened source).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two lengths:
  1. **Screening depth.** \(\lambda\), 16–85 nm in the elements and 80–100 nm in the YBCO *ab* plane, is the e-folding length of the field inside the surface. A body several \(\lambda\) thick has a field-free interior. A thinner body screens partially, by \(1/\cosh(d/2\lambda)\), and still superconducts.
  2. **Condensate coherence.** The parent state of [superconductivity](superconductivity.md), with length \(\xi\). The ratio \(\lambda/\xi\) decides type I or type II. [type-ii-critical-field](type-ii-critical-field.md) owns the vortex lattice.

- **Clock rate / latency.** Expulsion on cooling is limited by thermal diffusion, eddy currents and flux motion: laboratory times. The static observation is the \(\omega = 0\) expelled state.

- **Energy barriers or thresholds.** \(H_c\) (type I) and \(H_{c1}\) (type II) gate complete expulsion. Holding the expelled state costs no continuous power.

- **Dominant failure modes.**
  - **Threshold** — field, type I: \(H > H_c\); the field enters and superconductivity ends together.
  - **Threshold** — field, type II: \(H > H_{c1}\); first flux entry. Zero resistance can persist to \(H_{c2}\).
  - **Threshold** — thermal: \(T > T_c\).
  - **Crossover** — thickness: mid-plane field \(B_0/\cosh(d/2\lambda)\); 89 % of the applied field at \(d = \lambda\), 1.3 % at \(d = 10\lambda\). No thickness at which expulsion switches off.
  - **Crossover** — geometry (type I): a body with a demagnetizing factor passes through an intermediate state of normal and superconducting regions below the nominal \(H_c\). No measured scale filed.

- **Emergent constant or stable output.** A field-free interior behind a surface layer of depth \(\lambda\), with \(\chi = -1\) for the expelled volume, inside the envelope above.

### 4.6 Internal Consistency Notes

\(\lambda\) is the same kind of quantity as the optical decay length on [reflection](reflection.md): the e-folding length of a field in a collective charged population. In both cases the response of a body thinner than that length is reduced, with no minimum thickness.

Sourcing changed two things. The thin-film clause is a crossover with the form \(1/\cosh(d/2\lambda)\), and a film thinner than \(\lambda\) keeps its superconductivity with a raised critical field; \(\lambda\) is a minimum for a field-free interior only. The aluminium penetration depth is 16 nm in the opened table, where the first version said about 50 nm, and niobium is listed at 32 or 85 nm.

The split from zero resistance is required: a mixed state has field in the bulk and can carry a lossless current.

A remaining gap: QSA does not derive why the equilibrium state is expulsion and not flux trapping. The data distinguish the two; the mapping records expulsion as the stable output.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(\lambda\), \(\chi = -1\) and the \(H_c / H_{c1}\) gates are measured screening and field-threshold specifications; the open items are the derivation of expulsion and the factor-of-several spread in tabulated \(\lambda\).

## Related entries

- [Superconductivity (zero-resistance transport)](superconductivity.md) — different artifact, same condensate
- [Type-II critical field](type-ii-critical-field.md) — mixed state; \(H_{c1}\) and \(H_{c2}\)
- [Flux quantization](flux-quantization.md) — \(\Phi_0\) in a closed loop or one vortex
- [Josephson effect](josephson-effect.md) — weak-link current

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Schmüser, Proc. 11th Workshop on RF Superconductivity (2003), paper MOT01](https://jacow.org/SRF2003/papers/MOT01.pdf) | full-text | Secondary (lecture). Meissner–Ochsenfeld; London equation and 20–50 nm; type I and II; thin sheets below the penetration depth; table of penetration depth and coherence length; Nb fields at 2 K. |
| S2 | [Arutyunov, Golubev and Zaikin, "Superconductivity in one dimension", arXiv:0805.2118 (2008)](https://arxiv.org/abs/0805.2118) | full-text | Table I: penetration depth, coherence length and critical field of Al, Sn, Pb, Nb. |
| S3 | [Hoffman Lab, Harvard, YBCO materials page](https://hoffman.physics.harvard.edu/materials/ybco/) | full-text | Tertiary. YBCO penetration depths along a, b, c (Pereg-Barnea et al. 2004) and in-plane coherence length (Gauzzi et al. 2000). |
| S4 | [CODATA 2022, magnetic flux quantum (NIST)](https://physics.nist.gov/cgi-bin/cuu/Value?flxquhs2e) | full-text | Flux quantum, exact since 2019. |
| S5 | [Zhang et al., *Nature Phys.* 6, 104 (2010)](https://doi.org/10.1038/nphys1499) | snippet | Superconductivity in one-atomic-layer Pb and In films on Si(111). Publisher page not reachable; statement seen in a search excerpt. |
