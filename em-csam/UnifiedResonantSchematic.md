# Schematic Description – Unified Resonant Bridge Driver Board
EM-CSAM Micro-Railgun · Version 0.2

A net-level description with values, sufficient to begin schematic capture, plus a bring-up order that works on a 0–30 V bench supply.

**What changed in 0.2.** Launch is one unipolar pulse, not a ≥200 kHz burst (see [`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) §3). This file now has an explicit schematic with reference designators, real gate-drive values, a grounding decision, a conditioning path that works, launch-current sensing, and the protection that was missing. Findings and sources: [`DesignReview-2026-11.md`](DesignReview-2026-11.md) and [`References.md`](References.md). Values marked *start* are bench starting points, not final.

## 1. Purpose of this Document

One low-inductance power stage with these jobs:

- **Launch:** a single 0.2–0.7 ms pulse of up to 1.4 kA (4+4 FETs), shaped by the bank and `L1`.
- **Conditioning:** ballast-limited current of up to about 20 A from a low bus.
- **Measure every shot:** current, slug voltage, bank voltage.

Bus voltage: ≤30 V for first light; 48–56 V later.

## 2. Schematic

```
                 F1        D1          K1          R1
SUPPLY+ ───────[fuse]─────▷|───────[charge en.]──[10 Ω]───┬────────┬────────┬────────┬───── BUS+
                                                          │        │        │        │
                                                        C1–C6    C7–C10     D2       R2
                                                      4700 µF    10 µF    5KP58A   1.5 kΩ bleeder
                                                       100 V     film       │        │      (R3 10 Ω dump via S1)
                                                          │        │        │        │
SUPPLY− ──────────────────────────────────────────────────┴────────┴────┬───┴────────┴───── RETURN ★ (star point)
                                                                        │
          ┌── drains ── BUS+                                            │
   Q1–Q4 (HS, 4 in parallel; Rg 10 Ω and Rgs 10 kΩ each)                │
          └── sources ──┬── SW ──── L1 (L_series) ──── RAIL A           │
          ┌── drains ───┘                                ║              │
   Q5–Q8 (LS, 4 in parallel)                            slug            │
          └── sources ── RETURN ★                        ║              │
                                                       RAIL B ── RC1 (Rogowski, around the bar) ── U4 ACS772 ── RETURN ★

   BUS+ ── K2 (conditioning relay) ── R4 (ballast 1–10 Ω) ── RAIL A

   Snubber R9 + C11 across each leg, at the FETs.
   Muzzle taps: MA (rail A, muzzle end), MB (rail B, muzzle end) → twisted pair → sense network (§3.7).
```

Gate drive and logic:

```
PS3 floating 12 V ──┬── PS1 R12P212S ── VDDA/VSSA (HS gate rail; VSSA = SW via Kelvin pair)
                    ├── PS2 R12P212S ── VDDB/VSSB (LS gate rail; VSSB = LS sources via Kelvin pair)
                    ├── U2 7805 ── 5 V ── 3.3 V LDO ── U3 sequencer, U1 VCCI, U4 ACS772
                    └── K1, K2 coils

U3 sequencer ── HS_CMD ──[one-shot limit]──[fault gate]── INA ┐
              ── LS_CMD (strapped low for first light) ── INB ┤ U1 UCC21551A ── OUTA → Rg → Q1–Q4 gates
              ── ARM ──[supply-good A]──[supply-good B]── EN  ┘                 OUTB → Rg → Q5–Q8 gates
              ── ADC: bus, MA, MB, Rogowski, ACS772, temperature
              ── isolated link (optocouplers or USB isolator) ── printer controller / PC
```

**Reading the power path.** High-side drains to BUS+. High-side sources, low-side drains and one end of `L1` are the switch node SW. Low-side sources go to RETURN at the star point. `L1` is in series with the rails. Rail B returns through the Rogowski loop and the Hall sensor.

## 3. Block Descriptions and Values

### 3.1 DC Input and Charging

| Ref | Part | Value / note |
|---|---|---|
| F1 | DC fuse | 10 A, rated for at least the bus voltage. Automotive blade fuses are 32 V parts and will not do for a 48 V pack. |
| D1 | MBR20100CT | Reverse-polarity protection, in the charge path only ([DS-MBR20100](https://assets.rs-online.com/v1698967684/Datasheets/8209c593df7f907f3184c5a5cc9a980e.pdf)). |
| K1 | Charge enable | On a bench supply, the supply's own output switch does this job and K1 is a link. On a pack, use a switch rated for the DC voltage; the T9AS relay is rated 28 VDC only ([DS-T9A](https://tvsat.com.pl/PDF/1/1-1393210-3.pdf)). |
| R1 | HS25 10 Ω | Charge resistor. **Never jumpered on a battery**: it is the only current limit between a pack and a shorted FET. |
| D2 | 5KP58A | Bus transient clamp; 64.4 V minimum breakdown, so keep the bus at or below 56 V ([DS-5KP](https://cdn.eicom.ru/media/PDF24/69681.pdf)). It also absorbs part of the bank-to-film pump on a hard turn-off. |

- **Bench supply setting:** current limit ≤1 A while charging. A stuck-on high side then dissipates about 10 W in R1 instead of 90 W.
- **Charge time:** R1 with six cans is a 0.28 s time constant.
- **Bus sense:** 220 kΩ / 10 kΩ divider to the sequencer ADC, with clamp diodes.

### 3.2 Capacitor Bank

| Ref | Part | Value / note |
|---|---|---|
| C1–C6 | LGU2A472MELC | 4700 µF 100 V. Pulse-forming capacitor and energy store. Two for first light, six for useful shots, twelve footprints. |
| C7–C10 | B32774D4106K000 | 10 µF 450 V film, directly at the FET legs. Commutation decoupling only: about 300 A peak each ([DS-B32774](https://www.tdk-electronics.tdk.com/inf/20/20/db/fc_2009/MKP_B32774_778.pdf)). |
| R2 | Bleeder | 1.5 kΩ 10 W, hard-wired. Time constant 14 s (two cans) or 42 s (six); 76–102 s to fall below 5 V. |
| R3, S1 | Dump | 10 Ω 25 W through a push switch, for a fast safe discharge. |

- **ESR is half the loop.** Nichicon gives ≤56 mΩ at 120 Hz and nothing at kilohertz ([DS-LGU](https://www.nichicon.co.jp/english/series_items/catalog_pdf/e-lgu.pdf)). Measure each can before relying on any current figure.
- **Keep the electrolytics close to the film cans.** The inductance between them sets the pump term in the turn-off budget (§4).
- **Bank reversal.** If the bank reaches zero with the high side still on, the low-side body diodes clamp it at about −1.3 to −1.8 V. Tolerable briefly; leave the charger connected so it recovers.
- Standard electrolytics are not rated for rapid, frequent discharge ([DS-LGU-GUIDE](https://www.mouser.lt/pdfDocs/nichicon-gxc-app-guidelines.pdf)). Keep the shot rate low and watch can temperature.

### 3.3 Power Bridge

| Ref | Part | Value / note |
|---|---|---|
| Q1–Q4 | IRFP4568 | High-side launch switch. Tabs isolated from the heatsink bar. |
| Q5–Q8 | IRFP4568 | Low-side group. First light: used as diodes, gates tied to sources. |
| R9, C11 | Snubber | 2.7 Ω + 10 nF per leg, *start*. Damps ringing; it does not absorb the commutation energy. |

- **Current limit:** 450 A per FET for 0.5 ms, 350 A for 1 ms; about 1.4 kA for 4+4 with a sharing derate ([DS-IRFP4568](https://www.infineon.com/dgdl/irfp4568pbf.pdf?fileId=5546d462533600a4015356310e811e5b)).
- **First light with the low side as diodes.** Link each low-side gate to its source with a short wire at the FET. There is then no shoot-through path, and the fast rise of the switch node cannot turn the low side on through its Miller capacitance.
- **Kelvin source connections.** Take each gate-drive return from the middle of its source bar, as a twisted pair with the gate lead.
- **Freewheel path:** the FET body diodes (684 A pulse each). The MUR1560 on the original list is a 150 A part and is not in this path ([DS-MUR1560](https://www.onsemi.com/download/data-sheet/pdf/mur1520-d.pdf)).

### 3.4 Gate Drive

U1 is a UCC21551**A** on a SOIC-16 adapter. Source for everything below: [DS-UCC21551](https://www.ti.com/lit/ds/symlink/ucc21551.pdf).

| Item | Value | Why |
|---|---|---|
| VDDA, VDDB decoupling | 10 µF + 0.1 µF each, **soldered on the adapter** | One edge of four gates moves 0.6 µC, which droops 0.1 µF by 6 V. |
| VCCI decoupling | 0.1 µF + 1 µF at the adapter | Supply is some distance away. |
| DT pin | 51 kΩ to ground (452 ns), with ≤1 nF | tDT[ns] = 8.6·RDT[kΩ] + 13. **Never open, never tied to VCCI**: either removes the interlock. |
| EN pin | 10 kΩ pull-down; driven through the supply-good chain | Low or floating means both outputs off. |
| INA, INB | 100 Ω + 100 pF at the adapter | The bars radiate; filter where the signal enters the driver. |
| INB | Strapped low for first light | Low side stays off. |
| Gate resistors | 10 Ω per FET, *start* | One per device, at the device. |
| Gate–source resistors | 10 kΩ per FET | Defined gate with the driver unpowered. |
| Gate rails | 12 V nominal from PS1 and PS2 | Unregulated modules; expect 12–13 V lightly loaded ([DS-R12P](https://recom-power.com/pdf/Econoline/RxxP2xx.pdf)). |

**The suffix.** The A is the 5 V-UVLO part (turn-on about 6 V), not 8 V as earlier notes said. It is still the right choice for 12 V rails; the B and C are not sold in SOIC-16, and the C needs at least 13.5 V. But a 6 V lockout is below the 7–8 V a FET needs at 450 A, so it does not protect the FETs from a sagging gate rail. Hence the supervisor.

**Supply-good supervisor.** On each isolated rail: a 9.1 V zener, an optocoupler LED and 1 kΩ in series across the rail. The LED lights only above about 10 V. The two optocoupler transistors sit in series between the sequencer's ARM output and EN. If either gate rail sags, EN falls and both outputs go low.

**Turn-off speed.** The gate resistor has little effect on how fast the current falls until it is very large; source inductance inside the gate loop sets it. A lower turn-off resistance (2.2–4.7 Ω through a Schottky diode) holds the gate against Miller turn-on. Choose on the bench from measured overshoot.

### 3.5 `L1` (`L_series`)

- Air core, 0.5–3 µH, on two-bolt pads so coils can be swapped. No ferrite: it would saturate.
- 2 µH for first light. It limits the rate of rise to 15 A/µs at 30 V.
- Later, 4–8 flat turns over and under the rails serve as part of `L1` and as augmentation ([`RailgunHeadPrototype.md`](RailgunHeadPrototype.md)). Count about 2.6 µH and 6 mΩ for eight turns.
- **No bypass across `L1`.** A relay contact cannot shunt a milliohm coil, and a closed contact at launch removes the current limit.

### 3.6 Conditioning Path

| Ref | Part | Value / note |
|---|---|---|
| K2 | T9AS1D12-12 | Switches the ballast path. Stay at or below 28 V and 20 A (its DC rating). 15 ms operate and release. |
| R4 | Ballast | 1–10 Ω, 25–50 W. Sets the current: 10 V across 10 Ω is 1 A; 28 V across 2.2 Ω is about 13 A. |

- **Why a resistor.** With ballast much larger than the slug, power into the slug falls as the slug sinters. A stiff source does the opposite and runs away ([PC-ALLEN08](https://cris.vtt.fi/en/publications/electrical-sintering-of-nanoparticle-structures/), [PC-HUMMELGARD11](https://pmc.ncbi.nlm.nih.gov/articles/PMC3044741)).
- **Bridge state:** both FET groups off. Rail A sits at the slug voltage; `L1` just connects it to the floating switch node.
- **Compliance:** the conditioning bus must exceed the breakdown voltage of the paste across this gap. Bead-chain data give 2–8 V ([PC-FALCON05](https://ar5iv.labs.arxiv.org/html/cond-mat/0407773)); a 0.50 mm bed of heavily oxidised copper powder needed 33 V unloaded and about 9–20 V under compaction ([PC-ALIOUAT22](https://doi.org/10.3390/ma15124096)). Until T0 measures the real paste, assume a 30 V bench supply may not be enough for an oxidised, uncompacted fill.
- **Current cap:** about 20 A without magnets or augmenting turns, so the slug is not pushed off its seat.
- **Timing:** the relay limits conditioning to steps of about 15 ms. That is acceptable because the ballast is self-limiting. An energy-capped alternative is in [`TestPlan.md`](TestPlan.md) T4.
- **Later:** a solid-state stage with its own inductor of at least 50 µH and peak-current control.

### 3.7 Sensing

| Signal | How | Notes |
|---|---|---|
| Launch current | RC1, a Rogowski loop around the return bar, sampled raw and integrated in the sequencer | About 100 turns on a 6 mm former gives roughly 0.35 V at 10 A/µs. Calibrate against U4 at 100–200 A. |
| Conditioning current | U4, ACS772ECB-200B | ±200 A, 10 mV/A, 2.5 µs. Clamps during launch; carries up to 0.4 A of offset afterwards, so re-zero after every shot ([DS-ACS772](https://www.allegromicro.com/-/media/files/datasheets/acs772-datasheet.pdf)). |
| Slug voltage | MA and MB, a twisted pair from the **muzzle** ends of the rails | Reads the slug alone: no rail drop, no inductive term. |
| Bus voltage | 220 kΩ / 10 kΩ divider | Before and after each shot gives the charge used. |
| Switch node | 220 kΩ / 10 kΩ divider | For the over-current comparator and for scope work. |
| Temperature | TMP36 or NTC on the FET bar and on a can | Slow; for shot-rate limits. |

**Muzzle tap network.** Each of MA and MB goes through 10 kΩ to its own ADC channel, with BAT85 clamps to 3.3 V and ground. The sequencer subtracts them. Add a second pair of channels through 220 kΩ / 10 kΩ for the high range.

- The low range resolves about 1 mV, which is 0.1 mΩ at 10 A.
- It must be differential. Rail B sits tens of millivolts above RETURN at conditioning current because of the sensor and bar drops.
- With no slug, MA rises to the full bus. The clamp then passes up to about 6 mA into the 3.3 V rail; give that rail a bleed load so it cannot be lifted.

**What is not used.** A sense winding on `L1` reads flux, which depends on slug position, so it is not a current sensor. The ACS772 is not a launch sensor.

### 3.8 Control, Protection Logic and Grounding

**Sequencer (U3).** An RP2040-class board on the power-return ground. It times the pulse, runs conditioning, samples the sense channels and talks to the printer controller. Printer firmware cannot do this job.

**Hardware limits, independent of firmware:**

| Function | Suggested parts | Behaviour |
|---|---|---|
| Maximum on-time | 74HC123 + 74HC08 | INA = HS_CMD AND a 2 ms monostable started by HS_CMD's rising edge. A stuck command cannot hold the switch on. |
| Over-current / desaturation latch | LM393 + 74HC74 | Trips if (BUS+ − SW) exceeds about 6 V more than 20 µs after turn-on. Latches INA low until the sequencer clears it. |
| Supply-good | 2 × optocoupler + zener (§3.4) | EN low unless both gate rails are above 10 V. |
| Firmware abort | — | Cancel the pulse if no current appears within about 30 µs. |

The on-time limit acts on the high-side command, not on EN.

**Grounding decision.** Logic ground is the power return.

- One star point at the low-side sources and film negative. The sequencer ground, the divider bottoms and the ACS772 signal ground meet there by a single wire.
- U1's input side shares that ground. Its isolation is still doing its job for the floating high side.
- VSSB returns only by the Kelvin pair from the low-side sources. Do not add a second bond between VSSB and logic ground on the board.
- The galvanic boundary is between the sequencer and anything else: two optocouplers (FIRE in, FAULT/READY out) to the printer controller, and a USB isolator on any PC link.

**Earth.** The rig floats. A bench supply's earth terminal stays unlinked. An oscilloscope ground lead goes on RETURN and nowhere else.

- If RETURN is earthed through a PC's USB, clipping a scope ground to the switch node shorts the bank through protective earth.
- Probe floating nodes differentially.

### 3.9 Auxiliary Power

| Ref | Part | Note |
|---|---|---|
| PS3 | Floating 12 V, ≥1 A | A double-insulated wall adapter. Feeds PS1, PS2, U2 and the relay coils. Not derived from a gate rail. |
| PS1, PS2 | R12P212S | Isolated gate rails. Maximum capacitive load 680 µF. |
| U2 | 7805, then a 3.3 V LDO | Sequencer, U1 VCCI, U4. |

Sequence: logic and gate rails up and proven before the bars are energised.

## 4. Limits and Mode Configuration

Limits are derived in [`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) §5. The ones that govern wiring and bring-up:

| Limit | Value |
|---|---|
| Peak per FET | 450 A (0.5 ms), 350 A (1 ms); 4+4 ≈ 1.4 kA |
| Bus ceiling, six cans + 2 µH | 19–21 V |
| Bus ceiling, six cans + 1 µH | 16–18 V |
| Bus ceiling, two cans + 2 µH | above 30 V, so the whole bench range is safe |
| Hard turn-off | V_bus + I·√(L_bank/C_film) + Lσ·di/dt ≤ 120 V |
| Bus maximum | 56 V |

| Mode | K2 | HS | LS | Bus |
|---|---|---|---|---|
| Idle | open | off | off (gates tied) | any |
| Conditioning | closed | off | off | 5–28 V |
| Launch, dump | open | one pulse | diodes | set point, under the ceiling |
| Launch, truncated | open | pulse cut early | diodes | ≤30 V until measured |

## 5. Protection Summary

- DC fuse at the source; charge resistor always in circuit.
- Reverse-polarity diode in the charge path.
- Bench current limit ≤1 A while charging.
- Hardware maximum on-time on the high-side command.
- Over-current / desaturation latch.
- Gate-supply supervisor on EN; dead-time interlock set by resistor.
- Low side unable to turn on at first light.
- Bank-reversal clamp through the low-side diodes.
- Hard-wired bleeder and a dump resistor; a voltmeter check before touching the bars.
- Thermal monitoring on the FET bar and a can.
- Enclosure with interlock, backstop behind the target, eye protection, E-stop, fume extraction.

## 6. Layout Directives

- **Commutation loop** (C7–C10 → Q1–Q4 → Q5–Q8 → C7–C10): the smallest area the parts allow. Film cans directly across the legs.
- **Bank next to the film cans**, on wide bars laid as a go-and-return pair.
- **Launch loop** (bank → high side → `L1` → rails → return): short, flat, go-and-return. Its inductance is part of `L1`.
- **Star point** at the low-side sources.
- **Gate leads** as twisted pairs with their returns, under 100 mm, kept away from the bars.
- **Sense leads** twisted; the muzzle pair run along the barrel away from the rails' own loop.
- **Room for a second leg** in the rail B return.
- Test points for bus, switch node, both gates, muzzle voltage and the Rogowski signal.
- Single-sided board with external bars remains acceptable.

## 7. Scaling Notes

- **Capacitors:** 2 → 6 → 12 as voltage ceilings and FET count allow.
- **FETs:** 4+4 → 6+6 → 8+8. The driver IC has current to spare for single pulses; gate power only matters in the high-frequency experiment.
- **`L1`:** swappable. Smaller values shorten the tail and raise the peak.
- **Voltage:** 48–56 V needs a DC-rated charge switch, a ≥60 V fuse, and a measured turn-off budget.

## 8. Bring-Up Order (0–30 V Bench Supply)

Full procedures and exit criteria are in [`TestPlan.md`](TestPlan.md). In outline:

1. **Bench checks, nothing connected.** ESR and capacitance of each can. PS1–PS3 rails under a dummy load.
2. **Logic board only.** Driver outputs into a spare FET's gate. Confirm: EN low by default; dead time; a 10 ms command is cut to about 2 ms; pulling either gate rail drops EN; rail droop during a pulse is under 0.5 V.
3. **Bars, two cans, 2 µH, a copper strap across the rail pads.** Low-side gates tied to sources. Supply at 5 V, current limit 1 A. Fire. Expect about 180–210 A, inside the ACS772's range. Calibrate the Rogowski channel.
4. **Step up:** 10, 15, 20, 25, 30 V (about 1.1–1.2 kA at 30 V). At each step record current, switch node and bus; feel for a FET running hotter than its neighbours.
5. **Truncation at low current** (100, 200, 400 A). Measure overshoot and ring frequency; extract Lσ and the bank-to-film inductance; extrapolate to the 120 V budget before going further.
6. **Six cans.** Obey the ceiling: 19–21 V with 2 µH.
7. **Barrel in place of the strap.** Solid-armature shots, then conditioning, then paste.

No step uses the battery pack.

## 9. Breadboard Placement Sketch

Placement only. First-build populate: eight MOSFETs, two then six cans. Parts match [`UnifiedResonantShoppingList.md`](UnifiedResonantShoppingList.md).

**This is a bring-up jig, not the PCB.** An eventual board will have tighter gate loops, Kelvin sources, pours or bars under the FETs, and no solderless contacts. Do not copy these row numbers into KiCad.

Two physical pieces:

1. **Logic breadboard** — PS3 input, 5 V and 3.3 V, sequencer, U1 on its adapter, the protection logic, sense networks, relay coil drive.
2. **High-current bar strip** — supply input, bank, FETs, `L1`, rails, Rogowski loop, ACS772 current path, ballast and relay contacts. Never through breadboard springs.

They meet only at the two gate pairs, the Kelvin returns, the sense taps and the relay coil.

### 9.1 Logic breadboard

> ```
>  +12 / +5 / +3.3 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
>  GND (to star ★)  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
>
>  1–4        [ PS3 input, 7805, 3.3 V LDO            ]
>  6–16       [ Sequencer (RP2040 board)              ]  ADC, HS_CMD, ARM, relay, isolated link
>  18–21      [ Isolated link: 2 optocouplers         ]  FIRE in, FAULT/READY out
>  23–30      [ 74HC123 + 74HC08 + LM393 + 74HC74     ]  on-time limit, fault latch
>  32–39      [ UCC21551A on SOIC-16 adapter          ]  decoupling soldered to the adapter
>  41–44      [ PS1 R12P212S  (high-side gate rail)   ]  + zener/optocoupler supervisor
>  46–49      [ PS2 R12P212S  (low-side gate rail)    ]  + zener/optocoupler supervisor
>  51–54      [ Dividers: bus, switch node            ]  220k / 10k, clamps
>  55–58      [ Muzzle taps MA, MB                    ]  10k per leg, clamps, two ranges
>  59–60      [ ACS772 signal, Rogowski input         ]
>  61–62      [ Relay coil driver, flyback diode      ]
>  63         [ Gate header: two twisted pairs        ]
> ```

- Solder the driver's decoupling capacitors, DT resistor and input filters onto the adapter itself. Do not plug them in rows away.
- Keep the two isolated secondaries off the breadboard ground rail. VSSA goes only to the switch node; VSSB only to the low-side sources.
- Solid 22 AWG jumpers on the board; no long Dupont leads on gate or sense lines.

### 9.2 High-current bar strip

> ```
>  SUPPLY+ ─ F1 ─ D1 ─ R1 10 Ω ─┬─ BUS+ bar ─┬─ C1–C6 ─┬─ C7–C10 (at the legs) ─┬─ D2, R2
>                               │            │         │                        │
>                               │         Q1–Q4 drains                          │
>                               │         Q1–Q4 sources ─┬─ SW bar ─ L1 pads ─ RAIL A clamp
>                               │         Q5–Q8 drains ──┘
>                               │         Q5–Q8 sources ─ RETURN bar ★
>                               └─ K2 contact ─ R4 ballast ─ RAIL A clamp
>
>  SUPPLY− ─────────────────────── RETURN bar ★ ─ ACS772 ─ (Rogowski loop around this bar) ─ RAIL B clamp
> ```

| Position | Part | Notes |
|---|---|---|
| Supply input | F1, D1, R1 | Charge path only. |
| Bank | C1–C6, then C7–C10 | Electrolytics as close to the film cans as they will sit. Film cans directly across the legs. |
| Bridge | Q1–Q8 on one heatsink bar, tabs isolated | Rg and Rgs at each gate. Low-side gates tied to sources for first light. |
| After the bridge | `L1` two-bolt pads | No relay across them. |
| Conditioning | K2 contacts and R4 | From BUS+ to the rail A clamp. |
| Far end | Rail clamps, same as the print head | Muzzle taps run back as a twisted pair. |
| Return | RETURN bar through ACS772, Rogowski loop around it | Star point at the low-side sources. |
| Across the bank | R2, hard-wired; R3 on a push switch | Not a jumper that can fall out. |

### 9.3 First electrical bring-up on this placement

Follow §8. Steps 1–2 are entirely on the breadboard with a spare FET as the gate load and nothing on the bars. Do not energise the bar strip until the enable default, the on-time limit and the supervisor have each been seen to work.

---

## 10. Status

A net-level description of the re-baselined driver. The power stage is the half-bridge of version 0.1; the gate-drive values, grounding, conditioning path, sensing and protection are new. Every *start* value and every limit awaits the measurements in [`TestPlan.md`](TestPlan.md).

Next concrete step: schematic capture from §2–3, then a layout that respects §6.
