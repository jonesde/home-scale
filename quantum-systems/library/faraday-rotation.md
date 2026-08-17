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
related:
  - cyclotron-resonance
  - refraction-dielectric
  - plasma-frequency-cutoff
  - curie-paramagnetism
updated: 2026-08-17
---

# Faraday Rotation (Magneto-Optical Path Accumulator)

### 4.1 Effect Name

Faraday rotation (magneto-optical path accumulator)

### 4.2 Macroscopic Observation

The plane of linear polarization rotates as light travels through a medium along a magnetic field. The sense of rotation is locked to \(\mathbf{B}\), not to the direction of travel: a round trip adds, rather than cancels. Terbium gallium garnet (TGG) rotators and silica-fibre current sensors are laboratory-scale instances. Polarized pulsar and synchrotron radiation traversing the interstellar plasma shows a rotation that grows as \(\lambda^2\). With \(B\to 0\), or with a path too short for the medium’s Verdet constant, the rotation is gone.

### 4.3 Established Quantitative Boundaries

- Linear regime (ordinary laboratory fields and transparent media):

  \[
  \theta = VBL
  \]

  \(V\) is the measured Verdet constant of the medium at that wavelength and temperature.

- Material classes, not a single number:
  - Paramagnetic Tb-based crystals (TGG): \(\lvert V\rvert\) of order \(10^{2}\,\mathrm{rad\,T^{-1}\,m^{-1}}\) in the red (published values near \(-130\,\mathrm{rad\,T^{-1}\,m^{-1}}\) at \(632\)–\(633\,\mathrm{nm}\)), falling to about \(40\,\mathrm{rad\,T^{-1}\,m^{-1}}\) at \(1064\,\mathrm{nm}\). \(V(T)\) is strongly temperature-dependent.
  - Diamagnetic fused silica / ordinary fibre: \(V\approx 3\)–\(4\,\mathrm{rad\,T^{-1}\,m^{-1}}\) near \(633\,\mathrm{nm}\), smaller in the infrared. Weak \(T\) dependence.
- There is no universal \(L\) or \(B\) cliff. The rotation falls below a given polarimetric floor when the product \(VBL\) does. Absorption sets an independent upper bound on \(L\).
- Magnetized plasma / interstellar case (conventional observational form):

  \[
  \theta = \mathrm{RM}\,\lambda^2,\qquad
  \mathrm{RM} = 0.81\int n_e B_\parallel\,\mathrm{d}l
  \]

  with \(n_e\) in \(\mathrm{cm^{-3}}\), \(B_\parallel\) in \(\mu\mathrm{G}\), \(\mathrm{d}l\) in \(\mathrm{pc}\), \(\mathrm{RM}\) in \(\mathrm{rad\,m^{-2}}\). Dilute plasma plus a long path is the same product budget as \(VBL\), written in radio-astronomy units.
- Non-reciprocity is part of the data: two passes through the same \(B\) double \(\theta\). That is the isolator observation, recorded as an operating fact.

**Data confidence:** High — \(\theta=VBL\), the TGG vs silica class of \(V\), \(\lambda^{-2}\) interstellar Faraday, and non-reciprocity are standard and multiply reproduced. Any one crystal’s \(V(\lambda,T)\) is a measured curve (high as a class, medium for an uncited grade).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Circular birefringence:

  \[
  \theta = \frac{\pi}{\lambda}(n_- - n_+)L
  \]

  \(V\) packages \((n_--n_+)/B\). The split tracks a cyclotron / Zeeman-scale difference between the two circular indices.

- Diamagnetic (Becquerel) working relation: \(V \propto \lambda\,\mathrm{d}n/\mathrm{d}\lambda\). Paramagnetic terms add a population-weighted magnetic moment. Both are descriptive accounts of measured \(V\), not node derivations.
- Cold-plasma Faraday (high-frequency, \(\omega\gg\omega_c,\omega_p\)): \(\theta\propto n_e B_\parallel L/\omega^2\), the origin of the \(\mathrm{RM}\,\lambda^2\) form above.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A path \(L\) through a magneto-optically active population — bound charges with a magnetic splitting, or a magnetized plasma. The buffer is the *path*, not a film thickness. TGG at tesla-scale \(B\) accumulates a detectable \(\theta\) in centimetres; silica needs a much longer fibre; the interstellar case uses parsecs of dilute plasma. There is no analogue of the 10–20 nm mirror threshold.

- **Clock rate / latency.** Optical (or radio) carrier frequency. The circular-index split is a cyclotron / Zeeman-scale perturbation of the same polarization response written under [refraction-dielectric](refraction-dielectric.md). \(V(\lambda)\) is that dispersion. Drive near a strong electronic or cyclotron resonance changes the regime; the ordinary Verdet law is the off-resonant accumulator.

- **Energy barriers or thresholds.** No latch. \(B\) is a load-bearing resource, not a gate with a finite onset: \(\theta\propto B\) through zero. Tagging `field-threshold` here marks that resource, not a step-function threshold.

- **Dominant failure modes.**
  - Field: \(B\to 0\) → \(\theta\to 0\).
  - Spatial: \(L\) below the \(VBL\) detection budget → no measurable rotation.
  - Spectral / material: \(V\to 0\) (wrong window; or, for paramagnetic media, loss of the magnetic population with \(T\)).
  - Opacity: the path becomes absorbing before \(\theta\) is usable.

- **Emergent constant or stable output.** A rotation angle linear in \(B\) and \(L\), non-reciprocal, with a material- and frequency-specific \(V\) (or an \(\mathrm{RM}\) in the plasma case).

### 4.6 Internal Consistency Notes

The mapping is a product budget, not a hard machine death. A 5–10 nm metal film either is or is not a mirror; a Faraday path that is slightly short is just a smaller angle. That is why the mapping is not rated high, even though the resources (path, field, magneto-optical population) are unambiguous.

[Cyclotron resonance](cyclotron-resonance.md) is the resonant cousin: absorption when \(\omega=\omega_c\). Faraday is the off-resonant, cumulative phase between the two circular modes. They share the \(eB/m\) scale and must not be filed as one artifact. The interstellar plasma form also sits next to `plasma-frequency-cutoff`: Faraday in a magnetized plasma is written in the same \(\omega_p,\omega_c\) language, far below cutoff.

QSA *takes* \(V\) (or the 0.81 prefactor) as measured. It does not derive TGG’s \(10^{2}\,\mathrm{rad\,T^{-1}\,m^{-1}}\) from node rules. Paramagnetic \(V(T)\) touches `curie-paramagnetism` but the Faraday output is a path integral, not a susceptibility reading.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — path buffer and field resource are correctly identified and the Verdet / RM data are solid, but the collapse is a detection budget (\(VBL\) too small) rather than a sharp buffer/clock/barrier cliff.

## Related entries

- [cyclotron-resonance](cyclotron-resonance.md) — resonant absorption at \(\omega_c\); Faraday is the off-resonant circular-index split
- [refraction-dielectric](refraction-dielectric.md) — the underlying polarizable medium; Faraday is magnetically split \(n_\pm\)
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — magnetized-plasma Faraday is written in the same \(\omega_p,\omega_c\) language
- [Curie paramagnetism](curie-paramagnetism.md) — unlocked-moment ensemble that feeds paramagnetic \(V(T)\)
