---
origin: application
device: charged high-strength metal (bolts, welds, hydride-formed parts)
updated: 2026-08-17
---

# Application: Hydrogen embrittlement / delayed fracture

**Device.** A high-strength steel, Ni-alloy, or titanium part that has taken up hydrogen (plating, welding, corrosion, high-pressure H₂, or a hydride-forming service).
**QSA machines.** `anisotropy-latch` / `exchange-pin` applied to interstitial occupancy; `oscillator-grid` as the crack path; `ensemble-average` as the bulk H you already measure.
**Status.** Working application. Handbook effect. No nuclear layer.
**Why it is here.** Same configuration hypothesis as [EM-LENR](EM-LENR.md) with the energy-gate cut off. If this mapping cannot recover bake-out and the hardness × H window, do not trust it on a coil cell.

Derived specs: [design-spec-sheets](../library/derived/design-spec-sheets.md), [requirement-audit](../library/derived/requirement-audit.md).

---

## 1. Claim

Delayed hydrogen cracking is not predicted by bulk hydrogen content alone. The load-bearing object is a **pinned, high-occupancy hydrogen population at traps** (dislocations, grain boundaries, inclusions, hydride platelets). Bulk H (ppm, H/M) is **capacity**. Bake-out is **erase**. A critical hardness / yield window is the **barrier matrix**: too soft and there is nothing to pin; too little H and the cell cannot be written.

This is the interstitial latch without a fourth-layer gate.

---

## 2. Theory of operation

| Layer | What it is in this device |
|---|---|
| Grid | Host lattice. Plastic zone, weld residual stress, and cyclic load write and move traps. |
| Latch | H clustered at a trap, held at zero continuous power until *kT*, a bake, or a crack dumps it. |
| Pin | The trap site itself. Its collapse is a **detrapping / blocking** line, not the bulk solubility isotherm. |
| Average | Lattice H in ordinary interstitial sites. TDS low-temperature peak. Necessary reservoir. |

Write: charge (cathodic, gas, corrosion) + stress opens volume and drives H into traps.  
Hold: trapped H stays after the charging current is off (hold-power test).  
Erase: bake (typically 150–200 °C class for steels — check the relevant spec), or a crack that dumps the cell.

Failure that is *not* “we didn’t have enough ppm”:

- Grain / trap volume below a blocking analog → H is mobile, no delayed crack, just permeability.
- Soft annealed ferrite → no high triaxiality well; H does not stay.
- Bake-out after charge → signature gone. That is erase, and it is how the industry already proves the latch.

---

## 3. Knobs (which way)

| Parameter | Toward isolation | Collapse / null |
|---|---|---|
| Bulk H | Cross a threshold, then stop using ppm as the knob | Chasing a single magic ppm |
| Hardness / YS | Walk a series through the known susceptible window (e.g. high-strength steels above a spec hardness) | Only dead-soft material |
| Grain / inclusion size | A size series; look for a cliff, not a smooth ppm trend | “Finer is always worse” without a window |
| Stress state | Residual + external tension, not pure compression | Unstressed coupons only |
| Time after charge | Hours–days (delayed). That delay *is* the hold clock | Only in-situ under charge |
| Bake | A bake-out column on every charged lot | No erase control |
| Temperature in service | A *T* scan for a drop of susceptibility (detrap), not a rise that is just faster diffusion plus yield drop | |

---

## 4. Isolation sequence

0. Uncharged, same alloy, same stress — baseline toughness / time-to-fail.  
1. Charge to a measured bulk H, no bake, delayed test.  
2. Same charge + bake-out + same test (**erase**).  
3. Same bulk H, annealed vs cold-worked / hard lot (**barrier matrix**).  
4. Size / inclusion series at fixed bulk H (**volume cliff**).  
5. After-charge wait with the charging circuit dark (**hold-power**).

A latch mapping wants: (1) fails, (2) lives, (3) hard lot worse, (4) a size window, (5) the delay survives without continuous charging.

---

## 5. Falsifiers

- Bake-out does not restore toughness at fixed remaining lattice H.  
- Soft and hard lots behave the same at the same ppm.  
- Failure is instantaneous under charge and never delayed after current-off.  
- No size / trap-density structure at all.

Those are published directions. If this application cannot state them, the EM-LENR write/erase protocol is fiction.

---

## 6. Link to EM-CSAM

Spraying high-strength steel or Ti with a hydrogen-rich carrier is a **write** of this machine whether you wanted it or not. See [EM-CSAM](EM-CSAM.md) § experimental: carrier chemistry as an H-charge knob, post-spray bake as erase, residual stress as the pin.
