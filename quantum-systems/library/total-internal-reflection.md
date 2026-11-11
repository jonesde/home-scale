---
id: total-internal-reflection
title: Total Internal Reflection (Index/Geometry Gate)
status: formal
family: collective-field-response
constraints:
  - spatial-buffer
confidence_data: high
confidence_mapping: high
review_depth: light
related:
  - refraction-dielectric
  - reflection
  - surface-plasmon-resonance
  - plasma-frequency-cutoff
updated: 2026-11-11
---

# Total Internal Reflection (Index/Geometry Gate)

### 4.1 Effect Name

Total internal reflection (index / geometry gate)

### 4.2 Macroscopic Observation

A light beam travelling in glass or water and striking an interface with air is entirely returned once the angle of incidence exceeds a critical value. Below that angle a transmitted beam appears in the air and the reflection is partial. Binocular prisms and the core/cladding boundary of an optical fibre operate in the totally reflecting regime. If a second piece of glass is brought within a few wavelengths of the interface, light crosses the gap (frustrated total internal reflection) and the reflection is no longer total.

### 4.3 Established Quantitative Boundaries

- **Convention.** Critical angle for incidence from medium 1 onto medium 2 (Snell's law at a refraction angle of 90°) [S1]:

  \[
  \theta_c = \arcsin(n_2/n_1),\qquad n_1 > n_2
  \]

  Total internal reflection occurs only when the second medium has the lower index [S1].
- **Computed here.** Against air: water (\(n = 1.333\)) 48.6°, glass (\(n = 1.50\)) 41.8°, polystyrene (\(n = 1.49\)) 42.2°, diamond (\(n = 2.42\)) 24.4°. The water, polystyrene and diamond angles match the textbook's [S1]; the glass angle matches [S2]. Flint glass to crown glass is 66.3° [S1].
- **Model (Fresnel, lossless plane wave).** For \(\theta > \theta_c\) both reflection coefficients have magnitude 1 and carry a polarization-dependent phase [S2]. The field on the low-index side is evanescent, with amplitude falling by \(e\) over

  \[
  d = \frac{1}{\kappa} = \frac{\lambda_0}{2\pi\sqrt{n_1^2\sin^2\theta - n_2^2}}
  \]

  which grows without limit as \(\theta \to \theta_c\) [S2].
- **Computed here.** For glass/air (\(n_1 = 1.50\)): \(d = 0.19\,\lambda_0\) at 60°, \(0.45\,\lambda_0\) at 45° (285 nm at 633 nm) and \(1.85\,\lambda_0\) at 42°, which is 0.2° above \(\theta_c\).
- **Measured.** Frustrated total internal reflection: a third medium brought within a few wavelengths of the surface receives a transmitted wave, and transmission rises as the gap narrows [S2]. The dependence on gap is continuous.
- **Measured.** A beam of finite width is displaced laterally on reflection (Goos–Hänchen shift) [S2].
- **Measured.** Optical-fibre cladding has a lower index than the core and prevents light passing between fibres in a bundle [S1].

**Data confidence:** High — the critical angle follows from measured indices and the evanescent tail and frustrated reflection are standard. The decay-length formula, the unit-magnitude statement and the frustrated-reflection behaviour were read on a tertiary page [S2]; no measured transmission-against-gap curve was opened. The first version's clause on X-ray total external reflection is withdrawn: no opened source.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Snell's law, \(n_1\sin\theta_1 = n_2\sin\theta_2\), gives \(\theta_2 \to 90^\circ\) at \(\theta_1 = \theta_c\). For \(\theta_1 > \theta_c\) the transmitted wavevector component normal to the interface is imaginary and equal to \(\kappa\) above.
- Intensity in the tail falls as \(e^{-2\kappa z}\). For a gap much wider than \(1/\kappa\), transmission across it falls roughly as \(e^{-2\kappa g}\) with gap width \(g\).
- The time-averaged energy flux through the interface is zero in the lossless case. Energy still occupies the evanescent volume.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** An interface between two polarizable populations with \(n_1 > n_2\): the bound-charge machines of [refraction-dielectric](refraction-dielectric.md), not a new species. On the far side the evanescent field occupies a buffer of depth \(1/\kappa\), from about \(0.2\,\lambda_0\) well above \(\theta_c\) to several wavelengths close to it. A third medium inside that buffer takes light out. The incident beam must have its angular content above \(\theta_c\).

- **Clock rate / latency.** The optical period. The clock is not the load-bearing specification: the gate works wherever the two media are transparent and \(n_1 > n_2\), and it fails where the index contrast does, which is a failure of the refraction machines.

- **Energy barriers or thresholds.** None. A driven boundary response, not a latch. "Barrier" for the low-index gap in frustrated reflection is a wave-tunnelling metaphor and is not an energy-barrier tag.

- **Dominant failure modes.**
  - **Threshold** — geometry: \(\theta < \theta_c\) gives a propagating transmitted beam and \(R < 1\). The angle is sharp for a plane wave in lossless media; a finite beam has an angular spread across it.
  - **Threshold** — contrast: \(n_1 \le n_2\), no critical angle exists.
  - **Crossover** — spatial buffer: a third body in the tail. Transmission rises continuously as the gap narrows, roughly as \(e^{-2\kappa g}\), with \(1/\kappa\) between \(0.2\,\lambda_0\) and a few \(\lambda_0\).
  - **Crossover** — dissipation: absorption in either medium gives \(|r| < 1\) above \(\theta_c\); no measured scale filed.

- **Emergent constant or stable output.** Unit reflectance (lossless case) for all \(\theta > \theta_c\), with a non-propagating field in a wavelength-scale volume on the far side.

### 4.6 Internal Consistency Notes

Total internal reflection is not a new collective oscillator. It is a kinematic gate on the \(n_1, n_2\) produced by the refraction machines. Family membership is still collective-field-response: without those polarizable volumes there is no index contrast and no interface field. Two of the failure modes are sharp (a definite angle and the condition \(n_1 > n_2\)), which is why the mapping rates higher than the parent refraction entry.

Sourcing changed two things; no number changed. Frustrated reflection is a crossover in gap width, not a cut at a fixed distance, and the buffer depth is not one length: it diverges at \(\theta_c\). The X-ray clause was dropped for lack of an opened source.

The six allowed tags have no slot for angle or index contrast. `spatial-buffer` covers the interface, the evanescent tail and frustrated reflection. It does not name the critical-angle gate. That is a limitation of the tag list.

[Surface plasmon resonance](surface-plasmon-resonance.md) uses a prism's evanescent field as a coupler: shared hardware, different failure conditions. Metal [reflection](reflection.md) gives high \(R\) with no critical angle.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(\theta < \theta_c\) and \(n_1 \le n_2\) are sharp conditions that translate into a geometry / contrast gate, and the evanescent tail is a spatial buffer with a computed depth. Starving that buffer is a crossover.

## Related entries

- [refraction-dielectric](refraction-dielectric.md) — the \(n_1, n_2\) this gate acts on
- [reflection](reflection.md) — high \(R\) from a metal electron gas, without a critical-angle condition
- [surface-plasmon-resonance](surface-plasmon-resonance.md) — uses the evanescent field of a prism as the coupler
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — a metal goes from reflecting to transmitting with frequency, not angle

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [OpenStax, *University Physics* vol. 3, §1.4 Total Internal Reflection](https://openstax.org/books/university-physics-volume-3/pages/1-4-total-internal-reflection) | full-text | Open textbook: critical-angle formula and its condition; 48.6° water, 24.4° diamond, 42.2° polystyrene (n = 1.49), 66.3° flint to crown; fibre cladding. |
| S2 | [Wikipedia, "Total internal reflection"](https://en.wikipedia.org/wiki/Total_internal_reflection) | full-text | Tertiary (first 100,000 characters read): penetration-depth formula and its divergence at the critical angle; unit-magnitude reflection coefficients with phase; frustrated reflection within a few wavelengths, rising as the gap narrows; Goos–Hänchen shift; glass/air about 41.8°. |
