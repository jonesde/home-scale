---
id: faraday-rotation
title: Faraday Rotation (Magneto-Optical Path Accumulator)
status: formal
family: collective-field-response
constraints:
  - spatial-buffer
  - field-threshold
  - clock-latency
confidence_data: high
confidence_mapping: medium
review_depth: light
related:
  - cyclotron-resonance
  - refraction-dielectric
  - plasma-frequency-cutoff
  - curie-paramagnetism
  - reflection
updated: 2026-11-11
---

# Faraday Rotation (Magneto-Optical Path Accumulator)

### 4.1 Effect Name

Faraday rotation (magneto-optical path accumulator)

### 4.2 Macroscopic Observation

The plane of linear polarization rotates as light travels through a medium along a magnetic field. The sense of rotation is fixed by \(\mathbf{B}\), not by the direction of travel, so a return pass adds to the rotation. Terbium gallium garnet (TGG) rotators and silica-fibre current sensors are laboratory instances. Polarized pulsar radiation crossing the interstellar plasma and the ionosphere shows a rotation that grows as \(\lambda^2\). With \(B \to 0\) the rotation is gone.

### 4.3 Established Quantitative Boundaries

- **Convention.** Linear regime: \(\theta = VBL\), with \(B\) the flux density along the propagation direction and \(V\) the Verdet constant of the medium at that wavelength and temperature [S1].
- **Measured.** TGG (paramagnetic): \(V = -131\) to \(-134\,\mathrm{rad\,T^{-1}\,m^{-1}}\) at 632 nm and \(-38\,\mathrm{rad\,T^{-1}\,m^{-1}}\) at 1064 nm [S1][S2]. \(V\) increases substantially toward cryogenic temperatures [S2].
- **Measured.** Fused silica (diamagnetic): \(3.7\,\mathrm{rad\,T^{-1}\,m^{-1}}\) at 633 nm [S3].
- **Computed here.** Path for a 45° rotation at 1 T: 6.0 mm of TGG at 632 nm, 2.1 cm of TGG at 1064 nm, 21 cm of silica at 633 nm.
- **Measured.** Non-reciprocity: a double pass through the medium doubles the rotation; this is the basis of optical isolators, which transmit light in one direction only [S1].
- **Model (cold magnetized plasma).** Plasma form used in radio astronomy [S4]:

  \[
  \psi = \psi_0 + \mathrm{RM}\,\lambda^2,\qquad
  \mathrm{RM} = 0.81\int n_e B_\parallel\,\mathrm{d}l
  \]

  with \(n_e\) in \(\mathrm{cm^{-3}}\), \(B_\parallel\) in \(\mu\mathrm{G}\), \(\mathrm{d}l\) in pc and RM in \(\mathrm{rad\,m^{-2}}\). In SI units the prefactor is \(2.62\times10^{-13}\,\mathrm{T^{-1}}\) [S1].
- **Computed here.** \(e^3/(8\pi^2\varepsilon_0 m_e^2 c^3) = 2.63\times10^{-13}\,\mathrm{T^{-1}}\), which is 0.81 in the radio-astronomy units.
- **Measured.** Pulsar Faraday rotation is measured at about 100–200 MHz and follows the \(\lambda^2\) law. The ionosphere contributes an RM of order 1–4 \(\mathrm{rad\,m^{-2}}\), varying by up to 80 % during a day [S4].
- **Computed here.** At 150 MHz (\(\lambda^2 = 4.0\,\mathrm{m^2}\)) an RM of 1–4 \(\mathrm{rad\,m^{-2}}\) is a rotation of 4–16 rad. The observing band is 11 to 200 times the ionospheric plasma frequency of 1 to 9 MHz (sourced in [plasma-frequency-cutoff](plasma-frequency-cutoff.md)). Doubling the frequency cuts the rotation by a factor of 4.

**Data confidence:** High as a class — the linear law, the \(\lambda^2\) plasma law and non-reciprocity are standard. The TGG values come from two tertiary pages and the silica value from one secondary citation; the primary papers were not opened. Silica's infrared value and temperature dependence, given in the first version, had no opened source and were dropped.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Circular birefringence:

  \[
  \theta = \frac{\pi}{\lambda}(n_- - n_+)L
  \]

  \(V\) packages \((n_- - n_+)/B\).
- Diamagnetic (Becquerel) working relation \(V \propto \lambda\,\mathrm{d}n/\mathrm{d}\lambda\); paramagnetic media add a population-weighted term. No source opened for either form.
- Cold plasma at \(\omega \gg \omega_c, \omega_p\): \(\theta \propto n_e B_\parallel L/\omega^2\), the origin of the \(\mathrm{RM}\,\lambda^2\) form [S4].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A path \(L\) through a magneto-optically active population: bound charges with a magnetic splitting, or a magnetized plasma. The buffer is the path. At 1 T a 45° rotation takes millimetres to centimetres of TGG and about 21 cm of silica; the interstellar case uses parsecs of dilute plasma. The rotation is proportional to \(L\) and has no minimum length.

- **Clock rate / latency.** The optical or radio carrier. The circular-index split is a magnetic perturbation of the polarization response filed under [refraction-dielectric](refraction-dielectric.md), and \(V(\lambda)\) is its dispersion. In a plasma the carrier must be above the plasma frequency for the wave to propagate at all; above it the rotation falls as \(1/\omega^2\).

- **Energy barriers or thresholds.** No latch. \(B\) is a resource with no finite onset: \(\theta \propto B\) through zero. The `field-threshold` tag marks that resource.

- **Dominant failure modes.**
  - **Crossover** — field: \(\theta \propto B\), reaching zero at \(B = 0\).
  - **Crossover** — path: \(\theta \propto L\); the rotation drops below a polarimeter's floor when \(VBL\) does.
  - **Crossover** — carrier frequency, plasma: \(\theta \propto \lambda^2\). The rotation fades by a factor of 4 per doubling of frequency and is still measured at 11–200 times the plasma frequency. It does not stop at the plasma edge.
  - **Threshold** — carrier below the plasma frequency (collisionless model): no propagating wave, so no path. Owned by [plasma-frequency-cutoff](plasma-frequency-cutoff.md).
  - **Crossover** — thermal, paramagnetic media: \(V\) falls as temperature rises; functional form not filed.
  - **Crossover** — opacity: absorption along the path limits usable \(L\); no scale filed.

- **Emergent constant or stable output.** A rotation angle linear in \(B\) and \(L\), non-reciprocal, with a material- and frequency-specific \(V\), or an RM in the plasma case.

### 4.6 Internal Consistency Notes

The mapping is a product budget. Every dependence filed is continuous (linear in \(B\) and \(L\), quadratic in \(\lambda\) for a plasma), and a path that is slightly short gives a smaller angle. That is why the mapping is not rated high although the resources (path, field, magneto-optical population) are unambiguous.

Sourcing changed one statement of fact and removed two comparisons. The first version placed plasma Faraday rotation "far below cutoff"; it is measured far above the plasma frequency, and below that frequency there is no transmitted wave to rotate. The comparisons with a thickness threshold for metal mirrors are removed, since [reflection](reflection.md) files no such threshold. The TGG and silica numbers did not change; silica's infrared value was dropped.

[Cyclotron resonance](cyclotron-resonance.md) is the resonant relative: absorption at \(\omega = \omega_c\). Faraday rotation is the off-resonant, cumulative phase between the two circular modes. They share the \(eB/m\) scale and are separate entries.

Magneto-optical Kerr rotation is the same population read in reflection. It is a clause on this file and on [reflection](reflection.md), not a second catalog row.

The mapping takes \(V\) as measured and does not derive it. The 0.81 prefactor is different: it follows from \(e\), \(m_e\), \(c\) and \(\varepsilon_0\) in the cold-plasma model. Paramagnetic \(V(T)\) touches `curie-paramagnetism`, but the output is a path integral, not a susceptibility reading.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the path buffer and field resource are identified and the Verdet and RM data are standard, but every filed dependence is a crossover and the only threshold belongs to another entry.

## Related entries

- [cyclotron-resonance](cyclotron-resonance.md) — resonant absorption at \(\omega_c\); Faraday rotation is the off-resonant circular-index split
- [refraction-dielectric](refraction-dielectric.md) — the underlying polarizable medium
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — plasma Faraday rotation is observed above this edge and fades as \(\lambda^2\)
- [Curie paramagnetism](curie-paramagnetism.md) — the moment ensemble behind paramagnetic \(V(T)\)
- [reflection](reflection.md) — Kerr rotation is the reflection-side counterpart on a magnetized metal face

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Wikipedia, "Faraday effect"](https://en.wikipedia.org/wiki/Faraday_effect) | full-text | Tertiary: rotation = V B d; double pass doubles the rotation; isolators; TGG about −134 rad/(T m) at 632 nm; SI plasma prefactor 2.62 × 10⁻¹³ T⁻¹; ionospheric rotation proportional to wavelength squared. |
| S2 | [Wikipedia, "Terbium gallium garnet"](https://en.wikipedia.org/wiki/Terbium_gallium_garnet) | full-text | Tertiary, citing Vojna et al. (2019, 2020) and Majeed et al. (2013): −131 rad/(T m) at 632 nm, −38 at 1064 nm; increase toward cryogenic temperatures. |
| S3 | [Hrabovsky et al., "Optical, magneto-optical properties and fiber-drawing ability of tellurite glasses in the TeO2–ZnO–BaO ternary system", arXiv:2308.01186](https://arxiv.org/abs/2308.01186) | full-text | Secondary (cites a fibre-optics textbook): fused silica 3.7 rad/(T m) at 633 nm. |
| S4 | [Porayko et al., "Testing the accuracy of the ionospheric Faraday rotation corrections through LOFAR observations of bright northern pulsars", arXiv:1812.01463](https://arxiv.org/abs/1812.01463) | full-text | Wavelength-squared law and RM = 0.81 ∫ n B dl with units; observations at about 100–200 MHz; ionospheric RM of order 1–4 rad m⁻², varying up to 80 % in a day. Preprint. |
