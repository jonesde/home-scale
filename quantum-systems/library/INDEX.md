# Effect library index

Entries are utility and internal-consistency tests, not interpretive claims. Families are QSA machine/collapse classes; conventional names are in the Effect column.

Every catalog row links to a file. Column meanings: [library README](README.md). Family definitions: [TAXONOMY.md](TAXONOMY.md).

**Sourcing:** 63 of 63 files carry opened references, evidence tags and threshold/crossover labels ([standard](README.md#sourcing-standard)); the Sourced column says which, and how deeply each was checked. A row marked — still holds numbers recalled by a language model; treat its "High" data rating as unverified until the file is converted.

**Status:** 63 formal · 0 draft · 0 queued. Mapping: 27 High · 36 Medium · 0 Low. Data is High except [dielectric breakdown](dielectric-breakdown.md) and [pyroelectric fusion](pyroelectric-fusion.md) (Medium).

Logically derived spec sheets, a shared-requirement audit, and an analog-slot map live in [`derived/`](derived/README.md) — not catalog rows. Conventional topics that stay **clauses** rather than files are listed under [Handbook topics not filed as effects](#handbook-topics-not-filed-as-effects). Device applications: [`../application/`](../application/README.md).

Medium mapping is not a failed entry. It means the collapse is real and the machine class is assigned, but a hardware scale is statistical, mesoscale, or taken from a measured constant rather than derived. Those are the places a second pass should tighten.

---

## 1. Collective field response

Many charged nodes must occupy a minimum coherent volume and synchronize before a stable macroscopic EM output appears.

| Effect | Slug | Status | Data | Mapping | Sourced | Dominant collapse | Notes |
|---|---|---|---|---|---|---|---|
| [Reflection (electron-cloud response)](reflection.md) | `reflection` | formal | High | Medium | deep | Drive above the plasma or interband edge; loss of dc continuity in a deposited film. Thickness is a smooth crossover with no minimum | Visible light returns from Ag/Al; reflectance falls smoothly as the film thins (Ag at half its bulk value near 12–14 nm) and standard thin-film optics reproduces it; a collective response is measured at one atomic layer |
| [Refraction / dielectric polarization](refraction-dielectric.md) | `refraction-dielectric` | formal | High | Medium | standard | n−1 → 0 (X-ray / vacuum / path ≪ λ); breakdown is a different family | Snell's law as bound-charge output; no single nm-scale cliff |
| [Skin effect](skin-effect.md) | `skin-effect` | formal | High | High | deep | No edge: δ is the 1/e length of an exponential; the superconducting transition is the one threshold | Steady drive, a single pulse and a moving contact follow three different rules; Cu 66 µm at 1 MHz and 8.4 mm at 60 Hz, but 3–6 mm for a 0.2–0.7 ms pulse |
| [Plasma-frequency cutoff](plasma-frequency-cutoff.md) | `plasma-frequency-cutoff` | formal | High | High | deep | ω above the plasma edge: sharp only in the collisionless model, a steep crossover in a real metal | Clock-failure twin of reflection; Al and Na sit 3–5 % below the free-electron value, K/Rb/Cs 13–18 %, Ag at 0.42 of it (3.8 eV measured against 9 eV) |
| [Surface plasmon resonance](surface-plasmon-resonance.md) | `surface-plasmon-resonance` | formal | High | Medium | standard | No momentum match; Re ε > 0; metal fill below about 0.4. Film thickness is a crossover around an optimum | Interface-bound mode; needs a metal–dielectric face plus a coupler; Au optimum near 45–50 nm at 633 nm; island films lose the mode below a fill fraction of about 0.4 |
| [Total internal reflection](total-internal-reflection.md) | `total-internal-reflection` | formal | High | High | light | θ < θc, or n1 ≤ n2 (thresholds); a third body in the evanescent field frustrates it continuously with gap width | Geometry / index gate on the same n as refraction |
| [Faraday rotation](faraday-rotation.md) | `faraday-rotation` | formal | High | Medium | light | B → 0 or path below the Verdet · B · L detection budget | Polarization rotates as VBL; product budget, not a hard cliff |
| [Cyclotron resonance](cyclotron-resonance.md) | `cyclotron-resonance` | formal | High | High | light | ω ≠ ωc; visibility is a crossover in mobility × field (ωc τ) | Absorption at eB/m*; m* is a measured output; needs a long enough scattering time |
| [Aharonov–Bohm (enclosed-flux phase)](aharonov-bohm.md) | `aharonov-bohm` | formal | High | High | light | Path does not enclose Φ, or coherence lost | Fringe shift periodic in h/e; the shielded electron-beam test is from 1986; metal rings also show a weaker h/2e component |
| [Casimir force (mode-cutoff attraction)](casimir-force.md) | `casimir-force` | formal | High | Medium | standard | Gap too large (thermal regime above about 3 µm). Conducting contrast is a crossover: thin or transparent faces reduce the force by up to half | Uncharged plates attract ~1/d⁴; 1.3 mPa at 1 μm for ideal plates, real metals about half of ideal at 0.1 μm; prefactor taken |

---

## 2. Latched order

An energy barrier holds a directional or configurational state at zero continuous power.

| Effect | Slug | Status | Data | Mapping | Sourced | Dominant collapse | Notes |
|---|---|---|---|---|---|---|---|
| [Permanent magnet (directional latch)](permanent-magnet-latch.md) | `permanent-magnet-latch` | formal | High | High | deep | T > Tc (exchange threshold); reverse field; shock; KV ≲ 25 kT only at a few nm | NdFeB holds a directional force with no power draw; soft iron does not; real coercivity is under a fifth of the anisotropy field |
| [Superparamagnetism](superparamagnetism.md) | `superparamagnetism` | formal | High | High | deep | KV ≲ kT ln(τm/τ0), a crossover; 25 kT is the 100 s convention | Thermal loss of direction in a small grain; Nd₂Fe₁₄B about 3.5 nm, magnetite 20–50 nm at room temperature; depends on the observer's clock |
| [Ferromagnetic hysteresis](ferromagnetic-hysteresis.md) | `ferromagnetic-hysteresis` | formal | High | High | deep | T > Tc (threshold); coercivity itself is a continuum over six decades, so the soft limit is a crossover | Write–erase cycle; hold costs zero; the major-loop area is one protocol's write cost, with a measured floor near kT for a single-domain bit; Hc is 15–20 % of Ha in sintered Nd-Fe-B |
| [Ferroelectric remanence](ferroelectric-remanence.md) | `ferroelectric-remanence` | formal | High | Medium | standard | T > Tc (threshold); reverse field and thin or poorly screened films are crossovers | Electrical twin: remnant P at E = 0; Ec and the depolarization buffer stay mesoscale |
| [Antiferromagnetic order](antiferromagnetic-order.md) | `antiferromagnetic-order` | formal | High | High | deep | T > TN; spin-flop field in uniaxial crystals | Ordered opposing sublattices; net macro moment ~0; Curie–Weiss θ up to five times TN in the monoxides |
| [Exchange bias](exchange-bias.md) | `exchange-bias` | formal | High | Medium | deep | T > TB of the pin, a rate-dependent crossover (TB ≤ TN of the layer); AFM thinner than a few nm | Second ordered body pinning the first; can stabilize a grain that is superparamagnetic alone; interface energy remains unspecified |
| [Shape anisotropy](shape-anisotropy.md) | `shape-anisotropy` | formal | High | Medium | deep | Aspect ratio → 1, a continuous zero (half the needle limit is reached near aspect ratio 2) | Geometry / demag barrier; an Fe needle reaches at most 0.92 MJ/m³, a semi-hard latch; real particles reverse at 15–19 % of the ideal field |
| [Magnetic domains](magnetic-domains.md) | `magnetic-domains` | formal | High | Medium | deep | T > Tc (threshold); single-domain size and saturation are crossovers | How a large body partitions the aligned population; wall width by formula 4–63 nm, measured 4–9 nm in Nd₂Fe₁₄B; exchange stiffness is inferred, and tabulations differ 2.4× |
| [Ferroelectric domains](ferroelectric-domains.md) | `ferroelectric-domains` | formal | Medium | Medium | standard | Screening and applied field change the pattern continuously; no sharp single-domain size was found | Polar twin of magnetic domains; nm-class walls; charged walls possible; Pr can remain after the pattern is gone |
| [Hydrogen in metals](hydrogen-in-metals.md) | `hydrogen-in-metals` | formal | Medium | Medium | deep | Hydride plateau: a first-order transition with hysteresis (Pd about 2 kPa at 298 K; Ni above 6 kbar). Solubility and detrapping are crossovers | Sieverts solubility (H/Ni 1.8×10⁻⁵ at 1 bar, 298 K); Pd reaches H/Pd 0.68 at 1 atm with 3.5 % linear strain; trapped hydrogen is bound per atom; hydride hysteresis is size-dependent below about 30 nm in Pd |

---

## 3. Gapped coherence

A protected collective mode with critical temperature, field, and/or current.

| Effect | Slug | Status | Data | Mapping | Sourced | Dominant collapse | Notes |
|---|---|---|---|---|---|---|---|
| [Superconductivity (zero resistance)](superconductivity.md) | `superconductivity` | formal | High | Medium | light | T > Tc, H > Hc (Hc2), or I > Ic | R → 0 below a material-specific triple; coherent volume is not one number; pinning still unspecified |
| [Meissner effect](meissner.md) | `meissner` | formal | High | High | light | H > Hc (type I) or H > Hc1 (type II); thickness ≪ λ | Field expulsion with χ = −1; London λ is the spatial buffer; not the same artifact as R = 0 |
| [Josephson effect](josephson-effect.md) | `josephson-effect` | formal | High | High | light | Junction too thick (Ic → 0); I > Ic; T > Tc | Weak-link pair current; voltage–frequency lock 483.6 MHz/μV |
| [Flux quantization](flux-quantization.md) | `flux-quantization` | formal | High | High | light | Loop not superconducting; phase slips destabilize the integer in wires near 10 nm | Closed loop holds n Φ0 = n h/2e |
| [Type-II critical field / vortices](type-ii-critical-field.md) | `type-ii-critical-field` | formal | High | High | light | Hc1 first penetration; Hc2 gap destroyed; unpinned flux flow | Mixed-state vortex lattice; extra spatial scale √(Φ0/B) |
| [Superfluid helium-4](superfluid-helium-4.md) | `superfluid-helium-4` | formal | High | High | light | T > Tλ (2.17 K); v > vc | Chargeless superflow / fountain; family name “gapped” is slightly loose (no pairing gap) |
| [Bose–Einstein condensate](bose-einstein-condensate.md) | `bose-einstein-condensate` | formal | High | Medium | light | T > Tc(n), or density drops; phase coherence lost | Dilute alkali BEC; clean thermal/density cliff; no measured pairing gap; not a zero-power latch |
| [Quantum Hall effect](quantum-hall-effect.md) | `quantum-hall-effect` | formal | High | Medium | light | B off a plateau; T or current too high; 2DEG lost | Integer RH = h/(ν e²); gap + edge channel recorded, not derived |
| [Quantum point contact](quantum-point-contact.md) | `quantum-point-contact` | formal | High | Medium | light | Pinch-off; T or mfp wash the steps | 1D conductance steps at 2e²/h; no B required; not QHE |
| [Neutron gravitational states](neutron-gravitational-states.md) | `neutron-gravitational-states` | formal | High | Medium | light | Absorber below z1; not UCN; no mirror | UCN bound in mgz + mirror; z1 ≈ 13.7 μm; gapped name loose |

---

## 4. Threshold conversion

A discrete energetic or field gate. Below threshold the conversion does not occur.

| Effect | Slug | Status | Data | Mapping | Sourced | Dominant collapse | Notes |
|---|---|---|---|---|---|---|---|
| [Photoelectric threshold](photoelectric-threshold.md) | `photoelectric-threshold` | formal | High | High | light | hν < φ (typical φ 2–6 eV) | Electrons leave a metal only above the work function; KE = hν − φ; contrast case for reflection |
| [Work function / thermionic emission](work-function-thermionic.md) | `work-function-thermionic` | formal | High | High | standard | Emission falls as exp(−φ/kT), a crossover with no cut-off temperature | Same surface gate as photoelectric on a clean uniform surface, opened by heat; W 4.55 eV |
| [Semiconductor gap absorption](semiconductor-gap-absorption.md) | `semiconductor-gap-absorption` | formal | High | High | light | hν < Eg | Crystal transmits below the gap and absorbs above; Si 1.12 eV, Ge 0.66 eV, GaAs 1.42 eV |
| [X-ray absorption edge](x-ray-absorption-edge.md) | `x-ray-absorption-edge` | formal | High | High | light | hν below the shell binding energy | Element-specific inner-shell gates; Cu K-edge 8.979 keV |
| [Ionization threshold](ionization-threshold.md) | `ionization-threshold` | formal | High | High | standard | E < I | Gas stays neutral below the binding energy; H 13.598 eV, He 24.587 eV |
| [Pair production](pair-production.md) | `pair-production` | formal | High | High | light | Eγ < 1.022 MeV; no nearby nucleus | Photon → e⁺e⁻ only above 2mec² and with a momentum sink |
| [Muon-catalyzed fusion](muon-catalyzed-fusion.md) | `muon-catalyzed-fusion` | formal | High | High | standard | No muon; muon decay and α-sticking, which add (about 150 fusions per muon at best) | Published experiment; needs a muon and a host D₂/DT molecule; releases about 2.6 GeV per muon against an estimated 5–10 GeV to make one |
| [Dielectric breakdown](dielectric-breakdown.md) | `dielectric-breakdown` | formal | Medium | Medium | deep | Field below breakdown; the value is statistical and set by pressure × gap (Paschen), gap size and pulse length | Air 3 MV/m holds for mm–cm gaps only; Paschen minimum 327–352 V near 7.5 µm at 1 atm; below about 5–10 µm field emission lowers the voltage again |
| [Electrical contacts](electrical-contacts.md) | `electrical-contacts` | formal | Medium | Medium | deep | Contact voltage reaches the softening or melting voltage (Cu melts at 0.43 V); surface films puncture at 10⁷–10⁸ V/m | Constriction resistance at a-spots; bead chains plateau at 0.2–0.4 V per contact by micro-welding; nothing is measured for a powder slurry |
| [Photoconductivity](photoconductivity.md) | `photoconductivity` | formal | High | High | light | hν < Eg or trap depth | Same gap gate as absorption, read out as current; gain set by lifetime / transit time |
| [Coulomb blockade](coulomb-blockade.md) | `coulomb-blockade` | formal | High | High | light | Thermal smearing and loss of tunnel resistance are crossovers, ending at a ballistic contact near 2e²/h | Single-electron charging gate; island aF–fF |
| [Deuteron photodisintegration](deuteron-photodisintegration.md) | `deuteron-photodisintegration` | formal | High | High | standard | Eγ below 2.2259 MeV (binding energy plus recoil) | Photon unbinds d → p+n; opposite arrow to μCF |
| [Pyroelectric fusion](pyroelectric-fusion.md) | `pyroelectric-fusion` | formal | Medium | High | standard | No ΔT or no D; potential too low is a crossover (D–D cross-section negligible below 20 keV) | Published device (2005, replicated 2006): a polar crystal accelerates D; 10⁴–10⁵ neutrons at 2.45 MeV per thermal cycle of hundreds of seconds |
| [Coherent neutrino–nucleus scattering](coherent-neutrino-scattering.md) | `coherent-neutrino-scattering` | formal | High | Medium | light | Coherence is lost gradually as qR grows (full below about 10 MeV); no nucleus | CEνNS N² recoils (COHERENT); coherence window, no IBD threshold |

---

## 5. Lattice modes

The ion grid as coupled mechanical oscillators.

| Effect | Slug | Status | Data | Mapping | Sourced | Dominant collapse | Notes |
|---|---|---|---|---|---|---|---|
| [Phonon dispersion](phonon-dispersion.md) | `phonon-dispersion` | formal | High | Medium | light | Zone-boundary cutoff; mode softening; loss of Bragg order | Measured ω(q) is the lattice allowed-clock map; no single hardware number |
| [Speed of sound](speed-of-sound.md) | `speed-of-sound` | formal | High | High | standard | No medium; no shear wave in a liquid at acoustic frequencies; qa ~ 1 ends the long-wave slope | Long-wave vs = √(C/ρ); no shear sound in a vacuum or a liquid |
| [Debye cutoff](debye-cutoff.md) | `debye-cutoff` | formal | High | High | light | Modes end at the top measured branch; the Debye frequency is a model cut that lies below it in Si and diamond | Finite N ⇒ 3N modes; ΘD is the clock ceiling |
| [Melting](melting.md) | `melting` | formal | High | Medium | deep | T → Tm; loss of Bragg order and shear | The grid stops being a grid; Lindemann is a criterion, not a derivation |
| [Phonon thermal conductivity](thermal-conductivity-phonon.md) | `thermal-conductivity-phonon` | formal | Medium | Medium | standard | Umklapp / boundary / amorphization kills the mean free path | κ = (1/3) C v ℓ for the lattice channel; diamond 2200–3100 W/m/K; in metals phonons carry only a few per cent (Cu 4.7 %) |
| [Elasticity](elasticity.md) | `elasticity` | formal | High | Medium | deep | Stress above yield or fracture; the shear modulus drops in a step at melting | Hooke at small strain; dislocations are the mesoscale gap |
| [Piezoelectricity](piezoelectricity.md) | `piezoelectricity` | formal | High | Medium | standard | Inversion symmetry present; T > Tc; depoling below Tc is a crossover | Strain ↔ P only without inversion; coupling taken from handbook d_ij |
| [Magnetostriction](magnetostriction.md) | `magnetostriction` | formal | High | Medium | deep | T > Tc (the strain falls continuously to zero there); lattice destroyed | Length change locked to the moment and even in M; Ni −35 to −40 ppm, Terfenol-D 1000–2000 ppm; clamped Ni gives 7–9 MPa, about 5 % of yield |
| [Thermal expansion](thermal-expansion.md) | `thermal-expansion` | formal | High | Medium | standard | Vanishes for a harmonic lattice; in real solids a continuous function of temperature that can change sign | Metals 4.5–30 × 10⁻⁶ /K at 293 K; Invar's low value holds only in a temperature window; Si and fused silica contract at low temperature |
| [Mössbauer effect](mossbauer-effect.md) | `mossbauer-effect` | formal | High | Medium | light | Recoilless fraction falls continuously with temperature and with diffusion; no resonance in ordinary liquids | Recoilless 14.4 keV ⁵⁷Fe resonance; needs a binding solid host, crystalline or glassy |

---

## 6. Ensemble averages

Stable macro constants or spectra that exist only as the averaged output of a large population.

Every mapping in this family is Medium for the same recorded reason: the hardware scale is statistical. There is no universal N-cliff analogous to a 10 nm film or a Curie point.

| Effect | Slug | Status | Data | Mapping | Sourced | Dominant collapse | Notes |
|---|---|---|---|---|---|---|---|
| [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) | `thermal-equilibrium-temperature` | formal | High | Medium | light | Too few independent contributors, or observation faster than the exchange window | T is the stable averaged output of a large population; no universal N |
| [Ideal-gas pressure](ideal-gas-pressure.md) | `ideal-gas-pressure` | formal | High | Medium | light | Continuum picture fails gradually over Kn 0.1–10; N too small for a stable reading | Wall force P = nkT; continuum hydro is a second, density-tracking envelope |
| [Blackbody spectrum](blackbody-spectrum.md) | `blackbody-spectrum` | formal | High | Medium | light | Cavity modes under-populated; wall T undefined; surface not black | Planck u(ν,T) as the thermal EM average; Rayleigh–Jeans is the failed high-ν envelope |
| [Stefan–Boltzmann law](stefan-boltzmann.md) | `stefan-boltzmann` | formal | High | Medium | light | Same envelope as the spectrum; surface not black; T → 0 | j = εσT⁴ is the integral of the Planck curve; σ is defined |
| [Electron heat capacity](electron-heat-capacity.md) | `electron-heat-capacity` | formal | High | Medium | standard | T → 0 (γT into noise), or a gapped spectrum | Ce = γT from a Fermi-surface slice ~ T/TF; a superconducting gap removes the linear term |
| [Brownian motion](brownian-motion.md) | `brownian-motion` | formal | High | Medium | light | Particle so large the kicks average below the window’s resolution | Visible jitter is an incomplete impact average; D = kT/γ; large bodies look still |
| [Johnson–Nyquist noise](johnson-nyquist-noise.md) | `johnson-nyquist-noise` | formal | High | Medium | light | T → 0 or Δf → 0; hf ≳ kT leaves the classical envelope | ⟨V²⟩ = 4kTRΔf; electrical FDR twin of Brownian; no resistor-volume cliff |
| [Curie paramagnetism](curie-paramagnetism.md) | `curie-paramagnetism` | formal | High | Medium | standard | Magnetic ordering at Tc or TN (threshold); saturation and the 1/T fall are crossovers | χ = C/T unlocked-spin ensemble; contrast with the latched magnet / AFM order |
| [Electrical resistivity and Joule heating](electrical-resistivity.md) | `electrical-resistivity` | formal | High | Medium | deep | The superconducting transition is the one sharp collapse; steps at melting; heating to melt set by the action integral | ρ(T) as a scattering average; Cu 1.678×10⁻⁸ Ω·m at 293 K; action to the start of melting about 8×10¹⁶ A²·s/m⁴ for Cu |

---

## Handbook topics not filed as effects

Conventional names a handbook would give their own chapter. Here they are **clauses** on existing files, not catalog rows: the collapse is already owned, or there is no portable number, or the topic is a write channel of a partition rather than a distinct output. Analog slots (which machine owns latch / loop / partition, and which holes are still file-worthy) live in [`derived/analog-slots.md`](derived/analog-slots.md).

Do not add a file to “complete a chapter.” Add one only when the collapse is sharp and is not already a clause.

| Name | What it is here | See |
|---|---|---|
| Thin-film and small-crystal loss of polarization | Net *P* is lost continuously as a film thins or its faces are less well screened; the polar phase itself survives to 1.2 nm films and 5 nm crystals. Not a thermal-volume limit, so not a twin of superparamagnetism (an earlier version filed it as "superparaelectric collapse"). | [ferroelectric-remanence](ferroelectric-remanence.md), [ferroelectric-domains](ferroelectric-domains.md) |
| Ferroelectric *P*–*E* loop | Write/erase cycle of the polar latch. Magnet side split this out as hysteresis; polar remanence already owns loop area and *E<sub>c</sub>*. | [ferroelectric-remanence](ferroelectric-remanence.md), [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) |
| Polar slab depolarization | Geometry / uncompensated *P* empties the well (*E<sub>d</sub>* ~ *P*/ε). Electrical analog of shape anisotropy; still an open mesoscale buffer, not a second file. | [ferroelectric-remanence](ferroelectric-remanence.md), [shape-anisotropy](shape-anisotropy.md), [depolarization-fuse](../application/depolarization-fuse.md) |
| Optical domain-wall write | Visible light is said to move ferroelectric walls (photovoltaic / thermal / flexoelectric); no source was opened for this when the ferroelectric files were sourced. A write channel of the partition, not a photon-energy gate. | [ferroelectric-domains](ferroelectric-domains.md), [photoelectric-threshold](photoelectric-threshold.md) |
| Charged-wall addressing | Head-to-head / tail-to-tail walls carry bound charge and can conduct. Extra constraint on the polar partition, not a nested pin and not a 13th design. | [ferroelectric-domains](ferroelectric-domains.md), [exchange-bias](exchange-bias.md) |
| Magneto-optical Kerr | Polarization rotation on *reflection* from a magnetized surface. Faraday’s reflection-side twin; same *eB/m* population, not a second collapse. | [faraday-rotation](faraday-rotation.md), [reflection](reflection.md) |
| Ferroelasticity (90° walls) | Strain switches with a 90° polar wall. Coupling already owned by piezo + this partition + the elastic grid. | [ferroelectric-domains](ferroelectric-domains.md), [piezoelectricity](piezoelectricity.md), [elasticity](elasticity.md) |

---

## Slug list

`aharonov-bohm` · `antiferromagnetic-order` · `blackbody-spectrum` · `bose-einstein-condensate` · `brownian-motion` · `casimir-force` · `coherent-neutrino-scattering` · `coulomb-blockade` · `curie-paramagnetism` · `cyclotron-resonance` · `debye-cutoff` · `deuteron-photodisintegration` · `dielectric-breakdown` · `elasticity` · `electrical-contacts` · `electrical-resistivity` · `electron-heat-capacity` · `exchange-bias` · `faraday-rotation` · `ferroelectric-domains` · `ferroelectric-remanence` · `ferromagnetic-hysteresis` · `flux-quantization` · `hydrogen-in-metals` · `ideal-gas-pressure` · `ionization-threshold` · `johnson-nyquist-noise` · `josephson-effect` · `magnetic-domains` · `magnetostriction` · `meissner` · `melting` · `mossbauer-effect` · `muon-catalyzed-fusion` · `neutron-gravitational-states` · `pair-production` · `permanent-magnet-latch` · `phonon-dispersion` · `photoconductivity` · `photoelectric-threshold` · `piezoelectricity` · `plasma-frequency-cutoff` · `pyroelectric-fusion` · `quantum-hall-effect` · `quantum-point-contact` · `reflection` · `refraction-dielectric` · `semiconductor-gap-absorption` · `shape-anisotropy` · `skin-effect` · `speed-of-sound` · `stefan-boltzmann` · `superconductivity` · `superfluid-helium-4` · `superparamagnetism` · `surface-plasmon-resonance` · `thermal-conductivity-phonon` · `thermal-equilibrium-temperature` · `thermal-expansion` · `total-internal-reflection` · `type-ii-critical-field` · `work-function-thermionic` · `x-ray-absorption-edge`
