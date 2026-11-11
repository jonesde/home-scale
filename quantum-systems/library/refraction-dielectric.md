---
id: refraction-dielectric
title: Refraction / Dielectric Polarization (Bound-Charge Response)
status: formal
family: collective-field-response
constraints:
  - spatial-buffer
  - clock-latency
  - field-threshold
confidence_data: high
confidence_mapping: medium
review_depth: standard
related:
  - reflection
  - total-internal-reflection
  - surface-plasmon-resonance
  - plasma-frequency-cutoff
  - dielectric-breakdown
  - semiconductor-gap-absorption
  - x-ray-absorption-edge
updated: 2026-11-12
---

# Refraction / Dielectric Polarization (Bound-Charge Response)

### 4.1 Effect Name

Refraction / dielectric polarization (bound-charge response)

### 4.2 Macroscopic Observation

A light beam crossing an interface between air and glass, water, or another transparent dielectric changes direction. A straight object standing in a pool looks bent; a prism produces a spectrum; a lens forms an image. The dielectric itself draws no continuous power. The same slab bends hard X-rays by a far smaller amount, and it ceases to be an insulator if the electric field is raised through dielectric breakdown.

### 4.3 Established Quantitative Boundaries

- **Computed here.** Refractive indices at 589.3 nm, evaluated from the dispersion formulas that were fitted to measurements (coefficients in the cited database files): water at 20.0 °C 1.33335 [S1]; fused silica at 20 °C 1.45840 [S2]; a borosilicate crown glass, N-BK7, 1.51673 [S3]; diamond 2.4173 [S4]; standard dry air at 15 °C and 101.325 kPa 1.000277 [S5]. These confirm the first version's rounded values.
- **Measured.** Static dielectric constant of water: 78.30 at 25 °C and 80.10 at 20 °C [S6].
- **Computed here.** Optical permittivity of water, \(n^2 = 1.7778\) from the index above. The static value is 45 times larger. A polarization channel that responds at low frequency contributes nothing at optical frequency.
- **Convention.** The X-ray index is written \(n = 1 - \delta - i\beta\), with \(\delta\) the refractive-index decrement and \(\beta\) the absorption index. The sign of the \(\beta\) term depends on the time convention [S7]. The first version wrote \(+i\beta\), the other convention.
- **Model (atomic scattering factors; free-electron limit).** \(\delta = (r_e\lambda^2/2\pi)\sum_i n_i f_i(0)\); at high photon energy \(f_1\) approaches the atomic number, so away from absorption edges \(\delta \propto n_e\lambda^2\) [S7].
- **Computed here.** \(\delta = n_e r_e\lambda^2/2\pi\) in that limit. Si (2.33 g cm⁻³): 5.4 × 10⁻⁵ at 3 keV, 7.4 × 10⁻⁶ at 8.05 keV, 1.2 × 10⁻⁶ at 20 keV. Water: 2.6 × 10⁻⁵, 3.6 × 10⁻⁶, 5.8 × 10⁻⁷. Au (19.3 g cm⁻³): 5.0 × 10⁻⁵ at 8.05 keV. At 1 keV the same formula gives 4.8 × 10⁻⁴ for Si. The first version put \(\delta\) of 10⁻⁶–10⁻⁵ "at a few keV"; that range belongs to about 8–20 keV in light solids. The mass densities are handbook inputs that were not separately sourced, and no tabulated \(\delta\) was opened.
- **Convention.** A slab of thickness \(d\) adds a phase \(2\pi(n-1)d/\lambda\) relative to vacuum. The phase is proportional to \(d\). A slab much thinner than a wavelength shifts a fringe and a longer path gives a resolvable ray kink; no thickness marks a beginning of refraction.
- **Computed here.** Optical period \(\lambda/c\): 1.50 fs at 450 nm, 1.83 fs at 550 nm, 2.17 fs at 650 nm.
- **Measured.** Dielectric strength, from a handbook compilation read on a tertiary page: air 3 MV m⁻¹ (geometry-dependent); window glass 9.8–13.8, alumina 13.4, borosilicate glass 20–40, polyethylene 19–160, mica 118, fused silica 470–670 and diamond 2000 MV m⁻¹ [S8]. The first version gave solids as "10⁷–10⁸ V m⁻¹"; the listed solids run from 10⁷ to above 10⁹ V m⁻¹. Breakdown ends the dielectric operating window; it is not a sharper location of \(n\).

**Data confidence:** High — the indices and the static constant of water come from fitted measurements and a primary paper. Three points are weaker. The dielectric strengths rest on a tertiary page only [S8]. The X-ray \(\delta\) values are this file's free-electron estimate. The first version's list of polarization channels (electronic, ionic, orientational) and the bands in which each falls away was not checked against an opened source; the water numbers show that such a channel exists, and the assignment is the textbook account.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Snell's law:

  \[
  n_1\sin\theta_1 = n_2\sin\theta_2
  \]

- Non-magnetic media: \(n = \sqrt{\varepsilon_r}\). The frequency-dependent permittivity \(\varepsilon(\omega)\) is the measured dielectric function of the bound-charge population.

- Clausius–Mossotti (static, mean field) and Lorentz–Lorenz (optical):

  \[
  \frac{\varepsilon_r - 1}{\varepsilon_r + 2} = \frac{N\alpha}{3\varepsilon_0},\qquad
  \frac{n^2 - 1}{n^2 + 2} = \frac{N\alpha}{3\varepsilon_0}
  \]

  \(N\) is number density, \(\alpha\) polarizability. These relate measured bulk constants to a molecular parameter; they are not a derivation of \(n\) from node rules. No source for them was opened in this pass.

- X-ray decrement [S7]: \(\delta = (r_e\lambda^2/2\pi)\sum_i n_i f_i(0)\). Sellmeier and similar pole expansions [S1][S2][S3][S4] are fits to \(n(\lambda)\), not mechanisms.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A volume of polarizable bound charge, and a path through it. The accumulated phase is proportional to \((n-1)\) times the path, so the output grows with the amount of responding material traversed and no minimum is measured. Vacuum (\(N = 0\)) and the X-ray limit (\(\delta \to 0\)) are the low-contrast end of the same resource: a dielectric of any thickness shows \(n - 1 \approx 0\) if its charges do not respond at that frequency.

- **Clock rate / latency.** The polarization must follow the optical cycle, 1.5–2.2 fs across the visible. A channel too slow for the drive drops out, which is why the optical permittivity of water is 1.78 against a static 80. Drive far above the electronic response leaves \(n \approx 1\).

- **Energy barriers or thresholds.** Refraction is a driven collective response, not a latch: zero continuous power, no stored directional state. The high-field edge of the window is dielectric breakdown, which converts the insulator into a conducting path and belongs to a different machine class ([dielectric-breakdown](dielectric-breakdown.md)).

- **Dominant failure modes.**
  - **Crossover** — spectral and density: \(n - 1\) falls continuously toward zero as the drive frequency rises past the electronic response, as \(\delta \propto n_e\lambda^2\) in the X-ray range (10⁻⁵ near 8 keV and 10⁻⁶ near 20 keV for light solids).
  - **Crossover** — path: the phase \(2\pi(n-1)d/\lambda\) is proportional to \(d\). "A path of a wavelength or more" is a convention for when the result is called a ray.
  - **Crossover** — contrast: the bend goes continuously to zero as \(n_1 \to n_2\), by Snell's law.
  - **Threshold** — field: a given sample stops insulating at its breakdown field. Where that field lies, and how it depends on gap, thickness and time, is owned by [dielectric-breakdown](dielectric-breakdown.md).

- **Emergent constant or stable output.** A stable, material- and frequency-specific \(n(\omega)\) and the macroscopic ray kink of Snell's law, produced by polarization of the bound charge in step with the field.

### 4.6 Internal Consistency Notes

Bound-charge refraction and free-electron [reflection](reflection.md) sit in the same family: many charged nodes and a collective electromagnetic output. The node species differs (bound against free). [Total internal reflection](total-internal-reflection.md) is the geometry and index gate on this same \(n\); it is not a new population.

Sourcing changed the comparison with reflection. The first version said this mapping does not close "at the same sharpness as the metal mirror" and twice contrasted refraction with "the 10–20 nm metal-mirror threshold". That threshold does not exist: reflectance, like the phase here, grows continuously with the thickness traversed (see reflection). The two entries now agree on the spatial clause, and neither has a minimum buffer. Two numbers were also corrected: the photon energy at which \(\delta\) is 10⁻⁶–10⁻⁵, and the range of solid breakdown fields.

The mapping takes tabulated \(n(\omega)\) and the X-ray \(\delta\) as the contrast specification. Clausius–Mossotti and Lorentz–Lorenz relate that contrast to \(N\alpha\) but do not derive \(\alpha\) from node rules. That is a gap, not a contradiction.

Breakdown is listed as a failure of the dielectric window, not as the primary collapse of refraction. Filing it here under the field-threshold tag and pointing at `dielectric-breakdown` keeps the families from being mixed. X-ray \(n < 1\) (grazing total external reflection) is the same kinematic gate as total internal reflection with inverted contrast; the geometry is owned by that entry.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — Snell's law and \(n(\omega)\) are stable collective outputs of a polarizable population, and the loss of contrast at high frequency is measured, but every failure of refraction itself is a crossover and the contrast is taken, so the mapping locates no buffer or clock threshold.

## Related entries

- [reflection](reflection.md) — free-electron counterpart: collective screening instead of bound-charge phase delay
- [total-internal-reflection](total-internal-reflection.md) — geometry and index gate on this same \(n\)
- [surface-plasmon-resonance](surface-plasmon-resonance.md) — metal–dielectric interface using both populations
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — free-electron spectral edge; contrast case for the bound-charge spectrum
- [Dielectric breakdown](dielectric-breakdown.md) — field-opened destruction of the insulating window
- [Semiconductor gap absorption](semiconductor-gap-absorption.md) — a crystal can refract below the gap and absorb above it
- [X-ray absorption edge](x-ray-absorption-edge.md) — structure in \(\delta(\omega)\) and \(\beta(\omega)\) at inner-shell gates

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Daimon and Masumura, *Appl. Opt.* 46, 3811 (2007), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/H2O/nk/Daimon-20.0C.yml) | full-text | Sellmeier fit for distilled water at 20.0 °C; index and optical permittivity. Database copy, secondary. |
| S2 | [Malitson, *J. Opt. Soc. Am.* 55, 1205 (1965), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/SiO2/nk/Malitson.yml) | full-text | Sellmeier fit for fused silica. Secondary. |
| S3 | [SCHOTT optical glass catalogue (Zemax file of 2017-01-20), N-BK7, as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/specs/schott/optical/N-BK7.yml) | full-text | Maker's Sellmeier fit for one borosilicate crown glass. Secondary. |
| S4 | [Peter, *Z. Phys.* 15, 358 (1923), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/C/nk/Peter.yml) | full-text | Sellmeier fit for diamond. Secondary. |
| S5 | [Ciddor, *Appl. Opt.* 35, 1566 (1996), as tabulated in the refractiveindex.info database](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/other/mixed%20gases/air/nk/Ciddor.yml) | full-text | Fitted equation for standard dry air. Secondary. |
| S6 | [Malmberg and Maryott, *J. Res. Natl. Bur. Stand.* 56, 1 (1956)](https://nvlpubs.nist.gov/nistpubs/jres/56/jresv56n1p1_A1b.pdf) | full-text | Static dielectric constant of water: 78.30 at 25 °C, 80.10 at 20 °C. |
| S7 | [Gullikson, *X-Ray Data Booklet*, sec. 1.7 "Atomic scattering factors" (Lawrence Berkeley National Laboratory)](https://xdb.lbl.gov/Section1/Sec_1-7.pdf) | full-text | Form of the X-ray index, the decrement formula and its high-energy limit. |
| S8 | [Wikipedia, "Dielectric strength", table citing the *CRC Handbook of Chemistry and Physics*](https://en.wikipedia.org/wiki/Dielectric_strength) | full-text | Dielectric strengths of air and of the listed solids. Tertiary. |
