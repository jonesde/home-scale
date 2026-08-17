---
id: total-internal-reflection
title: Total Internal Reflection (Index/Geometry Gate)
status: formal
family: collective-field-response
constraints:
  - spatial-buffer
confidence_data: high
confidence_mapping: high
related:
  - refraction-dielectric
  - reflection
  - surface-plasmon-resonance
  - plasma-frequency-cutoff
updated: 2026-08-17
---

# Total Internal Reflection (Index/Geometry Gate)

### 4.1 Effect Name

Total internal reflection (index / geometry gate)

### 4.2 Macroscopic Observation

A light beam travelling in glass or water and striking an interface with air is entirely returned once the angle of incidence exceeds a critical value. Below that angle a transmitted beam appears in the air and the reflected intensity is only partial. Binocular prisms and the core/cladding boundary of an optical fibre operate in the totally reflecting regime. If a second piece of glass is brought within a fraction of a wavelength of the interface, light crosses the gap (frustrated TIR) and the “total” reflection is no longer total.

### 4.3 Established Quantitative Boundaries

- Critical angle, incidence from medium 1 onto medium 2:

  \[
  \theta_c = \arcsin(n_2/n_1),\qquad n_1 > n_2
  \]

  No real \(\theta_c\) exists if \(n_1\le n_2\).

- Textbook interfaces: crown glass / air (\(n_1\approx 1.50\)) \(\theta_c\approx 41.8^\circ\); water / air (\(n_1\approx 1.333\)) \(\theta_c\approx 48.6^\circ\); diamond / air (\(n_1\approx 2.42\)) \(\theta_c\approx 24.4^\circ\).
- For \(\theta>\theta_c\) there is no propagating transmitted wave. An evanescent field occupies the low-index side. Amplitude decay length:

  \[
  \frac{1}{\kappa} = \frac{\lambda_0}{2\pi\sqrt{n_1^2\sin^2\theta - n_2^2}}
  \]

  The length is of order \(\lambda/2\pi\) well above \(\theta_c\) and becomes several wavelengths as \(\theta\to\theta_c^+\). Intensity falls as \(e^{-2\kappa z}\).
- Frustrated TIR: a third medium placed inside that tail accepts a propagating wave. The isolation fails without any change in \(\theta\) or in \(n_1,n_2\).
- X-ray total *external* reflection at grazing incidence is the same kinematic gate with inverted contrast (\(n_{\mathrm{material}}=1-\delta<1=n_{\mathrm{vacuum}}\)). It is not a separate node species.

**Data confidence:** High — \(\theta_c\) from measured \(n\), the existence of the evanescent tail, and frustrated TIR as a gap-scale effect are textbook and multiply demonstrated. The exact numerical decay length is high once \(\theta\), \(\lambda\), and the two indices are specified.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Snell’s law, \(n_1\sin\theta_1=n_2\sin\theta_2\), gives \(\theta_2\to 90^\circ\) at \(\theta_1=\theta_c\). For \(\theta_1>\theta_c\), \(\sin\theta_2>1\): the transmitted wavevector component normal to the interface is imaginary and equal to \(\kappa\) above.
- Fresnel reflection coefficients have magnitude 1 (lossless media) for \(\theta>\theta_c\), with an angle- and polarization-dependent phase. A lateral Goos–Hänchen shift is the measured spatial counterpart of that phase; it is recorded as data, not used here as a mechanism claim.
- Time-averaged Poynting flux through the interface is zero in lossless TIR. Energy still occupies the evanescent volume.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** An interface between two polarizable populations with \(n_1>n_2\) — the same bound-charge machines as [refraction-dielectric](refraction-dielectric.md), not a new species. On the far side, the evanescent field occupies a buffer of order \(1/\kappa\) (a fraction of a wavelength to a few wavelengths). Starve that gap with a third medium and the total-reflection output fails. The incident beam must be a collective electromagnetic field whose angular content sits above \(\theta_c\).

- **Clock rate / latency.** The optical period. Clock is not the load-bearing collapse: TIR works across the transparency window of the two dielectrics. The effect dies when \(n(\omega)\) contrast disappears (X-ray \(\delta\to 0\), or an absorption band), which is a failure of the underlying refraction machines rather than of the geometric gate itself.

- **Energy barriers or thresholds.** None. Driven boundary response, not a latch. The word “barrier” for the low-index gap in frustrated TIR is a wave-tunneling metaphor; it is not an energy-barrier tag.

- **Dominant failure modes.**
  - Geometry: \(\theta<\theta_c\) → a propagating transmitted beam; \(R<1\).
  - Contrast: \(n_1\le n_2\) → the gate never exists.
  - Spatial buffer: a third body inside \(\sim 1/\kappa\) → frustrated TIR.
  - Dissipative: absorption in either medium → \(|r|<1\) even above \(\theta_c\).

- **Emergent constant or stable output.** Unit reflectance (lossless case) for all \(\theta>\theta_c\), together with a non-propagating field occupying a wavelength-scale volume on the far side of the interface.

### 4.6 Internal Consistency Notes

TIR is not a new collective oscillator. It is a kinematic gate on the \(n_1,n_2\) already produced by the refraction machines. Family membership is still collective-field-response: without those polarizable volumes there is no index contrast and no interface field. The *collapse* is sharper than refraction’s continuum — a definite angle and a binary \(n_1>n_2\) condition — which is why the mapping rates higher than the parent refraction entry.

The six allowed tags have no slot for “angle” or “index contrast.” `spatial-buffer` covers the interface, the evanescent tail, and frustrated-TIR starvation. It does not name the critical-angle gate. That is a limitation of the tag list, not a reason to invent a tag for one file.

[Surface plasmon resonance](surface-plasmon-resonance.md) uses the prism’s TIR evanescent field as a coupler. Shared hardware, different collapse: SPR dies when momentum, metal thickness, or \(\varepsilon_m+\varepsilon_d\) fail; TIR dies when \(\theta\) or \(n_1/n_2\) fail. Metal [reflection](reflection.md) can give high \(R\) without any critical angle; TIR is not that mirror.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(\theta<\theta_c\), \(n_1\le n_2\), and a third body inside \(1/\kappa\) are sharp, measured collapses that translate directly into a geometry / contrast gate and an evanescent spatial buffer.

## Related entries

- [refraction-dielectric](refraction-dielectric.md) — the \(n_1,n_2\) this gate acts on
- [reflection](reflection.md) — high \(R\) from a metal electron gas, without a critical-angle condition
- [surface-plasmon-resonance](surface-plasmon-resonance.md) — uses the TIR evanescent field of a prism as the coupler
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — a metal can go from reflecting to transmitting by clock failure, not by angle
