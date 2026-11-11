---
id: coherent-neutrino-scattering
title: Coherent Elastic Neutrino–Nucleus Scattering (CEνNS)
status: formal
family: threshold-conversion
constraints:
  - spatial-buffer
  - energy-barrier
confidence_data: high
confidence_mapping: medium
review_depth: light
related:
  - pair-production
  - deuteron-photodisintegration
updated: 2026-11-11
---

# Coherent Elastic Neutrino–Nucleus Scattering (CEνNS)

### 4.1 Effect Name

Coherent elastic neutrino–nucleus scattering (CEνNS)

### 4.2 Macroscopic Observation

A low-energy neutrino scatters from a whole nucleus and leaves a small nuclear recoil. The cross section grows with the square of the neutron number, which makes it the largest low-energy neutrino coupling. It has been observed with neutrinos of 16–53 MeV from a spallation source and with reactor antineutrinos. As the neutrino energy rises the nucleus is resolved and the enhancement is gradually lost. The interaction has no energy threshold; what limits its observation is the size of the recoil.

### 4.3 Established Quantitative Boundaries

- **Model (Standard Model neutral current).** Predicted in 1974 as a coherent forward peak in neutrino–nucleus elastic scattering [S1]. For momentum transfer \(q\) and nuclear radius \(R\) with \(qR < 1\) the nucleus responds as a whole and the interaction probability rises with the square of the number of neutrons; this restricts the process to neutrino energies below a few tens of MeV [S2].
- **Measured.** First observation: a 14.6 kg CsI[Na] scintillator at the Spallation Neutron Source, 6.7 σ, with 134 ± 22 events observed against 173 ± 48 predicted. The neutrinos were 30 MeV prompt \(\nu_\mu\) and a delayed spectrum ending near 53 MeV; the measurement covered about 16–53 MeV, the lower bound set by the lowest measured recoil energy [S2].
- **Measured.** Argon: more than 3 σ, with a flux-averaged cross section of (2.2 ± 0.7) × 10⁻³⁹ cm². Its neutron-number dependence, with the CsI result, confirms the process [S3].
- **Measured.** Reactor antineutrinos: germanium detectors 20.7 m from a 3.6 GW core recorded 395 ± 106 events in 119 days against 347 ± 59 predicted, 3.7 σ. The lowest detector threshold was 160 eV of ionization energy and the fit window was 160–800 eV [S4].
- **Model (Standard Model).** Above about 10 MeV there is a transition from the fully coherent to the partially coherent regime, and nuclear-structure uncertainties enter [S4]. The spallation-source measurement carries a 5 % form-factor uncertainty [S2]. The interaction itself has no energy threshold, so neutrinos below the inverse-beta-decay threshold of about 1.8 MeV could in principle be measured [S4].
- **Computed here.** Inverse beta decay on a free proton has a threshold of \(((m_n + m_e)^2 - m_p^2)/2m_p = 1.806\) MeV [S5].
- **Computed here.** Elastic kinematics give a maximum recoil energy \(2E_\nu^2/(M + 2E_\nu)\). For germanium (72.63 u) it is 96 eV at 1.8 MeV and 1.9 keV at 8 MeV; for caesium (132.9 u) it is 14.5 keV at 30 MeV [S5]. A 96 eV recoil is below the 160 eV ionization threshold of [S4] before any loss to quenching, so the reactor signal comes from neutrinos well above 1.8 MeV.
- **Computed here.** \(N^2\) is 6084 for ¹³³Cs (\(N = 78\)) and 484 for ⁴⁰Ar (\(N = 22\)), a ratio of 12.6.

**Data confidence:** High for existence, in three targets and two kinds of source. The quoted uncertainties of the three results are 16–32 %. No opened measurement uses neutrinos below 1.8 MeV, and no opened source gives the form factor as a function.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Coherent cross section: proportional to \(N^2\) for \(qR < 1\) [S2], reduced at larger momentum transfer by a nuclear form factor, which the analyses take from nuclear models [S2][S4].
- Maximum recoil energy of a nucleus of mass \(M\):

  \[
  T_\mathrm{max} = \frac{2E_\nu^2}{M + 2E_\nu}
  \]

These describe the observed recoil rate. They do not derive the weak coupling.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One neutrino and one nucleus. Coherence is a condition on the momentum transfer against the nuclear size. A heavier nucleus raises the amplitude as \(N^2\) and lowers the recoil energy as \(1/M\).

- **Clock rate / latency.** No interaction time was sourced. Detector integration is collection.

- **Energy barriers or thresholds.** The process has no energy threshold. Inverse beta decay, a different channel, has one at 1.806 MeV. The coherence condition \(qR < 1\) is a window in momentum transfer, full below about 10 MeV. The recoil threshold of a detector is an instrument floor.

- **Dominant failure modes.**
  - **Crossover** — coherence: the form factor falls continuously as \(qR\) grows; coherence is full below about 10 MeV and partial at the 16–53 MeV of the spallation-source measurements, where the \(N^2\) signal is still observed.
  - **Threshold** — no nucleus: no recoil.
  - **Crossover** — detection: the recoil energy scales as \(E_\nu^2/M\) (96 eV for 1.8 MeV on germanium), so a detector floor removes the low-energy part of a spectrum. The process still occurs unread.
  - **Threshold** — channel identity: inverse beta decay opens at 1.806 MeV. That gate belongs to another machine.

- **Emergent constant or stable output.** A nuclear-recoil rate that scales as \(N^2\) while coherence holds.

### 4.6 Internal Consistency Notes

The extra node is the neutrino. The nucleus is the same class of partner as in [pair production](pair-production.md), used here as the scatterer.

Sourcing changed three things. The first version placed the spallation-source neutrinos inside the window \(qR \ll 1\); at 16–53 MeV they are in the partially coherent regime, and full coherence holds below about 10 MeV, which is the reactor range. The loss of coherence is a crossover through a form factor, with no collapse at \(qR \approx 1\). And the process has now been observed with reactor antineutrinos, which the first version did not record. The contrast with a thickness cliff in a metal film is removed; no such cliff exists.

The absence of an energy threshold is a Standard Model statement that the measurements do not yet test below 1.8 MeV: every detected recoil so far requires a neutrino of higher energy. The mapping is Medium because the readout floor and the form factor depend on the target, and because the weak coupling and the form factor are taken.

CEνNS is a measured Standard Model channel and is not to be identified with a dark-matter signal.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — existence and the \(N^2\) scaling are established in three targets; the coherence limit is a crossover, the detection floor is not the process gate, and the threshold-free claim is untested below 1.8 MeV.

## Related entries

- [pair-production](pair-production.md) — another conversion that needs a nearby nucleus; different probe and product
- [deuteron-photodisintegration](deuteron-photodisintegration.md) — photon + few-nucleon target; an energy threshold, not a coherence window

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Freedman, "Coherent effects of a weak neutral current", *Phys. Rev. D* 9, 1389 (1974)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.9.1389) | abstract | Prediction of a coherent forward peak in neutrino–nucleus elastic scattering. |
| S2 | [COHERENT Collaboration, "Observation of coherent elastic neutrino-nucleus scattering", *Science* 357, 1123 (2017), arXiv:1708.01294](https://arxiv.org/pdf/1708.01294) | full-text | 6.7 σ in 14.6 kg CsI[Na]; 134 ± 22 observed and 173 ± 48 predicted; qR < 1 and N² scaling; 30 MeV prompt neutrinos, 16–53 MeV range; 5 % form-factor uncertainty. |
| S3 | [COHERENT Collaboration, "First measurement of coherent elastic neutrino-nucleus scattering on argon", arXiv:2003.10630](https://arxiv.org/abs/2003.10630) | abstract | Greater than 3 σ; flux-averaged cross section (2.2 ± 0.7) × 10⁻³⁹ cm²; neutron-number dependence with CsI. |
| S4 | [Ackermann et al. (CONUS+), "Direct observation of coherent elastic antineutrino-nucleus scattering", arXiv:2501.05206 (2025)](https://arxiv.org/pdf/2501.05206) | full-text | 3.7 σ; 395 ± 106 against 347 ± 59 in 119 days; 20.7 m from a 3.6 GW core; 160 eV threshold; fully against partially coherent regime near 10 MeV; no threshold for the interaction. Journal reference not opened. |
| S5 | [NIST, CODATA 2022 recommended values: neutron mass energy equivalent in MeV (with the proton, electron and atomic-mass-constant pages, and the NIST atomic-weights pages for Ge and Cs)](https://physics.nist.gov/cgi-bin/cuu/Value?mnc2mev) | full-text | Masses for the inverse-beta-decay threshold and the recoil energies. |
