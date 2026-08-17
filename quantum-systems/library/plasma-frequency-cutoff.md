---
id: plasma-frequency-cutoff
title: Plasma-Frequency Cutoff (Collective Clock Failure)
status: formal
family: collective-field-response
constraints:
  - clock-latency
  - spatial-buffer
confidence_data: high
confidence_mapping: high
related:
  - reflection
  - skin-effect
  - surface-plasmon-resonance
  - photoelectric-threshold
  - refraction-dielectric
updated: 2026-08-17
---

# Plasma-Frequency Cutoff (Collective Clock Failure)

### 4.1 Effect Name

Plasma-frequency cutoff (collective clock failure)

### 4.2 Macroscopic Observation

A metal that is a good visible-light reflector becomes transmitting once the drive frequency is raised through a material-specific edge in the ultraviolet (or, for the alkali metals, the near-UV). Thin alkali films that look metallic in the visible pass ultraviolet light. The same frequency gate appears in dilute plasmas: short-wave radio traverses the ionosphere; longer-wave radio is returned. No continuous external power is required beyond the incident field.

### 4.3 Established Quantitative Boundaries

- Free-electron / volume-plasmon energies (handbook and electron-energy-loss values): Al \(\hbar\omega_p \approx 15\,\mathrm{eV}\) (\(\lambda_p \approx 83\,\mathrm{nm}\)); Na \(\hbar\omega_p \approx 5.7\,\mathrm{eV}\) (\(\approx 220\,\mathrm{nm}\)); K \(\hbar\omega_p \approx 3.8\,\mathrm{eV}\) (\(\approx 330\,\mathrm{nm}\)). Ag’s free-electron \(\hbar\omega_p \approx 9\,\mathrm{eV}\), but the *optical* reflectivity edge sits near \(3.9\,\mathrm{eV}\) (\(\sim 320\,\mathrm{nm}\)) because d-band interband transitions shift \(\operatorname{Re}\varepsilon = 0\). Al and the alkalis track the free-electron edge; Ag does not.
- Corresponding plasma periods: \(\sim 0.3\,\mathrm{fs}\) (Al), \(\sim 0.5\,\mathrm{fs}\) (Ag free-electron), \(\sim 0.7\,\mathrm{fs}\) (Na). The Ag *optical* edge period is \(\sim 1\,\mathrm{fs}\).
- Carrier densities that feed those \(\omega_p\) values: Al \(\sim 1.8 \times 10^{29}\,\mathrm{m^{-3}}\); Ag \(\sim 5.9 \times 10^{28}\,\mathrm{m^{-3}}\); Na \(\sim 2.7 \times 10^{28}\,\mathrm{m^{-3}}\).
- Below the edge, bulk reflectivity is high (polished Al \(\sim 90\%\) in the visible; alkalis similarly metallic). Above it, the bulk supports propagating electromagnetic modes and a previously opaque film transmits. Residual absorption and surface scattering remain; the cliff is a loss of *metallic reflection*, not a claim of lossless vacuum-like transmission.
- Dilute-plasma instance of the same rule: ionospheric electron densities of order \(10^{11}\)–\(10^{12}\,\mathrm{m^{-3}}\) give plasma frequencies of a few to \(\sim 10\,\mathrm{MHz}\). HF broadcast below that ceiling is returned; higher frequencies pass. Same \(\omega > \omega_p\) gate, \(\sim 10^{17}\) lower density than a metal.
- The spatial buffer of the related [reflection](reflection.md) entry is still required: a discontinuous or \(\lesssim 5\)–\(10\,\mathrm{nm}\) film never forms the collective response, at any frequency. This entry owns the *spectral* collapse of an already-continuous metal.

**Data confidence:** High — plasma energies, optical edges, and the ionospheric HF cutoff are multiply reproduced handbook measurements. The exact numerical location of Ag’s interband-shifted edge is high as a class (\(\sim 3.9\,\mathrm{eV}\)) and medium at the \(0.1\,\mathrm{eV}\) digit (sample- and temperature-dependent).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Plasma frequency of a free-electron gas:

  \[
  \omega_p = \sqrt{\frac{ne^2}{\varepsilon_0 m}}
  \]

- Drude dielectric function:

  \[
  \varepsilon(\omega) = 1 - \frac{\omega_p^2}{\omega(\omega + i\gamma)}
  \]

  For small damping, \(\operatorname{Re}\varepsilon < 0\) when \(\omega < \omega_p\), and a vacuum–metal interface supports high reflectivity. For \(\omega > \omega_p\), \(\operatorname{Re}\varepsilon > 0\) and the bulk supports propagating waves.

- Normal-incidence Fresnel reflectance from complex index \(\tilde n = n + ik\):

  \[
  R = \left|\frac{1 - \tilde n}{1 + \tilde n}\right|^2
  \]

- In a dilute plasma the same \(\omega_p(n)\) is read as a radio cutoff frequency \(f_p = \omega_p/2\pi\).

Interband terms, omitted from the free-electron Drude function, shift the frequency at which \(\operatorname{Re}\varepsilon = 0\). That shift is the Ag optical-edge discrepancy.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Same connected metallic buffer as reflection: a continuous stack on the order of the optical penetration depth (about 10–20 nm in Ag or Al). The cutoff is a property of that already-provisioned population. The ionospheric instance shows the same clock rule operating in a much more dilute charged gas; the hardware there is a column of free electrons, not a crystal.

- **Clock rate / latency.** The load-bearing specification. The electron population must complete a collective screening cycle within one drive period. That cycle runs on the plasma-period timescale (a few \(10^{-16}\) to \(10^{-15}\,\mathrm{s}\) in metals; microseconds in the ionosphere). When the drive period drops below that cycle time, screening is not finished before the field has reversed and the reflected beam collapses.

- **Energy barriers or thresholds.** The operating condition is \(\omega < \omega_p\) (or, in Ag, \(\omega\) below the interband-shifted optical edge). There is no static latch; this is a driven collective response. \(\hbar\omega_p\) is an energy *scale* of the clock, not an activation barrier that holds a memory.

- **Dominant failure modes.**
  - Temporal / spectral: \(\omega > \omega_p\) (Al, alkalis) or \(\hbar\omega \gtrsim 3.9\,\mathrm{eV}\) (Ag optical edge) → the population cannot finish the screening cycle → transmission. This is the same machine as reflection, failed by clock rather than by thickness.
  - Spatial: continuous thickness \(\lesssim 5\)–\(10\,\mathrm{nm}\), or a discontinuous morphology → buffer starvation at any \(\omega\). Owned by [reflection](reflection.md).
  - Dissipative: large \(\gamma\) (dirty metal, liquid metal, high \(T\)) rounds the edge; \(R\) falls without a sharp cliff.

- **Emergent constant or stable output.** A material-typical plasma (or interband) edge: high \(R\) below, transmission above, produced with no continuous power input to the medium beyond the incident field.

### 4.6 Internal Consistency Notes

The mapping is the clock-failure twin of reflection and closes on the same node population, the same \(\omega_p\), and the same penetration-depth buffer. Changing only the drive frequency, at fixed thickness, takes the system across the collapse this entry owns. That is internally consistent.

Ag’s interband-shifted edge means the simplest “clock \(= \omega_p\)” statement is too coarse for silver in the near-UV. Al and the alkali metals are the clean test, which is why the UV transparency of Na and K is the historical demonstration. Visible-band mirrors still sit well below both the free-electron and the interband edges, so everyday reflection is not threatened.

A closed mapping would also say *why* the collective cycle time is \(2\pi/\omega_p\) from node rules alone. QSA currently *takes* the measured \(\omega_p(n)\) as the clock specification; it does not derive that period from a more primitive node update. That is the same class of gap recorded on reflection (taking \(\lambda/4\pi k\) as the buffer). It is a gap, not a contradiction.

Contrast case: [photoelectric-threshold](photoelectric-threshold.md) is a single-electron energy gate in the same metals (\(\varphi \sim 2\)–\(6\,\mathrm{eV}\)). Plasma cutoff is collective and is set by \(n\), not by the work function. The two thresholds can sit near each other in energy (Ag’s optical edge \(\sim 3.9\,\mathrm{eV}\), Ag \(\varphi \sim 4.3\)–\(4.7\,\mathrm{eV}\)) without being the same constraint.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the spectral boundary is a well-measured clock ceiling and translates directly onto the same collective screening population as reflection; remaining gaps are about deriving \(\omega_p\) from node rules and about Ag’s interband shift, not about the existence or location of the collapse.

## Related entries

- [Reflection (electron-cloud response)](reflection.md) — same collective screening, failed by thickness instead of drive frequency
- [Skin effect](skin-effect.md) — low-frequency limit of the same screening length
- [Surface plasmon resonance](surface-plasmon-resonance.md) — interface-bound collective mode of the same electron population
- [Photoelectric threshold](photoelectric-threshold.md) — single-electron energy gate in the same metals; contrast case
- [Refraction / dielectric polarization](refraction-dielectric.md) — bound-charge polarizability; the \(\varepsilon \to 1\) X-ray limit is the insulator analogue of \(\omega \gg \omega_p\)
