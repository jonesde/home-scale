---
id: cyclotron-resonance
title: Cyclotron Resonance (Orbital Clock Match)
status: formal
family: collective-field-response
constraints:
  - clock-latency
  - field-threshold
  - thermal
confidence_data: high
confidence_mapping: high
review_depth: light
related:
  - faraday-rotation
  - skin-effect
  - plasma-frequency-cutoff
  - quantum-hall-effect
  - semiconductor-gap-absorption
updated: 2026-11-11
---

# Cyclotron Resonance (Orbital Clock Match)

### 4.1 Effect Name

Cyclotron resonance (orbital clock match)

### 4.2 Macroscopic Observation

A semiconductor or metal in a magnetic field absorbs a microwave or infrared drive when the drive frequency matches the cyclotron frequency of the carriers. The resonance field at a known frequency is read as an effective mass. Off resonance the absorption falls. In a sample whose carriers scatter too often the line is not resolved at the matching field. No continuous power is required of the sample beyond the probing field.

### 4.3 Established Quantitative Boundaries

- **Convention.** Cyclotron frequency \(\omega_c = eB/m^*\), \(f_c = eB/2\pi m^*\) [S4].
- **Computed here.** Free electron, from the CODATA mass [S1]: \(f_c/B = 27.99\,\mathrm{GHz\,T^{-1}}\). The electron spin-resonance value is \(28.025\,\mathrm{GHz\,T^{-1}}\) [S2], higher by 0.116 %. The two lines are close but distinct, and they belong to different degrees of freedom (orbital and spin).
- **Measured.** GaAs conduction electrons: \(m^* = 0.067\,m_0\) [S4]. Germanium electrons near 4 K: \(m_l = 1.58\,m\), \(m_t = 0.082\,m\), spheroids along ⟨111⟩. Silicon electrons: \(m_l = 0.97\,m\), \(m_t = 0.19\,m\), spheroids along ⟨100⟩ [S3].
- **Computed here.** \(f_c/B\) is \(0.42\,\mathrm{THz\,T^{-1}}\) for GaAs, \(0.34\,\mathrm{THz\,T^{-1}}\) for the Ge transverse mass and \(0.15\,\mathrm{THz\,T^{-1}}\) for the Si transverse mass.
- **Model (Drude line).** A well-resolved line needs \(\omega_c\tau \gg 1\), which is the same statement as \(\mu B \gg 1\) with \(\mu\) the mobility [S5].
- **Computed here.** \(\omega_c\tau = 1\) at 1 T needs \(\tau = 5.7\) ps for a free electron and 0.38 ps in GaAs, or a mobility of \(10^4\,\mathrm{cm^2\,V^{-1}\,s^{-1}}\) for any mass.
- **Measured.** Low temperature is one way to meet the condition, not a requirement. Films with a mobility of \(100\,\mathrm{cm^2\,V^{-1}\,s^{-1}}\) give resolved lines in fields above 100 T, one of them at 295 K [S5]; at 100 T that mobility gives \(\mu B = 1\) (computed here).
- **Measured.** Semiconductors: the line is seen with radiation travelling along \(\mathbf{B}\), for one sense of circular polarization only, at frequencies above the plasma frequency where the field penetrates the sample [S4].
- **Measured.** Metals: the line is seen below the plasma frequency with \(\mathbf{B}\) parallel to the surface. The field occupies a thin skin layer ([skin-effect](skin-effect.md)); carriers accelerated there orbit in the bulk and return to the layer in step with the drive (Azbel'–Kaner resonance) [S4].
- **Measured.** In a two-dimensional electron sheet the collective absorption line is shifted above \(\omega_c\) by the sheet's plasma oscillation, \(\omega^2 = \omega_p^2 + \omega_c^2\); a line at the unshifted \(\omega_c\) was seen at the edge of a metal electrode [S4].

**Data confidence:** High — the masses are primary measurements and the frequency scale follows from CODATA constants. The Si and Ge values were read in an abstract. The first version's harmonic condition \(\omega = n\omega_c\) had no opened source and was dropped.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Resonance at \(\omega = \omega_c\) for a uniform drive; at \(\omega^2 = \omega_p^2 + \omega_c^2\) for the collective mode of a sheet [S4].
- Absorption against \(B\) or \(\omega\) is a line of width about \(1/\tau\). The measured resonance field at known \(\omega\) is inverted for \(m^*\).
- Anisotropic bands: \(\omega_c\) depends on the direction of \(\mathbf{B}\) relative to the mass tensor, and the angular pattern gives \(m_l\) and \(m_t\) [S3].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A carrier population in a field, with a scattering time long enough that an orbit is a defined clock (\(\omega_c\tau\) above about 1). In a metal the added spatial resource is the skin layer the orbit must re-enter. There is no film-thickness specification. The quantity that gates the line is the scattering time against the orbit period, a clock resource.

- **Clock rate / latency.** Load-bearing. The drive must match \(\omega_c = eB/m^*\): 28 GHz per tesla for a free electron, 0.42 THz per tesla in GaAs. \(B\) sets the clock and \(\tau\) is the reset time of the orbital motion. In a sheet the collective clock is \(\sqrt{\omega_p^2 + \omega_c^2}\).

- **Energy barriers or thresholds.** No latch. \(B\) sets \(\omega_c\) and raises \(\omega_c\tau\). The `field-threshold` tag marks that resource.

- **Dominant failure modes.**
  - **Crossover** — clock: detuning from \(\omega_c\) lowers the absorption along a line of width about \(1/\tau\).
  - **Crossover** — scattering / thermal: the line broadens and merges into the background as \(\omega_c\tau = \mu B\) falls through about 1. Temperature acts by shortening \(\tau\); a higher field compensates.
  - **Threshold** — polarization: the opposite circular sense is not absorbed.
  - **Threshold** — metal geometry: the line is observed with \(\mathbf{B}\) parallel to the surface, where orbits re-enter the skin layer.
  - **Crossover** — field: \(B \to 0\) sends \(\omega_c\) and \(\omega_c\tau\) to zero together.

- **Emergent constant or stable output.** An absorption line whose position gives the effective mass, or mass tensor, of the carrier population.

### 4.6 Internal Consistency Notes

A clock match with a scattering-time condition is a clean specification, and the pair named in the index (\(\omega \ne \omega_c\), or \(\omega_c\tau < 1\)) is that pair.

Sourcing changed four things. The free-electron line is at 27.99 GHz per tesla and the spin line at 28.025; the first version said they coincide. The visibility condition is a crossover in \(\mu B\), met at room temperature above 100 T in a low-mobility film, so "clean and cold" is one route to it. In a sheet the line that an absorption experiment sees is shifted by the plasma term, so the line position is the mass only after that correction. And the metal-geometry statement now rests on a source that says where the line is observed, not that it is absent elsewhere. The GaAs mass did not change.

The open item is \(m^*\). The mapping records \(0.067\,m_0\) as a measured output of the lattice-plus-carrier machine and does not derive it. Filing under collective-field-response is consistent: the line is a synchronized orbital response of many carriers and fades when their common clock cannot be kept.

[Faraday rotation](faraday-rotation.md) is the off-resonant cumulative relative. `quantum-hall-effect` uses the same two-dimensional carriers at high \(\mu B\); its output is a quantized Hall resistance, not a mass line.

### 4.7 Overall Confidence in the QSA Mapping

**High** — matching \(\omega\) to \(eB/m^*\) and the \(\omega_c\tau\) condition translate into clock, field and scattering specifications. Both are crossovers with a stated scale, and \(m^*\) is left as a measured output.

## Related entries

- [faraday-rotation](faraday-rotation.md) — off-resonant circular-index accumulator on the same \(eB/m\) scale
- [skin-effect](skin-effect.md) — in a metal the drive reaches only the skin layer
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — a different collective clock of the same carriers; it shifts the line in a sheet
- [Quantum Hall effect](quantum-hall-effect.md) — same high-\(\mu B\) two-dimensional hardware; different output
- [Semiconductor gap absorption](semiconductor-gap-absorption.md) — the gapped host whose band mass the line reads out

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [NIST, CODATA 2022 recommended values: electron mass](https://physics.nist.gov/cgi-bin/cuu/Value?me) | full-text | Electron mass 9.109 383 7139 × 10⁻³¹ kg; with the exact elementary charge it gives the free-electron cyclotron frequency. |
| S2 | [NIST, CODATA 2022 recommended values: electron gyromagnetic ratio in MHz/T](https://physics.nist.gov/cgi-bin/cuu/Value?gammaebar) | full-text | Spin-resonance value 28 024.951 MHz T⁻¹. |
| S3 | [Dresselhaus, Kip and Kittel, *Phys. Rev.* 98, 368 (1955)](https://doi.org/10.1103/PhysRev.98.368) | abstract | Cyclotron resonance in Si and Ge near 4 K with circularly polarized microwaves; longitudinal and transverse electron masses and spheroid orientations. |
| S4 | [Andreev, Muravev, Belyanin and Kukushkin, "Azbel'-Kaner-like cyclotron resonance in a two-dimensional electron system", arXiv:1709.00840](https://arxiv.org/abs/1709.00840) | full-text | Cyclotron frequency formula; GaAs mass 0.067; geometry and polarization in semiconductors; skin-layer (Azbel'–Kaner) resonance in metals; shifted collective line in a sheet. |
| S5 | [Takeyama, "Bridging the gap between extreme environments and precision measurements: recent progress in megagauss physics", arXiv:2605.11379](https://arxiv.org/abs/2605.11379) | full-text | Review: resolved line needs mobility × field ≫ 1, equivalently ω_c τ ≫ 1; lines resolved above 100 T at 100 cm²/(V s), one at 295 K. |
