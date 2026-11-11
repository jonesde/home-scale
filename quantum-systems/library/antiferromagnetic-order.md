---
id: antiferromagnetic-order
title: Antiferromagnetic Order (Cancelled Latch)
status: formal
family: latched-order
constraints:
  - energy-barrier
  - thermal
  - mechanical-lattice
  - field-threshold
  - spatial-buffer
confidence_data: high
confidence_mapping: high
review_depth: deep
related:
  - permanent-magnet-latch
  - ferromagnetic-hysteresis
  - exchange-bias
  - curie-paramagnetism
  - superparamagnetism
updated: 2026-11-11
---

# Antiferromagnetic Order (Cancelled Latch)

### 4.1 Effect Name

Antiferromagnetic order (cancelled latch)

### 4.2 Macroscopic Observation

Below a material-specific Néel temperature an antiferromagnet orders, but the sample exerts no useful permanent-magnet force and shows no large remanent dipole. Neutron diffraction nevertheless finds extra magnetic reflections: opposing sublattices are each magnetized and locked antiparallel. Above \(T_N\) those reflections are gone and the material is an ordinary paramagnet. Ordinary laboratory fields do not turn the ordered body into a permanent magnet.

### 4.3 Established Quantitative Boundaries

- **Measured.** Néel temperatures of the rock-salt monoxides: \(\mathrm{MnO}\) \(118\,\mathrm{K}\) (sources span 116–120 K) [S1][S2]; \(\mathrm{FeO}\) \(198\,\mathrm{K}\) (early reports 183–198 K; \(195(2)\,\mathrm{K}\) for \(\mathrm{Fe_{0.93}O}\); strongly stoichiometry-dependent) [S2][S3]; \(\mathrm{CoO}\) \(291\,\mathrm{K}\) [S2]; \(\mathrm{NiO}\) \(523\,\mathrm{K}\) (sources span 520–525 K) [S2][S4]. Uniaxial fluorides: \(\mathrm{MnF_2}\) \(67.7\,\mathrm{K}\) [S12], \(\mathrm{FeF_2}\) \(78.4\,\mathrm{K}\) [S13]; other sources put these at 67–69 K and 75.8–79 K.
- **Measured.** Magnetic superlattice. Neutron diffraction on \(\mathrm{MnO}\) at \(80\,\mathrm{K}\) shows reflections that are absent at room temperature, from a magnetic cell twice the chemical cell along each axis [S5][S6]. In \(\mathrm{NiO}\), superlattice reflections present at room temperature are absent at \(563\,\mathrm{K}\), above \(T_N\) [S7].
- **Measured.** Susceptibility. \(\chi\) does not diverge at \(T_N\) [S8]. In single-crystal \(\mathrm{MnF_2}\) the parallel susceptibility approaches zero as \(T\to 0\), while the perpendicular susceptibility rises about 12 % between 70 K and 14 K, so it is roughly, not exactly, constant [S9].
- **Model (Curie–Weiss fit above \(T_N\)).** The fitted paramagnetic temperature \(\theta\) is several times \(T_N\) in the monoxides: \(\mathrm{MnO}\) 610 K, \(\mathrm{FeO}\) 570 K, \(\mathrm{CoO}\) 330 K, \(\mathrm{NiO}\) about 2000 K [S2]. \(\theta\) depends on the fitted temperature window: published fits for \(\mathrm{Fe_{0.93}O}\) range from 94 K to 570 K [S3], and a recent \(\mathrm{MnO}\) analysis quotes about 550 K [S1]. \(\theta = T_N\) holds only in the nearest-neighbour two-sublattice mean-field model [S10].
- **Computed here.** \(\theta/T_N\) from the handbook pairs in [S2]: \(\mathrm{MnO}\) \(610/116 = 5.3\); \(\mathrm{FeO}\) \(570/198 = 2.9\); \(\mathrm{CoO}\) \(330/291 = 1.1\); \(\mathrm{NiO}\) \(2000/525 = 3.8\).
- **Measured.** Spin-flop fields exist as clean thresholds in uniaxial crystals: \(\mathrm{MnF_2}\) \(93 \pm 2\,\mathrm{kOe}\) (9.3 T) [S11]; \(\mathrm{Cr_2O_3}\) \(60 \pm 3\,\mathrm{kG}\) (6.0 T) [S14]; \(\mathrm{FeF_2}\) 41.9 T [S15]; \(\mathrm{CoO}\) 7.0 T at 240 K [S16]. For cubic \(\mathrm{NiO}\) the opened sources give only 0.24 T in the (111) plane at 300 K, computed from anisotropy and susceptibility, and 1.54 T quoted second-hand [S17][S7]. No value was found for \(\mathrm{MnO}\).
- **Measured.** Antiferromagnetic resonance at low temperature: \(\mathrm{MnF_2}\) \(261.4 \pm 1.5\,\mathrm{GHz}\) [S12]; \(\mathrm{MnO}\) \(27.5\,\mathrm{cm^{-1}}\) and \(\mathrm{NiO}\) \(36.6\,\mathrm{cm^{-1}}\) [S18]; \(\mathrm{FeF_2}\) \(52.7 \pm 0.2\,\mathrm{cm^{-1}}\) [S13]. Ferromagnets resonate in the GHz range [S8].
- **Computed here.** With \(1\,\mathrm{cm^{-1}} = 29.979\,\mathrm{GHz}\): \(\mathrm{MnO}\) 0.82 THz, \(\mathrm{NiO}\) 1.10 THz, \(\mathrm{FeF_2}\) 1.58 THz. For comparison \(kT_N/h\) is 2.5 THz for \(\mathrm{MnO}\) and 10.9 THz for \(\mathrm{NiO}\), so the resonance sits at 0.33 and 0.10 of that scale.
- **Measured.** Weak ferromagnetism. Hematite above its Morin transition (about \(-10\,^\circ\mathrm{C}\)) carries a spontaneous magnetization of about \(0.4\,\mathrm{A\,m^2\,kg^{-1}}\) from a slight canting of the sublattices [S19]; the canting is attributed to antisymmetric exchange [S20].
- **Measured.** Size. In \(\mathrm{CoO}\) layers \(T_N\) falls with thickness along a finite-size scaling curve with shift exponent \(1.55 \pm 0.05\) [S21]; a later study attributes the sharp drop below 20 Å to the layers being amorphous [S22]. Small \(\mathrm{NiO}\) crystals show susceptibility maxima that neutron diffraction shows are not shifted Néel points [S4]. Antiferromagnetic nanoparticles can relax superparamagnetically and carry moments from uncompensated surface spins [S23].
- **Convention.** Holding the ordered state costs zero continuous power: it is a static equilibrium configuration, and no source reports a dissipation at rest.

**Data confidence:** High — \(T_N\), the magnetic superlattice, and the susceptibility behaviour are multiply reproduced; ordering temperatures agree across sources to a few kelvin. \(\theta\) is a fit parameter and is Medium. Spin-flop fields are High for the uniaxial crystals and Low for the cubic monoxides. Several primaries were opened only as abstracts (see Sources).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Two-sublattice accounting: \(\mathbf{M}_A \approx -\mathbf{M}_B\), so \(\mathbf{M}_\mathrm{net} \approx 0\).
- Curie–Weiss form above \(T_N\):

  \[
  \chi = \frac{C}{T + \theta},\qquad \theta > 0
  \]

  In the nearest-neighbour two-sublattice model \(\theta = T_N\) [S10]. The measured ratios of 1.1 to 5.3 show that model is too simple for the monoxides.
- Uniaxial two-sublattice resonance and spin-flop field: both scale as \(\sqrt{2H_E H_A}\), the geometric mean of the exchange and anisotropy fields [S11][S14]. The resonance is therefore not set by exchange alone.
- Magnetic Bragg intensity \(\to 0\) as \(T\to T_N^-\) [S5].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two or more interpenetrating sublattices, each ordered, correlated over a volume large enough to hold the antiparallel relation against \(kT\). A single spin is not an antiferromagnet. The readable hardware is the magnetic superlattice (neutron or electron diffraction, resonance), not a dipole field.

- **Clock rate / latency.** The measured clock is the antiferromagnetic resonance, 0.26–1.6 THz in the crystals above, two to three orders above ferromagnetic resonance. It is set by exchange *and* anisotropy together, \(\sqrt{2H_E H_A}\), and sits well below \(kT_N/h\). The earlier statement that the rate is "set by \(kT_N\)" was wrong.

- **Energy barriers or thresholds.** Exchange holds each sublattice against the other; anisotropy fixes the axis. Two energy scales, not one. The emergent dipole is about zero because the sublattices are opposed; the cancelled force is the output, not a failure.

- **Dominant failure modes.**
  - **Threshold** — thermal: \(T > T_N\). A continuous phase transition; sublattice order and magnetic Bragg intensity go to zero. Sharp in a large crystal, rounded and shifted in thin layers.
  - **Threshold** — field, uniaxial crystals only: at the spin-flop field (6–42 T in the crystals above) the sublattices rotate perpendicular to the field. In cubic monoxides there is no single clean spin-flop; domain and in-plane effects appear below 1 T.
  - **Crossover** — size: \(T_N\) and the stability of the sublattice direction fall continuously with layer thickness or particle size (finite-size scaling, exponent 1.55 in one system). No portable length; the sharp drop once reported turned out to be structural.
  - **Crossover** — mechanical or chemical: off-stoichiometry and disorder move \(T_N\) continuously (\(\mathrm{FeO}\) 183–200 K). No measured threshold is filed.

- **Emergent constant or stable output.** A static antiparallel superlattice with \(M_\mathrm{net}\approx 0\), held at zero continuous power below \(T_N\). Its coupling into a ferromagnet is filed as [exchange-bias](exchange-bias.md).

### 4.6 Internal Consistency Notes

A latch here means a configuration held at zero continuous power, not a nonzero dipole. Antiferromagnetic order meets that: ordered sublattices, a sharp thermal threshold, no hold-power bill. Reading "no force on iron" as "nothing is ordered" would contradict the diffraction data.

Sourcing changed three things. First, \(\theta\) is not of the order of \(T_N\) in the monoxides this file is built on; it is up to five times larger. The sum of the couplings (\(\theta\)) and the temperature at which order survives (\(T_N\)) are different measurements, and a "two opposed latches" picture with one exchange number does not reproduce their ratio. Second, the clock is not \(kT_N/h\); it is a lower frequency that needs the anisotropy as well. Third, the field failure is a clean threshold only for uniaxial crystals, which the first version did not list; the monoxides it did list do not show one.

The mapping still takes the sign of the coupling as data. QSA does not derive why \(\mathrm{MnO}\) is antiferromagnetic and Fe is ferromagnetic. Weak ferromagnetism from canting is a small uncancelled remainder (0.4 A m² kg⁻¹ in hematite); it does not convert this entry into the permanent-magnet latch.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(T_N\), the vanishing net moment, the magnetic superlattice, and zero hold power specify a cancelled latch cleanly. The open items are the origin of the sign of the coupling and the fact that one exchange number does not account for both \(\theta\) and \(T_N\).

## Related entries

- [permanent-magnet-latch](permanent-magnet-latch.md) — the uncancelled cousin: nonzero macro moment
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — write / erase cycle of uncancelled order; contrast case
- [exchange-bias](exchange-bias.md) — this cancelled latch as the pin on a ferromagnet
- [curie-paramagnetism](curie-paramagnetism.md) — unlocked ensemble above \(T_N\)
- [superparamagnetism](superparamagnetism.md) — thermal relaxation of a small ordered particle; antiferromagnetic particles show the analog

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Paddison et al., *Phys. Rev. B* 97, 014429 (2018), arXiv:1602.08420](https://arxiv.org/abs/1602.08420) | full-text | MnO orders at 118 K; Curie–Weiss temperature about 550 K; frustration ratio 5.17. |
| S2 | [Harrison, arXiv:cond-mat/0701423 (2007), Table 2, quoting Kittel, *Introduction to Solid State Physics*, 5th ed., p. 481](https://arxiv.org/abs/cond-mat/0701423) | full-text | Handbook Néel and Curie–Weiss temperatures of MnO, FeO, CoO, NiO. Kittel itself was not opened. |
| S3 | [Schrettle et al., *Eur. Phys. J. B* 85 (2012), arXiv:1203.1201](https://arxiv.org/abs/1203.1201) | full-text | FeO orders near 200 K (183–198 K in early work, 195 K for Fe0.93O); stoichiometry dependence; the spread of fitted Curie–Weiss temperatures. |
| S4 | [Richardson and Milligan, *Phys. Rev.* 102, 1289 (1956)](https://doi.org/10.1103/PhysRev.102.1289) | abstract | NiO Néel point 523 K; susceptibility maxima in small NiO crystals are not shifted Néel points. |
| S5 | [Shull, Strauser and Wollan, *Phys. Rev.* 83, 333 (1951)](https://doi.org/10.1103/PhysRev.83.333) | abstract | Strong coherent magnetic scattering from antiferromagnets; magnetic cell larger than the chemical cell; temperature dependence of the magnetic intensities. Follows Shull and Smart, *Phys. Rev.* 76, 1256 (1949), not opened in full. |
| S6 | [Wills, arXiv:1609.09666](https://arxiv.org/abs/1609.09666) | full-text | Describes the 1949 MnO experiment: new peaks below the transition, doubled magnetic cell. |
| S7 | [Loudon, arXiv:1206.6734 (2012)](https://arxiv.org/abs/1206.6734) | full-text | NiO superlattice reflections absent at 563 K; quotes a 1.54 T spin-flop for NiO second-hand. |
| S8 | [Baltz et al., *Rev. Mod. Phys.* 90, 015005 (2018), arXiv:1606.04284](https://arxiv.org/abs/1606.04284) | full-text | Susceptibility does not diverge at the Néel point; antiferromagnetic modes at hundreds of GHz to THz against GHz in ferromagnets. |
| S9 | [Griffel and Stout, *J. Chem. Phys.* 18, 1455 (1950)](https://doi.org/10.1063/1.1747512) | abstract | MnF2 single crystal: perpendicular susceptibility rises 12 % from 70 to 14 K, parallel goes to zero. |
| S10 | [Johnston, *Phys. Rev. B* 91, 064427 (2015), arXiv:1407.6353](https://arxiv.org/abs/1407.6353) | full-text | Curie–Weiss temperature equals the Néel temperature only for the nearest-neighbour Néel antiferromagnet. |
| S11 | [Jacobs, *J. Appl. Phys.* 32, S61 (1961)](https://doi.org/10.1063/1.2000500) | abstract | MnF2 spin-flop field 93 ± 2 kOe, given by the combination of anisotropy and exchange. |
| S12 | [Johnson and Nethercot, *Phys. Rev.* 114, 705 (1959)](https://doi.org/10.1103/PhysRev.114.705) | abstract | MnF2 antiferromagnetic resonance 261.4 ± 1.5 GHz; Néel temperature 67.7 K. |
| S13 | [Ohlmann and Tinkham, *Phys. Rev.* 123, 425 (1961)](https://doi.org/10.1103/PhysRev.123.425) | abstract | FeF2 resonance 52.7 ± 0.2 cm⁻¹; Néel temperature 78.4 K. |
| S14 | [Foner, *Phys. Rev.* 130, 183 (1963)](https://doi.org/10.1103/PhysRev.130.183) | abstract | Cr2O3 spin-flop combination 60 ± 3 kG from 4.2 to 235 K. |
| S15 | [Corrêa and Výborný, arXiv:1805.11339 (2018), Table I](https://arxiv.org/abs/1805.11339) | full-text | FeF2 spin-flop 41.9 T (secondary; cites Jaccarino et al. 1983, not opened); fluoride Néel temperatures. |
| S16 | [Grzybowski et al., *Phys. Rev. B* 107, L060403 (2023)](https://doi.org/10.1103/PhysRevB.107.L060403) | abstract | CoO spin-flop at 7.0 T at 240 K. |
| S17 | [Wang, Hou et al., arXiv:1708.09564](https://arxiv.org/abs/1708.09564) | full-text | NiO in-plane spin-flop field 2400 Oe at 300 K, computed from anisotropy and susceptibility. |
| S18 | [Sievers and Tinkham, *Phys. Rev.* 129, 1566 (1963)](https://doi.org/10.1103/PhysRev.129.1566) | abstract | Resonance at 27.5 cm⁻¹ in MnO and 36.6 cm⁻¹ in NiO at 2 K. |
| S19 | [de Boer, Mullender and Dekkers, *Geophys. J. Int.* 146, 201 (2001)](https://dspace.library.uu.nl/bitstream/handle/1874/1357/DeBoer01a.pdf) | full-text | Hematite weak moment about 0.4 A m² kg⁻¹ from spin canting; Morin transition near −10 °C. |
| S20 | [Moriya, *Phys. Rev.* 120, 91 (1960)](https://doi.org/10.1103/PhysRev.120.91) | abstract | Antisymmetric exchange as the origin of weak ferromagnetism in hematite. |
| S21 | [Ambrose and Chien, *Phys. Rev. Lett.* 76, 1743 (1996)](https://doi.org/10.1103/PhysRevLett.76.1743) | abstract | Néel temperature of CoO layers follows finite-size scaling, exponent 1.55 ± 0.05. |
| S22 | [Tang et al., *Phys. Rev. B* 67, 054408 (2003)](https://doi.org/10.1103/PhysRevB.67.054408) | abstract | The sharp drop below 20 Å in CoO is due to amorphous layers. |
| S23 | [Makhlouf et al., *J. Appl. Phys.* 81, 5561 (1997)](https://doi.org/10.1063/1.364661) | abstract | Antiferromagnetic nanoparticles: superparamagnetic relaxation and uncompensated surface moments, as first noted by Néel. |
