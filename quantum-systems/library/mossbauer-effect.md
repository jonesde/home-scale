---
id: mossbauer-effect
title: Mössbauer Effect (Recoilless Nuclear Resonance)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
  - thermal
  - energy-barrier
confidence_data: high
confidence_mapping: high
related:
  - debye-cutoff
  - phonon-dispersion
  - melting
  - x-ray-absorption-edge
updated: 2026-08-17
---

# Mössbauer Effect (Recoilless Nuclear Resonance)

### 4.1 Effect Name

Mössbauer effect (recoilless nuclear resonance)

### 4.2 Macroscopic Observation

A solid host containing a suitable nucleus (the calibration case is \(^{57}\mathrm{Fe}\), \(14.4\,\mathrm{keV}\)) emits and absorbs that gamma line without Doppler-recoil shift, so source and absorber resonate at laboratory velocities of millimetres per second. In a gas, a liquid, or a lattice that cannot take the recoil as a whole, the emission and absorption lines miss each other by the recoil energy and the resonant absorption disappears.

### 4.3 Established Quantitative Boundaries

- \(^{57}\mathrm{Fe}\) calibration line: \(E_\gamma = 14.4\,\mathrm{keV}\). Natural width \(\Gamma \approx 4.7\,\mathrm{neV}\) (\(\tau \approx 141\,\mathrm{ns}\)).
- Free-atom recoil energy \(E_R = E_\gamma^2 / 2Mc^2 \approx 2\,\mathrm{meV}\). \(E_R \gg \Gamma\), so a free Fe atom has no overlap of emission and absorption.
- Recoilless fraction \(f\) (Lamb–Mössbauer / Debye–Waller) is appreciable only when the lattice can absorb the recoil as a whole — low \(E_\gamma\), stiff / heavy host, not too high \(T\). Raising \(T\) toward and above the host Debye temperature drives \(f\to 0\).
- Melting or dissolving the host destroys the recoilless channel.

**Data confidence:** High — \(E_\gamma\), \(E_R\gg\Gamma\), and the solid-only resonance are textbook nuclear / lattice facts. Any one host’s \(f(T)\) is medium.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

\[
E_R = \frac{E_\gamma^2}{2Mc^2}, \qquad
f = \exp\!\left(-k_\gamma^2\langle x^2\rangle\right).
\]

Resonance exists when a recoilless fraction is present so the lines overlap within \(\Gamma\). These describe the observed absorption. They do not derive \(E_\gamma\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A crystalline (or otherwise bound) host that can take nuclear recoil as a whole-body mode. The nucleus is \(N=1\); the *lattice* is the buffer. A free atom is under-provisioned.

- **Clock rate / latency.** Nuclear lifetime (\(\sim 10^{-7}\,\mathrm{s}\) for \(^{57}\mathrm{Fe}\)) sets \(\Gamma\). Lattice vibrations that destroy \(f\) are the Debye / phonon clocks of the host.

- **Energy barriers or thresholds.** The nuclear line is a gate of width \(\Gamma\). The lattice condition \(E_R\) absorbed by the grid is the operating window, not a latch of a written nuclear state.

- **Dominant failure modes.**
  - Lattice: gas / liquid / melt \(\to\) \(f\to 0\) \(\to\) no resonance.
  - Thermal: \(T\) high enough that \(\langle x^2\rangle\) kills \(f\).
  - Nuclear: \(E_R\gg\Gamma\) with no host \(\to\) lines miss.
  - Doppler: laboratory velocity of \(\mathrm{mm\,s^{-1}}\) class walks off the line (that is how the spectrum is *read*, and also how it is destroyed).

- **Emergent constant or stable output.** A recoilless resonant absorption (and the isomer / hyperfine spectrum built on it) while the host lattice and \(T\) keep \(f\) finite.

### 4.6 Internal Consistency Notes

This is a lattice-mode effect whose *payload* is a nuclear line. [Debye cutoff](debye-cutoff.md) owns the phonon ceiling that sets \(f(T)\); this file owns the recoilless resonance as the output. Do not file it as an `energy-gate` whose collapse is \(E_\gamma < 14.4\,\mathrm{keV}\) — the 14.4 keV is the *line*, not an under-threshold non-occurrence of the Mössbauer channel.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(E_R\gg\Gamma\), the solid-only condition, and the \(f(T)\) collapse are sharp and translate into a lattice buffer plus a thermal / melt failure envelope.

## Related entries

- [debye-cutoff](debye-cutoff.md) — the phonon budget that sets \(f\)
- [phonon-dispersion](phonon-dispersion.md) — \(\langle x^2\rangle\) lives on the same grid
- [melting](melting.md) — grid loss kills recoilless emission
- [x-ray-absorption-edge](x-ray-absorption-edge.md) — another nuclear/atomic photon gate; not recoilless resonance
