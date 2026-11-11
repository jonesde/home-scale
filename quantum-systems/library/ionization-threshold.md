---
id: ionization-threshold
title: Ionization Threshold (Single-Particle Binding Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - thermal
confidence_data: high
confidence_mapping: high
review_depth: standard
related:
  - photoelectric-threshold
  - work-function-thermionic
  - x-ray-absorption-edge
  - semiconductor-gap-absorption
  - pair-production
  - dielectric-breakdown
  - plasma-frequency-cutoff
  - blackbody-spectrum
updated: 2026-11-11
---

# Ionization Threshold (Single-Particle Binding Gate)

### 4.1 Effect Name

Ionization threshold (single-particle binding gate)

### 4.2 Macroscopic Observation

A dilute gas remains electrically neutral under illumination or electron bombardment until the supplied energy reaches a species-specific ionization energy. Below that energy this channel furnishes no free charges; above it, ions and electrons appear (a photoionization continuum, the precursors of a discharge, a spectroscopic series limit). Cold atomic hydrogen is not ionized by light of wavelength longer than the Lyman limit and is ionized by shorter wavelengths.

### 4.3 Established Quantitative Boundaries

- **Model (calculated values in the NIST database).** Hydrogen, first ionization energy: 13.598434599702 eV, uncertainty 1.2 × 10⁻¹¹ eV. The one-electron ion He II: 54.4177655282 eV, uncertainty 1.0 × 10⁻⁹ eV. The database prints both in parentheses, read here as its marker for a calculated value [S1].
- **Measured.** Helium, first ionization energy: 24.587389011 eV, uncertainty 2.5 × 10⁻⁸ eV [S1]. Helium's two values are successive gates of one atom: 24.59 eV for the first electron and 54.42 eV for the second.
- **Measured.** Molecular hydrogen: evaluated ionization energy 15.42593 ± 0.00005 eV. Individual determinations run from 15.37 to 15.98 eV; the spectroscopic ones agree at 15.4256–15.4259 eV [S2].
- **Computed here.** The Lyman limit \(hc/I\) for hydrogen is 91.175 nm in vacuum, from the value above and the exact constants [S1][S3].
- **Computed here.** \(kT\) is 0.02585 eV at 300 K and 0.02526 eV at 293.15 K [S3], so \(I/kT\) for hydrogen is 526 and 538. \(I/k\) is 1.58 × 10⁵ K.
- **Model (Saha, ideal-gas ionization equilibrium).** Thermal ionization of a gas in equilibrium follows \(n_in_e/n_n \propto T^{3/2}\exp(-I/kT)\) [S4]. With \(I/kT\) above 500 the equilibrium ionized fraction of cold hydrogen is negligible.
- **Convention.** The ionization energy is the energy to remove the electron from the ground state of the species to rest at infinity. The electron-impact onset and the convergence of a Rydberg series on \(I\) are recorded in §4.4 as standard forms; no opened source was found for either.

**Data confidence:** High — the four values come from NIST databases opened on 2026-11-11. The helium and molecular-hydrogen values are measured optical limits. The hydrogen and He II values are calculated and are more precise than any direct measurement. The Saha form rests on a tertiary source.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Photoionization onset:

  \[
  h\nu \ge I,\qquad \mathrm{KE}_{e} = h\nu - I
  \]

- Electron-impact onset: projectile kinetic energy \(\ge I\). No opened source.
- Rydberg convergence (hydrogen-like), \(E_n = I(1 - 1/n^2) \to I\) as \(n \to \infty\). No opened source.
- Saha ionization equilibrium for a hot dilute gas, the thermal opening of the same gate [S4]:

  \[
  \frac{n_i n_e}{n_n}
  \propto T^{3/2}\exp\!\left(-\frac{I}{kT}\right)
  \]

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One atom or molecule is the hardware for one conversion. A macroscopic ionized gas is the summed output of a large population. No collective buffer has to be filled before a single ionization can happen. Density enters later: recombination, screening, and breakdown avalanches are many-body sequels.

- **Clock rate / latency.** No opening time is filed; no opened source gives one. The standard description puts photoionization on the optical cycle of the photon and electron-impact ionization on the collision time, both far below any laboratory clock. Recombination is the closing clock of the ionized state.

- **Energy barriers or thresholds.** The operating gate is the ionization energy \(I\) of the species and charge state: 13.598 eV for H, 15.426 eV for H₂, 24.587 eV for He, 54.418 eV for He⁺. Photons, projectiles, or a thermal tail are interchangeable opening resources for that one barrier.

- **Dominant failure modes.**
  - **Threshold** — photon or projectile energy below \(I\): the conversion does not occur and the neutral stays neutral in this channel.
  - **Crossover** — thermal opening: the equilibrium ionized fraction follows \(T^{3/2}\exp(-I/kT)\), with scale \(I/k = 1.58 \times 10^5\) K for hydrogen. There is no critical temperature; at 300 K the exponent is −526.
  - **Threshold** — missing species: an atom already stripped of that electron has lost that gate. A deeper one may remain (24.59 eV, then 54.42 eV, in helium).
  - **Crossover** — recombination: the ionized population decays when the drive is removed. It is not a latched state. No rate filed.

- **Emergent constant or stable output.** A species-specific series limit and a free-charge yield that turns on at \(I\), together with whatever plasma or chemical sequels the freed charges support.

### 4.6 Internal Consistency Notes

The mapping is the cleanest single-node member of the photoelectric-class family: one bound electron, one number, one gate. [Photoelectric-threshold](photoelectric-threshold.md) and [work-function-thermionic](work-function-thermionic.md) are the same unbinding, with the solid's work function in place of \(I\). [Semiconductor-gap-absorption](semiconductor-gap-absorption.md) is unbinding into a crystal band. [X-ray-absorption-edge](x-ray-absorption-edge.md) is the inner-shell rung of this ladder. [Pair-production](pair-production.md) is rest-mass creation and must not be folded into \(I\).

[Dielectric-breakdown](dielectric-breakdown.md) uses ionization as a microscopic step inside a field-driven avalanche. The present entry owns the single-particle gate; breakdown owns the many-body field condition.

Sourcing changed no number. It changed two statements. The first version described all four values as measured handbook numbers; the hydrogen and He II entries in the database are calculated, and the measured ones are helium and molecular hydrogen. The first version also listed the thermal case with the photon and projectile cases as one under-threshold cliff. The photon and projectile cases are thresholds; the thermal case is a crossover on the Saha form with no critical temperature.

A remaining gap: QSA takes \(I\) from the database. For hydrogen the calculated value is the closed description; for many-electron species the number is measured. The molecular onset depends on method: determinations of H₂ spread over 0.6 eV while the spectroscopic values agree to 0.3 meV.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(I\) is a precisely known single-particle energy gate, non-occurrence below it is the observed behaviour for photons and projectiles, and the family mapping is the same conversion as the photoelectric and X-ray edges.

## Related entries

- [photoelectric-threshold](photoelectric-threshold.md) — unbinding from a metal surface; \(\varphi\) in place of \(I\)
- [work-function-thermionic](work-function-thermionic.md) — the same surface unbinding, opened by heat
- [x-ray-absorption-edge](x-ray-absorption-edge.md) — inner-shell rung of the same ionization ladder
- [semiconductor-gap-absorption](semiconductor-gap-absorption.md) — unbinding into a crystal band at \(E_g\)
- [pair-production](pair-production.md) — rest-mass creation, not ionization of a pre-existing electron
- [dielectric-breakdown](dielectric-breakdown.md) — field-driven avalanche that uses this gate as a step
- [plasma-frequency-cutoff](plasma-frequency-cutoff.md) — collective response of the charge population after ionization
- [blackbody-spectrum](blackbody-spectrum.md) — thermal photon bath that may or may not sit above \(I\)

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Kramida, Ralchenko, Reader and NIST ASD Team, NIST Atomic Spectra Database ver. 5.12 (2024), Ionization Energies form](https://physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=H+I%2C+He+I%2C+He+II&units=1&format=1&order=0&at_num_out=on&sp_name_out=on&ion_charge_out=on&el_name_out=on&e_out=0&unc_out=on&biblio=on&submit=Retrieve+Data) | full-text | Ionization energies and uncertainties of H I, He I and He II; H I and He II printed as calculated values. Database output. |
| S2 | [NIST Chemistry WebBook, SRD 69, Hydrogen (H2), gas phase ion energetics data](https://webbook.nist.gov/cgi/cbook.cgi?ID=C1333740&Units=SI&Mask=20) | full-text | Evaluated ionization energy of H2 and the range of individual determinations. Database page. |
| S3 | [NIST, CODATA 2022 recommended values: Boltzmann constant (with the pages for h, c and e)](https://physics.nist.gov/cgi-bin/cuu/Value?k) | full-text | Exact constants used for the Lyman limit, kT and I/kT. |
| S4 | [Wikipedia, "Saha ionization equation"](https://en.wikipedia.org/wiki/Saha_ionization_equation) | full-text | Tertiary: the Saha form. The T to the 3/2 factor is read from the thermal de Broglie wavelength in its prefactor. |
