---
id: piezoelectricity
title: Piezoelectricity (Strain–Polarization Coupling)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
  - field-threshold
  - thermal
confidence_data: high
confidence_mapping: medium
review_depth: standard
related:
  - ferroelectric-remanence
  - ferroelectric-domains
  - elasticity
  - magnetostriction
  - melting
  - phonon-dispersion
  - refraction-dielectric
  - dielectric-breakdown
updated: 2026-11-13
---

# Piezoelectricity (Strain–Polarization Coupling)

### 4.1 Effect Name

Piezoelectricity (strain–polarization coupling)

### 4.2 Macroscopic Observation

Compressing a quartz plate, a poled PZT ceramic or an AlN film produces charge on its electrodes. Applying a voltage produces a proportional strain. The effect is linear at ordinary drive and reverses with the sign of the stress or field. It is absent in crystals that have a centre of symmetry. In ferroelectric piezoelectrics (PZT, \(\mathrm{BaTiO_3}\)) the coupling of a poled ceramic disappears on heating through the Curie point. Quartz is not ferroelectric; its coupling belongs to the crystal structure and needs no poling.

### 4.3 Established Quantitative Boundaries

- **Convention.** Symmetry requirement. Of the 32 crystal classes, 21 have no centre of symmetry, and 20 of those are piezoelectric; the exception is the cubic class 432. Ten of the 20 are polar classes with a spontaneous polarization [S1]. A non-centrosymmetric structure is therefore necessary [S2] and, with one exception, sufficient.
- **Measured.** Quartz. \(d_{11}\) = 2.25–2.31 pm V⁻¹ in four tabulated determinations, and \(d_{14}\) = 0.57–0.85 pm V⁻¹. \(d_{11}\) falls with temperature: 2.31 at −196 °C and 2.05 at 100 °C in one series. The low–high (α–β) inversion is at 573.3 °C on heating, and "quartz" in the electronic sense means the phase below it [S3].
- **Computed here.** 573.3 °C is 846 K. The fall in \(d_{11}\) between −196 °C and 100 °C is 11 %.
- **Measured.** PZT ceramics, \(d_{33}\) in pC N⁻¹ with Curie point: PZT5A 400 (365 °C); PZT5H 618 (195 °C); PZT4 290 (320 °C); PZT8 225 (300 °C) [S4]. One vendor's grades run 390, 500 and 650 pC N⁻¹ [S5].
- **Measured.** \(\mathrm{BaTiO_3}\): \(d_{33}\) = 85.6 pC N⁻¹ and \(d_{15}\) = 392 pC N⁻¹ in a single crystal [S6]; 190 pC N⁻¹ for the ceramic, with a Curie point of 115 °C in that table [S7]. The tetragonal-to-cubic transition is otherwise given as 120 °C [S2].
- **Measured.** AlN: \(d_{33}\) = 5.6 pm V⁻¹ for the bulk single crystal, 3.4–5.15 pm V⁻¹ for polycrystalline material, and an effective 1.8 pm V⁻¹ for a film clamped to a silicon substrate [S8]. \(\mathrm{LiNbO_3}\): \(d_{33}\) = 6–16 pC N⁻¹ and \(d_{15}\) = 68–74 pC N⁻¹ across three determinations [S6].
- **Measured.** PVDF polymer: \(d_{33}\) = −21 and −27.1 pC N⁻¹ in two determinations [S6]. The sign is opposite to that of the ceramics.
- **Computed here.** \(d_{33}\) of PZT5H is 270 times \(d_{11}\) of quartz (618/2.30) and 110 times \(d_{33}\) of AlN. At 1 MV m⁻¹ the strain \(dE\) is \(6.2\times10^{-4}\) in PZT5H and \(2.3\times10^{-6}\) in quartz. The Curie points are 468 K (PZT5H), 638 K (PZT5A) and 393 K (\(\mathrm{BaTiO_3}\), 120 °C).
- **Measured.** Curie point and depoling. Above the Curie point each crystallite of a perovskite ceramic is cubic with no dipole moment; poling is done slightly below it [S9]. A ceramic can lose its poled state below the Curie point: \(\mathrm{Na_{0.5}Bi_{0.5}TiO_3}\) depolarizes at 187 °C against a Curie point of 325 °C [S2]. Acceptor-doped ("hard") PZT is harder both to pole and to depole [S2].
- **Computed here.** That depolarization temperature is 138 K below the Curie point.
- **Measured.** The response of a ferroelectric ceramic has an intrinsic part (lattice deformation) and an extrinsic part (domain-wall motion). Acceptor doping pins walls, which is why hard PZT has smaller coefficients than soft PZT [S4].

**Data confidence:** High for the symmetry rule, quartz and the PZT grades, read in full text. Medium for \(\mathrm{BaTiO_3}\), \(\mathrm{LiNbO_3}\) and PVDF, which rest on a tertiary list, and for the ceramic \(\mathrm{BaTiO_3}\) value, which was seen only as a search excerpt of [S7]. Whether β-quartz remains piezoelectric above 573 °C was not settled by an opened source and is not claimed.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Linear constitutive pair (direct and converse):

  \[
  D_3 = d_{33}\,\sigma_3, \qquad S_3 = d_{33}\,E_3
  \]

  and in general \(P_i = d_{ijk}\sigma_{jk}\), \(\varepsilon_{jk} = d_{ijk}E_i\). The direct and converse coefficients are equal [S2]. \(d_{ijk}\) is a measured tensor and is identically zero when inversion is a symmetry of the crystal.

- Electrostriction (\(\varepsilon \propto E^2\)) exists in all dielectrics and is not this effect.

- In a ferroelectric ceramic the measured \(d\) is the sum of intrinsic and extrinsic contributions [S4] and exists only while the grains hold a net poled direction.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A crystal in one of the 20 piezoelectric classes, or a ceramic of ferroelectric grains with a net poled direction. A centrosymmetric crystal of any size does not provide the coupling. Film thickness matters through clamping: an AlN film on silicon shows 1.8 pm V⁻¹ against 5.6 in the free crystal. The poled state of a ceramic is the latch of [ferroelectric-remanence](ferroelectric-remanence.md); this file owns the strain–polarization link.

- **Clock rate / latency.** The mechanical side follows the acoustic clocks of [elasticity](elasticity.md) and `speed-of-sound` (transit across the plate); the electrical side follows the dielectric response ([refraction-dielectric](refraction-dielectric.md)). No clock number is filed here.

- **Energy barriers or thresholds.** The existence condition is a symmetry, not an energy barrier. A ferroelectric adds a thermal threshold at the Curie point and a poled state that can be lost below it. The coercive field writes the poled state; it is not the coupling.

- **Dominant failure modes.**
  - **Threshold** — symmetry: with a centre of symmetry (or in class 432) every \(d_{ijk}\) is zero. Exact, by symmetry.
  - **Threshold** — Curie point of a ferroelectric: 393 K (\(\mathrm{BaTiO_3}\)), 468–638 K across PZT grades. The grains become cubic and the poled state is erased. A phase transition.
  - **Crossover** — depoling below the Curie point: the net poled direction of a ceramic can be lost well below \(T_C\) (187 °C against 325 °C in one titanate) and by reverse field or stress. Gradual and composition-dependent; no functional form filed.
  - **Threshold** — structural transition of a non-ferroelectric: quartz at 846 K, where the low-temperature set of coefficients ends.
  - **Crossover** — temperature within a phase: quartz \(d_{11}\) falls 11 % from −196 °C to 100 °C.
  - **Crossover** — clamping and amplitude: a substrate reduces the effective coefficient; large drive leaves the linear range. No scale filed for the latter.
  - **Threshold** — loss of the lattice by melting ([melting](melting.md)) or of the insulator by breakdown ([dielectric-breakdown](dielectric-breakdown.md)).

- **Emergent constant or stable output.** A linear, reversible conversion between strain and polarization with a material coefficient from 2.3 pm V⁻¹ (quartz) to about 600 pm V⁻¹ (soft PZT), present while the crystal class, and for a ceramic the poled state, hold.

### 4.6 Internal Consistency Notes

The symmetry condition is exact: where inversion is a symmetry the linear output is forbidden at any field short of breakdown.

Two routes to failure stay separate. Quartz keeps its coupling until the crystal structure changes. A PZT ceramic loses its coupling when its grains lose their common poled direction, at the Curie point at the latest and possibly well below it. The latch entry owns the poled state; this entry owns \(d_{ijk}\).

Sourcing changed three things. The first version said twenty of the 32 crystal classes lack an inversion centre; twenty-one do, and twenty are piezoelectric, so lack of inversion is necessary and not quite sufficient. It gave the ferroelectric failure as a single threshold at \(T_C\); the opened sources add depoling below \(T_C\), which is gradual. And it described the coupling of a ceramic as a property of the polar lattice alone; the measured coefficient includes domain-wall motion, which is why doping that pins walls lowers it. The statement that β-quartz stays non-centrosymmetric was dropped for want of an opened source.

The mapping takes measured \(d_{ijk}\) as the coupling strength. It does not derive the factor of 270 between quartz and soft PZT, and the extrinsic share ties that factor to the wall dynamics of [ferroelectric-domains](ferroelectric-domains.md), which are themselves open.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the symmetry condition and the Curie threshold are sharp and correctly placed; the coupling magnitude is taken from measurement, and in ceramics part of it belongs to domain walls.

## Related entries

- [ferroelectric-remanence](ferroelectric-remanence.md) — the polar latch; owns the poled state
- [ferroelectric-domains](ferroelectric-domains.md) — wall motion supplies the extrinsic part of a ceramic's coefficient
- [elasticity](elasticity.md) — the strain hardware
- [magnetostriction](magnetostriction.md) — the magnetic analogue
- [melting](melting.md) — destruction of the lattice
- [phonon-dispersion](phonon-dispersion.md) — the lattice whose symmetry is the condition
- [refraction-dielectric](refraction-dielectric.md) — bound-charge polarization without the strain coupling
- [dielectric-breakdown](dielectric-breakdown.md) — high-field destruction of the dielectric

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Wikipedia, "Piezoelectricity"](https://en.wikipedia.org/wiki/Piezoelectricity) | full-text | Tertiary: 21 non-centrosymmetric classes of 32, 20 piezoelectric, class 432 the exception, ten polar. |
| S2 | [Aksel and Jones, *Sensors* 10, 1935 (2010)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3264460/) | full-text | Secondary review: non-centrosymmetry as the requirement; direct and converse coefficients equal; BaTiO3 transition at 120 °C; NBT depolarization at 187 °C against a Curie point of 325 °C; hard PZT harder to pole and depole. |
| S3 | [Ward, "The Constants of Alpha Quartz", IEEE UFFC](https://ieee-uffc.org/node/2520) | full-text | Compilation: d11 and d14 of quartz, d11 against temperature, inversion at 573.3 °C. |
| S4 | [Liu, Zhang, Jiang and Cao, *Mater. Sci. Eng. R* 89, 1 (2015)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4369800/) | full-text | Review, Table 8: d33 and Curie points of PZT5A, PZT5H, PZT4, PZT8; intrinsic and extrinsic contributions; wall pinning in hard PZT. |
| S5 | [Piezo.com, "Material Properties"](https://support.piezo.com/article/62-material-properties) | full-text | Tertiary (vendor): d33 of 390, 500 and 650 pC/N for three PZT grades. |
| S6 | [Wikipedia, "List of piezoelectric materials"](https://en.wikipedia.org/wiki/List_of_piezoelectric_materials) | full-text | Tertiary: BaTiO3 single-crystal d33 and d15; LiNbO3 coefficients; PVDF d33. |
| S7 | [Shrout and Zhang, *J. Electroceram.* 19, 111 (2007)](https://doi.org/10.1007/s10832-007-9047-0) | snippet | BaTiO3 ceramic: d33 190 pC/N, Curie point 115 °C. |
| S8 | [Ciers et al., arXiv:2402.12196 (2024)](https://arxiv.org/abs/2402.12196) | full-text | Secondary: AlN d33 of 5.6 pm/V (single crystal) and 3.4–5.15 pm/V (polycrystalline); 1.8 pm/V measured for a clamped film. |
| S9 | [APC International, "Piezoelectricity"](https://www.americanpiezo.com/knowledge-center/piezo-theory/piezoelectricity.html) | full-text | Tertiary (vendor): cubic symmetry with no dipole moment above the Curie point; poling slightly below it. |
