---
origin: application
device: mirror, transparent conductor, SPR chip, EMI shield
updated: 2026-08-17
---

# Application: Thin-film optics and transparent conductors

**Device.** A deposited metal or TCO stack: Ag/Al mirror, ITO/AZO window, Au/Ag SPR chip, RF mesh / skin shield.
**QSA machines.** `collective-screening` (core); `energy-gate` (photoelectric / gap absorption as contrast); `oscillator-grid` (adhesion, anneal, melt).
**Status.** Working application. High-data, High-mapping calibration. **Not a tested coating process.**

If QSA cannot recover “Ag goes transparent below ~5–10 nm continuous, and above the plasma / interband edge,” do not take the interstitial-latch mapping seriously.

---

## 1. Claim

The device dies when the **connected screening buffer** is starved or when the **drive outruns ωp** (or the material’s optical edge). Those are one machine, two knobs. Island films and too-thin continuous films are the same failure class (buffer), not two mysteries.

`coupled-screening-failure` (derived): a film that loses specular *R* in that window should also lose a Kretschmann SPR dip and transmit in the same spectral band.

---

## 2. Theory of operation

| Knob | Machine clause |
|---|---|
| Thickness / percolation | Hardware scale. Need ~10–20 nm continuous Ag/Al for a visible mirror; SPR often lives in a tens-of-nm window. |
| *n* (carrier density) | Sets ωp. ITO is a metal you can starve by doping or oxidation. |
| Wavelength / RF frequency | Clock. Visible vs RF skin are the same population, different δ(ω). |
| Interface + coupler | SPR only. Momentum match. A mirror does not need a prism; SPR does. |
| Contamination / work function | Energy-gate on the same surface. Photoemission is *N* = 1 and is **not** the mirror. |

Hold-power: 0 extra W. If the stack needs a bias to “stay reflective,” that is a different device (electrochromic, not this machine).

---

## 3. Knobs (which way)

| Parameter | Toward a working device | Collapse |
|---|---|---|
| Metal thickness | **Up** through percolation to ≳ 10–20 nm for a visible mirror | ≲ 5–10 nm continuous, or islands at any nominal *t* |
| Sheet carrier density (TCO) | **Up** until the plasma edge sits where you want IR reject / vis pass | Over-anneal / oxidize that kills *n* |
| Wavelength | Stay below the plasma / interband edge for high *R* | UV on Ag (interband ~3.9 eV) |
| RF frequency (shield) | Higher *f* → thinner δ → easier to be “thick” electrically | *f* → 0, δ exceeds the foil |
| SPR angle / index | Hit the coupler match | No prism/grating, or *t* off the window |
| Adhesion layer (Cr/Ti) | Thin enough not to eat the optical buffer | Thick Cr that is the new “metal” |

---

## 4. Isolation / acceptance tests

1. Thickness series of Ag on glass: *R*(λ), *T*(λ). Cliff at percolation, not a linear fade.  
2. Same series in a Kretschmann mount: dip should vanish with the mirror.  
3. ITO anneal series: *n* down, IR *R* dies, vis *T* may rise — plasma-edge motion, not “the coating disappeared.”  
4. Photoemission on the same Ag: threshold is *φ*, not the 3.9 eV edge.

---

## 5. Falsifiers

- A 3 nm *continuous* Ag (proven continuous, not islanded) that still mirrors like bulk.  
- SPR dip that survives after the film is plasma-transparent at that λ.  
- Optical *R* that requires a hold current.

---

## 6. Link to EM-CSAM

A micro-railgun can throw metal at a substrate and make a coating. Whether that coating is a **mirror** is this application: you are asking whether the splat field percolated and whether it is thick enough. Spray + *R*/*T* on glass is a cheap Phase-1 for both devices. See [EM-CSAM](EM-CSAM.md).
