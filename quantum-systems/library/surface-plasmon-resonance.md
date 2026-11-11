---
id: surface-plasmon-resonance
title: Surface Plasmon Resonance (Interface-Bound Collective Mode)
status: formal
family: collective-field-response
constraints:
  - spatial-buffer
  - clock-latency
confidence_data: high
confidence_mapping: medium
review_depth: standard
related:
  - reflection
  - plasma-frequency-cutoff
  - skin-effect
  - total-internal-reflection
  - refraction-dielectric
updated: 2026-11-11
---

# Surface Plasmon Resonance (Interface-Bound Collective Mode)

### 4.1 Effect Name

Surface plasmon resonance (interface-bound collective mode)

### 4.2 Macroscopic Observation

At a metal–dielectric interface, a narrow dip appears in reflected intensity as angle or wavelength is scanned, provided a coupler (prism or grating) is present. Gold and silver films in the visible are the ordinary laboratory cases. The dip moves when the refractive index of the medium against the metal changes. Light incident from free space on a flat metal surface does not produce the dip. Away from the working thickness, in a strongly damped metal, or in a film of separate metal grains with too little metal, the feature broadens and then disappears.

### 4.3 Established Quantitative Boundaries

- **Model (Maxwell boundary-value solution for a planar interface).** A surface plasmon resonance is obtained when the real part of the metal film's permittivity is negative and larger in magnitude than both its own imaginary part and the permittivity of the adjoining medium. In the same prism geometry a film whose real permittivity is positive, and larger than its imaginary part and the surrounding permittivity, gives a different, "lossy mode" resonance [S1].
- **Model (dispersion relation).** The wavevector of the surface mode exceeds that of light in the adjoining dielectric, so a free-space photon cannot couple to it directly. A prism in attenuated total reflection (Kretschmann or Otto arrangement) or a grating supplies the difference [S2][S3].
- **Measured.** In the Kretschmann arrangement, gold films of 30, 52 and 70 nm were compared and a thickness of around 50 nm was found appropriate for sensitivity [S4].
- **Computed here.** Minimum p-polarised reflectance of prism (index 1.515) / metal / air at 633 nm, from the three-layer Fresnel formula with tabulated constants [S5]. Au (\(0.183 + 3.433i\)): 6 % at 40 nm, 0.9 % at 45 nm, 0.6 % at 50 nm, 15 % at 60 nm. Ag (\(0.056 + 4.278i\)): 13 % at 45 nm, 2.9 % at 50 nm, 1.0 % at 55 nm, 7 % at 60 nm. At 550 nm the Au minimum (\(0.424 + 2.472i\)) is deepest near 40 nm: 8 % at 30 nm, 0.03 % at 40 nm, 8 % at 50 nm. The working thickness is a window about 10 nm wide whose centre moves with metal and wavelength.
- **Computed here.** Lengths of the mode on a single interface, from the dispersion relation of §4.4 with tabulated \(n\) and \(k\); water is taken as \(\varepsilon_d = 1.7778\) [S8]:

  | Interface, wavelength | \(n,\ k\) | Run along the surface (intensity 1/e) | Field 1/e depth in the dielectric | Field 1/e depth in the metal |
  |---|---|---|---|---|
  | Ag–air, 633 nm [S5] | 0.056, 4.278 | 65 µm | 419 nm (0.66 λ) | 23 nm |
  | Ag–air, 633 nm [S6] | 0.0513, 4.318 | 73 µm | 423 nm (0.67 λ) | 23 nm |
  | Ag–water, 633 nm [S5] | 0.056, 4.278 | 25 µm | 230 nm (0.36 λ) | 22 nm |
  | Ag–air, 450 nm [S5] | 0.040, 2.648 | 13 µm | 176 nm (0.39 λ) | 25 nm |
  | Au–air, 633 nm [S5] | 0.183, 3.433 | 9.8 µm | 332 nm (0.52 λ) | 28 nm |
  | Au–air, 633 nm [S6] | 0.143, 3.610 | 15 µm | 350 nm (0.55 λ) | 27 nm |
  | Au–water, 633 nm [S5] | 0.183, 3.433 | 3.7 µm | 180 nm (0.28 λ) | 27 nm |
  | Au–air, 550 nm [S5] | 0.424, 2.472 | 1.3 µm | 207 nm (0.38 λ) | 33 nm |
  | Au–air, 450 nm [S5] | 1.383, 1.916 | 0.4 µm | 219 nm (0.49 λ) | 35 nm |

  The field reaches 22–35 nm into the metal and 0.3–0.7 of a wavelength into the dielectric. Along the surface the mode runs tens of micrometres on silver in the red and 5 to 7 times less far on gold at the same wavelength; on gold it falls to about a micrometre at 550 nm and below a micrometre at 450 nm.
- **Model (single-interface dispersion with measured constants; tertiary).** A tabulation at 650 nm gives 84 µm for Ag and 20 µm for Au, and names silver as the lowest-loss metal in the visible and near infrared [S3].
- **Measured.** Films of separate metal grains. Gold–dielectric composite films in the Kretschmann arrangement fall into three regimes by metal fill fraction: above about 0.6 the usual sharp dip; between about 0.4 and 0.6 a broad dip from a different surface mode; below about 0.4 the film supports no surface mode [S7].
- **Measured.** A colloid of spherical Au particles has an extinction band near 520 nm. It needs no prism and is a resonance of the particle, not the planar dip. The particle resonance appears only above a size of 1.5–2 nm [S2].
- **Computed here.** Above silver's edge a reflectance minimum can remain without a bound mode. At 300 nm, where \(\tilde n = 1.345 + 0.985i\) and so \(\varepsilon = 0.84 + 2.65i\) [S5], a 30 nm Ag film on a prism of index 1.488 has p-polarised reflectance 0.4 % at 55° and s-polarised reflectance 22 % at the same angle.

**Data confidence:** High — the existence condition, the need for a coupler and the thickness window are standard and were read in two reviews. The lengths in the table are model values from measured optical constants; no direct measurement of a propagation length was opened, and the one tabulation found is tertiary [S3]. The 50 nm thickness study [S4] was read as an abstract. No experiment that scans a Kretschmann dip through the plasma or interband edge of Ag or Al was found. The first version's statement that Al is used further into the ultraviolet was not checked against an opened source and is dropped.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Planar dispersion (semi-infinite metal / dielectric) [S3]:

  \[
  k_{\mathrm{sp}} = \frac{\omega}{c}\sqrt{\frac{\varepsilon_m\varepsilon_d}{\varepsilon_m+\varepsilon_d}}
  \]

  The run length is \(1/(2\operatorname{Im}k_{\mathrm{sp}})\). The field depth on each side is \(1/\lvert\operatorname{Im}k_z\rvert\) with \(k_z^2 = \varepsilon\,\omega^2/c^2 - k_{\mathrm{sp}}^2\).

- Prism matching (Kretschmann / Otto): \(k_\parallel = n_p(\omega/c)\sin\theta\). Resonance is the crossing of that line with \(k_{\mathrm{sp}}(\omega)\).
- The laboratory readout is a minimum in \(R(\theta)\) or \(R(\lambda)\) of the three-layer p-polarised Fresnel reflectance.
- Localized-particle resonance is a different condition on \(\varepsilon_m(\omega)\), not the planar \(k_{\mathrm{sp}}\) formula.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Three spatial resources, all required:
  1. a metal–dielectric interface (the mode is not a bulk plasma oscillation);
  2. a metal thickness inside the coupler window, about 45–55 nm for Au and Ag at 633 nm;
  3. enough metal in the plane: a fill fraction above about 0.6 for the sharp dip and above about 0.4 for any surface mode.

  The field occupies 22–35 nm of metal and 0.3–0.7 of a wavelength of dielectric. A coupler (prism index and angle, or a grating period) is part of the hardware although it is not the electron gas.

- **Clock rate / latency.** The optical cycle. The metal electrons must follow at the drive frequency, below the interband-screened edge, in the femtosecond class given in [reflection](reflection.md).

- **Energy barriers or thresholds.** None. Driven collective resonance, not a latch.

- **Dominant failure modes.**
  - **Threshold** — momentum: light whose in-plane wavevector is below \(k_{\mathrm{sp}}\) does not excite the mode, and from free space on a flat surface it is below at every angle. With a coupler the dip sits at the matching angle.
  - **Crossover** — thickness: the minimum reflectance changes continuously across the window, for Au at 633 nm from 6 % at 40 nm through 0.6 % at 50 nm to 15 % at 60 nm.
  - **Crossover** — metal fill of a granular film: the dip is sharp above a fill fraction of about 0.6, broad between about 0.4 and 0.6, and absent below about 0.4. The two boundaries are approximate values from one study.
  - **Threshold** — spectral, for the bound mode: it exists only while \(\operatorname{Re}\varepsilon_m\) is negative and exceeds \(\varepsilon_d\) in magnitude. A reflectance minimum of another origin can remain past that point, so the measured dip need not vanish there.
  - **Crossover** — dissipation: the run length on gold falls from 9.8 µm at 633 nm to 1.3 µm at 550 nm and 0.4 µm at 450 nm as interband absorption grows, and the dip widens with it.

- **Emergent constant or stable output.** A narrow angular or spectral absorption feature and a field bound to the interface, produced by oscillation of the metal electrons against the dielectric.

### 4.6 Internal Consistency Notes

The responding population is the same free-electron gas as [reflection](reflection.md) and [skin-effect](skin-effect.md). What is new is the interface and the coupler: this mode needs a second medium and extra in-plane momentum.

The coupler is an extra constraint that does not sit in the six allowed tags. It is a wavevector match, not a buffer, clock, barrier, lattice, field threshold, or thermal limit. Recording that as a gap in the tag set is more honest than inventing a seventh tag for one entry.

Sourcing changed three things. The first version contrasted "50 nm of gold" with "the 10–20 nm mirror threshold", which it called an electromagnetic and morphological floor. No such floor exists: reflectance falls smoothly with thickness (see reflection), and the morphological limit for this mode is the measured fill-fraction result above, with a broad dip surviving down to a fill of about 0.4. The spatial failure listed as "discontinuous morphology" is therefore a crossover with two named regimes. And the spectral failure is sharp only for the bound mode; in the same geometry an absorbing film above the edge still gives a p-polarised minimum, so a dip that persists above the edge would not by itself contradict the existence condition.

The 50 nm figure is the centre of a window whose location moves with wavelength, metal and coupler. Localized particle resonance is the same family with a different spatial resource (the particle) and must not be averaged into the planar-film number.

[Total internal reflection](total-internal-reflection.md) supplies the evanescent prism field that the Kretschmann and Otto arrangements use as the coupler. That is shared hardware, not a shared collapse.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — interface, optical clock and damping map onto the same electron gas as reflection, but the load-bearing momentum match is outside the present constraint tags, and the thickness and fill-fraction limits are windows and regimes, not a single buffer number.

## Related entries

- [reflection](reflection.md) — same metal electrons; bulk mirror against interface-bound mode
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — the edge above which the bound mode no longer exists
- [skin-effect](skin-effect.md) — decay into the metal is the optical end of the same screening
- [total-internal-reflection](total-internal-reflection.md) — the evanescent prism field is the usual coupler
- [refraction-dielectric](refraction-dielectric.md) — the dielectric half-space that sets \(\varepsilon_d\) and the light line

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Del Villar et al., "Optical sensors based on lossy-mode resonances", *Sens. Actuators B* 240, 174 (2017), accepted manuscript](https://ueaeprints.uea.ac.uk/71023/1/Accepted_Manuscript.pdf) | full-text | Existence condition for a surface plasmon resonance; lossy-mode resonance for positive real permittivity. Journal pages from a search listing, not re-opened. |
| S2 | [Amendola et al., *J. Phys.: Condens. Matter* 29, 203002 (2017), repository copy](https://iris.cnr.it/retrieve/dec6e068-f4c7-40b9-8749-a86d6318f7d8/prod_370803-doc_189094.pdf) | full-text | Attenuated-total-reflection couplers; Au colloid band near 520 nm; particle resonance emerging between 1.5 and 2 nm. Review. |
| S3 | [Wikipedia, "Surface plasmon polariton"](https://en.wikipedia.org/wiki/Surface_plasmon_polariton) | full-text | Momentum mismatch with a free-space photon; dispersion relation; propagation lengths at 650 nm computed from McPeak et al. data. Tertiary. |
| S4 | [Gwon and Lee, *Mater. Trans.* 51, 1150 (2010)](https://www.jstage.jst.go.jp/article/matertrans/51/6/51_M2010003/_article) | abstract | Kretschmann measurements on 30, 52 and 70 nm gold; about 50 nm appropriate. |
| S5 | [Johnson and Christy, *Phys. Rev. B* 6, 4370 (1972), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/Au/nk/Johnson.yml) | full-text | Au and Ag n and k (the Ag file is Ag/nk/Johnson.yml in the same database) for the computed minima and lengths. Database tabulation, secondary. |
| S6 | [McPeak et al., *ACS Photonics* 2, 326 (2015), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/Ag/nk/McPeak.yml) | full-text | Second set of Ag and Au constants (the Au file is Au/nk/McPeak.yml), giving the spread of the computed lengths. Secondary. |
| S7 | [Shi et al., *Opt. Lett.* 34, 3535 (2009)](https://doi.org/10.1364/OL.34.003535) | full-text | Three regimes of Kretschmann reflectance of gold–dielectric composite films by metal fill fraction. |
| S8 | [Daimon and Masumura, *Appl. Opt.* 46, 3811 (2007), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/H2O/nk/Daimon-20.0C.yml) | full-text | Index of water at 20.0 °C, giving the optical permittivity 1.7778 used for the water rows. Secondary. |
