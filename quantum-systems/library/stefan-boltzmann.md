---
id: stefan-boltzmann
title: Stefan–Boltzmann Law (Integrated Thermal Radiance)
status: formal
family: ensemble-averages
constraints:
  - thermal
  - spatial-buffer
confidence_data: high
confidence_mapping: medium
related:
  - blackbody-spectrum
  - thermal-equilibrium-temperature
  - reflection
  - work-function-thermionic
  - photoelectric-threshold
updated: 2026-08-17
---

# Stefan–Boltzmann Law (Integrated Thermal Radiance)

### 4.1 Effect Name

Stefan–Boltzmann law (integrated thermal radiance)

### 4.2 Macroscopic Observation

A hot black surface radiates a net power per unit area that rises steeply with the thermometer reading. Doubling \(T\) multiplies the exitance by sixteen. The same \(T^{4}\) envelope is recovered from independent black surfaces (soot, a cavity port, a black-coated radiator) once the geometry is close to a hemisphere of collected flux. A polished metal at the same \(T\) radiates much less. A surface that is grey (\(\varepsilon\) constant, less than one) still follows \(T^{4}\) with a reduced prefactor; a selective surface does not. As \(T\to 0\) the radiated power vanishes into the instrument floor.

### 4.3 Established Quantitative Boundaries

- Black-body hemispherical exitance:

  \[
  j = \varepsilon\sigma T^{4}
  \]

  with \(\varepsilon = 1\) for a black surface and

  \[
  \sigma = 5.670374\times 10^{-8}\,\mathrm{W\,m^{-2}\,K^{-4}}
  \]

  (\(\sigma\) is fixed by the defined constants \(h\), \(k\), and \(c\)). At \(300\,\mathrm{K}\) a black surface radiates \(\sigma T^{4}\approx 459\,\mathrm{W\,m^{-2}}\).
- Kirchhoff’s relation: at each frequency the emissivity equals the absorptivity, \(\varepsilon(\nu)=\alpha(\nu)\). A good mirror is a poor emitter in the same band.
- Real materials: \(\varepsilon=\varepsilon(\nu,T,\theta)\). Metals in the infrared can sit at \(\varepsilon\) of a few percent; carbon-black and cavity ports approach 1. Only the black (or grey, constant-\(\varepsilon\)) case produces a clean \(\sigma T^{4}\) reading.
- Finite-size / diffraction corrections appear when the radiating object is not large compared with the wavelengths that carry the energy (\(\lambda_{\max}T\approx 2898\,\mu\mathrm{m\cdot K}\); \(\sim 10\,\mu\mathrm{m}\) at \(300\,\mathrm{K}\)). There is no single universal size cliff; the required area tracks \(T\).
- Net exchange between two black surfaces is \(\sigma(T_{1}^{4}-T_{2}^{4})\). A body in a room radiates against a nonzero background; the \(T^{4}\) law is still the envelope for each side.

**Data confidence:** High — \(\sigma\) is defined; the \(T^{4}\) envelope, Kirchhoff’s relation, and the collapse toward \(\varepsilon<1\) or toward a selective spectrum are standard radiometric facts. Material \(\varepsilon(\nu)\) tables are high as a class and medium for any one finish.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- \(\sigma\) as the frequency integral of the [Planck](blackbody-spectrum.md) function:

  \[
  \sigma = \frac{2\pi^{5}k^{4}}{15 c^{2}h^{3}}
  \]

- Grey-body envelope: \(j=\varepsilon\sigma T^{4}\) with \(\varepsilon\) independent of frequency. This is an approximation, not a second independent law.
- Spectral exitance follows \(\varepsilon(\nu)B_{\nu}(T)\). If \(\varepsilon(\nu)\) varies across the band that carries the energy, the integrated power is not \(\sigma T^{4}\).
- Wien’s displacement law locates the band that dominates the integral. That band, not the entire electromagnetic axis, is what a finite object must be large compared with.

These relations describe the integrated output of a thermal electromagnetic population. They do not derive \(k\) or \(h\), and they do not fix a universal radiating area.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The same statistical electromagnetic population as the [blackbody spectrum](blackbody-spectrum.md), now read as a single integrated current. Two buffers, neither a universal number:
  1. The surface must present \(\varepsilon\approx 1\) across the Wien band (a cavity port, a black coating) or the output is not \(\sigma T^{4}\).
  2. The radiating area must be large enough, and the object large compared with \(\lambda_{\max}(T)\), that the mode average has already been taken. Small or few-mode objects fall off the \(T^{4}\) envelope for the same reason a sparse cavity falls off the Planck curve.

- **Clock rate / latency.** No separate clock beyond the wall-equilibration window and the spectral content already fixed by \(kT/h\). The \(T^{4}\) law is a time-averaged power. A detector faster than the wall exchange, or a surface whose \(T\) is not itself stable, does not report \(\sigma T^{4}\).

- **Energy barriers or thresholds.** None holding a latched state. A high-[reflectivity](reflection.md) metal is a resource failure of the black boundary condition (\(\varepsilon\) collapsed), not a stored configuration.

- **Dominant failure modes.**
  - Spectral: surface not black (\(\varepsilon(\nu)\neq 1\) across the Wien band) → reduced or non-\(T^{4}\) output. Same physical surface can be nearly black in the thermal infrared and reflective in the visible.
  - Geometric: object or cavity not large compared with \(\lambda_{\max}(T)\), or modes under-populated → the integral of a non-Planck spectrum is not \(\sigma T^{4}\).
  - Thermal: \(T\to 0\) → \(j\to 0\), lost in the instrument floor. Or the wall population has no stable \(T\).
  - Undefined \(T\): the same collapse as the temperature entry, inherited by every thermal-radiation readout.

- **Emergent constant or stable output.** The \(T^{4}\) exitance \(j=\varepsilon\sigma T^{4}\), with \(\sigma\) the integrated constant of the Planck curve, as the power-meter reading of a black thermal surface.

### 4.6 Internal Consistency Notes

This entry is the integral of [blackbody spectrum](blackbody-spectrum.md) and must share that entry’s buffer, clock, and failure class. It does. The extra collapse — surface not black — is a boundary-condition failure of the same population, not a new machine. [Reflection](reflection.md) and [plasma-frequency cutoff](plasma-frequency-cutoff.md) explain why a metal wall fails that boundary condition; they do not replace this integral.

\(\sigma\) is a combination of defined constants. Extracting \(\sigma\) as if it were an independent machine constant would double-count \(k\) and \(h\). The mapping’s job is the \(T^{4}\) envelope and its failures, not a re-derivation of the prefactor.

Finite-size corrections are real and measured (small particles, near-field radiative transfer, micromachined cavities). They confirm that area and \(\lambda_{\max}\) are the spatial resources. They do not yield a single universal area, and the mapping should not invent one.

Thermionic emission from the same hot surface is a charged-particle gate ([work-function / thermionic](work-function-thermionic.md)), not a photon-current integral. The two outputs can coexist on one filament; they are not the same artifact.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the \(T^{4}\) law, the defined \(\sigma\), and the non-black / small-object failures are sharp; the QSA translation is the integrated form of the spectrum entry and inherits that entry’s missing universal-volume number.

## Related entries

- [Blackbody spectrum](blackbody-spectrum.md) — the curve whose integral is this law
- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the wall average that \(T^{4}\) reports
- [Reflection](reflection.md) — high-\(R\) metal wall, low \(\varepsilon\), failed black boundary condition
- [Work function / thermionic emission](work-function-thermionic.md) — charged-particle output of a hot surface; contrast case
- [Photoelectric threshold](photoelectric-threshold.md) — single-electron optical gate on the same metals
