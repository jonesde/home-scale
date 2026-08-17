# Effect library index

Entries are utility and internal-consistency tests, not interpretive claims. Families are QSA machine/collapse classes; conventional names are in the Effect column.

Every first-wave row now links to a file. Column meanings: [library README](README.md). Family definitions: [TAXONOMY.md](TAXONOMY.md).

**Status:** 49 formal · 0 draft · 0 queued. Mapping: 24 High · 25 Medium · 0 Low. Data is High except [dielectric breakdown](dielectric-breakdown.md) (Medium).

Logically derived spec sheets and a shared-requirement audit live in [`derived/`](derived/README.md) — not catalog rows. Device applications: [`../application/`](../application/README.md).

Medium mapping is not a failed entry. It means the collapse is real and the machine class is assigned, but a hardware scale is statistical, mesoscale, or taken from a measured constant rather than derived. Those are the places a second pass should tighten.

---

## 1. Collective field response

Many charged nodes must occupy a minimum coherent volume and synchronize before a stable macroscopic EM output appears.

| Effect | Slug | Status | Data | Mapping | Dominant collapse | Notes |
|---|---|---|---|---|---|---|
| [Reflection (electron-cloud response)](reflection.md) | `reflection` | formal | High | High | Continuous film ≲ 5–10 nm, or drive above the plasma / interband edge | Visible light returns from Ag/Al; the mirror dies when the connected buffer is starved |
| [Refraction / dielectric polarization](refraction-dielectric.md) | `refraction-dielectric` | formal | High | Medium | n−1 → 0 (X-ray / vacuum / path ≪ λ); breakdown is a different family | Snell's law as bound-charge output; no single nm-scale cliff |
| [Skin effect](skin-effect.md) | `skin-effect` | formal | High | High | δ exceeds the conductor, or ω → 0 | Low-frequency end of the same screening as reflection; keep classical, anomalous, and optical lengths distinct |
| [Plasma-frequency cutoff](plasma-frequency-cutoff.md) | `plasma-frequency-cutoff` | formal | High | High | ω > ωp (Al, alkalis); Ag optical edge ~3.9 eV | Clock-failure twin of reflection; alkalis are the clean test, Ag is interband-shifted |
| [Surface plasmon resonance](surface-plasmon-resonance.md) | `surface-plasmon-resonance` | formal | High | Medium | No momentum match; film thickness off the resonance window | Interface-bound mode; needs a metal–dielectric face plus a coupler; tens of nm typical, not universal |
| [Total internal reflection](total-internal-reflection.md) | `total-internal-reflection` | formal | High | High | θ < θc, or n1 ≤ n2; third body inside the evanescent tail | Geometry / index gate on the same n as refraction |
| [Faraday rotation](faraday-rotation.md) | `faraday-rotation` | formal | High | Medium | B → 0 or path below the Verdet · B · L detection budget | Polarization rotates as VBL; product budget, not a hard cliff |
| [Cyclotron resonance](cyclotron-resonance.md) | `cyclotron-resonance` | formal | High | High | ω ≠ ωc, or ωc τ < 1 | Absorption at eB/m*; m* is a measured output; needs a long enough scattering time |

---

## 2. Latched order

An energy barrier holds a directional or configurational state at zero continuous power.

| Effect | Slug | Status | Data | Mapping | Dominant collapse | Notes |
|---|---|---|---|---|---|---|
| [Permanent magnet (directional latch)](permanent-magnet-latch.md) | `permanent-magnet-latch` | formal | High | High | T > Tc; KV ≲ 25 kT; lattice shock | NdFeB holds a directional force with no power draw; soft iron does not |
| [Superparamagnetism](superparamagnetism.md) | `superparamagnetism` | formal | High | High | KV ≲ kT ln(τm/τ0); ~25 kT is a lab-time convention | Volume collapse of the same latch; NdFeB blocks near 30 nm; the factor 25 is a timescale contour |
| [Ferromagnetic hysteresis](ferromagnetic-hysteresis.md) | `ferromagnetic-hysteresis` | formal | High | High | Loop area / Hc → 0 (soft limit); also T > Tc | Write–erase cycle; hold costs zero, write costs the loop area; Hc ≪ Ha is the mesoscale gap |
| [Ferroelectric remanence](ferroelectric-remanence.md) | `ferroelectric-remanence` | formal | High | Medium | T > Tc; coercive E exceeded; grain / film too small | Electrical twin: remnant P at E = 0; Ec and the depolarization buffer stay mesoscale |
| [Antiferromagnetic order](antiferromagnetic-order.md) | `antiferromagnetic-order` | formal | High | High | T > TN | Latched opposing sublattices; net macro moment ~0 — a latch whose emergent output is zero force |
| [Exchange bias](exchange-bias.md) | `exchange-bias` | formal | High | Medium | T > TB of the AFM pin (TB ≤ TN) | Second latch pinning the first; Hex and TB/TN remain interface / grain data |
| [Shape anisotropy](shape-anisotropy.md) | `shape-anisotropy` | formal | High | High | Aspect ratio → 1 (demag barrier vanishes) | Geometry / demag barrier; needles latch without large K1; spheres do not |
| [Magnetic domains](magnetic-domains.md) | `magnetic-domains` | formal | High | Medium | Single-domain size, or saturation (walls expelled) | How a large body partitions the aligned population; wall width ~√(A/K) is a measured buffer |

---

## 3. Gapped coherence

A protected collective mode with critical temperature, field, and/or current.

| Effect | Slug | Status | Data | Mapping | Dominant collapse | Notes |
|---|---|---|---|---|---|---|
| [Superconductivity (zero resistance)](superconductivity.md) | `superconductivity` | formal | High | Medium | T > Tc, H > Hc (Hc2), or I > Ic | R → 0 below a material-specific triple; coherent volume is not one number; pinning still unspecified |
| [Meissner effect](meissner.md) | `meissner` | formal | High | High | H > Hc (type I) or H > Hc1 (type II); thickness ≪ λ | Field expulsion with χ = −1; London λ is the spatial buffer; not the same artifact as R = 0 |
| [Josephson effect](josephson-effect.md) | `josephson-effect` | formal | High | High | Junction too thick (Ic → 0); I > Ic; T > Tc | Weak-link pair current; voltage–frequency lock 483.6 MHz/μV |
| [Flux quantization](flux-quantization.md) | `flux-quantization` | formal | High | High | Loop not superconducting; fluxoid not conserved | Closed loop holds n Φ0 = n h/2e |
| [Type-II critical field / vortices](type-ii-critical-field.md) | `type-ii-critical-field` | formal | High | High | Hc1 first penetration; Hc2 gap destroyed; unpinned flux flow | Mixed-state vortex lattice; extra spatial scale √(Φ0/B) |
| [Superfluid helium-4](superfluid-helium-4.md) | `superfluid-helium-4` | formal | High | High | T > Tλ (2.17 K); v > vc | Chargeless superflow / fountain; family name “gapped” is slightly loose (no pairing gap) |
| [Bose–Einstein condensate](bose-einstein-condensate.md) | `bose-einstein-condensate` | formal | High | Medium | T > Tc(n), or density drops; phase coherence lost | Dilute alkali BEC; clean thermal/density cliff; no measured pairing gap; not a zero-power latch |
| [Quantum Hall effect](quantum-hall-effect.md) | `quantum-hall-effect` | formal | High | Medium | B off a plateau; T or current too high; 2DEG lost | Integer RH = h/(ν e²); gap + edge channel recorded, not derived |

---

## 4. Threshold conversion

A discrete energetic or field gate. Below threshold the conversion does not occur.

| Effect | Slug | Status | Data | Mapping | Dominant collapse | Notes |
|---|---|---|---|---|---|---|
| [Photoelectric threshold](photoelectric-threshold.md) | `photoelectric-threshold` | formal | High | High | hν < φ (typical φ 2–6 eV) | Electrons leave a metal only above the work function; KE = hν − φ; contrast case for reflection |
| [Work function / thermionic emission](work-function-thermionic.md) | `work-function-thermionic` | formal | High | High | kT well below φ (Richardson tail dies) | Same surface gate as photoelectric, opened by heat; W ~4.5 eV, Cs ~2 eV |
| [Semiconductor gap absorption](semiconductor-gap-absorption.md) | `semiconductor-gap-absorption` | formal | High | High | hν < Eg | Crystal transmits below the gap and absorbs above; Si 1.12 eV, Ge 0.66 eV, GaAs 1.42 eV |
| [X-ray absorption edge](x-ray-absorption-edge.md) | `x-ray-absorption-edge` | formal | High | High | hν below the shell binding energy | Element-specific inner-shell gates; Cu K-edge 8.979 keV |
| [Ionization threshold](ionization-threshold.md) | `ionization-threshold` | formal | High | High | E < I | Gas stays neutral below the binding energy; H 13.598 eV, He 24.6 eV |
| [Pair production](pair-production.md) | `pair-production` | formal | High | High | Eγ < 1.022 MeV; no nearby nucleus | Photon → e⁺e⁻ only above 2mec² and with a momentum sink |
| [Dielectric breakdown](dielectric-breakdown.md) | `dielectric-breakdown` | formal | Medium | Medium | E < Ebd (no conversion); above it the insulator is destroyed | Field-opened insulator → conductor; dry air ~3 MV/m class; geometry- and damage-dependent |
| [Photoconductivity](photoconductivity.md) | `photoconductivity` | formal | High | High | hν < Eg or trap depth | Same gap gate as absorption, read out as current; gain set by lifetime / transit time |

---

## 5. Lattice modes

The ion grid as coupled mechanical oscillators.

| Effect | Slug | Status | Data | Mapping | Dominant collapse | Notes |
|---|---|---|---|---|---|---|
| [Phonon dispersion](phonon-dispersion.md) | `phonon-dispersion` | formal | High | Medium | Zone-boundary cutoff; mode softening; loss of Bragg order | Measured ω(q) is the lattice allowed-clock map; no single hardware number |
| [Speed of sound](speed-of-sound.md) | `speed-of-sound` | formal | High | High | No medium, or G = 0 (no shear); qa ~ 1 kills the long-wave slope | Long-wave vs = √(C/ρ); no shear sound in a vacuum or a liquid |
| [Debye cutoff](debye-cutoff.md) | `debye-cutoff` | formal | High | High | ω > ωD (mode absent) | Finite N ⇒ 3N modes; ΘD is the clock ceiling |
| [Melting](melting.md) | `melting` | formal | High | Medium | T → Tm; loss of Bragg order and shear | The grid stops being a grid; Lindemann is a criterion, not a derivation |
| [Phonon thermal conductivity](thermal-conductivity-phonon.md) | `thermal-conductivity-phonon` | formal | High | Medium | Umklapp / boundary / amorphization kills the mean free path | κ = (1/3) C v ℓ; peak at intermediate T; Casimir at low T |
| [Elasticity](elasticity.md) | `elasticity` | formal | High | Medium | Stress above yield / fracture; G → 0 at Tm | Hooke at small strain; dislocations are the mesoscale gap |
| [Piezoelectricity](piezoelectricity.md) | `piezoelectricity` | formal | High | Medium | Inversion present, or T > Tc (ferroelectric) | Strain ↔ P only without inversion; coupling taken from handbook d_ij |
| [Magnetostriction](magnetostriction.md) | `magnetostriction` | formal | High | Medium | T > Tc or lattice destroyed | Length change locked to the moment; Ni ~10⁻⁵ vs Terfenol-D 10⁻³ class |
| [Thermal expansion](thermal-expansion.md) | `thermal-expansion` | formal | High | Medium | Anharmonicity → 0 (Grüneisen → 0) | Harmonic lattice does not expand; metals 10⁻⁶–10⁻⁵/K; Invar is cancellation |

---

## 6. Ensemble averages

Stable macro constants or spectra that exist only as the averaged output of a large population.

Every mapping in this family is Medium for the same recorded reason: the hardware scale is statistical. There is no universal N-cliff analogous to a 10 nm film or a Curie point.

| Effect | Slug | Status | Data | Mapping | Dominant collapse | Notes |
|---|---|---|---|---|---|---|
| [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) | `thermal-equilibrium-temperature` | formal | High | Medium | Too few independent contributors, or observation faster than the exchange window | T is the stable averaged output of a large population; no universal N |
| [Ideal-gas pressure](ideal-gas-pressure.md) | `ideal-gas-pressure` | formal | High | Medium | Kn = λ/L ≳ 1, or N too small for a stable reading | Wall force P = nkT; continuum hydro is a second, density-tracking envelope |
| [Blackbody spectrum](blackbody-spectrum.md) | `blackbody-spectrum` | formal | High | Medium | Cavity modes under-populated; wall T undefined; surface not black | Planck u(ν,T) as the thermal EM average; Rayleigh–Jeans is the failed high-ν envelope |
| [Stefan–Boltzmann law](stefan-boltzmann.md) | `stefan-boltzmann` | formal | High | Medium | Same envelope as the spectrum; surface not black; T → 0 | j = εσT⁴ is the integral of the Planck curve; σ is defined |
| [Electron heat capacity](electron-heat-capacity.md) | `electron-heat-capacity` | formal | High | Medium | T → 0 (γT into noise), or a gapped spectrum | Ce = γT from a Fermi-surface slice ~ T/TF; a superconducting gap removes the linear term |
| [Brownian motion](brownian-motion.md) | `brownian-motion` | formal | High | Medium | Particle so large the kicks average below the window’s resolution | Visible jitter is an incomplete impact average; D = kT/γ; large bodies look still |
| [Johnson–Nyquist noise](johnson-nyquist-noise.md) | `johnson-nyquist-noise` | formal | High | Medium | T → 0 or Δf → 0; hf ≳ kT leaves the classical envelope | ⟨V²⟩ = 4kTRΔf; electrical FDR twin of Brownian; no resistor-volume cliff |
| [Curie paramagnetism](curie-paramagnetism.md) | `curie-paramagnetism` | formal | High | Medium | Order at Tc / TN / θ, or χ → 0 as T → ∞; saturation if μB ≳ kT | χ = C/T unlocked-spin ensemble; contrast with the latched magnet / AFM order |

---

## Slug list

`antiferromagnetic-order` · `blackbody-spectrum` · `bose-einstein-condensate` · `brownian-motion` · `curie-paramagnetism` · `cyclotron-resonance` · `debye-cutoff` · `dielectric-breakdown` · `elasticity` · `electron-heat-capacity` · `exchange-bias` · `faraday-rotation` · `ferroelectric-remanence` · `ferromagnetic-hysteresis` · `flux-quantization` · `ideal-gas-pressure` · `ionization-threshold` · `johnson-nyquist-noise` · `josephson-effect` · `magnetic-domains` · `magnetostriction` · `meissner` · `melting` · `pair-production` · `permanent-magnet-latch` · `phonon-dispersion` · `photoconductivity` · `photoelectric-threshold` · `piezoelectricity` · `plasma-frequency-cutoff` · `quantum-hall-effect` · `reflection` · `refraction-dielectric` · `semiconductor-gap-absorption` · `shape-anisotropy` · `skin-effect` · `speed-of-sound` · `stefan-boltzmann` · `superconductivity` · `superfluid-helium-4` · `superparamagnetism` · `surface-plasmon-resonance` · `thermal-conductivity-phonon` · `thermal-equilibrium-temperature` · `thermal-expansion` · `total-internal-reflection` · `type-ii-critical-field` · `work-function-thermionic` · `x-ray-absorption-edge`
