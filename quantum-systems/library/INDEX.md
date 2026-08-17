# Effect library index

Entries are utility and internal-consistency tests, not interpretive claims. Families are QSA machine/collapse classes; conventional names are in the Effect column.

`formal` / `draft` rows link to a file. `queued` rows are the build list — no file yet. Column meanings: [library README](README.md). Family definitions: [TAXONOMY.md](TAXONOMY.md).

**Status:** 2 formal · 0 draft · 47 queued.

---

## Suggested next

Write these before mining the long tables. Each has a sharp measured collapse, and the first four were already named in the handover. The last two close spatial/clock pairs on the two files that now exist.

| Effect | Slug | Why next |
|---|---|---|
| Superconductivity (zero resistance) | `superconductivity` | Sharp Tc, Hc, Ic; opens gapped-coherence |
| Meissner effect | `meissner` | Same condensate, different failure envelope; split-rule test |
| Photoelectric / optical absorption threshold | `photoelectric-threshold` | Contrast case for [reflection](reflection.md) |
| Phonon dispersion | `phonon-dispersion` | Opens lattice-modes; clean measured curves |
| Plasma-frequency cutoff | `plasma-frequency-cutoff` | Clock-failure twin of [reflection](reflection.md) |
| Superparamagnetism | `superparamagnetism` | Volume-failure twin of [permanent-magnet-latch](permanent-magnet-latch.md) |

---

## 1. Collective field response

Many charged nodes must occupy a minimum coherent volume and synchronize before a stable macroscopic EM output appears.

| Effect | Slug | Status | Data | Mapping | Dominant collapse | Notes |
|---|---|---|---|---|---|---|
| [Reflection (electron-cloud response)](reflection.md) | `reflection` | formal | High | High | Continuous film ≲ 5–10 nm, or drive above the plasma / interband edge | Visible light returns from Ag/Al; the mirror dies when the connected buffer is starved |
| Refraction / dielectric polarization | `refraction-dielectric` | queued | High | — | ε → 1 (X-ray / vacuum limit); breakdown at high E | Snell's law as the macro output of a polarized bound-charge population |
| Skin effect | `skin-effect` | queued | High | — | δ = √(2/ωμσ) exceeds the conductor, or ω → 0 | AC current confined to a surface layer; low-frequency end of the same screening as reflection |
| Plasma-frequency cutoff | `plasma-frequency-cutoff` | queued | High | — | ω > ωp (Al, alkalis); Ag interband edge ~3.9 eV | Metal turns transmitting when the drive outruns collective screening |
| Surface plasmon resonance | `surface-plasmon-resonance` | queued | High | — | No momentum match; film thickness off the resonance window | Interface-bound collective mode; needs a metal–dielectric boundary plus a coupler |
| Total internal reflection | `total-internal-reflection` | queued | High | — | θ < θc, or n1 ≤ n2 | Evanescent buffer on the far side of an interface; collapse is a geometry / index gate |
| Faraday rotation | `faraday-rotation` | queued | High | — | B → 0 or path length below the Verdet · B · L budget | Polarization plane rotates in proportion to path × field through the medium |
| Cyclotron resonance | `cyclotron-resonance` | queued | High | — | ω ≠ ωc, or ωτ < 1 | Absorption when the drive matches eB/m; needs a long enough scattering time |

---

## 2. Latched order

An energy barrier holds a directional or configurational state at zero continuous power.

| Effect | Slug | Status | Data | Mapping | Dominant collapse | Notes |
|---|---|---|---|---|---|---|
| [Permanent magnet (directional latch)](permanent-magnet-latch.md) | `permanent-magnet-latch` | formal | High | High | T > Tc; KV ≲ 25 kT; lattice shock | NdFeB holds a directional force with no power draw; soft iron does not |
| Superparamagnetism | `superparamagnetism` | queued | High | — | Grain volume below the KV/kT stability line | Same latch as the magnet; the buffer is now the grain, not the Curie point |
| Ferromagnetic hysteresis | `ferromagnetic-hysteresis` | queued | High | — | Loop area / coercivity → 0 (soft limit) | Write–erase cycle: remanence and coercivity as operating points of the latch |
| Ferroelectric remanence | `ferroelectric-remanence` | queued | High | — | T > Tc; coercive E exceeded; grain too small | Electrical twin of the magnet: remnant P at zero continuous field |
| Antiferromagnetic order | `antiferromagnetic-order` | queued | High | — | T > TN | Latched opposing sublattices; net macro moment cancels — a latch whose emergent output is zero force |
| Exchange bias | `exchange-bias` | queued | High | — | Blocking temperature of the pinned layer | Loop shift from an AFM/FM interface; a second latch pinning the first |
| Shape anisotropy | `shape-anisotropy` | queued | High | — | Aspect ratio → 1 (demag barrier vanishes) | Geometry / demagnetizing-field barrier; can latch without large K1 |
| Magnetic domains | `magnetic-domains` | queued | High | — | Wall energy vs. magnetostatic tradeoff fails (single-domain limit, or saturation) | How a large body partitions the aligned population; wall width is a measured buffer |

---

## 3. Gapped coherence

A protected collective mode with critical temperature, field, and/or current.

| Effect | Slug | Status | Data | Mapping | Dominant collapse | Notes |
|---|---|---|---|---|---|---|
| Superconductivity (zero resistance) | `superconductivity` | queued | High | — | T > Tc, H > Hc (Hc2), or I > Ic | R → 0 below a material-specific triple of critical values |
| Meissner effect | `meissner` | queued | High | — | H > Hc (type I) or vortex penetration (type II); λ / ξ violated | Field expulsion, not the same artifact as R = 0; London λ is the spatial buffer |
| Josephson effect | `josephson-effect` | queued | High | — | Junction too thick (Ic → 0); I > Ic; T > Tc | Pair current through a weak link; voltage–frequency lock V = (h/2e)ν |
| Flux quantization | `flux-quantization` | queued | High | — | Loop not superconducting; fluxoid not conserved | Closed superconducting loop holds Φ0 = h/2e |
| Type-II critical field / vortices | `type-ii-critical-field` | queued | High | — | Hc1 (first penetration), Hc2 (gap destroyed) | Mixed state as a lattice of phase defects; a second spatial scale next to λ and ξ |
| Superfluid helium-4 | `superfluid-helium-4` | queued | High | — | T > Tλ; critical velocity | Zero viscosity / fountain effect below 2.17 K; a gapped-coherence analog without charge |
| Bose–Einstein condensate | `bose-einstein-condensate` | queued | High | — | T > Tc(n); loss of phase coherence | Macro occupation of one mode; density sets Tc; harder mapping, clean thermal cliff |
| Quantum Hall effect | `quantum-hall-effect` | queued | High | — | B off a plateau; T or current too high | Quantized Hall resistance; gap + edge channel as the surviving hardware |

---

## 4. Threshold conversion

A discrete energetic or field gate. Below threshold the conversion does not occur.

| Effect | Slug | Status | Data | Mapping | Dominant collapse | Notes |
|---|---|---|---|---|---|---|
| Photoelectric threshold | `photoelectric-threshold` | queued | High | — | hν < φ | Electrons leave a metal only above a material work function; KE = hν − φ |
| Work function / thermionic emission | `work-function-thermionic` | queued | High | — | kT well below φ (Richardson tail dies) | Same energy gate as photoelectric, opened by heat instead of a photon |
| Semiconductor gap absorption | `semiconductor-gap-absorption` | queued | High | — | hν < Eg | Crystal goes from transmitting to absorbing at the band edge; Eg is the gate |
| X-ray absorption edge | `x-ray-absorption-edge` | queued | High | — | hν below the shell binding energy | Element-specific inner-shell gates; same pattern at keV |
| Ionization threshold | `ionization-threshold` | queued | High | — | E < I (atom / molecule) | Gas stays neutral below the ionization energy; a single-particle gate |
| Pair production | `pair-production` | queued | High | — | Eγ < 1.022 MeV; no nearby nucleus | Photon → e⁺e⁻ only above 2mec²; the sharpest textbook gate |
| Dielectric breakdown | `dielectric-breakdown` | queued | High | — | E < Ebd (no conversion); above it the insulator is destroyed | Field-opened conversion of insulator → conductor; messy after the first spark |
| Photoconductivity | `photoconductivity` | queued | High | — | hν < Eg (or trap depth) | Same gate as gap absorption, read out as a current instead of as opacity |

---

## 5. Lattice modes

The ion grid as coupled mechanical oscillators.

| Effect | Slug | Status | Data | Mapping | Dominant collapse | Notes |
|---|---|---|---|---|---|---|
| Phonon dispersion | `phonon-dispersion` | queued | High | — | Zone-boundary cutoff; mode softening / imaginary ω | Measured ω(q) is the lattice's allowed-clock map |
| Speed of sound | `speed-of-sound` | queued | High | — | Long-wavelength slope of the acoustic branch; fails in a vacuum or a liquid for shear | Macroscopic vs = √(C/ρ) as the long-wave output of the same grid |
| Debye cutoff | `debye-cutoff` | queued | High | — | ω > ωD (no more modes) | Finite node count ⇒ finite mode count; ΘD is the clock ceiling |
| Melting | `melting` | queued | High | — | Lindemann / measured Tm; loss of Bragg order | Lattice-mode collapse: the grid stops being a grid |
| Phonon thermal conductivity | `thermal-conductivity-phonon` | queued | High | — | Umklapp / boundary scattering kills the mean free path | Heat current in insulators as a phonon-population transport spec |
| Elasticity | `elasticity` | queued | High | — | Stress above the yield point (plastic / fracture) | Linear moduli as the small-amplitude restoring output; yield is the failure envelope |
| Piezoelectricity | `piezoelectricity` | queued | High | — | Above Tc of the polar phase; or centrosymmetric lattice | Strain ↔ polarization only in a lattice that lacks inversion |
| Magnetostriction | `magnetostriction` | queued | High | — | T > Tc of the ordered magnet; or lattice destroyed | Length change locked to the moment; mechanical twin of the magnet latch |
| Thermal expansion | `thermal-expansion` | queued | High | — | Anharmonicity → 0 (harmonic lattice does not expand) | Length change as the anharmonic correction; vanishes in the purely harmonic limit |

---

## 6. Ensemble averages

Stable macro constants or spectra that exist only as the averaged output of a large population.

| Effect | Slug | Status | Data | Mapping | Dominant collapse | Notes |
|---|---|---|---|---|---|---|
| Thermal equilibrium temperature | `thermal-equilibrium-temperature` | queued | High | — | Too few degrees of freedom for a stable average; or observation faster than equilibration | T as the synchronized output of a large population, not a primitive of one node |
| Ideal-gas pressure | `ideal-gas-pressure` | queued | High | — | Mean free path / N too small for P = nkT to be a stable reading | Wall force as the averaged momentum transfer |
| Blackbody spectrum | `blackbody-spectrum` | queued | High | — | Cavity modes under-populated; T undefined | Planck curve as the stable spectral output of a thermal EM population |
| Stefan–Boltzmann law | `stefan-boltzmann` | queued | High | — | Same envelope as the spectrum; surface not black | j = σT⁴ as the integrated emergent output |
| Electron heat capacity | `electron-heat-capacity` | queued | High | — | T → 0 (γT term vanishes into the noise); or a gapped spectrum | Linear-in-T electronic C as a Fermi-surface average |
| Brownian motion | `brownian-motion` | queued | High | — | Particle so large the kicks average to zero on the observation window | Visible jitter as incomplete averaging of molecular impacts |
| Johnson–Nyquist noise | `johnson-nyquist-noise` | queued | High | — | T → 0; or bandwidth → 0 | ⟨V²⟩ = 4kTRΔf as the electrical readout of the same thermal average |
| Curie paramagnetism | `curie-paramagnetism` | queued | High | — | T → 0 (order sets in) or T → ∞ (χ → 0) | χ ∝ 1/T as the unlocked-spin ensemble; contrast with the latched magnet |

---

## Slug list

Formal: `reflection` · `permanent-magnet-latch`

Queued: `refraction-dielectric` · `skin-effect` · `plasma-frequency-cutoff` · `surface-plasmon-resonance` · `total-internal-reflection` · `faraday-rotation` · `cyclotron-resonance` · `superparamagnetism` · `ferromagnetic-hysteresis` · `ferroelectric-remanence` · `antiferromagnetic-order` · `exchange-bias` · `shape-anisotropy` · `magnetic-domains` · `superconductivity` · `meissner` · `josephson-effect` · `flux-quantization` · `type-ii-critical-field` · `superfluid-helium-4` · `bose-einstein-condensate` · `quantum-hall-effect` · `photoelectric-threshold` · `work-function-thermionic` · `semiconductor-gap-absorption` · `x-ray-absorption-edge` · `ionization-threshold` · `pair-production` · `dielectric-breakdown` · `photoconductivity` · `phonon-dispersion` · `speed-of-sound` · `debye-cutoff` · `melting` · `thermal-conductivity-phonon` · `elasticity` · `piezoelectricity` · `magnetostriction` · `thermal-expansion` · `thermal-equilibrium-temperature` · `ideal-gas-pressure` · `blackbody-spectrum` · `stefan-boltzmann` · `electron-heat-capacity` · `brownian-motion` · `johnson-nyquist-noise` · `curie-paramagnetism`
