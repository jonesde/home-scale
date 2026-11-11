---
id: casimir-force
title: Casimir Force (Mode-Cutoff Attraction)
status: formal
family: collective-field-response
constraints:
  - spatial-buffer
  - thermal
confidence_data: high
confidence_mapping: medium
review_depth: standard
related:
  - reflection
  - blackbody-spectrum
  - total-internal-reflection
updated: 2026-11-11
---

# Casimir Force (Mode-Cutoff Attraction)

### 4.1 Effect Name

Casimir force (mode-cutoff attraction)

### 4.2 Macroscopic Observation

Two uncharged conducting plates, or a sphere and a plate, brought to sub-micrometre separation attract. The force is not Coulomb attraction of charge and is not gravity. It falls rapidly as the gap opens. It has been measured from about 50 nm to 7 µm. Faces that are thin, or transparent in the visible, give a smaller force and not a zero one.

### 4.3 Established Quantitative Boundaries

- **Model (perfect conductors at zero temperature).** Parallel-plate pressure \(P = \pi^2\hbar c/240d^4 = K_C/d^4\), with \(K_C = \pi hc/480 = 1.3 \times 10^{-27}\) N m² [S1].
- **Computed here.** \(K_C = 1.300 \times 10^{-27}\) N m², so the ideal pressure is 1.30 mPa at \(d = 1\) µm and 13.0 Pa at 0.1 µm.
- **Measured.** Parallel plates: \(K_C = (1.22 \pm 0.18) \times 10^{-27}\) N m² for gaps of 0.5–3.0 µm, a precision of 15 %. The faces were silicon coated with 50 nm of chromium [S1]. The measured coefficient is 0.94 of the ideal one, inside its uncertainty.
- **Measured.** Sphere and plate. A torsion pendulum covered 0.6–6 µm and reported agreement with theory at the 5 % level [S2]; a later review finds that figure incompatible with the size of the thermal correction above 2 µm [S3]. An atomic force microscope covered 0.1–0.9 µm, with a deviation of 1 % at the smallest separation [S4]. A torsion balance covered 0.7–7 µm [S5]. Shorter ranges, about 50–150 nm and 70–400 nm, are in [S8] and [S9].
- **Model (proximity-force approximation).** For a sphere and a plate the force goes as \(1/d^3\); thin-film data were fitted with \(C/d^3\) over 100–300 nm [S7].
- **Model (Lifshitz theory with tabulated optical data).** Thick real metals fall short of the ideal force at short gaps. The force is 0.48 of ideal for Au and Cu and 0.55 for Al at 0.1 µm, 0.81 and 0.85 at 0.5 µm, and about 0.96 at 3 µm [S6].
- **Measured.** A thin metal face. A sphere coated with 29 ± 2 Å of titanium and 92 ± 3 Å of palladium, against a thick Au plate, gives a force smaller than the same sphere after a further 2000 Å of palladium. The thin-film force is present and follows \(C/d^3\); theory and experiment for it differ by about 17 %. The size of the reduction is not stated as a number in the text. A film is thinner than the relevant skin depth below about 100 Å for common metals [S7].
- **Measured.** A face transparent in the visible. An Au sphere against 190 nm of indium tin oxide on glass, in air, gives a force gradient about 40–50 % smaller than Au against Au at all separations from about 50 to 150 nm [S8].
- **Measured.** A face switched from reflecting to transparent. With a hydrogen-switchable mirror on the sphere and an Au plate, at about 70–400 nm, no significant difference in force was observed between the reflecting and the transparent state [S9].
- **Model (Lifshitz theory).** The force is governed by the response of the faces around a characteristic frequency \(\omega_c = c/2d\) and integrates over a wide band, so a transparency window confined to the visible and near infrared does not substantially alter it [S3][S9].
- **Computed here.** \(\hbar c/2d\) is 0.99 eV at \(d = 100\) nm and 0.10 eV at 1 µm (\(\hbar c/d\): 1.97 eV and 0.20 eV). At laboratory gaps the characteristic energy lies in the infrared, and the force draws on the response of the faces over a wide band around it; a window of transparency in the visible and near infrared is one part of that band.
- **Computed here.** The thermal length \(\hbar c/kT\) is 7.6 µm at 300 K. The first version gave "tens of micrometres".
- **Measured.** The thermal contribution dominates above about 3 µm at 300 K [S5], and the high-temperature limit is reached at 6 µm and above [S3].

**Data confidence:** High as a class — the attraction, its steep dependence on gap and its reduction by real and thin faces are each measured by more than one group. The first torsion-pendulum result [S2] was read as an abstract, and its 5 % claim is disputed. No measurement on an islanded metal film below percolation was found. No source on the limits set by roughness or electrostatic patch potentials was opened in this pass, so the first version's statements about them are not carried in §4.3.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms. \(P = \pi^2\hbar c/240d^4\) is the perfect-conductor, zero-temperature result [S1]. Sphere and plate use the proximity-force reduction, \(F \propto 1/d^3\) [S7]. Real faces enter through Lifshitz theory, which takes the dielectric function of each face over a band around \(\omega_c = c/2d\) [S3][S6]. These describe the observed attraction. They do not derive \(\hbar\) from a node count.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two faces with an electromagnetic contrast, separated by a gap of 0.05–7 µm for a measured force. The resource is the gap. The faces need not be a thick metal: 9 nm of palladium, or a conducting oxide that is transparent in the visible, still gives a force. No minimum face thickness is measured.

- **Clock rate / latency.** The characteristic frequency \(c/2d\), an energy of 0.1–1 eV at gaps of 1–0.1 µm. This is below the plasma edge of the metal. The force integrates the response of the faces over a wide band around that frequency, so transparency in one part of the band removes only part of the force.

- **Energy barriers or thresholds.** No latch. The force is an output of the geometry and the response of the faces. Nothing is stored.

- **Dominant failure modes.**
  - **Crossover** — gap: \(1/d^4\) for plates and \(1/d^3\) for a sphere and plate. No critical gap; the largest measured is 7 µm.
  - **Crossover** — conducting contrast of the faces: the force falls continuously below the perfect-conductor value. Thick Au, Cu or Al gives 0.48–0.55 of it at 0.1 µm; a 9 nm palladium film gives less than a thick one; indium tin oxide gives about half the Au value at 50–150 nm. It does not reach zero in any measurement found.
  - **Crossover** — temperature: a thermal contribution grows with gap on the scale \(\hbar c/kT = 7.6\) µm at 300 K and dominates above about 3 µm.
  - **Crossover** — roughness, tilt and electrostatic patches: these compete with the force at a given gap. No measured scale is filed.

- **Emergent constant or stable output.** An attractive force of the Casimir–Lifshitz class in \(d\), reduced from the ideal value by the real response of the faces.

### 4.6 Internal Consistency Notes

This is not the optical mirror of [reflection](reflection.md): the output is a force set by the gap and by the response of the faces over a wide band centred in the infrared, not a re-radiated beam.

Sourcing changed the entry in four places. The first version said conducting, optically reflecting faces are required, that the faces "must still be conducting on their own screening depth", and that starving them of conductivity is "a real collapse". The measurements show a reduction: a film thinner than the skin depth gives a smaller force, a visibly transparent conducting oxide gives about half, and a mirror switched to transparent gave no measurable change. The stated reason is that the force depends on the response over a wide band around \(c/2d\), which at these gaps is centred in the infrared, so a window of transparency in the visible and near infrared removes only part of it. Second, even thick real metals give about half the ideal force at 0.1 µm, so the ideal number is approached only at gaps of micrometres. Third, the thermal length at 300 K is 7.6 µm. Fourth, the 5 % agreement of the first torsion-pendulum measurement is disputed above 2 µm.

One prediction that leaned on this entry is affected. A film that has lost its visible reflectance is not thereby expected to lose the force. The case of an islanded film below percolation is untested.

The mapping takes \(\pi^2\hbar c/240d^4\) from the mode sum. That is the same class of taken output as taking \(\delta = \lambda/4\pi k\) for a metal. The number is not derived from a node rule.

The dynamical Casimir effect, photons from a modulated boundary, was observed in a transmission line terminated by a superconducting quantum interference device modulated at about 11 GHz [S10]. It is a driven relative of this static force and is not filed here.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the dependence on gap and the large-gap fall-off are established and map onto a mode spectrum set by the gap. The ideal prefactor is taken, and the role of the faces is a continuous reduction that the mapping describes only through the measured response of each face.

## Related entries

- [reflection](reflection.md) — the same carrier population in the faces; a different output and a different frequency band
- [blackbody-spectrum](blackbody-spectrum.md) — thermal electromagnetic average; the finite-temperature contribution is related
- [total-internal-reflection](total-internal-reflection.md) — another boundary-conditioned electromagnetic mode

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Bressi, Carugno, Onofrio and Ruoso, *Phys. Rev. Lett.* 88, 041804 (2002), arXiv:quant-ph/0203002](https://arxiv.org/abs/quant-ph/0203002) | full-text | Ideal-plate formula and coefficient; parallel-plate measurement at 0.5–3.0 µm with 15 % precision. |
| S2 | [Lamoreaux, *Phys. Rev. Lett.* 78, 5 (1997)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.78.5) | abstract | Torsion-pendulum measurement at 0.6–6 µm; claimed 5 % agreement. |
| S3 | [Klimchitskaya, Mohideen and Mostepanenko, "The Casimir force between real materials: experiment and theory", arXiv:0902.4022](https://arxiv.org/abs/0902.4022) | full-text | Characteristic frequency c/2a; high-temperature limit at 6 µm and above; criticism of the 5 % claim. Review; journal pages not re-opened. |
| S4 | [Mohideen and Roy, *Phys. Rev. Lett.* 81, 4549 (1998), arXiv:physics/9805038](https://arxiv.org/abs/physics/9805038) | full-text | Atomic-force-microscope measurement at 0.1–0.9 µm. |
| S5 | [Sushkov et al., "Observation of the thermal Casimir force", arXiv:1011.5219](https://arxiv.org/abs/1011.5219) | full-text | Measurement at 0.7–7 µm; thermal force dominant near 3 µm and above. Journal pages not re-opened. |
| S6 | [Lambrecht and Reynaud, "Casimir force between metallic mirrors", arXiv:quant-ph/9907105](https://arxiv.org/abs/quant-ph/9907105) | full-text | Force reduction factors for Al, Au and Cu at 0.1, 0.5 and 3 µm. Journal pages not re-opened. |
| S7 | [Lisanti, Iannuzzi and Capasso, *Proc. Natl. Acad. Sci. USA* 102, 11989 (2005), arXiv:quant-ph/0502123](https://arxiv.org/abs/quant-ph/0502123) | full-text | Reduced force with a 9 nm palladium film; fit to C/d³; skin-depth condition near 100 Å. |
| S8 | [de Man, Heeck, Wijngaarden and Iannuzzi, *Phys. Rev. Lett.* 103, 040402 (2009), arXiv:0901.3720](https://arxiv.org/abs/0901.3720) | full-text | Force with indium tin oxide 40–50 % smaller than with gold at 50–150 nm. |
| S9 | [Iannuzzi, Lisanti and Capasso, *Proc. Natl. Acad. Sci. USA* 101, 4019 (2004), arXiv:quant-ph/0403142](https://arxiv.org/abs/quant-ph/0403142) | full-text | No significant change in force when a hydrogen-switchable mirror becomes transparent; a visible transparency window matters little. |
| S10 | [Wilson et al., "Observation of the Dynamical Casimir Effect in a Superconducting Circuit", arXiv:1105.4714](https://arxiv.org/abs/1105.4714) | full-text | Dynamical Casimir effect in a line terminated by a modulated superconducting interference device. Journal pages not re-opened. |
