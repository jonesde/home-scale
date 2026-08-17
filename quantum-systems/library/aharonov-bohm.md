---
id: aharonov-bohm
title: Aharonov–Bohm Effect (Enclosed-Flux Phase)
status: formal
family: collective-field-response
constraints:
  - spatial-buffer
  - clock-latency
  - field-threshold
confidence_data: high
confidence_mapping: high
related:
  - flux-quantization
  - josephson-effect
  - cyclotron-resonance
  - faraday-rotation
  - quantum-hall-effect
updated: 2026-08-17
---

# Aharonov–Bohm Effect (Enclosed-Flux Phase)

### 4.1 Effect Name

Aharonov–Bohm effect (enclosed-flux phase)

### 4.2 Macroscopic Observation

An electron interferometer whose two arms enclose a magnetic flux, with the electrons travelling in a region of vanishing \(\mathbf{B}\), shows a shift of the interference fringes as that enclosed flux is changed. The pattern is periodic in a universal flux quantum built from \(h\) and a single \(e\). Opening a path so the loop no longer encircles the flux, or destroying the interferometer’s phase coherence, removes the shift. Chambers (1960) and Tonomura’s shielded toroidal magnet established the field-free-path case.

### 4.3 Established Quantitative Boundaries

- Single-charge flux period (not the superconducting \(\Phi_0 = h/2e\)):

  \[
  \Phi_{\mathrm{AB}} = \frac{h}{e} = 4.135667\times 10^{-15}\,\mathrm{Wb}.
  \]

- Phase difference between the two paths:

  \[
  \Delta\varphi = \frac{e}{\hbar}\oint\mathbf{A}\cdot d\mathbf{l} = 2\pi\,\frac{\Phi}{\Phi_{\mathrm{AB}}}.
  \]

- Hardware: a multiply connected coherent path around a confined flux (whisker, solenoid, or shielded toroid). \(\mathbf{B}\) on the electron’s support can be made negligible compared with the enclosed flux; the shift remains.
- Collapse of the *shift* (not of ordinary two-slit fringes): enclosed \(\Phi\to 0\); a path that does not encircle the flux; coherence length shorter than the interferometer.

**Data confidence:** High — the \(h/e\) period and the field-free-path geometry are multiply reproduced. Residual leakage-\(B\) in any one whisker is medium.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms. The line integral of \(\mathbf{A}\) around a closed path equals the enclosed flux. The interference intensity is periodic in \(\Phi/\Phi_{\mathrm{AB}}\). These describe the observed shift. They do not derive \(h/e\) from a node count.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two coherent paths that together enclose a flux, plus an electron (or other charge-\(e\) carrier) whose coherence length spans the loop. The solenoid interior is *not* the electron’s buffer; the loop is. A simply connected path is under-provisioned.

- **Clock rate / latency.** The carrier’s de Broglie / interferometer transit. Decoherence faster than that transit erases the shift. This is not a plasma-period screening cycle.

- **Energy barriers or thresholds.** No latch. Enclosed flux is a field resource that *writes a phase*, not a stored directional moment.

- **Dominant failure modes.**
  - Topology: path does not enclose \(\Phi\) \(\to\) no AB shift.
  - Field: \(\Phi\to 0\) \(\to\) unshifted pattern.
  - Coherence: scattering / path difference beyond the coherence length \(\to\) no stable fringes to shift.
  - Charge: a neutral interferometer does not see this \(e\mathbf{A}\) phase (Aharonov–Casher is a different, harder case and is not this file).

- **Emergent constant or stable output.** A fringe shift periodic in \(h/e\), while the loop, the coherence, and the confined flux remain inside the envelope.

### 4.6 Internal Consistency Notes

The \(h/e\) period versus superconducting \(h/2e\) is a load-bearing split, the same honesty as not identifying \(\varphi\) with \(\omega_p\). This file owns the single-charge phase. [Flux quantization](flux-quantization.md) owns the pair increment.

Family assignment is by loss of collective phase / under-provisioned loop, not by a pairing gap. Do not fold this into `gapped-condensate`.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the \(h/e\) period, the enclosed-path hardware, and the coherence / topology collapses are well measured and translate into buffer and failure specifications.

## Related entries

- [flux-quantization](flux-quantization.md) — \(h/2e\) on a superconducting loop; different charge increment
- [josephson-effect](josephson-effect.md) — same \(h/2e\), read as a voltage–frequency lock
- [cyclotron-resonance](cyclotron-resonance.md) — electrons in a *local* \(B\), not a field-free enclosed flux
- [quantum-hall-effect](quantum-hall-effect.md) — another macroscopic \(h,e\) combination; 2DEG + perpendicular \(B\), not this interferometer
