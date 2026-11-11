---
id: ferroelectric-remanence
title: Ferroelectric Remanence (Polar Latch)
status: formal
family: latched-order
constraints:
  - energy-barrier
  - field-threshold
  - thermal
  - spatial-buffer
  - mechanical-lattice
confidence_data: high
confidence_mapping: medium
review_depth: standard
related:
  - permanent-magnet-latch
  - ferromagnetic-hysteresis
  - superparamagnetism
  - ferroelectric-domains
  - piezoelectricity
  - refraction-dielectric
  - dielectric-breakdown
updated: 2026-11-11
---

# Ferroelectric Remanence (Polar Latch)

### 4.1 Effect Name

Ferroelectric remanence (polar latch)

### 4.2 Macroscopic Observation

A ferroelectric crystal or ceramic, after a large electric field is applied and removed, retains a remanent polarization \(P_r\). The sample stays poled at zero applied field and zero continuous power. A reverse field of the size of the coercive field \(E_c\) switches the polarization. Heating through the Curie point removes the polar phase. A film thin enough that its bound surface charge is not compensated loses its net polarization while the polar phase itself can remain. A linear dielectric polarizes in a field and returns to \(P = 0\) when the field is removed.

### 4.3 Established Quantitative Boundaries

- **Measured.** Curie points. \(\mathrm{BaTiO_3}\): 120 °C, with 120–130 °C quoted depending on crystal growth [S1][S2]. \(\mathrm{PbTiO_3}\): 760 K, one tertiary source [S3]. Commercial PZT grades: 195 °C (PZT5H), 300 °C (PZT8), 320 °C (PZT4), 365 °C (PZT5A) [S4]. Congruent \(\mathrm{LiNbO_3}\): reported from 1413 to 1475 K. \(\mathrm{LiTaO_3}\): reported from 874 to 958 K [S5].
- **Computed here.** 120 °C is 393 K; 760 K is 487 °C; the PZT range of 195–365 °C is 468–638 K; \(\mathrm{LiNbO_3}\) is 1140–1202 °C and \(\mathrm{LiTaO_3}\) 601–685 °C.
- **Measured.** \(\mathrm{BaTiO_3}\) has four polymorphs: cubic, tetragonal, orthorhombic and rhombohedral from high to low temperature. All but the cubic phase are ferroelectric [S2][S1]. The temperatures of the two lower transitions were not found in an opened source.
- **Measured.** Spontaneous polarization at room temperature. \(\mathrm{BaTiO_3}\): 0.263 C m⁻² [S6]; 0.15 C m⁻² in older flux-grown crystals and 0.26 in later ones [S2]. \(\mathrm{LiNbO_3}\): 71 µC cm⁻². \(\mathrm{LiTaO_3}\): 60 µC cm⁻² [S5]. Remanent polarization of a PZT film: about 40 µC cm⁻² [S6].
- **Computed here.** 0.263 C m⁻² is 26.3 µC cm⁻², and 40 µC cm⁻² is 0.40 C m⁻².
- **Measured.** Coercive field. Bulk ferroelectrics: typically several kV cm⁻¹ [S6]. \(\mathrm{BaTiO_3}\) films 5–30 nm thick between \(\mathrm{SrRuO_3}\) electrodes: 300–400 kV cm⁻¹ [S7]. The empirical scaling \(E_c \propto d^{-2/3}\) describes films from 100 µm down to 200 nm [S6].
- **Computed here.** 300–400 kV cm⁻¹ is \(3\times10^{7}\)–\(4\times10^{7}\) V m⁻¹. The scaling law raises \(E_c\) by a factor of \(500^{2/3} = 63\) between 100 µm and 200 nm.
- **Measured.** Switching is nucleation at the electrode, forward growth of domains across the film, then slower sideways growth. Switching models use an activation field for nucleation, which differs from the coercive field, or a broad distribution of waiting times over independent regions [S6]. No opened source gives a sharp switching field.
- **Model (electrostatics of a polarized slab).** A slab polarized along its normal has a depolarizing field opposing the polarization; unless compensated it destabilizes the polar state [S6]. Compensation comes from free charge in electrodes or on the surface, or from the formation of domains [S6][S9].
- **Computed here.** A slab with \(P = 0.263\) C m⁻² and no compensation would carry \(P/\varepsilon_0 = 3.0\times10^{10}\) V m⁻¹. A field equal to the measured thin-film coercive field, \(3\times10^{7}\)–\(4\times10^{7}\) V m⁻¹, is 0.10–0.13 % of that. Compensation has to be complete to about one part in a thousand before the residual field drops below the write field.
- **Model (first-principles calculation, short circuit, zero temperature).** \(\mathrm{BaTiO_3}\) between \(\mathrm{SrRuO_3}\) electrodes loses its ferroelectric instability below about six unit cells (24 Å), because dipoles at the interface leave a depolarizing field [S8]. Similar calculations for \(\mathrm{PbTiO_3}\) capacitors give 2 to 7 unit cells, depending on the density functional [S9]. An earlier Landau-theory estimate for PZT was about 200 Å [S11].
- **Computed here.** Six unit cells in 24 Å is 0.40 nm per cell; three cells are 1.2 nm.
- **Measured.** \(\mathrm{PbTiO_3}\) films on insulating \(\mathrm{SrTiO_3}\): the ferroelectric phase is stable at room temperature down to 3 unit cells (1.2 nm) [S10], and films of 12–420 Å form periodic 180° stripe domains [S11]. The polar phase survives; the net polarization is zero.
- **Measured.** \(\mathrm{PbTiO_3}\) films on a conducting substrate, 500 down to 24 Å: the tetragonality falls below 200 Å. Films below 50 Å have a reduced polarization and remain ferroelectric [S11].
- **Measured.** \(\mathrm{SrRuO_3}/\mathrm{BaTiO_3}/\mathrm{SrRuO_3}\) capacitors, 5–30 nm: the net polarization relaxes in time, with a large change between 10 and 500 µs. The depolarizing field, found from the applied field that stops the relaxation, is comparable to or larger than the coercive field and agrees with an electrostatic calculation from the electrode screening length of 0.8 ± 0.1 Å. For a 15 nm film with noble-metal electrodes 500–900 kV cm⁻¹ is expected. The authors conclude that this relaxation limits capacitor devices before the critical thickness does [S7].
- **Measured.** Small crystals. Individual \(\mathrm{BaTiO_3}\) nanocubes and GeTe nanocrystals show polarization switching at room temperature down to about 5 nm, with a monodomain polarization state [S12]. No opened source gives a thermal-activation size criterion for a ferroelectric particle.
- **Convention.** The energy dissipated per unit volume per cycle is the loop area \(\oint E\,dP\). Holding \(P_r\) at \(E = 0\) costs zero continuous power: it is a static configuration.

**Data confidence:** High for the Curie points, the spontaneous polarization of \(\mathrm{BaTiO_3}\) and the thin-film results, which were read in full text or in the abstracts of the primary papers. The \(\mathrm{PbTiO_3}\) Curie point rests on one tertiary source. Bulk-ceramic values of \(P_r\) and \(E_c\) for named grades were not opened; the file carries a class for the bulk ("several kV cm⁻¹") and measured values for films. The six-unit-cell critical thickness is a calculation.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Dielectric displacement: \(\mathbf{D} = \varepsilon_0\mathbf{E} + \mathbf{P}\).
- Remanence \(P_r\): intercept at \(E = 0\) after saturation. Coercive field \(E_c\): intercept at \(P = 0\).
- Dissipated energy density per cycle:

  \[
  w = \oint \mathbf{E}\cdot d\mathbf{P}
  \]

- Landau–Devonshire expansion, a fit to the observed transition:

  \[
  F = \tfrac{1}{2}\alpha(T - T_C)P^2 + \tfrac{1}{4}\beta P^4 + \cdots - EP
  \]

  The double well below \(T_C\) is the standard description of two remanent polarities.

- Depolarizing field of a slab between real electrodes: the screening charge sits a finite length \(\lambda\) inside the metal, so compensation is incomplete and the residual field grows as the film thickness \(d\) falls [S7]. With no compensation the field is \(P/\varepsilon_0\).
- Thickness scaling of the coercive field (empirical): \(E_c \propto d^{-2/3}\) [S6].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A polar lattice and a source of compensating charge. The polar phase needs very little material: it is measured at 1.2 nm in a film and at about 5 nm in a crystal. A net remanent polarization needs more, and how much depends on the electrodes: with \(\mathrm{SrRuO_3}\) the residual field already matches the write field in films of 5–30 nm. The buffer is the screening, counted as the fraction of bound charge left uncompensated, and has no single length.

- **Clock rate / latency.** Switching proceeds by nucleation and domain growth under the applied field, with the sideways growth the slowest stage. Without full compensation the net polarization relaxes on its own, within 10–500 µs in the measured capacitors. The wall-motion clock and the domain pattern are owned by [ferroelectric-domains](ferroelectric-domains.md).

- **Energy barriers or thresholds.** A polar double well holds \(\pm P_r\) at \(E = 0\) with zero continuous power. Energy is spent on transitions (the loop area). The write field is \(E_c\), set by nucleation and growth and rising as \(d^{-2/3}\) in thinner films. The residual depolarizing field acts as a standing reverse bias on the same well.

- **Dominant failure modes.**
  - **Threshold** — Curie point: above \(T_C\) the polar phase is gone (393 K in \(\mathrm{BaTiO_3}\), 468–638 K across PZT grades, 874–958 K reported for \(\mathrm{LiTaO_3}\)). A phase transition.
  - **Crossover** — reverse field: switching is nucleation and growth with a distribution of waiting times. \(E_c\) is the loop intercept at a given sweep and thickness, \(E_c \propto d^{-2/3}\). Larger fields destroy the insulator ([dielectric-breakdown](dielectric-breakdown.md)).
  - **Crossover** — thickness and screening: the polarization falls gradually below about 200 Å and is reduced but present at 24 Å. The net remanence is lost first, by relaxation when the residual field reaches \(E_c\), or by stripe domains when there is no free charge. The calculated critical thickness (6 unit cells for \(\mathrm{BaTiO_3}\) with \(\mathrm{SrRuO_3}\); 2–7 for \(\mathrm{PbTiO_3}\)) is a threshold in a zero-temperature model for one electrode.
  - **Crossover** — crystal size: switching is observed down to about 5 nm. No critical size and no thermal-activation criterion were found.
  - **Crossover** — mechanical or electrode damage: no measured scale filed.

- **Emergent constant or stable output.** A remanent polarization (0.26 C m⁻² spontaneous in \(\mathrm{BaTiO_3}\), about 0.4 C m⁻² remanent in a PZT film) and its bound charge at zero continuous power, while the temperature and the compensation stay inside the envelope above.

### 4.6 Internal Consistency Notes

The accounting matches the magnet latch: a remanent state at zero field, zero hold power, a loop-area write cost, a Curie threshold, and a linear limit when the well is absent. [Piezoelectricity](piezoelectricity.md) is the strain readout of the same polar lattice; [refraction-dielectric](refraction-dielectric.md) is the unlatched polarization.

Sourcing changed the size limit. The first version described a "superparaelectric / depolarization collapse" below a process-dependent grain or film size and treated it as the polar counterpart of the magnetic \(KV\) limit. The opened sources give no thermal-volume criterion. The limit is electrostatic: the depolarizing field of a thin slab, opposed by screening charge or avoided by forming domains. It is continuous in thickness, it depends on the electrode, and the polar phase is still present at 1.2 nm. The magnetic comparison also moved: [superparamagnetism](superparamagnetism.md) is now a crossover in retention time (25 \(kT\) is a 100 s convention), so neither side has a sharp volume threshold. The mechanisms differ: thermal activation over \(KV\) on the magnetic side, an uncompensated field on the polar side.

The mapping is not closed on the write field. \(E_c\) is taken from loops and from an empirical thickness law; it is not derived from the Landau well. The depolarizing field is now a measured quantity in one capacitor system and agrees there with electrostatics, so that half of the old gap has numbers. A general specification of the screening required for a given retention time is not filed.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the Curie threshold, remanence at zero field and zero hold power map cleanly onto a latch, and the thin-film loss of remanence is measured; \(E_c\) and the screening requirement remain empirical.

## Related entries

- [permanent-magnet-latch](permanent-magnet-latch.md) — magnetic counterpart: remanent moment at zero continuous field
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — the same loop accounting in \(M(H)\)
- [superparamagnetism](superparamagnetism.md) — loss of a small grain's direction by thermal activation; a crossover in retention time, with no measured polar equivalent
- [ferroelectric-domains](ferroelectric-domains.md) — how a polar body partitions; stripe domains replace the net polarization of an unscreened film
- [piezoelectricity](piezoelectricity.md) — strain coupled to polarization on a lattice without inversion
- [refraction-dielectric](refraction-dielectric.md) — linear bound-charge response without remanence
- [dielectric-breakdown](dielectric-breakdown.md) — field destruction of the insulator that hosts the latch

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Aksel and Jones, *Sensors* 10, 1935 (2010)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3264460/) | full-text | Secondary review: BaTiO3 tetragonal-to-cubic transition at 120 °C; further structural transitions on cooling. |
| S2 | [Wikipedia, "Barium titanate"](https://en.wikipedia.org/wiki/Barium_titanate) | full-text | Tertiary: Curie point 120–130 °C; spontaneous polarization 0.15 to 0.26 C/m²; four polymorphs, all but the cubic one ferroelectric. |
| S3 | [Wikipedia, "Lead titanate"](https://en.wikipedia.org/wiki/Lead_titanate) | full-text | Tertiary: PbTiO3 transition at 760 K. |
| S4 | [Liu, Zhang, Jiang and Cao, *Mater. Sci. Eng. R* 89, 1 (2015)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4369800/) | full-text | Review, Table 8: Curie points of PZT5A, PZT5H, PZT4 and PZT8. |
| S5 | [El Azzouzi et al., arXiv:2403.16717 (2024)](https://arxiv.org/abs/2403.16717) | full-text | Secondary for the reported ranges: LiNbO3 1413–1475 K and 71 µC/cm²; LiTaO3 874–958 K and 60 µC/cm². |
| S6 | [Dawber, Rabe and Scott, *Rev. Mod. Phys.* 77, 1083 (2005), arXiv:cond-mat/0503372](https://arxiv.org/abs/cond-mat/0503372) | full-text | Standard review: BaTiO3 polarization 0.263 C/m²; coercive fields of several kV/cm; thickness scaling of the coercive field; PZT film remanence; switching stages and models; depolarizing field and its compensation. |
| S7 | [Kim et al., *Phys. Rev. Lett.* 95, 237602 (2005), arXiv:cond-mat/0506480](https://arxiv.org/abs/cond-mat/0506480) | full-text | 5–30 nm BaTiO3 capacitors: coercive field 300–400 kV/cm; measured depolarizing field; polarization relaxation between 10 and 500 µs; screening length; noble-metal estimate. |
| S8 | [Junquera and Ghosez, *Nature* 422, 506 (2003)](https://doi.org/10.1038/nature01501) | abstract | Calculated critical thickness of about six unit cells (24 Å) for BaTiO3 between SrRuO3 electrodes; depolarizing field from interface dipoles. |
| S9 | [Liu, Chen, Wang and Zheng, *Materials* 7, 6502 (2014)](https://doi.org/10.3390/ma7096502) | full-text | Review: calculated critical thickness of 2 to 7 unit cells for PbTiO3 capacitors; residual depolarizing field from finite screening length; compensation by electrodes or adsorbates. |
| S10 | [Fong et al., *Science* 304, 1650 (2004)](https://doi.org/10.1126/science.1098252) | abstract | PbTiO3 ferroelectric phase stable at room temperature down to 3 unit cells (1.2 nm). |
| S11 | [Lichtensteiger, Triscone, Junquera and Ghosez, *Phys. Rev. Lett.* 94, 047603 (2005), arXiv:cond-mat/0404228](https://arxiv.org/abs/cond-mat/0404228) | full-text | PbTiO3 films 500 to 24 Å: tetragonality falls below 200 Å; reduced polarization below 50 Å, still ferroelectric; stripe domains in 12–420 Å films on insulating substrates; earlier 200 Å estimate. |
| S12 | [Polking et al., *Nature Mater.* 11, 700 (2012)](https://doi.org/10.1038/nmat3371) | abstract | Room-temperature polarization switching down to about 5 nm in individual nanocrystals; monodomain state. |
