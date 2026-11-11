---
id: plasma-frequency-cutoff
title: Plasma-Frequency Cutoff (Collective Clock Failure)
status: formal
family: collective-field-response
constraints:
  - clock-latency
  - spatial-buffer
confidence_data: high
confidence_mapping: high
review_depth: deep
related:
  - reflection
  - skin-effect
  - surface-plasmon-resonance
  - photoelectric-threshold
  - refraction-dielectric
updated: 2026-11-11
---

# Plasma-Frequency Cutoff (Collective Clock Failure)

### 4.1 Effect Name

Plasma-frequency cutoff (collective clock failure)

### 4.2 Macroscopic Observation

A metal that reflects visible light well stops doing so once the drive frequency is raised through a material-specific edge in the ultraviolet (or, for the alkali metals, the near ultraviolet). Thin alkali films that look metallic in the visible pass ultraviolet light. Silver has a narrow band of low reflectance and raised transmission near 320 nm. The same frequency gate appears in dilute plasmas: short-wave radio above a few megahertz traverses the ionosphere and lower frequencies are returned. No continuous external power is required beyond the incident field.

### 4.3 Established Quantitative Boundaries

- **Measured.** Plasmon energies as tabulated: Al 15.0 eV, Na 5.75 eV, K 3.80 eV, Rb 3.40 eV, Cs 2.90 eV, Ag 3.78 eV [S2]. The original electron-energy-loss measurement on Al found an elementary loss of 15.3 eV [S1].
- **Measured.** Onset of ultraviolet transparency in the alkali metals: Cs 4400 Å, Rb 3600 Å, K 3150 Å, Na 2100 Å, Li 2050 Å. The onset moves to shorter wavelength with decreasing atomic number [S3].
- **Computed here.** The free-electron value \(\hbar\omega_p = \hbar\sqrt{ne^2/\varepsilon_0 m}\) from the tabulated carrier density [S2], beside the measured energy and the wavelength \(hc/E\) of each:

  | Metal | \(n\) (10²⁸ m⁻³) | Free-electron \(\hbar\omega_p\) | \(hc/E\) | Measured plasmon [S1][S2] | \(hc/E\) | Measured over model | Transparency onset [S3] |
  |---|---|---|---|---|---|---|---|
  | Al | 18.1 | 15.8 eV | 78.5 nm | 15.0–15.3 eV | 82.7–81.0 nm | 0.95–0.97 | not filed |
  | Na | 2.65 | 6.04 eV | 205 nm | 5.75 eV | 216 nm | 0.95 | 210 nm |
  | K | 1.40 | 4.39 eV | 282 nm | 3.80 eV | 326 nm | 0.87 | 315 nm |
  | Rb | 1.15 | 3.98 eV | 311 nm | 3.40 eV | 365 nm | 0.85 | 360 nm |
  | Cs | 0.91 | 3.54 eV | 350 nm | 2.90 eV | 428 nm | 0.82 | 440 nm |
  | Ag | 5.86 | 8.99 eV | 138 nm | 3.78 eV | 328 nm | 0.42 | see below |

  Al and Na lie 3–5 % below the free-electron value. K, Rb and Cs lie 13–18 % below it. Ag is at 0.42 of it. The observed transparency onsets of the alkalis fall within 12 nm of the wavelengths of their measured plasmon energies. The first version listed Na 5.7 eV and K 3.8 eV as free-electron values and said the alkalis track the free-electron edge. Those are measured energies, and only Na tracks the free-electron value closely.
- **Model (free-electron gas, with interband screening for the second figure).** The Drude plasma energy of Ag is 9.2 eV. Screening by the d bands lowers the plasma frequency to \(\omega_p^* = \omega_{pD}/\sqrt{\varepsilon_d} \approx 3.8\) eV [S4].
- **Measured.** Silver's edge: an energy-loss plasmon peak at 3.83 eV and a narrow reflectance dip at 3.92 eV [S5]; a resonance at about 3.8 eV [S4]; 3.79 eV (327 nm) in thin films [S6]. The spread across sources is 3.78–3.92 eV.
- **Computed here.** What silver does at and above the edge, from tabulated \(n\) and \(k\) [S7]. Bulk reflectance is 95.6 % at 381.5 nm (\(0.05 + 1.864i\)), 5.5 % at 320.4 nm (\(0.81 + 0.392i\); 3.87 eV) and 16 % at 300.9 nm (\(1.34 + 0.964i\)). The intensity decay length \(\lambda/4\pi k\) is 12 nm at 550 nm (\(k = 3.597\)), 65 nm at 320.4 nm and 25 nm at 300.9 nm. Silver therefore has a transmission window near 320 nm, and interband absorption closes it again within 20 nm of wavelength. The first version said a previously opaque film transmits above the edge; above its edge silver is an absorber with one narrow window.
- **Computed here.** Plasma periods \(h/E\): 0.28 fs for Al (15.0 eV); 0.72 fs for Na (5.75 eV); 1.1 fs for K (3.80 eV); for Ag 0.46 fs at the free-electron 9.0 eV and 1.1 fs at the measured 3.8 eV.
- **Measured.** Below the edge the metal reflects. A freshly aluminised telescope mirror reflects 90.00–91.35 % between 404 and 624 nm [S8]. Reflectance computed from optical constants is in [reflection](reflection.md).
- **Measured.** Ionosphere: peak electron densities of the layers vary between 10⁴ and more than 10⁶ per cm³ (10¹⁰ to more than 10¹² m⁻³), and inserting them into the plasma formula gives 1 to more than 9 MHz [S9].
- **Computed here.** \(f_p = \omega_p/2\pi\) is 0.90 MHz at 10¹⁰ m⁻³, 2.84 MHz at 10¹¹ m⁻³ and 8.98 MHz at 10¹² m⁻³. The plasma periods are 1.1 µs, 0.35 µs and 0.11 µs. The first version gave the ionospheric cycle as "microseconds"; for the densities it quoted the period is below a microsecond. The carrier density of a metal exceeds these by a factor of 5.9 × 10¹⁶ (Ag over 10¹² m⁻³) to 1.8 × 10¹⁸ (Al over 10¹¹ m⁻³); the first version said about 10¹⁷.
- **Measured.** Above its plasma frequency the ionospheric plasma still acts on a wave. Faraday rotation through the ionosphere and interstellar plasma is measured at about 100–200 MHz and follows \(\psi = \psi_0 + \mathrm{RM}\,\lambda^2\) [S10]. The effect of the plasma fades as \(\lambda^2\) above the edge; it does not stop at the edge.
- **Measured.** No thickness cutoff accompanies the spectral one. A continuous 5.66 nm Au film transmits as the bulk-constant calculation predicts [S11], and Au on a copper seed is optically a continuous metal down to 1 nm [S12]. The first version said a film below 5–10 nm "never forms the collective response, at any frequency".
- **Measured.** Work functions, for the contrast in §4.6: Ag 4.26–4.74 eV; the tabulated elements span 1.95 eV (Cs) to 5.93 eV [S13].

**Data confidence:** High — plasmon energies, the silver edge and the ionospheric densities are multiply reproduced. The silver edge is 3.78–3.92 eV across four sources. Weaker points: the Al energy-loss value [S1] and the alkali transparency onsets [S3] were read in abstracts only; the plasmon energies and densities come from one secondary table [S2], since the textbook tables it draws on were not opened; the work functions are from a tertiary page [S13]. No opened source gives the measured width of the ionospheric cutoff.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Plasma frequency of a free-electron gas [S2]:

  \[
  \omega_p = \sqrt{\frac{ne^2}{\varepsilon_0 m}}
  \]

- Drude dielectric function [S14]:

  \[
  \varepsilon(\omega) = 1 - \frac{\omega_p^2}{\omega(\omega + i\gamma)}
  \]

  With \(\gamma = 0\), \(\varepsilon\) is real and negative below \(\omega_p\), the wave does not propagate and the reflectance is 1; above \(\omega_p\), \(\varepsilon > 0\) and the bulk supports propagating waves. In that limit the cutoff is sharp. With damping or interband terms the edge has a width.

- Normal-incidence Fresnel reflectance from complex index \(\tilde n = n + ik\):

  \[
  R = \left|\frac{1 - \tilde n}{1 + \tilde n}\right|^2
  \]

- In a dilute plasma the same \(\omega_p(n)\) is read as a radio cutoff frequency \(f_p = \omega_p/2\pi\) [S9].
- Interband screening: \(\omega_p^* = \omega_{pD}/\sqrt{\varepsilon_d}\) [S4]. This is the origin of the gap between silver's 9 eV and 3.8 eV.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A population of free carriers; its density sets the edge. Metals: 10²⁸–10²⁹ m⁻³. Ionosphere: 10¹⁰–10¹² m⁻³, a column of free electrons and not a crystal. No minimum thickness is measured for the metal; the thickness dependence of reflection is a crossover and is owned by [reflection](reflection.md).

- **Clock rate / latency.** The load-bearing specification. The collective cycle is the plasma period: 0.28–1.1 fs in the metals tabulated and 0.1–1 µs in the ionosphere. A drive slower than that is returned. For Al and Na the period follows from the carrier density to about 5 %. For K, Rb and Cs the measured clock is 13–18 % slower than the density alone gives, and for Ag it is slower by a factor of 2.4 because the d bands screen the carriers.

- **Energy barriers or thresholds.** The operating condition is a drive below the measured edge. There is no static latch; this is a driven collective response. \(\hbar\omega_p\) is an energy scale of the clock, not an activation barrier that holds a memory.

- **Dominant failure modes.**
  - **Crossover** — spectral edge in a real metal: reflectance falls across the edge over a width set by damping and interband transitions. In Ag it goes from 95.6 % at 381.5 nm to 5.5 % at 320.4 nm. The energy quoted for an edge (3.78–3.92 eV in Ag) is the plasmon peak or the reflectance minimum, a convention for locating a steep but continuous fall.
  - **Threshold** — the collisionless model: with \(\gamma = 0\) a wave below \(f_p(n)\) does not propagate and one above it does. The ionospheric return of radio below 1–9 MHz is the filed case nearest to this limit. The label rests on the model; no measured width of that cutoff was opened.
  - **Crossover** — above the edge: the medium keeps acting on the wave. In a plasma the rotation of polarization fades as \(\lambda^2\). In Ag absorption returns within 20 nm of the window.
  - **Crossover** — thickness: reflectance falls smoothly as a continuous film thins, with no cutoff. Owned by [reflection](reflection.md).
  - **Crossover** — dissipation: larger \(\gamma\) widens the edge. No measured width against damping is filed here.

- **Emergent constant or stable output.** A material-typical edge: high reflectance below it, and above it a propagating or absorbed wave, produced with no continuous power input to the medium beyond the incident field.

### 4.6 Internal Consistency Notes

The mapping is the clock side of [reflection](reflection.md): the same carrier population, with the drive frequency as the knob. Changing only the drive frequency takes the system across the edge this entry owns.

Sourcing changed five things. The alkali energies in the first version were measured values labelled as free-electron ones; with both columns in view, only Na and Al sit close to the free-electron formula, 3–5 % below it. Above its edge silver has a narrow transmission window near 320 nm and is otherwise absorbing, so "transmits above the edge" describes the alkalis and the ionosphere and does not describe silver. The ionospheric cycle is 0.1–1 µs. The edge in a real metal is a crossover with a width; the sharp cutoff belongs to the collisionless model. And the spatial clause is withdrawn: the first version said a film below 5–10 nm never forms the collective response, which followed from the thickness cliff in the first version of reflection. That cliff does not exist, so this entry carries no thickness floor.

"Clock \(= \omega_p(n)\)" is too coarse for silver and for the heavy alkalis. For silver two numbers are needed: the free-electron 9.0–9.2 eV, which reflects the carrier density, and the screened 3.8–3.9 eV, which is where the reflectance falls. One plasma clock per metal holds only if the screening constant is carried with it.

The mapping takes the measured edge as the clock specification. It does not derive the period from a more primitive node update, and the free-electron formula it leaned on needs a material-specific correction in four of the six metals tabulated. The same class of gap is recorded on reflection for the decay length.

Contrast case: [photoelectric-threshold](photoelectric-threshold.md) is a single-electron energy gate in the same metals. The plasma edge is collective and set by carrier density and screening; the work function is not. The two can sit near each other in energy (Ag edge 3.8–3.9 eV; Ag work function 4.26–4.74 eV) without being the same constraint.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the spectral boundary is a measured ceiling on drive frequency that scales with carrier density from the ionosphere to aluminum, and it maps onto a collective cycle time. The grade is for that reading. The edge is a crossover in a real metal, the clock is taken and needs a screening correction in silver and the heavy alkalis, and the thickness clause inherited from reflection is withdrawn.

## Related entries

- [Reflection (electron-cloud response)](reflection.md) — the same population below the edge; owns the thickness dependence
- [Skin effect](skin-effect.md) — low-frequency limit of the same decay length
- [Surface plasmon resonance](surface-plasmon-resonance.md) — interface-bound collective mode of the same electron population
- [Photoelectric threshold](photoelectric-threshold.md) — single-electron energy gate in the same metals; contrast case
- [Refraction / dielectric polarization](refraction-dielectric.md) — bound-charge polarizability; the \(\varepsilon \to 1\) X-ray limit is the insulator analogue of \(\omega \gg \omega_p\)

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Powell and Swan, *Phys. Rev.* 115, 869 (1959)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.115.869) | abstract | Elementary 15.3 eV energy loss in Al. |
| S2 | [v. Baltz, "Plasmons and surface plasmons in bulk metals, metallic clusters, and metallic heterostructures", lecture article, Universität Karlsruhe](https://www.tkm.kit.edu/img/mitarbeiter/Er1995-Plasmons.pdf) | full-text | Table of carrier densities and measured plasmon energies for Al, Na, K, Rb, Cs and Ag. Secondary; publication details are not in the opened text. |
| S3 | [Wood, *Phys. Rev.* 44, 353 (1933)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.44.353) | abstract | Onset wavelengths of ultraviolet transparency in Cs, Rb, K, Na and Li. |
| S4 | [Cazalilla et al., "Plasmonic excitations in noble metals: The case of Ag", arXiv:cond-mat/9907204](https://arxiv.org/abs/cond-mat/9907204) | full-text | Ag Drude plasma energy 9.2 eV; resonance near 3.8 eV; interband-screened plasma frequency. Journal reference not re-opened. |
| S5 | [Marini, Del Sole and Onida, *Phys. Rev. B* 66, 115101 (2002), arXiv:cond-mat/0206322](https://arxiv.org/abs/cond-mat/0206322) | full-text | Ag energy-loss plasmon peak at 3.83 eV and reflectance dip at 3.92 eV. |
| S6 | [Gong et al., *Sci. Rep.* 5, 9279 (2015)](https://www.nature.com/articles/srep09279) | full-text | Ag plasmon at 327 nm (3.79 eV) in thin films. |
| S7 | [Johnson and Christy, *Phys. Rev. B* 6, 4370 (1972), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/Ag/nk/Johnson.yml) | full-text | Ag n and k at 300.9, 320.4, 381.5 and 550 nm: the reflectance edge and the transmission window. Database tabulation, secondary. |
| S8 | [Isaac Newton Group, "2016 Aluminization of WHT Primary Mirror (M1) – Reflectivity Data from CT7 reflectometer"](https://www.ing.iac.es/~eng/optics/reflectivity/pdf/20160518_WHTM1_Alum.pdf) | full-text | Measured reflectance of fresh aluminium at 404–624 nm. Observatory technical report. |
| S9 | [*Handbook of Geophysics and the Space Environment* (Air Force Geophysics Laboratory, 1985), ch. 10](https://www.ngdc.noaa.gov/stp/space-weather/online-publications/miscellaneous/afrl_publications/handbook_1985/Chptr10.pdf) | full-text | Ionospheric peak densities and the resulting plasma-frequency range of 1 to more than 9 MHz. |
| S10 | [Porayko et al., "Testing the accuracy of the ionospheric Faraday rotation corrections through LOFAR observations of bright northern pulsars", arXiv:1812.01463](https://arxiv.org/abs/1812.01463) | full-text | Faraday rotation through the ionosphere measured at about 100–200 MHz, following a wavelength-squared law. Preprint; journal reference not re-opened. |
| S11 | [Lemasters et al., *ACS Photonics* 6, 2600 (2019), author manuscript](https://par.nsf.gov/servlets/purl/10230835) | full-text | Continuous 5.66 nm Au film matching the bulk-permittivity calculation. |
| S12 | [Maniyara et al., *Nat. Photonics* 13, 328 (2019), arXiv:1809.01449](https://arxiv.org/abs/1809.01449) | full-text | Seeded Au optically a continuous metal down to 1 nm. |
| S13 | [Wikipedia, "Work function", table citing the *CRC Handbook of Chemistry and Physics* (2008)](https://en.wikipedia.org/wiki/Work_function) | full-text | Ag work function 4.26–4.74 eV; range 1.95–5.93 eV across elements. Tertiary. |
| S14 | [Cohen and Louie, *Fundamentals of Condensed Matter Physics*, ch. 9, sec. 9.2 (excerpt)](https://webdisk.science.upjs.sk/~martin_gmitra/Theory%20of%20Condensed%20Matter/Supporting%20Materials/08%20-%2009/Drude_model_src%3AM.L.Cohen_S.G.Louie_Gauss_units.pdf) | full-text | Drude dielectric function. Textbook excerpt. |
