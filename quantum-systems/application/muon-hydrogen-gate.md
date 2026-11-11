---
origin: application
device: muon-catalyzed hydrogen-isotope fusion cycle as an extra-node energy-gate
updated: 2026-11-14
envelope: industrial / accelerator only; no consumer muon source exists
---

# Application: Extra-node hydrogen gate

**Device.** A hydrogen-isotope target in a stopped-muon beam. One muon plus two nuclei is the hardware for one catalysis cycle. Output is fusion-product yield per stopped muon, only while muons are present.
**QSA machines.** `energy-gate` (core); `muon` node as `input`. Contrast: [polar-beam-gate](polar-beam-gate.md); [deuteron-photodisintegration](../library/deuteron-photodisintegration.md); the muon-free coil cell in [EM-LENR](EM-LENR.md).
**Status.** Working application of the extra-node spec, not a restatement of the historical LAMPF/PSI campaign as a product and not a net-energy plant. **Not a beamline SOP.**
**Envelope.** Accelerator / industrial only. Home-scale waits on a consumer muon source that does not exist.
**Sources.** Facts are cited to [muon-catalyzed-fusion](../library/muon-catalyzed-fusion.md) (below **MCF**) by source key; its Sources table holds the references.

> **What changed on 2026-11-14.** The library entry was checked against sources and this file was brought into line. (1) The device is an existing published experiment, not a new concept: about 150 fusions per muon were measured in cold, dense d–t at LAMPF (Jones, *Nature* 321, 127 (1986); MCF [S4]), and a diamond-anvil d–t target is running at PSI (MuFusE, arXiv:2606.05333; MCF [S9]). (2) The yield is *Y* ≈ 1/(*ω<sub>s</sub>* + *λ*<sub>0</sub>/*λ<sub>c</sub>*): decay and sticking losses add, and at optimum each limits the yield about equally (MCF [S6]). The earlier "supply × cycle × (1−*ω<sub>s</sub>*)" wording is replaced. (3) Sticking is 0.35–0.6 % and falls with density (MCF [S5][S7]). (4) The fast cycle needs a host D₂ or DT molecule for resonant formation (MCF [S6]). (5) The energy balance is stated: 2.64 GeV released per muon at the record yield against an estimated 5 GeV electrical (10 GeV thermal) to make one muon (MCF [S7][S8]).

> **Hazards (read [SAFETY.md](../SAFETY.md)).** Muon production is an accelerator problem (prompt radiation, activated beamline, cryogenic or high-pressure H-isotope targets). This file is a mapping, not a factory design. Do not scale muon current, target inventory, or pulse energy in search of a nuclear signature. A muon-free hydride is not this machine — do not “make up for” missing muons with pressure or cold work.

---

## 1. Claim

The gate requires a **named extra node**. Absence of the muon shuts the channel at every lattice strain and every H/M (`predicted:muon-catalyzed-fusion:muon-free-cell-is-null`). Target density and volume are **capacity**: they raise the cycle rate and the number of stopped muons; they do not open a muon-free cell.

| Resource | Role |
|---|---|
| One muon + two H-isotope nuclei, plus a host D₂ or DT molecule | Hardware for one fast cycle (*N* = 1 muon). The host molecule takes up the 0.66 eV released when the muonic ion forms |
| *τ<sub>μ</sub>* = 2.197 μs | Stop. One cycle takes about 10⁻⁸ s, so decay alone allows about 220 cycles. Observation after the muon population is gone is not this effect. |
| Sticking *ω<sub>s</sub>* = 0.35–0.6 % | Loss of the muon onto helium, per fusion; adds to the decay loss |
| Isotope mix | Fusion is observed for every isotope pair except two protons; only ddμ and dtμ form resonantly |
| Lattice / H/M / defects | **Not** the opener. Contrast with [EM-LENR](EM-LENR.md) |

Opposite arrow on the same two nucleons: a 2.224 MeV *γ* unbinds *d* → *p*+*n* and does not start this cycle (`predicted:deuteron-photodisintegration:photon-is-not-a-muon`).

---

## 2. Theory of operation

**Open.** A stopped muon forms a muonic molecule (dtμ / ddμ class). The mass ratio of about 207 shrinks the bound orbit by the same factor, and fusion inside the ion takes about a picosecond. The muon is recycled until it decays or sticks.

**Output.** Yield per stopped muon, about 150 at the record and over 100 as the reproduced class for dense d–t, *Y* ≈ 1/(*ω<sub>s</sub>* + *λ*<sub>0</sub>/*λ<sub>c</sub>*). Not a remnant cell at 0 W.

**Erase / collapse.**

- No muon → identically null.  
- Decay at *τ<sub>μ</sub>* removes the catalyst (exponential).  
- Sticking removes it with probability *ω<sub>s</sub>* per fusion. The two losses add.  
- Two protons give no observed fusion.  
- Cosmic-ray flux over a hydride is not this cycle; macroscopic yield tracks *stopped-muon* inventory.

Energy balance (not used to locate the gate, but it bounds the application): 150 fusions release 2.64 GeV per muon. Estimates of the cost of one stopped muon are about 5 GeV electrical or 10 GeV thermal, with 2–8 GeV quoted; none is a measurement, since no such muon source has been built. Break-even needs about 300 or more fusions per muon, and more once heat is converted to electricity.

---

## 3. Knobs

| Parameter | Toward isolating this gate | Not a substitute |
|---|---|---|
| Stopped-muon inventory | **The** supply knob | Lattice compression, bake-out, cold work |
| Target density | Capacity (raises *λ<sub>c</sub>*, lowers *ω<sub>s</sub>*) | Opening a muon-free cell |
| Isotope mix | d–t vs d–d vs protium (ordering of the cycle) | “Any hydrogen” |
| Sticking / recycle | Witness the *ω<sub>s</sub>* loss | Treating ⟨*n*⟩ as a latch lifetime |
| Clock | Count while muons are present | A seconds-scale pyro ramp ([polar-beam-gate](polar-beam-gate.md)) |
| Photon beam at 2.224 MeV | Contrast only (photodisintegration) | Substituting for the muon |

---

## 4. Isolation sequence

0. Same H-isotope target, **no** muon beam — null.  
1. Stopped muons on dense d–t (or d–d) — yield per muon, time structure set by *τ<sub>μ</sub>* and sticking.  
2. Beam off — yield gone on the muon clock, not on a blocking temperature.  
3. Protium-rich mix — cycle suppressed relative to d–t.  
4. Same target under a 2.224 MeV *γ* and no muons — photoneutrons, not this cycle.  
5. Muon-free Pd–D / Ni–H coil ([EM-LENR](EM-LENR.md)) and a pyroelectric D cell ([polar-beam-gate](polar-beam-gate.md)) — neither may reproduce the per-muon, *τ<sub>μ</sub>*-limited yield.

---

## 5. Falsifiers

- Yield after the muon population is gone.  
- Yield that tracks bake-out, cold work, or H/M in a muon-free hydride.  
- A 2.224 MeV *γ* substituting for the muon.  
- A remnant fusion cycle at 0 W with zero muon inventory (that would be a latch).  
- Identifying this gate with pyroelectric 2.45 MeV neutrons (wrong clock, wrong extra node).

---

## 6. What this file is not

- Not the historical beam-campaign runbook.  
- Not a net-energy factory.  
- Not [polar-beam-gate](polar-beam-gate.md) and not [EM-LENR](EM-LENR.md).  
- Not photodisintegration, pair production, or ionization of electronic H.  
- Not a reason to add a muon source to any other application in this directory.

## 7. Links

- [muon-catalyzed-fusion](../library/muon-catalyzed-fusion.md) — library source, with references  
- [deuteron-photodisintegration](../library/deuteron-photodisintegration.md) — opposite arrow  
- [polar-beam-gate](polar-beam-gate.md) — muon-free H-isotope burst  
- [EM-LENR](EM-LENR.md) — isolate a materials state first; this gate stays closed  
