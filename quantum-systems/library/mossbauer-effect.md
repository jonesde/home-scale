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
confidence_mapping: medium
review_depth: light
related:
  - debye-cutoff
  - phonon-dispersion
  - melting
  - x-ray-absorption-edge
updated: 2026-11-11
---

# Mössbauer Effect (Recoilless Nuclear Resonance)

### 4.1 Effect Name

Mössbauer effect (recoilless nuclear resonance)

### 4.2 Macroscopic Observation

A solid containing a suitable nucleus (the reference case is \(^{57}\mathrm{Fe}\), 14.4 keV) emits and absorbs that gamma line with no recoil shift for a fraction \(f\) of events, so a source and an absorber resonate and the line is scanned with relative velocities of fractions of a millimetre per second. For a free atom, a gas or an ordinary liquid the emission and absorption lines are displaced by the recoil energy and broadened by motion, and the resonance is not seen.

### 4.3 Established Quantitative Boundaries

- **Measured.** \(^{57}\mathrm{Fe}\) first excited state: \(14.4129(6)\,\mathrm{keV}\), half-life \(98.3(3)\,\mathrm{ns}\) [S1].
- **Computed here.** Mean life \(98.3/\ln 2 = 141.8\,\mathrm{ns}\); natural width \(\Gamma=\hbar/\tau = 4.64\,\mathrm{neV}\) (quoted as \(4.7\,\mathrm{neV}\) in [S2]).
- **Computed here.** Free-atom recoil energy \(E_R=E_\gamma^2/2Mc^2 = 1.96\,\mathrm{meV}\), with \(M=56.9354\,\mathrm{u}\) [S1]. \(E_R/\Gamma = 4.2\times10^{5}\), in line with the "5–6 orders of magnitude" of [S2]. \(E_R/k = 22.7\,\mathrm{K}\).
- **Computed here.** Doppler velocity that shifts the line by one natural width: \(c\Gamma/E_\gamma = 0.097\,\mathrm{mm\,s^{-1}}\).
- **Measured.** The effect is not observed for freely moving atoms or molecules, in a gas or a liquid. Recoilless emission and absorption occur in the solid state, crystalline or non-crystalline [S2]. Except under extreme conditions the effect cannot be achieved in liquids; solutions are studied frozen [S4].
- **Model (Debye lattice).** \(f\) rises with falling \(E_\gamma\), falling temperature and rising Debye temperature of the host [S2]. The dependence is continuous. No numeric \(f(T)\) for a named host was opened.
- **Measured.** Approach to melting, metallic tin (\(^{119}\mathrm{Sn}\), 24 keV), 120 K to the melting point: the Debye–Waller factor follows a Debye temperature of 142 K at low temperature with marked anharmonicity above; in the last few degrees below melting the absorption drops rapidly and the line broadens. The authors attribute this to self-diffusion in the solid, with a diffusion coefficient of about \(10^{-8}\,\mathrm{cm^2\,s^{-1}}\) at 0.6 K below the melting point [S3].
- **Model (Singwi–Sjölander continuous diffusion).** Diffusion broadens the line by \(\Delta\varepsilon = 4\pi E_\gamma^2 D/hc^2 = 2\hbar k_\gamma^2 D\) [S4].
- **Computed here.** For \(^{57}\mathrm{Fe}\) with \(D = 0.6\times10^{-9}\,\mathrm{m^2\,s^{-1}}\) (iron ions in water [S4]) the broadening is \(4.2\,\mathrm{meV}\), about \(9\times10^{5}\,\Gamma\). The broadening equals \(\Gamma\) at \(D = 6.6\times10^{-16}\,\mathrm{m^2\,s^{-1}}\).

**Data confidence:** High for the nuclear line (evaluated nuclear data) and for the solid-only observation. Medium for the thermal behaviour: one abstract for tin near melting, a model for the diffusive width, and no opened value of \(f\) for any host.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

\[
E_R = \frac{E_\gamma^2}{2Mc^2}, \qquad
f = \exp\!\left(-k_\gamma^2\langle x^2\rangle\right), \qquad
\Delta\varepsilon_\mathrm{diff} = 2\hbar k_\gamma^2 D .
\]

\(\langle x^2\rangle\) is the mean-square displacement of the nucleus along the photon direction [S2]. The relations describe the observed absorption. They do not derive \(E_\gamma\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A host that binds the nucleus so that recoil is taken by the body as a whole. The nucleus is one node; the host is the buffer. Crystalline order is not required: a non-crystalline solid works. What is required is that the nucleus neither recoils freely nor diffuses appreciably during the nuclear lifetime.

- **Clock rate / latency.** The nuclear mean life (142 ns for \(^{57}\mathrm{Fe}\)) sets \(\Gamma\) and is the window over which the nucleus must stay put. The host's vibration spectrum ([debye-cutoff](debye-cutoff.md)) sets \(f\).

- **Energy barriers or thresholds.** The nuclear line is a gate of width \(\Gamma\). The host condition is an operating window, not a latch of a written state.

- **Dominant failure modes.**
  - **Threshold** — no host: for a free atom \(E_R\) exceeds \(\Gamma\) by \(4\times10^{5}\) and the lines do not overlap.
  - **Crossover** — thermal: \(f=\exp(-k_\gamma^2\langle x^2\rangle)\) falls continuously as \(\langle x^2\rangle\) grows with temperature; the scale is the host's Debye temperature.
  - **Crossover** — diffusion: the line broadens by \(2\hbar k_\gamma^2 D\). It reaches the natural width near \(D\sim7\times10^{-16}\,\mathrm{m^2\,s^{-1}}\) for \(^{57}\mathrm{Fe}\) and is \(10^{6}\) widths in a water-like liquid. In tin the loss starts in the solid, a few degrees below melting.
  - **Crossover** — Doppler: relative velocity detunes the line on the scale \(c\Gamma/E_\gamma\approx0.1\,\mathrm{mm\,s^{-1}}\); this is also how the spectrum is read.

- **Emergent constant or stable output.** A recoilless resonant absorption, and the isomer and hyperfine spectrum built on it, while the host keeps \(f\) finite and the line narrow.

### 4.6 Internal Consistency Notes

The effect is a lattice-mode effect whose payload is a nuclear line. [Debye cutoff](debye-cutoff.md) owns the phonon spectrum that sets \(f(T)\); this file owns the resonance. The 14.4 keV is the line, not a threshold below which the channel fails, so the entry is not an energy gate.

Sourcing changed the failure picture. The first version treated melting as the collapse and the crystal as the buffer. The sources show three corrections: non-crystalline solids support the effect, so Bragg order is not the resource; the thermal loss is a continuous fall of \(f\), not a cut at the Debye temperature; and near melting the measured loss in tin begins in the solid and is assigned to diffusion. A simple melt still shows no resonance, so the outcome "no resonance in the liquid" stands while its cause moves from grid loss to diffusion and free recoil. Nuclear numbers are unchanged apart from precision (\(\Gamma\) 4.64 neV, \(E_R\) 1.96 meV).

Open: no measured \(f\) for iron or tin was opened, and the diffusive width in liquids is disputed in at least one study [S4], so the crossover value of \(D\) is a model figure.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the nuclear gate and the need for a binding host are firm, but the failure modes are crossovers in temperature and diffusion with only model numbers attached, and the buffer is binding rather than crystalline order. Lowered from High.

## Related entries

- [debye-cutoff](debye-cutoff.md) — the phonon spectrum that sets \(f\)
- [phonon-dispersion](phonon-dispersion.md) — \(\langle x^2\rangle\) is a sum over the same modes
- [melting](melting.md) — the liquid shows no resonance; the loss begins below the melting point
- [x-ray-absorption-edge](x-ray-absorption-edge.md) — an atomic photon gate; not a recoilless resonance

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [IAEA Nuclear Data Services, LiveChart data service: ENSDF levels and ground-state data for ⁵⁷Fe (evaluator M. R. Bhat, 1998)](https://nds.iaea.org/relnsd/v1/data?fields=levels&nuclides=57fe) | full-text | First excited state 14.4129(6) keV, half-life 98.3(3) ns; atomic mass 56.93539195 u from the ground-state record. |
| S2 | [Gütlich, "Mössbauer Spectroscopy – Principles and Applications", lecture notes, Universität Mainz](https://www.blogs.uni-mainz.de/fb09akguetlich/files/2017/11/Moessbauer_Lectures.pdf) | full-text | Width 4.7 neV, recoil 2 meV, 5–6 orders of magnitude; no effect in gas or liquid; solid state, crystalline or non-crystalline; dependence of f on energy, temperature and Debye temperature; formula for f. Secondary. |
| S3 | [Boyle, Bunbury, Edwards and Hall, "The Mössbauer effect in tin from 120 K to the melting point", *Proc. Phys. Soc.* 77, 129 (1961)](https://www.osti.gov/biblio/4070011) | abstract | Debye temperature 142 K; anharmonicity; rapid drop and line broadening in the last degrees below melting, assigned to self-diffusion of about 10⁻⁸ cm²/s. |
| S4 | [Vankó et al., *J. Radioanal. Nucl. Chem.* 246, 97 (2000)](https://nucssp.rmki.kfki.hu/articles/catalog/00/vanko.jrnc.246.97.2000.pdf) | full-text | The effect cannot be achieved in liquids except under extreme conditions; Singwi–Sjölander diffusional broadening formula; diffusion coefficient of iron ions in water; doubt about the diffusive reading of one liquid spectrum. |
