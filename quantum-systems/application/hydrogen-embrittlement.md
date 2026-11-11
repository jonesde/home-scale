---
origin: application
device: charged high-strength metal (bolts, welds, hydride-formed parts)
updated: 2026-11-13
---

# Application: Hydrogen embrittlement / delayed fracture

**Device.** A high-strength steel, Ni-alloy, or titanium part that has taken up hydrogen (plating, welding, corrosion, high-pressure H₂, or a hydride-forming service).
**QSA machines.** Trapped hydrogen at defects (per-atom binding, Arrhenius release); `oscillator-grid` as the crack path; `ensemble-average` as the lattice hydrogen.
**Status.** Working application. Handbook effect. No nuclear layer. **Not a tested protocol** and not a process spec for a load-bearing part. See [SAFETY.md](../SAFETY.md).
**Why it is here.** It is the established relative of [EM-LENR](EM-LENR.md): the same write, hold and erase vocabulary applied to a case where the measurements exist. If the mapping cannot restate bake-out and trapping as measured, it should not be used on a coil cell.

Derived specs: [design-spec-sheets](../library/derived/design-spec-sheets.md), [requirement-audit](../library/derived/requirement-audit.md).

> **Changed 2026-11-13**, after [hydrogen-in-metals](../library/hydrogen-in-metals.md) (below **HM**) was sourced. The accepted mechanisms are now named. The "blocking analog", "volume cliff" and "detrapping line" are removed: trap binding is per atom, falls with occupancy, and has no sourced volume threshold; release is an Arrhenius crossover. Reversible and irreversible traps are distinguished. The earlier claim that a deeply pinned population is the load-bearing object is restated as a hypothesis, with the sourced statement that sits against it.

---

## 1. Claim

Sourced (HM §4.3, "Embrittlement" and "Trapping"):

- Embrittlement needs a hydrogen content above a critical level **and** a sufficient stress, applied or residual. Bulk content alone does not predict it. In one martensitic steel 5 wt ppm lowers the tensile strength.
- The named mechanisms are hydrogen-enhanced decohesion (HEDE), hydrogen-enhanced local plasticity (HELP) and adsorption-induced dislocation emission (AIDE).
- At low temperature hydrogen segregates to defects; the total is lattice hydrogen plus hydrogen at defects.
- Traps differ in depth. bcc iron: dislocation strain field 12–27 kJ mol⁻¹, grain boundary 9–49, single vacancy 24–78, incoherent TiC 60–129. By convention a trap deeper than 50 kJ mol⁻¹ is irreversible at room temperature. The review that tabulates these states that irreversible traps act as sinks until saturated, while reversible traps can act as sinks or as sources.
- Binding is an energy per atom at a site and falls as the site fills. No source gives a trap a minimum volume.

Mapping (speculative): lattice hydrogen is **capacity**; trapped hydrogen is a **held** state at zero power; bake-out is **erase**.

Hypothesis, kept from the earlier version and not sourced: the population that matters for delayed fracture is a high-occupancy trapped one. The sourced statement on sinks and sources sits against the strong form of this, since a deep trap that never releases removes hydrogen from play, and the hydrogen that reaches a crack tip is mobile or reversibly trapped.

---

## 2. Theory of operation

| Layer | What it is in this device |
|---|---|
| Grid | Host lattice. Plastic zone, weld residual stress and cyclic load create and move defects |
| Trapped hydrogen | Hydrogen at a defect site, bound per atom, in equilibrium with the lattice concentration. In iron at 0.01 wt ppm lattice hydrogen, 50 kJ mol⁻¹ traps are over 90 % full and 10 kJ mol⁻¹ traps under 10 % full |
| Lattice hydrogen | Ordinary interstitial sites. Diffuses fast in iron: 1 µm in 0.14 ms, 100 µm in 1.4 s at 298 K, before trapping slows it |

Write: charging (cathodic, gas, corrosion) raises the lattice concentration; traps fill from it.
Hold: trapped hydrogen remains after charging stops. Smaller specimens retain less, and loss is faster in vacuum than in argon.
Erase: a bake. Release goes as \(e^{-E_a/RT}\) per atom; a 50 kJ mol⁻¹ trap releases 1750 times faster at 473 K than at 298 K. One sourced example: 200 °C for 10 min removed the hydrogen from a hot-stamped martensitic steel. Bake schedules for a real part come from the governing specification, not from this file.

---

## 3. Knobs (which way)

| Parameter | Toward isolation | Uninformative |
|---|---|---|
| Hydrogen content | Measure lattice and trapped hydrogen separately (thermal desorption) | A single total ppm |
| Hardness / yield strength | A series through the susceptible range | Only dead-soft material |
| Microstructure | Lots that differ in one trap type (grain size, carbide coherency) | Unknown history |
| Stress state | Residual plus external tension | Unstressed coupons only |
| Time after charge | Hours to days, with the charging circuit off | Only tests under charge |
| Bake | Temperature and time series on every charged lot | No erase control |
| Service temperature | Arrhenius scan of susceptibility and of desorption | A single temperature |

---

## 4. Isolation sequence

0. Uncharged, same alloy, same stress: baseline toughness and time to failure.
1. Charge to a measured content; record the desorption spectrum; delayed test.
2. Same charge, then bake, then the same spectrum and test (**erase**).
3. Same lattice content, annealed against hard lot.
4. Lots that differ in one trap type, at fixed lattice content.
5. Wait after charging with the circuit off; repeat the spectrum and the test (**hold**).

---

## 5. Falsifiers

- Bake-out removes the desorption peaks and does not restore toughness.
- Soft and hard lots behave the same at the same lattice and trapped content.
- Failure occurs only under charge and never after the current is off.
- Susceptibility tracks total content and is indifferent to which traps hold it.

The first three run against published experience. The fourth is the test of the hypothesis in §1.

---

## 6. Link to EM-CSAM

Spraying high-strength steel or Ti with a hydrogen-rich carrier charges the part whether or not that was intended. See [EM-CSAM](EM-CSAM.md) § experimental: carrier chemistry as a charging knob, post-spray bake as erase, residual stress as the second required condition.
