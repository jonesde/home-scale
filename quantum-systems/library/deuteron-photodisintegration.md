---
id: deuteron-photodisintegration
title: Deuteron Photodisintegration (2.224 MeV Unbinding Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
confidence_data: high
confidence_mapping: high
related:
  - pair-production
  - ionization-threshold
  - muon-catalyzed-fusion
  - photoelectric-threshold
updated: 2026-08-17
---

# Deuteron Photodisintegration (2.224 MeV Unbinding Gate)

### 4.1 Effect Name

Deuteron photodisintegration (2.224 MeV unbinding gate)

### 4.2 Macroscopic Observation

A gamma-ray beam on a deuterium target produces a proton and a neutron only when the photon energy exceeds the deuteron binding energy. Below that energy the two-body photodisintegration channel is closed: no photoneutrons from this process. The channel was used historically as a gamma-energy standard and remains a clean nuclear unbinding gate.

### 4.3 Established Quantitative Boundaries

- Deuteron binding energy / photodisintegration threshold:

  \[
  E_\gamma^{\mathrm{th}} = B_d = 2.224\,\mathrm{MeV}.
  \]

- Below \(B_d\) the \(\gamma + d \to p + n\) channel does not occur. Other photon processes (Compton on the electron cloud, pair production above 1.022 MeV) may still remove photons; they are different gates.
- The inverse capture \(p+n\to d+\gamma\) returns a 2.224 MeV photon; that line witnesses the same binding.

**Data confidence:** High — \(B_d = 2.224\,\mathrm{MeV}\) is a nuclear-data standard. Detailed angular distributions are high as a class.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

\[
\gamma + d \;\to\; p + n, \qquad E_\gamma \ge B_d = 2.224\,\mathrm{MeV}.
\]

Below threshold the channel is absent. The formula is the measured mass defect of the deuteron, not an extra postulate.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One photon plus one deuteron. Macroscopic yield scales with deuterium column density. No metal film and no muon.

- **Clock rate / latency.** Nuclear photodisintegration is far below any laboratory clock. Collection of \(p\) or \(n\) is a later step.

- **Energy barriers or thresholds.** \(B_d = 2.224\,\mathrm{MeV}\) is the load-bearing gate. It is an unbinding of a pre-existing \(pn\) bound state, not pair creation and not electronic ionization (\(I_{\mathrm{H}} = 13.6\,\mathrm{eV}\)).

- **Dominant failure modes.**
  - Under-threshold: \(E_\gamma < 2.224\,\mathrm{MeV}\) \(\to\) this channel closed.
  - Missing target: no deuterium \(\to\) no photoneutrons from this gate.
  - Competition: Compton / pair production can remove photons above their own gates without opening this one.

- **Emergent constant or stable output.** A photoneutron / photoproton yield above \(2.224\,\mathrm{MeV}\), as the synchronized output of many independent \(\gamma d\) conversions.

### 4.6 Internal Consistency Notes

Sits cleanly between [ionization-threshold](ionization-threshold.md) (eV electronic unbinding) and [pair-production](pair-production.md) (1.022 MeV *creation*). [Muon-catalyzed fusion](muon-catalyzed-fusion.md) *fuses* hydrogen isotopes with a muon present; this file *unbinds* a deuteron with a photon. Opposite arrows, same two nucleons.

\(B_d\) is taken from the measured mass defect. QSA does not here derive the nuclear force.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the 2.224 MeV cliff is among the cleanest nuclear gates and translates directly into an energy threshold plus a one-deuteron buffer.

## Related entries

- [pair-production](pair-production.md) — 1.022 MeV creation gate; different product
- [ionization-threshold](ionization-threshold.md) — electronic unbinding of H
- [muon-catalyzed-fusion](muon-catalyzed-fusion.md) — the fusion-direction hydrogen gate; needs a muon
- [photoelectric-threshold](photoelectric-threshold.md) — eV surface unbinding
