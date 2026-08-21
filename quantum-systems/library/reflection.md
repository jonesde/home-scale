---
id: reflection
title: Reflection (Electron-Cloud Response)
status: formal
family: collective-field-response
constraints:
  - spatial-buffer
  - clock-latency
confidence_data: high
confidence_mapping: high
related:
  - plasma-frequency-cutoff
  - skin-effect
  - photoelectric-threshold
  - surface-plasmon-resonance
  - faraday-rotation
updated: 2026-08-20
---

# Reflection (Electron-Cloud Response)

### 4.1 Effect Name

Reflection (electron-cloud response)

### 4.2 Macroscopic Observation

Visible light incident on a polished silver or aluminum surface returns as a reflected beam with high efficiency. The surface appears mirror-like. No continuous external power is required to maintain the reflected image. If the metal film is made thin enough, the same surface becomes significantly transmitting and the mirror disappears.

### 4.3 Established Quantitative Boundaries

- Optical penetration / absorption depth in continuous Ag and Al in the visible is approximately 10–20 nm (set by the large imaginary part of the refractive index; penetration depth \(\lambda / 4\pi k\)).
- Below roughly 5–10 nm of *continuous* film thickness, reflectivity collapses and transmission rises sharply. Two experimental conditions are easily confused and must be kept separate:
  - **Electromagnetic penetration** in an already-continuous metal (the screening length above).
  - **Morphological continuity** of a deposited film (island / percolation threshold, also typically several nanometres, substrate-dependent). Both destroy the mirror; they are not the same constraint.
- Free-electron plasma energies (handbook / electron-energy-loss values): Al \(\hbar\omega_p \approx 15\,\mathrm{eV}\); Ag \(\hbar\omega_p \approx 9\,\mathrm{eV}\). The corresponding plasma periods are \(\sim 0.3\,\mathrm{fs}\) (Al) and \(\sim 0.5\,\mathrm{fs}\) (Ag).
- Ag’s *optical* reflectivity edge sits near \(3.9\,\mathrm{eV}\) (\(\sim 320\,\mathrm{nm}\)), well below the free-electron \(\omega_p\), because of d-band interband transitions. Al tracks the free-electron plasma edge much more closely. Alkali metals are the cleanest plasma-edge cases.
- Polished bulk Ag reflects \(\gtrsim 95\%\) across most of the visible; Al is typically \(\sim 90\%\). Reflectivity remains high through the infrared (Hagen–Rubens regime) and falls once the drive frequency reaches the plasma / interband edge.
- Close-packed (111) interplanar spacings: Ag \(2.36\,\mathrm{\AA}\), Al \(2.34\,\mathrm{\AA}\). A 10–20 nm continuous stack is therefore about 40–85 atomic planes, not 100–200. (The preliminary handover figure of 100–200 layers overstated the plane count; the nanometre threshold is the measured quantity and is unchanged.)
- Underlying single-electron response in time-resolved photoemission and streaking experiments resolves into the attosecond regime (\(10^{-18}\,\mathrm{s}\) scale). The collective optical response of the metal sits on the femtosecond plasma period.

**Data confidence:** High — optical constants, thin-film reflectivity, and plasma energies are multiply reproduced handbook measurements. The exact numerical location of the deposited-film percolation threshold is medium (process-dependent); the existence of a few-nanometre continuity cliff is not.

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

  For \(\omega < \omega_p\) and small damping, \(\operatorname{Re}\varepsilon < 0\) and a vacuum–metal interface supports high reflectivity.

- Normal-incidence Fresnel reflectance from complex index \(\tilde n = n + ik\):

  \[
  R = \left|\frac{1 - \tilde n}{1 + \tilde n}\right|^2
  \]

- Intensity penetration depth:

  \[
  \delta = \frac{\lambda}{4\pi k}
  \]

- Hagen–Rubens (low-frequency metals): \(R \approx 1 - 2\sqrt{2\varepsilon_0\omega / \sigma}\).

Carrier densities that feed \(\omega_p\): Al \(\sim 1.8 \times 10^{29}\,\mathrm{m^{-3}}\) (three valence electrons per atom); Ag \(\sim 5.9 \times 10^{28}\,\mathrm{m^{-3}}\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A continuous metal stack on the order of the optical penetration depth — about 10–20 nm, \(\sim 40\)–\(85\) atomic planes in Ag or Al — is required before a stable collective screening response can form and return a macroscopic reflected beam. Below that thickness the responding node count is under-provisioned and the reflection calculation fails (the film transmits). Islanded films fail earlier: the connected buffer never forms.

- **Clock rate / latency.** The electron population must register the incident field, synchronize into a collective oscillation, and emit the phase-reversed field on the plasma-period timescale (a few \(10^{-16}\) to \(10^{-15}\,\mathrm{s}\)). Single-electron dynamics underneath that collective step resolve faster (attosecond). Relative to any human or mechanical clock the result is already complete; the reflected image appears instantaneous.

- **Energy barriers or thresholds.** The operating condition is \(\omega < \omega_p\) (or, in Ag, below the interband-shifted optical edge) together with a continuous conducting volume at least one penetration depth thick. There is no static energy barrier holding a latched state; this is a driven collective response, not a memory.

- **Dominant failure modes.**
  - Spatial: continuous thickness \(\lesssim 5\)–\(10\,\mathrm{nm}\) (or a discontinuous morphology at any nominal thickness) → loss of coherent collective output → transparency.
  - Temporal / spectral: drive frequency above the plasma (or interband) edge → the population cannot complete the screening cycle in one drive period → transmission. This is the same machine failing a clock constraint rather than a buffer constraint; it is filed as the related queued entry `plasma-frequency-cutoff`.
  - Dissipative: large \(\gamma\) (poor metal, high temperature, dirty film) → reduced \(R\), not a sharp cliff.

- **Emergent constant or stable output.** A stable, phase-reversed reflected beam with material-typical \(R(\lambda)\) in the visible and infrared, produced with no continuous power input to the metal beyond the incident field itself.

### 4.6 Internal Consistency Notes

The spatial threshold and the ultrafast timescale map cleanly onto minimum connected node count and collective latency. The two thin-film cliffs (electromagnetic penetration vs. morphological percolation) are the same QSA failure class — buffer starvation — arriving by different experimental routes; they should not be collapsed into one number.

A closed mapping would also say *why* the required buffer is tens of nanometres rather than two or two hundred from node rules alone. In the standard description that length is \(\lambda / 4\pi k\), and \(k\) is itself an emergent optical constant of the same electron population. QSA currently *takes* the measured penetration depth as the buffer specification; it does not yet derive that depth from a more primitive node count. That is a gap, not a contradiction.

Ag’s interband-shifted edge means the simplest “clock = \(\omega_p\)” statement is too coarse for silver in the near-UV. Al and the alkali metals are the cleaner test of that clause. Visible-band mirrors still sit comfortably below both the free-electron and the interband edges, so the everyday reflection mapping is not threatened.

Contrast case, not yet written: `photoelectric-threshold` is a single-electron energy gate in the same metal. The mirror is a collective, below-threshold, zero-ejection response; photoemission is the above-threshold conversion. If both entries close, they should share the metal’s work function / plasma scales without conflicting buffer numbers.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the spatial and temporal boundaries are well measured and translate directly into a minimum connected buffer and a femtosecond collective latency; remaining gaps are about deriving the buffer length from node rules, not about the existence or location of the collapse.

## Related entries

- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — same collective screening, failed by drive frequency instead of thickness
- [Skin effect](skin-effect.md) — low-frequency limit of the same screening length
- [Surface plasmon resonance](surface-plasmon-resonance.md) — interface-bound collective mode of the same electron population
- [Photoelectric threshold](photoelectric-threshold.md) — single-electron energy gate in the same metals; contrast case
- [faraday-rotation](faraday-rotation.md) — Kerr rotation is Faraday on this metal face; a clause, not a second file
