---
id: deuteron-photodisintegration
title: Deuteron Photodisintegration (2.224 MeV Unbinding Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
confidence_data: high
confidence_mapping: high
review_depth: standard
related:
  - pair-production
  - ionization-threshold
  - muon-catalyzed-fusion
  - photoelectric-threshold
updated: 2026-11-11
---

# Deuteron Photodisintegration (2.224 MeV Unbinding Gate)

### 4.1 Effect Name

Deuteron photodisintegration (2.224 MeV unbinding gate)

### 4.2 Macroscopic Observation

A gamma-ray beam on a deuterium target produces free protons and neutrons when the photon energy exceeds the deuteron binding energy by a small recoil term. Below that energy the reaction \(\gamma + d \to p + n\) does not occur. Above it the yield rises continuously from zero, passes a maximum near 4.4 MeV and falls. The reverse reaction, capture of a neutron by a proton, emits a gamma ray of 2.223 MeV, and the wavelength of that line is how the binding energy is measured.

### 4.3 Established Quantitative Boundaries

- **Measured.** Deuteron binding energy \(B_d = 2\,224\,566.14(41)\,\mathrm{eV}\), from the wavelength of the \(n + p \to d + \gamma\) capture line, \(5.576\,712\,99(99)\times 10^{-13}\,\mathrm{m}\), measured by crystal diffraction and corrected for recoil [S1].
- **Computed here.** That wavelength is a photon energy of 2.223248 MeV. The deuteron recoil takes \(E_\gamma^2/(2 M_d c^2) = 1.318\,\mathrm{keV}\), using \(M_d c^2 = 1875.612945\,\mathrm{MeV}\) [S2]. The capture photon therefore carries 1.3 keV less than \(B_d\).
- **Computed here.** Photodisintegration threshold on a deuteron at rest: \(B_d\,(1 + B_d/2M_dc^2) = 2.225885\,\mathrm{MeV}\), 1.32 keV above \(B_d\). A secondary source quotes 2.226 MeV [S3].
- **Measured.** The neutron mass is obtained from this binding energy, as \(m(n) = m({}^{2}\mathrm{H}) - m({}^{1}\mathrm{H}) + B_d\) [S1]. \(B_d\) is therefore an input to the mass table and not a consequence of it.
- **Measured.** Cross-section. Maximum of 2.5 mb at about 4.4 MeV, falling to 0.5 mb at 22 MeV [S3]; the peak position of 4.4 MeV is also given by the NBS evaluation [S5]. Measured points quoted in [S4]: \(1.300 \pm 0.029\,\mathrm{mb}\) at 2.62 MeV, \(1.474 \pm 0.032\,\mathrm{mb}\) at 2.76 MeV and \(2.430 \pm 0.170\,\mathrm{mb}\) at 4.45 MeV.
- **Model (effective-range theory).** Just above threshold the cross-section rises as the square root of the excess energy, through a magnetic-dipole transition to the unbound spin-singlet state; that term dominates up to about 2.4 MeV, and the electric-dipole term dominates above [S3][S5].
- **Measured.** Inverse reaction: thermal neutron capture on the proton has a cross-section of \(334.2 \pm 0.5\,\mathrm{mb}\) at 0.0253 eV [S4].

**Data confidence:** High — the binding energy was read in the primary measurement. The cross-section values come from two secondary sources that quote the measurements and from one evaluation; the original cross-section papers were not opened.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

\[
\gamma + d \;\to\; p + n, \qquad E_\gamma \ge B_d\left(1 + \frac{B_d}{2M_dc^2}\right) = 2.225885\,\mathrm{MeV}.
\]

\[
n + p \;\to\; d + \gamma, \qquad E_\gamma = B_d - \frac{E_\gamma^2}{2M_dc^2} = 2.223248\,\mathrm{MeV}\ \text{(capture at rest)}.
\]

Near threshold, with \(E_\gamma\) in MeV [S3]:

\[
\sigma \approx 675\,\frac{\sqrt{E_\gamma - 2.226}}{E_\gamma\,(E_\gamma - 2.149)}\ \mathrm{mb}, \qquad E_\gamma \lesssim 2.3\,\mathrm{MeV}.
\]

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One photon and one deuteron. The two products carry the momentum, so no third body is needed. Yield scales with the deuterium column density.

- **Clock rate / latency.** No delay is resolved in the sources read. Collection of the proton or neutron is a later step.

- **Energy barriers or thresholds.** \(B_d = 2.224566\,\mathrm{MeV}\) plus 1.32 keV of recoil. It unbinds an existing proton–neutron bound state; nothing is created and no state is held.

- **Dominant failure modes.**
  - **Threshold** — photon energy below 2.225885 MeV: the reaction does not occur.
  - **Crossover** — just above threshold: the cross-section rises from zero as \(\sqrt{E_\gamma - E_\mathrm{th}}\) and reaches its 2.5 mb maximum only near 4.4 MeV, so a detector sees a gradual onset.
  - **Threshold** — no deuterium: no photoneutrons from this reaction.
  - **Crossover** — photon energy far above the peak: the cross-section falls, to 0.5 mb by 22 MeV.

- **Emergent constant or stable output.** Photoneutrons and photoprotons above threshold, at a cross-section of order 1–2.5 mb between 2.6 and 4.5 MeV. In the reverse direction, a 2.223248 MeV line.

### 4.6 Internal Consistency Notes

The entry sits between [ionization-threshold](ionization-threshold.md) (electronvolt unbinding of an electron) and [pair-production](pair-production.md) (creation of a pair). [Muon-catalyzed fusion](muon-catalyzed-fusion.md) joins hydrogen nuclei with a muon present; this entry separates a deuteron with a photon.

Sourcing changed four things. The binding energy is now the measured value, 2.224566 MeV. The first version said the capture reaction returns a 2.224 MeV photon; the photon is 2.223248 MeV, because the recoiling deuteron keeps 1.3 keV, and for the same reason the photodisintegration threshold is 2.225885 MeV and not \(B_d\). The first version called \(B_d\) the measured mass defect; in practice the dependence runs the other way, and the neutron mass is derived from \(B_d\). The onset was described only as a cliff; the energy threshold is sharp, and the yield above it grows continuously from zero. A statement that the reaction served as a gamma-energy standard was dropped for lack of a source.

\(B_d\) is taken, not derived. QSA does not here derive the nuclear force.

For the [EM-LENR](../application/EM-LENR.md) application this entry fixes the scale of nuclear binding: 2.2 MeV per deuteron, and a thermal capture cross-section of 0.33 b, so free neutrons in hydrogenous material produce the 2.223 MeV line.

### 4.7 Overall Confidence in the QSA Mapping

**High** — a measured energy threshold on a two-body system translates directly into an energy gate and a one-deuteron buffer.

## Related entries

- [pair-production](pair-production.md) — creation gate; different product
- [ionization-threshold](ionization-threshold.md) — electronic unbinding of hydrogen
- [muon-catalyzed-fusion](muon-catalyzed-fusion.md) — fusion of hydrogen isotopes; needs a muon
- [photoelectric-threshold](photoelectric-threshold.md) — electronvolt surface unbinding

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Dewey and Kessler, *J. Res. Natl. Inst. Stand. Technol.* 105, 11 (2000)](https://nvlpubs.nist.gov/nistpubs/jres/105/1/j51dew.pdf) | full-text | Capture-line wavelength 5.57671299(99)e-13 m; binding energy 2 224 566.14(41) eV after recoil correction; neutron mass obtained from it. Reports the measurement of Kessler et al., *Phys. Lett. A* 255, 221 (1999), not opened. |
| S2 | [NIST CODATA 2022, deuteron mass energy equivalent in MeV](https://physics.nist.gov/cgi-bin/cuu/Value?mdc2mev) | full-text | Deuteron rest energy 1875.612945 MeV, used for the recoil terms. |
| S3 | [Jabs, arXiv:quant-ph/9604027 (1996)](https://arxiv.org/abs/quant-ph/9604027) | full-text | Secondary: threshold 2.226 MeV; near-threshold cross-section formula; maximum 2.5 mb at about 4.4 MeV and 0.5 mb at 22 MeV; magnetic-dipole term up to about 2.4 MeV. |
| S4 | [Ivanov, Oberhummer, Troitskaya and Faber, arXiv:nucl-th/0006051 (2000)](https://arxiv.org/abs/nucl-th/0006051) | full-text | Secondary: measured cross-sections at 2.62, 2.76 and 4.45 MeV; thermal capture cross-section 334.2 ± 0.5 mb. |
| S5 | [NBSIR 83-2647, "The photodisintegration of the deuteron, 1982" (National Bureau of Standards, 1983)](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nbsir83-2647.pdf) | full-text | Evaluation from threshold to 44 MeV: total cross-section peaks at 4.4 MeV; magnetic-dipole term peaks just above threshold and dominates up to 2.4 MeV. |
