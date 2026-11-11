---
id: ferroelectric-domains
title: Ferroelectric Domains (Partitioned Polar Alignment)
status: formal
family: latched-order
constraints:
  - spatial-buffer
  - energy-barrier
  - field-threshold
  - thermal
  - mechanical-lattice
confidence_data: medium
confidence_mapping: medium
review_depth: standard
related:
  - ferroelectric-remanence
  - magnetic-domains
  - piezoelectricity
  - ferromagnetic-hysteresis
  - superparamagnetism
  - shape-anisotropy
  - type-ii-critical-field
  - elasticity
updated: 2026-11-11
---

# Ferroelectric Domains (Partitioned Polar Alignment)

### 4.1 Effect Name

Ferroelectric domains (partitioned polar alignment)

### 4.2 Macroscopic Observation

On cooling through the Curie point a ferroelectric divides into regions of uniform polarization (domains) separated by thin walls. At zero applied field the net polarization can be far below the spontaneous value even though each domain is locally polar. An applied field nucleates and grows favourably oriented domains. A film with no free charge to compensate its surfaces forms fine stripe domains and has no net polarization. Wall positions are imaged and are static at rest: no continuous power is needed to hold a given partition.

### 4.3 Established Quantitative Boundaries

- **Measured.** Domains form on cooling through the Curie point, as regions with different orientations of the lower-symmetry structure [S12]. Walls are imaged by electron microscopy [S2][S5], electron holography [S3][S10] and x-ray scattering from periodic stripes [S8].
- **Convention.** Wall kinds in a tetragonal ferroelectric are named by the angle between the polarizations on either side: 180° and 90° [S1][S2]. A 180° wall lies parallel to the polarization because a wall carrying net bound charge is energetically unfavourable [S1].
- **Model (first-principles calculation).** Width of a 180° wall: of the order of one lattice constant in \(\mathrm{BaTiO_3}\) [S1]; one to two lattice constants for both 180° and 90° walls in \(\mathrm{PbTiO_3}\) [S2]. Measuring a 180° wall is harder than measuring a 90° wall [S2]; the width of 180° walls in a \(\mathrm{PbZr_{0.2}Ti_{0.8}O_3}\) film was measured by aberration-corrected microscopy, with the number not given in the abstract [S5]. No measured 180° wall width in \(\mathrm{BaTiO_3}\) was found.
- **Computed here.** With a cell of 0.40 nm (24 Å in six cells, from [ferroelectric-remanence](ferroelectric-remanence.md)), one to two lattice constants is 0.4–0.8 nm.
- **Measured.** Width of a 90° wall. \(\mathrm{PbTiO_3}\): 10 ± 3 Å, 15 ± 3 Å and 21 ± 7 Å in three microscopy studies [S2]. \(\mathrm{BaTiO_3}\): 20–50 Å by electron holography [S3]; 40–60 Å from microscopy combined with x-ray diffraction [S2]. In ceramics, 14 nm, an order of magnitude wider than in single crystals [S4].
- **Computed here.** In nanometres: 1.0, 1.5 and 2.1 nm (\(\mathrm{PbTiO_3}\)); 2–5 and 4–6 nm (\(\mathrm{BaTiO_3}\)). The measured range across crystals and ceramics is 1–14 nm.
- **Model (first-principles calculation).** Wall energy. \(\mathrm{PbTiO_3}\): 132 mJ m⁻² for the 180° wall and 35 mJ m⁻² for the 90° wall, with a very small barrier to motion of the 90° wall [S2]. \(\mathrm{BaTiO_3}\) 180° wall: 7.2–7.5 mJ m⁻² at zero temperature [S2] and 16 erg cm⁻² from a finite-temperature simulation [S1]. An experimental estimate for the \(\mathrm{PbTiO_3}\) 90° wall is 50 mJ m⁻² [S2].
- **Computed here.** The \(\mathrm{PbTiO_3}\) 180° wall costs 132/35 = 3.8 times the 90° wall. 16 erg cm⁻² is 16 mJ m⁻².
- **Measured.** Charged walls. Charged and uncharged 180° walls in a PZT film differ strongly in atomic structure [S5]. Charged walls in \(\mathrm{BaTiO_3}\) conduct steadily, with a metallic-type conductivity \(10^{9}\) times that of the surrounding crystal, attributed to a quasi-two-dimensional electron gas that compensates the bound charge [S6].
- **Computed here.** With \(P_s = 0.263\) C m⁻², a head-to-head 180° wall would carry \(2P_s = 0.53\) C m⁻² of bound charge and a head-to-head 90° wall \(\sqrt{2}P_s = 0.37\) C m⁻².
- **Measured.** Domains in thin films. \(\mathrm{PbTiO_3}\) films 12–420 Å thick on insulating \(\mathrm{SrTiO_3}\) (1.2–42 nm) form periodic 180° stripe domains [S8], and the polar phase is stable down to 3 unit cells (1.2 nm) [S7]. On conducting substrates the depolarizing field is compensated mainly by free charge; domain formation is the alternative [S4].
- **Measured.** Small crystals. Individual \(\mathrm{BaTiO_3}\) nanocubes hold a linearly ordered, monodomain polarization at nanometre dimensions and switch down to about 5 nm; particle shape and electrostatic boundary conditions set the extent of the ordered region [S10].
- **Measured.** Response to a field. Reversal is nucleation at an electrode, forward growth, then slower sideways growth of domains. A domain written by a voltage pulse grows logarithmically with pulse length beyond 20 µs, and wall velocity varies continuously with field. Models use an activation field for nucleation or a broad distribution of waiting times [S4]. In 5–30 nm \(\mathrm{BaTiO_3}\) capacitors wall motion is strongly suppressed and a depolarizing field comparable to the coercive field re-forms domains within 10–500 µs [S11]. No opened source gives a field at which the last wall is removed.
- **Convention.** Holding a static domain pattern costs zero continuous power: it is a static configuration. Moving walls around a loop dissipates the loop area, which is owned by [ferroelectric-remanence](ferroelectric-remanence.md).

**Data confidence:** Medium. That domains and walls exist, that 90° walls are 1–5 nm wide in crystals, and that unscreened films form stripes down to 1.2 nm are measured. The 180° wall width and all wall energies are calculations. The holography, charged-wall, PZT-film and nanocrystal papers were opened as abstracts only, and the \(\mathrm{PbTiO_3}\) 90° widths are quoted from a paper that cites the measurements. No domain period and no saturation field were found.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Bound charge on a wall:

  \[
  \sigma_b = (\mathbf{P}_2 - \mathbf{P}_1)\cdot\hat{\mathbf{n}}
  \]

  Zero for a 180° wall parallel to \(\mathbf{P}\); of order \(2P_s\) for a head-to-head wall. Uncompensated \(\sigma_b\) produces a depolarizing field of the same kind as the slab field on the remanence entry.

- Continuum (Landau–Ginzburg) descriptions of the wall take gradient and Landau coefficients estimated from experiment; their use for atomically sharp walls is questionable [S2].

- Partitioning lowers the electrostatic and elastic cost of a uniformly polarized body and adds wall area times wall energy. In a film this gives a stripe period that depends on thickness (Kittel law, derived for magnetic films and carried over to ferroelectrics) [S9]. No measured period is filed.

- The term \(-\mathbf{E}\cdot\mathbf{P}\) favours one set of domains over another under an applied field.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two nested buffers:
  1. **Wall.** A transition strip between adjacent polar directions: about one lattice constant (0.4 nm) by calculation for a 180° wall, 1–5 nm measured for 90° walls in crystals, 14 nm in ceramics. A charged wall needs in addition a supply of compensating carriers.
  2. **Domain pattern.** Set by the electrical boundary, not by a size. With free charge at the surfaces a body can be one domain at any thickness measured, including a 5 nm crystal. Without it, stripes form in films as thin as 1.2 nm. The period depends on the film thickness; no value is filed.

- **Clock rate / latency.** Pattern changes are nucleation and wall-motion events under an applied or residual field: sideways wall growth is the slow stage, written domains grow logarithmically in time, and an unscreened pattern re-forms within 10–500 µs. A static pattern has no ongoing clock cost.

- **Energy barriers or thresholds.** Each domain is the polar well of [ferroelectric-remanence](ferroelectric-remanence.md). The wall energy per area is the cost of a partition: 7–16 mJ m⁻² (\(\mathrm{BaTiO_3}\) 180°), 35 and 132 mJ m⁻² (\(\mathrm{PbTiO_3}\) 90° and 180°), all calculated. Pinning of walls is the barrier that appears as \(E_c\) on the loop. Holding a static partition costs zero continuous power.

- **Dominant failure modes.**
  - **Threshold** — Curie point: above \(T_C\) the polar phase and the domains are gone. A phase transition.
  - **Crossover** — screening: whether a body is one domain or many depends continuously on how much of its bound surface charge is compensated. No single-domain size was found; stripes occur down to 1.2 nm and monodomain crystals at 5 nm.
  - **Crossover** — applied field: reversal is nucleation and growth with a distribution of waiting times; wall velocity varies continuously with field. No sharp field for removing the last wall is reported.
  - **Crossover** — relaxation: with a residual depolarizing field comparable to \(E_c\), a poled film returns to a multidomain state within 10–500 µs in the measured capacitors.
  - **Crossover** — mechanical damage: acts through pinning and strain at 90° walls; no measured scale filed.

- **Emergent constant or stable output.** A static partition of the polar population with walls of finite width and a net polarization anywhere from zero (stripes) to the spontaneous value (one domain), at zero continuous power while the pattern is at rest. A 90° wall also changes the strain across it.

### 4.6 Internal Consistency Notes

Domains are many polar wells sharing a body, with walls as the finite-width boundaries. Zero hold power on a static pattern and dissipation only when walls move fit the family.

Sourcing changed the picture in six places. The 180° wall width was presented as imaged in \(\mathrm{BaTiO_3}\); it is a calculation, and the opened measurements are of 90° walls. The first version said 90° walls cost more energy; the calculated \(\mathrm{PbTiO_3}\) energies are the other way round by a factor of 3.8. The single-domain size was called a cliff with a \(\mathrm{BaTiO_3}\) class of "10 nm to tens of nm"; no such size was found, and the outcome follows the screening. Field expulsion of walls was called a sharp collapse; the sources describe nucleation, field-dependent wall motion and waiting-time distributions. Statements that walls thicken near \(T_C\) and that an optical beam can move walls had no opened source and were removed. And the comparisons with the magnetic entry were stale:

| | Magnetic domains | Ferroelectric domains |
|---|---|---|
| Wall width | 3.6–82 nm by formula; 4–9 nm measured in \(\mathrm{Nd_2Fe_{14}B}\) | about 0.4 nm calculated (180°); 1–5 nm measured (90°, crystals); 14 nm (ceramics) |
| Inputs to the width | exchange stiffness (inferred, two tabulations differ by 2.4×) and \(K_1\) | first-principles calculation; continuum coefficients are rough estimates |
| Single-domain condition | crossover with a shape-dependent prefactor: 12–25 nm in Fe, 0.2–0.4 µm in \(\mathrm{Nd_2Fe_{14}B}\) | no size; set by screening of the bound charge |
| Field response | walls unpin at \(H_c\), rotation follows; no sharp saturation reported | nucleation and growth; no sharp saturation reported |
| Small-grain limit | [superparamagnetism](superparamagnetism.md): retention-time crossover | no thermal criterion found; depolarization instead |

The measured wall widths of the two families overlap: 4–9 nm in a hard magnet against 1–14 nm in ferroelectrics, so the earlier instruction not to carry magnetic "tens of nanometres" over does not hold as a general contrast. What differs is free charge: nothing compensates the surface poles of a magnetic body, so it partitions above its single-domain size, while a ferroelectric with good electrodes need not partition at all.

The mapping is not closed on pattern selection. Which wall types and what period a sample shows is an electrostatic, elastic and pinning problem whose output is imaged and is not derived here. Wall pinning as the origin of \(E_c\) is the same open item as on the remanence entry.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — nanometre wall widths, stripe domains in unscreened films and zero hold power are sourced; the 180° width and all wall energies are calculated, and pattern choice and pinning remain without a closed specification.

## Related entries

- [ferroelectric-remanence](ferroelectric-remanence.md) — the polar well of which each domain is a copy; owns net \(P_r\), the loop and the thin-film depolarizing field
- [magnetic-domains](magnetic-domains.md) — magnetic counterpart; comparison table in §4.6
- [piezoelectricity](piezoelectricity.md) — strain coupled to polarization; 90° walls change strain
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — magnetic loop; walls unpin at the coercive field and rotation follows
- [superparamagnetism](superparamagnetism.md) — thermal loss of direction in a small magnetic grain; no polar equivalent was found
- [shape-anisotropy](shape-anisotropy.md) — demagnetizing factors of a magnetic body; the polar analogue is the slab depolarizing field
- [type-ii-critical-field](type-ii-critical-field.md) — vortex lattice: a partition in `gapped-coherence`
- [elasticity](elasticity.md) — the strain that 90° walls change

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Padilla, Zhong and Vanderbilt, *Phys. Rev. B* 53, R5969 (1996)](https://www.physics.rutgers.edu/~dhv/pubs/local_copy/jp_dw.pdf) | full-text | Calculated BaTiO3 180° wall: width of the order of a lattice constant; energy 16 erg/cm²; neutral walls lie parallel to the polarization. |
| S2 | [Meyer and Vanderbilt, *Phys. Rev. B* 65, 104111 (2002), arXiv:cond-mat/0109257](https://arxiv.org/abs/cond-mat/0109257) | full-text | Calculated PbTiO3 walls: widths of one to two lattice constants; 132 and 35 mJ/m²; BaTiO3 7.2–7.5 mJ/m². Secondary for the measured 90° widths (10 ± 3, 15 ± 3, 21 ± 7 Å in PbTiO3; 40–60 Å in BaTiO3) and the 50 mJ/m² estimate. |
| S3 | [Zhang and Joy, MRS Online Proceedings Library (1993)](https://www.cambridge.org/core/journals/mrs-online-proceedings-library-archive/article/electron-holographic-characterization-of-ferroelectric-thin-films/FAD472927F071C931628E39755872EB6) | abstract | Electron holography: 90° wall width of 20–50 Å in BaTiO3. |
| S4 | [Dawber, Rabe and Scott, *Rev. Mod. Phys.* 77, 1083 (2005), arXiv:cond-mat/0503372](https://arxiv.org/abs/cond-mat/0503372) | full-text | Standard review: 90° walls 14 nm wide in ceramics and earlier wide-wall claims; switching stages, written-domain growth, wall velocity against field, switching models; compensation by free charge or by domains. |
| S5 | [Jia et al., *Nature Mater.* 7, 57 (2008)](https://www.nature.com/articles/nmat2080) | abstract | Aberration-corrected microscopy of 180° walls in a PZT film; charged and uncharged walls differ. |
| S6 | [Sluka, Tagantsev, Bednyakov and Setter, *Nature Commun.* 4, 1808 (2013)](https://doi.org/10.1038/ncomms2839) | abstract | Charged walls in BaTiO3 conduct at 10⁹ times the bulk conductivity through a compensating electron gas. |
| S7 | [Fong et al., *Science* 304, 1650 (2004)](https://doi.org/10.1126/science.1098252) | abstract | PbTiO3 polar phase stable down to 3 unit cells (1.2 nm). |
| S8 | [Lichtensteiger, Triscone, Junquera and Ghosez, *Phys. Rev. Lett.* 94, 047603 (2005), arXiv:cond-mat/0404228](https://arxiv.org/abs/cond-mat/0404228) | full-text | Secondary: periodic 180° stripe domains in 12–420 Å PbTiO3 films on insulating SrTiO3, seen by x-ray scattering. |
| S9 | [Liu, Chen, Wang and Zheng, *Materials* 7, 6502 (2014)](https://doi.org/10.3390/ma7096502) | full-text | Review: Kittel law of domain period against film thickness and its extension to ferroelectrics. |
| S10 | [Polking et al., *Nature Mater.* 11, 700 (2012)](https://doi.org/10.1038/nmat3371) | abstract | Monodomain polarization in individual BaTiO3 nanocubes; switching down to about 5 nm; role of shape and boundary conditions. |
| S11 | [Kim et al., *Phys. Rev. Lett.* 95, 237602 (2005), arXiv:cond-mat/0506480](https://arxiv.org/abs/cond-mat/0506480) | full-text | 5–30 nm BaTiO3 capacitors: suppressed wall motion; depolarizing field comparable to the coercive field re-forms domains between 10 and 500 µs. |
| S12 | [Aksel and Jones, *Sensors* 10, 1935 (2010)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3264460/) | full-text | Secondary review: domains and walls form on cooling through the Curie point. |
