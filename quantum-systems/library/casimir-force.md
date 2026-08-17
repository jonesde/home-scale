---
id: casimir-force
title: Casimir Force (Mode-Cutoff Attraction)
status: formal
family: collective-field-response
constraints:
  - spatial-buffer
  - thermal
confidence_data: high
confidence_mapping: medium
related:
  - reflection
  - blackbody-spectrum
  - total-internal-reflection
updated: 2026-08-17
---

# Casimir Force (Mode-Cutoff Attraction)

### 4.1 Effect Name

Casimir force (mode-cutoff attraction)

### 4.2 Macroscopic Observation

Two uncharged, conducting plates (or a sphere and a plate) brought to sub-micrometre separation attract. The force is not Coulomb charge and is not gravity. It falls rapidly as the gap opens and becomes unmeasurable at ordinary laboratory spacings. Non-conducting or very rough / patchy surfaces spoil the ideal \(1/d^{4}\) plate law. Lamoreaux (1997) measured the force in the \(0.6\)–\(6\,\mu\mathrm{m}\) class; later sphere–plate work tightened the comparison.

### 4.3 Established Quantitative Boundaries

- Ideal parallel-plate pressure at \(T=0\):

  \[
  \frac{F}{A} = \frac{\pi^2\hbar c}{240\,d^4}
    \approx 1.3\,\mathrm{mPa}
    \quad\text{at}\quad d = 1\,\mu\mathrm{m}.
  \]

- Working window in modern torsion / AFM geometries: tenths of a micrometre to a few micrometre. Below that, roughness and electrostatic patches dominate; above it the force drops into the instrument floor as \(1/d^{4}\) (or \(1/d^{3}\) for sphere–plate).
- Conducting, optically reflecting faces are required for the electromagnetic-mode cutoff that produces this number. A dielectric contrast still produces a (smaller) Casimir–Lifshitz force; vacuum / vacuum does not.
- Finite \(T\) adds a thermal correction that becomes important near and above \(d\sim \hbar c/kT\) (tens of micrometres at 300 K). That is a correction to this machine, not a second family.

**Data confidence:** High as a class (attraction exists, steep \(d\) law, needs conductors). Any one apparatus’s approach to the ideal plate formula is medium (geometry, roughness, patch potentials).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms. The \(\pi^2\hbar c/240d^4\) law is the mode-sum difference between the allowed electromagnetic spectrum inside the gap and the free spectrum outside. Sphere–plate uses the proximity-force reduction. These describe the observed attraction. They do not derive \(\hbar\) from a node count.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two faces with an electromagnetic contrast, separated by a gap of order \(0.1\)–\(1\,\mu\mathrm{m}\) for a laboratory force. The buffer is the *gap* (which modes fit), not a 10–20 nm metal stack — though the faces themselves must still be conducting on their own screening depth.

- **Clock rate / latency.** The electromagnetic modes of the cavity (\(\sim c/d\)). This is not a plasma-period of the metal electrons, though those electrons provide the boundary.

- **Energy barriers or thresholds.** No latch. The force is a driven-by-geometry output of the mode spectrum. Hold-power is not a stored bit.

- **Dominant failure modes.**
  - Spatial: \(d\) large \(\to\) \(F\) into the noise (\(1/d^{4}\)).
  - Spatial / morphology: roughness or tilt comparable to \(d\) \(\to\) the ideal law fails.
  - Contrast: no conducting / dielectric contrast \(\to\) no mode cutoff of this kind.
  - Electrostatic: residual patch charge can swamp Casimir at the same \(d\). That is a contrast channel, not this force.

- **Emergent constant or stable output.** An attractive force following the Casimir / Lifshitz class in \(d\), while the faces, the gap, and the electrostatic background remain inside the envelope.

### 4.6 Internal Consistency Notes

This is not the optical mirror of [reflection](reflection.md): the load-bearing resource is the *spectrum of allowed vacuum modes in the gap*, not a re-radiated beam. The faces still need a screening population; starving them of conductivity is a real collapse.

The mapping takes \(\pi^2\hbar c/240d^4\) from the mode sum. That is the same class of taken output as taking \(\delta=\lambda/4\pi k\). Mapping is therefore Medium: the collapses are real; the number is not derived from a node rule.

The dynamical Casimir effect (photons from a modulated boundary; Wilson et al. 2011 in a SQUID circuit) is a driven cousin and is not this static-force file.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the \(d\)-law, the conducting-face requirement, and the large-gap collapse are established; the ideal prefactor is taken, and patch / roughness sit between the formula and any one apparatus.

## Related entries

- [reflection](reflection.md) — the faces must still screen; that is a different output
- [blackbody-spectrum](blackbody-spectrum.md) — thermal EM average; the finite-\(T\) Casimir correction is a cousin, not this \(T=0\) plate law
- [total-internal-reflection](total-internal-reflection.md) — another boundary-conditioned EM mode
