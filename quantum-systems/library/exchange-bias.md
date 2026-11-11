---
id: exchange-bias
title: Exchange Bias (Pinned-Loop Shift)
status: formal
family: latched-order
constraints:
  - energy-barrier
  - thermal
  - field-threshold
  - spatial-buffer
confidence_data: high
confidence_mapping: medium
related:
  - antiferromagnetic-order
  - ferromagnetic-hysteresis
  - permanent-magnet-latch
  - superparamagnetism
  - magnetic-domains
updated: 2026-11-11
---

# Exchange Bias (Pinned-Loop Shift)

### 4.1 Effect Name

Exchange bias (pinned-loop shift)

### 4.2 Macroscopic Observation

A ferromagnet in contact with an antiferromagnet, after cooling in a magnetic field through the antiferromagnet's ordering temperature, shows a hysteresis loop that is shifted along the field axis rather than centered at \(H = 0\). The shift is the exchange-bias field \(H_\mathrm{ex}\). Warming through a blocking temperature, or removing the antiferromagnet, returns a centered loop. The shifted remanent state is held with no applied power.

### 4.3 Established Quantitative Boundaries

- **Measured.** Discovery. Compacts of fine cobalt particles (about 200 Å) with a coherent cobaltous-oxide shell; the effect occurs only below the Néel temperature of the oxide, 291 K for \(\mathrm{CoO}\) [S1][S2][S4]. Cooled from room temperature to 77 K in 10 kOe the loop is displaced by 1600 Oe; cooled in zero field it is centered; the displacement survives applied fields of 70 kOe [S3][S4].
- **Measured.** Above the Néel temperature the same material behaves as an ordinary ferromagnet [S2]. In a spin valve the NiFe layer touching FeMn has a shifted loop and the identical NiFe layer without the antiferromagnet has a conventional loop [S3].
- **Measured.** Systems. Metallic pins FeMn, IrMn, PtMn, NiMn and oxide or fluoride pins NiO, CoO, \(\mathrm{FeF_2}\), \(\mathrm{MnF_2}\) are tabulated with their interface energy, blocking temperature and Néel temperature [S3]. Fe–FeO particles show rotational hysteresis that vanishes at the Néel temperature of FeO but no loop shift; oxidized Fe films show a small one [S2][S3].
- **Measured.** Size of the shift. Up to 9500 Oe in Co–CoO particles at 4–10 K. Interface energy per unit area: 0.01–0.47 erg cm⁻² for FeMn, 0.01–0.19 for IrMn, 0.004–0.29 for NiO, up to 3.5 for oxidized Co at 10 K (1 erg cm⁻² = 1 mJ m⁻²) [S3].
- **Measured.** Blocking temperature \(T_B\), where the shift vanishes, against bulk Néel temperature [S3][S6]: FeMn (111) 380–480 K against 490 K; IrMn (111) 400–520 K against 690 K; NiO (111) 450–500 K against 520 K; \(\mathrm{FeF_2}\) 79 K against 79 K; Co/CoO(25 Å) 180 K against 291 K [S4]. Thick or single-crystal antiferromagnets have \(T_B \approx T_N\); very thin films have \(T_B < T_N\), and a real film has a distribution of blocking temperatures [S3][S5].
- **Measured.** \(T_B\) is not a second name for the ordering temperature. In \(\mathrm{Fe_3O_4}\)/CoO, \(T_B\) falls below 291 K for CoO thinner than 50 Å while neutron diffraction shows the CoO ordering temperature does not follow it [S7]. \(T_B\) rises with measurement sweep rate [S6]. Annealed polycrystalline FeMn is listed with \(T_B\) of 420–570 K against a bulk Néel point of 490 K, so \(T_B \le T_N\) holds against the ordering temperature of the actual layer, not always against the handbook value [S3].
- **Measured.** Between \(T_B\) and \(T_N\) the loop is centered but its coercivity can stay enhanced [S4]. An increase in coercivity accompanies the shift [S3].
- **Measured.** Ferromagnet thickness. The shift is roughly inversely proportional to the ferromagnet thickness, up to several hundred nanometres, and fails when the layer is too thin to be continuous [S3]; in Co/CoO it holds down to 2 nm [S4].
- **Measured.** Antiferromagnet thickness. Above about 20 nm the shift is independent of it; it then falls abruptly and reaches zero at a few nanometres [S3]. One study finds 6 nm for IrMn [S14]. The critical thickness is an order of magnitude smaller for the more anisotropic fluoride [S13].
- **Measured.** Reach. With Ag, Au or Cu spacers between the layers the coupling decays exponentially and extends to as much as 50 Å [S8].
- **Measured.** Setting. Cooling in zero field from a demagnetized state gives no shift; cooling in zero field from a remanent state still gives one. The size of the cooling field matters little in ordinary systems, about 10 % between 300 Oe and 5 T for FeMn/NiFe [S3].
- **Measured.** Sign. The shift is generally opposite to the cooling field. In Fe/\(\mathrm{FeF_2}\) a large cooling field (70 kOe against 2 kOe) reverses it [S9][S3].
- **Measured.** Training. The shift falls over consecutive loops; strong with polycrystalline antiferromagnets, small or absent with single crystals [S3][S5].
- **Measured.** Small grains. Cobalt particles of about 4 nm lose their moment at 10 K in a paramagnetic matrix and remain ferromagnetic to about 290 K in an antiferromagnetic one [S10]. In 4 nm Co cores with CoO shells, isolated shells give blocking at 5 K and a shift of 0.8 mT; shells in contact give blocking at 220 K and a shift of 367 mT that persists to about 200 K [S11]. A 1.0 nm CoO shell gives no shift and a 3.2 nm shell does [S12]; 3 nm oxidized Co in alumina shows none [S15].
- **Model (Néel–Arrhenius, \(KV = 25\,k_BT_B\)).** The bare 4 nm cobalt core in [S11] should block at about 6 K.
- **Model (Meiklejohn–Bean ideal interface).** Taking the interface coupling equal to the ferromagnetic exchange predicts a shift several orders of magnitude larger than measured; for Co/CoO the observed coupling is below the expected 4 mJ m⁻² by a factor of three to several orders [S3][S4][S5].
- **Convention.** Holding the shifted remanent state costs zero continuous power: it is a static configuration, and no source reports a dissipation at rest.

**Data confidence:** High as a class — the shift, its disappearance at \(T_B\), the thickness trends and the small-grain results are multiply reproduced and were read in full-text reviews. The original 1956 letter was not opened; its numbers come from the 1957–58 abstracts and from two reviews that reproduce its figure. Any one stack's \(H_\mathrm{ex}\) and \(T_B\) are Medium (interface, grain size, setting protocol).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Shifted-loop accounting: the loop of [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) is recentered from \(H = 0\) to \(H = -H_\mathrm{ex}\).
- Meiklejohn–Bean interface form:

  \[
  H_\mathrm{ex} \approx \frac{\Delta E}{\mu_0 M_s t_\mathrm{FM}}
  \]

  \(\Delta E\) is the interface energy per unit area defined from the measured shift [S3]. The \(1/t_\mathrm{FM}\) factor is the part that tracks data. In the same model a pin exists only when the antiferromagnet's anisotropy energy per area exceeds the interface coupling, which gives a critical antiferromagnet thickness [S3].
- Training: the shift falls roughly as \(1/\sqrt{n}\) with loop number \(n\) (empirical) [S3].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two ordered bodies and a coupling between them:
  1. An antiferromagnet thick and anisotropic enough to hold its own direction when the ferromagnet reverses (a few nanometres and up; the number depends on its anisotropy).
  2. A ferromagnet thin enough that the interface term is not diluted.
  3. Proximity. The coupling is not strictly contact: it reaches through up to 50 Å of nonmagnetic metal.

- **Clock rate / latency.** Setting the pin is a thermal write on the laboratory cooling clock. Reading it depends on the sweep: \(T_B\) rises with sweep rate, so the pin is a thermally activated object with its own relaxation time, like a grain in [superparamagnetism](superparamagnetism.md).

- **Energy barriers or thresholds.** The antiferromagnet adds a unidirectional term to the ferromagnet's energy. In a small grain that term can be the dominant barrier: a 4 nm cobalt core that blocks near 6–10 K on its own anisotropy stays blocked to 220–290 K when pinned. The pin is therefore not just an offset on an existing latch; it can supply the latch.

- **Dominant failure modes.**
  - **Crossover** — thermal: the shift falls to zero at \(T_B\). A film has a distribution of blocking temperatures and \(T_B\) moves with sweep rate, so this is thermal activation of the pin, not a phase transition. The phase transition is \(T_N\), which can lie well above.
  - **Threshold** — antiferromagnet thickness: the shift drops abruptly to zero below a critical thickness of a few nanometres (6 nm in one IrMn study), set by the antiferromagnet's anisotropy.
  - **Crossover** — ferromagnet thickness: the shift falls as \(1/t_\mathrm{FM}\).
  - **Crossover** — separation: exponential decay through a metal spacer, gone by about 50 Å.
  - **Crossover** — cycling: training, roughly \(1/\sqrt{n}\).
  - **Crossover** — chemical or mechanical damage to the interface: no measured scale filed.

- **Emergent constant or stable output.** A stable offset of the ferromagnet's loop held at zero continuous power below \(T_B\), usually opposite to the cooling field.

### 4.6 Internal Consistency Notes

Two ordered bodies in series match the data: unblocking the pin removes the shift and leaves the ferromagnet's loop; the ferromagnet's own Curie point is a separate threshold. Zero hold power on the shifted remanence is the same accounting as the parent magnet.

Sourcing changed the picture in four places. The collapse at \(T_B\) is a crossover with a distribution and a rate dependence, not a threshold. \(T_B \le T_N\) is true of the layer's own ordering temperature but has listed exceptions against bulk handbook values. The interface is not a sharp boundary; the coupling has a reach of nanometres. And the direction of dependence between the two bodies was wrong in the first version: it treated the ferromagnetic grain's own \(KV\) as a precondition for the pin, where the measurements show the pin can stabilize a grain that would otherwise be superparamagnetic.

The mapping is not closed on the interface. The ideal-interface estimate exceeds the measured coupling by a factor of three to several orders of magnitude; roughness, uncompensated spins and antiferromagnetic domains are the named ingredients in the standard description and are not reduced here to a buffer or barrier number. Loop shifts are also reported with pins that are not antiferromagnets (ferrimagnets, disordered particle surfaces) [S3], so "antiferromagnet" in this entry is the common case, not a requirement.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the loop shift, its thermal unblocking, and the two-body topology are solid, but the interface energy and \(T_B/T_N\) remain interface- and grain-level data without a closed specification.

## Related entries

- [antiferromagnetic-order](antiferromagnetic-order.md) — the cancelled latch that supplies the pin
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — the loop that is shifted
- [permanent-magnet-latch](permanent-magnet-latch.md) — the ferromagnet's own remanent state
- [superparamagnetism](superparamagnetism.md) — thermal unblocking of a small ordered body; the pin can raise a grain's blocking temperature
- [magnetic-domains](magnetic-domains.md) — domain structure at the interface

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Meiklejohn and Bean, *Phys. Rev.* 105, 904 (1957)](https://doi.org/10.1103/PhysRev.105.904) | abstract | Co particles with a CoO shell; effect only below the oxide's Néel temperature; interface torque at 77 K. The 1956 letter (*Phys. Rev.* 102, 1413) was not opened. |
| S2 | [Meiklejohn, *J. Appl. Phys.* 29, 454 (1958)](https://doi.org/10.1063/1.1723179) | abstract | Particle size about 200 Å; ordinary ferromagnetic behaviour above the Néel temperature; Fe–FeO rotational hysteresis vanishing at the Néel temperature of FeO. |
| S3 | [Nogués and Schuller, *J. Magn. Magn. Mater.* 192, 203 (1999)](https://nucssp.rmki.kfki.hu/articles/catalog/99/nogues.jmm.192.203.1999.pdf) | full-text | Standard review: tables of interface energy, blocking and Néel temperatures; thickness dependences; setting, sign, training; pinned and free layers in a spin valve; ideal-interface overestimate; non-antiferromagnetic pins. |
| S4 | [Radu and Zabel, arXiv:0705.2055](https://arxiv.org/abs/0705.2055) | full-text | Reproduces the original loops (10 kOe, 77 K, centered zero-field-cooled loop, 70 kOe); CoO 291 K; Co/CoO(25 Å) blocking at 180 K with coercivity enhanced up to 291 K; coupling below 4 mJ m⁻². |
| S5 | [Kiwi, *J. Magn. Magn. Mater.* 234, 584 (2001)](https://nucssp.rmki.kfki.hu/articles/catalog/01/kiwi.jmm.234.584.2001.pdf) | full-text | Blocking temperature usually near, sometimes far below, the Néel temperature; ideal-interface estimate too large by orders of magnitude; training. |
| S6 | [Baltz et al., *Rev. Mod. Phys.* 90, 015005 (2018), arXiv:1606.04284](https://arxiv.org/abs/1606.04284) | full-text | Bulk Néel temperatures of FeMn, IrMn, PtMn, NiMn; blocking temperature rises with sweep rate. |
| S7 | [van der Zaag et al., *Phys. Rev. Lett.* 84, 6102 (2000)](https://doi.org/10.1103/PhysRevLett.84.6102) | abstract | Blocking temperature falls below 291 K for CoO under 50 Å while the ordering temperature does not. |
| S8 | [Gökemeijer, Ambrose and Chien, *Phys. Rev. Lett.* 79, 4270 (1997)](https://doi.org/10.1103/PhysRevLett.79.4270) | abstract | Coupling through Ag, Au, Cu spacers decays exponentially and extends to 50 Å. |
| S9 | [Nogués, Lederman, Moran and Schuller, *Phys. Rev. Lett.* 76, 4624 (1996)](https://doi.org/10.1103/PhysRevLett.76.4624) | abstract | Large cooling fields make the shift positive in Fe/FeF2. |
| S10 | [Skumryev et al., *Nature* 423, 850 (2003)](https://www.nature.com/articles/nature01687) | abstract | 4 nm Co particles: moment lost at 10 K in a paramagnetic matrix, ferromagnetic to about 290 K in an antiferromagnetic one. |
| S11 | [Nogués et al., *Phys. Rev. Lett.* 97, 157203 (2006)](https://ddd.uab.cat/pub/artpub/2006/114271/phyrevlet_a2006m10v97n15p157203.pdf) | full-text | 4 nm Co cores in CoO shells: bare-core blocking estimate 6 K; blocking 5 K against 220 K and shift 0.8 mT against 367 mT depending on whether the shells are in contact. |
| S12 | [Tracy et al., *Phys. Rev. B* 72, 064404 (2005)](https://doi.org/10.1103/PhysRevB.72.064404) | abstract | No bias with a 1.0 nm CoO shell; bias and enhanced thermal stability with a 3.2 nm shell. |
| S13 | [Lund et al., *Phys. Rev. B* 66, 054422 (2002)](https://doi.org/10.1103/PhysRevB.66.054422) | abstract | Critical antiferromagnet thickness an order of magnitude smaller for the more anisotropic fluoride. |
| S14 | [Gritsenko et al., *Phys. Procedia* 82, 51 (2016)](https://doi.org/10.1016/j.phpro.2016.05.010) | abstract | 6 nm IrMn as the critical thickness in NiFe/IrMn films. |
| S15 | [Dobrynin et al., *Appl. Phys. Lett.* 87, 012501 (2005)](https://doi.org/10.1063/1.1978977) | abstract | 3 nm oxidized Co particles show no exchange bias; a critical grain size is proposed. |
