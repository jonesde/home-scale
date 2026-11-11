---
id: reflection
title: Reflection (Electron-Cloud Response)
status: formal
family: collective-field-response
constraints:
  - spatial-buffer
  - clock-latency
confidence_data: high
confidence_mapping: medium
review_depth: deep
related:
  - plasma-frequency-cutoff
  - skin-effect
  - photoelectric-threshold
  - surface-plasmon-resonance
  - faraday-rotation
updated: 2026-11-12
---

# Reflection (Electron-Cloud Response)

### 4.1 Effect Name

Reflection (electron-cloud response)

### 4.2 Macroscopic Observation

Visible light incident on a polished silver or aluminum surface returns as a reflected beam with high efficiency. The surface appears mirror-like. No continuous external power is required to maintain the reflected image. As a metal film is made thinner the reflected fraction falls and the transmitted fraction rises, continuously. A film deposited as separate islands does not conduct a direct current across the substrate and shows an absorption band that a continuous film lacks.

### 4.3 Established Quantitative Boundaries

Optical constants and the decay length:

- **Measured.** Complex refractive index \(n + ik\) of Ag and Al, tabulated against wavelength. At 550 nm: Ag \(0.060 + 3.597i\) [S1], \(0.044 + 3.610i\) [S2], \(0.053 + 3.485i\) [S3]; Al \(0.789 + 5.852i\) [S2] and, for epitaxial Al, \(0.591 + 5.276i\) [S6]. The values were read from the refractiveindex.info database files, which name each primary dataset, and interpolated linearly between tabulated points.
- **Model (Kramers–Kronig analysis; Brendel–Bormann and Lorentz–Drude oscillator fits).** Fitted constants at 550 nm: Al \(1.015 + 6.627i\) [S5] and \(0.965 + 6.400i\) [S4]; Ag \(0.145 + 3.190i\) and \(0.134 + 3.172i\) [S4]. The Ag fits give a larger \(n\), so more absorption, than the measured sets.
- **Convention.** \(\delta = \lambda/4\pi k\) is the distance over which the intensity of the field inside a continuous metal falls by a factor of e; the amplitude falls by e in twice that distance. It marks one point on a continuous exponential decay. It is not a minimum thickness.
- **Computed here.** \(\delta\) and the bulk reflectance \(R = \lvert(1-\tilde n)/(1+\tilde n)\rvert^2\) from the constants above:

  | Metal | Dataset | \(n,\ k\) at 550 nm | \(\delta\) at 550 nm | Bulk \(R\) at 550 nm |
  |---|---|---|---|---|
  | Ag | Johnson and Christy, measured [S1] | 0.060, 3.597 | 12.2 nm | 98.3 % |
  | Ag | McPeak et al., measured [S2] | 0.044, 3.610 | 12.1 nm | 98.8 % |
  | Ag | Yang et al., measured [S3] | 0.053, 3.485 | 12.6 nm | 98.4 % |
  | Ag | Rakić et al., Brendel–Bormann fit [S4] | 0.145, 3.190 | 13.7 nm | 95.0 % |
  | Ag | Rakić et al., Lorentz–Drude fit [S4] | 0.134, 3.172 | 13.8 nm | 95.3 % |
  | Al | Rakić 1995, Kramers–Kronig analysis [S5] | 1.015, 6.627 | 6.6 nm | 91.5 % |
  | Al | Rakić et al., Brendel–Bormann fit [S4] | 0.965, 6.400 | 6.8 nm | 91.4 % |
  | Al | McPeak et al., measured [S2] | 0.789, 5.852 | 7.5 nm | 91.6 % |
  | Al | Cheng et al., epitaxial, measured [S6] | 0.591, 5.276 | 8.3 nm | 92.2 % |

  Across 450–650 nm, \(\delta\) for Ag runs from 11.6 nm (\(k = 4.460\) at 650 nm [S2]) to 15.4 nm (\(k = 2.328\) at 450 nm [S4]); for Al from 6.6 nm (\(k = 5.454\) at 450 nm [S5]) to 8.3 nm (\(k = 4.297\) at 450 nm [S6]). The amplitude depths are 23–31 nm for Ag and 13–17 nm for Al. The first version gave "about 10–20 nm" for both metals; Al lies below that range.

  Across the same band, bulk \(R\) for Ag is 97.3 % (\(0.053 + 2.610i\) at 450 nm [S3]) to 99.0 % (\(0.052 + 4.409i\) at 650 nm [S1]) in the measured sets and 91.9 % (\(0.136 + 2.328i\) at 450 nm) to 96.5 % (\(0.146 + 3.937i\) at 650 nm) in the fits [S4]. For Al it is 90.4 % (\(1.246 + 6.852i\) at 650 nm [S2]) to 92.4 % (\(0.390 + 4.297i\) at 450 nm [S6]).
- **Measured.** A freshly aluminised telescope primary mirror reflects 91.35 % at 404 nm, 90.90 % at 464 nm, 90.95 % at 522 nm and 90.00 % at 624 nm [S7]. No primary measurement of the reflectance of polished silver was opened; the Ag figures above rest on measured \(n\) and \(k\).

Thickness:

- **Computed here.** Reflectance \(R\) and transmittance \(T\) of a continuous film at 550 nm and normal incidence, from the single-layer Fresnel (Airy) formula of §4.4 with the bulk constants above:

  | Film | 3 nm | 5 nm | 10 nm | 20 nm | 30 nm | 50 nm | 100 nm |
  |---|---|---|---|---|---|---|---|
  | Ag [S1], free-standing, \(R\) | 5.4 % | 13.6 % | 38.9 % | 73.8 % | 88.1 % | 96.4 % | 98.3 % |
  | Ag [S1], free-standing, \(T\) | 93.3 % | 84.3 % | 58.0 % | 23.3 % | 9.5 % | 1.7 % | 0.03 % |
  | Ag [S1] on glass (\(n = 1.5\)), \(R\) from the air side | 7.8 % | 13.8 % | 34.2 % | 68.5 % | 85.3 % | 95.8 % | 98.3 % |
  | Al [S5], free-standing, \(R\) | 30.0 % | 49.9 % | 74.2 % | 87.5 % | 90.5 % | 91.5 % | 91.5 % |
  | Al [S2], free-standing, \(R\) | 22.4 % | 41.2 % | 68.4 % | 85.4 % | 89.8 % | 91.4 % | 91.6 % |

  The curve is smooth. Reflectance reaches half its bulk value at 12.2 nm for free-standing Ag and 13.7 nm for Ag on glass; at 4.5 nm [S5] to 5.6 nm [S2] for free-standing Al, and 5.9 nm for Al [S2] on glass. It reaches 90 % of bulk at about 31 nm (free-standing) and 33 nm (on glass) for Ag, and at 14 nm [S5] to 17 nm [S2] for Al. The epitaxial-Al constants [S6] give 34 % at 5 nm and 63 % at 10 nm. The first version said reflectivity "collapses" below 5–10 nm. At 5 nm a silver film still reflects 14 % and an aluminum film 34–50 %; at 10 nm, 39 % and 63–74 %.
- **Measured.** The calculation holds for a real continuous film. A 5.66 nm Au film, deposited at −195 °C without a wetting layer, has a transmittance spectrum in good agreement with the transfer-matrix calculation that uses bulk Au permittivity [S8]. For sputtered Ag at 6 nm, bulk optical properties were found sufficient for simulation-based design [S10].
- **Measured.** The measured departures are toward more opacity. Continuous Au films from 5.4 nm to 10 nm on mercaptosilane-treated silica transmit less than the ideal bulk-constant film, which the authors explain by graded interfaces; agreement with the ideal film improves as the thickness approaches 15–20 nm [S9].
- **Measured.** Damping rises as the film thins. Plasmon damping in 10 monolayers of Ag(111) is about 93 meV against 21 meV in bulk [S16]. In evaporated Au of 3–10 nm the scattering rate rises and the effective electron density falls with decreasing thickness, and the spectral weight reaches its bulk value at about 10 nm [S12].
- **Model (Drude fit to measured spectra).** The damping fitted to 3 nm Au films on a copper seed is 0.19 eV, several times the bulk value [S11].

How thin a film still responds collectively:

- **Measured.** One atomic layer of graphene absorbs \(\pi\alpha = 2.3\,\%\) of white light [S17].
- **Measured.** Seven monolayers of Ag(111), 1.65 nm, have a sheet resistance of about 20 Ω per square, twice the bulk estimate. Ten monolayers carry plasmons with a quality factor near 4 [S16].
- **Measured.** Au on a 1 nm copper seed behaves optically as a continuous metal down to 1 nm nominal thickness, and plasmon resonances are measured in 3 nm films [S11].
- **Measured.** In single Ag particles the plasmon resonance is followed from 20 nm to below 2 nm diameter. It shifts to higher energy by 0.5 eV and does not disappear [S18]. In Au particles the resonance emerges at a size between 1.5 and 2 nm [S19].

Morphology:

- **Measured.** Percolation thickness, below which a deposited film is separate islands. Au without a seed: 7 nm [S11]; 6–7 nm on Si/SiO₂ [S12]. Au on 1 nm of copper: 1 nm [S11]. Continuous Au is also reported at 5.4 nm on a mercaptosilane layer [S9] and at 5.66 nm on a substrate at −195 °C [S8]. Ag without a seed: 12 nm in one study [S13] and 6 nm in another [S14]; with a TiOₓ seed, 9 nm [S13]; with 1 nm of copper, 3 nm [S14]. Ag thinned back from a thicker film is continuous at 4.5 nm and discontinuous, though still conducting, at 3 nm [S13]. Epitaxial Ag(111) on silicon is continuous at 7 monolayers [S16].
- **Measured.** The percolation transition is abrupt in dc conductance and is not abrupt in the optical response. In Au films of 3–10 nm on Si/SiO₂ the dc metal–insulator transition lies between 6 and 7 nm, and the optical spectra show no sign of it: spectral weight moves monotonically from the island plasmons to the Drude peak [S12]. In unseeded Au an island-plasmon dip near 600–650 nm fades from 7 nm upward while infrared transmission falls progressively [S11].
- **Measured.** In unseeded sputtered Ag the effective \(n\) and \(k\) change with thickness below about 12 nm, and the film is described as non-metallic below 8 nm; above 12 nm both approach the bulk values [S15]. This is islanding, a property of the deposition, and not a limit on a continuous film.

Plasma energies and periods:

- **Measured.** Volume-plasmon energies: Al 15.0 eV; Ag 3.78 eV in the same tabulation [S20], and a narrow resonance at about 3.8 eV in electron energy loss [S21].
- **Model (free-electron gas, with interband screening for the second figure).** The Drude plasma energy of Ag is 9.2 eV. Screening by the d bands lowers it to \(\omega_p^* = \omega_{pD}/\sqrt{\varepsilon_d} \approx 3.8\) eV [S21].
- **Computed here.** \(\hbar\omega_p = \hbar\sqrt{ne^2/\varepsilon_0 m}\) from tabulated carrier densities [S20]: Al 15.8 eV (\(n = 1.81 \times 10^{29}\) m⁻³), Ag 8.99 eV (\(5.86 \times 10^{28}\) m⁻³). The measured Al plasmon is 5 % below the model value. The measured Ag plasmon is 0.42 of it. The first version listed "Ag ≈ 9 eV" among electron-energy-loss values; 9 eV is the model value and energy loss in Ag shows 3.8 eV. Periods \(h/E\): 0.28 fs at 15.0 eV, 0.46 fs at 9.0 eV, 1.1 fs at 3.8 eV. The optical period at 550 nm is 1.8 fs.
- **Computed here.** The silver edge, from bulk \(R\) at three tabulated points [S1]: 95.6 % at 381.5 nm (\(0.05 + 1.864i\)); 5.5 % at 320.4 nm (\(0.81 + 0.392i\)), which is 3.87 eV; 16 % at 300.9 nm (\(1.34 + 0.964i\)). Reflectance falls across 61 nm of wavelength and recovers only to 16 % on the short-wavelength side.
- **Computed here.** Carrier densities from the lattice constants (Ag 4.0862 Å, Al 4.04958 Å [S22]), four atoms per cubic cell: Al with three electrons per atom \(1.81 \times 10^{29}\) m⁻³, Ag with one \(5.86 \times 10^{28}\) m⁻³, as tabulated [S20]. Close-packed (111) plane spacing \(a/\sqrt{3}\): Ag 2.359 Å, Al 2.338 Å; Ag(111) planes are seen at 0.236 nm in cross-section electron microscopy [S16]. One intensity e-folding length is therefore 49–65 planes of Ag (11.6–15.4 nm) or 28–36 planes of Al (6.6–8.3 nm), and 7 monolayers of Ag are 1.65 nm. The first version's "40–85 planes" is correct arithmetic for 10–20 nm of Ag (42–85); the thickness it was applied to is not a threshold.
- **Measured.** The attosecond photoemission experiment on a metal surface was made on single-crystal tungsten, not on Ag or Al. It found a delay of about 100 as between photoelectrons from localized core states and those from the conduction band [S23].
- **Computed here.** The plasma periods above are 276 as (Al, 15.0 eV) and 460 as (Ag, 9.0 eV), the same order as that delay. The first version placed the single-electron response at the "10⁻¹⁸ s scale", in Ag and Al, and said it resolves faster than the collective step. The measurement was on tungsten, the delay is 10⁻¹⁶ s, and no opened source separates a single-electron time from the collective one.

**Data confidence:** High — the optical constants agree across five Ag and four Al datasets to within the spreads tabulated above, and the thin-film curve follows from them by standard arithmetic that is confirmed on a 5.66 nm Au film. Three points are weaker. No measured \(R(d)\) series for seeded continuous Ag was found to set beside the computed table; the direct comparisons are for Au, plus one statement for Ag at 6 nm. The reflectance of polished Ag rests on \(n\) and \(k\), not on a mirror measurement. The seeded-Ag percolation figure [S14], the particle series [S18] and the attosecond delay [S23] were read in abstracts only.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Plasma frequency of a free-electron gas [S20]:

  \[
  \omega_p = \sqrt{\frac{ne^2}{\varepsilon_0 m}}
  \]

- Drude dielectric function [S24]:

  \[
  \varepsilon(\omega) = 1 - \frac{\omega_p^2}{\omega(\omega + i\gamma)}
  \]

  For \(\omega < \omega_p\) and small damping, \(\operatorname{Re}\varepsilon < 0\) and the reflectance of a vacuum–metal interface is high. With \(\gamma = 0\) the reflectance is exactly 1 below \(\omega_p\) and falls from 1 at \(\omega_p\); with damping or interband terms the edge has a width.

- Normal-incidence Fresnel reflectance of a thick metal with complex index \(\tilde n = n + ik\):

  \[
  R = \left|\frac{1 - \tilde n}{1 + \tilde n}\right|^2
  \]

- A single layer of thickness \(d\) between media 0 and 2 (Airy formula), with \(r_{ij} = (\tilde n_i - \tilde n_j)/(\tilde n_i + \tilde n_j)\) and \(\beta = 2\pi\tilde n d/\lambda\):

  \[
  r = \frac{r_{01} + r_{12}e^{2i\beta}}{1 + r_{01}r_{12}e^{2i\beta}},\qquad R = \lvert r\rvert^2
  \]

  The transmitted intensity carries the factor \(\lvert e^{i\beta}\rvert^2 = e^{-d/\delta}\).

- Intensity decay length:

  \[
  \delta = \frac{\lambda}{4\pi k}
  \]

- Hagen–Rubens (low-frequency metals, \(\omega\tau \ll 1\)): \(R \approx 1 - 2\sqrt{2\varepsilon_0\omega/\sigma}\) [S24]. The source gives the Gaussian form \(1 - \sqrt{2\omega/\pi\sigma}\); the SI form follows by \(\sigma_\mathrm{Gaussian} = \sigma/4\pi\varepsilon_0\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** No minimum is measured. The reflected fraction grows continuously with the amount of responding metal the field passes through, on the scale of the decay length \(\lambda/4\pi k\): 12–15 nm (49–65 planes) in Ag and 6.6–8.3 nm (28–36 planes) in Al. Half the bulk reflectance is reached at about one such length in Ag (12–14 nm) and within one in Al (4.5–6 nm); 90 % at 31–33 nm and 14–17 nm. At the thin end, one atomic layer absorbs 2.3 %, seven planes of Ag conduct within a factor of two of bulk, and a particle resonance appears between 1.5 and 2 nm. In-plane connection of the film is a separate resource. It sets the dc conductance; it does not set whether a collective optical response exists, since separate islands have a plasmon of their own.

- **Clock rate / latency.** The plasma period: 0.28 fs for Al at its measured plasmon energy; for Ag 0.46 fs at the free-electron value and 1.1 fs at the measured, interband-screened one. Visible light, with a period near 1.8 fs, is slower than all three. A photoemission delay of about 100 as measured on tungsten is of the same order as these periods, so the data do not show a single-electron step that is faster than the collective one.

- **Energy barriers or thresholds.** None that holds a state. The operating condition is a drive frequency below the plasma edge (Al) or the interband-screened edge (Ag, 3.8–3.9 eV). There is no thickness condition. This is a driven collective response, not a memory.

- **Dominant failure modes.**
  - **Crossover** — thickness of a continuous film: the transmitted intensity falls as \(e^{-d/\delta}\) with \(\delta = \lambda/4\pi k\), and \(R(d)\) rises smoothly toward the bulk value. Half of bulk \(R\) at 12–14 nm in Ag and 4.5–6 nm in Al, at 550 nm; "half" is the convention behind those numbers. Thinner films depart from the bulk-constant curve through extra damping, also gradually.
  - **Threshold** — morphology, in dc conductance: a deposited film conducts across the substrate only above its percolation thickness, 6–7 nm for unseeded Au, 6–12 nm for unseeded Ag, 1–3 nm on a copper seed. The value belongs to the deposition process.
  - **Crossover** — morphology, at optical frequencies: through the same percolation point the optical response changes monotonically, with spectral weight moving from island plasmons to the Drude peak.
  - **Crossover** — spectral edge in a real metal: the reflectance of Ag falls from 95.6 % at 381.5 nm to 5.5 % at 320.4 nm, a steep edge whose width is set by damping and interband transitions. A sharp cutoff at \(\omega_p\) exists only in the collisionless Drude model of §4.4. Owned by [plasma-frequency-cutoff](plasma-frequency-cutoff.md).
  - **Crossover** — dissipation: larger damping lowers \(R\) continuously. The fitted Ag constants with larger \(n\) give 95 % where the measured sets give 98 %; in the low-frequency limit \(1 - R\) grows as \(\sqrt{\omega/\sigma}\).

- **Emergent constant or stable output.** A reflected beam with a material-typical \(R(\lambda)\): 97–99 % for Ag and 90–92 % for Al across 450–650 nm, from a thick film. No continuous power is supplied to the metal beyond the incident field.

### 4.6 Internal Consistency Notes

The clock and the output map as before: a population that responds within a plasma period returns a field driven more slowly than that, and holding the image costs nothing. The spatial clause is where the mapping changed.

Sourcing changed the central claim of this entry. The first version read a 10–20 nm film as a minimum connected buffer of 40–85 atomic planes below which "the reflection calculation fails", and called the fall of reflectance below 5–10 nm a collapse. Five corrections follow from the sources. The 10–20 nm figure was the e-folding length \(\lambda/4\pi k\), a convention on a continuous decay; it is 12–15 nm for Ag and 6.6–8.3 nm for Al. Reflectance falls smoothly with thickness, ordinary thin-film optics with bulk constants reproduces the curve, a measured 5.66 nm Au film agrees with it, and the measured departures in thinner films are toward less transmission and more damping. A collective optical response is measured at one atomic layer, at 1.65 nm of Ag, at 1 nm of seeded Au and in 2 nm particles. The sharp transition in this subject is percolation, which is sharp in dc conductance and monotonic in the optical response. The 9 eV plasma energy of Ag is a model value beside a measured 3.8 eV, and the attosecond delay was measured on tungsten at 10⁻¹⁶ s.

This entry was the project's calibration anchor: the worked example of an implication ("reflection needs a ~10–20 nm connected film"), the calibration case of [thin-film-optics](../application/thin-film-optics.md), and the optical instance behind the shared requirements `connected-spatial-buffer` and `coupled-screening-failure`. Three things follow for the entries that cited it. An entry that quoted the mirror threshold as a floor of its own or as a contrast has lost that clause; [plasma-frequency-cutoff](plasma-frequency-cutoff.md), [surface-plasmon-resonance](surface-plasmon-resonance.md), [refraction-dielectric](refraction-dielectric.md) and [casimir-force](casimir-force.md) were corrected with this file. The optical instance of `connected-spatial-buffer` is contradicted, and `coupled-screening-failure` is contradicted as worded, since neither reflectance nor the Casimir force switches off with thickness; the magnetic and superconducting instances of the first were not examined here. And a mapping elsewhere that was graded against this entry's cliff was graded against a claim that the measurements do not support, so it does not inherit confidence from here.

What the mapping now says is weaker and is what the data support: the output scales with how much responding material the field passes through and saturates over a few decay lengths, with no minimum node count. That statement is the content of the Airy formula with bulk \(n\) and \(k\). Standard thin-film optics already predicts every thickness number in §4.3, so at this level the mapping makes no prediction that would distinguish it from the standard description. A continuous 3 nm Ag film is expected to reflect about 5 % on either account.

The decay length is taken, not derived. It is \(\lambda/4\pi k\), and \(k\) is an optical constant of the same electron population. A closed mapping would obtain it from node rules. That gap stands, with the length now read as a decay scale instead of a buffer size.

Whether a floor exists at all is open at the 1–2 nm scale. The particle resonance in Au appears only above 1.5–2 nm, and damping at 2–3 nm is several times the bulk value. No opened source reports a planar film that is continuous and fails to respond.

Silver needs two numbers where the first version had one clock. The free-electron value of 9.0–9.2 eV describes the carrier density and the infrared response; the edge that a visible or ultraviolet beam meets is at 3.8–3.9 eV. Visible mirrors sit below both.

Contrast case: [photoelectric-threshold](photoelectric-threshold.md) is a single-electron energy gate in the same metal. The mirror is a collective response with no ejection; photoemission is a conversion above a threshold. The two do not share a spatial specification.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — lowered from High. The plasma-period clock, the spectral edge and the zero-power output map onto measured quantities. The spatial clause that carried the earlier grade, a minimum connected buffer with a collapse below it, is withdrawn: thickness is a crossover with a decay length that standard optics supplies and that the mapping takes without deriving.

## Related entries

- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — the same population driven through its spectral edge
- [Skin effect](skin-effect.md) — low-frequency limit of the same decay length
- [Surface plasmon resonance](surface-plasmon-resonance.md) — interface-bound collective mode of the same electron population
- [Photoelectric threshold](photoelectric-threshold.md) — single-electron energy gate in the same metals; contrast case
- [faraday-rotation](faraday-rotation.md) — Kerr rotation is Faraday on this metal face; a clause, not a second file

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Johnson and Christy, *Phys. Rev. B* 6, 4370 (1972), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/Ag/nk/Johnson.yml) | full-text | Ag n and k from 300 to 650 nm; the thin-film table for Ag; the reflectance edge near 320 nm. Database tabulation, secondary to the paper. |
| S2 | [McPeak et al., *ACS Photonics* 2, 326 (2015), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/Al/nk/McPeak.yml) | full-text | Ag and Al n and k (the Ag file is Ag/nk/McPeak.yml in the same database); shortest Ag decay length; lowest Al bulk R. Secondary. |
| S3 | [Yang et al., *Phys. Rev. B* 91, 235137 (2015), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/Ag/nk/Yang.yml) | full-text | Ag n and k; lowest measured-set bulk R. Secondary. |
| S4 | [Rakić et al., *Appl. Opt.* 37, 5271 (1998), Brendel–Bormann and Lorentz–Drude fits, as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/Ag/nk/Rakic-BB.yml) | full-text | Fitted Ag and Al constants (files Rakic-BB.yml and Rakic-LD.yml); longest Ag decay length; the lower bulk R of the fits. Secondary. |
| S5 | [Rakić, *Appl. Opt.* 34, 4755 (1995), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/Al/nk/Rakic.yml) | full-text | Al constants from a Kramers–Kronig analysis of film data; shortest Al decay length; thin-film table for Al. Secondary. |
| S6 | [Cheng et al., *ACS Nano* 10, 9852 (2016), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/Al/nk/Cheng.yml) | full-text | Epitaxial Al n and k; longest Al decay length; highest Al bulk R. Secondary. |
| S7 | [Isaac Newton Group, "2016 Aluminization of WHT Primary Mirror (M1) – Reflectivity Data from CT7 reflectometer"](https://www.ing.iac.es/~eng/optics/reflectivity/pdf/20160518_WHTM1_Alum.pdf) | full-text | Measured reflectance of a fresh aluminium mirror at 404–624 nm. Observatory technical report. |
| S8 | [Lemasters et al., *ACS Photonics* 6, 2600 (2019), author manuscript](https://par.nsf.gov/servlets/purl/10230835) | full-text | Continuous 5.66 nm Au film whose transmittance agrees with the bulk-permittivity transfer-matrix calculation. |
| S9 | [Kossoy et al., *Adv. Opt. Mater.* 3, 71 (2015), arXiv:1409.7338](https://arxiv.org/abs/1409.7338) | full-text | Continuous Au from 5.4 nm transmits less than the ideal film; agreement improves toward 15–20 nm. |
| S10 | [Goetz et al., *Nanoscale Adv.* 2, 869 (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9418784/) | full-text | Bulk optical properties sufficient for 6 nm sputtered Ag. |
| S11 | [Maniyara et al., *Nat. Photonics* 13, 328 (2019), arXiv:1809.01449](https://arxiv.org/abs/1809.01449) | full-text | Au percolation at 7 nm unseeded and 1 nm on a copper seed; continuous-metal optics to 1 nm; Drude damping 0.19 eV at 3 nm; island-plasmon dip fading from 7 nm. |
| S12 | [Hövel et al., *Phys. Rev. B* 81, 035402 (2010), arXiv:0904.4335](https://arxiv.org/abs/0904.4335) | full-text | Au 3–10 nm: dc transition at 6–7 nm with no optical signature; scattering rate and effective density against thickness. |
| S13 | [Ma et al., *Nat. Commun.* 15, 2248 (2024)](https://www.nature.com/articles/s41467-024-46467-6) | full-text | Ag percolation 12 nm, 9 nm with a TiOx seed; continuous at 4.5 nm and discontinuous but conducting at 3 nm when thinned back. |
| S14 | [Formica et al., *ACS Appl. Mater. Interfaces* 5, 3048 (2013)](https://research.birmingham.ac.uk/en/publications/ultrastable-and-atomically-smooth-ultrathin-silver-films-grown-on/) | abstract | Ag percolation thickness lowered to 3 nm by a 1 nm copper seed. |
| S15 | [Gong et al., *Sci. Rep.* 5, 9279 (2015)](https://www.nature.com/articles/srep09279) | full-text | Unseeded sputtered Ag: thickness-dependent n and k below 12 nm, non-metallic below 8 nm. |
| S16 | [Abd El-Fattah et al., "Plasmonics in Atomically-Thin Crystalline Silver Films", arXiv:1901.07739](https://arxiv.org/abs/1901.07739) | full-text | 7 monolayers of Ag(111): 1.65 nm, about 20 Ω per square; 10 monolayers: plasmons, damping 93 meV against 21 meV bulk; plane spacing 0.236 nm. Journal reference not re-opened. |
| S17 | [Nair et al., arXiv:0803.3718, published as *Science* 320, 1308 (2008)](https://arxiv.org/abs/0803.3718) | full-text | One atomic layer of graphene absorbs 2.3 % of white light. |
| S18 | [Scholl, Koh and Dionne, *Nature* 483, 421 (2012)](https://www.nature.com/articles/nature10904) | abstract | Plasmon resonance of single Ag particles from 20 nm to below 2 nm, shifting up by 0.5 eV. |
| S19 | [Amendola et al., *J. Phys.: Condens. Matter* 29, 203002 (2017), repository copy](https://iris.cnr.it/retrieve/dec6e068-f4c7-40b9-8749-a86d6318f7d8/prod_370803-doc_189094.pdf) | full-text | Resonance of Au particles emerges between 1.5 and 2 nm. Review. |
| S20 | [v. Baltz, "Plasmons and surface plasmons in bulk metals, metallic clusters, and metallic heterostructures", lecture article, Universität Karlsruhe](https://www.tkm.kit.edu/img/mitarbeiter/Er1995-Plasmons.pdf) | full-text | Table of carrier densities and measured plasmon energies: Al 15.0 eV, Ag 3.78 eV. Secondary; publication details are not in the opened text. |
| S21 | [Cazalilla et al., "Plasmonic excitations in noble metals: The case of Ag", arXiv:cond-mat/9907204](https://arxiv.org/abs/cond-mat/9907204) | full-text | Ag Drude plasma energy 9.2 eV; observed resonance near 3.8 eV; interband-screened plasma frequency. Journal reference not re-opened. |
| S22 | [Wyckoff, *Crystal Structures*, 2nd ed. (1963), as held in the Crystallography Open Database, entry 9008459](https://www.crystallography.net/cod/9008459.cif) | full-text | Lattice constants of Ag (entry 9008459) and Al (entry 9008460). Database copy, secondary. |
| S23 | [Cavalieri et al., *Nature* 449, 1029 (2007)](https://www.nature.com/articles/nature06229) | abstract | Delay of about 100 as between core and conduction-band photoelectrons from tungsten. |
| S24 | [Cohen and Louie, *Fundamentals of Condensed Matter Physics*, ch. 9, sec. 9.2 (excerpt)](https://webdisk.science.upjs.sk/~martin_gmitra/Theory%20of%20Condensed%20Matter/Supporting%20Materials/08%20-%2009/Drude_model_src%3AM.L.Cohen_S.G.Louie_Gauss_units.pdf) | full-text | Drude dielectric function and the Hagen–Rubens region, in Gaussian units. Textbook excerpt. |
