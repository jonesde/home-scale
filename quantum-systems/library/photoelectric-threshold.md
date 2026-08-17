---
id: photoelectric-threshold
title: Photoelectric Threshold (Single-Electron Energy Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - thermal
confidence_data: high
confidence_mapping: high
related:
  - reflection
  - plasma-frequency-cutoff
  - work-function-thermionic
  - semiconductor-gap-absorption
  - ionization-threshold
  - photoconductivity
  - x-ray-absorption-edge
updated: 2026-08-17
---

# Photoelectric Threshold (Single-Electron Energy Gate)

### 4.1 Effect Name

Photoelectric threshold (single-electron energy gate)

### 4.2 Macroscopic Observation

Light incident on a clean metal surface ejects electrons into vacuum only when the optical frequency is high enough. Below that threshold the photocurrent is absent (apart from a small thermal tail). Above it, ejected electrons carry a maximum kinetic energy that rises linearly with frequency and does not rise with intensity. Intensity changes the *number* of electrons, not the cutoff energy. The same metals that act as mirrors in the visible can emit once the drive is taken into the ultraviolet.

### 4.3 Established Quantitative Boundaries

- Work function \(\varphi\) of common metals lies in the \(2\)–\(6\,\mathrm{eV}\) class. Handbook ranges (clean surfaces; face- and contamination-dependent): Cs \(\approx 1.95\,\mathrm{eV}\) (low end); K \(\approx 2.29\,\mathrm{eV}\); Al \(4.06\)–\(4.26\,\mathrm{eV}\); Ag \(4.26\)–\(4.74\,\mathrm{eV}\); W \(\approx 4.3\)–\(4.6\,\mathrm{eV}\); Pt \(5.12\)–\(5.93\,\mathrm{eV}\) (high end). \(\varphi\) is a *surface* number, not a bulk constant; adsorbates shift it by tenths of an eV.
- Threshold wavelength \(\lambda_\mathrm{th} = hc/\varphi\): about \(640\,\mathrm{nm}\) at \(1.95\,\mathrm{eV}\) (Cs, red / near-IR) and about \(210\,\mathrm{nm}\) at \(6\,\mathrm{eV}\) (deep UV). Most structural metals therefore emit only in the ultraviolet.
- Einstein relation, confirmed by stopping-potential measurements: \(K_\mathrm{max} = h\nu - \varphi\), or \(eV_s = h\nu - \varphi\). \(K_\mathrm{max}\) is independent of intensity in the linear (one-photon) regime.
- Finite temperature rounds the T=0 cliff. A Fowler tail of thermally occupied states above the Fermi level produces a small photocurrent slightly below \(h\nu = \varphi\). The gate is sharp on the scale of \(\varphi\), not infinitely sharp on the scale of \(kT\).
- Escape depth of the photoelectron is a nanometre-class inelastic mean free path (the “universal curve,” a minimum near \(0.5\,\mathrm{nm}\) around \(50\,\mathrm{eV}\), a few nanometres nearer threshold). That is a spatial scale of *collection*, not the collapse of the conversion. The conversion fails when \(h\nu < \varphi\), at any thickness.
- High intensity is a different channel: multiphoton emission when \(n h\nu > \varphi\). That is not the linear single-photon gate this entry owns.

**Data confidence:** High — the linear \(K_\mathrm{max}(\nu)\) law, the existence of a material threshold, and the \(2\)–\(6\,\mathrm{eV}\) class are among the most reproduced measurements in metal physics. Any one polycrystalline \(\varphi\) is medium at the \(0.1\,\mathrm{eV}\) digit.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Einstein photoelectric equation:

  \[
  K_\mathrm{max} = h\nu - \varphi \qquad (h\nu \ge \varphi)
  \]

  For \(h\nu < \varphi\) there is no linear emission.

- Stopping potential:

  \[
  eV_s = h\nu - \varphi
  \]

- Threshold wavelength:

  \[
  \lambda_\mathrm{th} = \frac{hc}{\varphi}
  \]

  with \(hc \approx 1240\,\mathrm{eV\cdot nm}\).

- Fowler (finite-\(T\)) yield near threshold is a thermal-smearing correction to the T=0 step, not a second gate.

Yield (electrons per incident photon) is surface-, angle-, and polarization-dependent and is not a universal constant.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One electron at a surface. This is not a collective buffer. A single conversion event is already the microscopic effect; the macroscopic photocurrent is just a rate of such events. That is the contrast with [reflection](reflection.md), which needs a continuous 10–20 nm metal stack before a stable reflected beam exists. The nanometre escape depth limits how deep a converted electron can start and still be collected; it does not set the on/off of the gate.

- **Clock rate / latency.** The conversion itself resolves in the attosecond regime (streaking delays of tens to hundreds of attoseconds). Relative to any optical-cycle-averaged laboratory clock the electron is already gone. Intensity sets the *rate*, not the latency of one event.

- **Energy barriers or thresholds.** \(\varphi\) is the load-bearing gate. Below it, in the linear regime, the conversion does not occur. Above it, the surplus \(h\nu - \varphi\) appears as kinetic energy. There is no latch: the electron leaves; the surface is not left in a stored directional state.

- **Dominant failure modes.**
  - Under-threshold input: \(h\nu < \varphi\) → no linear photoemission (only the Fowler tail, exponentially small in \((\varphi - h\nu)/kT\)).
  - Surface shift: contamination or a different crystal face moves \(\varphi\) by tenths of an eV and relocates the gate. That is a change of the threshold, not a failure of the gate logic.
  - Thermal: \(kT\) comparable to \(\varphi\) opens the related thermionic channel ([work-function-thermionic](work-function-thermionic.md)) even at \(h\nu = 0\).
  - Intensity (exception): multiphoton conversion when the field is large enough that \(n h\nu > \varphi\). Outside the scope of the linear gate.

- **Emergent constant or stable output.** A material- and face-typical threshold \(\varphi\), a photocurrent that is zero below it, and a linear \(K_\mathrm{max}(\nu)\) above it.

### 4.6 Internal Consistency Notes

The mapping is a single-particle energy gate and closes on that description. Hardware scale, clock, and failure are all the same number: \(\varphi\), compared with \(h\nu\). No collective buffer is required, and none is observed — photoemission persists from adsorbate-covered or atomically thin emitters once \(h\nu\) clears the (possibly shifted) threshold.

Contrast with reflection is the internal-consistency check. The same Ag or Al surface, below \(\varphi\) and below \(\omega_p\), returns a collective reflected beam and ejects no electrons. Above \(\varphi\), single-electron conversion turns on. The two thresholds are numerically close in some metals (Ag optical plasma edge \(\sim 3.9\,\mathrm{eV}\), Ag \(\varphi \sim 4.3\)–\(4.7\,\mathrm{eV}\)) and must not be identified: one tracks \(n\) and interband structure, the other tracks a surface dipole plus the bulk Fermi level. [Plasma-frequency cutoff](plasma-frequency-cutoff.md) is the collective spectral twin of reflection, not a second name for \(\varphi\).

A remaining gap: QSA takes measured \(\varphi\) as the gate. It does not derive the 2–6 eV class from a surface-dipole plus chemical-potential construction. Face dependence and contamination shifts show that the gate is a surface resource; they do not by themselves supply that derivation. That is a gap, not a contradiction.

Related entries occupy the same gate pattern at other openings: heat ([work-function-thermionic](work-function-thermionic.md)), a crystal gap ([semiconductor-gap-absorption](semiconductor-gap-absorption.md)), an atomic binding energy ([ionization-threshold](ionization-threshold.md), [x-ray-absorption-edge](x-ray-absorption-edge.md)).

### 4.7 Overall Confidence in the QSA Mapping

**High** — the collapse is a single measured energy gate and translates directly into a threshold-conversion specification; the open item is deriving \(\varphi\) from more primitive surface numbers, not the location or the single-electron character of the gate.

## Related entries

- [Reflection (electron-cloud response)](reflection.md) — collective, below-threshold, zero-ejection response of the same metals
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — collective spectral gate set by \(n\), not by \(\varphi\)
- [Work function / thermionic emission](work-function-thermionic.md) — the same energy gate, opened by heat instead of a photon
- [Semiconductor gap absorption](semiconductor-gap-absorption.md) — crystal-wide absorption edge; a volume gate rather than a surface \(\varphi\)
- [Ionization threshold](ionization-threshold.md) — atomic / molecular single-particle gate
- [Photoconductivity](photoconductivity.md) — a gap gate read out as a current inside the solid
- [X-ray absorption edge](x-ray-absorption-edge.md) — inner-shell gates at keV
