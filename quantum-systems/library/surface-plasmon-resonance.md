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
related:
  - reflection
  - plasma-frequency-cutoff
  - skin-effect
  - total-internal-reflection
  - refraction-dielectric
updated: 2026-08-17
---

# Surface Plasmon Resonance (Interface-Bound Collective Mode)

### 4.1 Effect Name

Surface plasmon resonance (interface-bound collective mode)

### 4.2 Macroscopic Observation

At a metal–dielectric interface, a narrow dip appears in reflected intensity as angle or wavelength is scanned, provided a coupler (prism or grating) is present. Gold and silver films in the visible are the ordinary laboratory cases. The dip walks when the refractive index of the medium against the metal changes. Light incident from free space on a flat metal surface does not produce the dip. If the film is far from the working thickness window, or the metal is a poor, highly damped conductor, the feature washes out.

### 4.3 Established Quantitative Boundaries

- A bound surface-plasmon polariton (SPP) at a single planar interface exists only while \(\operatorname{Re}\varepsilon_m < 0\) and \(\lvert\varepsilon_m\rvert > \varepsilon_d\) — i.e. below the metal’s screened plasma / interband edge, against a positive-index dielectric. Ag and Au in the visible are the standard pair (low damping relative to most other metals); Al is used further into the UV.
- The SPP wavevector lies outside the free-space (or dielectric) light line: \(k_{\mathrm{sp}} > n_d\,\omega/c\). A momentum-matching coupler is required. Textbook couplers: Kretschmann (prism / thin metal / dielectric), Otto (prism / gap / metal), and a grating on the metal. Without that match there is no resonance, however good the metal.
- Kretschmann film thickness sits in a *window* of tens of nanometres — commonly about \(40\)–\(50\,\mathrm{nm}\) of Au in the visible — thick enough that a bound interface mode exists, thin enough that the prism field still reaches the outer metal–dielectric face. The number is metal-, wavelength-, and coupler-dependent. It is not a universal 50 nm law.
- Field decay into the metal is of order the optical penetration depth (tens of nm; see [reflection](reflection.md)). Decay into the dielectric is longer, typically a fraction of a visible wavelength up to about one wavelength. Along the interface, a propagating SPP in good Ag in the red can run tens of micrometres; Au is shorter (more interband damping).
- Localized plasmon resonance of Au particles (the ruby-glass / colloid extinction near \(520\,\mathrm{nm}\) in water) is a related resonance of the same electron gas in a different geometry. It does not need a prism; it is not the planar Kretschmann dip.

**Data confidence:** High — SPP dispersion, the need for a coupler, Ag/Au as the visible metals, and a tens-of-nm Kretschmann window are standard, multiply reproduced facts. Any one film’s exact optimum thickness is medium (process, wavelength, indices).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Planar SPP dispersion (semi-infinite metal / dielectric):

  \[
  k_{\mathrm{sp}} = \frac{\omega}{c}\sqrt{\frac{\varepsilon_m\varepsilon_d}{\varepsilon_m+\varepsilon_d}}
  \]

  bound while \(\varepsilon_m+\varepsilon_d < 0\).

- Prism matching (Kretschmann / Otto): \(k_\parallel = n_p(\omega/c)\sin\theta\). Resonance is the crossing of that line with \(k_{\mathrm{sp}}(\omega)\).
- The laboratory readout is a minimum in \(R(\theta)\) or \(R(\lambda)\). Width tracks Im\(\varepsilon_m\) (damping \(\gamma\) in the Drude picture already written under [reflection](reflection.md)).
- Localized-particle resonance is a different electrostatic / Mie condition on \(\varepsilon_m(\omega)\), not the planar \(k_{\mathrm{sp}}\) formula.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Three nested spatial resources, all required:
  1. a metal–dielectric *interface* (the mode is not a bulk plasma oscillation);
  2. a metal thickness inside the coupler window (tens of nm in ordinary Kretschmann Au/Ag; not a single universal number);
  3. a continuous, not islanded, film so the in-plane mode can exist.

  The dielectric-side evanescent tail is an additional buffer of order a visible wavelength. A coupler (prism index plus angle, or a grating period) is part of the hardware even though it is not itself the electron gas.

- **Clock rate / latency.** Optical cycle. The metal electrons must follow at the SPP frequency, below the screened plasma / interband edge — the same femtosecond class as reflection. Drive above that edge unbinds the mode (\(\varepsilon_m+\varepsilon_d\) no longer negative).

- **Energy barriers or thresholds.** None. Driven collective resonance, not a latch.

- **Dominant failure modes.**
  - Momentum: no coupler, or \(\theta\) / grating period off the match → no dip.
  - Spatial: film thickness off the window; discontinuous morphology; missing metal–dielectric face.
  - Spectral: \(\omega\) too high for \(\varepsilon_m+\varepsilon_d < 0\), or sitting on a strong interband (Ag near-UV edge; Au already damped through much of the blue).
  - Dissipative: large \(\gamma\) → a shallow, washed-out feature rather than a sharp cliff.

- **Emergent constant or stable output.** A sharp angular or spectral absorption feature and a field bound to the interface, produced by synchronized oscillation of the metal electrons against the dielectric.

### 4.6 Internal Consistency Notes

The responding population is the same free-electron gas as [reflection](reflection.md) and [skin-effect](skin-effect.md). What is new is the *interface plus coupler*. Reflection needs a thick-enough continuous metal; SPR needs that metal *and* a second dielectric *and* extra in-plane momentum. The family assignment is still collective-field-response: starve the connected metal, raise the drive through the plasma / interband edge, or destroy the interface, and the macro feature dies.

The coupler is a genuine extra constraint that does not sit in the six allowed tags. It is a wavevector match, not a buffer, clock, barrier, lattice, field threshold, or thermal limit. Recording that as a gap in the tag set is more honest than inventing a seventh tag for one entry.

Do not treat “50 nm of gold” as the SPR equivalent of the 10–20 nm mirror threshold. The mirror threshold is an electromagnetic / morphological floor. The SPR thickness is a *window* whose location moves with \(\lambda\), \(\varepsilon_d\), and coupler. Localized particle resonance is the same family with a different spatial buffer (the particle), and must not be averaged into the planar-film number.

[Total internal reflection](total-internal-reflection.md) supplies the evanescent prism field that Kretschmann and Otto use as the coupler. That is shared hardware, not a shared collapse.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — interface, optical clock, and damping failures map cleanly onto the same electron-gas machine as reflection, but the load-bearing momentum match is outside the present constraint tags and the thickness window is not a single buffer number.

## Related entries

- [reflection](reflection.md) — same metal electrons; bulk mirror vs. interface-bound mode
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — unbinding when the drive outruns the screened plasma / interband edge
- [skin-effect](skin-effect.md) — decay into the metal is the optical end of screening
- [total-internal-reflection](total-internal-reflection.md) — prism TIR evanescent field is the usual coupler
- [refraction-dielectric](refraction-dielectric.md) — the dielectric half-space that sets \(\varepsilon_d\) and the light line
