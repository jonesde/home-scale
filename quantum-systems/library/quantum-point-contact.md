---
id: quantum-point-contact
title: Quantum Point Contact (1D Conductance Steps)
status: formal
family: gapped-coherence
constraints:
  - spatial-buffer
  - thermal
  - field-threshold
confidence_data: high
confidence_mapping: medium
related:
  - quantum-hall-effect
  - cyclotron-resonance
  - coulomb-blockade
updated: 2026-08-17
---

# Quantum Point Contact (1D Conductance Steps)

### 4.1 Effect Name

Quantum point contact (1D conductance steps)

### 4.2 Macroscopic Observation

A short, narrow constriction in a 2DEG (split-gate quantum point contact) shows flat steps in the two-terminal conductance at integer multiples of a universal conductance quantum as the gate voltage opens the channel. Pinch-off (\(n=0\)) gives near-zero conductance. Raising temperature, lengthening the constriction into a diffusive wire, or destroying the 2DEG washes the steps out. No perpendicular magnetic field is required. van Wees et al. and Wharam et al. (1988).

### 4.3 Established Quantitative Boundaries

- Conductance quantum (spin-degenerate 1D mode):

  \[
  G = n\,\frac{2e^2}{h}, \qquad
  \frac{2e^2}{h} \approx 7.748\times 10^{-5}\,\mathrm{S}.
  \]

- Hardware: a ballistic constriction of width comparable to the Fermi wavelength (tens of nanometres in a GaAs 2DEG), shorter than the mean free path, at low \(T\).
- Collapse: pinch-off (gate closes the last mode); \(T\) high enough to smear the subband edges; diffusive / dirty channel; 2DEG density or mobility collapsed.
- The “0.7 structure” is a harder related feature and is not the primary artifact.

**Data confidence:** High — the \(2e^2/h\) steps and pinch-off are multiply reproduced. Step flatness in any one device is medium (adiabaticity, interactions).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms. Landauer: each occupied 1D mode contributes \(2e^2/h\) (spin degeneracy). Gate voltage moves the saddle relative to \(E_F\) and changes the integer \(n\). These describe the observed staircase. They do not derive \(h/e^2\) from a node count.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A ballistic 1D constriction in a 2DEG, width \(\sim\lambda_F\). A wide 2D or 3D conductor is the wrong buffer (no mode staircase). Length must stay below the mean free path.

- **Clock rate / latency.** Fermi velocity / transit through the saddle. The DC staircase is not a radiated frequency.

- **Energy barriers or thresholds.** 1D subband edges are the gates that open one by one. Pinch-off is the last gate closing. No pairing gap and no perpendicular-\(B\) Landau gap.

- **Dominant failure modes.**
  - Gate: pinch-off \(\to\) \(G\to 0\).
  - Thermal: \(kT\) comparable to subband spacing \(\to\) steps smear.
  - Spatial: channel longer than the mfp, or wider than a few \(\lambda_F\) without mode resolution \(\to\) no staircase.
  - Buffer: 2DEG lost.

- **Emergent constant or stable output.** A conductance locked to \(n\times 2e^2/h\) while the constriction, the 2DEG, and \(T\) remain inside the envelope.

### 4.6 Internal Consistency Notes

This is **not** [quantum-hall-effect](quantum-hall-effect.md). QHE needs a perpendicular field, a bulk gap, and an edge path, and outputs \(h/\nu e^2\) Hall resistance. A QPC needs no \(B\) and outputs two-terminal \(2e^2/h\) steps. Same \(h,e\) bricks; different machine.

The constriction stack is assembled as draft `landauer-channel`. Contrast on `edge-channel` stays. Do not fold the two designs together.

The quantized value is taken from Landauer / metrology, the same class of underived output as \(R_K\). Mapping is Medium for that reason and for the 0.7 feature being out of scope.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the steps, pinch-off, and no-\(B\) hardware are sharp; \(2e^2/h\) is taken, and the 0.7 shoulder is explicitly unmapped.

## Related entries

- [quantum-hall-effect](quantum-hall-effect.md) — the other metrological \(h,e\) transport leftover; needs perpendicular \(B\)
- [cyclotron-resonance](cyclotron-resonance.md) — same 2DEG setting can host \(\omega_c\); not this DC staircase
- [coulomb-blockade](coulomb-blockade.md) — another small-structure electron gate; charging, not 1D modes
