---
origin: application
device: hydrogen-switchable rare-earth / Mg hydride film (metal ↔ transparent)
updated: 2026-08-17
envelope: lab / industrial thin-film hydride; home-scale only after sealed low-inventory packaging
---

# Application: Hydrogen-switchable screening film

**Device.** A Y-, rare-earth–, or Mg-class hydride film that is metal-reflecting in one occupancy and dielectric-transparent in another, switched by a *P*–*T* or electrochemical H swing.
**QSA machines.** `collective-screening` (connected metal buffer vs starved / gapped hydride); `ensemble-average` (reversible lattice H); `anisotropy-latch` / `exchange-pin` analog (pinned residual that *sticks* the shutter).
**Status.** Working application of a combination, not a used window product and not a storage tank. **Not a tested coating process.**
**Envelope.** Lab / industrial until a sealed, low-inventory package exists. Closest of the eight new files to later home-scale packaging.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** H₂ over a thin metal film is still hydrogen service: leak, fire, and (if powdered or decrepitated) dust. Electrochemical loading adds electrolyte and current. This file is a mapping, not a process spec.

---

## 1. Claim

The output is the **screening buffer turning on and off with occupancy**. In the metal hydride the connected electron population re-radiates (`collective-screening`). In the transparent hydride that population is gone or gapped; the film is no longer a mirror. Thickness / percolation still applies in the metal phase: an island metal hydride is not a shutter, it is a starved buffer.

Two hydrogen populations share the film, as in [hydride-storage](hydride-storage.md):

| Population | Machine | What it does to the shutter |
|---|---|---|
| Reversible lattice / interstitial H | Ensemble / grid | Design swing opens and closes the screening buffer. |
| H at defects, oxide, grain boundaries | Latch / pin | Residual that will **not** follow the swing. The shutter sticks open or shut. |

This is not an electrochromic stack. Hold-power of the *optical* state is 0 extra W once occupancy is set. A bias required to “stay reflective” is a different machine (already named in [thin-film-optics](thin-film-optics.md)).

---

## 2. Theory of operation

**Write of the metal state.** Load H (or unload, depending on the alloy’s metal/transparent assignment) until the connected screening population is back. *R* rises; the plasma / interband edge of that metal phase returns.

**Write of the transparent state.** Drive occupancy through the metal–dielectric line. *R* collapses; the film transmits. That is clock/buffer failure of screening, opened by chemistry rather than by thinning.

**Write of the pin.** Cycles, oxidation, and plastic shock create traps. Residual H after the design swing leaves a permanent metal patch or a permanent window.

**Erase of the pin.** A bake / activation above the service swing. If the stuck state returns to the reversible envelope, the pin had a blocking / detrapping line.

`coupled-screening-failure` still applies in the metal phase: starve connected thickness or *n* and specular *R*, SPR (if coupled), and conducting-plate Casimir contrast die together. See [percolation-dual-switch](percolation-dual-switch.md).

---

## 3. Knobs

| Parameter | Toward a reversible shutter | Collapse / stick |
|---|---|---|
| Thickness | **Up** through percolation in the metal phase (same 10–20 nm class as a visible mirror) | Island metal hydride at any nominal *t* |
| H chemical potential (*P*, electrochemical *E*) | Across the metal/transparent line, then **stop** using H/M as the knob | Chasing a magic loading as if it were the cliff |
| Cycle count | Minimize oxidation and decrepitation | Residual grows; shutter sticks |
| Bake / activation | Only as an erase of the pin | No erase column |
| Alloy / cap layer | Pd cap as a known H window, not as the optical metal | Thick cap that becomes the new screening buffer |
| *T* | Service band of the hydride line | Overshoot toward host *T*<sub>m</sub> (`coupled-grid-loss`) |

---

## 4. Isolation sequence

0. Thickness series in the *metal* phase, no swing: recover the percolation cliff of [thin-film-optics](thin-film-optics.md).  
1. One swing on a fresh, well-activated film: *R*(*λ*) / *T*(*λ*) should flip with occupancy, not with a hold voltage.  
2. *N* cycles, same swing — residual optical offset vs *N*.  
3. Bake — does the offset return?  
4. Same film, photoemission: *φ* is not the plasma edge (`predicted:photoelectric-threshold:not-the-plasma-edge`).  
5. Optional: RF *δ* or IR *R* on the metal phase while *n* is starved (`predicted:skin-effect:same-n-kills-optical-and-rf`).

---

## 5. Falsifiers

- Optical switch with no hydrogen (electrochromic / bias-held).  
- Hold voltage required to stay reflective after occupancy is fixed.  
- Residual after the design swing always explained by the isotherm (no bake effect, no second TDS peak).  
- A 3 nm *continuous* metal-phase film that never mirrors, or an island film that “switches” like a connected buffer.

---

## 6. What this file is not

- Not a storage tank ([hydride-storage](hydride-storage.md) owns capacity vs pin).  
- Not an Ag/Al mirror or SPR chip ([thin-film-optics](thin-film-optics.md)).  
- Not EM-LENR. Do not add a coil or a muon to “help” the shutter.  
- Not a consumer smart window until the H inventory is packaged.

## 7. Links

- [hydride-storage](hydride-storage.md) — same two H populations; this file reads them as optical  
- [thin-film-optics](thin-film-optics.md) — metal-phase calibration  
- [percolation-dual-switch](percolation-dual-switch.md) — starve the metal phase and the force channel dies too  
- [EM-CSAM](EM-CSAM.md) — a splat field can *make* the film; percolation is still the cliff  
