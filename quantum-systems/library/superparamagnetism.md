---
id: superparamagnetism
title: Superparamagnetism (Thermal Loss of Direction in a Small Grain)
status: formal
family: latched-order
constraints:
  - spatial-buffer
  - energy-barrier
  - thermal
  - mechanical-lattice
confidence_data: high
confidence_mapping: high
review_depth: deep
related:
  - permanent-magnet-latch
  - ferromagnetic-hysteresis
  - magnetic-domains
  - shape-anisotropy
  - curie-paramagnetism
  - exchange-bias
updated: 2026-11-11
---

# Superparamagnetism (Thermal Loss of Direction in a Small Grain)

### 4.1 Effect Name

Superparamagnetism (thermal loss of direction in a small grain)

### 4.2 Macroscopic Observation

A fine ferromagnetic or ferrimagnetic powder that would hold a remanent moment as larger grains shows no remanence and no coercivity on the timescale of the measurement. Magnetization follows an applied field reversibly and saturates at large field; when the field is removed the net moment returns to zero. Cooling the same particles restores hysteresis below a blocking temperature. Measuring faster does the same.

### 4.3 Established Quantitative Boundaries

- **Model (Néel–Brown thermal activation).** The moment of a single-domain grain reverses with characteristic time \(\tau = \tau_0\exp(KV/kT)\); it appears blocked when \(\tau\) exceeds the measurement time \(\tau_m\), which gives \(T_B = KV/[k\ln(\tau_m/\tau_0)]\) [S1].
- **Measured.** The model holds for one particle at a time: waiting-time, switching-field and telegraph-noise measurements on individual 15–30 nm particles at 0.1–6 K agree with thermal activation over a single barrier, with an activation volume close to the particle volume [S14].
- **Convention.** The attempt time \(\tau_0\) is a fitted constant, usually taken as 10⁻⁹–10⁻¹⁰ s; values as short as 10⁻¹³ s and attempt frequencies of 10⁹–10¹² s⁻¹ are used [S1][S12][S3].
- **Convention.** Measurement windows: about 100 s for dc magnetometry, 10⁻⁹–10⁻⁷ s for Mössbauer spectroscopy, 10⁻¹²–10⁻⁸ s for neutron scattering [S1]. The same grain can be blocked in one apparatus and unblocked in another.
- **Convention.** "\(KV = 25\,kT\)" is \(\ln(\tau_m/\tau_0)\) for a 100 s measurement with \(\tau_0 = 10^{-9}\) s, or equally for 1 s with an attempt frequency of 10¹¹ s⁻¹ [S1][S3]. The usual primary citation is [S5], whose derivation was not opened.
- **Computed here.** \(\ln(100\,\mathrm{s}/10^{-9}\,\mathrm{s}) = 25.3\). Ten years with the same \(\tau_0\) gives 40.3. A Mössbauer window of 10⁻⁸ s gives 2.3. The first version said 25 corresponds to "hours to years"; it corresponds to about a hundred seconds.
- **Measured.** Magnetic recording: thermal decay sets in at \(K_uV/kT \approx 35 \pm 2\), and about 60 is required for ten-year storage of a recorded pattern [S6][S17]. The first version quoted "40–60" as the convention; 40 was not found as a stated figure.
- **Measured.** Anisotropy constants at room temperature: \(\mathrm{Nd_2Fe_{14}B}\) 4.3–4.9 MJ m⁻³ [S3][S4]; magnetite \(K_1 = -1.35 \times 10^{4}\) J m⁻³, cubic [S7][S11]; Fe 48, Co 530, Ni −5 kJ m⁻³ [S2].
- **Model (\(KV = 25\,kT\) for a sphere, bulk \(K_1\) taken as the barrier).** Room-temperature blocking diameter \(d = (150\,kT/\pi K_1)^{1/3}\): Fe 16 nm, Co 7 nm, Ni 34 nm as tabulated [S2].
- **Computed here.** The same formula at 300 K:

  | Material | \(K\) used | Sphere diameter at 25 \(kT\) |
  |---|---|---|
  | \(\mathrm{Nd_2Fe_{14}B}\) | 4.3–4.9 MJ m⁻³ | 3.4–3.6 nm (volume 2.1–2.4 × 10⁻²⁶ m³; cube edge 2.8–2.9 nm) |
  | \(\mathrm{Nd_2Fe_{14}B}\), 60 \(kT\) | 4.3–4.9 MJ m⁻³ | 4.6–4.8 nm |
  | Magnetite | 13.5 kJ m⁻³ | 24.5 nm |
  | Magnetite, cubic barrier \(K_1/12\) | 1.1 kJ m⁻³ | 56 nm |

  The anisotropy of \(\mathrm{Nd_2Fe_{14}B}\) is 320–360 times that of magnetite, so its stable volume is that much smaller and its diameter about seven times smaller. The first version had this backwards ("magnetite smaller") and gave \(\mathrm{Nd_2Fe_{14}B}\) as about 30 nm, ten times too large. No opened source states a \(\mathrm{Nd_2Fe_{14}B}\)-specific blocking diameter; the figure above is this file's arithmetic on sourced \(K_1\).
- **Model (cubic anisotropy).** For \(K_1 < 0\) the barrier between easy ⟨111⟩ directions is \(K_1/12\) per unit volume, not \(K_1\) [S7].
- **Measured and model.** Magnetite's room-temperature threshold is reported as 20–30 nm [S9], about 20 nm [S7], 23.6–29.2 nm for \(K\) of 15–8 kJ m⁻³ [S10], and about 50 nm for a cube-shaped grain on the Néel relaxation equation [S8]. The single-domain upper limit is about 76 nm for a cube and 1.4 µm at 5:1 elongation [S8].
- **Model (same formula, with wall energy against magnetostatic energy for the upper limit).** For Fe and Ni the tabulated blocking diameters (16 and 34 nm) exceed the tabulated single-domain diameters (12 and 31 nm) [S2]. On crystal anisotropy alone those metals have no size range in which a single-domain grain is stable; \(\mathrm{Nd_2Fe_{14}B}\) has one two orders of magnitude wide.
- **Computed here.** The dependence on size is steep but continuous. Near 25 \(kT\), a 10 % increase in diameter raises \(KV/kT\) by a third and the retention time by a factor of about four thousand. Going from a 100 s criterion to a ten-year criterion raises the required diameter by only 17 %.
- **Measured.** Cooling restores hysteresis. 4–5 nm magnetite: coercivity 294(10) Oe and remanence 10.1(8) emu g⁻¹ at 5 K against 12(7) Oe and zero at 300 K, with blocking near 45 K in 500 Oe [S11]. 5 nm magnetite blocks near 24 K, spread over 3–45 K; 20 nm blocks over 150–300 K [S12].
- **Model (Néel–Brown fit).** The effective anisotropy of a 5 nm magnetite particle is 356 kJ m⁻³ against the bulk 13.5 kJ m⁻³, a factor of 26 [S11].
- **Measured.** Coupling to an antiferromagnet raises the blocking temperature: 4 nm cobalt particles lose their moment at 10 K in a paramagnetic matrix and stay ferromagnetic to about 290 K in an antiferromagnetic one [S16].
- **Model.** In a fluid a second channel exists: the whole particle rotates, with \(\tau_B = 3\eta V_\mathrm{hyd}/kT\), and the two rates add [S10]. For magnetite in water the Néel channel is expected to dominate below about 10 nm; a 13.5 nm particle has a measured Brownian time of 12.6 µs at 300 K [S13].
- **Measured.** At the molecular end, \(\mathrm{Mn_{12}}\) acetate (spin 10) blocks near 3 K with a barrier of 45 cm⁻¹ and Arrhenius relaxation down to 2.1 K. Its hysteresis loop has steps every 0.46 T, attributed to thermally assisted resonant tunnelling between spin states: a relaxation channel that is not thermal activation over the barrier [S15].
- **Model (Langevin).** Unblocked magnetization follows \(M = nmL(\mu_0 mH/kT)\), with curves that superpose when plotted against \(H/T\) and no remanence or coercivity [S1].

**Data confidence:** High — the Néel–Brown form, the dependence of blocking on the measurement window, and the recovery of hysteresis on cooling are measured, including on single particles. \(\tau_0\) is a fitted convention. The origin of "25 \(kT\)" in the 1959 primary was not verified. The \(\mathrm{Nd_2Fe_{14}B}\) diameter is computed here, not taken from a published table.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Néel–Arrhenius time and blocking condition [S1]:

  \[
  \tau = \tau_0 \exp\!\left(\frac{KV}{kT}\right),\qquad KV = kT\ln(\tau_m/\tau_0)
  \]

- Uniaxial barrier \(\Delta E = K_1V\); cubic barrier \(K_1V/4\) for \(K_1 > 0\) and \(K_1V/12\) for \(K_1 < 0\) [S7].
- Langevin magnetization of the unblocked ensemble [S1].
- Brownian rotation time \(\tau_B = 3\eta V_\mathrm{hyd}/kT\); total rate \(1/\tau = 1/\tau_N + 1/\tau_B\) [S10].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** There is no minimum. There is a retention time that falls exponentially with the grain's barrier, and a size quoted for a chosen waiting time. For \(\mathrm{Nd_2Fe_{14}B}\) at room temperature and 100 s that size is 3.4–3.6 nm; for magnetite 20–50 nm depending on shape and on how the cubic barrier is counted.

- **Clock rate / latency.** Two clocks, and the effect is their ratio: the attempt time \(\tau_0\) (10⁻⁹ to 10⁻¹² s) and the observer's window \(\tau_m\) (10⁻¹² s to years). Blocking is a statement about the observer as much as about the grain.

- **Energy barriers or thresholds.** The barrier \(KV\) of the grain, with three corrections the first version did not carry: the cubic factor (a twelfth of \(K_1\) in magnetite); the effective anisotropy of a nanoparticle, which can be an order of magnitude above bulk; and the surroundings, since an antiferromagnetic matrix can raise the blocking temperature from 10 K to 290 K.

- **Dominant failure modes.**
  - **Crossover** — size, temperature and time together: \(\tau = \tau_0\exp(KV/kT)\) against \(\tau_m\). Steep in size (a factor of thousands in retention for 10 % in diameter) but with no critical value. The number 25 is a convention for one waiting time.
  - **Threshold** — parent order: \(T > T_C\), where the grain's moment itself vanishes. A grain can be superparamagnetic far below \(T_C\).
  - **Crossover** — tunnelling: in a molecular magnet below a few kelvin, relaxation speeds up at regularly spaced fields. An escape route through the barrier rather than over it.
  - **Crossover** — rotation in a fluid: Brownian relaxation removes the remanence of the suspension without the grain's own barrier failing.

- **Emergent constant or stable output.** Unblocked: a reversible, zero-remanence magnetization curve that scales with \(H/T\). Blocked: the directional state of the parent magnet. Zero continuous power either way.

### 4.6 Internal Consistency Notes

Mapping the barrier \(KV\) onto a time-dependent loss of direction is consistent with the parent entry, and the single-particle measurements show the picture holds grain by grain.

Sourcing changed the entry substantially. The headline number was wrong by a factor of ten and the magnetite comparison was reversed, which a recomputation would have caught; both are now guarded by [`analysis/computed_checks.py`](../analysis/computed_checks.py). The first version called this "the volume collapse of the latch" and compared it to a thin-film cliff. It is a crossover: the data are a smooth exponential, and the quoted size moves with the clock. The first version also said the latch hardware is unchanged and only the volume differs. Measured effective anisotropy at 5 nm is 26 times the bulk value, and an antiferromagnetic neighbour changes the blocking temperature by a factor of 29, so at this scale the barrier is a property of the grain and its surroundings together.

Two kinds of randomness appear here and should be kept apart. Thermal reversal has random waiting times that the Néel–Brown model accounts for as ignorance of the heat bath; every account of quantum mechanics agrees on that. Resonant tunnelling in \(\mathrm{Mn_{12}}\) is the other kind, where the standard theory supplies only a rate. [`Determinism.md`](../Determinism.md) takes this up.

### 4.7 Overall Confidence in the QSA Mapping

**High** — for the reading of blocking as a barrier compared with two clocks. The first version's "volume cliff" framing is withdrawn, and the effective barrier of a nanometre grain remains taken from fits rather than specified.

## Related entries

- [Permanent magnet (directional latch)](permanent-magnet-latch.md) — the same barrier in a grain large enough to hold
- [Ferromagnetic hysteresis](ferromagnetic-hysteresis.md) — remanence and coercivity go to zero on the unblocked side
- [Magnetic domains](magnetic-domains.md) — the single-domain size: the upper end of a wide stable window in hard magnets, and below the blocking size in iron and nickel
- [Shape anisotropy](shape-anisotropy.md) — a geometric contribution to the barrier
- [Exchange bias](exchange-bias.md) — an antiferromagnetic pin that raises the blocking temperature
- [Curie paramagnetism](curie-paramagnetism.md) — moments that were never held

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Kechrakos, "Magnetic Nanoparticle Assemblies", arXiv:0907.4417](https://arxiv.org/abs/0907.4417) | full-text | Néel–Arrhenius law, blocking condition, attempt time, measurement windows, Langevin behaviour. |
| S2 | [Coey, "Materials for Spin Electronics", *Lecture Notes in Physics* 569, 277 (2001)](https://boulderschool.yale.edu/sites/default/files/files/coey_spintronics.pdf) | full-text | Blocking-diameter formula and tabulated values for Fe, Co, Ni; their anisotropy constants. |
| S3 | [Bance et al., *JOM* 67, 1350 (2015), arXiv:1603.08365](https://arxiv.org/abs/1603.08365) | full-text | Nd2Fe14B anisotropy 4.30 MJ/m³ (secondary); 25 kT as 1 s with an attempt frequency of 10¹¹ Hz. |
| S4 | [Zickler et al., arXiv:1510.01958](https://arxiv.org/abs/1510.01958) | full-text | Nd2Fe14B anisotropy 4.9 MJ/m³. |
| S5 | [Bean and Livingston, *J. Appl. Phys.* 30, S120 (1959)](https://pubs.aip.org/jap/article/30/4/S120/388906/Superparamagnetism) | abstract | The usual citation for the 25 kT criterion; the derivation is in the paywalled text and was not verified. |
| S6 | [Weller and Moser, *IEEE Trans. Magn.* 35, 4423 (1999)](https://research.ibm.com/publications/thermal-effect-limits-in-ultrahigh-density-magnetic-recording) | abstract | Thermal decay onset at 35 ± 2; about 60 for ten-year storage. |
| S7 | [Tauxe, *Essentials of Paleomagnetism* (online edition), ch. 4](https://earthref.org/MagIC/books/Tauxe/Essentials/) | full-text | Magnetite anisotropy; cubic barrier fractions; threshold near 20 nm. Secondary textbook. |
| S8 | [Butler and Banerjee, *J. Geophys. Res.* 80, 4049 (1975)](https://earthref.org/ERR/43638/) | abstract | Magnetite thresholds: about 0.05 µm superparamagnetic, 0.076 µm single-domain for a cube, 1.4 µm at 5:1 elongation. |
| S9 | [Baumgartner et al., *PLoS ONE* 8, e57070 (2013)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0057070) | full-text | Magnetite superparamagnetic threshold 20–30 nm. |
| S10 | [Serantes and Baldomir, arXiv:2011.09223](https://arxiv.org/abs/2011.09223) | full-text | Magnetite 23.6–29.2 nm at 300 K; Néel and Brownian relaxation times. |
| S11 | [Goya and Morales, arXiv:1103.3784 (2004)](https://arxiv.org/abs/1103.3784) | full-text | 4–5 nm magnetite: hysteresis at 5 K and none at 300 K; effective anisotropy 356 kJ/m³ against bulk 13.5. |
| S12 | [Frandsen et al., arXiv:2101.00258](https://arxiv.org/abs/2101.00258) | full-text | Blocking of 5 nm and 20 nm magnetite; attempt times down to 10⁻¹³ s. |
| S13 | [Vajtai et al., *Nanomaterials* 14, 634 (2024), arXiv:2402.08553](https://arxiv.org/abs/2402.08553) | full-text | Néel channel expected below about 10 nm in water; Brownian time 12.6 µs at 13.5 nm. |
| S14 | [Wernsdorfer et al., *Phys. Rev. Lett.* 78, 1791 (1997)](https://doi.org/10.1103/PhysRevLett.78.1791) | abstract | Single-particle test of the Néel–Brown model. |
| S15 | [Friedman et al., *J. Appl. Phys.* 79, 6031 (1996)](https://jrfriedman.people.amherst.edu/Mn12_steps_JAP.pdf) | full-text | Mn12: spin 10, blocking near 3 K, barrier 45 cm⁻¹, steps every 0.46 T attributed to resonant tunnelling. |
| S16 | [Skumryev et al., *Nature* 423, 850 (2003)](https://www.nature.com/articles/nature01687) | abstract | 4 nm Co: blocking raised from 10 K to about 290 K by an antiferromagnetic matrix. |
| S17 | [Hono and Takahashi, "L10-FePt granular films for heat assisted magnetic recording media", ch. 5 in *Ultrahigh-Density Magnetic Recording* (Pan Stanford, 2016)](https://mdr.nims.go.jp/filesets/a78cda54-f66c-4452-82ea-d574e7f1242a/download) | full-text | Stability factor above 60 for ten years. |
