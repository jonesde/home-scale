---
origin: application
device: mirror, transparent conductor, SPR chip, EMI shield
updated: 2026-11-14
---

# Application: Thin-film optics and transparent conductors

**Device.** A deposited metal or TCO stack: Ag/Al mirror, ITO/AZO window, Au/Ag SPR chip, RF mesh / skin shield.
**QSA machines.** `collective-screening` (core); `energy-gate` (photoelectric / gap absorption as contrast); `oscillator-grid` (adhesion, anneal, melt).
**Status.** Working application. High-data. It was filed as the High-mapping calibration case; the mapping of [reflection](../library/reflection.md) is now Medium and the thickness half of the calibration is withdrawn (note below). **Not a tested coating process.**

> **Corrected 2026-11-12.** This file opened with a test: if QSA cannot recover "Ag goes transparent below ~5–10 nm continuous, and above the plasma / interband edge," do not take the interstitial-latch mapping seriously. Sourcing [reflection](../library/reflection.md) showed that the first half of that sentence is not a measured cliff. The reflectance of a continuous film falls smoothly with thickness (Ag at 550 nm, computed from bulk constants: 96 % at 50 nm, 74 % at 20 nm, 39 % at 10 nm, 14 % at 5 nm; Al keeps 34–50 % at 5 nm, depending on the optical constants used), a continuous 5.66 nm Au film matches that calculation, and a collective optical response is measured down to one atomic layer. The sharp change in a deposited film is percolation, and it is sharp in dc conductance, not in reflectance. Ordinary thin-film optics predicts the same thickness curve, so recovering it does not test the mapping against the standard description. The spectral half stands: the edge is measured (Ag 3.8–3.9 eV). Sections 1–6 are rewritten to match; the device list is unchanged.

> **Re-checked 2026-11-14** against the library as it now stands. Changes: the Al figure at 5 nm is 34–50 % (the epitaxial-Al constants give the low end); `coupled-screening-failure` is now recorded as in tension in [requirement-audit](../library/derived/requirement-audit.md); the SPR thickness window and the Ag work function are linked to their library files; the statements about transparent conducting oxides, adhesion layers and RF meshes are marked as unsourced, since no sourced library file covers them; §6 says which EM-CSAM regime can make a film thin enough for this series.

---

## 1. Claim

The output falls when the field passes through less responding metal, or when the **drive outruns the plasma or interband edge**. One machine, two knobs. The thickness knob is a crossover: a thinner continuous film gives less reflectance, on the scale of the decay length *δ* = *λ*/4π*k* (Ag 12–15 nm, Al 6.6–8.3 nm), with no starved state below it.

Island films and thin continuous films are two cases, not one failure class. A thin continuous film follows the bulk-constant curve, with extra damping in films of a few nanometres. An islanded film has lost dc conduction across the substrate and has an island-plasmon absorption band; its optical response changes monotonically as the islands join.

`coupled-screening-failure` (derived) said that a film which loses specular *R* in that window should also lose a Kretschmann SPR dip, transmit in the same spectral band, and lose conducting-plate Casimir contrast. Checked against the literature, that is contradicted as worded: *R* has no thickness threshold, and the Casimir force is reduced, not removed, by a thin or visibly transparent face. What the measurements support is a coupled *reduction*, each channel on its own scale: *R* on the decay length; the SPR dip sharp above a metal fill fraction of about 0.6, broad between 0.4 and 0.6 and absent below 0.4; the force about half for a conducting oxide. SPR siblings: `predicted:surface-plasmon-resonance:dies-above-plasma-edge`, `predicted:surface-plasmon-resonance:island-film-no-dip`. The force channel as a device is [percolation-dual-switch](percolation-dual-switch.md). The requirement is now recorded as in tension in [requirement-audit](../library/derived/requirement-audit.md).

---

## 2. Theory of operation

| Knob | Machine clause |
|---|---|
| Thickness | Hardware scale, with no minimum. *R* rises with thickness on the scale *δ*: half of bulk *R* at 12–14 nm (Ag) and 4.5–6 nm (Al), 90 % by about 31–33 nm (Ag) and 14–17 nm (Al), at 550 nm. For SPR the working thickness is a window about 10 nm wide whose centre moves with metal and wavelength: near 45–50 nm for Au and 50–55 nm for Ag at 633 nm ([surface-plasmon-resonance](../library/surface-plasmon-resonance.md)). |
| Percolation | A threshold in dc conductance: 6–12 nm for unseeded Ag, 6–7 nm for unseeded Au, 1–3 nm on a copper seed. Not a threshold in *R*. |
| *n* (carrier density) | Sets ωp in the free-electron model; in Ag the measured edge (3.8 eV) is 0.42 of that model value because of interband screening ([plasma-frequency-cutoff](../library/plasma-frequency-cutoff.md)). A transparent conducting oxide is the case where *n* is a process variable. No sourced library file covers TCOs; the TCO rows below are unsourced. |
| Wavelength / RF frequency | Clock. The visible decay length and the RF skin depth belong to the same electrons and follow different formulas ([skin-effect](../library/skin-effect.md) §4.6); the RF formula gives a tenth of the measured optical depth if carried to the visible. |
| Interface + coupler | SPR only. Momentum match. A mirror does not need a prism; SPR does. |
| Contamination / work function | Energy-gate on the same surface. Photoemission is *N* = 1 and is **not** the mirror. |

Hold-power: 0 extra W. If the stack needs a bias to “stay reflective,” that is a different device (electrochromic, not this machine).

---

## 3. Knobs (which way)

| Parameter | Toward a working device | Loss of output |
|---|---|---|
| Metal thickness | **Up** to about 30 nm (Ag) or 15 nm (Al) for 90 % of bulk *R* in the visible | Gradual: Ag reflects 39 % at 10 nm and 14 % at 5 nm. Below percolation the film also stops conducting dc |
| Sheet carrier density (TCO; unsourced) | **Up** until the plasma edge sits where you want IR reject / vis pass | Over-anneal / oxidize that lowers *n* |
| Wavelength | Stay below the plasma / interband edge for high *R* | UV on Ag (edge at 3.8–3.9 eV; a narrow transmission window near 320 nm, absorbing beyond it) |
| RF frequency (shield) | Higher *f* → smaller δ (Cu: 2.1 mm at 1 kHz, 66 µm at 1 MHz, 2.1 µm at 1 GHz) | *f* → 0: δ grows without limit and exceeds the foil. A crossover, with no critical frequency |
| SPR angle / index | Hit the coupler match | No prism or grating (a threshold: no momentum match); *t* off the window (gradual) |
| Adhesion or seed layer | A 1 nm Cu seed takes Au percolation from 6–7 nm to 1 nm and Ag from 6 nm to 3 nm | A thick absorbing layer (Cr/Ti; unsourced) that becomes the film the light meets |

---

## 4. Isolation / acceptance tests

1. Thickness series of Ag on glass: *R*(λ), *T*(λ) **and sheet resistance**. Expected for continuous films: the smooth bulk-constant curve (*R* from the air side at 550 nm: 14 % at 5 nm, 34 % at 10 nm, 69 % at 20 nm, 96 % at 50 nm). The first version expected a cliff at percolation in *R* and *T*; in Au the optical response passes through percolation monotonically and the abrupt step is in dc conductance. Below percolation, look for an island-plasmon band that fades as the film closes (near 600–650 nm in unseeded Au). No measured *R*(*d*) series for seeded continuous Ag was found to compare with; this test would supply one.  
2. Same series in a Kretschmann mount. Measured on gold–dielectric composite films: a sharp dip above a fill fraction of about 0.6, a broad dip between 0.4 and 0.6, none below 0.4. So `predicted:surface-plasmon-resonance:island-film-no-dip` holds at low fill and fails near percolation. A film driven above its edge loses the bound mode (`predicted:surface-plasmon-resonance:dies-above-plasma-edge`, which is the textbook existence condition), but an absorbing film can still show a p-polarised minimum of another origin, so record the s-polarised trace as well. No scan of a dip through the Ag or Al edge was found.  
3. ITO anneal series (unsourced in the library; the trend is recorded only in the note on `predicted:skin-effect:same-n-kills-optical-and-rf`, which is marked untested): as *n* falls the plasma edge moves to longer wavelength, IR *R* falls and the RF skin depth grows. No opened source measured both on one sample.  
4. Photoemission on the same Ag: threshold is *φ* (4.26–4.74 eV, a tertiary table quoted in [plasma-frequency-cutoff](../library/plasma-frequency-cutoff.md)), not the 3.8–3.9 eV edge (`predicted:photoelectric-threshold:not-the-plasma-edge`).  
5. Optional: conducting-plate attraction on the same thickness series ([percolation-dual-switch](percolation-dual-switch.md)). Expect a force reduced by up to about half on thin or transparent films, and present ([casimir-force](../library/casimir-force.md)).

---

## 5. Falsifiers

- The first version listed "a 3 nm *continuous* Ag that still mirrors like bulk". Ordinary thin-film optics predicts about 5 % reflectance at 3 nm, so that outcome is expected by no one and does not separate the mapping from standard optics. On thickness, this file now has no falsifier that does. A step in *R*(*d*) of a film shown to be continuous would contradict both.  
- A sharp bound-mode SPR dip that survives where Re *ε* of the metal is positive at that λ (after ruling out a lossy-mode minimum with the s-polarised trace).  
- Optical *R* that requires a hold current.

---

## 6. Link to EM-CSAM

A micro-railgun can throw metal at a substrate and make a coating. Whether that coating is a **mirror** is this application: you are asking how much metal the light passes through. Whether the splat field percolated decides dc conduction; it does not by itself decide reflectance. A solid-slug or splat shot lands micrometre-class metal, which is optically thick, so the thickness series in §4 needs the exploding or vapor regime (a thin foil or fine wire as the armature). No percolation thickness is sourced for Cu or for a film made by impact. Deposit + *R*/*T* + sheet resistance on glass is a cheap first series for both devices. See [EM-CSAM](EM-CSAM.md) §3.2. Occupancy as a way to reduce the same response is [switchable-hydride-mirror](switchable-hydride-mirror.md).
