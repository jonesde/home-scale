---
id: quantum-hall-effect
title: Quantum Hall Effect (Landau-Gap Plateaus)
status: formal
family: gapped-coherence
constraints:
  - field-threshold
  - spatial-buffer
  - thermal
  - energy-barrier
  - clock-latency
confidence_data: high
confidence_mapping: medium
related:
  - cyclotron-resonance
  - superconductivity
  - flux-quantization
  - josephson-effect
  - electron-heat-capacity
  - faraday-rotation
updated: 2026-08-17
---

# Quantum Hall Effect (Landau-Gap Plateaus)

### 4.1 Effect Name

Quantum Hall effect (Landau-gap plateaus)

### 4.2 Macroscopic Observation

A high-mobility two-dimensional electron gas in a strong magnetic field perpendicular to the plane shows flat plateaus in the Hall resistance at a universal set of values, while the longitudinal resistance drops toward zero. Moving the field off a plateau, raising the temperature, or raising the current destroys the flatness and restores a finite \(R_{xx}\). The primary laboratory artifact is the *integer* sequence of plateaus. Fractional plateaus exist in cleaner samples at lower temperature and are recorded here only as a harder related case.

### 4.3 Established Quantitative Boundaries

- Quantized Hall resistance (integer plateaus):

  \[
  R_H = \frac{h}{\nu e^2} = \frac{R_K}{\nu}, \qquad \nu = 1, 2, 3, \ldots
  \]

  with the von Klitzing constant

  \[
  R_K = \frac{h}{e^2} \approx 25812.807\,\Omega
  \]

  On a plateau, \(R_{xx} \to 0\). Off the plateau, \(R_{xx}\) is finite and \(R_H\) is not flat.

- Hardware window: a 2D electron system (Si inversion layer, GaAs/AlGaAs heterojunction, later graphene) plus a magnetic field *perpendicular* to the plane. An in-plane field does not open this artifact. Low temperature and modest current are required; raising either washes the plateaus out. Graphene in a large perpendicular field can still show integer plateaus near room temperature — the same gap-versus-\(kT\) constraint, not a different machine.
- Filling factor (descriptive bookkeeping of density and field):

  \[
  \nu = \frac{n_s h}{eB}
  \]

  Plateaus are centred where this ratio sits near an integer.
- Fractional plateaus at certain rational \(\nu\) appear in higher-mobility samples at still lower \(T\). They are a related, harder case and are not the primary artifact of this file.

**Data confidence:** High — \(R_K\), the integer sequence, the 2DEG + perpendicular-\(B\) requirement, and destruction by temperature or current are metrological / handbook facts. The precise current and temperature at which a given sample leaves metrological flatness are medium (mobility- and geometry-dependent).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Hall and longitudinal resistances on an integer plateau:

  \[
  R_H = \frac{h}{\nu e^2}, \qquad R_{xx} \to 0 \qquad (\nu \in \mathbb{N})
  \]

- Cyclotron scale of the applied field (same combination as [cyclotron-resonance](cyclotron-resonance.md)):

  \[
  \omega_c = \frac{eB}{m}, \qquad \ell_B = \sqrt{\frac{\hbar}{eB}}
  \]

  \(\hbar\omega_c\) is the Landau-level spacing; \(\ell_B\) is the magnetic length. Plateaus survive only while \(kT\) and the Hall electric field remain small compared with the gap that this spacing (plus the sample’s disorder-broadened mobility gap) sets.

- Filling \(\nu = n_s h / (eB)\) locates the plateaus in the \((n_s, B)\) plane. It is bookkeeping, not a derivation of why \(R_H\) equals \(h/\nu e^2\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A two-dimensional electron buffer plus a perpendicular field. The 2D confinement is a spatial resource: a bulk 3D metal in the same \(B\) does not produce these plateaus. Once the field opens a gap in the bulk of the 2DEG, the surviving current path is along the edges. Magnetic length \(\ell_B\) is the in-plane spatial scale set by \(B\). QSA records this layered hardware (2D well / bulk gap / edge path) as the measured architecture; it does not derive the edge path from node rules.

- **Clock rate / latency.** The cyclotron frequency \(\omega_c = eB/m\) is the field-set clock. It is the same combination that [cyclotron-resonance](cyclotron-resonance.md) reads as an absorption line. The Hall plateau is not itself a radiated frequency; it is a DC resistance that remains stable while that clock keeps the Landau ladder resolved against scattering and against \(kT\).

- **Energy barriers or thresholds.** The Landau-level (mobility) gap is the energy barrier that protects a plateau. \(kT\) comparable to the gap, or a Hall field / current large enough to break down the gap, collapses the quantization. The perpendicular-field condition is a field threshold that *opens* the gap; moving \(B\) so that \(\nu\) sits between integers takes the system out of a gap and off the plateau.

- **Dominant failure modes.**
  - Field / filling: \(B\) off a plateau (\(\nu\) not in a gap) \(\to\) \(R_H\) not flat, \(R_{xx}\) finite.
  - Orientation: \(B\) in-plane \(\to\) this artifact does not open.
  - Thermal: \(T\) high enough to populate adjacent levels \(\to\) plateaus wash out.
  - Current: Hall-field / current breakdown \(\to\) same loss of flatness and of \(R_{xx}\to 0\).
  - Buffer: 2DEG destroyed (density or mobility collapsed) \(\to\) no integer ladder to sit in.

- **Emergent constant or stable output.** A Hall resistance locked to \(R_K / \nu = h/(\nu e^2)\) with \(R_K \approx 25812.807\,\Omega\), together with a vanishing longitudinal resistance, while the 2DEG, the perpendicular field, the temperature, and the current remain inside the envelope above.

### 4.6 Internal Consistency Notes

The failure envelope — off-plateau \(B\), in-plane \(B\), high \(T\), high current, lost 2DEG — is internally consistent with a gapped 2D machine whose surviving transport path is an edge channel. Graphene’s high-temperature integer plateaus sit on the same gap-versus-\(kT\) clause and do not require a second family.

The mapping does not close tightly, for three recorded reasons.

1. **Underived output.** QSA *takes* \(R_H = h/\nu e^2\) from metrology. It does not obtain that combination from a node-count or buffer rule. This is the same class of gap as taking \(\lambda/4\pi k\) as the mirror thickness on [reflection](reflection.md), but here the output is a universal constant rather than a material optical depth, so the missing derivation is more load-bearing.
2. **Architecture recorded, not derived.** Bulk gap plus edge path is the measured surviving hardware. Why the current is expelled to the edge, and why that forces the Hall resistance onto \(R_K/\nu\), is not a QSA specification yet.
3. **Fractional effect out of scope.** Fractional plateaus are a harder related case. No anyon, composite-fermion, or fractional-charge story is used or required, and none is added to close the integer mapping.

The 2DEG / bulk-gap / edge-path stack is assembled as draft `edge-channel` in the analysis layer. That names the leftover; it does not derive \(R_K\). A 1D constriction ([quantum-point-contact](quantum-point-contact.md)) is contrast, not a member.

Disorder (the mobility gap that *widens* a plateau) is an extra, sample-dependent resource, analogous to pinning on [type-ii-critical-field](type-ii-critical-field.md). The integer values of \(R_H\) do not depend on closing it; the width of the flat region does.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the integer plateaus, \(R_K\), and the \(B\) / \(T\) / current collapses are metrological, but the quantized value is taken rather than derived, the edge-channel architecture is recorded rather than specified from node rules, and the fractional case is explicitly unmapped.

## Related entries

- [cyclotron-resonance](cyclotron-resonance.md) — same \(\omega_c = eB/m\) clock, read as absorption rather than as a resistance plateau
- [superconductivity](superconductivity.md) — another dissipationless channel protected by a gap; different hardware, different constant
- [flux-quantization](flux-quantization.md) — macroscopic integer built from \(h\) and \(e\); loop fluxoid rather than Hall resistance
- [josephson-effect](josephson-effect.md) — complementary metrological lock (\(2e/h\)); voltage standard next to this resistance standard
- [electron-heat-capacity](electron-heat-capacity.md) — density of states of the same electron population, including Landau quantization as a field-tuned average
- [faraday-rotation](faraday-rotation.md) — another macroscopic reading of electrons in a magnetic field; not quantized, not 2D
