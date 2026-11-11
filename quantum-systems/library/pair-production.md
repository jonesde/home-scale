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
review_depth: light
related:
  - ionization-threshold
  - photoelectric-threshold
  - muon-catalyzed-fusion
  - x-ray-absorption-edge
  - semiconductor-gap-absorption
  - blackbody-spectrum
  - plasma-frequency-cutoff
updated: 2026-11-11
---

# Pair Production (Rest-Mass Conversion Gate)

### 4.1 Effect Name

Pair production (rest-mass conversion gate)

### 4.2 Macroscopic Observation

A gamma-ray beam passing through matter produces electron–positron pairs once the photon energy exceeds twice the electron rest energy, and only where a second body, almost always a nucleus, takes up recoil momentum. Below that energy the channel is absent from the attenuation tables. Above it the pair cross section rises from zero and, in heavy elements, becomes the largest contribution to attenuation at a few MeV.

### 4.3 Established Quantitative Boundaries

- **Measured.** Electron rest energy \(m_ec^2 = 0.51099895069\) MeV [S1].
- **Computed here.** Energy and momentum conservation give a threshold of \(2m_ec^2(1 + m_e/M)\) for a photon converting in the field of a body of mass \(M\) at rest. For a heavy nucleus this is 1.0220 MeV; the recoil term adds 0.56 keV for a proton and 47 eV for ¹²C [S1]. For an electron as the partner (\(M = m_e\)) it is \(4m_ec^2 = 2.0440\) MeV. As \(M \to 0\) the threshold diverges: a single photon with no partner cannot convert at any energy.
- **Model (NIST XCOM evaluated cross sections).** In lead the nuclear-field pair coefficient is zero at 1.022 MeV, 3.3 × 10⁻⁸ cm² g⁻¹ at 1.03 MeV, 1.8 × 10⁻³ at 1.5 MeV and 3.67 × 10⁻² at 10 MeV. The electron-field coefficient is zero at 2.044 MeV and 4.8 × 10⁻⁹ cm² g⁻¹ at 2.1 MeV [S2].
- **Computed here.** From the same tables, pair production is 3.5 % of the total attenuation of lead at 1.5 MeV. Pair production (both fields) equals incoherent scattering at about 4.7 MeV in lead and about 26 MeV in carbon. At 10 MeV the nuclear-field coefficient per unit mass is 9.5 times larger in lead than in carbon.
- **Model (Tsai; Bethe–Heitler with screening).** The high-energy pair and bremsstrahlung cross sections carry a leading term in \(Z^2\) from the nucleus and a term in \(Z\) from the atomic electrons; at high energy photons lose energy predominantly by pair production [S3].
- **Measured.** The positron: 15 tracks of positive particles in 1300 cloud-chamber photographs of cosmic rays, with a mass under twenty electron masses [S4].
- **Measured.** Two photons can supply the partner for each other. 6085 exclusive electron–positron pairs were observed in ultra-peripheral Au+Au collisions, with features consistent with the collision of two photons from the fields of the nuclei [S5].
- **Computed here.** Annihilation of a pair at rest into two photons gives each photon \(m_ec^2\), 511.0 keV [S1].

**Data confidence:** High — the thresholds follow from the measured electron mass and are reproduced in the evaluated tables. The cross sections are evaluated theory checked against experiment, not single measurements.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Threshold in the field of a mass \(M\):

  \[
  E_\gamma^\mathrm{th} = 2m_ec^2\left(1 + \frac{m_e}{M}\right)
  \]

- A single photon has zero invariant mass and a pair has at least \(2m_e\), so conversion needs a second body: a nucleus, an electron or another photon.
- Bethe–Heitler cross section in a nuclear Coulomb field: zero at threshold, rising with energy, leading term \(Z^2\) with screening corrections [S3].
- Annihilation at rest: \(e^+ + e^- \to 2\gamma\) with \(E_\gamma = m_ec^2\).

Below threshold, or with no partner, the conversion does not occur. Photoelectric absorption and scattering still remove photons.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One photon and one partner that can recoil. The rate in matter scales with the column density of nuclei and with \(Z^2\). A photon alone is under-provisioned at every energy. No length for "nearby" is filed.

- **Clock rate / latency.** No conversion time was sourced. The slowing of the pair and the annihilation of the positron are later steps that witness the conversion.

- **Energy barriers or thresholds.** The operating gate is the rest energy of the pair, 1.0220 MeV with a nucleus. It is not the unbinding of an existing electron.

- **Dominant failure modes.**
  - **Threshold** — photon energy below \(2m_ec^2(1 + m_e/M)\): no conversion. The threshold is kinematic and exact. The yield has no step: the lead coefficient is 3.3 × 10⁻⁸ cm² g⁻¹ at 1.03 MeV and rises continuously.
  - **Threshold** — no recoil partner: the channel is closed at every energy.
  - **Threshold** — an electron as the only partner: closed below 2.0440 MeV.
  - **Crossover** — competition: the pair share of attenuation grows continuously, 3.5 % in lead at 1.5 MeV, and passes incoherent scattering at about 4.7 MeV in lead and 26 MeV in carbon.

- **Emergent constant or stable output.** A pair yield above 1.022 MeV that depends on material and energy, followed by the 511 keV annihilation line.

### 4.6 Internal Consistency Notes

The gate is fixed by one measured rest mass and one kinematic clause, and the mapping closes on those two constraints. Unlike [ionization-threshold](ionization-threshold.md) and [photoelectric-threshold](photoelectric-threshold.md), which unbind an electron that already exists, this conversion creates the charge pair. [X-ray-absorption-edge](x-ray-absorption-edge.md) is a different gate at keV.

Sourcing changed no number; the thresholds, the recoil clause and the \(Z^2\) scaling are confirmed. Three statements are sharper. The threshold is a threshold in existence, with a yield that starts at zero, so there is no jump in attenuation at 1.022 MeV. "Dominant at multi-MeV" is now a crossover energy, 4.7 MeV in lead and 26 MeV in carbon. The two-photon case, left as an extension in the first version, has been observed. The reference to cloud-chamber records of the threshold is dropped; the opened source establishes the positron, not the threshold.

QSA takes \(m_ec^2\) as a measured node specification and does not derive it.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the 1.022 MeV threshold and the recoil requirement follow from a measured mass and conservation laws, and translate directly into an energy threshold plus a partner condition.

## Related entries

- [muon-catalyzed-fusion](muon-catalyzed-fusion.md) — another conversion that stays closed without a named extra node (here a muon, not a recoil nucleus)
- [ionization-threshold](ionization-threshold.md) — unbinding of a pre-existing electron; a different gate at a different energy
- [photoelectric-threshold](photoelectric-threshold.md) — surface unbinding, eV scale; no positron
- [x-ray-absorption-edge](x-ray-absorption-edge.md) — inner-shell photoelectric channel that competes with pairs at keV–MeV
- [semiconductor-gap-absorption](semiconductor-gap-absorption.md) — eV-scale interband conversion; same family, different hardware
- [blackbody-spectrum](blackbody-spectrum.md) — a thermal photon population; ordinary temperatures sit far below \(2m_e c^2\)
- [plasma-frequency-cutoff](plasma-frequency-cutoff.md) — collective response of charges *after* they exist; not a rest-mass gate

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [NIST, CODATA 2022 recommended values: electron mass energy equivalent in MeV (with the pages for the proton and the atomic mass constant)](https://physics.nist.gov/cgi-bin/cuu/Value?mec2mev) | full-text | Electron rest energy; proton and ¹²C masses for the recoil term. |
| S2 | [Berger et al., XCOM: Photon Cross Sections Database, NIST Standard Reference Database 8](https://physics.nist.gov/cgi-bin/Xcom/xcom2?Method=Elem&Output2=Hand) | full-text | Evaluated coefficients for lead and carbon, 0.5–100 MeV: pair production in the nuclear and electron fields, incoherent scattering, totals. Values read from the generated tables. |
| S3 | [Particle Data Group, "Passage of Particles Through Matter", *Review of Particle Physics* (2024)](https://pdg.lbl.gov/2024/reviews/rpp2024-rev-passage-particles-matter.pdf) | full-text | High-energy photons lose energy mainly by pair production; Z² and Z terms in Tsai's formula; nuclear-field and electron-field pair channels. |
| S4 | [Anderson, "The Positive Electron", *Phys. Rev.* 43, 491 (1933)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.43.491) | abstract | 15 positive tracks in 1300 photographs; mass under twenty electron masses. |
| S5 | [STAR Collaboration, arXiv:1910.12400 (2019), on electron–positron pairs from photon collisions in Au+Au](https://arxiv.org/abs/1910.12400) | abstract | 6085 exclusive pairs in ultra-peripheral Au+Au collisions, consistent with the Breit–Wheeler process. Journal reference not opened. |
