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
related:
  - faraday-rotation
  - skin-effect
  - plasma-frequency-cutoff
  - quantum-hall-effect
  - semiconductor-gap-absorption
updated: 2026-08-17
---

# Cyclotron Resonance (Orbital Clock Match)

### 4.1 Effect Name

Cyclotron resonance (orbital clock match)

### 4.2 Macroscopic Observation

A semiconductor or metal in a magnetic field absorbs a radio, microwave, or far-infrared drive when the drive frequency matches the cyclotron frequency of the carriers. The resonance field at a known frequency is read as an effective mass. Off resonance the absorption falls. In a dirty or warm sample the line is absent even at the nominal matching field. No continuous power is required of the sample beyond the probing field.

### 4.3 Established Quantitative Boundaries

- Cyclotron frequency:

  \[
  \omega_c = \frac{eB}{m^*},\qquad
  f_c = \frac{eB}{2\pi m^*}
  \]

  Free electrons: \(f_c \approx 28.0\,\mathrm{GHz\,T^{-1}}\). That number coincides with the \(g=2\) spin-resonance frequency; the degree of freedom is different (orbital vs spin) and the two lines must not be treated as one measurement.
- Band masses are the usual laboratory output. GaAs conduction electrons: \(m^*\approx 0.067\,m_e\), so \(f_c\approx 0.42\,\mathrm{THz\,T^{-1}}\). Si and Ge are anisotropic (distinct longitudinal and transverse masses); the original microwave resonances were recorded near liquid-helium temperature (Dresselhaus–Kip–Kittel).
- Visibility condition, textbook form: \(\omega_c\tau\gtrsim 1\) (equivalently \(\omega\tau\gtrsim 1\) on resonance). If the carrier scatters before completing an orbit, there is no line. That is why CR is done in clean crystals, at low \(T\), and/or at high \(B\). A specific \(\tau\) is sample-dependent and is not a universal constant; the *inequality* is the boundary.
- Metals: the microwave field occupies only the skin layer ([skin-effect](skin-effect.md)). Azbel–Kaner geometry (\(B\) parallel to the surface) lets a carrier recut that layer once per orbit. Without that geometry, bulk-metal CR is not observed.
- The cyclotron radius \(r_c=m^*v_\perp/eB\) is a real orbit size. It is not the usual collapse: the line dies from clock mismatch or from \(\omega_c\tau<1\), not from a universal nanometre floor.

**Data confidence:** High — \(\omega_c=eB/m^*\), the 28 GHz T\(^{-1}\) free-electron scale, standard semiconductor masses, and the \(\omega_c\tau\gtrsim 1\) visibility condition are multiply reproduced. Any one sample’s \(\tau(T)\) is medium.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Resonance condition \(\omega=\omega_c\) (or \(\omega=n\omega_c\) in Azbel–Kaner / harmonic geometries). In a dielectric host the matching field can appear shifted by the background index; the laboratory reduction already includes that.
- Power absorption as a function of \(B\) (or \(\omega\)) is a line of width set by \(1/\tau\). The measured \(B_{\mathrm{res}}\) at known \(\omega\) is inverted for \(m^*\).
- Anisotropic bands: \(\omega_c\) depends on the direction of \(\mathbf{B}\) relative to the mass tensor. The angular pattern is data from which the tensor is read.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A carrier population in a field, with a scattering time long enough that an orbit is a well-defined clock (\(\omega_c\tau\gtrsim 1\)). In 3D metals the additional spatial resource is the skin layer the orbit must recut. There is no single film-thickness cliff. The “buffer” that actually gates the macro line is the *mean free path versus the orbit*, i.e. a clock resource written as a length.

- **Clock rate / latency.** Load-bearing. \(\omega\) must match \(\omega_c=eB/m^*\). \(B\) sets that clock. \(\tau\) is the reset / decoherence time of the orbital motion. This is a synchronization condition on a driven population, not a plasma-period screening cycle, though the same electrons can do both in a metal.

- **Energy barriers or thresholds.** No latch. \(B\) is required both to set \(\omega_c\) and, in practice, to push \(\omega_c\tau\) through unity. Tag `field-threshold` marks that resource.

- **Dominant failure modes.**
  - Clock: \(\omega\neq\omega_c\) → off resonance, no line.
  - Scattering / thermal: \(\omega_c\tau<1\) (impurity scattering, or phonon scattering as \(T\) rises) → the orbit is not completed; the line washes out. This is the thermal tag: \(T\) kills CR by shortening \(\tau\), not by a Curie-like transition.
  - Geometry: wrong polarization, or (in a metal) no Azbel–Kaner recut of the skin.
  - Field: \(B\to 0\) sends \(\omega_c\to 0\) and \(\omega_c\tau\to 0\) together.

- **Emergent constant or stable output.** An absorption line whose position is the effective mass (or mass tensor) of the carrier population.

### 4.6 Internal Consistency Notes

Clock match plus a scattering-time gate is a clean QSA specification. The collapse pair named in the index — \(\omega\neq\omega_c\), or \(\omega\tau<1\) — is exactly that pair.

The open item is \(m^*\) itself. QSA records \(0.067\,m_e\) in GaAs as a *measured output* of the lattice-plus-carrier machine. It does not derive that fraction from node rules. Filing CR under collective-field-response is still consistent: the macroscopic line is a synchronized orbital response of many carriers, and it fails when their common clock cannot be kept. The lattice that renormalizes the mass is tagged only by pointing at `semiconductor-gap-absorption` and the lattice-mode family; CR does not become a lattice-mode entry because the collapse is not a phonon cutoff.

[Faraday rotation](faraday-rotation.md) is the off-resonant cumulative cousin (circular-index split of order \(\omega_c/\omega\)), not this absorption line. Spin resonance shares the 28 GHz T\(^{-1}\) number for free \(g=2\) electrons and is a different degree of freedom; it is not filed here. `quantum-hall-effect` uses the same clean, high-\(B\), low-\(T\) 2DEG setting; the output there is a quantized Hall resistance, not an \(m^*\) line.

### 4.7 Overall Confidence in the QSA Mapping

**High** — matching \(\omega\) to \(eB/m^*\) and the \(\omega_c\tau\gtrsim 1\) visibility condition translate directly into clock, field, and thermal/scattering specifications; \(m^*\) is honestly left as an emergent output rather than a derived node mass.

## Related entries

- [faraday-rotation](faraday-rotation.md) — off-resonant circular-index accumulator on the same \(eB/m\) scale
- [skin-effect](skin-effect.md) — metal CR (Azbel–Kaner) is sampled only inside the skin layer
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — a different collective clock (\(\omega_p\)) of the same carriers
- [Quantum Hall effect](quantum-hall-effect.md) — same clean high-\(B\) 2DEG hardware; different macro output
- [Semiconductor gap absorption](semiconductor-gap-absorption.md) — the gapped host whose band mass CR reads out
