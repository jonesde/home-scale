---
id: muon-catalyzed-fusion
title: Muon-Catalyzed Fusion (Mass-Rescaled Nuclear Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - clock-latency
  - spatial-buffer
confidence_data: high
confidence_mapping: high
review_depth: standard
related:
  - pair-production
  - ionization-threshold
  - photoelectric-threshold
  - pyroelectric-fusion
  - deuteron-photodisintegration
updated: 2026-11-11
---

# Muon-Catalyzed Fusion (Mass-Rescaled Nuclear Gate)

### 4.1 Effect Name

Muon-catalyzed fusion (mass-rescaled nuclear gate)

### 4.2 Macroscopic Observation

A negative muon that stops in a hydrogen-isotope target replaces an electron, forms a muonic atom and then a muonic molecule with two nuclei, and the two nuclei fuse. The muon is usually released and repeats the cycle. Fusion neutrons appear at a rate set by the number of stopped muons and the number of cycles each completes. Each muon stops catalyzing when it decays or when it stays bound to a helium nucleus. The effect is observed in solid, liquid and gaseous deuterium–tritium, with no metal host. No fusion cycle of this kind is reported from a hydrogen target without muons.

### 4.3 Established Quantitative Boundaries

- **Measured.** Muon rest energy \(m_\mu c^2 = 105.6583755(23)\,\mathrm{MeV}\) and mean life \(\tau_\mu = 2.1969811(22)\times 10^{-6}\,\mathrm{s}\) (PDG 2026) [S1]. Muon–electron mass ratio \(m_\mu/m_e = 206.7682827(46)\) (CODATA 2022) [S2].
- **Model (Bohr scaling with the lepton mass).** The muon occupies orbitals smaller than the electron's by \(m_\mu/m_e \approx 207\), before reduced-mass corrections; a muonic deuterium atom is about 200 times more compact than hydrogen, and the internuclear distance in a muonic molecular ion is about 500 times smaller than in \(\mathrm{H_2^+}\) [S8][S9].
- **Computed here.** \(a_0/(m_\mu/m_e) = 256\,\mathrm{fm}\), from \(a_0 = 5.29177\times 10^{-11}\,\mathrm{m}\) [S3] and the ratio in [S2]. The muon decay rate is \(\lambda_0 = 1/\tau_\mu = 4.55\times 10^{5}\,\mathrm{s^{-1}}\).
- **Measured.** Reaction: \(d + t \to \alpha + n + 17.6\,\mathrm{MeV}\), with 14.1 MeV on the neutron and 3.5 MeV on the alpha [S9].
- **Measured.** Yield. About 150 fusions per muon in cold, dense deuterium–tritium (LAMPF) [S4]; quoted as \(150 \pm 20\) [S9]. The average measured yield rose from 80 in 1984 to 150 in 1985 [S5]. Reviews state "over 100" as the reproduced class [S6][S9]. The cycle has been observed from 3 K to 800 K [S9].
- **Measured.** Cycling rate \(\lambda_c \approx 10^{8}\,\mathrm{s^{-1}}\) at the best confirmed conditions [S7].
- **Model (coupled-channel three-body calculation).** Fusion inside a formed \(dt\mu\) ion proceeds at about \(10^{12}\,\mathrm{s^{-1}}\) (\(1.15\times 10^{12}\,\mathrm{s^{-1}}\) computed) [S8][S10].
- **Computed here.** \(10^{12}\,\mathrm{s^{-1}} \times \tau_\mu = 2.2\times 10^{6}\): the nuclear step is about a million times faster than muon decay. \(\lambda_c\tau_\mu = 220\): the atomic and molecular steps of the cycle are only about 200 times faster.
- **Measured.** Molecule formation. Fusion has been observed for every pair of hydrogen isotopes except two protons. Only \(dd\mu\) and \(dt\mu\) form by a resonant process; the non-resonant process is slower than muon decay, so it gives less than one fusion per muon. The \(dt\mu\) formation rate depends non-linearly on target density [S6].
- **Model (variational three-body calculation).** The resonant state of \(dt\mu\) is bound by 0.660 eV. That energy is taken up by rotation and vibration of the host \(\mathrm{D_2}\) or DT molecule (dissociation energy about 4.5 eV) in which the muonic ion forms [S6].
- **Measured.** Effective sticking (fraction of fusions after which the muon stays on the alpha): 0.45 % in the molecular cycle [S7]; \((0.35 \pm 0.05)\,\%\) at the highest densities, against about 0.6 % as the smallest value two years earlier [S5]; about 0.6 % in a 2026 review [S8]. It falls with rising density [S5][S9]. For the \(d + d \to {}^{3}\mathrm{He} + n\) branch it is 12.2 % [S7].
- **Model (sudden approximation on a three-body wave function).** Initial sticking, before the fast muonic helium ion can lose the muon in collisions: 1.16–1.2 % with an adiabatic wave function, 0.89 % non-adiabatic, 0.92 % as the accepted value in 1991 [S6][S7], 0.857 % in a 2023 calculation [S10]. Measured effective values are 10–50 % below what these models give after reactivation [S6][S9].
- **Model (steady-state cycle kinetics).** Under optimum conditions the limit from muon decay and the limit from sticking are each about 300 fusions [S6].
- **Computed here.** Two limits of 300 combine to \(1/(1/300 + 1/300) = 150\). With \(\lambda_c = 10^{8}\,\mathrm{s^{-1}}\) and sticking of 0.45 %, \(1/(0.0045 + \lambda_0/\lambda_c) = 110\).
- **Computed here.** Energy released per muon at the record yield: \(150 \times 17.6\,\mathrm{MeV} = 2.64\,\mathrm{GeV}\), 25 times the muon rest energy ([S7] quotes 2.7 GeV).
- **Model (accelerator and hadronic-cascade estimates; no muon source of this kind has been built).** Energy cost per stopped negative muon: about 10 GeV thermal, or about 5 GeV electrical [S7][S8]; 8 GeV is described as soft, with other estimates of 5 GeV and as low as 2 GeV [S6]. Break-even is put at about 300 or more fusions per muon for 5 GeV [S8].
- **Computed here.** \(5\,\mathrm{GeV}/17.6\,\mathrm{MeV} = 284\) fusions to return the electrical cost as heat; \(8\,\mathrm{GeV}/17.6\,\mathrm{MeV} = 455\), and 1,140 if only 40 % of the heat becomes electricity, the conversion argued in [S6]. The record yield is a factor of 1.9 to 7.6 short.
- **Measured.** Discovery: fusion of a proton and a deuteron catalyzed by a muon, found by chance in a hydrogen bubble chamber in late 1956 [S6][S8]; the primary is [S12].

**Data confidence:** High — the muon constants, the cycle, the yield of about 150 and sticking of 0.35–0.6 % are reproduced and were read in full-text reviews and one primary abstract. The standard review [S11] and the discovery paper [S12] were not opened. Tabulated formation rates for each isotope pair were not found. The muon production cost is an estimate, not a measurement.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Mass scaling of the bound orbit:

  \[
  a_\mu \approx \frac{m_e}{m_\mu}\,a_0 \approx \frac{a_0}{207}
  \]

  before reduced-mass corrections [S8].
- Fusions per muon in the steady state [S6][S7][S8]:

  \[
  Y \approx \frac{1}{\omega_s + \lambda_0/\lambda_c}
  \]

  with \(\omega_s\) the effective sticking fraction, \(\lambda_0 = 1/\tau_\mu\) and \(\lambda_c\) the cycling rate. The two loss terms add. \(1/\omega_s\) and \(\lambda_c\tau_\mu\) are each an upper bound, and \(Y\) is below both.
- Effective sticking from initial sticking \(\omega_s^0\) and reactivation probability \(R\): \(\omega_s = \omega_s^0(1 - R)\) [S6].
- Energy balance: \(Y \times 17.6\,\mathrm{MeV}\) released against the cost of one muon [S7].

These relations describe the observed cycle. They do not derive \(m_\mu\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One muon and two hydrogen-isotope nuclei make the fusing ion. The fast cycle needs one more object: a host \(\mathrm{D_2}\) or DT molecule that absorbs the 0.66 eV binding energy when the ion forms. The hardware is therefore a few bodies, not a collective medium. Target density is capacity: it raises \(\lambda_c\) and lowers sticking.

- **Clock rate / latency.** \(\tau_\mu = 2.197\,\mu\mathrm{s}\) is the stop. Within it, the nuclear step takes about \(10^{-12}\,\mathrm{s}\) and one full cycle about \(10^{-8}\,\mathrm{s}\). The cycle time, set by atomic and molecular steps, is the clock that competes with decay.

- **Energy barriers or thresholds.** Not a latch. The muon's mass shrinks the bound orbit by about 207, which brings the nuclei close enough to fuse in about a picosecond. The product leaves and the muon is reused. No state is held.

- **Dominant failure modes.**
  - **Threshold** — no muon: the cycle is defined by a stopped muon, and no muon-free hydrogen target is reported to produce it.
  - **Crossover** — decay: the muon population falls as \(e^{-t/\tau_\mu}\), \(\tau_\mu = 2.197\,\mu\mathrm{s}\).
  - **Crossover** — sticking: each fusion removes the muon with probability \(\omega_s\) of 0.35–0.6 %, so survival after \(n\) fusions is \((1-\omega_s)^n\). Together with decay, \(Y \approx 1/(\omega_s + \lambda_0/\lambda_c)\).
  - **Threshold** — isotope pair: two protons give no observed fusion. Pairs without resonant formation give less than one fusion per muon.
  - **Crossover** — density: \(\lambda_c\) rises and \(\omega_s\) falls as density rises.

- **Emergent constant or stable output.** Fusion neutrons at about 100–150 per stopped muon in dense deuterium–tritium, while muons are present.

### 4.6 Internal Consistency Notes

The mapping has the shape of [pair production](pair-production.md): a named extra constituent is required hardware. Here it is the muon.

It is not a latch. With no muons there is no cycle, and nothing is retained after the last muon decays.

Sourcing changed five things. The yield relation was written as the smaller of \(1/\omega_s\) and \(\lambda_c\tau_\mu\); the two losses add, and at measured values the correct relation gives about half of that (110 against 220). Sticking was called the hard ceiling; at optimum conditions decay during the cycle limits the yield about equally. The hardware was given as one muon and two nuclei; the fast cycle also needs a host molecule for resonant formation. The d–d sticking figure is 12.2 %, and the d–t range is 0.35–0.6 % and falls with density. The energy balance, which the first version set aside, is now stated: the record yield releases 2.64 GeV per muon against an estimated cost of 5–10 GeV.

This entry is not the object discussed in the [EM-LENR](../application/EM-LENR.md) application. That application concerns hydrogen in a metal with no muon source. The facts here bound it from the side of established nuclear physics: the one demonstrated low-temperature fusion cycle requires a particle that costs gigaelectronvolts to make and lasts 2.2 µs.

\(m_\mu\) and \(\tau_\mu\) are taken from PDG. Measured sticking remains 10–50 % below theory; that gap is open in the standard description as well.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the muon requirement, the lifetime clock, the additive decay and sticking losses, and the isotope ordering are measured and translate into hardware, clock and failure-envelope specifications. The open items are the sticking discrepancy and the muon production cost.

## Related entries

- [pair-production](pair-production.md) — another conversion that needs a named extra constituent
- [pyroelectric-fusion](pyroelectric-fusion.md) — D–D fusion by acceleration, with no muon
- [deuteron-photodisintegration](deuteron-photodisintegration.md) — a photon unbinding the deuteron
- [ionization-threshold](ionization-threshold.md) — electronic unbinding of hydrogen
- [photoelectric-threshold](photoelectric-threshold.md) — a one-electron gate

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Particle Data Group (Takahashi et al.), *Int. J. Mod. Phys. A* 41, 2630011 (2026), muon listing](https://pdg.lbl.gov/2026/listings/rpp2026-list-muon.pdf) | full-text | Muon rest energy 105.6583755 MeV and mean life 2.1969811 µs. |
| S2 | [NIST CODATA 2022, muon-electron mass ratio](https://physics.nist.gov/cgi-bin/cuu/Value?mmusme) | full-text | Mass ratio 206.7682827(46). |
| S3 | [NIST CODATA 2022, Bohr radius](https://physics.nist.gov/cgi-bin/cuu/Value?bohrrada0) | full-text | Bohr radius used for the 256 fm figure. |
| S4 | [Jones, *Nature* 321, 127 (1986)](https://www.nature.com/articles/321127a0) | abstract | Muons replace the electrons and form muonic molecules; about 150 fusions per muon in cold, dense deuterium–tritium. |
| S5 | [Jones, *Fusion Technol.* 10, 157 (1986)](https://wx1.ans.org/pubs/journals/download/a_24757) | full-text | Workshop summary: sticking (0.35 ± 0.05) % at high density against about 0.6 % in 1984; average yield 80 rising to 150; density dependence of sticking. |
| S6 | [Cohen, "Muon-catalyzed fusion theory: introduction and review", LA-UR-89-4070 (1989)](https://library.sciencemadness.org/lanl2_a/lib-www/la-pubs/00364559.pdf) | full-text | Over 100 fusions per muon; all isotope pairs except two protons; resonant formation only for ddµ and dtµ; 0.660 eV state and host molecule; decay and sticking limits each about 300; initial sticking 1.16 % and 0.89 %; theory above experiment; 8, 5 and 2 GeV cost estimates and the 40 % conversion argument; the 1956–57 discovery (secondary). |
| S7 | [Rafelski, "Energy related applications of elementary particle physics", DOE/ER/13858-3 (1991)](https://www.osti.gov/servlets/purl/6694614) | full-text | Yield 150 and cycling rate 1e8 per second; 2.7 GeV per muon; sticking 0.45 % for d–t and 12.2 % for d–d; initial sticking 0.92 %; cost about 10 GeV thermal; yield relation. |
| S8 | [Rafelski and Steinmetz, "Science of nuclear fusion: insights and ideas", arXiv:2609.01366 (2026)](https://arxiv.org/abs/2609.01366) | full-text | Secondary review: orbit scaling by 207 and molecule about 500 times smaller; fusion rate about 1e12 per second; sticking about 0.6 %; yield relation; about 5 GeV electrical per muon and break-even near 300 fusions; discovery history. |
| S9 | [Kalow et al. (MuFusE), arXiv:2606.05333 (2026)](https://arxiv.org/abs/2606.05333) | full-text | 17.6 MeV split 14.1 and 3.5 MeV; 150 ± 20 fusions per muon; observed from 3 K to 800 K; sticking falls with density and lies 10–50 % below models; muonic atom about 200 times more compact. |
| S10 | [Kamimura, Kino and Yamashita, *Phys. Rev. C* 107, 034607 (2023), arXiv:2112.08399](https://arxiv.org/abs/2112.08399) | abstract | Computed dtµ fusion rate 1.15e12 per second and initial sticking 0.857 %. |
| S11 | [Breunlich, Kammel, Cohen and Leon, *Annu. Rev. Nucl. Part. Sci.* 39, 311 (1989)](https://doi.org/10.1146/annurev.ns.39.120189.001523) | cited-only | Standard review of the field; not opened (access refused). Its content is represented here by S6, written by one of its authors in the same year. |
| S12 | [Alvarez et al., *Phys. Rev.* 105, 1127 (1957)](https://doi.org/10.1103/PhysRev.105.1127) | cited-only | Discovery of muon-catalyzed p–d fusion in a hydrogen bubble chamber; not opened; described in S6 and S8. |
