---
id: ferromagnetic-hysteresis
title: Ferromagnetic Hysteresis (Write–Erase Cycle)
status: formal
family: latched-order
constraints:
  - energy-barrier
  - field-threshold
  - thermal
  - spatial-buffer
  - mechanical-lattice
confidence_data: high
confidence_mapping: high
review_depth: deep
related:
  - permanent-magnet-latch
  - superparamagnetism
  - magnetic-domains
  - shape-anisotropy
  - exchange-bias
  - magnetostriction
  - curie-paramagnetism
updated: 2026-11-11
---

# Ferromagnetic Hysteresis (Write–Erase Cycle)

### 4.1 Effect Name

Ferromagnetic hysteresis (write–erase cycle)

### 4.2 Macroscopic Observation

A ferromagnet driven around a closed cycle of applied field \(H\) returns a multi-valued magnetization (or induction) loop. After a large field is removed, a remanent magnetization remains. A reverse field equal to the coercivity brings the magnetization back through zero. Coercivity varies continuously between materials, from under 1 A/m in annealed nickel–iron alloys to about \(10^6\) A/m in rare-earth magnets. Whether the remanence survives in an open body depends on the coercivity compared with the body's own demagnetizing field. The measured loop depends on temperature and on how fast the field is swept. A sample at rest on a remanent branch produces no continuous hysteresis heat. Driving the loop repeatedly dissipates heat.

### 4.3 Established Quantitative Boundaries

- **Measured.** Coercivity of soft magnets [S1]: permalloy and mumetal 0.3–2 A/m; highly purified iron 1–2 A/m; grain-oriented Fe–Si 4–15 A/m; polycrystalline iron 10–100 A/m; non-oriented Fe–Si 30–80 A/m; impure iron a few hundred A/m.
- **Measured.** Coercivity of hard magnets. One alnico-8-type alloy after full heat treatment: 1707 Oe [S2]. The first sintered Nd-Fe-B magnet: \(B_r = 1.23\) T, \(H_{cJ} = 960\) kA/m [S3]. A current N50 grade: \(\mu_0 H_c\) about 1.2 T; with 30 % of the Nd replaced by Dy, 3.0 T [S4].
- **Computed here.** In one unit: 1707 Oe is 136 kA/m; 1.2 T is 955 kA/m; 3.0 T is 2.39 MA/m; 960 kA/m is \(\mu_0 H_{cJ} = 1.21\) T. From permalloy (0.3–2 A/m) to the first sintered Nd-Fe-B magnet (960 kA/m) the ratio is \(4.8\times10^{5}\) to \(3.2\times10^{6}\), which is 5.7 to 6.5 decades, with iron, electrical steel and alnico in between.
- **Convention.** The soft/hard boundary. One review calls a magnet soft below 1000 A/m and hard above it [S6]; another calls a material soft when its coercivity is of the order of the Earth's field, about 40 A/m, or lower [S1]. Both are cuts on a continuous scale.
- **Measured.** Coercivity follows microstructure. In iron and Fe–Si the coercive field is the field at which domain walls unpin from defects [S1], and near it wall motion is the dominant magnetization mechanism [S7]. Purity moves iron between a few hundred A/m and 1–2 A/m [S1]. In the alnico alloy above, heat treatment moved the intrinsic coercivity from 35 Oe to 476 Oe to 1707 Oe [S2].
- **Model (demagnetizing-field criterion).** A magnet that keeps its remanence in any shape needs a coercivity above half its magnetization, and preferably above the magnetization itself. Alnico falls short of that and needs a shape that keeps its demagnetizing field below its coercive field [S8].
- **Computed here.** \(H_c/M_s\). First sintered Nd-Fe-B magnet: 960 kA/m over \(M_s = 1.61\,\mathrm{T}/\mu_0 = 1.28\) MA/m gives 0.75 [S3][S5]. Polycrystalline iron: 10–100 A/m over \(2.15\,\mathrm{T}/\mu_0 = 1.71\) MA/m gives \(5.8\times10^{-6}\) to \(5.8\times10^{-5}\) [S1][S5].
- **Measured.** Curie temperature, where the spontaneous magnetization vanishes. Iron: 770 °C (1043 K) [S1] or 1044 K [S5]. \(\mathrm{Nd_2Fe_{14}B}\): 585 K in the discovery paper [S3] and in one tabulation [S5]; 312 °C, 588 K and 320 °C in three reviews, a span of 585–593 K [S9][S8][S4]; 565 K and 558 K in two other opened papers [S10][S11].
- **Measured.** Anisotropy constant of \(\mathrm{Nd_2Fe_{14}B}\), extracted from fits to magnetization curves: \(K_1 = 4.3\) MJ/m³ [S8][S11] to 4.9 MJ/m³ [S5]; the 1984 paper estimated about 3.5 MJ/m³ [S3]. \(\mu_0 M_s = 1.61\) T [S5][S8].
- **Model (uniaxial \(K_1\) only, \(H_a = 2K_1/\mu_0 M_s\)).** Anisotropy field of \(\mathrm{Nd_2Fe_{14}B}\): 6.7 T [S11], 7.2 T [S9], about 7.5 T [S4], 7.6 T [S5], 7.7 T [S12].
- **Measured.** Coercivity against that field. Commercial sintered Nd-Fe-B reaches about 0.2 \(H_a\); the N50 figure of 1.2 T is about 15 % of 7.5 T [S4]. As a general statement for permanent magnets, years of development are needed to reach 20–30 % of \(H_a\) [S8]. One text puts the overestimate at one order of magnitude [S5]. The maximum possible coercive field is never reached experimentally [S11].
- **Model (micromagnetic interpretation).** Two coercivity mechanisms are distinguished: nucleation of a reversed region, and pinning of domain walls at inhomogeneities [S5]. Sintered Nd-Fe-B with 5–10 µm grains was first classed as nucleation-controlled from its initial magnetization curve; the same review concludes from the angular dependence of coercivity that exchange-coupled sintered and hot-deformed magnets are pinning-type at grain boundaries [S4]. \(\mathrm{Sm_2Co_{17}}\)-type magnets are pinning-controlled [S8].
- **Convention.** Loop area. The energy lost per unit volume in one complete cycle is the area of the loop, \(W = \oint H\,dB = \oint H\,dJ\) with \(J = \mu_0 M\); the \(\mu_0 H\,dH\) term integrates to zero [S1][S6]. This is an energy identity.
- **Measured.** Cost of a single-bit operation. The Landauer limit for an irreversible single-bit operation is \(k_BT\ln 2\), 2.8 zJ at 300 K. In Permalloy nanomagnets smaller than 100 nm the dissipation, from integrated \(m\)–\(H\) loop areas (magneto-optic Kerr), was \(6.09 \pm 1.43\) zJ, or \(1.45 \pm 0.35\,k_BT\), averaged over five trials at 300 K, consistent with the limit within two standard deviations [S13].
- **Measured.** Reversal is thermally activated. In individual ferromagnetic particles of 15–30 nm at 0.1–6 K, waiting times, switching fields and telegraph noise agree with thermal activation over a single energy barrier (the Néel–Brown model), with an activation volume close to the particle volume [S14]. The switching field of a single-domain particle therefore depends on waiting time and temperature.
- **Model (simulated loops, Sharrock-like scaling).** In simulated \(M\)–\(H\) loops of recording media at sweep rates spanning five decades, the coercivity depends on the sweep rate [S15].
- **Measured.** Precession scale: \(\gamma/2\pi = 28.025\) GHz/T (CODATA 2022, free electron) [S16].
- **Convention.** Thermal stability of a grain. A particle counts as superparamagnetic when its barrier is below \(25\,k_BT\), for a measurement lasting about 100 s [S17]. Grain sizes are filed in [superparamagnetism](superparamagnetism.md).
- **Convention.** Holding a remanent point costs zero continuous power: it is a static configuration, and no source reports a dissipation at rest.

**Data confidence:** High — the coercivity classes, Curie points, loop-area identity and the gap between coercivity and anisotropy field were read in full-text reviews that agree. \(K_1\) and \(H_a\) of \(\mathrm{Nd_2Fe_{14}B}\) are Medium (fit- and model-dependent). The first-magnet numbers [S3], the single-particle result [S14] and the sweep-rate result [S15] were opened as abstracts only. No opened source gives the commercial range of \(B_r\) and \(H_{cJ}\) across sintered Nd-Fe-B grades, and the alnico figure is one alloy.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Remanence \(M_r\) or \(B_r\): the intercept at \(H = 0\) after saturation. Coercivity: the intercept at \(M = 0\) (intrinsic, \(H_{cJ}\)) or at \(B = 0\) (\(H_{cB}\)). The two differ when remanence is large: 960 against 880 kA/m in the first sintered Nd-Fe-B magnet [S3].
- Dissipated energy density per complete cycle [S1]:

  \[
  W = \oint H\,dB = \oint H\,dJ
  \]

- Coherent rotation (Stoner–Wohlfarth) [S18][S5]. For an aligned uniaxial particle the energy minimum of the magnetized state vanishes at

  \[
  H_N = \frac{2K_1}{\mu_0 M_s}
  \]

  and the loop is rectangular with \(H_c = H_N\). For a random ensemble of uniaxial particles \(H_c = 0.479\,H_a\) [S5]. Measured coercivities are 15–30 % of \(H_a\) (§4.3).
- Empirical form used for real magnets: \(H_c(T) = \alpha H_a(T) - N_\mathrm{eff} M_s(T)\), with \(\alpha\) for defects and grain misalignment and \(N_\mathrm{eff}\) for the local demagnetizing field [S4].
- Thermal escape over a barrier \(\Delta E\): \(\tau = \tau_0\exp(\Delta E/k_BT)\), with the blocked/unblocked cut at \(\Delta E = 25\,k_BT\) for a measuring time of about 100 s [S17]. Single-particle switching follows this law [S14]; coercivity against sweep rate is fitted with a Sharrock-like scaling [S15].
- Landauer bound on an irreversible single-bit operation: \(E \ge k_BT\ln 2\) [S13].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** An ordered ferromagnetic volume with an anisotropy barrier. Switching has been measured on single particles of 15–30 nm, and a Permalloy element under 100 nm serves as one bit. A bulk loop is the sum over grains and walls, each reversing at its own field. The remanent branch is usable in an open body when the coercivity exceeds the demagnetizing field: \(H_c/M_s\) is 0.75 for sintered Nd-Fe-B and below \(10^{-4}\) for iron.

- **Clock rate / latency.** The carrier is precession at 28.025 GHz/T. The loop itself depends on the clock: reversal is thermally activated, so the switching field of a particle depends on waiting time and temperature, and the coercivity of a recording medium depends on sweep rate. In bulk soft material the loop is traversed by walls unpinning from defects. A coercivity quoted without a sweep rate and a temperature is a convention.

- **Energy barriers or thresholds.** The barrier that protects remanence is the anisotropy barrier of the [permanent-magnet latch](permanent-magnet-latch.md): \(K_1V\) plus shape terms. The write field is the coercivity, about 15–20 % of the anisotropy field in sintered Nd-Fe-B. Hold cost is zero. The loop area \(\oint H\,dB\) is the cost of a full major-loop write. The minimum is lower: a single-domain Permalloy bit has been operated at \(1.45\,k_BT\), so the measured floor for one bit is of order \(k_BT\).

- **Dominant failure modes.**
  - **Crossover** — soft limit: coercivity runs continuously over about six orders of magnitude, from 0.3 A/m to about \(10^6\) A/m. Remanence in an open body is lost when the coercivity is below the body's demagnetizing field; retention in any shape needs \(H_c > M_s/2\). The soft/hard line at 1000 A/m (or 40 A/m) is a convention. The metal stays ferromagnetic.
  - **Threshold** — Curie point: \(T > T_C\) (iron 1043–1044 K; \(\mathrm{Nd_2Fe_{14}B}\) 585 K, sources 585–593 K). The spontaneous magnetization vanishes and the loop with it. A phase transition.
  - **Crossover** — thermal, volume: the relaxation time \(\tau_0\exp(KV/k_BT)\) changes continuously with grain volume. The cut at \(KV = 25\,k_BT\) is the convention for a 100 s measurement. Sizes are in [superparamagnetism](superparamagnetism.md).
  - **Crossover** — field: reversal at the coercive field. For one ideal aligned grain at zero temperature this is a threshold, the field \(H_N\) at which the energy minimum vanishes. In a real magnet it is smeared twice: grains and pinning sites reverse over a distribution of fields, and each reversal is thermally activated, so the measured \(H_c\) moves with sweep rate and temperature. This is the write step of the cycle and leaves the hardware intact.
  - **Crossover** — microstructure: \(H_c\) moves continuously with defect content and heat treatment (iron between 1–2 and a few hundred A/m; one alnico between 35 and 1707 Oe). Mechanical or chemical damage acts through this term. No measured threshold is filed.

- **Emergent constant or stable output.** A remanent magnetization at \(H = 0\) held at zero continuous power, and a dissipation \(\oint H\,dB\) each time the major loop is cycled.

### 4.6 Internal Consistency Notes

The mapping closes on the distinction the parent latch needs: ferromagnetic order and a usable directional latch are different properties. Iron is ordered up to 1043 K with \(H_c/M_s\) below \(10^{-4}\); sintered Nd-Fe-B is ordered only up to 585 K with \(H_c/M_s = 0.75\).

Sourcing changed five things. First, the soft limit is a crossover: coercivity is a continuum and the soft/hard line is a convention. The first version gave the class boundary, \(10^2\)–\(10^3\) A/m, as the typical soft value; typical values are 0.3–100 A/m. Second, the write field is also a crossover. It is a threshold only for one ideal grain at zero temperature, and in a real magnet it depends on sweep rate and temperature. Third, the loop area is the cost of a full major-loop write. The first version called it the write/erase cost without qualification; a single-domain bit has been operated near the Landauer bound. Fourth, \(K_1 = 4.5\) MJ/m³ and \(\mu_0H_a = 7\)–8 T were not found in any opened source; the opened values are 4.3–4.9 MJ/m³ and 6.7–7.7 T. Fifth, the gap between \(H_c\) and \(H_a\) now has numbers, and the Curie temperatures carry a spread of a few kelvin.

The mesoscale gap remains, and it is open in the literature as well. Measured \(H_c\) is 15–30 % of \(H_a\), the empirical form \(\alpha H_a - N_\mathrm{eff}M_s\) carries two fitted microstructural numbers, and reviews disagree on whether sintered Nd-Fe-B is controlled by nucleation or by pinning at grain boundaries. QSA has no buffer or barrier specification that produces \(H_c\). The Curie threshold and the zero-hold-power clause do not depend on closing that gap.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the remanent branch, the loop-area dissipation, \(T_C\) and zero hold power translate into barrier, failure and output specifications, and the identification of the loop as the latch cycle holds. The open items are the mesoscale origin of \(H_c\), whose mechanism is contested in the literature, and the lack of a write field that is independent of the clock.

## Related entries

- [permanent-magnet-latch](permanent-magnet-latch.md) — the held directional state whose write / erase cycle this loop is
- [superparamagnetism](superparamagnetism.md) — thermal relaxation of the remanent branch in a small grain; owns the sizes
- [magnetic-domains](magnetic-domains.md) — walls whose unpinning carries reversal near the coercive field in bulk soft material
- [shape-anisotropy](shape-anisotropy.md) — geometry contribution to the barrier that the loop is written over
- [exchange-bias](exchange-bias.md) — a second latch that shifts this loop along \(H\)
- [magnetostriction](magnetostriction.md) — lattice–moment coupling on the same ordered body
- [curie-paramagnetism](curie-paramagnetism.md) — unlocked ensemble above \(T_C\); contrast case

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Fiorillo, Bertotti, Appino and Pasquale, "Soft Magnetic Materials", *Wiley Encyclopedia of Electrical and Electronics Engineering* (2016), accepted version](https://iris.inrim.it/bitstream/11696/54676/4/SoftMagneticMaterials_Wiley_Enciclopedia_2016_postprint.pdf) | full-text | Review chapter. Coercivity table for soft magnets; iron 1–2 A/m purified and a few hundred impure; soft defined by the Earth's field; iron Curie point 770 °C; loop area as energy loss; coercive field as wall unpinning. |
| S2 | [Zhou et al., arXiv:1810.12580 (2018)](https://arxiv.org/abs/1810.12580) | full-text | Alnico-8-type alloy: intrinsic coercivity 35 Oe, 476 Oe after magnetic annealing, 1707 Oe after draw. |
| S3 | [Sagawa, Fujimura, Togawa, Yamamoto and Matsuura, *J. Appl. Phys.* 55, 2083 (1984)](https://pubs.aip.org/jap/article/55/6/2083/13308/New-material-for-permanent-magnets-on-a-base-of-Nd) | abstract | First sintered Nd-Fe-B magnet: remanence 1.23 T, coercivities 880 and 960 kA/m; Curie temperature 585 K; anisotropy about 3.5 MJ/m³. |
| S4 | [Li, Sepehri-Amin, Sasaki, Ohkubo and Hono, *Sci. Technol. Adv. Mater.* 22, 386 (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8183520/) | full-text | Coercivity about 0.2 of the anisotropy field; N50 at 1.2 T against 7.5 T; 3.0 T with Dy; nucleation against grain-boundary pinning; 5–10 µm grains; the alpha and N-eff form; Curie point 320 °C. |
| S5 | [Skomski, "Micromagnetic Spin Structure", in *Spin Electronics*, Lecture Notes in Physics 569, 204 (2001)](https://boulderschool.yale.edu/sites/default/files/files/heinonen_skomski.pdf) | full-text | Saturation polarization, Curie temperature and anisotropy tables (Fe, Nd2Fe14B); anisotropy field 7.6 T; coherent-rotation nucleation field; 0.479 for a random ensemble; overestimate by one order of magnitude; nucleation and pinning. |
| S6 | [Silveyra, Ferrara, Huber and Monson, *Science* 362, eaao0195 (2018), submitted version](https://iris.inrim.it/bitstream/11696/59709/4/Soft%20magnetic%20materials%20for%20a%20sustainable%20and%20electrified%20world_preprint%20copy.pdf) | full-text | Soft/hard boundary at 1000 A/m; loop area as the energy lost per cycle. |
| S7 | [Durin and Zapperi, "The Barkhausen effect", arXiv:cond-mat/0404512 (2004)](https://arxiv.org/abs/cond-mat/0404512) | full-text | Around the coercive field, wall motion is the dominant and often the only magnetization mechanism. |
| S8 | [Coey, *Engineering* 6, 119 (2020)](https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2018.11.034) | full-text | Nd2Fe14B anisotropy 4.3 MJ/m³, polarization 1.61 T, Curie point 588 K; coercivity of 20–30 % of the anisotropy field; coercivity above half the magnetization for a shape-independent magnet; alnico needs a special shape; Sm2Co17 pinning-controlled. |
| S9 | [Horikawa, Yamazaki, Matsuura and Sugimoto, *Sci. Technol. Adv. Mater.* 22, 729 (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8451657) | full-text | Nd2Fe14B anisotropy field 7.2 T and Curie point 312 °C. Read through a fetch tool, not checked against the raw page. |
| S10 | [Kreyssig et al., arXiv:0901.3515 (2009)](https://arxiv.org/abs/0901.3515) | full-text | Quotes 565 K for the Nd2Fe14B Curie temperature. |
| S11 | [Fischbacher et al., *J. Phys. D* 51, 193002 (2018), arXiv:1903.11922](https://arxiv.org/abs/1903.11922) | full-text | Ideal nucleation field 6.7 T for 4.3 MJ/m³ and 1.61 T; the maximum coercive field is never reached; quotes 558 K for the Curie temperature. |
| S12 | [de Campos and de Castro, *Arch. Electr. Eng.* 73, 1087 (2024)](https://czasopisma.pan.pl//Content/133391/PDF/14_2k.pdf) | full-text | Nd2Fe14B anisotropy field 77 kOe. |
| S13 | [Hong, Lambson, Dhuey and Bokor, *Science Advances* 2, e1501492 (2016)](https://escholarship.org/uc/item/5fm3w6xx) | full-text | Landauer limit 2.8 zJ at 300 K; 6.09 ± 1.43 zJ (1.45 ± 0.35 kT) dissipated per single-bit operation in Permalloy nanomagnets, from integrated loop areas. |
| S14 | [Wernsdorfer et al., *Phys. Rev. Lett.* 78, 1791 (1997)](https://doi.org/10.1103/PhysRevLett.78.1791) | abstract | Single 15–30 nm particles at 0.1–6 K reverse by thermal activation over one barrier (Néel–Brown); activation volume close to the particle volume. |
| S15 | [Plumer, Leblanc, Whitehead and van Ek, arXiv:1203.3340 (2012)](https://arxiv.org/abs/1203.3340) | abstract | Simulated loops of recording media over five decades of sweep rate; coercivity depends on sweep rate, with Sharrock-like scaling. |
| S16 | [NIST, CODATA 2022 recommended value, electron gyromagnetic ratio in MHz/T](https://physics.nist.gov/cgi-bin/cuu/Value?gammaebar) | full-text | 28 024.951 MHz/T. |
| S17 | [Kachkachi, arXiv:cond-mat/0307457 (2003)](https://arxiv.org/abs/cond-mat/0307457) | full-text | Superparamagnetic range is a barrier below 25 kT for a measuring time of about 100 s, which depends on the apparatus. |
| S18 | [Stoner and Wohlfarth, *Phil. Trans. R. Soc. Lond. A* 240, 599 (1948)](https://doi.org/10.1098/rsta.1948.0007) | cited-only | Primary for coherent rotation. Publisher page not reachable; the formulas were read in S5 and S8. |
