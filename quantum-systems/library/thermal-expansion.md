---
id: thermal-expansion
title: Thermal Expansion (Anharmonic Length Change)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
  - thermal
confidence_data: high
confidence_mapping: medium
review_depth: standard
related:
  - phonon-dispersion
  - debye-cutoff
  - elasticity
  - melting
  - thermal-conductivity-phonon
  - magnetostriction
  - speed-of-sound
  - thermal-equilibrium-temperature
updated: 2026-11-13
---

# Thermal Expansion (Anharmonic Length Change)

### 4.1 Effect Name

Thermal expansion (anharmonic length change)

### 4.2 Macroscopic Observation

A metal rod lengthens when heated and shortens when cooled, reversibly, below melting. The fractional change is between about 5 and 30 parts per million per kelvin at room temperature and grows with temperature. Invar, an iron–nickel alloy with 36 % nickel, expands a hundred times less than iron near room temperature and regains an ordinary expansivity when hot. A few solids contract on heating over part of their range. A lattice of purely harmonic springs would do none of this: its mean spacing does not depend on vibration amplitude.

### 4.3 Established Quantitative Boundaries

- **Convention.** The expansivity is \(\alpha = (1/L)(dL/dT)\) at a stated temperature; engineering texts often quote a mean coefficient over a range instead, and the two can differ noticeably [S1].
- **Measured.** Linear expansivity of polycrystalline elements, in \(10^{-6}\) K⁻¹ [S1]:

  | Element | 100 K | 293 K | 500 K | 800 K |
  |---|---|---|---|---|
  | Tungsten | 2.6 | 4.5 | 4.6 | 5.0 |
  | Titanium | 4.5 | 8.6 | 9.9 | 11.1 |
  | Iron | 5.6 | 11.8 | 14.4 | 16.2 |
  | Nickel | 6.6 | 13.4 | 15.3 | 16.8 |
  | Copper | 10.3 | 16.5 | 18.3 | 20.3 |
  | Aluminium | 12.2 | 23.1 | 26.4 | 34.0 |
  | Zinc | 24.5 | 30.2 | 32.8 | – |

  At 293 K the metals listed run from 4.5 (tungsten) to 30.2 (zinc).
- **Measured.** The expansivities of most solids increase with temperature [S1]; aluminium rises by a factor of 2.8 between 100 K and 800 K.
- **Measured.** Invar (64 Fe, 36 Ni): 1.4 at 100 K, 0.53 at 200 K, 0.13 at 293 K, 5.1 at 500 K and 17.1 at 800 K, in the same units. Super Invar (63 Fe, 32 Ni, 4 Co): 0.0 at 293 K [S1]. Nickel–iron–cobalt alloys have low expansivity below a transformation temperature and high expansivity above it, and both depend critically on composition [S1].
- **Computed here.** At 293 K iron expands 91 times as much as Invar. Invar's own expansivity is 39 times larger at 500 K than at 293 K, so the low value belongs to a window around room temperature.
- **Measured.** Negative expansivity exists: silicon \(-0.4\) and fused silica \(-0.53\) at 100 K; pyrolytic graphite \(-0.6\) perpendicular to the deposition direction at 293 K. Diamond is 0.05 at 100 K and 1.0 at 293 K [S1].
- **Model (isotropic solid).** The volume expansivity is three times the linear one to first approximation [S1].
- **Model (magnetovolume).** Invar's low expansion is attributed to a magnetic contribution to the volume that shrinks on heating and offsets the lattice term [S2]. The reference was not opened; the handbook's statement that the low value ends at a transformation temperature is consistent with it [S1]. Volume magnetostriction proportional to the square of the magnetization is measured in gadolinium [S3].
- **Model (harmonic lattice).** With purely quadratic wells the mean spacing is independent of temperature and \(\alpha = 0\). No source was opened for this statement; it is a textbook result.
- **Computed here.** Strains for scale: copper heated by 100 K, \(1.65 \times 10^{-3}\); aluminium by 100 K, \(2.31 \times 10^{-3}\); nickel by 10 K, \(1.34 \times 10^{-4}\). The copper figure is 2.4 times the elastic strain at yield of annealed copper, 90 MPa over 129.8 GPa or \(6.9 \times 10^{-4}\) [S4][S5], so a fully constrained copper part heated by 100 K yields.

**Data confidence:** High for the tabulated expansivities, read in one handbook section that cites the standard compilation. The Invar mechanism rests on a reference that was not opened. No table of Grüneisen parameters was found, so none is quoted.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Definition: \(\alpha = \frac{1}{L}\bigl(\frac{\partial L}{\partial T}\bigr)_P\), and \(\alpha_V \approx 3\alpha\) for an isotropic solid [S1].
- Over limited ranges, \(\alpha = a + bT + cT^2\) [S1].
- Grüneisen relation: \(\gamma = 3\alpha B/(C_V\rho) = -d\ln\omega/d\ln V\). The second form makes \(\gamma\) the volume sensitivity of the lattice frequencies. A harmonic spectrum has \(\gamma = 0\). A mode with negative \(\gamma\) contributes contraction, which is how the negative values above are described.
- Thermal strain over a finite range: \(\varepsilon = \int\alpha\,dT\).

No equation in this entry predicts Invar's window from its composition.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A coupled lattice whose wells are not purely quadratic. The harmonic lattice that gives sound speeds and moduli is not sufficient. Invar adds a magnetic volume term.

- **Clock rate / latency.** No clock of its own. The length follows the temperature of the specimen ([thermal-equilibrium-temperature](thermal-equilibrium-temperature.md)).

- **Energy barriers or thresholds.** None. The condition is anharmonic wells and a finite temperature.

- **Dominant failure modes.**
  - **Crossover** — low temperature: \(\alpha\) falls toward zero as the modes freeze out; copper drops from 16.5 at 293 K to 10.3 at 100 K.
  - **Crossover** — compensation: a second channel offsets the lattice term over a limited temperature window. Invar is 0.13 at 293 K and 5.1 at 500 K.
  - **Crossover** — sign: modes that soften under compression contribute negative expansion; silicon and fused silica are negative at 100 K.
  - **Threshold** — melting: the solid's \(\alpha\) ends at \(T_m\) ([melting](melting.md)).
  - **Threshold** — harmonic limit: \(\gamma = 0\) gives \(\alpha = 0\). This is a limiting condition on the wells and no material reaches it.

- **Emergent constant or stable output.** A material-typical \(\alpha(T)\), 4.5 to 30 \(\times 10^{-6}\) K⁻¹ for the metals tabulated at 293 K, rising with temperature.

### 4.6 Internal Consistency Notes

The harmonic lattice of [elasticity](elasticity.md) and [speed-of-sound](speed-of-sound.md) gives moduli and sound speeds and no expansion. Expansion is the leading anharmonic correction, and umklapp scattering in [thermal-conductivity-phonon](thermal-conductivity-phonon.md) draws on the same anharmonicity.

Sourcing changed three points. The metal class is 4.5 to 30 \(\times 10^{-6}\) K⁻¹ at room temperature; the first version gave \(10^{-6}\) to \(10^{-5}\), which excludes aluminium and zinc. Anharmonicity does not fix the sign: some solids contract on heating, so "anharmonic wells produce expansion" was too strong. Invar's near-zero value is confined to a window near room temperature and is gone by 500 K.

The mapping is medium because anharmonicity is a condition and not one number. There is no measured threshold at which expansion appears. The Grüneisen parameter that would quantify it could not be sourced here.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the measured \(\alpha(T)\), the Invar window and the negative-expansion cases identify anharmonicity as the resource, but it is not pinned to a single measured hardware number.

## Related entries

- [phonon-dispersion](phonon-dispersion.md) — \(\omega(q)\) whose volume shift is \(\gamma\)
- [debye-cutoff](debye-cutoff.md) — heat capacity that \(\alpha\) tracks at low temperature
- [elasticity](elasticity.md) — harmonic moduli that expansion corrects; yield strain for comparison
- [melting](melting.md) — the high-temperature end of the same wells
- [thermal-conductivity-phonon](thermal-conductivity-phonon.md) — umklapp from the same anharmonicity
- [magnetostriction](magnetostriction.md) — uses the nickel expansivity for scale; Invar's magnetic volume term
- [speed-of-sound](speed-of-sound.md) — long-wave speeds that shift with volume
- [thermal-equilibrium-temperature](thermal-equilibrium-temperature.md) — the temperature that occupies the modes

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Kaye and Laby, *Tables of Physical and Chemical Constants*, §2.3.5 Thermal expansion (NPL, archived)](https://web.archive.org/web/2019/http://www.kayelaby.npl.co.uk/general_physics/2_3/2_3_5.html) | full-text | Definitions; expansivity of elements, Invar and Super Invar against temperature; negative values; rise with temperature; volume expansivity. |
| S2 | [van Schilfgaarde, Abrikosov and Johansson, *Nature* 400, 46 (1999)](https://www.nature.com/articles/21848) | cited-only | Magnetic origin of the Invar effect. The page redirected to a login, so neither the text nor the bibliographic details were verified. |
| S3 | [Hutchinson, "The magnetostriction of nickel and gadolinium", PhD thesis, Durham (1958)](https://etheses.durham.ac.uk/id/eprint/9170/) | abstract | Volume magnetostriction of gadolinium proportional to the square of the magnetization. |
| S4 | [Johnson and Cook, *Proc. 7th Int. Symp. on Ballistics*, The Hague (1983)](https://archive.org/details/AConstitutiveModelAndDataForMetals) | full-text | Yield constant of OFHC copper, 90 MPa. |
| S5 | [Kaye and Laby, §2.2.2 Elasticities and strengths (NPL, archived)](https://web.archive.org/web/2018/http://www.kayelaby.npl.co.uk/general_physics/2_2/2_2_2.html) | full-text | Young's modulus of copper. |
