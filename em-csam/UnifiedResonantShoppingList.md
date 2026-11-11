# EM-CSAM Unified Resonant Driver – Shopping List (v0.2)

Companion to [`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) and [`UnifiedResonantSchematic.md`](UnifiedResonantSchematic.md). This is the half-bridge + series inductor driver, **not** a drop-in replacement for the older [`DriverShoppingList.md`](DriverShoppingList.md).

**What changed in 0.2.** The driver was reviewed and re-baselined ([`DesignReview-2026-11.md`](DesignReview-2026-11.md)). Nothing on the 0.1 list is wasted, but several parts have a different job, a few claims about them were wrong, and a short list of additions is needed. Datasheet values below were checked against the manufacturer documents on 2026-11-10; the links and the verified numbers are in [`References.md`](References.md) §1.

**Notes for builders**
- Quantities show **typical first build → designed maximum**. Populate only what you need.
- Prices are approximate USD (mid-2026 street prices) and will fluctuate. Distributor stock and prices were last checked 2026-08-18.
- **Digi-Key is the primary retailer** for semiconductors, sensors and film capacitors. Mouser is the usual alternate.
- PCB layout is **not frozen**. Leave the board itself until schematic capture.
- High-current MOSFETs and the gate driver benefit from buying a few extras.

---

## Nothing bought is wasted: what each part does now

| Part on the 0.1 list | Job in 0.1 | Job in 0.2 |
|---|---|---|
| 4700 µF 100 V electrolytics | "DC energy store, not the tank" | **The pulse-forming capacitor.** With `L_series` they shape the launch pulse. Populate six for useful shots. |
| 4 × 10 µF film | "Pulse film at the legs" | Commutation decoupling only (about 300 A peak each). |
| IRFP4568 × 12 | 4 + 4 + 4 spare | Same. 4+4 carries about 1.4 kA. The low-side four act as diodes at first light. |
| UCC21551ADWR | Half-bridge driver | Same part, now with real decoupling, a dead-time resistor and a supply supervisor. |
| R12P212S × 2 | Isolated gate rails | Same. |
| `L_series` copper | 50 nH–2 µH kit for "≥200 kHz" | 0.5–3 µH pulse-forming coils; later 4–8 augmenting turns on the head. |
| T9AS relay | Bypass across `L_series` | **Conditioning switch** in the ballast path (≤28 V, ≤20 A). Not a bypass. |
| ACS772 200 A | "Protection / peak" for launch | Conditioning current only. It clamps at ±200 A. |
| HS25 10 Ω | Charge resistor, "may be jumpered" | Charge resistor, **never jumpered on a battery**. Buy a second as a dump resistor. |
| MUR1560 | Freewheel clamp | Not in the launch path (150 A surge). Keep for small clamps. |
| 5KP58A × 2 | Bus and rail-pad clamp | One on the bus. The rail-pad one is not a muzzle-arc suppressor (54.5 A). |
| MBR20100CT | Reverse polarity | Same. |
| Small pulse film caps (optional table) | "Experimental series tank" | The series capacitor for the high-frequency experiment. |

---

## How big the bank has to be

Version 0.1 sized the capacitors around a 200 kHz resonance that the circuit does not have. What matters is charge and energy.

**What a shot needs** (constant current, 100 mm barrel):

| Slug | Charge | Loss in a 10–20 mΩ loop at 300 m/s |
|---|---|---|
| 2 mg | 1.2–1.4 C | 30–60 J |
| 1 mg | 1.0 C | 15–30 J |
| 0.5 mg | 0.7 C | 8–15 J |
| 0.25 mg | 0.5 C | 4–8 J |

**What the bank holds:**

| Cans | 30 V | 48 V | 55 V |
|---|---|---|---|
| 2 | 0.28 C, 4.2 J | 0.45 C, 10.8 J | 0.52 C, 14.2 J |
| 6 | 0.85 C, 12.7 J | 1.35 C, 32.5 J | 1.55 C, 42.7 J |
| 12 | 1.69 C, 25.4 J | 2.71 C, 65.0 J | 3.10 C, 85.3 J |

- "Two cans is enough for first shots" was wrong for anything but a strap test or a very light slug. **Two cans are the right first-light bank for a different reason:** with 2 µH they cannot exceed the FET limit anywhere in a 0–30 V range.
- Six cans at 30 V into a short deliver 2.0–2.6 kA, more than four FETs per leg carry. Obey the voltage ceiling in [`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) §5.2.
- Capacitor ESR is about half the loop. Nichicon publishes no kilohertz ESR for these cans; measure it.

Produced by `python3 em-csam/tools/shot_model.py tables` (tables 1–3).

---

## Main BOM (first-revision half-bridge)

| Component | Qty (min→max) | Primary (Digi-Key) | Verified values | Approx. unit | Notes |
|-----------|---------------|--------------------|-----------------|--------------|-------|
| Power MOSFET, TO-247 | 8→16 (+4 spare) | [IRFP4568PBFXKMA1](https://www.digikey.com/en/products/detail/infineon-technologies/IRFP4568PBFXKMA1/16669015) | 150 V; 4.8 mΩ typ / 5.9 max; IDM 684 A; Qg 151 nC ([datasheet](https://www.infineon.com/dgdl/irfp4568pbf.pdf?fileId=5546d462533600a4015356310e811e5b)) | $4–9 | Design to **450 A each for 0.5 ms**, not IDM. Alternatives: [IRFP4468PBFXKMA1](https://www.digikey.com/en/products/detail/infineon-technologies/IRFP4468PBFXKMA1/16669046) 100 V (less voltage margin); [IRFP4668PBFXKMA1](https://www.digikey.com/en/products/detail/infineon-technologies/IRFP4668PBFXKMA1/16669049) 200 V. |
| Isolated dual-channel gate driver | 1 (+1 spare) | [UCC21551ADWR](https://www.digikey.com/en/products/detail/texas-instruments/UCC21551ADWR/24708455) | **A = 5 V UVLO** (turn-on ~6 V), not 8 V. 4 A / 6 A. Only the A is sold in SOIC-16 ([datasheet](https://www.ti.com/lit/ds/symlink/ucc21551.pdf)) | $2–5 | Right part for 12 V rails. Its lockout will not protect the FETs; add the supervisor below. `UCC21551C*` needs ≥13.5 V and will not start on 12 V. |
| Isolated 12 V DC-DC, 2 W | 2 | [R12P212S](https://www.digikey.com/en/products/detail/recom-power/R12P212S/2256185) | Unregulated; 680 µF max load; 1.5–10 pF isolation ([datasheet](https://recom-power.com/pdf/Econoline/RxxP2xx.pdf)) | $8–17 | One per gate rail. Expect 12–13 V lightly loaded. |
| DC-bus electrolytic | 2→12 | [LGU2A472MELC](https://www.digikey.com/en/products/detail/nichicon/LGU2A472MELC/2540733) | 4700 µF 100 V, 35 × 50 mm; ESR ≤56 mΩ at 120 Hz; no kHz ESR published ([catalog](https://www.nichicon.co.jp/english/series_items/catalog_pdf/e-lgu.pdf)) | $4–10 | Two for first light, six for useful shots. Not rated by the maker for rapid, frequent discharge; keep the shot rate low. |
| Bridge film | 4→8 | [B32774D4106K000](https://www.digikey.com/en/products/detail/tdk/B32774D4106K000/3492300) | 10 µF 450 V; ESR 10.9 mΩ; ESL 24 nH; 30 V/µs ≈ 300 A peak ([datasheet](https://www.tdk-electronics.tdk.com/inf/20/20/db/fc_2009/MKP_B32774_778.pdf)) | $5–12 | Directly across the FET legs. More film lowers the turn-off pump. 22 µF alternative: [B32774D4226K000](https://www.digikey.com/en/products/detail/tdk/B32774D4226K000/1884963). |
| HF decouple (C0G) | 8→16 | [C350C104F1G5TA](https://www.digikey.com/en/products/detail/kemet/C350C104F1G5TA/6562499) | 0.1 µF 100 V C0G radial | $1–3 | The ±1 % "F" part is costly; the ±5 % `C350C104J1G5TA` is electrically the same here. |
| Gate resistor | 16 | Search: [`10 ohm 0.5W 1% metal film axial`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=10+ohm+0.5W+1%25+metal+film+axial) | — | $0.10–0.25 | 10 Ω to start. Also buy 2.2 Ω and 4.7 Ω for a faster turn-off path. |
| Gate–source resistor | 16 | Search: [`10k 0.25W 1% metal film axial`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=10k+0.25W+1%25+metal+film+axial) | — | $0.03–0.10 | One per FET. |
| Current sensor (conditioning) | 1 | [ACS772ECB-200B-PFF-T](https://www.digikey.com/en/products/detail/allegro-microsystems/ACS772ECB-200B-PFF-T/9674832) | ±200 A; 10 mV/A; 2.5 µs; clamps beyond range; ≤0.4 A offset after overload ([datasheet](https://www.allegromicro.com/-/media/files/datasheets/acs772-datasheet.pdf)) | $10–15 | **Not a launch sensor.** Re-zero after each shot. Do not buy a 400 A sibling for launch; use the Rogowski loop. |
| Relay (conditioning switch) | 1 | [T9AS1D12-12](https://www.digikey.com/en/products/detail/te-connectivity-potter-brumfield-relays/T9AS1D12-12/254519) | SPST-NO; **DC rating 20 A at 28 VDC**; 75 mΩ initial; 15 ms ([datasheet copy](https://tvsat.com.pl/PDF/1/1-1393210-3.pdf)) | $4–10 | 30 A is its AC rating. Use at ≤28 V in the ballast path. It cannot break a 48–60 V DC circuit. |
| Bus TVS | 1→2 | [5KP58A](https://www.digikey.com/en/products/detail/littelfuse-inc/5KP58A/556577) | 58 V standoff; 64.4 V min breakdown; 93.6 V at 54.5 A | $1.50–3 | Keep the bus ≤56 V. `5KP64A` for a 16s LFP pack. |
| Snubber R | 2→4 | Search: [`2.7 ohm 2W metal oxide axial`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=2.7+ohm+2W+metal+oxide) | — | $0.30–1 | 2.7 Ω to start; tune on the bench. |
| Snubber C | 2→4 | Search: [`10nF 250V C0G`](https://www.digikey.com/en/products/filter/ceramic-capacitors/60?keywords=10nF+250V+C0G) | — | $0.20–1 | 10 nF to start. It damps ringing; it does not absorb the commutation energy. |
| Bleeder | 2→4 | Search: [`1.5k 10W wirewound`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=1.5k+10W+wirewound) | — | $0.80–3 | 14 s time constant with two cans, 42 s with six: 76–102 s to fall below 5 V. Wait, then check with a meter. |
| Charge resistor | 1 | [HS25 10R J](https://www.digikey.com/en/products/detail/ohmite/HS25-10R-J/5307681) | 25 W on a heatsink, 9 W without; no pulse rating published | $3–8 | Never jumpered on a battery. |
| Reverse-polarity Schottky | 1 | [MBR20100CT-E3/4W](https://www.digikey.com/en/products/detail/vishay-general-semiconductor-diodes-division/MBR20100CT-E3-4W/2153208) | 100 V; 10 A per diode | $1.50–4 | Charge path only. |
| Small clamp diode | 2 | [MUR1560G](https://www.digikey.com/en/products/detail/onsemi/MUR1560G/919902) | 600 V; 15 A; IFSM 150 A | $1.50–4 | Not a launch freewheel diode. |
| Temperature sensor | 2 | [TMP36GT9Z](https://www.digikey.com/en/products/detail/analog-devices-inc/TMP36GT9Z/820404) | — | $0.70–2 | One on the FET bar, one on a can. |
| Voltage dividers | 4 sets | Search: [`220k 1% 0.25W metal film`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=220k+1%25+0.25W+metal+film) + [`10k 1% 0.25W metal film`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=10k+1%25+0.25W+metal+film) | — | $0.10–0.30 | Bus, switch node, and the high range of the two muzzle taps. |
| Clamp diodes | 20 | [BAT85S-TAP](https://www.digikey.com/en/products/detail/vishay-general-semiconductor-diodes-division/BAT85S-TAP/3104127) | 30 V / 200 mA Schottky, DO-35 | $0.15–0.50 | Two per ADC input. |
| 5 V / 3.3 V regulators | 1 set | Search: [`L7805CV`](https://www.digikey.com/en/products/filter/voltage-regulators-linear-low-drop-out-ldo-regulators/699?keywords=L7805CV) + [`AMS1117-3.3`](https://www.digikey.com/en/products/filter/voltage-regulators-linear-low-drop-out-ldo-regulators/699?keywords=AMS1117-3.3) | — | $0.50–2 | Fed from the floating 12 V supply, **not** from a gate rail. |
| TO-247 heatsink + hardware | 1 bar | Search: [`TO-247 heatsink`](https://www.digikey.com/en/products/filter/thermal-heat-sinks/219?keywords=TO-247+heatsink) | — | $10–25 | One bar for all eight; tabs isolated. |
| Copper sheet / bar | as needed | McMaster: [copper sheet](https://www.mcmaster.com/products/copper/copper-sheets/) | — | variable | Bars, coil pads, spreader plates. |
| Bolts / hardware | assorted | M5 / M6 stainless + washers | — | $5–15 | Two-bolt clamps. |
| PCB | 1 | **Do not order yet.** | — | $15–60 | — |

---

## Additions for 0.2 (order these)

About $50–90 in total.

### Gate drive and logic

| Item | Qty | What to buy | Why |
|------|-----|-------------|-----|
| Bulk decoupling | 4 | 10 µF 25 V, leaded film or X7R | 10 µF + 0.1 µF at each gate rail, soldered on the adapter. |
| Dead-time resistor | 2 | 51 kΩ 1 % | 452 ns. The DT pin is never left open. |
| Input filter parts | few | 100 Ω, 100 pF C0G | At the driver inputs. |
| Supply supervisor | 2 sets | 9.1 V zener + optocoupler (PC817 class) + 1 kΩ | EN stays low unless both gate rails are above 10 V. |
| Sequencer | 1 (+1) | RP2040 board (Raspberry Pi Pico class) | Times the pulse; printer firmware cannot. |
| On-time limit | 1 set | 74HC123 + 74HC08 | Cuts any high-side command at about 2 ms. |
| Over-current latch | 1 set | LM393 + 74HC74 | Trips on excess drop across the high side. |
| Isolated link | 2 | Optocouplers (PC817 class) | FIRE in, FAULT/READY out, to the printer controller. |
| USB isolator | 1 | ADuM3160-class module | On every PC link. Without it the return bar is earthed through the PC. |
| Logic supply | 1 | Double-insulated 12 V wall adapter, ≥1 A | Floating; feeds the DC-DC inputs, the 7805 and relay coils. |

### Power and protection

| Item | Qty | What to buy | Why |
|------|-----|-------------|-----|
| DC fuse + holder | 1 | 10 A, rated ≥60 VDC (a 10 × 38 mm solar "gPV" fuse is a cheap choice) | Automotive blade fuses are 32 V parts. |
| Ballast resistors | 1 each | 1 Ω, 2.2 Ω, 4.7 Ω, 10 Ω at 25–50 W, chassis mount | Conditioning current limit. |
| Dump resistor + push switch | 1 | 10 Ω 25 W (a second HS25) | Fast safe discharge of the bank. |
| More electrolytics | to 6 | Same LGU2A472MELC | If only two are on hand. |
| More FETs | 4 | Same IRFP4568 | Only if moving to 6+6 with spares. |

### Sensing and diagnostics

| Item | Qty | What to buy | Why |
|------|-----|-------------|-----|
| Rogowski loop | 1 | 30–34 AWG magnet wire, about 100 turns on a 6 mm flexible former, return lead threaded back through the middle | Launch current. Around the return bar. |
| Muzzle tap leads | 1 | Thin twisted pair, high-temperature insulation | Slug voltage. |
| Photogates | 2 | Slotted optical switches, or IR LED + phototransistor pairs | Velocity. |
| Witness plates | several | Copper, aluminium, steel and glass coupons | Splat tests. |

### Head

| Item | Qty | What to buy | Why |
|------|-----|-------------|-----|
| Magnets | 4–8 | NdFeB bars about 40 × 10 × 5 mm, magnetised through the 5 mm, **SH grade** (150 °C) | 0.6–0.9 T across the bore over the downstream 80 mm. Standard N grades weaken above 80 °C. |
| Yoke | 2 | Mild steel strip, 3–5 mm | Flux return; raises the field. |
| Augmenting-turn strip | 1 lot | Copper strip about 4 × 0.5 mm, polyimide tape | 4–8 flat turns over and under the rails. |

### People

Polycarbonate enclosure with an interlock, a backstop behind the target, safety glasses, an emergency-stop switch, and fume extraction. These are part of the kit, not options. A 1 mg slug at 300 m/s will penetrate an eye; the oil mist can ignite; zinc and copper fume cause metal fume fever.

---

## Breadboard / proto kit

Logic and gate drive only — matches [`UnifiedResonantSchematic.md`](UnifiedResonantSchematic.md) §9. Skip cheap "MB-102 + Dupont" kits: sloppy contacts and floppy leads.

Do **not** buy clip-on breadboard 3.3/5 V power hats. They invite mixing the bus into the logic rails.

| Item | Qty | Primary (Digi-Key) | Approx. | Notes |
|------|-----|--------------------|---------|-------|
| Full-size breadboard, 830 point | 1–2 | [BB830](https://www.digikey.com/en/products/detail/busboard-prototype-systems/BB830/19200392) | $9–17 | The 0.2 logic needs more rows than 0.1; a second board or a [BB1660](https://www.digikey.com/en/products/detail/busboard-prototype-systems/BB1660/19200358) helps. |
| Pre-formed 22 AWG jumpers | 1 kit | [WK-2](https://www.digikey.com/en/products/detail/global-specialties/WK-2/5231341) | $7–10 | Solid 22 AWG seats reliably. |
| SOIC-16 → DIP adapter | 2 | [PA0006](https://www.digikey.com/en/products/detail/chip-quik-inc/PA0006/5014721) | $4 | For the wide-body (7.5 mm) DW package. The Digi-Key page does not state body width; confirm the fit and the DIP row spacing on arrival. |
| Breakaway 0.1″ header | 1 | [PRPC040SAAN-RC](https://www.digikey.com/en/products/detail/sullins-connector-solutions/PRPC040SAAN-RC/2775214) | $1–2 | Adapter and gate headers. |

Solder the driver's decoupling capacitors, dead-time resistor and input filters to the adapter pins, not into breadboard rows.

---

## `L_series` winding kit

Do **not** buy a catalog ferrite power inductor. It will saturate.

| Item | What to buy | Notes |
|------|-------------|-------|
| Conductor | 1/4″ or 6 mm copper tube, or doubled 10 AWG | Tube keeps resistance near 1 mΩ; single 10 AWG is about 4 mΩ for a 2 µH coil. |
| Formers | PVC pipe or printed bobbins, about 38 mm diameter | Air core. |
| Target values | **0.5, 1, 2 and 3 µH** | On a 38 mm former: about 4 turns over 20 mm, 6 over 30 mm, 10 over 50 mm, 13 over 65 mm (Wheeler's formula; measure each). |
| Terminals | Two-bolt copper pads, same pattern for every coil | So they swap. |

- Start with 2 µH. It keeps the first-light bank inside the FET limit.
- Smaller values shorten the freewheel tail and raise the peak.
- The 50–150 nH coils on the 0.1 list have no role: the rails and bars already supply that much.
- Measure each coil with an LCR meter or by ringing it against a known film capacitor.

---

## Optional and possibly needed

| Status | Item | When you need it | Candidate | Approx. |
|--------|------|------------------|-----------|---------|
| Optional — HF experiment | Small pulse film 0.22–2.2 µF, 1 kV class | The series-resonant experiment in [`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) §4.4 | [940C10W1K-F](https://www.digikey.com/en/products/detail/cornell-dubilier-knowles/940C10W1K-F/809448) 1 µF; [940C6P22K-F](https://www.digikey.com/en/products/detail/cornell-dubilier-knowles/940C6P22K-F/1929440) 0.22 µF. Check the peak-current rating. | $5–12 |
| Needed for 48–56 V | DC-rated charge switch | Moving from the bench supply to a pack | A relay or contactor rated for the pack voltage, or a MOSFET high-side switch | $10–30 |
| Needed for 48–56 V | Isolated 48–56 V source | Same | Bench supply, or pack through fuse and charge resistor | $40–90 |
| Possibly needed | Adjustable bench supply | If none is on hand | 0–30 V, 5–10 A, current-limited. Enough for all of first light. | $50–100 |
| Optional | Scope current probe or Pearson-class monitor | Independent check on the Rogowski channel | [Pearson](https://www.pearsonelectronics.com/products/wideband-current-monitors) | $$$ |
| Optional | Differential probe | Scope work on the switch node | Any 100 V-class differential probe | $50–300 |
| Optional — later | 15 V gate rails | More gate margin at high current | `R12P215S` class; A-suffix driver still fits | $10–18 |
| Optional — later | Second driver + 8 FETs | A second leg in the rail B return (full bridge) | Same parts | ~$70–100 |
| Optional — later | Solid-state conditioning stage | Faster, finer conditioning | ≥50 µH inductor rated 20 A + comparator + one FET | $10–20 |
| Optional | Fan | Long runs | 12 V 40–60 mm | $5–12 |

---

## Assumed already owned

- BigTreeTech board + Raspberry Pi (or equivalent) for motion; it only sends FIRE to the sequencer.
- A current-limited bench supply. 0–30 V at 10 A covers all of first light.
- An oscilloscope, 100 MHz class, two or more channels.
- An LCR meter, or the patience to do ring tests.
- A pair of thick copper straps for first current tests.

---

## Two circuit parts (breadboard or later PCB)

Treat the driver as two circuits that meet at a few defined points.

**1. Logic, gate drive, sense** — the floating 12 V supply, sequencer, UCC21551, protection logic, dividers, relay coil.

- Fine on a solderless breadboard for bring-up.
- Prove the enable default, the on-time limit and the supervisor **with nothing on the bars**, using a spare FET as the gate load.
- Gate leads are twisted pairs with their returns, under 100 mm.

**2. High-current pulse path** — supply input, bank, film, MOSFETs, `L_series`, rails, bleeder, the ACS772 conductor, the ballast path.

- Never through breadboard springs.
- Short, thick external conductors bolted to wide pads, laid as go-and-return pairs.
- Film cans directly across the FET legs; electrolytics right beside them.
- Bleeder hard-wired.

The two meet only at the FET gates and their Kelvin returns, the sense taps, and the relay coil.

---

## Builder advice

- Buy the driver, MOSFETs, ACS772 and film capacitors from Digi-Key or Mouser. Counterfeits are common on marketplaces.
- **The UCC21551 suffix.** `A` is correct for 12 V rails. Its lockout is about 6 V, so it needs the external supervisor. `C` will not start on 12 V.
- Measure the ESR of every can before the first shot. It sets peak current more than anything else on this list.
- Start with two cans, 2 µH and 5 V into a strap.
- Do not order the PCB or a second leg until the half-bridge has fired cleanly at 30 V.
