---
origin: application
device: metal-hydride storage bed / tank / compressor
updated: 2026-08-17
---

# Application: Metal-hydride storage

**Device.** A packed bed or tank of hydride-forming metal (LaNi₅-class, TiFe, Mg, Pd, Ni) that is supposed to take up and give back hydrogen on a *P*–*T* swing.
**QSA machines.** `ensemble-average` (reversible lattice H); `anisotropy-latch` / `exchange-pin` (trapped H at defects); `oscillator-grid` (*T*<sub>m</sub>, decrepitation, thermal conductivity of the bed).
**Status.** Working application. No anomaly claim.

---

## 1. Claim

Two populations share the same tank:

| Population | Machine | What you want |
|---|---|---|
| Lattice / interstitial H in equilibrium sites | Ensemble / grid | Reversible capacity. Plateau pressure. TDS low-*T* peak. |
| H at dislocations, grain boundaries, oxide interfaces, deep traps | Latch / pin | Residual that will **not** come off on the design swing. Capacity fade. |

Bulk H/M is the sum. Designers who only measure a Sieverts isotherm are reading the average and missing the pin.

---

## 2. Theory of operation

**Write of useful capacity.** Raise *P*, lower *T*, wait for the plateau. That is not a latch write; it is filling the reservoir.

**Write of the pin.** Plastic decrepitation, cycling strain, oxidation, and cold work create traps. H that falls into those wells is held at zero continuous power and does not follow the plateau.

**Erase of the pin.** A high-*T* bake / activation protocol that the storage swing was not supposed to need. If fade reverses on a bake above the service *T*, you have a blocking / detrapping line, not a lost tank.

**Grid.** Mg-class hydrides sit near a thermal-cliff of the host (*T* to move H, *T*<sub>m</sub> if you overshoot). Bed *κ* is `thermal-conductivity-phonon` plus gas in the voids — starve the mfp and the bed has a hot core and a cold skin.

---

## 3. Knobs

| Parameter | Toward a reversible bed | Toward isolating trapped H |
|---|---|---|
| Cycle count | Minimize plastic shock | Walk cycles and watch residual H grow |
| Particle size | Heat/mass transfer vs fire risk | A size series: fines trap more per gram |
| Activation / bake | Only as needed to open the surface | A dedicated high-*T* erase column |
| Alloy / coating | Plateau *P* in the service band | Compare a “clean” lot to a cold-worked lot at the same H/M |
| *P*–*T* swing amplitude | Stay on the plateau | Over-swing that decrepitates the grid |
| TDS / residual after designed desorption | Should go to the spec residual | A second, hotter peak is the pin |

---

## 4. Isolation sequence

0. First absorption / desorption on a well-activated, un-cycled lot — plateau and residual.  
1. *N* cycles, same swing — residual vs *N*.  
2. Bake / re-activate — does residual return to (0)?  
3. Cold-worked vs annealed powder, same chemistry, first cycle.  
4. Size cuts at fixed *N*.

Latch mapping: residual grows with damage, shrinks with bake, worse in fines and cold work, and is **not** the same as the plateau capacity.

---

## 5. Falsifiers

- Residual after designed desorption is always explained by the isotherm (no second TDS peak, no bake effect).  
- Cold work does not change residual at fixed plateau H/M.  
- Fines and coarse particles leave the same residual per reversible H.

---

## 6. Link to EM-CSAM

A railgun or coil pulse on hydride powder is an extreme **decrepitation / trap-write**. Useful as a way to *make* a pinned population on purpose (then measure residual), and a warning if the feedstock is a storage alloy you still wanted reversible. See [EM-CSAM](EM-CSAM.md).
