---
id: skin-effect
title: Skin Effect (Low-Frequency Screening Length)
status: formal
family: collective-field-response
constraints:
  - spatial-buffer
  - clock-latency
confidence_data: high
confidence_mapping: high
related:
  - reflection
  - plasma-frequency-cutoff
  - surface-plasmon-resonance
  - cyclotron-resonance
  - meissner
  - superconductivity
updated: 2026-08-17
---

# Skin Effect (Low-Frequency Screening Length)

### 4.1 Effect Name

Skin effect (low-frequency screening length)

### 4.2 Macroscopic Observation

An alternating current in a thick copper conductor is confined to a surface layer. The interior of a large bus-bar or coaxial outer carries little of the current; the AC resistance is higher than the DC resistance of the same metal. At zero frequency the current fills the cross-section uniformly. The metal requires no auxiliary power beyond the current itself.

### 4.3 Established Quantitative Boundaries

- Classical skin depth (local Ohm’s law, non-magnetic conductor):

  \[
  \delta = \sqrt{\frac{2}{\omega\mu\sigma}} = \frac{1}{\sqrt{\pi f\mu\sigma}}
  \]

- Room-temperature copper, handbook conductivity \(\sigma \approx 5.8\times 10^{7}\,\mathrm{S\,m^{-1}}\): \(\delta \approx 8.5\,\mathrm{mm}\) at \(60\,\mathrm{Hz}\); \(\approx 2.1\,\mathrm{mm}\) at \(1\,\mathrm{kHz}\); \(\approx 66\,\mu\mathrm{m}\) at \(1\,\mathrm{MHz}\); \(\approx 2\,\mu\mathrm{m}\) at \(1\,\mathrm{GHz}\). Silver and gold sit in the same millimetre-to-micrometre class at these frequencies.
- \(\omega\to 0\) sends \(\delta\to\infty\): DC current is uniform. A conductor whose radius or half-thickness \(a\ll\delta\) is an AC conductor with no skin/core contrast — the whole cross-section participates.
- Classical formula assumes a local conductivity, i.e. electron mean free path \(\ell \ll \delta\). When \(\ell\gtrsim\delta\) (high-purity metals at cryogenic temperature, microwave / radio frequencies) the regime is the *anomalous* skin effect: the local-\(\sigma\) length ceases to be the right buffer.
- Optical penetration in the same metals is \(\lambda/4\pi k\), already measured in [reflection](reflection.md) as \(\sim 10\)–\(20\,\mathrm{nm}\) in Ag/Al in the visible. That is not \(\sqrt{2/\omega\mu\sigma}\). Hagen–Rubens connects the infrared end of reflectance to \(\sigma\), but the optical formula is the one that applies once interband structure and the plasma edge matter.
- A superconductor replaces this dissipative skin with a static London depth (Meissner expulsion). That is a different length in a different family.

**Data confidence:** High — \(\delta(f)\) in ordinary metals is a standard, multiply reproduced engineering measurement. The existence of an anomalous regime at \(\ell\gtrsim\delta\) is high as a class; the numerical \(\ell\) of any one sample is medium (purity / temperature).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- From Maxwell plus local \(\mathbf{J}=\sigma\mathbf{E}\), the field in a thick conductor decays as \(e^{-z/\delta}e^{-iz/\delta}\) with \(\delta\) as above.
- AC resistance of a wire rises once \(a\) is no longer \(\ll\delta\); in the thick limit the effective cross-section is a ring of thickness \(\sim\delta\).
- Anomalous (extreme) skin depth scales more slowly with frequency than the classical square root (Reuter–Sondheimer class, \(\delta\sim\omega^{-1/3}\) in the extreme limit). The exponent is recorded as data for that regime, not used here as a derived node rule.
- Optical intensity penetration:

  \[
  \delta_{\mathrm{opt}} = \frac{\lambda}{4\pi k}
  \]

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A conducting volume at least of order \(\delta\) thick is required before a distinct screened interior exists. If the conductor is thinner than \(\delta\), the responding node count occupies the entire cross-section and the macroscopic “skin” is absent. \(\delta\) itself moves: millimetres at power frequencies, micrometres at radio frequencies, and — by a different formula — tens of nanometres optically. The buffer is the screening length, not a fixed millimetre.

- **Clock rate / latency.** The same free-electron population that completes an optical screening cycle on the plasma-period (femtosecond) scale screens a \(60\,\mathrm{Hz}\) field over millimetres. Raising \(\omega\) shrinks \(\delta\). The low-frequency clock constraint is magnetic diffusion / charge relaxation across the conductor, set by the measured \(\sigma\) and \(\mu\).

- **Energy barriers or thresholds.** None. This is a driven dissipative response, not a latch and not a gapped condensate.

- **Dominant failure modes.**
  - Temporal: \(\omega\to 0\) → \(\delta\) exceeds any laboratory conductor → uniform fill.
  - Spatial: conductor thickness \(\ll\delta\) → no skin/core contrast.
  - Local-response: \(\ell\gtrsim\delta\) → classical \(\delta\) is no longer the operating length (anomalous regime).
  - Material: collapse of \(\sigma\) (poor metal, high \(T\)) inflates \(\delta\) and weakens confinement. Not a sharp cliff.

- **Emergent constant or stable output.** A frequency-dependent confinement of AC current to a surface layer, and the associated rise in AC resistance, produced by collective screening in the conductor.

### 4.6 Internal Consistency Notes

This is the low-frequency end of the same free-electron screening machine as [reflection](reflection.md). Reflection fails when the film is thinner than the *optical* penetration depth, or when the drive outruns the plasma clock (`plasma-frequency-cutoff`). The skin effect fails when the conductor is thinner than the *classical* \(\delta\), or when the drive is too slow. Same family, different clock band, different measured length.

Three lengths must not be collapsed into one number:

1. classical \(\delta=\sqrt{2/\omega\mu\sigma}\) (local Ohm, \(\ell\ll\delta\));
2. anomalous penetration (\(\ell\gtrsim\delta\));
3. optical \(\lambda/4\pi k\) (already owned by reflection).

London \(\lambda\) is a fourth length and belongs to `meissner`. Using one word, “penetration depth,” for all four is an internal-consistency error.

QSA *takes* \(\sqrt{2/\omega\mu\sigma}\) as the buffer specification. It does not yet derive the square-root from a more primitive node count. That is the same class of gap recorded for the optical penetration depth: the length is measured, then used as the hardware spec.

[Cyclotron resonance](cyclotron-resonance.md) in metals (Azbel–Kaner) uses this skin layer as the only volume the microwave field occupies. The skin is the buffer; the cyclotron match is a different clock.

### 4.7 Overall Confidence in the QSA Mapping

**High** — conductor size versus \(\delta\), and \(\omega\to 0\), translate directly into a spatial buffer and a clock failure; the remaining work is keeping the three metallic lengths (and London \(\lambda\)) from being treated as one artifact.

## Related entries

- [reflection](reflection.md) — optical end of the same screening; penetration is \(\lambda/4\pi k\), not \(\sqrt{2/\omega\mu\sigma}\)
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — clock-failure twin of reflection; high-frequency end of this machine
- [surface-plasmon-resonance](surface-plasmon-resonance.md) — interface-bound mode of the same electrons; decay into the metal is the optical skin
- [cyclotron-resonance](cyclotron-resonance.md) — Azbel–Kaner CR is cyclotron motion sampled inside this skin layer
- [Meissner effect](meissner.md) — static, dissipationless expulsion; London \(\lambda\) is not this \(\delta\)
- [Superconductivity](superconductivity.md) — the condensate that replaces dissipative skin with Meissner screening
