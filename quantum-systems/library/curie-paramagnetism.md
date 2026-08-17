---
id: curie-paramagnetism
title: Curie Paramagnetism (Unlocked-Spin Ensemble)
status: formal
family: ensemble-averages
constraints:
  - thermal
  - field-threshold
confidence_data: high
confidence_mapping: medium
related:
  - permanent-magnet-latch
  - superparamagnetism
  - ferromagnetic-hysteresis
  - antiferromagnetic-order
  - thermal-equilibrium-temperature
  - faraday-rotation
updated: 2026-08-17
---

# Curie Paramagnetism (Unlocked-Spin Ensemble)

### 4.1 Effect Name

Curie paramagnetism (unlocked-spin ensemble)

### 4.2 Macroscopic Observation

A paramagnetic salt, a dilute magnetic ion in a host, or a piece of oxygen-bearing gas acquires a magnetization along an applied field and loses that magnetization when the field is removed. The susceptibility falls as the thermometer reading rises. There is no remnant moment and no hysteresis loop of the kind a hard magnet keeps at zero field. Cooling toward an ordering temperature replaces this reversible \(1/T\) response with a latched ferromagnetic, ferrimagnetic, or antiferromagnetic state. Heating toward very high \(T\) drives the susceptibility toward zero: the same field produces less and less moment. Ordinary laboratory fields at room temperature stay inside the linear envelope; only large \(B/T\) saturates the response.

### 4.3 Established Quantitative Boundaries

- Curie law for an unlocked local-moment population:

  \[
  \chi = \frac{C}{T}
  \]

  Curie–Weiss form when mean interactions are present but have not yet locked the population:

  \[
  \chi = \frac{C}{T-\theta}
  \]

  \(\theta>0\) is a ferromagnetic tendency; \(\theta<0\) is an antiferromagnetic tendency. \(C\) and \(\theta\) are material-specific.
- The linear \(\chi\) envelope fails when \(\mu B\) is no longer small compared with \(kT\). With \(\mu_B/k\approx 0.672\,\mathrm{K\,T^{-1}}\), \(kT/\mu_B\) at \(300\,\mathrm{K}\) is several hundred tesla, so a \(1\,\mathrm{T}\) laboratory field sits deep in the linear regime. At a kelvin, tesla-scale fields reach saturation (Brillouin / Langevin rollover).
- Ordering collapses the unlocked ensemble:
  - ferromagnetic / ferrimagnetic lock at \(T_C\) (see [permanent-magnet latch](permanent-magnet-latch.md), [ferromagnetic hysteresis](ferromagnetic-hysteresis.md));
  - antiferromagnetic lock at \(T_N\) (see [antiferromagnetic order](antiferromagnetic-order.md)).
  Below those temperatures \(\chi\) is no longer \(C/T\).
- High-\(T\) collapse of the *useful* output: \(\chi\to 0\) as \(T\to\infty\). The population is still unlocked; the same \(B\) simply produces a vanishing moment.
- Pauli paramagnetism of a metal is a different envelope: a Fermi-surface average, nearly independent of \(T\), analogous to the linear [electron heat capacity](electron-heat-capacity.md). It must not be filed as Curie \(1/T\).

**Data confidence:** High — Curie’s law, Curie–Weiss fits, Brillouin saturation, and the replacement of \(\chi=C/T\) by order at \(T_C\) or \(T_N\) are standard magnetometry. \(C\) and \(\theta\) for any one compound are medium (sample- and fit-range-dependent); the functional collapses are not.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Isolated-moment Curie constant (spin \(S\), Landé \(g\)):

  \[
  C = \frac{\mu_0 n\,g^{2}\mu_B^{2}S(S+1)}{3k}
  \]

  Recorded as the descriptive prefactor that sets the scale of \(\chi\); \(C\) is taken from fit or from a known ionic configuration, not derived here from a more primitive node rule.
- Magnetization of an unlocked population in a field: \(M = n\mu\,B_S(x)\) with \(x = g\mu_B S B/kT\) and \(B_S\) the Brillouin function. Small \(x\) recovers \(\chi=C/T\); large \(x\) saturates at \(n\mu\).
- Curie–Weiss: replace \(T\) by \(T-\theta\) in the linear envelope, with \(\theta\) a measured intercept. \(\theta\) is not a second independent thermometer; it marks the temperature where this unlocked description stops being the right envelope.

These relations describe the averaged moment of a population that is free to follow the field. They do not describe a latched remnant, and they do not derive \(k\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A large population of unlocked moments sharing a bath \(T\), observed as a net \(M\) in an applied \(B\). The hardware scale is statistical: one spin is not a susceptibility; the macro \(\chi\) is the averaged response of the population. There is no universal \(N\) cliff. Dilute moments still follow Curie once \(N\) is large enough for the magnetometer; concentrated moments follow Curie–Weiss until they lock. Volume enters this family as count, not as an anisotropy barrier. The barrier-times-volume collapse of a *latched* grain is [superparamagnetism](superparamagnetism.md), a different family.

- **Clock rate / latency.** Single-moment Larmor / attempt clocks are the same gigahertz-per-tesla scale already recorded on the [magnet latch](permanent-magnet-latch.md) (\(\gamma/2\pi\approx 28\,\mathrm{GHz\,T^{-1}}\)). The Curie reading is a time-averaged projection along \(B\). Observation faster than the bath exchange, or faster than the moment’s relaxation in the host, is not \(\chi=C/T\).

- **Energy barriers or thresholds.**
  - Operating condition of this effect: *no* latching barrier. The moments remain unlocked.
  - Field threshold for the linear envelope: \(\mu B\sim kT\). Above it the Brillouin function saturates and \(\chi\) is no longer \(C/T\).
  - Thermal threshold out of the family: cooling through \(\theta\), \(T_C\), or \(T_N\) installs a latch or a staggered order and this entry no longer applies.

- **Dominant failure modes.**
  - Thermal, low \(T\): order sets in at \(T_C\) or \(T_N\) (or the Curie–Weiss intercept \(\theta\)) → the unlocked ensemble is replaced by a latched or staggered state. \(\chi=C/T\) dies because the machine has changed family.
  - Thermal, high \(T\): \(\chi\to 0\) → the average is still Curie, but the useful moment for a given \(B\) has vanished into the instrument floor.
  - Field: \(\mu B\gtrsim kT\) → saturation; linear susceptibility is the wrong envelope.
  - Population: too few independent moments in the sampled volume → \(M\) is a telegraph of individual flips, not a susceptibility.
  - Mis-filing: treating a hard magnet’s remnant \(M(B=0)\) as Curie. Remanence is the latch, not this average.

- **Emergent constant or stable output.** A reversible susceptibility \(\chi=C/T\) (or \(C/(T-\theta)\)), linear in \(B\) at small \(x\), with zero remnant at \(B=0\), as the averaged projection of an unlocked-moment population.

### 4.6 Internal Consistency Notes

The contrast with the [permanent-magnet latch](permanent-magnet-latch.md) is the load-bearing internal-consistency test for this entry. A latched grain holds a directional moment at zero continuous field and zero continuous power; an unlocked Curie population holds nothing at \(B=0\) and presents a moment only while the field is applied. Soft iron above its useful coercivity but below \(T_C\) is *not* Curie paramagnetism — it is still a ferromagnetic collective, just a poorly latched one. [Ferromagnetic hysteresis](ferromagnetic-hysteresis.md) owns that distinction.

[Superparamagnetism](superparamagnetism.md) is the other contrast: a small ferromagnetic grain *above* its blocking temperature behaves as one giant unlocked moment (Langevin / superparamagnetic), and *below* it becomes a latch. That grain has an anisotropy barrier and a volume threshold. A true Curie ion does not. Filing both as “1/T magnetism” would erase the barrier that the latch family is built on.

Pauli paramagnetism shares this family’s statistical character (a Fermi-surface slice, like \(\gamma T\)) but not the \(1/T\) envelope. It is noted so it is not forced into \(C/T\); it is not given a fake home in this file.

The mapping does not compute \(C\) or \(\theta\) from node rules, and it does not invent a universal spin count. Those are the same honest gaps as on the other ensemble-average entries.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the \(C/T\) envelope, Brillouin saturation, and the \(T\to T_C/T_N\) replacement by order are sharp, and the unlocked-versus-latched contrast closes against the magnet entries; the hardware scale remains statistical, with no single \(N\) cliff.

## Related entries

- [Permanent magnet (directional latch)](permanent-magnet-latch.md) — locked contrast case; remnant \(M\) at \(B=0\)
- [Superparamagnetism](superparamagnetism.md) — small-grain latch that looks unlocked only above its blocking temperature
- [Ferromagnetic hysteresis](ferromagnetic-hysteresis.md) — write / erase cycle of the ordered state this ensemble dies into
- [Antiferromagnetic order](antiferromagnetic-order.md) — staggered lock at \(T_N\); \(\chi\) is no longer \(C/T\)
- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the bath average that sets the \(1/T\) scale
- [Faraday rotation](faraday-rotation.md) — optical readout that can ride on either an unlocked or a latched moment population
