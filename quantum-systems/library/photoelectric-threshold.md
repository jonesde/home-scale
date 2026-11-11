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
review_depth: light
related:
  - reflection
  - plasma-frequency-cutoff
  - work-function-thermionic
  - semiconductor-gap-absorption
  - ionization-threshold
  - photoconductivity
  - x-ray-absorption-edge
updated: 2026-11-11
---

# Photoelectric Threshold (Single-Electron Energy Gate)

### 4.1 Effect Name

Photoelectric threshold (single-electron energy gate)

### 4.2 Macroscopic Observation

Light on a clean metal surface ejects electrons into vacuum once the photon energy exceeds the work function of the surface. The maximum kinetic energy of the electrons rises linearly with frequency and does not depend on intensity; intensity sets the number of electrons. Just above the threshold the yield grows from zero as the square of the excess photon energy, and at finite temperature a weak thermal tail extends below it.

### 4.3 Established Quantitative Boundaries

- **Measured.** Work functions of polycrystalline metals, as compiled: Cs 1.95 eV, K 2.29 eV, Al 4.25 eV, Ag 4.33 eV, W 4.55 eV, Cu 4.55 eV, Pt 5.41 eV [S1]. The tungsten value agrees with [work-function-thermionic](work-function-thermionic.md), which also records a 1.81–2.14 eV spread for caesium across compilations.
- **Measured.** The work function belongs to a surface. The (100) face of tungsten is listed at 4.65 eV against 4.55 eV for the polycrystal, and on a surface made of patches the photoemission signal of the lower-work-function patch tends to eclipse the others [S1].
- **Computed here.** Threshold wavelength \(hc/\varphi\) with \(hc = 1239.84\) eV nm [S6]: Cs 636 nm, K 541 nm, Al 292 nm, Ag 286 nm, W and Cu 272 nm, Pt 229 nm. Of these only the alkalis emit under visible light.
- **Measured.** Stopping-potential measurements obey \(\tfrac{1}{2}mv^2 = hf - P\) and gave \(h = 6.57 \times 10^{-27}\) erg s with a stated precision of about 0.5 % [S4]. That is 0.8 % below the present exact value [S6].
- **Model (Fowler; Fermi–Dirac occupation in a free-electron metal).** At zero temperature the quantum efficiency near threshold is proportional to \((h\nu - \varphi)^2\) [S2][S3]. The temperature dependence near threshold comes from the number of electrons available for extraction; the threshold is found by fitting the whole curve at several temperatures, not by extrapolating to zero current, and cannot be fixed to better than about 1 % [S3]. For a copper-like cathode at 300 K the calculated efficiency is raised by about 0.1 %, and temperature matters little until \(k_BT/(h\nu - \varphi)\) approaches unity [S2].
- **Computed here.** \(k_BT\) at 300 K is 25.85 meV [S6], 0.57 % of the 4.55 eV work function of tungsten. That is the energy scale of the rounding.
- **Measured.** Timing. Photoelectrons from localized core states of tungsten emerge about 100 attoseconds after those from the conduction band [S5]. This is a relative delay between two channels. No opened source gives an absolute latency.
- **Measured.** Silver has a sharp reflectance minimum at 3.92 eV [S7], below its 4.33 eV work function [S1].
- **Convention.** This entry covers one-photon emission. Multiphoton emission at high intensity and the escape depth of the photoelectron are not quantified here: no source was opened for either.

**Data confidence:** High — the linear law, the existence of a material threshold and the quadratic onset are standard and were read in the cited sources. The Millikan result was read in a secondary account [S4] and the Fowler paper in its abstract [S3]. Work functions come from one compilation table [S1]; any one value is Medium at the 0.1 eV digit.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Einstein relation and stopping potential [S4]:

  \[
  K_\mathrm{max} = eV_s = h\nu - \varphi \qquad (h\nu \ge \varphi)
  \]

- Threshold wavelength: \(\lambda_\mathrm{th} = hc/\varphi\).
- Yield near threshold at zero temperature [S2][S3]:

  \[
  \mathrm{QE} \propto (h\nu - \varphi)^2
  \]

  The yield is continuous through the threshold. What starts at \(\varphi\) is the existence of emission, not a step in its size.

Yield depends on the surface, the angle and the polarization.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One electron at a surface. A single conversion is already the microscopic effect; the photocurrent is a rate of such events. No collective buffer is specified. No collection depth is filed.

- **Clock rate / latency.** The measured relative emission delay is about 100 attoseconds. Against any laboratory clock averaged over optical cycles the electron has left. Intensity sets the rate of events.

- **Energy barriers or thresholds.** \(\varphi\) is the load-bearing gate, 1.95–5.41 eV in the metals listed. Below it, in the one-photon regime at zero temperature, the conversion does not occur. Above it the surplus \(h\nu - \varphi\) appears as kinetic energy. There is no latch: the electron leaves and the surface holds no written state.

- **Dominant failure modes.**
  - **Threshold** — photon energy below \(\varphi\): no one-photon emission. The gate is an energy threshold that is exact at zero temperature. It is rounded on the scale of \(k_BT\) (26 meV at 300 K, 0.57 % of the tungsten gate), and the yield rises from zero as \((h\nu - \varphi)^2\), so the current has an onset and no step.
  - **Crossover** — surface nonuniformity: a real surface is a set of patches with different gates (0.10 eV between W(100) and polycrystalline W), so the observed onset is spread over tenths of an electronvolt and is weighted toward the lowest patches. Contamination moves the gate; no shift was sourced here.
  - **Crossover** — heat: emission without light grows as \(e^{-\varphi/k_BT}\) and is the subject of [work-function-thermionic](work-function-thermionic.md).

- **Emergent constant or stable output.** A surface-specific threshold, a photocurrent that starts there, and a linear \(K_\mathrm{max}(\nu)\) above it.

### 4.6 Internal Consistency Notes

The mapping is a single-particle energy gate: hardware scale, clock and failure all refer to \(\varphi\) compared with \(h\nu\).

Sourcing changed the numbers and left the threshold in place. This was one of three calibration files; the other two lost their headline cliffs when sourced, and this one keeps its: the gate is a true energy threshold, rounded by temperature over about 1 % of its value. Three corrections follow. The yield has no step at the threshold, only a quadratic onset. The work-function list now comes from one compilation (W 4.55 eV, where the first version had 4.3–4.6 eV; Ag 4.33 eV; Pt 5.41 eV). The attosecond figure is a relative delay between two emission channels. The escape-depth figures and the multiphoton clause of the first version are dropped for lack of an opened source, and the contrast with a thickness floor for reflection is removed because [reflection](reflection.md) has no such floor.

The work function and the plasma edge are different constraints on the same surface. In silver the reflectance minimum is at 3.92 eV and the work function is 4.33 eV; [plasma-frequency-cutoff](plasma-frequency-cutoff.md) gives the edge as 3.78–3.92 eV across sources. The edge follows carrier density and interband screening, the work function follows the surface.

A remaining gap: QSA takes measured \(\varphi\). It does not derive the 2–5 eV range from a surface-dipole and chemical-potential construction.

Related entries hold the same gate pattern at other openings: heat ([work-function-thermionic](work-function-thermionic.md)), a crystal gap ([semiconductor-gap-absorption](semiconductor-gap-absorption.md)), an atomic binding energy ([ionization-threshold](ionization-threshold.md), [x-ray-absorption-edge](x-ray-absorption-edge.md)).

### 4.7 Overall Confidence in the QSA Mapping

**High** — the collapse is a measured energy threshold that translates directly into a threshold-conversion specification. Open items: deriving \(\varphi\), and the spread of the gate over a patchy surface.

## Related entries

- [Reflection (electron-cloud response)](reflection.md) — collective response of the same metals below the threshold
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — collective spectral edge set by carrier density and screening, not by \(\varphi\)
- [Work function / thermionic emission](work-function-thermionic.md) — the same energy gate, opened by heat instead of a photon
- [Semiconductor gap absorption](semiconductor-gap-absorption.md) — crystal-wide absorption edge; a volume gate rather than a surface \(\varphi\)
- [Ionization threshold](ionization-threshold.md) — atomic / molecular single-particle gate
- [Photoconductivity](photoconductivity.md) — a gap gate read out as a current inside the solid
- [X-ray absorption edge](x-ray-absorption-edge.md) — inner-shell gates at keV

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Tran et al., "Anisotropic work function of elemental crystals", *Surf. Sci.* 687, 48 (2019), arXiv:1902.07811](https://arxiv.org/pdf/1902.07811) | full-text | Secondary for the compilations it tabulates (Kawano 2008; CRC Handbook): polycrystalline Cs, K, Al, Ag, W, Cu, Pt; W(100) 4.65 eV; lower-work-function patches dominate photoemission. |
| S2 | [Dowell and Schmerge, *Phys. Rev. ST Accel. Beams* 12, 074201 (2009)](https://journals.aps.org/prab/pdf/10.1103/PhysRevSTAB.12.074201) | full-text | Quadratic dependence of quantum efficiency on excess photon energy near threshold; size of the temperature effect at 300 K. |
| S3 | [Fowler, *Phys. Rev.* 38, 45 (1931)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.38.45) | abstract | Temperature dependence near threshold from the number of available electrons; graphical method using the whole curve; thresholds not determinable closer than about 1 %. |
| S4 | [Holton, "Millikan's Measurement of Planck's Constant", *Phys. Rev. Focus* 3, 23 (1999)](https://physics.aps.org/story/v3/st23) | full-text | Secondary account of Millikan, *Phys. Rev.* 7, 355 (1916), whose abstract page shows no text: the photoelectric equation, h = 6.57e-27 erg s, 0.5 % precision. |
| S5 | [Cavalieri et al., "Attosecond spectroscopy in condensed matter", *Nature* 449, 1029 (2007)](https://doi.org/10.1038/nature06229) | abstract | Delay of about 100 attoseconds between core-state and conduction-band photoelectrons from tungsten. Abstract read through the Europe PMC record. |
| S6 | [NIST, CODATA 2022 recommended values: Planck constant in eV/Hz (with the pages for e and k)](https://physics.nist.gov/cgi-bin/cuu/Value?hev) | full-text | Constants for hc, kT and the comparison with Millikan's h. |
| S7 | [Marini, Del Sole and Onida, *Phys. Rev. B* 66, 115101 (2002), arXiv:cond-mat/0206322](https://arxiv.org/abs/cond-mat/0206322) | abstract | Sharp reflectance minimum of silver at 3.92 eV. |
