---
id: speed-of-sound
title: Speed of Sound (Long-Wave Acoustic Slope)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
  - clock-latency
confidence_data: high
confidence_mapping: high
review_depth: standard
related:
  - phonon-dispersion
  - debye-cutoff
  - elasticity
  - melting
  - thermal-conductivity-phonon
  - ideal-gas-pressure
updated: 2026-11-13
---

# Speed of Sound (Long-Wave Acoustic Slope)

### 4.1 Effect Name

Speed of sound (long-wave acoustic slope)

### 4.2 Macroscopic Observation

A pressure or shear disturbance launched in air, water or a solid arrives at a distant detector after a finite delay. The implied speed is typical of the material and far below the speed of light. In water and in solids it does not depend on frequency across the acoustic and ultrasonic range; some polyatomic gases show a small step near a molecular relaxation frequency. Solids carry a faster longitudinal wave and a slower shear wave. Liquids and gases carry one compressional wave. A vacuum carries no sound.

### 4.3 Established Quantitative Boundaries

- **Measured.** Dry air with 0.03 % CO₂ at 0 °C and 101.325 kPa: \(331.46 \pm 0.10\) m s⁻¹. At 20 °C and 10 % relative humidity: 343.5 m s⁻¹, rising to 344.5 m s⁻¹ at 90 % [S1].
- **Model (ideal gas, adiabatic).** \(c = \sqrt{\gamma p/\rho} = \sqrt{\gamma RT/M}\), proportional to \(\sqrt T\) and independent of pressure to first order [S1]. For dry air \(\gamma\) is 1.401–1.402 between 0 and 17 °C [S3].
- **Computed here.** Scaling the 0 °C value by \(\sqrt{293.15/273.15}\) gives 343.4 m s⁻¹ for dry air at 20 °C, in agreement with the table.
- **Measured.** Air-free distilled water: 1482.36 m s⁻¹ at 20 °C (1447.28 at 10 °C, 1509.14 at 30 °C). The speed passes through a maximum near 74 °C, rises by about 0.156 m s⁻¹ per atmosphere, and water is non-dispersive [S1]. Mercury at 25 °C: 1449 m s⁻¹. Liquid tin at 240 °C: 2471 m s⁻¹; liquid zinc at 450 °C: 2780 m s⁻¹ [S1].
- **Model (continuum).** In a fluid \(c = (\beta_a\rho)^{-1/2}\) with \(\beta_a\) the adiabatic compressibility [S1].
- **Measured.** Solids, in m s⁻¹, as bulk longitudinal, thin-rod and shear speeds [S1]:

  | Material | Longitudinal (bulk) | Rod | Shear |
  |---|---|---|---|
  | Mild steel | 5960 | 5196 | 3235 |
  | Stainless steel | 5980 | 5282 | 3297 |
  | Iron, soft | 5957 | 5189 | 3224 |
  | Aluminium | 6374 | 5102 | 3111 |
  | Copper | 4759 | 3813 | 2325 |
  | Nickel, soft | 5608 | 4787 | 2929 |
  | Titanium | 6130 | 5164 | 3182 |
  | Fused silica | 5968 | 5760 | 3764 |
  | Lead | 2160 | 1188 | 700 |

- **Computed here.** From the elastic constants of [elasticity](elasticity.md) [S5] and handbook densities [S2], \(\sqrt{(K + 4G/3)/\rho}\) and \(\sqrt{G/\rho}\) give 4750 and 2322 m s⁻¹ for copper, 6393 and 3110 for aluminium, and 5595 and 2922 for nickel. Each is within 0.3 % of the measured value in the table. In mild steel the shear speed is 0.54 of the longitudinal speed.
- **Measured.** Liquids are tabulated with a single speed [S1]. At much higher frequency a liquid does carry short-lived transverse excitations: in liquid gallium above a wavevector of 9 nm⁻¹, with a lifetime of 0.5 ps and a range of 0.4–0.5 nm [S4].
- **Measured.** Dispersion in gases. Many polyatomic gases show a higher speed above a molecular relaxation frequency; carbon dioxide at 51 °C goes from 280 to 293 m s⁻¹ [S1].
- **Computed here.** Transit times: 5 m of air takes 14.6 ms; 5 m of steel rod takes 0.96 ms; 5 cm of steel rod takes 9.6 µs.

**Data confidence:** High. Every number was read in one handbook section and the solid speeds were cross-checked against elastic constants from a different section. The shear-in-liquid exception rests on an abstract.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Longitudinal speed in an extended solid: \(v_L = \sqrt{(K + 4G/3)/\rho}\). In a fluid \(G = 0\) and \(v_L = \sqrt{K_s/\rho}\).
- Thin rod: \(v = \sqrt{E/\rho}\).
- Shear speed, solid only: \(v_T = \sqrt{G/\rho}\).
- Long-wave dispersion: \(\omega = v_s|q|\) for \(qa \ll 1\). At shorter wavelength the full \(\omega(q)\) of [phonon-dispersion](phonon-dispersion.md) applies.
- Transit time over a path \(L\): \(t = L/v_s\).

The moduli are the small-strain numbers of [elasticity](elasticity.md). This entry does not derive them.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A coupled mechanical medium with many nodes per wavelength: a lattice in a solid, a colliding density field in a fluid. The continuum speed holds for wavelengths long against the spacing. A vacuum has no medium. A fluid has compressional coupling and, at acoustic frequencies, no shear coupling.

- **Clock rate / latency.** The transit time \(L/v_s\): 14.6 ms for 5 m of air, about a millisecond for 5 m of steel, about 10 µs for 5 cm of steel.

- **Energy barriers or thresholds.** None stored. The condition is a finite restoring modulus and a density.

- **Dominant failure modes.**
  - **Threshold** — medium: no medium, no wave.
  - **Threshold** — shear restoring force: on melting the static shear modulus goes from a finite value to zero and the shear wave is lost ([melting](melting.md)).
  - **Crossover** — frequency in a liquid: transverse response reappears when the period is shorter than the structural relaxation time, about 0.5 ps in liquid gallium.
  - **Crossover** — wavelength: as \(qa\) approaches 1 the speed is no longer the group velocity; the mode continues on the dispersion curve.
  - **Crossover** — relaxation and attenuation: the speed in a polyatomic gas steps up across a relaxation frequency (5 % in carbon dioxide); attenuation in water grows as the square of the frequency [S1].

- **Emergent constant or stable output.** A pair \(\{v_L, v_T\}\) in a solid or a single speed in a fluid, fixed by modulus and density.

### 4.6 Internal Consistency Notes

The split between vacuum, fluid and solid follows which restoring couplings are present. Reading \(v_s\) as the long-wave slope of the same lattice that [phonon-dispersion](phonon-dispersion.md) maps at finite \(q\) is consistent, and the computed speeds match the measured ones to 0.3 %.

Sourcing changed three statements. The transit time in a metal bar of room length is about a millisecond; the first version said microseconds, which holds for centimetres. Frequency independence has exceptions in relaxing gases. And "no shear in a liquid" is a statement about acoustic frequencies: at picosecond periods a liquid responds transversely over a few atomic spacings. The water value moved from 1480 to 1482 m s⁻¹.

A closed mapping would also give the moduli from node-level springs. That is the gap carried by [elasticity](elasticity.md) and does not affect the speeds.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the measured speeds follow from modulus and density to a fraction of a per cent, and the vacuum and fluid-shear failures translate directly into a medium-plus-modulus condition.

## Related entries

- [phonon-dispersion](phonon-dispersion.md) — full \(\omega(q)\); this entry is the acoustic \(q\to 0\) slope
- [debye-cutoff](debye-cutoff.md) — the short-wave ceiling on the same lattice
- [elasticity](elasticity.md) — the moduli that enter \(v_s=\sqrt{C/\rho}\)
- [melting](melting.md) — the shear wave is lost at \(T_m\)
- [thermal-conductivity-phonon](thermal-conductivity-phonon.md) — uses \(v_s\) as the carrier speed
- [ideal-gas-pressure](ideal-gas-pressure.md) — gas as a different mechanical medium

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Kaye and Laby, *Tables of Physical and Chemical Constants*, §2.4.1 The speed and attenuation of sound (NPL, archived)](https://web.archive.org/web/2018/http://www.kayelaby.npl.co.uk/general_physics/2_4/2_4_1.html) | full-text | Air, water, liquid metals and solids; gas and liquid formulas; dispersion in polyatomic gases; attenuation in water. |
| S2 | [NIST, X-Ray Mass Attenuation Coefficients, Table 1 (element densities)](https://physics.nist.gov/PhysRefData/XrayMassCoef/tab1.html) | full-text | Densities of Cu, Al and Ni for the computed speeds. |
| S3 | [Kaye and Laby, §2.3.6 Specific heat capacities (NPL, archived)](https://web.archive.org/web/2019/http://www.kayelaby.npl.co.uk/general_physics/2_3/2_3_6.html) | full-text | Ratio of specific heats of dry air. |
| S4 | [Hosokawa et al., *Phys. Rev. Lett.* 102, 105502 (2009)](https://doi.org/10.1103/PhysRevLett.102.105502) | abstract | Transverse acoustic excitations in liquid gallium. |
| S5 | [Kaye and Laby, §2.2.2 Elasticities and strengths (NPL, archived)](https://web.archive.org/web/2018/http://www.kayelaby.npl.co.uk/general_physics/2_2/2_2_2.html) | full-text | Bulk and shear moduli of Cu, Al and Ni for the computed speeds. |
