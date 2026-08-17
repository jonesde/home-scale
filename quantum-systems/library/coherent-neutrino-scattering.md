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
related:
  - pair-production
  - deuteron-photodisintegration
updated: 2026-08-17
---

# Coherent Elastic Neutrino–Nucleus Scattering (CEνNS)

### 4.1 Effect Name

Coherent elastic neutrino–nucleus scattering (CEνNS)

### 4.2 Macroscopic Observation

A low-energy neutrino beam (spallation source, reactor) incident on a heavy nucleus produces a small nuclear recoil with a cross section that scales as the square of the neutron number, far above incoherent neutrino–nucleon scattering. The COHERENT collaboration (2017, CsI[Na] at the SNS) first observed the process. When the momentum transfer is large enough to resolve the nucleus (\(qR\gtrsim 1\)), coherence is lost and the \(N^{2}\) enhancement collapses. Inverse beta decay is a different, higher-threshold channel and is not this file.

### 4.3 Established Quantitative Boundaries

- Coherence condition (order-of-magnitude): \(qR\ll 1\). For a mid-mass nucleus (\(R\sim 5\)–\(6\,\mathrm{fm}\)) this keeps \(E_\nu\) in the tens-of-MeV class and below. SNS neutrinos used by COHERENT sit in that window; higher-energy beams leave the coherent envelope.
- Cross section (descriptive): \(\sigma\propto N^{2}E_\nu^{2}\) times a form factor that falls when \(qR\sim 1\). There is **no** rest-mass energy threshold of the inverse-beta-decay kind (1.8 MeV); the laboratory *detection* threshold is a recoil-energy floor of the calorimeter, not the process gate.
- Hardware: a neutrino plus a nucleus. Heavy \(N\) is capacity of the coherent amplitude, not a second cliff of the same kind as a 10 nm film.

**Data confidence:** High for existence (COHERENT and later CsI / Ar / Ge / Xe work). Recoil-threshold and form-factor details are medium per target.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms. Freedman’s coherent cross section and a nuclear form factor \(F(qR)\) describe the observed recoil rate. Below the coherence window \(F\to 1\); above it \(F\to 0\). These do not derive \(G_F\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One neutrino plus one nucleus. “Coherent” is a spatial-buffer condition on the momentum transfer versus nuclear size. Empty space, or a probe that resolves nucleons, is under-provisioned for this \(N^{2}\) channel.

- **Clock rate / latency.** Weak interaction; far below laboratory clocks. Detector integration is collection.

- **Energy barriers or thresholds.** The process itself has no 1.8 MeV IBD gate. The *coherence* gate is \(qR\ll 1\). Detector recoil threshold is an instrument floor, not the conversion cliff.

- **Dominant failure modes.**
  - Coherence: \(qR\gtrsim 1\) (too-hard neutrino) \(\to\) \(N^{2}\) channel collapses.
  - Missing nucleus: no target \(\to\) no recoil.
  - Wrong channel: IBD / quasielastic nucleon knockout is a different machine.
  - Detection: recoil below the calorimeter floor \(\to\) the process can still occur and not be *read*.

- **Emergent constant or stable output.** A nuclear-recoil rate enhanced as \(N^{2}\) in the coherent window, as the synchronized output of many independent \(\nu A\) events.

### 4.6 Internal Consistency Notes

The extra node is the neutrino (forced by this file). The nucleus is the same class of recoil partner as in [pair production](pair-production.md), used here as the *scatterer*, not as a pair-conversion sink.

No energy threshold of the pair-production kind is a real difference and is recorded: the collapse is loss of coherence, not under-threshold non-occurrence of a rest-mass gate. Mapping is Medium because the laboratory readout floor and the form-factor shape are target-dependent, while the \(N^{2}\) coherent envelope is not.

Do not identify this with a dark-matter “trail.” CEνNS is a measured Standard Model channel.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — existence and the coherence / \(N^{2}\) envelope are established; the detection floor is not the process gate, and \(G_F\) / the form factor are taken.

## Related entries

- [pair-production](pair-production.md) — another conversion that needs a nearby nucleus; different probe and product
- [deuteron-photodisintegration](deuteron-photodisintegration.md) — photon + few-nucleon target; an energy threshold, not a coherence window
