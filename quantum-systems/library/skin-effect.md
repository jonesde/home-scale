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
review_depth: deep
related:
  - reflection
  - plasma-frequency-cutoff
  - surface-plasmon-resonance
  - cyclotron-resonance
  - meissner
  - superconductivity
  - electrical-resistivity
updated: 2026-11-11
---

# Skin Effect (Low-Frequency Screening Length)

### 4.1 Effect Name

Skin effect (low-frequency screening length)

### 4.2 Macroscopic Observation

An alternating current in a thick conductor has its highest density at the surface, and the density falls with depth. The AC resistance of a large bus-bar or coaxial conductor is higher than the DC resistance of the same metal. At zero frequency the current fills the cross-section uniformly. A current that is switched on suddenly starts at the surface and spreads inward with time. The metal requires no auxiliary power beyond the current itself.

### 4.3 Established Quantitative Boundaries

Steady sinusoidal drive:

- **Model (Maxwell's equations with a local Ohm's law).** For a conductor much thicker than \(\delta\) [S1][S2][S8]:

  \[
  \delta = \sqrt{\frac{2\rho}{\omega\mu}} = \sqrt{\frac{\rho}{\pi f\mu_0\mu_r}}
  \]

- **Convention.** \(\delta\) is the depth at which the field amplitude has fallen to \(1/e\) of its surface value. The profile is \(H = H_0e^{-x/\delta}\sin(\omega t - x/\delta)\): exponential in depth, with a phase lag of one radian per \(\delta\) [S2][S3]. The fields decay inside the metal and there is no edge [S1]. A tertiary source puts over 98 % of the current within \(4\delta\) of the surface [S7].
- **Computed here.** \(e^{-4} = 1.8\,\%\) is the amplitude left at \(4\delta\), and also the share of the integrated current magnitude that lies deeper.
- **Convention.** Standard annealed copper (IACS) is defined as 58 m Ω⁻¹ mm⁻² at 20 °C, which is 1.7241 µΩ·cm or \(5.80\times10^{7}\) S m⁻¹. It is a standard for commercial copper and was not measured on pure metal [S4].
- **Measured.** Critically evaluated resistivity at 293 K: annealed copper of 99.999 % purity \(1.678\times10^{-8}\) Ω·m; silver \(1.587\times10^{-8}\) Ω·m [S5]; aluminium \(2.650\times10^{-8}\) Ω·m [S6].
- **Computed here.** \(\delta\) from those resistivities with \(\mu_r = 1\):

  | Frequency | Cu, IACS | Cu, pure | Ag | Al |
  |---|---|---|---|---|
  | 50 Hz | 9.35 mm | 9.22 mm | 8.97 mm | 11.6 mm |
  | 60 Hz | 8.53 mm | 8.42 mm | 8.19 mm | 10.6 mm |
  | 1 kHz | 2.09 mm | 2.06 mm | 2.00 mm | 2.59 mm |
  | 1 MHz | 66.1 µm | 65.2 µm | 63.4 µm | 81.9 µm |
  | 1 GHz | 2.09 µm | 2.06 µm | 2.00 µm | 2.59 µm |

- **Model (same formula, as published).** Copper: 8.4 mm at 60 Hz and \(\delta = 65.2\,\mathrm{mm}/\sqrt{f}\) for \(\rho = 1.68\times10^{-8}\) Ω·m [S3]; \(\delta = 6.56\times10^{-2}f^{-1/2}\) m, which is 3.56 µm at 340 MHz and 293 K [S8]; about 3 µm at 400 MHz [S1]; about 1 cm at 60 Hz for copper or aluminium, and 1.1 cm for aluminium [S9]. A tertiary table lists 9.22 mm, 8.42 mm, 652 µm, 65.2 µm and 2.06 µm at 50 Hz, 60 Hz, 10 kHz, 1 MHz and 1 GHz [S7]. The spread at 60 Hz, 8.4–8.5 mm, comes from the resistivity chosen. No opened table lists 1 kHz; that row above is arithmetic only.
- **Model (same formula, assumed permeability).** In iron and steel \(\mu_r\) depends on the field and is not a material constant. Published examples: iron with \(\mu_r = 100\) at 1 Hz, 20 mm read from a chart [S2]; iron at 60 Hz, about 220 µm or 1/38 of copper's value (tertiary) [S7].
- **Computed here.** Steel 1020 at 15.90 µΩ·cm [S10]: with \(\mu_r = 100\), 2.6 mm at 60 Hz, 0.63 mm at 1 kHz and 20 µm at 1 MHz; with \(\mu_r = 1\) (saturated), 26 mm, 6.3 mm and 0.20 mm. No measured skin depth, and no stated \(\mu_r\), was found for a named low-carbon steel.
- **Computed here.** \(\delta\) scales as \(\sqrt{\rho}\): ten times the resistivity gives 3.2 times the depth. At 200 kHz, \(\delta\) is 0.148 mm in IACS copper, 0.47 mm in a body of ten times that resistivity and 1.48 mm at a hundred times.
- **Model (same equations).** As \(\omega \to 0\), \(\delta\) grows without limit, and when \(\delta\) is large against the conductor the field and current distributions are those of steady conduction. A factor of ten in frequency or conductivity changes \(\delta\) by a factor of about 3 [S9].
- **Model (same equations).** A wire much thicker than \(\delta\) has about the resistance of a hollow tube of wall thickness \(\delta\) carrying direct current [S7][S3].
- **Model (proximity effect).** The magnetic field of a neighbouring conductor redistributes the current into loops or concentrated patterns, which adds to the skin effect and raises the AC resistance [S11]. In two parallel conductors carrying opposite currents the current crowds toward the facing sides (tertiary) [S7].

Single pulse (magnetic diffusion):

- **Model (magnetic diffusion into a half-space).** A field \(H_0\) applied as a step at the surface enters as \(H(x,t) = H_0\,\mathrm{erfc}\big(x/2\sqrt{Dt}\big)\) with diffusivity \(D = 1/\mu\sigma = \rho/\mu\) [S2]. The current sheet is a Gaussian whose width grows as \(\sqrt{4Dt}\) [S3].
- **Convention.** The railgun literature takes the pulse depth as \(\delta(t) = \sqrt{4t/\mu\sigma} = 2\sqrt{Dt}\) [S12], or as \(2\lambda\) with \(\lambda = \sqrt{\xi_rt}\) and \(\xi_r = \eta_r/\mu_0\) [S13]. The factor inside the root is described there as somewhat arbitrary [S12].
- **Computed here.** Other cuts on the same profile: the \(1/e\) point of erfc is at \(1.27\sqrt{Dt}\); the depth that would hold the same flux at the full surface field is \((2/\sqrt{\pi})\sqrt{Dt} = 1.13\sqrt{Dt}\); the steady \(\delta\) evaluated at \(f = 1/2t\), which treats the pulse as one half-period, is \(\sqrt{2/\pi}\,\sqrt{Dt} = 0.80\sqrt{Dt}\). The four rules span a factor of 2.5.
- **Model (same diffusion law, as published).** In copper \(\lambda \approx 0.116\,t^{1/2}\) (SI units) at room temperature and \(0.219\,t^{1/2}\) at the melting temperature of aluminium [S13].
- **Computed here.** IACS copper has \(D = \rho/\mu_0 = 0.0137\) m² s⁻¹ and \(\sqrt{D} = 0.117\ \mathrm{m\,s^{-1/2}}\), in agreement with the published 0.116. Depths:

  | Pulse length \(t\) | \(2\sqrt{Dt}\) (published rule) | \(1/e\) of erfc | Flux depth | Steady \(\delta\) at \(f = 1/2t\) |
  |---|---|---|---|---|
  | 1 µs | 0.23 mm | 0.15 mm | 0.13 mm | 0.093 mm (500 kHz) |
  | 100 µs | 2.3 mm | 1.5 mm | 1.3 mm | 0.93 mm (5 kHz) |
  | 0.2 ms | 3.3 mm | 2.1 mm | 1.9 mm | 1.3 mm (2.5 kHz) |
  | 0.7 ms | 6.2 mm | 3.9 mm | 3.5 mm | 2.5 mm (714 Hz) |

  The steady value at 1 MHz, 66 µm, is below every figure in the 1 µs row. A step and a steady sine are both idealizations of a real discharge pulse; no opened source treats a half-sine pulse.
- **Computed here.** The step solution has no cut-off depth. At the end of a 0.2–0.7 ms pulse the field in copper is 20–49 % of its surface value at 3 mm and 9–36 % at 4 mm.

Moving contact (velocity skin effect):

- **Model (magnetic diffusion limited by the transit time).** A stationary rail is exposed to the current only while a sliding armature passes, so the rail current under the armature occupies a depth \(2\lambda\) with \(\lambda = \sqrt{\xi_ra/V}\), where \(a\) is the contact length and \(V\) the speed. The current crossing the interface concentrates at the rear of a solid armature. A worked case, \(a = 18.3\) mm at 500 m s⁻¹, gives \(\lambda = 1\) mm [S13]. [S12] uses a rail current layer whose thickness grows with time in the same way.
- **Model (velocity skin effect as a cause of transition).** This concentration is named as a principal cause of the transition from solid contact to arcing, with critical speeds near 1 km s⁻¹ in the worked cases [S13]; transition conditions are also reported for solid armatures with muzzle current feed [S14]. No opened source measured the current layer against speed.
- **Computed here.** The two published coefficients give 0.70 and 1.32 mm for the worked case and bracket its 1 mm. With the room-temperature coefficient, a 1 mm contact at 100 m s⁻¹ has a transit time of 10 µs and \(2\lambda = 0.73\) mm; at 500 m s⁻¹, 2 µs and 0.33 mm. These depths do not depend on the length of the pulse.

Limits of the local formula and neighbouring lengths:

- **Model (Pippard; Reuter and Sondheimer).** The local relation \(J = \sigma E\) fails when \(\delta\) falls below the electron mean free path \(\ell\); a non-local relation replaces it, and the regime is called the anomalous skin effect [S15][S1]. The two primary papers were not opened. In the extreme limit the surface resistance goes from \(\omega^{1/2}\) to \(\omega^{2/3}\), as \(R_n \propto \omega^{2/3}(\rho\ell)^{1/3}\), and \(\delta\) no longer depends on \(\ell\) [S15][S8][S1]. An effective depth varying as \(\omega^{-1/3}\) follows from \(R_s \propto \omega\mu\delta\); no opened source states that exponent for \(\delta\).
- **Model (free-electron estimate from measured conductivity).** Mean free path in copper at room temperature: 39 nm at 293 K [S8], about 40 nm [S1], and \(\rho\ell = 6.8\times10^{-16}\) Ω·m² [S15]. A value of 39.9 nm is cited from [S16], which was not opened. Cold copper with a residual resistivity ratio near 100 has about 4 µm [S1][S8].
- **Model (classical formula against that mean free path).** In copper at 293 K and 340 MHz, \(\delta = 3.56\) µm against \(\ell = 39\) nm, and the anomalous skin effect does not occur at room temperature [S8].
- **Computed here.** \(\rho\ell/\rho = 40\) nm for \(\rho = 1.68\times10^{-8}\) Ω·m. \(\delta/\ell\) is 91 at 340 MHz. \(\delta\) would equal 39 nm only near 2.8–2.9 THz, where \(\omega\tau \approx 0.45\) for the scattering time \(2.46\times10^{-14}\) s [S8], so the quasi-static formula is failing there for a second reason. At 0.7–4 kHz, \(\delta\) is 2.5–1.0 mm and \(\delta/\ell\) is \(6.4\times10^{4}\) to \(2.7\times10^{4}\).
- **Measured.** Optical constants: silver \(k = 3.093\) at 496 nm [S17]; aluminium \(k = 6.242\) at 517 nm [S18]. Both were read in the refractiveindex.info tabulation of the primary data.
- **Computed here.** The optical intensity depth \(\lambda/4\pi k\) is 12.8 nm for silver at 496 nm and 6.6 nm for aluminium at 517 nm. The field-amplitude depth \(\lambda/2\pi k\) is twice that: 25.5 and 13.2 nm. Across 413–689 nm the source check obtained 11.7–14.5 nm for silver and 6.6–6.8 nm for aluminium from the same tables; the end-point \(k\) values are not reproduced here, and [reflection](reflection.md) owns the full set. The first version gave 10–20 nm for both metals.
- **Model (Hagen–Rubens).** The infrared reflectance of a metal is tied to its surface resistance, and through it to the conductivity [S1].
- **Computed here.** The steady formula does not carry into the visible: for silver at 496 nm (604 THz) it gives 2.6 nm, a tenth of the 25.5 nm amplitude depth from the measured \(k\).
- **Model (Lorentz–Drude fit to optical data).** Plasma energies \(\hbar\omega_p\): Ag 9.01, Cu 10.83, Al 14.98 eV [S19].
- **Computed here.** The corresponding plasma periods \(h/\hbar\omega_p\) are 0.46, 0.38 and 0.28 fs.
- **Model (London).** A superconductor screens over \(\lambda_L = \sqrt{m/\mu_0n_se^2}\), a static length with no frequency in it [S15]. It is filed under [meissner](meissner.md).
- **Model (Azbel'–Kaner).** Near cyclotron resonance in a metal the skin depth is much less than the orbit radius; with the field parallel to the surface, electrons return to the skin layer many times when \(\ell/2\pi r \gg 1\) [S20].

**Data confidence:** High — the steady formula and its copper values agree across independent sources to within the spread set by the resistivity chosen, and the resistivities are critically evaluated. The pulse depth is a model with a convention inside it; the published rule and three other cuts differ by a factor of 2.5. The velocity skin effect rests on a diffusion model and on transition speeds; no direct measurement of the layer was found. The primary papers on the anomalous regime and one mean-free-path value are cited-only. Three statements (98 % within \(4\delta\), iron at 60 Hz, crowding to facing sides) are tertiary. Steel values rest on an assumed \(\mu_r\).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Steady profile in a thick conductor [S2][S3]:

  \[
  H(x,t) = H_0\,e^{-x/\delta}\sin(\omega t - x/\delta),\qquad \delta = \sqrt{\frac{2\rho}{\omega\mu}}
  \]

- Step response of a half-space, and the railgun pulse depth [S2][S12]:

  \[
  H(x,t) = H_0\,\mathrm{erfc}\!\left(\frac{x}{2\sqrt{Dt}}\right),\qquad D = \frac{\rho}{\mu},\qquad \delta(t) = 2\sqrt{Dt}
  \]

- Depth under a moving contact of length \(a\) at speed \(V\) [S13]: \(2\lambda = 2\sqrt{Da/V}\).
- AC resistance: in the thick limit the conducting cross-section is that of a tube of wall \(\delta\) [S7][S3].
- Anomalous limit: \(R_n \propto \omega^{2/3}(\rho\ell)^{1/3}\) [S15]. The exponent is recorded as data for that regime and is not used here as a node rule.
- Hagen–Rubens: \(r = 1 - 4R_s/R_0\), with \(R_s\) the surface resistance [S1].
- Optical intensity depth: \(\delta_\mathrm{opt} = \lambda/4\pi k\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** There is no minimum thickness. The field falls as \(e^{-x/\delta}\), and a conductor of half-thickness \(a\) shows a contrast between surface and centre that grows with \(a/\delta\). The buffer is the screening length \(\delta\), quoted at \(1/e\) by convention: millimetres in copper at power frequencies, micrometres at radio frequencies. Under a pulse or a moving contact the same role is taken by a diffusion depth of order \(\sqrt{Dt}\).

- **Clock rate / latency.** One constant, the magnetic diffusivity \(D = \rho/\mu\) (0.0137 m² s⁻¹ in copper), is read against three drive clocks: the period of a steady drive, giving \(\delta = \sqrt{D/\pi f}\); the time since a pulse began, giving 0.8–2 times \(\sqrt{Dt}\) depending on the rule; and the transit time \(a/V\) of a moving contact. The same electron population has a plasma period of 0.28–0.46 fs, which is the clock used in [reflection](reflection.md).

- **Energy barriers or thresholds.** None. This is a driven dissipative response. It holds no state and has no gap.

- **Dominant failure modes.**
  - **Crossover** — slow drive: \(\delta \propto \omega^{-1/2}\) grows without limit as \(\omega \to 0\), and the current distribution goes over to uniform fill. The scale is \(\delta = a\). No critical frequency exists.
  - **Crossover** — thin conductor: the same function \(e^{-x/\delta}\) read at fixed \(\omega\). For \(a \ll \delta\) the whole cross-section carries current; at \(a = 4\delta\) the centre amplitude is 1.8 % of the surface value.
  - **Crossover** — short pulse: \(\mathrm{erfc}(x/2\sqrt{Dt})\). Current reaches a depth \(x\) after a time of order \(x^2/4D\); the single number quoted depends on the rule chosen, over a factor of 2.5.
  - **Crossover** — moving contact: depth \(2\sqrt{Da/V}\), falling as \(V^{-1/2}\). For a 1 mm copper contact it is 0.73 mm at 100 m s⁻¹ and 0.33 mm at 500 m s⁻¹.
  - **Crossover** — local response: the classical formula degrades as \(\ell/\delta\) approaches 1, and the surface-resistance exponent moves from 1/2 to 2/3. In room-temperature copper \(\ell/\delta\) is about 10⁻² at 340 MHz and below 10⁻⁴ at kilohertz frequencies, so this regime is reached only in cold, pure metal at high frequency.
  - **Crossover** — material: \(\delta \propto \sqrt{\rho/\mu_r}\). Heating, melting, alloying or a granular body raise \(\rho\) and widen the layer; a ferromagnetic conductor below saturation narrows it. The resistivity side is filed under [electrical-resistivity](electrical-resistivity.md).
  - **Threshold** — superconducting transition: below \(T_c\) the dissipative, frequency-dependent layer is replaced by the static London depth. Owned by [meissner](meissner.md).

- **Emergent constant or stable output.** A current density that is highest at the surface and falls exponentially over the length \(\delta(\omega)\), and the rise in AC resistance that goes with it.

### 4.6 Internal Consistency Notes

This is the low-frequency end of the same free-electron screening machine as [reflection](reflection.md). Reflection fails when the film is thinner than the optical penetration depth, or when the drive outruns the plasma clock (`plasma-frequency-cutoff`). The skin effect fades when the conductor is thinner than the classical \(\delta\), or when the drive is too slow. Same family, different clock band, different measured length.

Six lengths must be kept apart:

1. steady \(\delta = \sqrt{2\rho/\omega\mu}\) (local Ohm's law, \(\ell \ll \delta\));
2. the diffusion depth of a single pulse, of order \(\sqrt{Dt}\);
3. the depth under a moving contact, \(2\sqrt{Da/V}\);
4. anomalous penetration (\(\ell \gtrsim \delta\));
5. optical \(\lambda/4\pi k\) (owned by reflection), which is an intensity depth and half the amplitude depth;
6. London \(\lambda\) (owned by `meissner`).

Using one word, "penetration depth", for all of them is an internal-consistency error. Lengths 1–3 share one diffusivity and differ only in the clock.

Sourcing changed the entry in seven places. The first version described a current "confined to a surface layer" with a "distinct screened interior"; the profile is an exponential and \(\delta\) is its \(1/e\) length. It had no pulse case, and the application file applied the steady formula to single pulses, which understates the published pulse depth by a factor of 2.5 (0.93 mm against 2.3 mm at 100 µs). The velocity skin effect was absent. The optical depth was given as 10–20 nm for silver and aluminium; aluminium is 6.6–6.8 nm as an intensity depth. The plasma period was called femtosecond-scale; it is 0.28–0.46 fs. The copper conductivity was called a handbook value; it is the IACS convention, and pure copper moves the 60 Hz depth from 8.5 to 8.4 mm. The \(\omega^{-1/3}\) scaling of the anomalous depth was stated as a fact; the opened sources give the surface-resistance exponent, from which it is inferred. The arithmetic is guarded by [`analysis/computed_checks.py`](../analysis/computed_checks.py).

QSA takes \(\sqrt{2\rho/\omega\mu}\) as the buffer specification. The square root is the diffusion law, so the three depths reduce to one measured constant \(D = \rho/\mu\). That constant is still taken, not derived from a more primitive node count. It is the same class of gap recorded for the optical penetration depth.

The velocity skin effect is filed on model evidence only. If a measurement of the current layer against speed is found, it belongs in §4.3 in place of the worked case.

[Cyclotron resonance](cyclotron-resonance.md) in metals (Azbel'–Kaner) uses the skin layer as the volume the microwave field occupies. The skin is the buffer; the cyclotron match is a different clock.

### 4.7 Overall Confidence in the QSA Mapping

**High** — one measured constant gives the buffer under all three drive clocks, and every failure mode except the superconducting transition is a crossover on that length. The first version's picture of a layer with an edge is withdrawn, and the velocity case remains model-only.

## Related entries

- [reflection](reflection.md) — optical end of the same screening; penetration is \(\lambda/4\pi k\), not \(\sqrt{2\rho/\omega\mu}\)
- [Plasma-frequency cutoff](plasma-frequency-cutoff.md) — clock-failure twin of reflection; high-frequency end of this machine
- [surface-plasmon-resonance](surface-plasmon-resonance.md) — interface-bound mode of the same electrons; decay into the metal is the optical depth
- [cyclotron-resonance](cyclotron-resonance.md) — Azbel'–Kaner resonance is cyclotron motion sampled inside the skin layer
- [Meissner effect](meissner.md) — static, dissipationless expulsion; London \(\lambda\) is not this \(\delta\)
- [Superconductivity](superconductivity.md) — the condensate that replaces the dissipative layer with Meissner screening
- [Electrical resistivity and Joule heating](electrical-resistivity.md) — the resistivity that sets \(D\), and the heating of the layer that carries the current

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Calatroni, "Materials & Properties: Thermal & Electrical Characteristics", CERN Accelerator School 2017, arXiv:2006.02842](https://arxiv.org/abs/2006.02842) | full-text | Skin-depth formula; exponential decay with no propagation into the metal; about 3 µm at 400 MHz; mean free path about 40 nm; anomalous condition and loss of dependence on mean free path; Hagen–Rubens law. |
| S2 | [Moritz, "Eddy currents in accelerator magnets", arXiv:1103.1800](https://arxiv.org/abs/1103.1800) | full-text | Harmonic profile with phase lag; step-field erfc solution (after Knoepfel, *Magnetic Fields*, not opened); iron at 1 Hz with a relative permeability of 100. |
| S3 | [University of Texas at Austin physics course notes, "eddy.pdf" (2022)](https://web2.ph.utexas.edu/~vadim/Classes/2022s/eddy.pdf) | full-text | 8.4 mm at 60 Hz and 65.2 mm over root f for copper; exponential current profile; Gaussian current sheet of width root 4Dt. Secondary. |
| S4 | [*Copper Wire Tables*, National Bureau of Standards Handbook 100 (1966)](https://nvlpubs.nist.gov/nistpubs/Legacy/hb/nbshandbook100.pdf) | full-text | IACS definition: 58 m per ohm mm² at 20 °C, 1.7241 µΩ·cm. |
| S5 | [Matula, *J. Phys. Chem. Ref. Data* 8, 1147 (1979)](https://srd.nist.gov/jpcrdreprint/1.555614.pdf) | full-text | Evaluated resistivity of pure copper and silver at 293 K. |
| S6 | [Desai, James and Ho, *J. Phys. Chem. Ref. Data* 13, 1131 (1984)](https://srd.nist.gov/jpcrdreprint/1.555725.pdf) | full-text | Evaluated resistivity of aluminium at 293 K. |
| S7 | [Wikipedia, "Skin effect"](https://en.wikipedia.org/wiki/Skin_effect) | full-text | Tertiary: table of copper skin depths; over 98 % of current within four skin depths; tube-of-wall-δ resistance; iron at 60 Hz; crowding of current between parallel conductors. |
| S8 | [Ratzinger and Wang, "The anomalous skin effect and copper cavity operation at cryogenic conditions", arXiv:2211.00135](https://arxiv.org/abs/2211.00135) | full-text | Copper formula 6.56e-2 over root f; 3.56 µm at 340 MHz; mean free path 39 nm and scattering time at 293 K; no anomalous effect at room temperature; surface-resistance exponent from 1/2 toward 2/3. |
| S9 | [Haus and Melcher, *Electromagnetic Fields and Energy* (MIT online edition), sec. 10.7](https://web.mit.edu/6.013_book/www/chapter10/10.7.html) | full-text | About 1 cm at 60 Hz; aluminium 1.1 cm; large-skin-depth limit; factor of about 3 per decade. |
| S10 | [IEEE Std 80-2000, *Guide for Safety in AC Substation Grounding*, Table 1 (single-page copy)](https://satcon.in/public/tech_info/1583400418.pdf) | full-text | Steel 1020 resistivity 15.90 µΩ·cm. Secondary copy of a design standard. |
| S11 | [Sullivan, *IEEE Trans. Power Electron.* 14, 283 (1999), mirror copy](https://cms.fi.uba.ar/uploads/Sullivan_Optimal_choice_for_number_of_strands_in_a_litz_wire_transformer_winding_PELS_1999_26877be9ec.pdf) | full-text | Definition of the proximity effect. The usual primary, Dowell (1966), was not opened. |
| S12 | [McCorkle and Bahder, "Tradeoff between Efficiency and Melting for a High-Performance Electromagnetic Rail Gun", arXiv:0810.2985](https://arxiv.org/abs/0810.2985) | full-text | Pulse skin depth root of 4t over μσ; the factor is somewhat arbitrary; current layer that thickens with time. |
| S13 | [Woods, "Analysis of the Armature-Rail Interface in Solid Armature Railguns", Institute for Advanced Technology report IAT.R 0120 (1996), DTIC ADA320642](https://apps.dtic.mil/sti/tr/pdf/ADA320642.pdf) | full-text | Velocity skin effect: depth 2λ with the transit time; copper coefficients 0.116 and 0.219; worked case; role in transition. |
| S14 | [Kareev and Zayatdinov, *IEEE Trans. Magn.* 31(1) (1995), OSTI record](https://www.osti.gov/biblio/32048) | abstract | Transition conditions for solid armatures with muzzle current feed. |
| S15 | [Ciovati, "AC/RF Superconductivity", arXiv:1501.07398](https://arxiv.org/abs/1501.07398) | full-text | Anomalous skin effect defined; extreme-limit surface resistance; ρℓ for copper; London depth. Secondary for Pippard (1947) and Reuter and Sondheimer (1948), which were not opened. |
| S16 | [Gall, *J. Appl. Phys.* 119, 085101 (2016)](https://doi.org/10.1063/1.4942216) | cited-only | Mean free path of copper, 39.9 nm. |
| S17 | [Johnson and Christy, *Phys. Rev. B* 6, 4370 (1972), as tabulated at refractiveindex.info](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/Ag/nk/Johnson.yml) | full-text | Silver optical constants. Secondary tabulation of the primary data. |
| S18 | [Rakić, *Appl. Opt.* 34, 4755 (1995), as tabulated at refractiveindex.info](https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/main/Al/nk/Rakic.yml) | full-text | Aluminium optical constants. Secondary tabulation of the primary data. |
| S19 | [Rakić, Djurišić, Elazar and Majewski, *Appl. Opt.* 37, 5271 (1998), hosted copy](https://cdn.optiwave.com/wp-content/uploads/2015/06/25150911/4.pdf) | full-text | Plasma energies of Ag, Cu and Al. |
| S20 | [Azbel' and Kaner, *Sov. Phys. JETP* 3, 772 (1956)](http://jetp.ras.ru/cgi-bin/dn/e_003_05_0772.pdf) | full-text | Skin depth much less than the orbit radius; repeated return of electrons to the skin layer. |
