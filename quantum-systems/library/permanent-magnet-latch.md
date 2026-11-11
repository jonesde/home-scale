---
id: permanent-magnet-latch
title: Permanent Magnet (Directional Latch)
status: formal
family: latched-order
constraints:
  - energy-barrier
  - thermal
  - mechanical-lattice
  - spatial-buffer
confidence_data: high
confidence_mapping: high
related:
  - superparamagnetism
  - ferromagnetic-hysteresis
  - magnetic-domains
  - shape-anisotropy
  - magnetostriction
updated: 2026-11-11
---

# Permanent Magnet (Directional Latch)

### 4.1 Effect Name

Permanent magnet (directional latch)

### 4.2 Macroscopic Observation

A hard permanent magnet (for example sintered Nd-Fe-B) exerts a continuous directional force on iron and on other magnets with no external power input and no heat generation while it sits at rest. Soft magnetic materials (annealed iron, electrical steels) take a large magnetization in an applied field and lose almost all useful remanence when the field is removed. Heating a hard magnet through its Curie point, shocking it hard enough, or breaking it down chemically destroys the net directional force.

### 4.3 Established Quantitative Boundaries

- **Measured.** Free-electron gyromagnetic ratio \(\gamma_e/2\pi = 28\,024.951\,3861(87)\,\mathrm{MHz\,T^{-1}}\) [S1].
- **Measured.** \(\mathrm{Nd_2Fe_{14}B}\) Curie temperature 585 K in the discovery paper and in two later papers; 588 K in one review. Spread 585–588 K [S2][S3][S4].
- **Measured.** \(\mathrm{Nd_2Fe_{14}B}\) room-temperature anisotropy constant \(K_1\): 4.30 MJ m⁻³ on single crystals [S5], 4.9 MJ m⁻³ in another tabulation [S6]; about 3.5 MJ m⁻³ in the 1984 first report on a polycrystal [S2]. Saturation polarization 1.61 T [S5][S6]. The first version of this file used 4.5 MJ m⁻³, which lies inside the range but was not found in any opened source.
- **Model (\(\mu_0 H_a = 2K_1/M_s\)).** Anisotropy field 7.6–7.65 T as tabulated [S6][S14]; 6.7 T if computed from \(K_1 = 4.30\) MJ m⁻³.
- **Measured.** Commercial Nd-Fe-B grades list Curie temperatures of 310–380 °C (vendor catalogues; tertiary) [S9].
- **Measured.** Elemental ferromagnets [S8][S4][S18]: Fe \(T_C\) 1043–1044 K, \(K_1 = 48\) kJ m⁻³, polarization 2.15 T. Ni \(T_C\) 628–631 K, \(K_1 = -5\) kJ m⁻³, 0.60–0.61 T. Co \(T_C\) 1360–1404 K (sources disagree), \(K_1 = 530\) kJ m⁻³.
- **Computed here.** Iron has about a hundredth of the anisotropy of \(\mathrm{Nd_2Fe_{14}B}\) (48 kJ m⁻³ against 4.3–4.9 MJ m⁻³, a factor of 90–102) and nearly twice its Curie temperature (1043 K against 585 K). The Curie temperature does not track the anisotropy.
- **Model (Heisenberg / mean field).** The Curie temperature is set by the exchange coupling between moments, mainly in the 3d sublattice; the magnetocrystalline anisotropy comes from spin–orbit coupling and the rare-earth crystal field [S3][S4].
- **Measured.** Soft materials have coercivities from under 1 A m⁻¹ (permalloys) to roughly 100 A m⁻¹ (annealed iron) in handbook compilations read second-hand [S10]. The values read in full text, which differ in detail, are in [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md).
- **Measured.** The first sintered Nd-Fe-B magnet had intrinsic coercivity 960 kA m⁻¹ (about 1.2 T), remanence 1.23 T and energy product 290 kJ m⁻³ [S2].
- **Computed here.** 1.2 T is 16–18 % of the 6.7–7.65 T anisotropy field.
- **Model (micromagnetic simulation).** Even a defect-free cubic grain falls short of the ideal nucleation field once its own demagnetizing field and thermal activation are included: 3.94 T against 6.09 T [S7].
- **Computed here.** 3.94 T is about 65 % of 6.09 T.
- **Measured.** Shock. A transverse explosive shock of 22.3 GPa turns \(\mathrm{Nd_2Fe_{14}B}\) from a hard ferromagnet into a weak magnet [S11]. Sintered Nd-Fe-B shocked at 6.26–7.16 GPa is demagnetized, with intergranular fracture and no structural change of the grain-boundary phase; the coercivity is recoverable by re-annealing [S12]. Hydrogen decrepitation turns sintered Nd-Fe-B into a demagnetized hydrogenated powder [S13]. No source was found for plastic deformation as a demagnetization route; the first version listed it.
- **Convention.** Thermal stability of one grain is written \(KV \ge 25\,kT\), which corresponds to a 100 s measurement with an attempt time of 10⁻⁹ s [S16]. Detail is in [superparamagnetism](superparamagnetism.md).
- **Computed here.** With \(K_1 = 4.3\)–4.9 MJ m⁻³ at 300 K, \(V = 25\,kT/K_1 = 2.1\)–\(2.4 \times 10^{-26}\,\mathrm{m^3}\): a sphere 3.4–3.6 nm across, or a cube 2.8–2.9 nm on a side. The first version of this file called the same volume "of order 30 nm". That was an arithmetic error; a 30 nm cube has \(KV \approx 29\,000\,kT\).
- **Model (wall energy against magnetostatic energy).** Single-domain diameter of \(\mathrm{Nd_2Fe_{14}B}\): 214 nm tabulated, about 200 nm calculated with the coercivity of milled powders peaking there, about 300 nm in lecture notes [S14][S15][S18].
- **Measured.** Reversal of a single small particle is thermally activated over one barrier: waiting-time, switching-field and telegraph-noise measurements on individual 15–30 nm particles at 0.1–6 K agree with the Néel–Brown model [S17].
- **Convention.** A magnet at rest dissipates nothing: it is a static state. Energy is spent to change the magnetization (the hysteresis loop).

**Data confidence:** High — Curie temperatures, saturation, and the hard/soft distinction agree across independent sources. \(K_1\) of \(\mathrm{Nd_2Fe_{14}B}\) is known to about ±7 %. The single-crystal primaries (Hock 1988; Durst and Kronmüller 1986) and the Herbst review were not opened; their values are read from papers that tabulate them. Commercial Curie ranges and soft-magnet coercivities rest on vendor and secondary tables.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Larmor frequency: \(f = \gamma_e B/2\pi\) [S1].
- Uniaxial anisotropy energy density \(E_A = K_1\sin^2\theta\), with a per-grain barrier \(\Delta E \approx K_1 V\) between the two easy directions [S16].
- Néel–Arrhenius escape time [S16]:

  \[
  \tau = \tau_0 \exp\!\left(\frac{K_1 V}{kT}\right)
  \]

- Anisotropy field \(\mu_0 H_a = 2K_1/M_s\) [S6].
- Force on a moment in a field gradient: \(\mathbf{F} = \nabla(\mathbf{m}\cdot\mathbf{B})\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two separate resources, and the first version ran them together:
  1. **Order.** Exchange coupling between moments. It makes the grain act as one moment and sets the Curie temperature.
  2. **Direction.** Anisotropy of the crystal. It holds that one moment along an axis and sets the latch barrier \(K_1V\).

  The smallest grain that holds its direction at room temperature on laboratory time is a few nanometres across for \(\mathrm{Nd_2Fe_{14}B}\). Real magnets are far from that limit: the single-domain diameter is about 200–300 nm and the grains of a sintered magnet are larger still, so thermal erasure of whole grains is not what limits a commercial magnet. The macroscopic force scales with the aligned moment; there is no minimum sample size.

- **Clock rate / latency.** Precession at 28.02 GHz T⁻¹. Thermal escape attempts on the \(\tau_0\) scale, 10⁻⁹ to 10⁻¹² s. Writing a hard magnet is set by the field sweep, nucleation and wall motion, not by either of those.

- **Energy barriers or thresholds.** \(K_1V\) per grain against rotation of the whole grain. In a real magnet reversal starts at defects and grain boundaries well below that barrier, which is why the coercivity is under a fifth of the anisotropy field. Holding the state costs no power.

- **Dominant failure modes.**
  - **Threshold** — thermal, order: \(T > T_C\). A continuous phase transition set by exchange; the magnetization goes to zero. This is not \(kT\) overcoming the anisotropy barrier, as the first version said.
  - **Crossover** — thermal, direction: \(\tau = \tau_0\exp(KV/kT)\). There is no critical size; the retention time falls exponentially as the grain shrinks, and the size quoted depends on the waiting time chosen. Owned by [superparamagnetism](superparamagnetism.md).
  - **Crossover** — field: a reverse field writes the opposite state. One grain at zero temperature has a definite switching field; a magnet has a distribution of them, and each is lowered by thermal activation and by waiting. Coercivity also falls continuously with temperature well before \(T_C\).
  - **Crossover** — mechanical: shock demagnetizes through fracture and through a pressure-induced change of the magnetic phase. Two measured points (about 6–7 GPa and 22 GPa), no threshold established.
  - **Threshold** — chemical: hydrogen decrepitation converts the alloy to a hydrided powder. A change of material, not of magnetic state.

- **Emergent constant or stable output.** A stable directional moment and its static field and force, at zero continuous power, for as long as temperature, reverse field and the lattice stay inside the envelope above.

### 4.6 Internal Consistency Notes

The volatile/non-volatile split maps onto absence or presence of a sufficient anisotropy barrier, and zero continuous power is what a static state costs. Those two clauses survived sourcing unchanged.

Sourcing changed four things. The grain size for thermal stability was wrong by a factor of ten in length and a thousand in volume, and the error had been copied into the requirement table, the spec sheets and three application files. The Curie point was attributed to the anisotropy barrier; it is an exchange threshold, and iron (a hundredth of the anisotropy, nearly twice the Curie temperature) shows the two are independent. The volume limit was described as a cliff and compared with a thin-film mirror; it is an exponential in \(KV/kT\) with no critical size, and the mirror comparison is withdrawn. "Plastic deformation" as an erase route had no source.

The correction matters for the mapping. A latch cell of a few nanometres, two orders of magnitude below the single-domain size, means the \(KV\) limit is not the operative constraint in any bulk hard magnet. What limits a real magnet is the mesoscale step this file already listed as open: reversal nucleates or depins at grain boundaries at under a fifth of the anisotropy field, and even an ideal grain reaches only about 65 % of its ideal nucleation field. QSA has no buffer or barrier specification for that step.

Soft iron's high Curie temperature with low coercivity is consistent: order without a direction barrier.

### 4.7 Overall Confidence in the QSA Mapping

**High** — for the two-resource reading (exchange for order, anisotropy for direction), the zero-power hold, and the Curie threshold. The open item is larger than the first version implied: the coercivity of a real magnet is a mesoscale quantity that the mapping does not specify.

## Related entries

- [Superparamagnetism](superparamagnetism.md) — thermal loss of direction in a small grain
- [Ferromagnetic hysteresis](ferromagnetic-hysteresis.md) — the write / erase cycle; remanence and coercivity
- [Magnetic domains](magnetic-domains.md) — how a large body partitions the aligned population
- [Shape anisotropy](shape-anisotropy.md) — a barrier from sample geometry
- [Magnetostriction](magnetostriction.md) — lattice–moment coupling

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [NIST, 2022 CODATA recommended values, electron gyromagnetic ratio in MHz/T](https://physics.nist.gov/cgi-bin/cuu/Value?gammaebar) | full-text | The precession constant. |
| S2 | [Sagawa et al., *J. Appl. Phys.* 55, 2083 (1984)](https://doi.org/10.1063/1.333572) | abstract | Discovery paper: Curie temperature 585 K, first-report anisotropy, coercivity 960 kA/m, remanence 1.23 T, 290 kJ/m³. |
| S3 | [Miyake and Akai, *J. Phys. Soc. Jpn.* (2018), arXiv:1801.03455](https://arxiv.org/abs/1801.03455) | full-text | Curie temperature 585 K; exchange sets the Curie temperature, spin–orbit and crystal field set the anisotropy. |
| S4 | [Matsumoto and Akai, arXiv:1812.04842](https://arxiv.org/abs/1812.04842) | full-text | Curie temperatures computed from exchange constants; Fe 1043 K, Co 1394 K. |
| S5 | [Bance et al., *JOM* 67, 1350 (2015), arXiv:1603.08365](https://arxiv.org/abs/1603.08365) | full-text | Single-crystal anisotropy 4.30 MJ/m³ and polarization 1.613 T at 300 K (secondary; cites Hock 1988, not opened). |
| S6 | [Zickler et al., arXiv:1510.01958](https://arxiv.org/abs/1510.01958) | full-text | Anisotropy 4.9 MJ/m³, anisotropy field 7.65 T, polarization 1.61 T. |
| S7 | [Fischbacher et al., *Appl. Phys. Lett.* 111, 072404 (2017)](https://eprints.whiterose.ac.uk/136462/1/1.4999315.pdf) | full-text | A perfect cubic grain reaches 3.94 T against an ideal 6.09 T. |
| S8 | [Coey, "Materials for Spin Electronics", *Lecture Notes in Physics* 569, 277 (2001)](https://boulderschool.yale.edu/sites/default/files/files/coey_spintronics.pdf) | full-text | Curie temperature, anisotropy and magnetization of Fe, Co, Ni (secondary; cites Wijn 1991). |
| S9 | [Arnold Magnetic Technologies, Neodymium-Iron-Boron Magnet Grades catalogue (2019)](https://www.arnoldmagnetics.com/wp-content/uploads/2019/06/Arnold-Neo-Catalog.pdf) | full-text | Commercial Curie temperatures 310–350 °C; a second vendor table gives up to 380 °C. Tertiary. |
| S10 | [HyperPhysics, "Magnetic Properties of Ferromagnetic Materials"](https://hyperphysics.gsu.edu/hbase/Tables/magprop.html) | full-text | Coercivities of annealed iron, silicon steel and permalloys. Secondary; primary handbooks not opened. |
| S11 | [Shkuratov et al., *AIP Conf. Proc.* (2006), doi:10.1063/1.2263318](https://scholarsmine.mst.edu/min_nuceng_facwork/1196) | abstract | Transverse explosive shock at 22.3 GPa turns the hard ferromagnet into a weak magnet. |
| S12 | [Zhu et al., *Rare Metals* 41, 2353 (2022)](https://pure.bit.edu.cn/en/publications/relation-between-microstructure-and-magnetic-properties-of-shock-/) | abstract | Shock at 6.26–7.16 GPa demagnetizes sintered magnets by intergranular fracture; coercivity recoverable by annealing. |
| S13 | [Walton et al., *J. Cleaner Production* 104, 236 (2015)](https://research.birmingham.ac.uk/en/publications/the-use-of-hydrogen-to-separate-and-recycle-neodymiumironboron-ty/) | abstract | Hydrogen decrepitation gives a demagnetized hydrogenated powder. |
| S14 | [Goo, PhD thesis, Universität Stuttgart (2007), Table 4.1](https://elib.uni-stuttgart.de/server/api/core/bitstreams/39e8c606-9f04-48eb-a6e2-20b9e9c7d5b6/content) | full-text | Single-domain diameter 214 nm and anisotropy field 7.6 T (secondary; cites Gutfleisch et al. 2005). |
| S15 | [Dirba et al., *J. Magn. Magn. Mater.* 582, 171018 (2023)](https://www.mawi.tu-darmstadt.de/fm/outreach_fm/news_fm/news_fm_details_78848.en.jsp) | abstract | Calculated single-domain grain size about 200 nm, with coercivity peaking there. |
| S16 | [Kechrakos, "Magnetic Nanoparticle Assemblies", arXiv:0907.4417](https://arxiv.org/abs/0907.4417) | full-text | Néel–Arrhenius law, the blocking condition, attempt times, measurement windows. |
| S17 | [Wernsdorfer et al., *Phys. Rev. Lett.* 78, 1791 (1997)](https://doi.org/10.1103/PhysRevLett.78.1791) | abstract | Single-particle switching statistics agree with thermal activation over one barrier. |
| S18 | [University of Birmingham, Magnetic Materials Background 5: Properties](https://www.birmingham.ac.uk/Documents/college-eps/metallurgy/research/Magnetic-Materials-Background/Magnetic-Materials-Background-5-Properties.pdf) | full-text | Ni Curie point 358 °C; single-domain size about 300 nm. Secondary lecture notes. |
