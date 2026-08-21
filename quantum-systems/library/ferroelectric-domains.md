---
id: ferroelectric-domains
title: Ferroelectric Domains (Partitioned Polar Alignment)
status: formal
family: latched-order
constraints:
  - spatial-buffer
  - energy-barrier
  - field-threshold
  - thermal
  - mechanical-lattice
confidence_data: high
confidence_mapping: medium
related:
  - ferroelectric-remanence
  - magnetic-domains
  - piezoelectricity
  - ferromagnetic-hysteresis
  - superparamagnetism
  - shape-anisotropy
  - type-ii-critical-field
  - elasticity
updated: 2026-08-20
---

# Ferroelectric Domains (Partitioned Polar Alignment)

### 4.1 Effect Name

Ferroelectric domains (partitioned polar alignment)

### 4.2 Macroscopic Observation

A large ferroelectric crystal or ceramic is not one polar block. It partitions into regions of essentially uniform polarization (domains) separated by thin walls. At zero applied field the net polarization can be far below the spontaneous value even though each domain is locally latched. Net \(P\) ranges from \(\approx 0\) (closed pattern) to \(P_s\) (walls expelled). An applied electric field grows favorably oriented domains and moves walls; after poling the walls are gone and the body is one domain with a remanent \(P\) owned by [ferroelectric-remanence](ferroelectric-remanence.md). Below a material- and process-dependent size, walls are not observed and the particle is a single domain. Wall positions are imaged (polarized light, etching, PFM, SHG) and are static at rest: no continuous power is required to hold a given partition.

### 4.3 Established Quantitative Boundaries

- Two wall kinds in tetragonal \(\mathrm{BaTiO_3}\) (and the same split in other ferroelectrics). A **180°** wall reverses \(P\) only. A **90°** wall also switches the tetragonal \(c\) axis and is ferroelastic: strain changes with the wall. 90° walls therefore sit on this partition *and* on the strain channel of [piezoelectricity](piezoelectricity.md).
- Imaged 180° walls in tetragonal \(\mathrm{BaTiO_3}\) are atomically sharp, of order one to two unit cells (\(\sim 0.5\,\mathrm{nm}\) class). 90° walls are thicker, still nanometre class (typically a few nanometres). Ferroelectric walls as a class sit in the \(1\)–\(10\,\mathrm{nm}\) range. Do not quote magnetic \(\sqrt{A/K}\) tens-of-nanometres as this number.
- Charged vs neutral. A wall whose normal has a jump in \(P\) (head-to-head or tail-to-tail) carries bound charge \(\sigma_b = (\mathbf{P}_2-\mathbf{P}_1)\cdot\hat{\mathbf{n}}\). Neutral 180° walls do not. Charged walls need screening (free charge, defects, or conductivity along the wall). Wall conductivity can sit many orders of magnitude above the bulk. Bloch/Néel magnetic walls are not bound-charge sheets; this electrostatic extra is the polar contrast with [magnetic-domains](magnetic-domains.md).
- Single-domain / no-pattern size: the particle size at which inserting a wall costs more than the electrostatic (depolarization) energy it would save. The existence of that cliff is the measured fact. Reported \(\mathrm{BaTiO_3}\) classes run from \(\sim 10\,\mathrm{nm}\) (order / superparaelectric collapse, owned by remanence) to tens of nanometres (single-domain still ferroelectric). Prefactors depend on electrodes, screening, and shape. This is not NdFeB’s \(\sim 30\,\mathrm{nm}\) *KV* line and it does not close the thin-film depolarization buffer.
- Saturation / poling: a large enough applied \(E\) drives walls out. The technical poling field is microstructure-dependent and is not the Landau well of a perfect crystal. After the walls are gone the body can still hold remanent \(P\) at \(E = 0\).
- A static domain pattern at rest produces no continuous hysteresis heat. Wall motion around a \(P\)–\(E\) loop dissipates the loop area (that loop is owned by remanence). An optical beam can move walls in some crystals (photovoltaic, thermal, or flexoelectric write); that is a write channel of this partition, not a photon-energy conversion gate.

**Data confidence:** High — 180° vs 90°, nm-class wall width, charged vs neutral walls, imaging of static patterns, and the existence of a no-pattern size are standard. A numerical critical diameter for a named particle, and a portable wall-energy density, are medium (process- and formula-dependent).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Bound charge on a wall:

  \[
  \sigma_b = (\mathbf{P}_2 - \mathbf{P}_1)\cdot\hat{\mathbf{n}}
  \]

  Neutral 180°: \(\sigma_b = 0\). Head-to-head: \(\sigma_b\) of order \(2P_s\). Uncompensated \(\sigma_b\) produces a depolarization field of the same electrostatic family as the slab field \(E_d \sim P/\varepsilon\) already named on remanence.

- Continuum wall width tracks a Ginzburg–Landau correlation length \(\xi \sim \sqrt{g/|\alpha(T-T_C)|}\) (gradient coefficient \(g\), Landau \(\alpha\)). Near \(T_C\) the wall can thicken. This is not the magnetic form \(\delta_w \approx \pi\sqrt{A/K}\) with two independently measured stiffnesses.

- Partitioning reduces the electrostatic / elastic cost of a uniformly polarized body and adds wall area times wall energy per area. Observed domain size is the scale at which those two measured costs are comparable. 90° walls pay an extra elastic term.

- Applied-field term \(-\mathbf{E}\cdot\mathbf{P}\) grows one set of domains at the expense of another until walls are expelled (poling / saturation of the *pattern*).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two nested buffers:
  1. **Wall.** A transition strip of nanometre-class width (atomically sharp 180°, few-nm 90°) in which \(P\) rotates or reverses between adjacent latched directions. Narrower than that and the two domains have merged. Charged walls additionally need a screening resource the neutral wall does not.
  2. **Domain pattern.** A body large enough that the electrostatic cost of a single-domain state exceeds the wall energy of a partition. Below the no-pattern size the pattern never forms; the particle is one latch cell. There is no universal millimetre-scale domain period.

- **Clock rate / latency.** The polar displacement is ionic and sits on the lattice-mode clock (optical-phonon / THz class). Pattern changes are nucleation and wall-motion events under applied \(E\) (or an optical write channel), far slower than that carrier. A static pattern has no ongoing clock cost.

- **Energy barriers or thresholds.** Locally, each domain is the same polar well as [ferroelectric-remanence](ferroelectric-remanence.md). The wall is a distributed transition whose energy per area is the cost of a partition; 90° walls cost more because they also switch strain. Pinning of walls at grains, electrodes, and charged-wall screening sites is the mesoscale barrier that shows up as \(E_c\) on the loop. Holding a static partition costs zero continuous power.

- **Dominant failure modes.**
  - Single-domain limit: particle below the wall-vs-depolarization cliff \(\to\) no domain pattern (one latch, not a partition).
  - Saturation / poling: applied \(E\) expels walls \(\to\) one domain spanning the body. The local well is still present; the *partition* is gone. Remanent \(P\) after that step is the parent latch, not this file.
  - Thermal: \(T > T_C\) \(\to\) polar well closes \(\to\) no domains. Grain-scale superparaelectric collapse is a clause on remanence, below the domain problem.
  - Mechanical: cracking, ferroelastic stress, or loss of the non-centrosymmetric lattice rewrites pinning and can scramble the pattern without reaching \(T_C\).

- **Emergent constant or stable output.** A static partition of the polar population, with a measured nm-class wall width and a net \(P\) anywhere from \(\approx 0\) (closed pattern) to \(P_s\) (walls expelled), at zero continuous power while the pattern is at rest. 90° walls additionally emit a strain reconfiguration locked to the partition.

### 4.6 Internal Consistency Notes

Domains do not contradict the polar latch: they *are* many wells sharing a body, with walls as the finite-width boundaries. Zero hold power on a static pattern, dissipative cost only when walls move, and two sharp collapses (no-pattern size, field-expelled walls) fit the family. Wall width is a length first, as on the magnetic twin.

The electrical twin of [magnetic-domains](magnetic-domains.md) is tight on that accounting and on the saturation split: a field can destroy the *pattern* while remanent \(P\) remains, just as \(H\) can expel magnetic walls while \(M_r\) remains. Remanence owns net \(P_r\) and the \(P\)–\(E\) loop; this file owns the partition.

| | Magnetic domains | Ferroelectric domains |
|---|---|---|
| Local latch | anisotropy cell | polar well |
| Partition cost | magnetostatic vs \(\sqrt{AK}\) | depolarization / electrostatic vs wall energy |
| Wall extra | Bloch/Néel (no bound-charge sheet) | charged walls possible |
| Saturation | \(H\) expels walls; \(M_r\) can remain | \(E\) expels walls; \(P_r\) can remain |
| Volume of the *latch* | [superparamagnetism](superparamagnetism.md) (own file) | superparaelectric (clause on remanence) |
| Strain face | [magnetostriction](magnetostriction.md) | 90° / [piezoelectricity](piezoelectricity.md) |

The mapping is not closed on pattern selection. Why one sample shows 90° stripes, another 180° lamellae, another a maze is an electrostatic-plus-elastic-plus-pinning problem whose output is imaged, not derived here from node rules. Continuum \(g\) and Landau \(\alpha\) are taken as inputs to \(\xi\); QSA does not yet produce those from a more primitive buffer. The same mesoscale gap as on remanence reappears as wall pinning \(\to E_c\). Charged-wall screening is an extra constraint the magnetic analog does not carry. None of those gaps moves the two collapse cliffs, and none of them closes `polar-depolarization-buffer`.

A vortex lattice ([type-ii-critical-field](type-ii-critical-field.md)) is another topological partition, in a different family. Topology is not a seventh family.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — nm-class wall width, the no-pattern size, field-expelled walls, charged vs neutral, and zero hold power are solid, but pattern choice and the pinning that sets technical \(E_c\) remain mesoscale data without a closed specification.

## Related entries

- [ferroelectric-remanence](ferroelectric-remanence.md) — the local polar well of which each domain is a copy; owns net \(P_r\) and the \(P\)–\(E\) loop
- [magnetic-domains](magnetic-domains.md) — magnetic twin: partitioned alignment, walls as a measured buffer
- [piezoelectricity](piezoelectricity.md) — strain \(\leftrightarrow\) \(P\); 90° walls are the ferroelastic face of this partition
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — magnet write/erase loop, mostly wall motion in bulk
- [superparamagnetism](superparamagnetism.md) — volume collapse of a directional latch; electrical analog is superparaelectric, still a clause on remanence
- [shape-anisotropy](shape-anisotropy.md) — magnetostatic geometry barrier; polar analog is slab depolarization, not a second file
- [type-ii-critical-field](type-ii-critical-field.md) — mixed-state vortex lattice: partition in `gapped-coherence`, not this family
- [elasticity](elasticity.md) — the strain hardware 90° walls switch
