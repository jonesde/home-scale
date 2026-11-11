---
id: shape-anisotropy
title: Shape Anisotropy (Geometry Barrier)
status: formal
family: latched-order
constraints:
  - energy-barrier
  - spatial-buffer
  - field-threshold
  - thermal
confidence_data: high
confidence_mapping: medium
review_depth: deep
related:
  - permanent-magnet-latch
  - ferromagnetic-hysteresis
  - magnetic-domains
  - superparamagnetism
  - magnetostriction
  - ferroelectric-remanence
updated: 2026-11-11
---

# Shape Anisotropy (Geometry Barrier)

### 4.1 Effect Name

Shape anisotropy (geometry barrier)

### 4.2 Macroscopic Observation

An elongated particle of a high-magnetization ferromagnet remains magnetized along its long axis after the applied field is removed, even when the crystal anisotropy \(K_1\) is small, and its coercive force rises with elongation. A sphere of the same material has no preferred axis from geometry. Thin films of soft magnets lie in-plane; ultrathin films with a strong interface anisotropy magnetize perpendicular to the plane. Alnico magnets hold their remanence in elongated Fe–Co precipitates inside a non-magnetic matrix, and the magnets themselves are made in elongated shapes.

### 4.3 Established Quantitative Boundaries

- **Convention.** Demagnetizing factors of a uniformly magnetized ellipsoid (exact magnetostatics). The three factors are positive and sum to 1. Sphere: 1/3 on every axis. Infinite wire: 1/2, 1/2, 0. Disk or thin film: 0, 0, 1 [S1]. Formulas and tables for the general ellipsoid are Osborn's [S2].
- **Convention.** Shape-anisotropy density of a body of revolution: \(K_\mathrm{shape} = (\mu_0/2)M_s^2\,\Delta N\) with \(\Delta N = N_t - N_l\), the transverse minus the long-axis factor [S3]. The same quantity is written \(\tfrac{1}{4}\mu_0M_s^2(1 - 3N_l)\), with maximum \(\tfrac{1}{4}\mu_0M_s^2\) for a needle [S4].
- **Computed here.** \(\Delta N\) of a prolate spheroid, from the long-axis formula in §4.4 [S2]: 0.240 at aspect ratio 2, 0.416 at 5, 0.470 at 10, against the needle limit 0.5. That is 48 %, 83 % and 94 % of the limit. It is zero at aspect ratio 1.
- **Measured.** Saturation polarization \(\mu_0M_s\) at room temperature, from handbook tabulations. Fe: 2.15 T [S5], 1.71 MA/m [S6], 21.4 kG [S7], 2.16 T for polycrystalline iron [S8]. Ni: 0.61–0.62 T [S5], 0.49 MA/m [S6], 6.1 kG [S7].
- **Computed here.** Magnetostatic scale \((\mu_0/2)M_s^2 = J_s^2/2\mu_0\) with \(J_s = \mu_0M_s\). Fe (2.15 T): 1.84 MJ/m³. Ni (0.61–0.62 T): 0.15 MJ/m³, 12 times smaller. \(\mathrm{Nd_2Fe_{14}B}\) (1.61 T): 1.03 MJ/m³. The needle maximum of \(K_\mathrm{shape}\) for Fe is half the scale, 0.92 MJ/m³; at aspect ratios 2, 5 and 10 it is 0.44, 0.77 and 0.86 MJ/m³.
- **Measured.** Crystal anisotropy \(K_1\), extracted from magnetization curves. Fe: 0.048–0.05 MJ/m³ [S6][S5]. Hard ferrites: 0.32–0.36 MJ/m³ [S5][S9]. \(\mathrm{Nd_2Fe_{14}B}\): 4.3–4.9 MJ/m³ [S4][S5]. \(\mathrm{SmCo_5}\): 17.2 MJ/m³, one source [S5].
- **Computed here.** The Fe needle maximum of 0.92 MJ/m³ is 18 times iron's own \(K_1\) (0.05) and 2.6–2.9 times a hard ferrite's. It is 4.7–5.3 times below \(\mathrm{Nd_2Fe_{14}B}\) and 19 times below \(\mathrm{SmCo_5}\).
- **Model (hardness parameter \(\kappa = \sqrt{K/\mu_0M_s^2}\)).** The maximum shape anisotropy gives \(\kappa = 0.5\). A magnet that can be made in any shape needs \(\kappa > 1\); \(\mathrm{Nd_2Fe_{14}B}\) has 1.54 [S4][S5]. Alnico magnets need a magnet shape that keeps the demagnetizing field below the coercive field [S4].
- **Measured.** Elongated single-domain iron particles. Particles 150 Å in diameter with a median length-to-diameter ratio of 3:1 have an intrinsic coercive force of 1600 Oe before packing [S10]. Coercive forces above 2000 Oe were measured, with a direct correlation between coercive force and elongation [S11]. Particles of 130–305 Å reverse by a non-coherent mode closest to chain-of-spheres fanning [S12]. The coercive force predicted for shape anisotropy "frequently far exceeds the observed value" [S13].
- **Computed here.** The coherent-rotation field of an infinite Fe needle is \(M_s/2\), 10.7 kOe from \(4\pi M_s = 21.4\) kG [S7]. The measured 1600 and 2000 Oe are 15 % and 19 % of it. In SI they are 127 and 159 kA/m; 127 kA/m is \(1.3\times10^{3}\) to \(1.3\times10^{4}\) times the 10–100 A/m of bulk polycrystalline iron [S8].
- **Model (two-term fit of coercivity against temperature).** In acicular \(\gamma\text{-}\mathrm{Fe_2O_3}\) particles of aspect ratio 5:1 and lengths 2000 and 6000 Å, the shape term accounts for about 67 % of the room-temperature coercive force [S14].
- **Measured.** Alnico. The coercivity is carried by elongated Fe–Co-rich rods in a continuous non-magnetic Ni–Al-rich matrix, formed by spinodal decomposition [S15][S4]. Typical rod diameters are 40–50 nm [S16]. In one alnico-8-type alloy the intrinsic coercivity is 35 Oe, 476 Oe after magnetic annealing and 1707 Oe after draw [S15].
- **Model (micromagnetic nucleation theory).** Reversal is coherent only below a coherence radius of about five exchange lengths, independent of \(K_1\) [S5]; the tabulated coherence radii are 7.4 nm (Fe), 9.7 nm (Co) and 16 nm (Ni) [S6]. The coherent diameter for alnico rods is about 20 nm, so 40–50 nm rods start to reverse by curling and do not reach the Stoner–Wohlfarth limit; the authors call the pure shape-anisotropy reading of alnico simplistic [S16]. Above the critical size the curling coercive force falls as \(1/R^2\) [S17].
- **Measured.** Cobalt nanorods of 28, 20 and 11 nm diameter have coercive fields of 0.36, 0.47 and 0.61 T [S3].
- **Model (film demagnetizing term against anisotropy).** A film magnetizes perpendicular to its plane when \(K > \mu_0M_s^2/2\), that is \(Q = 2K/\mu_0M_s^2 > 1\), and in-plane otherwise [S3]. In CoFeB/MgO with measured interface anisotropy 0.49 mJ/m² (as deposited) and 1.4 mJ/m² (annealed), the in-plane term is expected to win above a CoFeB thickness of 1.23 nm and 1.39 nm [S18].
- **Measured.** Ta- and Mo-capped MgO/CoFeB films annealed at 300 °C are perpendicular up to a CoFeB thickness of 1.5 nm [S19].
- **Measured.** Curie temperatures, where \(M_s\) and the barrier vanish: Fe 1044 K, Ni 628 K [S5].
- **Measured.** Precession scale: \(\gamma/2\pi = 28.025\) GHz/T (CODATA 2022, free electron) [S20].
- **Convention.** Thermal stability. For a measurement lasting about 100 s a particle counts as superparamagnetic when its barrier is below \(25\,k_BT\) [S21]; here the barrier is \(K_\mathrm{shape}V\). Sizes are filed in [superparamagnetism](superparamagnetism.md).
- **Convention.** Holding the long-axis remanent state costs zero continuous power: it is a static configuration, and no source reports a dissipation at rest.

**Data confidence:** High — the demagnetizing factors are exact magnetostatics and \(M_s\) of Fe and Ni agrees across four tabulations. Medium for the measured coercivities: the elongated-iron and \(\gamma\text{-}\mathrm{Fe_2O_3}\) papers were opened as abstracts only, and the alnico values are one alloy. The spheroid formula behind the \(\Delta N\) values rests on Osborn's paper, opened as an abstract only; its limits are confirmed in [S1]. \(K_1\) of \(\mathrm{SmCo_5}\) has one source. No opened source gives an effective anisotropy constant for alnico.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Uniform-ellipsoid demagnetizing field: \(\mathbf{H}_d = -\mathsf{N}\cdot\mathbf{M}\), with \(\mathrm{tr}\,\mathsf{N} = 1\) [S1].
- Magnetostatic energy density:

  \[
  u_d = \frac{\mu_0}{2}\,\mathbf{M}\cdot\mathsf{N}\cdot\mathbf{M}
  \]

- Uniaxial shape-anisotropy density along the long axis of a prolate body [S3][S4]:

  \[
  K_\mathrm{shape} = \frac{\mu_0}{2}M_s^2\,(N_t - N_l) = \frac{\mu_0}{4}M_s^2\,(1 - 3N_l)
  \]

- Prolate spheroid of aspect ratio \(m\) [S2]:

  \[
  N_l = \frac{1}{m^2 - 1}\left[\frac{m}{\sqrt{m^2 - 1}}\ln\!\left(m + \sqrt{m^2 - 1}\right) - 1\right],\qquad N_t = \frac{1 - N_l}{2}
  \]

  \(N_t - N_l\) is a continuous function of \(m\): 0 at \(m = 1\) and 1/2 as \(m \to \infty\).

- Coherent-rotation nucleation field with both terms: \(H_N = 2K_1/(\mu_0M_s) + \tfrac{1}{2}(1 - 3N_l)M_s\) [S5]. For rods at packing fraction \(p\) in a non-magnetic matrix, \(H_c = (1 - p)(N_t - N_l)M_s\) [S16].
- Curling above the critical radius: \(H_c = 6.78\,A/(I_sR^2)\) in the notation of the paper, with \(I_s\) the saturation magnetization [S17].
- Thin film: an out-of-plane magnetization pays \((\mu_0/2)M_s^2\); perpendicular magnetization needs \(K > \mu_0M_s^2/2\) [S3]. With an interface anisotropy \(K_i\) per unit area the two terms are equal at \(t_c = 2K_i/(\mu_0M_s^2)\) [S18].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A ferromagnetic body with nonzero \(\Delta N\). For the barrier to act as one cell the body must also be thinner than the coherent diameter (about 20 nm for alnico's Fe–Co rods; coherence radii of 7–16 nm in Fe, Co and Ni) and large enough to pass the thermal cut ([superparamagnetism](superparamagnetism.md)). The latch cell is the particle or precipitate. A sphere has no geometry barrier at any size.

- **Clock rate / latency.** Same carrier as the parent latch, 28.025 GHz/T. Write latency is set by the field sweep and by the reversal mode: coherent rotation below the coherence radius, curling above it, fanning in chains of particles. Geometry changes the barrier and leaves the carrier unchanged.

- **Energy barriers or thresholds.** The barrier is magnetostatic and geometric, \(\Delta N\,(\mu_0/2)M_s^2\,V\), at most 0.92 MJ/m³ times the volume in iron. No large \(K_1\) is required: that maximum is 18 times iron's own \(K_1\). It is 5 to 19 times below a rare-earth \(K_1\), so shape alone supplies a semi-hard latch (\(\kappa \le 0.5\)). Measured switching fields of elongated iron particles reach 15–19 % of the ideal needle field. Holding the long-axis state costs zero continuous power.

- **Dominant failure modes.**
  - **Crossover** — geometry: \(\Delta N\) is a continuous function of aspect ratio, 0 at 1, 0.240 at 2, 0.416 at 5, 0.470 at 10, with limit 0.5. The barrier goes to zero continuously as the body approaches a sphere, and half the needle limit is already reached near aspect ratio 2.
  - **Crossover** — thickness: above the coherent diameter reversal is by curling, and the model coercive force falls as \(1/R^2\). Measured cobalt nanorods lose coercivity with diameter, from 0.61 T at 11 nm to 0.36 T at 28 nm. Larger bodies support walls ([magnetic-domains](magnetic-domains.md)).
  - **Crossover** — thermal, volume: the relaxation time is exponential in \(K_\mathrm{shape}V/k_BT\); the cut at \(25\,k_BT\) is the convention for a 100 s measurement. Sizes are in [superparamagnetism](superparamagnetism.md).
  - **Threshold** — Curie point: the barrier goes as \(M_s^2\) and vanishes with \(M_s\) at \(T_C\) (Fe 1044 K, Ni 628 K). A phase transition. Between materials the dependence on \(M_s\) is continuous: the Ni scale is 12 times below the Fe scale.
  - **Crossover** — field: a reverse field writes the opposite long-axis state. The ideal value is \((N_t - N_l)M_s\); measured values in elongated iron are 15–19 % of it, and reversal depends on sweep rate and temperature as on [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md).
  - **Threshold** — film reorientation: a film with interface anisotropy switches between perpendicular and in-plane magnetization at the thickness where \(K_i/t\) equals \(\mu_0M_s^2/2\), about 1.2–1.5 nm for CoFeB/MgO. The critical thickness is system-specific.

- **Emergent constant or stable output.** A uniaxial remanent direction locked to the long axis of a particle, or to the plane of a film, at zero continuous power and without a large magnetocrystalline \(K_1\).

### 4.6 Internal Consistency Notes

The barrier is the \(\Delta N\) term, and it accounts for a low-\(K_1\) metal holding remanence as a needle: the Fe needle maximum is 18 times iron's crystal \(K_1\), and elongated iron particles hold 127–159 kA/m against 10–100 A/m in bulk. \(\mathrm{Nd_2Fe_{14}B}\) does not need shape: its \(K_1\) of 4.3–4.9 MJ/m³ exceeds its magnetostatic scale of 1.03 MJ/m³ (\(\kappa = 1.54\)). Alnico sits on this file, with the qualifier below. Sintered Nd-Fe-B sits on [permanent-magnet-latch](permanent-magnet-latch.md).

Sourcing changed six things. First, the aspect-ratio failure is a continuous zero. The first version called \(\Delta N = 0\) a sharp collapse; \(\Delta N\) is already 0.240 at aspect ratio 2. Second, the comparison with hard magnets was wrong. The first version put the Fe magnetostatic scale at the same order as a hard-magnet \(K_1\); the needle maximum is 0.92 MJ/m³ against 4.3–4.9 for \(\mathrm{Nd_2Fe_{14}B}\) and 17.2 for \(\mathrm{SmCo_5}\), only hard ferrite lies below it, and shape alone gives \(\kappa \le 0.5\). Third, the Ni scale is 12 times below the Fe scale; the first version said several times. Fourth, alnico needs a qualifier: its rods of 40–50 nm exceed the coherent diameter of about 20 nm, reversal starts by curling, the Stoner–Wohlfarth limit is not reached, and the magnet also needs a favourable outer shape. Fifth, real elongated iron particles reverse by fanning and reach 15–19 % of the ideal needle field; the first version listed curling and buckling and gave no measured value. Sixth, the bulk-iron coercivity it quoted, \(10^2\)–\(10^3\) A/m, is the soft/hard class boundary; polycrystalline iron is 10–100 A/m.

The uniform ellipsoid is an idealization. Real particles and precipitates are not uniformly magnetized, and above the coherence radius they do not reverse coherently, so \(\Delta N\) does not predict the measured switching field. This is the same mesoscale \(H_c\) gap as on the hysteresis file. Shape and crystal anisotropy add when both are present (the nucleation field in §4.4 carries both terms); this entry owns the \(\Delta N\) term only.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the demagnetizing factors, the sphere, needle and film limits and the \(M_s^2\) scale are exact or well measured and give the geometry barrier, but the measured write field is 15–19 % of the mapped barrier field in the cleanest example, and alnico reverses by a mode the uniform-ellipsoid picture excludes. Lowered from High when the file was sourced.

## Related entries

- [permanent-magnet-latch](permanent-magnet-latch.md) — crystal-\(K_1\) latch; this file is the geometry alternative
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — the write / erase cycle whose barrier may be this \(\Delta N\)
- [magnetic-domains](magnetic-domains.md) — magnetostatic energy that, in a large body, is spent on walls instead of a single-domain shape latch
- [superparamagnetism](superparamagnetism.md) — thermal relaxation with \(K\) equal to \(K_\mathrm{shape}\); owns the sizes
- [magnetostriction](magnetostriction.md) — strain that can change effective shape and add a magnetoelastic term
- [ferroelectric-remanence](ferroelectric-remanence.md) — polar analog of the geometry cost is slab depolarization, a clause on that latch, not a second file

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Tannous and Gieraltowski, "The Stoner-Wohlfarth model of ferromagnetism: static properties", arXiv:physics/0607117 (2008)](https://arxiv.org/abs/physics/0607117) | full-text | Demagnetizing coefficients sum to 1; sphere 1/3; disk 0, 0, 1; infinite wire 1/2, 1/2, 0 (secondary for the limits). |
| S2 | [Osborn, *Phys. Rev.* 67, 351 (1945)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.67.351) | abstract | Standard primary for ellipsoid demagnetizing factors. The abstract carries no numbers, so the prolate-spheroid formula used for the computed values was not read in it. |
| S3 | [Fischbacher et al., *J. Phys. D* 51, 193002 (2018), arXiv:1903.11922](https://arxiv.org/abs/1903.11922) | full-text | Shape-anisotropy formula; thin-film criterion and quality factor; cobalt nanorod coercive fields (reporting Ener et al.). |
| S4 | [Coey, *Engineering* 6, 119 (2020)](https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2018.11.034) | full-text | Shape anisotropy of an ellipsoid of revolution and its maximum; hardness parameter 0.5 for shape alone and 1.54 for Nd2Fe14B; Nd2Fe14B anisotropy 4.3 MJ/m³; alnico nanostructure and its need for a special magnet shape. |
| S5 | [Skomski, "Micromagnetic Spin Structure", in *Spin Electronics*, Lecture Notes in Physics 569, 204 (2001)](https://boulderschool.yale.edu/sites/default/files/files/heinonen_skomski.pdf) | full-text | Polarization, Curie temperature and anisotropy of Fe, Ni, BaFe12O19, Nd2Fe14B, SmCo5; hardness parameter; nucleation field with the shape term; coherence radius of about five exchange lengths. |
| S6 | [Coey, "Materials for Spin Electronics", in *Spin Electronics*, Lecture Notes in Physics 569, 277 (2001)](https://boulderschool.yale.edu/sites/default/files/files/coey_spintronics.pdf) | full-text | Magnetization and anisotropy of Fe and Ni (1.71 and 0.49 MA/m; 48 kJ/m³); coherence radii of Fe, Co, Ni. |
| S7 | [Dubowik and Gościańska, arXiv:1306.5988 (2014), Table I](https://arxiv.org/abs/1306.5988) | full-text | 4πM of 21.4 kG for Fe and 6.1 kG for Ni (cited there to O'Handley 1999, not opened). |
| S8 | [Fiorillo, Bertotti, Appino and Pasquale, "Soft Magnetic Materials", *Wiley Encyclopedia of Electrical and Electronics Engineering* (2016), accepted version](https://iris.inrim.it/bitstream/11696/54676/4/SoftMagneticMaterials_Wiley_Enciclopedia_2016_postprint.pdf) | full-text | Review chapter. Polycrystalline iron: polarization 2.16 T, coercivity 10–100 A/m. |
| S9 | [Granados-Miralles and Jenuš, *J. Phys. D* 54, 303001 (2021)](https://iopscience.iop.org/article/10.1088/1361-6463/abfad4) | full-text | Hard-ferrite anisotropy: 0.32–0.33 MJ/m³ (Ba), 0.35–0.36 MJ/m³ (Sr). Read through a fetch tool, not checked against the raw page. |
| S10 | [Mendelsohn, Luborsky and Paine, *J. Appl. Phys.* 26, 1274 (1955)](https://pubs.aip.org/jap/article/26/10/1274/160656/Permanent-Magnet-Properties-of-Elongated-Single) | abstract | Elongated iron particles: 150 Å diameter, 3:1, 1600 Oe before packing. |
| S11 | [Paine, Mendelsohn and Luborsky, *Phys. Rev.* 100, 1055 (1955)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.100.1055) | abstract | Coercive forces above 2000 Oe in elongated iron; correlation of coercive force with elongation. |
| S12 | [Luborsky, *J. Appl. Phys.* 32, S171 (1961)](https://pubs.aip.org/jap/article/32/3/S171/506552/Development-of-Elongated-Particle-Magnets) | abstract | Particles of 130–305 Å reverse by a non-coherent mode closest to chain-of-spheres fanning. |
| S13 | [Jacobs and Bean, *Phys. Rev.* 100, 1060 (1955)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.100.1060) | abstract | The coercive force predicted for shape anisotropy frequently far exceeds the observed value. |
| S14 | [Eagle and Mallinson, *J. Appl. Phys.* 38, 995 (1967)](https://pubs.aip.org/jap/article/38/3/995/693084/On-the-Coercivity-of-Fe2O3-Particles) | abstract | Acicular γ-Fe2O3, 5:1, lengths 2000 and 6000 Å: shape term about 67 % of the room-temperature coercive force. |
| S15 | [Zhou et al., arXiv:1810.12580 (2018)](https://arxiv.org/abs/1810.12580) | full-text | Alnico microstructure (Fe–Co-rich rods in a Ni–Al-rich matrix by spinodal decomposition); intrinsic coercivity 35, 476 and 1707 Oe. |
| S16 | [Ke et al., "Simulation of alnico coercivity", arXiv:1707.04180 (2017)](https://arxiv.org/abs/1707.04180) | full-text | Rod diameters 40–50 nm against a coherent diameter of about 20 nm; reversal by curling; Stoner–Wohlfarth limit not reached; coercivity formula with packing fraction. |
| S17 | [Frei, Shtrikman and Treves, *Phys. Rev.* 106, 446 (1957)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.106.446) | abstract | Curling against rotation in unison; curling coercive force falling as the inverse square of the radius. |
| S18 | [Yamanouchi et al., *IEEE Magn. Lett.* 2, 3000304 (2011), arXiv:1202.5128](https://arxiv.org/abs/1202.5128) | full-text | CoFeB/MgO interface anisotropy 0.49 and 1.4 mJ/m²; in-plane shape term expected to win above 1.23 and 1.39 nm. |
| S19 | [Liu, Zhang, Cai and Pan, *Sci. Rep.* 4, 5895 (2014)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4118150/) | full-text | Perpendicular magnetization up to 1.5 nm of CoFeB under Ta or Mo caps after a 300 °C anneal. Read through a fetch tool, not checked against the raw page. |
| S20 | [NIST, CODATA 2022 recommended value, electron gyromagnetic ratio in MHz/T](https://physics.nist.gov/cgi-bin/cuu/Value?gammaebar) | full-text | 28 024.951 MHz/T. |
| S21 | [Kachkachi, arXiv:cond-mat/0307457 (2003)](https://arxiv.org/abs/cond-mat/0307457) | full-text | Superparamagnetic range is a barrier below 25 kT for a measuring time of about 100 s. |
