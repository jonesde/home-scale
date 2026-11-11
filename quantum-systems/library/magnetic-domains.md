---
id: magnetic-domains
title: Magnetic Domains (Partitioned Alignment)
status: formal
family: latched-order
constraints:
  - spatial-buffer
  - energy-barrier
  - field-threshold
  - mechanical-lattice
confidence_data: high
confidence_mapping: medium
related:
  - permanent-magnet-latch
  - ferromagnetic-hysteresis
  - shape-anisotropy
  - superparamagnetism
  - exchange-bias
  - magnetostriction
  - ferroelectric-domains
updated: 2026-11-11
---

# Magnetic Domains (Partitioned Alignment)

### 4.1 Effect Name

Magnetic domains (partitioned alignment)

### 4.2 Macroscopic Observation

A large ferromagnetic body partitions into regions of essentially uniform magnetization (domains) separated by thin walls. In zero applied field the net moment can be far below saturation even though each domain is locally ordered. An applied field moves walls and grows the favorably oriented domains, then rotates the magnetization inside them; at saturation the body is one domain. Below a material-dependent particle size a single domain is the stable state. Walls are imaged directly, and a pattern at rest is static: no continuous power is required to hold it.

### 4.3 Established Quantitative Boundaries

- **Measured.** Walls are imaged: by Bitter powder patterns, electron microscopy and Kerr microscopy in soft films [S1], and by magnetic force microscopy, at 1000 Å resolution in its first report [S2]. A standard monograph chapter reviews the methods [S3].
- **Model (continuum 180° Bloch wall with \(K_1\) only; single-domain estimate from wall energy against magnetostatic energy).** Room-temperature tabulation [S4], with \(\delta_w = \pi\sqrt{A/K_1}\), \(\gamma_w = 4\sqrt{AK_1}\) and a single-domain radius \(36\sqrt{AK_1}/(\mu_0M_s^2)\). The Fe and Ni rows are uniaxial estimates for cubic metals.

  | Material | \(\mu_0M_s\) (T) | \(A\) (pJ/m) | \(K_1\) (MJ/m³) | \(\delta_w\) (nm) | \(\gamma_w\) (mJ/m²) | \(D_\mathrm{sd}\) (nm) |
  |---|---|---|---|---|---|---|
  | Fe | 2.15 | 8.3 | 0.05 | 40 | 2.6 | 12 |
  | Co | 1.76 | 10.3 | 0.53 | 14 | 9.3 | 68 |
  | Ni | 0.61 | 3.4 | −0.005 | 82 | 0.5 | 32 |
  | \(\mathrm{BaFe_{12}O_{19}}\) | 0.47 | 6.1 | 0.33 | 14 | 5.7 | 580 |
  | \(\mathrm{Nd_2Fe_{14}B}\) | 1.61 | 7.7 | 4.9 | 3.9 | 25 | 214 |
  | \(\mathrm{SmCo_5}\) | 1.07 | 22.0 | 17 | 3.6 | 77 | 1528 |

- **Computed here.** The \(D_\mathrm{sd}\) column is twice the radius tabulated in [S4] (6, 34, 16, 290, 107 and 764 nm). With \(K_1 = 4.3\) MJ/m³ [S5] in place of 4.9, the same formulas give for \(\mathrm{Nd_2Fe_{14}B}\) \(\delta_w = 4.2\) nm, \(\gamma_w = 23\) mJ/m² and \(D_\mathrm{sd} = 201\) nm; one review quotes about 200 nm [S6].
- **Model (inferred from spin-wave stiffness).** Exchange stiffness is an inferred quantity. A second tabulation gives Fe 2.0, Co 2.5, Ni 0.8 and \(\mathrm{Ni_{80}Fe_{20}}\) 1.0 µerg/cm, related to the spin-wave stiffness by \(D = 2g\mu_BA/M\) [S7], against 8.3, 10.3 and 3.4 pJ/m in [S4] and [S8].
- **Model (continuum Bloch wall).** A second tabulation of wall energy gives 1.2 (bcc Fe), 9 (\(\mathrm{BaFe_{12}O_{19}}\)), 27 (\(\mathrm{Nd_2Fe_{14}B}\)), 43 (\(\mathrm{Sm_2Co_{17}}\)) and 120 (\(\mathrm{SmCo_5}\)) mJ/m² [S9].
- **Computed here.** Disagreement between the tabulations. 1 µerg/cm is 10 pJ/m, so the second exchange set is 20, 25, 8 and 10 pJ/m: larger by 20/8.3 = 2.4 (Fe), 25/10.3 = 2.4 (Co) and 8/3.4 = 2.4 (Ni). Ni is below \(10^{-11}\) J/m in both sets. Width and energy go as \(\sqrt{A}\), a factor of 1.55: with \(A = 20\) pJ/m and \(K_1 = 0.05\) MJ/m³ the Fe wall width is 63 nm against 40 nm. The wall energies differ by 2.6/1.2 = 2.2 (Fe), 9/5.7 = 1.6 (\(\mathrm{BaFe_{12}O_{19}}\)), 120/77 = 1.6 (\(\mathrm{SmCo_5}\)) and 27/25 = 1.1 (\(\mathrm{Nd_2Fe_{14}B}\)).
- **Measured.** Wall width, directly. In \(\mathrm{Nd_2Fe_{14}B}\), electron holography on a sintered sample gives 90° and 180° walls no wider than 7 and 9 nm [S10], with an upper limit of 10 nm in a second report [S11]; small-angle neutron scattering gives about 6 nm, in agreement with 4–9 nm by other methods [S12]. The formula gives 3.9–4.2 nm. In Fe nanostripes on W(110), spin-polarized tunnelling microscopy images walls with a width on the scale of the lattice constant [S13]. No direct measurement of the wall width in bulk Fe, Co or Ni was found.
- **Model (wall energy against magnetostatic energy).** Single-domain size. The diameter is \(D_\mathrm{sd} = 72\sqrt{AK_1}/(\mu_0M_s^2)\) [S8][S6]; the prefactor 36 gives the radius [S4]. A second tabulation gives 12 nm (Fe), 64 nm (Co) and 31 nm (Ni) [S8]. Kittel's first estimates were \(2\times10^{-6}\) cm (20 nm) for particles and \(3\times10^{-5}\) cm (300 nm) for films, each movable by a factor of ten [S14]. Micromagnetic calculations give 25 nm for iron cubes (17 nm in earlier work) and about 73 nm for magnetite [S15].
- **Measured.** Single-domain size of \(\mathrm{Nd_2Fe_{14}B}\): about 0.2–0.4 µm, from magnetization measurements on polycrystalline samples [S12].
- **Model (room-temperature blocking diameter as tabulated).** Superparamagnetic diameter: Fe 16 nm, Co 7 nm, Ni 34 nm [S8]. For Fe and Ni it lies above the single-domain diameter of the same table (12 and 31 nm); the 25 nm micromagnetic value for iron [S15] would leave a window of 16–25 nm. For Co it lies below (7 against 64 nm). For \(\mathrm{Nd_2Fe_{14}B}\) the order of lengths is: the superparamagnetic limit (number in [superparamagnetism](superparamagnetism.md)), then the single-domain diameter of 0.2–0.4 µm [S12], then sintered-magnet grains of 5–10 µm [S6].
- **Measured.** Wall type in films. In continuous permalloy films cross-tie walls occupy a thickness range of about 30–90 nm, with Néel walls below it and asymmetric Bloch walls above [S1], which quotes the numbers from earlier work that was not opened. The thickness below which Néel walls are favoured is set by the exchange length [S4].
- **Measured.** Response to a field. Magnetization proceeds by wall motion and by rotation inside the domains. In iron and Fe–Si the coercive field (10–100 A/m in polycrystalline iron) is the field at which walls unpin from defects, and substantial rotation needs \(10^3\)–\(10^4\) A/m [S16]. Near the coercive field wall motion is the dominant mechanism, and Barkhausen jumps are irregular fluctuations in the motion of a wall [S17]. Sintered Nd-Fe-B with 5–10 µm grains shows a one-step initial magnetization curve, read as an absence of pinning sites inside the grains [S6]. No opened source gives a saturation field or reports saturation as a sharp transition.
- **Measured.** Curie temperatures: Fe 1044 K, Ni 628 K, \(\mathrm{BaFe_{12}O_{19}}\) 742 K, \(\mathrm{Nd_2Fe_{14}B}\) 585 K, \(\mathrm{SmCo_5}\) 1020 K [S4].
- **Measured.** Precession scale: \(\gamma/2\pi = 28.025\) GHz/T (CODATA 2022, free electron) [S18].
- **Convention.** Holding a static domain pattern costs zero continuous power: it is a static configuration, and no source reports a dissipation at rest. Moving walls around a [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) loop dissipates the loop area.

**Data confidence:** High for the existence of walls, domains and a single-domain size, which are imaged or measured. Medium for the numbers. Exchange stiffness is inferred and two tabulations differ by 2.4×; widths, energies and single-domain sizes are formula outputs, and the Fe and Ni rows are uniaxial estimates. The only direct wall-width measurements opened are for \(\mathrm{Nd_2Fe_{14}B}\) and for Fe nanostripes, and the holography, tunnelling-microscopy and Kittel papers were opened as abstracts only. The permalloy thickness range comes from a secondary source.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Continuum Bloch wall (180°, \(K_1\) only) [S4]:

  \[
  \delta_w = \pi\sqrt{\frac{A}{K_1}},\qquad \gamma_w = 4\sqrt{AK_1}
  \]

  Néel walls, with the magnetization rotating in the film plane, replace this form in thin films [S1][S4].

- Magnetostatic energy of a uniformly magnetized body is of order \((\mu_0/2)M_s^2 \times\) (shape factor) \(\times V\) ([shape-anisotropy](shape-anisotropy.md)). Partitioning into domains reduces that term and adds wall area \(\times\,\gamma_w\) [S14].

- Single-domain diameter of a sphere [S8][S6]:

  \[
  D_\mathrm{sd} = \frac{72\sqrt{AK_1}}{\mu_0M_s^2}
  \]

  The prefactor is 72 for the diameter and 36 for the radius [S4]. It depends on the assumed shape and wall.

- Applied-field term \(-\mu_0\mathbf{M}\cdot\mathbf{H}\) grows one set of domains at the expense of another until the walls are expelled.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two nested buffers:
  1. **Wall.** A transition strip in which the moment rotates between adjacent latched directions. Its width by formula is 3.6–82 nm across the tabulated materials; the measured width in \(\mathrm{Nd_2Fe_{14}B}\) is 4–9 nm. In films the wall type changes with thickness.
  2. **Domain pattern.** A body larger than the single-domain diameter: 12–25 nm by estimate in iron, 0.2–0.4 µm measured in \(\mathrm{Nd_2Fe_{14}B}\). Below that size the particle holds one domain. No domain period is filed; the opened sources give none.

- **Clock rate / latency.** Moments precess at the 28.025 GHz/T carrier. Pattern changes are wall-motion events, which proceed in unpinning jumps set by the defect structure. A static pattern has no ongoing clock cost.

- **Energy barriers or thresholds.** Each domain is the same anisotropy latch as [permanent-magnet-latch](permanent-magnet-latch.md). The wall is a distributed transition whose energy per area, 0.5–77 mJ/m² in the table, is the cost of a partition. Pinning of walls at defects is the barrier that appears as \(H_c\) on the loop of a soft material. Holding a static partition costs zero continuous power.

- **Dominant failure modes.**
  - **Crossover** — single-domain size: a comparison of wall energy with magnetostatic energy, \(D_\mathrm{sd} = 72\sqrt{AK_1}/(\mu_0M_s^2)\) for the diameter of a sphere. The prefactor depends on shape, and the first estimates carried a factor of ten. Values run from 12–25 nm in iron to 0.2–0.4 µm in \(\mathrm{Nd_2Fe_{14}B}\) and about 1.5 µm in \(\mathrm{SmCo_5}\). Below it the particle is one latch cell.
  - **Crossover** — saturation: a field first displaces walls, at the coercive field, and then rotates the magnetization, at \(10^3\)–\(10^4\) A/m in iron and Fe–Si. The technical saturation field, at which the last wall is removed, is microstructure-dependent, and no opened source reports a sharp transition. The local latch remains; the partition is gone.
  - **Crossover** — pinning: the field that moves walls varies continuously with defect content (iron from 1–2 to a few hundred A/m). With weak pinning a written pattern does not survive \(H \to 0\) as a useful net remanence. Mechanical damage acts through this term; no measured scale is filed.
  - **Threshold** — Curie point: \(T > T_C\) (Fe 1044 K, Ni 628 K, \(\mathrm{Nd_2Fe_{14}B}\) 585 K). Local order is gone and domains with it. A phase transition.
  - **Crossover** — thermal, volume: relaxation of a single grain is [superparamagnetism](superparamagnetism.md). In a hard magnet that limit lies below the single-domain diameter. In Fe and Ni the tabulated blocking diameter (16 and 34 nm) sits among the single-domain estimates (12–25 and 31–32 nm), so on crystal anisotropy alone the stable single-domain window is narrow or absent.

- **Emergent constant or stable output.** A static partition of the aligned population, with walls of finite width (4–9 nm measured in \(\mathrm{Nd_2Fe_{14}B}\)) and a net moment anywhere from about zero (closed pattern) to saturation (walls expelled), at zero continuous power while the pattern is at rest.

### 4.6 Internal Consistency Notes

Domains are many latches sharing one body, with walls as the finite-width boundaries. Zero hold power on a static pattern and dissipation only when walls move fit the family. Among latched-order entries the wall width is unusual in being a length.

Sourcing changed six things. First, the wall widths and energies in the first version were formula outputs presented as measurements. The opened direct measurements cover \(\mathrm{Nd_2Fe_{14}B}\) (4–9 nm against 3.9–4.2 nm by formula) and Fe nanostripes; none was found for bulk Fe, Co or Ni. Second, exchange stiffness is an inferred input: two tabulations differ by 2.4×, and Ni is below \(10^{-11}\) J/m in both, so "of order \(10^{-11}\) J/m in Fe, Co, Ni" was too coarse. Third, the single-domain size is a crossover with a shape-dependent prefactor. The first version called it a cliff and gave no numbers; iron sits at 12–25 nm and hard magnets at 0.2–1.5 µm. Fourth, saturation is not reported as a sharp collapse in any opened source, so the "two sharp collapses" of the first version are two crossovers. Fifth, the statement that two domains merge below the wall width had no source and is removed. Sixth, \(K_1 = 4.5\) MJ/m³ for \(\mathrm{Nd_2Fe_{14}B}\) was not found; the opened values are 4.3 and 4.9.

One consequence for the mapping: "below the single-domain size the particle is one latch cell" holds for the hard magnets and for Co. For Fe and Ni the tabulated room-temperature blocking diameter sits among the single-domain estimates, so on crystal anisotropy alone that cell is thermally stable in a narrow window at most.

The mapping is not closed on pattern selection. Why one sample shows closure domains, another stripes, another a maze is a magnetostatic-plus-pinning problem whose output is imaged and is not derived here from node rules. \(A\) and \(K_1\) are taken as inputs to \(\delta_w\) and \(\gamma_w\); QSA does not produce those two stiffnesses from a more primitive buffer, and \(A\) itself is uncertain by a factor of 2.4. The mesoscale gap of the hysteresis file reappears as wall pinning and \(H_c\).

The electrical twin is [ferroelectric-domains](ferroelectric-domains.md). Polar walls can carry bound charge and need screening; magnetic walls pay a magnetostatic cost. The wall widths in this file do not carry over to ferroelectric walls.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the finite wall width, the single-domain crossover and zero hold power are solid, but the wall numbers rest on an inferred exchange stiffness, and pattern choice and the pinning that sets technical \(H_c\) remain mesoscale data without a closed specification.

## Related entries

- [permanent-magnet-latch](permanent-magnet-latch.md) — the local directional state of which each domain is a copy
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — the write / erase cycle; wall motion dominates near the coercive field in bulk soft material
- [shape-anisotropy](shape-anisotropy.md) — magnetostatic energy that, unpartitioned, is the geometry barrier
- [superparamagnetism](superparamagnetism.md) — thermal relaxation of a single grain; owns the blocking sizes
- [exchange-bias](exchange-bias.md) — interface pinning of FM domains by an AFM latch
- [magnetostriction](magnetostriction.md) — strain locked to the local domain direction
- [ferroelectric-domains](ferroelectric-domains.md) — polar twin: partitioned *P*, nm-class walls, charged walls possible

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Wiese, McVitie, Chapman, Capella-Kort and Otto, *Europhys. Lett.* 80, 57003 (2007), arXiv:0710.1963](https://arxiv.org/abs/0710.1963) | full-text | Bitter, electron-microscopy and Kerr observation of walls; permalloy films: cross-tie walls at about 30–90 nm, Néel walls below, asymmetric Bloch walls above (secondary for the numbers; Middelhoek 1963 was not opened). |
| S2 | [Martin and Wickramasinghe, *Appl. Phys. Lett.* 50, 1455 (1987)](https://pubs.aip.org/apl/article/50/20/1455/52159/Magnetic-imaging-by-force-microscopy-with-1000-A) | abstract | First magnetic force microscopy, 1000 Å resolution. |
| S3 | [Hubert and Schäfer, *Magnetic Domains* (Springer, 1998), Ch. 2, "Domain Observation Techniques"](https://link.springer.com/chapter/10.1007/978-3-540-85054-0_2) | abstract | Standard review of domain observation methods (landing page and reference list only). |
| S4 | [Skomski, "Micromagnetic Spin Structure", in *Spin Electronics*, Lecture Notes in Physics 569, 204 (2001)](https://boulderschool.yale.edu/sites/default/files/files/heinonen_skomski.pdf) | full-text | The table of polarization, exchange stiffness, anisotropy, wall width, wall energy and single-domain radius; the wall and single-domain formulas; Fe and Ni as uniaxial estimates; Néel walls and the exchange length; Curie temperatures. |
| S5 | [Fischbacher et al., *J. Phys. D* 51, 193002 (2018), arXiv:1903.11922](https://arxiv.org/abs/1903.11922) | full-text | Nd2Fe14B parameter set with anisotropy 4.3 MJ/m³, polarization 1.61 T and exchange stiffness 7.7 pJ/m. |
| S6 | [Li, Sepehri-Amin, Sasaki, Ohkubo and Hono, *Sci. Technol. Adv. Mater.* 22, 386 (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8183520/) | full-text | Single-domain diameter formula with prefactor 72, about 200 nm for Nd2Fe14B; sintered grains of 5–10 µm; one-step initial curve read as no pinning inside grains. |
| S7 | [Dubowik and Gościańska, arXiv:1306.5988 (2014), Table I](https://arxiv.org/abs/1306.5988) | full-text | Second tabulation of exchange stiffness for Fe, Co, Ni and permalloy, tied to spin-wave stiffness (values cited there to Frait and Fraitová 1988, not opened). |
| S8 | [Coey, "Materials for Spin Electronics", in *Spin Electronics*, Lecture Notes in Physics 569, 277 (2001), Table 12.2](https://boulderschool.yale.edu/sites/default/files/files/coey_spintronics.pdf) | full-text | Exchange stiffness, single-domain diameter (formula with 72) and superparamagnetic diameter for Fe, Co, Ni. |
| S9 | [de Campos and de Castro, *Arch. Electr. Eng.* 73, 1087 (2024), Table 1](https://czasopisma.pan.pl//Content/133391/PDF/14_2k.pdf) | full-text | Second tabulation of wall energies. The column unit is printed as erg/cm³ and is read here as erg/cm². |
| S10 | [McCartney and Zhu, *J. Appl. Phys.* 83, 6414 (1998)](https://asu.elsevierpure.com/en/publications/off-axis-electron-holographic-mapping-of-magnetic-domains-in-nd-s/) | abstract | Nd2Fe14B walls no wider than 7 nm (90°) and 9 nm (180°) by electron holography. |
| S11 | [McCartney and Zhu, *Appl. Phys. Lett.* 72 (11) (1998), doi:10.1063/1.121060](https://www.osti.gov/biblio/615360) | abstract | Upper limit of 10 nm for the wall width in Nd2Fe14B. |
| S12 | [Kreyssig et al., arXiv:0901.3515 (2009)](https://arxiv.org/abs/0901.3515) | full-text | Wall width about 6 nm from neutron scattering, 4–9 nm by other methods; single-domain size 0.2–0.4 µm from magnetization measurements. |
| S13 | [Pratzer et al., *Phys. Rev. Lett.* 87, 127201 (2001)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.87.127201) | abstract | Walls on the scale of the lattice constant in Fe nanostripes, imaged by spin-polarized tunnelling microscopy. |
| S14 | [Kittel, *Phys. Rev.* 70, 965 (1946)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.70.965) | abstract | First single-domain estimates: 2×10⁻⁶ cm for particles, 3×10⁻⁵ cm for films, each uncertain by a factor of ten; domain structure as an energy balance. |
| S15 | [Muxworthy and Williams, *Geophys. J. Int.* 202, 578 (2015)](https://academic.oup.com/gji/article/202/1/578/592327) | full-text | Micromagnetic single-domain thresholds: 25 nm for iron cubes (17 nm earlier), about 73 nm for magnetite. Read through a fetch tool, not checked against the raw page. |
| S16 | [Fiorillo, Bertotti, Appino and Pasquale, "Soft Magnetic Materials", *Wiley Encyclopedia of Electrical and Electronics Engineering* (2016), accepted version](https://iris.inrim.it/bitstream/11696/54676/4/SoftMagneticMaterials_Wiley_Enciclopedia_2016_postprint.pdf) | full-text | Review chapter. Wall motion and rotation as the two mechanisms; coercive field as wall unpinning; rotation fields of 10³–10⁴ A/m; iron coercivities. |
| S17 | [Durin and Zapperi, "The Barkhausen effect", arXiv:cond-mat/0404512 (2004)](https://arxiv.org/abs/cond-mat/0404512) | full-text | Wall motion dominant near the coercive field; Barkhausen jumps as irregular wall motion (quoting Kittel 1949, not opened). |
| S18 | [NIST, CODATA 2022 recommended value, electron gyromagnetic ratio in MHz/T](https://physics.nist.gov/cgi-bin/cuu/Value?gammaebar) | full-text | 28 024.951 MHz/T. |
