---
id: pair-production
title: Pair Production (Rest-Mass Conversion Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - spatial-buffer
confidence_data: high
confidence_mapping: high
related:
  - ionization-threshold
  - photoelectric-threshold
  - x-ray-absorption-edge
  - semiconductor-gap-absorption
  - blackbody-spectrum
  - plasma-frequency-cutoff
updated: 2026-08-17
---

# Pair Production (Rest-Mass Conversion Gate)

### 4.1 Effect Name

Pair production (rest-mass conversion gate)

### 4.2 Macroscopic Observation

A gamma-ray beam passing through matter produces electron–positron pairs once the photon energy is high enough, and only in the presence of a third body (almost always a nucleus) that can take up recoil momentum. Below that energy the pair channel is simply absent: no positrons, no subsequent \(511\,\mathrm{keV}\) annihilation line from this process. Cloud-chamber and spectrometer records show the pair tracks opening above the threshold and remaining closed below it. Isolated photons in empty space do not convert.

### 4.3 Established Quantitative Boundaries

- Rest energy of one electron (or positron): \(m_e c^2 = 510.999\,\mathrm{keV} \approx 511\,\mathrm{keV}\). The pair gate in the field of a heavy nucleus is

  \[
  E_\gamma^{\mathrm{th}} = 2 m_e c^2 = 1.022\,\mathrm{MeV}.
  \]

  (A finite nuclear mass \(M\) raises the exact kinematic threshold by a fractional correction of order \(m_e/M\), negligible for ordinary nuclei.)
- Pair production on an electron (triplet production) opens only at \(4 m_e c^2 = 2.044\,\mathrm{MeV}\). That is the same conversion with a lighter momentum sink.
- A photon in free space, with no nearby mass to recoil, cannot satisfy energy and momentum together; the channel remains closed at every energy. The “nearby nucleus” is a spatial-buffer condition, not a decorative remark.
- Above threshold the pair cross section rises from zero and, in high-\(Z\) matter, becomes the dominant attenuation channel at multi-MeV energies. The Bethe–Heitler description scales as \(Z^2\) (nuclear charge squared), which is why lead is a more efficient pair converter than carbon at the same mass thickness.
- The inverse conversion — annihilation of a stopped positron on an electron — returns two \(511\,\mathrm{keV}\) photons. That line is the macroscopic witness that a pair was produced.

**Data confidence:** High — \(2m_e c^2\), the nuclear-recoil requirement, the annihilation line, and the qualitative \(Z^2\) rise are textbook-stable facts. Detailed screened cross sections are high as a class and medium in any one approximate formula.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Energy gate (nuclear field, \(M \gg m_e\)):

  \[
  E_\gamma \ge 2 m_e c^2 = 1.022\,\mathrm{MeV}
  \]

- Kinematic prohibition in free space: a single photon cannot convert to \(e^+e^-\) while conserving four-momentum. A third body (nucleus, electron, or a second photon) is required.
- Bethe–Heitler pair production in a nuclear Coulomb field: a calculated cross section, starting from zero at threshold, rising with \(E_\gamma\), and proportional to \(Z^2\) (with screening corrections at high energy). The formula is a fit of QED perturbation theory to the observed channel, not an extra postulate.
- Two-photon annihilation at rest:

  \[
  e^+ + e^- \;\to\; 2\gamma,\qquad E_\gamma = m_e c^2 = 511\,\mathrm{keV}
  \]

Below \(1.022\,\mathrm{MeV}\), or in the absence of a momentum sink, this conversion does not occur. That non-occurrence is the collapse of the effect. Photoelectric absorption and Compton scattering may still remove photons; they are other channels.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One photon plus one nearby nucleus (or other recoil partner) is the hardware for one conversion. “Nearby” is a real spatial constraint: the photon must pass through the Coulomb field of a mass that can recoil. A macroscopic conversion rate then scales with the nuclear column density. Empty space, however energetic the photon, is under-provisioned: the spatial buffer is missing and the channel stays closed.

- **Clock rate / latency.** The conversion, when allowed, is a high-energy QED process on timescales far below any laboratory clock. Subsequent slowing of the pair and annihilation are later steps with their own (still short) latencies. They witness the conversion; they are not the gate.

- **Energy barriers or thresholds.** The operating gate is the rest-mass sum \(2m_e c^2\). It is not the unbinding of a pre-existing electron. No amount of infrared light, and no optical photoelectric event, opens this channel.

- **Dominant failure modes.**
  - Under-threshold: \(E_\gamma < 1.022\,\mathrm{MeV}\) → pair conversion does not occur.
  - Spatial: no nearby nucleus (or other recoil partner) → the channel remains closed even for \(E_\gamma > 1.022\,\mathrm{MeV}\).
  - Wrong partner: an electron as the only recoil partner keeps the gate shut until \(2.044\,\mathrm{MeV}\).
  - Competition: at a given energy the photon may Compton-scatter or photoabsorb instead. That lowers the pair *yield*; it does not move the pair threshold.

- **Emergent constant or stable output.** A material- and energy-dependent pair yield above \(1.022\,\mathrm{MeV}\), followed by the \(511\,\mathrm{keV}\) annihilation line, as the synchronized output of many independent photon–nucleus conversions.

### 4.6 Internal Consistency Notes

This is the sharpest textbook member of the threshold-conversion family: a single number fixed by a measured rest mass, plus an equally sharp spatial clause. The mapping closes without remainder on those two constraints.

It must not be confused with [ionization-threshold](ionization-threshold.md) or [photoelectric-threshold](photoelectric-threshold.md). Those unbind an electron that already exists. Pair production *creates* a charge pair and is forbidden below \(2m_e c^2\) even in a fully ionized plasma. [X-ray-absorption-edge](x-ray-absorption-edge.md) sits on the way up in photon energy and is a different gate (inner-shell binding, keV, no positron).

A remaining gap: QSA takes \(m_e c^2 = 511\,\mathrm{keV}\) as a measured node specification. It does not here derive the electron mass from a more primitive resource count. The collapse clauses (\(E_\gamma < 1.022\,\mathrm{MeV}\); no recoil partner) do not depend on that derivation. Two-photon pair production in an intense photon bath is a real additional opening of the same rest-mass gate; it is not required to state the nuclear-field case and is left as a noted extension.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the \(1.022\,\mathrm{MeV}\) cliff and the nuclear-recoil requirement are among the cleanest measured gates in the library and translate directly into an energy threshold plus a spatial-buffer condition.

## Related entries

- [ionization-threshold](ionization-threshold.md) — unbinding of a pre-existing electron; a different gate at a different energy
- [photoelectric-threshold](photoelectric-threshold.md) — surface unbinding, eV scale; no positron
- [x-ray-absorption-edge](x-ray-absorption-edge.md) — inner-shell photoelectric channel that competes with pairs at keV–MeV
- [semiconductor-gap-absorption](semiconductor-gap-absorption.md) — eV-scale interband conversion; same family, different hardware
- [blackbody-spectrum](blackbody-spectrum.md) — a thermal photon population; ordinary temperatures sit far below \(2m_e c^2\)
- [plasma-frequency-cutoff](plasma-frequency-cutoff.md) — collective response of charges *after* they exist; not a rest-mass gate
