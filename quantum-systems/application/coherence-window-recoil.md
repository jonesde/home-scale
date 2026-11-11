---
origin: application
device: coherent neutrino–nucleus recoil counter split from an IBD tank on the same flux
updated: 2026-11-11
envelope: reactor / spallation — industrial; home-scale only if a packaged monitor exists later
---

# Application: Coherence-window recoil counter

**Device.** A heavy-nucleus target read for *N*² recoils in the *qR* ≪ 1 window, operated next to (or instead of) a charged-current inverse-beta-decay tank on the **same** neutrino flux. The device is the **split**, not a named IBD product.
**QSA machines.** `energy-gate` as CEνNS (supporting extra-node conversion); `neutrino` as `input`; `nucleus` as scatterer. Contrast: IBD as a different machine with a 1.8 MeV gate.
**Status.** Working application of `predicted:coherent-neutrino-scattering:no-ibd-threshold`. Not the COHERENT apparatus restated as a product. **Not a detector SOP.**
**Envelope.** Reactor / spallation — industrial. Home-scale waits on a packaged monitor.

> **Sourcing note, 2026-11-11.** Corrected against the sourced [coherent-neutrino-scattering](../library/coherent-neutrino-scattering.md). (1) Part of this device is an existing published experiment: CONUS+ (arXiv:2501.05206, 2025) detected reactor antineutrinos by CEνNS in germanium, 395 ± 106 events at 3.7 σ, 20.7 m from a 3.6 GW core, on a flux that inverse-beta-decay detectors also read. (2) The part that is not yet done is the claim below 1.8 MeV. A 1.8 MeV neutrino gives germanium a recoil of at most 96 eV, under the 160 eV threshold of that experiment, so every recoil detected so far comes from a neutrino above the IBD threshold. The row `predicted:coherent-neutrino-scattering:no-ibd-threshold` is untested. (3) The coherence limit is a crossover. Coherence is full below about 10 MeV and partial at the 16–53 MeV of the spallation-source measurements, where the *N*² signal is still observed; there is no collapse at *qR* ≈ 1. (4) The inverse-beta-decay threshold computed from the masses is 1.806 MeV. Wording below was changed in §1–§5 to match; the device, knobs and falsifiers are otherwise as first written.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** Reactor and spallation halls are radiation-controlled workplaces. This file is a mapping of a measured Standard Model channel, not a dark-matter trail and not a shielding design.

---

## 1. Claim

CEνNS has **no** 1.8 MeV IBD gate. The operating window is coherence, *qR* ≪ 1. A CEνNS target exposed to neutrinos well below 1.8 MeV should still produce *N*² recoils while that window holds (`predicted:coherent-neutrino-scattering:no-ibd-threshold`; untested, since such recoils are below 100 eV in germanium). The laboratory recoil threshold is an **instrument floor**, not the process cliff.

| Channel | Gate | Collapse |
|---|---|---|
| CEνNS (this file) | *qR* < 1 (full below about 10 MeV); nucleus present | Gradual loss as *qR* grows (crossover), or no nucleus |
| IBD (contrast) | *E<sub>ν</sub>* ≳ 1.8 MeV on a free proton | Under-threshold charged current |

Same flux, two machines. A large rate step at 1.8 MeV on the coherent target would mean the wrong machine was filed.

---

## 2. Theory of operation

**Hardware.** One neutrino plus one nucleus. Heavy *A* is capacity of the *N*² amplitude, not a second cliff.

**Clock.** Weak; far below laboratory clocks. Detector integration is collection.

**Open / close.** Soft spectrum, *qR* ≪ 1 → *N*² recoils. Harden the spectrum past *qR* ≈ 1 → the coherent enhancement falls gradually through the nuclear form factor even though energy is “enough.” Remove the nucleus → no recoil.

**Readout honesty.** Moving the calorimeter floor can hide recoils that still occur. That is not the CEνNS collapse.

Do not identify this with a dark-matter search. CEνNS is a measured SM channel.

---

## 3. Knobs

| Parameter | Toward isolating CEνNS | Not the process gate |
|---|---|---|
| Nucleus *A* / *N* | **Up** (capacity of *N*²) | Treating *A* as an IBD threshold |
| Spectrum vs *qR* | Below about 10 MeV for full coherence; 16–53 MeV is partially coherent | Hardening until nucleons resolve |
| Recoil threshold | Instrument floor: record it, do not file it as *E<sub>g</sub>* | “No counts below 1.8 MeV ⇒ CEνNS is off” |
| Contrast IBD tank | Same flux, proton-rich, 1.8 MeV on | Using IBD turn-on as this device’s cliff |
| Nucleus present | Required | Empty volume |

---

## 4. Isolation sequence

0. Same target, no neutrino flux — baseline.  
1. Soft flux, *qR* ≪ 1 — *N*²-class recoils below and above 1.8 MeV.  
2. Same flux on an IBD tank — that tank should turn on at 1.8 MeV; this target should not.  
3. Harden the spectrum past *qR* ≈ 1 — the coherent enhancement falls gradually.  
4. Move the recoil floor at fixed *qR* — rate into the detector changes; do not call that the process cliff.

---

## 5. Falsifiers

- Rate on the coherent target that turns on at 1.8 MeV.  
- Collapse when only the calorimeter floor moves and *qR* is unchanged.  
- *N*² scaling absent inside the coherent window (with nucleus present).  
- Filing this as pair production or as photodisintegration (wrong probe, wrong product).

---

## 6. What this file is not

- Not an IBD reactor-neutrino product.  
- Not a dark-matter detector.  
- Not [muon-hydrogen-gate](muon-hydrogen-gate.md) or [polar-beam-gate](polar-beam-gate.md).  
- Not a home-scale science-fair counter.

## 7. Links

- [coherent-neutrino-scattering](../library/coherent-neutrino-scattering.md) — library source  
- [pair-production](../library/pair-production.md) — another extra-node conversion; different probe  
