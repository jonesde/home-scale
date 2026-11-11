---
origin: application
device: hydrogen-switchable rare-earth / Mg hydride film (metal ↔ transparent)
updated: 2026-11-13
envelope: lab / industrial thin-film hydride; home-scale only after sealed low-inventory packaging
---

# Application: Hydrogen-switchable screening film

**Device.** A Y-, rare-earth–, or Mg-class hydride film that reflects as a metal at one hydrogen content and transmits as a semiconductor at a higher one, switched by hydrogen gas or electrochemically.
**QSA machines.** `collective-screening` (metal phase against gapped hydride); the hydride transition and trapped hydrogen of [hydrogen-in-metals](../library/hydrogen-in-metals.md).
**Status.** A QSA reading of an existing laboratory device. **Not a tested coating process.**
**Envelope.** Lab / industrial until a sealed, low-inventory package exists.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** H₂ over a thin metal film is still hydrogen service: leak, fire, and (if powdered or decrepitated) dust. Electrochemical loading adds electrolyte and current. This file is a mapping, not a process spec.

> **Changed 2026-11-13.** The prior art is now cited and the device is described as existing. The claim that conducting-plate Casimir attraction switches off with the mirror is withdrawn: it was measured and does not. The optical state is described as following the hydrogen atmosphere. "Same 10–20 nm class as a visible mirror" and "percolation cliff" are removed, because reflectance has no thickness cliff ([reflection](../library/reflection.md) §4.5). The distinction from "electrochromic" is dropped, since the literature uses that word for this device.

---

## 1. Prior art

These three papers are cited directly; they are not in the effect library.

- Huiberts et al., [*Nature* 380, 231 (1996)](https://www.nature.com/articles/380231a0) (abstract read): palladium-capped yttrium and lanthanum films go from metallic (YH₂, LaH₂) to semiconducting (YH₃, LaH₃) while absorbing hydrogen; yttrium hydride "changes from a shiny mirror to a yellow, transparent window"; the transition takes a few seconds.
- Richardson et al., [*Appl. Phys. Lett.* 78, 3047 (2001)](https://doi.org/10.1063/1.1371959) (abstract read): magnesium-rich Ni–Mg films are mirror-like, become transparent on exposure to hydrogen gas or on cathodic polarization in alkaline electrolyte, and recover when hydrogen is removed. The authors call it an electrochromic mirror electrode. A thin palladium overlayer speeds the kinetics and protects against oxidation.
- Iannuzzi, Lisanti and Capasso, [*PNAS* 101, 4019 (2004)](https://arxiv.org/abs/quant-ph/0403142) (full text read): the Casimir force between a gold-coated plate and a sphere coated with a palladium-capped Mg–Ni switchable mirror, at separations of about 70–400 nm, showed no significant decrease when the mirror was hydrogenated and became transparent.

---

## 2. Claim

The optical output is the screening response of the metal phase turning off as hydrogen content crosses a metal-to-semiconductor line. More hydrogen gives the transparent state in every system cited above.

Three points fixed by the prior art:

- **The state follows the hydrogen atmosphere.** The mirror returns when hydrogen is removed. No electrical power holds the state, but a hydrogen partial pressure does. A sealed device holds its state only as well as it holds its gas.
- **The switch is band-limited.** In the Casimir experiment the film's transparency window ran from about 0.2 µm to 2.5 µm; the force did not change, which the authors explain with Lifshitz theory. Switching the visible mirror does not switch the response at all wavelengths.
- **The palladium cap is a hydrogen window and an oxidation barrier**, a few nanometres to tens of nanometres thick.

Hydrogen populations in the film, as in [hydride-storage](hydride-storage.md): the hydride phase that the swing moves through its transition; dilute lattice hydrogen; and hydrogen trapped at defects, oxide and grain boundaries, bound per atom and released by Arrhenius detrapping ([hydrogen-in-metals](../library/hydrogen-in-metals.md) §4.3).

Hypothesis, not sourced: cycling damage and trapped hydrogen leave a residual optical offset (a film that no longer returns fully to mirror or to window). No cycling data were opened.

---

## 3. Theory of operation

**Toward transparent.** Raise the hydrogen chemical potential (gas pressure or cathodic potential) through the hydride transition. Reflectance falls and the film transmits.

**Toward mirror.** Lower it. The transition is first-order in the hydride formers sourced in the library, so absorption and desorption occur at different pressures and the optical switch has a hysteresis loop.

**Thickness.** Reflectance of a continuous metal film rises smoothly with thickness on the scale of the optical decay length; there is no threshold thickness ([reflection](../library/reflection.md) §4.3 and §4.5). An island film reflects less than a continuous film of the same nominal thickness. The palladium cap adds its own absorption.

**Casimir.** `coupled-screening-failure` supposed that specular reflectance and conducting-plate Casimir attraction fail together. For this device the measurement says they do not ([percolation-dual-switch](percolation-dual-switch.md) addresses thinning, a different knob).

---

## 4. Knobs

| Parameter | Toward a reversible switch | Loss of function |
|---|---|---|
| Hydrogen chemical potential (*P*, electrochemical *E*) | Swing wide enough to cross both branches of the hysteresis loop | A swing inside the loop |
| Film thickness | Enough metal-phase thickness for the wanted reflectance; a continuous film | Island film; cap thick enough to dominate the optics |
| Cap layer | Thin palladium as hydrogen window and oxidation barrier | No cap: oxidation |
| Cycle count | Minimize oxidation and mechanical damage | Residual offset (hypothesis) |
| Bake | A temperature and time series, read as Arrhenius release | — |
| *T* | Service band of the hydride transition | Overshoot toward the host's melting point (`coupled-grid-loss`) |

---

## 5. Isolation sequence

0. Thickness series in the metal phase, no swing: record the smooth *R*(*d*) curve.
1. One swing on a fresh film: *R*(*λ*) and *T*(*λ*) against hydrogen pressure, up and down, to record the loop.
2. *N* cycles on the same swing: residual optical offset against *N*.
3. Bake series: does the offset fall with temperature and time?
4. Remove the hydrogen atmosphere and record how long the transparent state lasts.
5. Infrared reflectance in both states, to map the band over which the film switches.

---

## 6. Falsifiers

- The residual offset after cycling does not respond to a bake and has no counterpart in a thermal desorption spectrum.
- The transparent state persists indefinitely with the hydrogen atmosphere removed and no cap leak.
- The film switches in the infrared as fully as in the visible.

---

## 7. What this file is not

- Not a storage tank ([hydride-storage](hydride-storage.md)).
- Not an Ag/Al mirror or SPR chip ([thin-film-optics](thin-film-optics.md)).
- Not [EM-LENR](EM-LENR.md). Do not add a coil or a muon to the film.
- Not a consumer smart window until the hydrogen inventory is packaged.

## 8. Links

- [hydride-storage](hydride-storage.md) — the same hydrogen populations, read as capacity
- [thin-film-optics](thin-film-optics.md) — metal-phase optics
- [percolation-dual-switch](percolation-dual-switch.md) — thinning as the knob
- [EM-CSAM](EM-CSAM.md) — a splat field can make the film; continuity still matters
