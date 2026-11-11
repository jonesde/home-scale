---
id: pyroelectric-fusion
title: Pyroelectric Fusion (Polar-Field Beam Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - field-threshold
  - thermal
confidence_data: medium
confidence_mapping: high
review_depth: standard
related:
  - muon-catalyzed-fusion
  - ferroelectric-remanence
  - dielectric-breakdown
  - deuteron-photodisintegration
updated: 2026-11-11
---

# Pyroelectric Fusion (Polar-Field Beam Gate)

### 4.1 Effect Name

Pyroelectric fusion (polar-field beam gate)

### 4.2 Macroscopic Observation

A pyroelectric crystal (\(\mathrm{LiTaO_3}\)) heated or cooled in low-pressure deuterium gas develops a potential of about 100 kV on its exposed face. A sharp tip on that face ionizes the gas, and the field accelerates deuterons into a deuterated solid target. D–D fusion in the target emits 2.45 MeV neutrons. Naranjo, Gimzewski and Putterman reported this in 2005; Geuther, Danon and Saglime reproduced it in 2006 with two crystals heated above room temperature. The neutron emission lasts while the temperature is changing and ends when the face discharges. The authors describe it as a neutron source and not a power source.

### 4.3 Established Quantitative Boundaries

- **Measured.** First report [S1]: the crystal field generates and accelerates a deuteron beam above 100 keV and above 4 nA; on a deuterated target it gives a neutron flux over 400 times background; the reaction is \(\mathrm{D + D \to {}^{3}He\,(820\,keV) + n\,(2.45\,MeV)}\), confirmed by pulse-shape analysis, proton-recoil spectroscopy and time of flight. The crystal was a single \(\mathrm{LiTaO_3}\) cylinder 30 mm in diameter and 10 mm thick, run between 240 K and 280 K, with a maximum potential below 110 kV [S2].
- **Measured.** Replication [S2]: two \(\mathrm{LiTaO_3}\) crystals, each 20 mm in diameter and 10 mm thick, 15 mm apart, heated to 130 °C over 350 s and left to cool; 200 kV between them, read from the X-ray end point; target of deuterated polystyrene 50 µm thick; 2.5 MeV neutrons detected for about 120 s per cycle.
- **Measured.** Neutrons per thermal cycle: about 10,500 in [S2]; 15,300 detected in [S1], which is 85,000 emitted after the stated detection efficiency of 0.18 [S2]. A news report of [S1] gives about 1,000 neutrons per second [S3].
- **Computed here.** From [S2]: 138 net counts, intrinsic efficiency 0.4 and solid-angle term 0.41 give \(4\pi \times 138/(0.4 \times 0.41) = 10{,}570\) neutrons. \(15{,}300/0.18 = 85{,}000\).
- **Measured.** D–D branches: \({}^{3}\mathrm{He} + n + 3.27\,\mathrm{MeV}\) and \(t + p + 4.03\,\mathrm{MeV}\) [S4]. Only the first gives neutrons [S2].
- **Computed here.** The neutron takes about three quarters of 3.27 MeV by momentum balance with \({}^{3}\mathrm{He}\) (mass numbers 3 and 1): 2.45 MeV.
- **Measured.** D–D cross-section (evaluated data quoted in [S2]): effectively zero below 20 keV and 16.3 mb at 100 keV. A 100 keV deuteron falls below 0.27 mb after 1 µm of target, so the reactions occur in the first micrometre [S2].
- **Measured.** Ionization conditions [S2]. A tungsten tip of 70 nm radius gave neutrons; a 600 nm tip, or no tip, gave no measurable yield. The best gas pressure was 1.2 mTorr; 10 mTorr halved the yield; below 0.7 mTorr no neutrons were observed.
- **Measured.** End of a burst: the X-ray rate that tracks the field fell from 4,000 counts per second to zero at an electrostatic discharge [S2].
- **Measured.** \(\mathrm{LiTaO_3}\) constants quoted in [S2]: pyroelectric coefficient \(190\,\mathrm{\mu C\,m^{-2}\,K^{-1}}\), relative permittivity 46. Its Curie temperature is reported from 874 K to 958 K [S5].
- **Model (parallel-plate capacitor, no charge loss).** \(V \approx \gamma\,\Delta T\,d_\mathrm{cr}/(\varepsilon_\mathrm{cr}\varepsilon_0)\); the potential grows nearly linearly with crystal thickness up to about 1 cm and little beyond [S2].
- **Computed here.** For a 10 mm crystal that relation gives 117 kV for a 25 K change and 187 kV for a 40 K change. The 240–280 K run reached less than 110 kV [S2]; if the full 40 K change was used, charge loss removed at least 40 % of the ideal potential.
- **Model (ion species).** If the ion is \(\mathrm{D_2^+}\), each deuteron carries half the energy; which ion forms at the tip was not determined [S2].
- **Computed here.** Yield per ion and energy balance, using 4 nA and 100 keV [S1] with 1,000 neutrons per second [S3]: 4 nA is \(2.5\times 10^{10}\) ions per second, so \(4\times 10^{-8}\) neutrons per ion. Beam power is \(4\times 10^{-4}\,\mathrm{W}\); the neutron branch releases \(5\times 10^{-10}\,\mathrm{W}\), about \(10^{-6}\) of the beam power.
- **Computed here.** The 130 °C peak in [S2] is 403 K, 46 % of the lowest reported Curie temperature.

**Data confidence:** Medium — the D–D neutron signal from a pyroelectric accelerator is reproduced by a second group. The body of [S1] was not opened: its crystal size, temperature range and count are taken from [S2], and the neutron rate from a news report [S3]. Yield per cycle depends on tip, pressure and crystal size.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Pyroelectric charge on an isolated face: \(\Delta\sigma = \gamma\,\Delta T\). Potential across the crystal and gap [S2]:

  \[
  V \approx \frac{\gamma\,\Delta T}{\varepsilon_\mathrm{cr}\varepsilon_0/d_\mathrm{cr} + \varepsilon_0/d_\mathrm{gap}}
  \]

  which reduces to \(\gamma\,\Delta T\,d_\mathrm{cr}/(\varepsilon_\mathrm{cr}\varepsilon_0)\) because \(\varepsilon_\mathrm{cr} \gg 1\).
- Thick-target yield: ion current times the integral of the D–D cross-section over the slowing-down path in the target [S2]. For 100 keV deuterons in deuterated polystyrene that integral gives 18,950 neutrons per cycle per nanoampere over 100 s [S2].

These describe the observed neutrons. They do not derive \(\gamma\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A polar crystal about 1 cm thick, a tip sharp enough to ionize the gas (70 nm worked, 600 nm did not), deuterium gas near 1 mTorr, and a deuterated target. Each nuclear event is one deuteron on one deuteron. Crystal area sets the available charge and is capacity.

- **Clock rate / latency.** The temperature change of the crystal, hundreds of seconds per cycle (350 s heating, about 120 s of emission). Fusion in the target is prompt.

- **Energy barriers or thresholds.** Two stages in series. The crystal must reach a potential that puts deuterons above about 20 keV; the D–D cross-section then rises steeply to 16.3 mb at 100 keV. No state is held: the potential exists only while the temperature changes and the face stays charged.

- **Dominant failure modes.**
  - **Threshold** — no temperature change: no pyroelectric charge and no field.
  - **Threshold** — no deuterium: no D–D neutrons.
  - **Crossover** — potential: the D–D cross-section falls continuously with ion energy and is effectively zero below 20 keV.
  - **Threshold** — discharge: an electrostatic breakdown removes the field and the emission stops at once.
  - **Crossover** — gas pressure: yield halves at 10 mTorr and is unobservable below 0.7 mTorr, with a maximum near 1.2 mTorr.
  - **Threshold** — tip radius: no measurable yield with a 600 nm tip or none; the limiting radius between 70 and 600 nm was not measured.
  - **Threshold** — Curie point of the crystal, 874–958 K reported for \(\mathrm{LiTaO_3}\): the polar phase is gone above it (owned by [ferroelectric remanence](ferroelectric-remanence.md)). The experiments stay below 403 K.

- **Emergent constant or stable output.** A burst of \(10^{4}\)–\(10^{5}\) neutrons of 2.45 MeV per thermal cycle, about \(4\times 10^{-8}\) per accelerated ion.

### 4.6 Internal Consistency Notes

This is not [muon-catalyzed fusion](muon-catalyzed-fusion.md). No muon is present. The nuclear step is ordinary beam-target D–D fusion; the unusual part is the crystal used as a compact high-voltage source. A pulsed-coil hydride cell has no such accelerator.

The polar crystal is a supporting resource that supplies the field. The neutron yield is an `energy-gate` output.

Sourcing changed five things. The device is a published one, reported in 2005 and reproduced in 2006, and the file now gives its dimensions and conditions. The cycle clock is hundreds of seconds, not seconds. The yield is \(10^{4}\)–\(10^{5}\) neutrons per cycle; no source was found for the earlier lower figure of \(10^{3}\). Three conditions the first version lacked are measured: a sharp tip, a pressure window, and termination by discharge. The Curie temperature of \(\mathrm{LiTaO_3}\) is a reported range, 874–958 K. The energy balance is also stated: the neutron branch returns about \(10^{-6}\) of the beam power.

SAFETY: this file maps a published neutron source. It is not a generator protocol.

### 4.7 Overall Confidence in the QSA Mapping

**High** on the machine class (pyroelectric field plus deuterium gives D–D neutrons; no field or no deuterium gives none); **Medium** on any one yield number.

## Related entries

- [muon-catalyzed-fusion](muon-catalyzed-fusion.md) — the other low-temperature hydrogen fusion route; needs a muon
- [ferroelectric-remanence](ferroelectric-remanence.md) — the polar crystal and its Curie point
- [dielectric-breakdown](dielectric-breakdown.md) — the discharge that ends a burst
- [deuteron-photodisintegration](deuteron-photodisintegration.md) — a photon unbinds the deuteron; this entry fuses two

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Naranjo, Gimzewski and Putterman, *Nature* 434, 1115 (2005)](https://www.nature.com/articles/nature03575) | abstract | Deuteron beam above 100 keV and 4 nA; neutron flux over 400 times background; D + D to 3He (820 keV) + n (2.45 MeV); not a viable power source. Body not opened. |
| S2 | [Geuther, Danon and Saglime, *Phys. Rev. Lett.* 96, 054803 (2006)](https://pages.github.rpi.edu/danony/html/Papers/PhysRevLett_96_054803%20Nuclear%20Reactions%20Induced%20by%20a%20Pyroelectric%20Accelerator.pdf) | full-text | Replication with two crystals: dimensions, 130 °C over 350 s, 200 kV, 120 s emission, about 10,500 neutrons per cycle, tip and pressure conditions, discharge; potential relation; pyroelectric coefficient and permittivity; D–D cross-section values; description of the 2005 apparatus and its 15,300 counts and 0.18 efficiency (secondary for those). |
| S3 | [Nature news, "Crystal creates table-top fusion", 27 April 2005, doi:10.1038/news050425-3](https://www.nature.com/news/2005/050425/full/news050425-3.html) | full-text | Tertiary (news report of S1): about 1,000 neutrons per second; the device cannot generate power. |
| S4 | [Rafelski and Steinmetz, arXiv:2609.01366 (2026)](https://arxiv.org/abs/2609.01366) | full-text | Secondary: D–D branch energies 3.27 MeV and 4.03 MeV. |
| S5 | [El Azzouzi et al., arXiv:2403.16717 (2024)](https://arxiv.org/abs/2403.16717) | full-text | Secondary: LiTaO3 transition temperature reported from 874 K to 958 K. |
