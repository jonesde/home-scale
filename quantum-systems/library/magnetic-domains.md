---
id: magnetic-domains
title: Magnetic Domains (Partitioned Alignment)
status: formal
family: latched-order
constraints:
  - spatial-buffer
  - energy-barrier
  - field-threshold
  - mechanical-lattice
confidence_data: high
confidence_mapping: medium
related:
  - permanent-magnet-latch
  - ferromagnetic-hysteresis
  - shape-anisotropy
  - superparamagnetism
  - exchange-bias
  - magnetostriction
  - ferroelectric-domains
updated: 2026-08-20
---

# Magnetic Domains (Partitioned Alignment)

### 4.1 Effect Name

Magnetic domains (partitioned alignment)

### 4.2 Macroscopic Observation

A large ferromagnetic body is not a single aligned block. It partitions into regions of essentially uniform magnetization (domains) separated by thin walls. In zero applied field the net moment can be far below saturation even though each domain is locally ordered. An applied field grows favorably oriented domains and moves walls; at saturation the walls are gone and the body is one domain. Below a material-dependent particle size, walls are not observed and the particle is single-domain. Wall positions are imaged (Bitter patterns, Kerr, MFM) and are static at rest: no continuous power is required to hold a given partition.

### 4.3 Established Quantitative Boundaries

- Wall width scales as \(\sqrt{A/K}\) (Bloch form \(\delta_w \approx \pi\sqrt{A/K}\)). Exchange stiffness \(A\) is of order \(10^{-11}\,\mathrm{J\,m^{-1}}\) in Fe, Co, Ni. With Fe-like cubic \(K_1\) (\(\sim 10^4\,\mathrm{J\,m^{-3}}\) class) that width is tens of nanometres. With NdFeB-like \(K_1 \approx 4.5\,\mathrm{MJ\,m^{-3}}\) it is a few nanometres. The wall is a measured spatial buffer, not a mathematical point.
- Wall energy per unit area scales as \(\sqrt{AK}\) (Bloch form \(\gamma_w \approx 4\sqrt{AK}\)). Soft, low-\(K\) magnets have cheap, wide walls and large domains; hard magnets have expensive, narrow walls and finer domains.
- Single-domain critical size: the particle diameter at which inserting a wall costs more than the magnetostatic energy it would save. Continuum estimates scale as \(\sqrt{AK}/(\mu_0 M_s^2)\) (Kittel / Brown class). In soft 3d metals that length is tens of nanometres; in high-\(K\) magnets it is larger. Prefactors depend on assumed shape and wall type; the existence of a size cliff is the measured fact.
- Saturation: a large enough applied field drives walls out. The technical saturation field is microstructure-dependent and is not \(H_a\).
- A static domain pattern at rest produces no continuous hysteresis heat. Wall motion around a [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) loop dissipates the loop area.

**Data confidence:** High — \(\sqrt{A/K}\) and \(\sqrt{AK}\) scaling, the soft-wide / hard-narrow contrast, imaging of walls, and the existence of a single-domain size are standard. A numerical critical diameter for a named particle is medium (shape- and formula-dependent).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Continuum Bloch wall (180°, uniaxial):

  \[
  \delta_w \approx \pi\sqrt{\frac{A}{K}},\qquad \gamma_w \approx 4\sqrt{AK}
  \]

  Néel walls (magnetization rotating in-plane) replace this form in thin films, where the stray-field cost of a Bloch rotation is larger. The scaling \(\delta_w \sim \sqrt{A/K}\) remains the descriptive core.

- Magnetostatic energy of a uniformly magnetized body is of order \((\mu_0/2)M_s^2 \times\) (shape factor) \(\times V\) ([shape-anisotropy](shape-anisotropy.md)). Partitioning into domains reduces that term and adds wall area \(\times\gamma_w\). Observed domain size is the scale at which those two measured costs are comparable.

- Single-domain condition (schematic): wall cost \(\gtrsim\) magnetostatic saving. The resulting critical diameter tracks \(\gamma_w / (\mu_0 M_s^2)\).

- Applied-field term \(-\mu_0\mathbf{M}\cdot\mathbf{H}\) grows one set of domains at the expense of another until walls are expelled (saturation).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two nested buffers:
  1. **Wall.** A transition strip of width \(\sim\sqrt{A/K}\) in which the moment rotates between adjacent latched directions. Narrower than that and the continuum wall is not a resolved object; the two domains have merged.
  2. **Domain pattern.** A body large enough that the magnetostatic cost of a single-domain state exceeds the wall energy of a partition. Below the single-domain size the pattern never forms; the particle is one latch cell. There is no universal millimetre-scale domain period.

- **Clock rate / latency.** Moments inside a wall still precess at the \(\approx 28\,\mathrm{GHz\,T^{-1}}\) carrier. Pattern changes are wall-motion events whose speed is set by damping, eddy currents, and pinning, and is far below that carrier. A static pattern has no ongoing clock cost.

- **Energy barriers or thresholds.** Locally, each domain is the same anisotropy latch as [permanent-magnet-latch](permanent-magnet-latch.md). The wall is a distributed transition whose energy per area \(\sim\sqrt{AK}\) is the cost of a partition. Pinning of walls at grains and defects is the mesoscale barrier that shows up as \(H_c\) on the loop. Holding a static partition costs zero continuous power.

- **Dominant failure modes.**
  - Single-domain limit: particle below the wall-vs-magnetostatic cliff \(\to\) no domain pattern (one latch, not a partition).
  - Saturation: applied \(H\) expels walls \(\to\) one domain spanning the body. The local latch is still present; the *partition* is gone.
  - Soft / low-\(K\): walls cheap and wide, pinning weak \(\to\) the pattern does not survive \(H\to 0\) as a useful net remanence.
  - Thermal: \(T > T_C\) \(\to\) local order gone \(\to\) no domains. Grain-scale \(KV\) collapse is [superparamagnetism](superparamagnetism.md), below the domain problem.
  - Mechanical: plastic strain and grain fracture rewrite pinning and can scramble the pattern without reaching \(T_C\).

- **Emergent constant or stable output.** A static partition of the aligned population, with a measured wall width \(\sim\sqrt{A/K}\) and a net moment anywhere from \(\approx 0\) (closed pattern) to saturation (walls expelled), at zero continuous power while the pattern is at rest.

### 4.6 Internal Consistency Notes

Domains do not contradict the latch: they *are* many latches sharing a body, with walls as the finite-width boundaries. Zero hold power on a static pattern, dissipative cost only when walls move, and two sharp collapses (single-domain size, saturation) fit the family. Wall width is the rare latched-order quantity that is a length first, not a temperature or a field.

The mapping is not closed on pattern selection. Why one sample shows closure domains, another stripes, another a maze is a magnetostatic-plus-pinning problem whose output is imaged, not derived here from node rules. Continuum \(A\) and \(K\) are taken as measured inputs to \(\delta_w\) and \(\gamma_w\); QSA does not yet produce those two stiffnesses from a more primitive buffer. The same mesoscale gap as on the hysteresis file reappears as wall pinning \(\to H_c\). None of those gaps moves the two collapse cliffs.

The electrical twin is [ferroelectric-domains](ferroelectric-domains.md). Polar walls can carry bound charge and need screening; magnetic Bloch/Néel walls pay a magnetostatic cost instead. Do not quote \(\sqrt{A/K}\) tens-of-nanometres as a ferroelectric wall width.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — wall-width scaling, the single-domain size, saturation, and zero hold power are solid, but pattern choice and the pinning that sets technical \(H_c\) remain mesoscale data without a closed specification.

## Related entries

- [permanent-magnet-latch](permanent-magnet-latch.md) — the local directional state of which each domain is a copy
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — the write / erase cycle traced mostly by wall motion in bulk
- [shape-anisotropy](shape-anisotropy.md) — magnetostatic energy that, unpartitioned, is the geometry barrier
- [superparamagnetism](superparamagnetism.md) — below both the single-domain size and the \(KV\) stability line
- [exchange-bias](exchange-bias.md) — interface pinning of FM domains by an AFM latch
- [magnetostriction](magnetostriction.md) — strain locked to the local domain direction
- [ferroelectric-domains](ferroelectric-domains.md) — polar twin: partitioned *P*, nm-class walls, charged walls possible
