# EM-CSAM Unified Resonant Driver – Shopping List (v0.1)

Companion to [`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) and [`UnifiedResonantSchematic.md`](UnifiedResonantSchematic.md). This is the half-bridge + swappable `L_series` + bypass variation, **not** a drop-in replacement for [`DriverShoppingList.md`](DriverShoppingList.md).

**Notes for builders**
- Quantities show **typical first build → designed maximum**. Populate only what you need.
- Prices are approximate USD (mid-2026 street prices) and will fluctuate. Check current stock on the linked page.
- **Digi-Key is the primary retailer** for first-build semiconductors, sensors, and pulse film. Mouser is the usual alternate. LCSC / AliExpress are fine for many passives once the design is proven.
- Always verify pin-compatible alternatives before ordering large quantities.
- PCB layout is **not frozen**. Order long-lead and stressed parts now; leave 0402-only passives, exact connector genders, and the board itself until schematic capture.
- High-current MOSFETs, isolated drivers, and pulse film benefit from buying a few extras.

**Checked 2026-08-18** on Digi-Key US for the primary MOSFET, isolated driver, Hall sensor, and 10 µF film can. Re-check stock the day you order.

---

## Delta vs the v0.1 low-side dump list

| Keep | Drop | Add |
|------|------|-----|
| 48–60 V bus, bolted rail pads, external bus bars, bleeders, charge LED, TO-247-friendly build | Separate preconditioning H-bridge (`BTS7960` / IR2104 module) | Half-bridge: 4–8 FETs **per leg** (8–16 devices) |
| Per-FET gate resistor, optional `Rgs` | `HCPL-3120` + `TC4420` as the **primary** drive | Isolated dual-channel half-bridge driver + two isolated 12 V supplies |
| Hall current sensor, TVS / snubber, copper hardware | Treating `12 × 4700 µF` as the 200 kHz resonant C | Two-tier capacitors (DC-bus electrolytic + pulse film at the bridge) |
| | | External air-core `L_series` kit + bypass relay / shorting bar |
| | | Reverse-polarity, inrush / charge limit, temp sense |

First revision is a **half-bridge**, as stated in the schematic. Do not buy a full-bridge FET pile “just in case.”

If you already bought parts from the v0.1 list, reuse MOSFETs, isolated 12 V modules, ACS772, bleeders, copper, and hardware. Do **not** reuse a leftover `BTS7960` as the launch switch.

---

## Why the capacitor bank is split

The Unified docs want both a useful joule budget (`½CV²`) **and** `f ≈ 1/(2π√(L C)) ≥ 200 kHz`. Those cannot be the same capacitor at 48–60 V:

| C used as the resonant tank | L needed for 200 kHz | Energy at 60 V |
|-----------------------------|----------------------|----------------|
| 6 × 4700 µF (v0.1 bank)     | ~23 pH (impossible)  | ~51 J          |
| 100 µF                      | ~6 nH                | 180 mJ         |
| 10 µF                       | ~63 nH (tight)       | 18 mJ          |
| 2.2 µF                      | ~290 nH (comfortable)| 4 mJ           |

A 0.5 mm-class plug at a few hundred m/s wants tens to hundreds of millijoules kinetic. A few-µF film-only tank is too small unless bus voltage rises a lot.

**Buy a two-tier bank:**

1. **DC bus / energy store** — 63–100 V low-ESR electrolytics on the DC side of the half-bridge. Holds the joules. Does **not** set 200 kHz.
2. **Bridge-local pulse film** — 10–22 µF, 250–450 V polypropylene right at the legs.
3. **Optional small pulse film** — 0.47–2.2 µF if you later want a true small series tank (see the optional table).

`L_series` then sets rise time / resonant-assisted current at ≥200 kHz.

---

## Order now vs wait for layout

| Order now (long-lead, stressed, or unique) | Wait for schematic / PCB |
|--------------------------------------------|--------------------------|
| MOSFETs + extras                           | The PCB itself           |
| Isolated half-bridge driver + isolated 12 V DC-DCs | Exact connector genders / JST vs header |
| ACS772 (or 400 A sibling)                  | 0402 / 0603-only passives whose footprint is still unknown |
| Pulse / DC-link film                       | Final snubber C after bench tune (buy a small assortment now) |
| Bypass relay                               | Solid-state bypass FETs (later revision) |
| Copper sheet / tube for bus bars, `L_series`, shorting bar | Full-bridge extras |
| Charge / bleeder power resistors, TVS, ultrafast clamps | |
| Breadboard + 22 AWG jumpers + PA0006 adapters | Clip-on “breadboard power” 3.3/5 V hats |

---

## Main BOM (first-revision half-bridge)

Links go to a specific Digi-Key product page where one exists. Mouser (or a Digi-Key keyword search) is the alternate.

| Component | Qty (min→max) | Primary (Digi-Key) | Good alternatives | Approx. unit | Notes |
|-----------|---------------|--------------------|-------------------|--------------|-------|
| Power MOSFET, TO-247 | 8→16 (+4 spare; order **12** for first build) | [IRFP4568PBFXKMA1](https://www.digikey.com/en/products/detail/infineon-technologies/IRFP4568PBFXKMA1/16669015) — 150 V, ~5.9 mΩ, in stock ~$8.21 | [IRFP4468PBFXKMA1](https://www.digikey.com/en/products/detail/infineon-technologies/IRFP4468PBFXKMA1/16669046) 100 V / 2.6 mΩ (~$7.75, **use only with TVS+snubber**); [IRFB4110PBF](https://www.digikey.com/en/products/detail/infineon-technologies/IRFB4110PBF/935978) TO-220 100 V (~$4.10); [IPP023N10N5XKSA1](https://www.digikey.com/en/products/detail/infineon-technologies/IPP023N10N5XKSA1/20841774) TO-220 OptiMOS. Mouser: search same OPNs. | $4–9 | Current Infineon OPN of the v0.1 FET. Old `IRFP4568PBF` (no XKMA1) is obsolete. 4 high + 4 low for first board. |
| Isolated dual-channel gate driver | 1→2 (+1 spare) | [UCC21551ADWR](https://www.digikey.com/en/products/detail/texas-instruments/UCC21551ADWR/24708455) — SOIC-16, **8 V UVLO / 6.7 V VDD min** (~$1.70) | [UCC21551ADWKR](https://www.digikey.com/en/products/detail/texas-instruments/UCC21551ADWKR/24708431) SOIC-14 same UVLO. Do **not** buy `UCC21551C*` (13.5 V min — will not run on 12 V). Fallback: [HCPL-3120-000E](https://www.digikey.com/en/products/detail/broadcom-limited/HCPL-3120-000E/669903) × 2 + [FOD3182](https://www.digikey.com/en/products/detail/onsemi/FOD3182/2804328). Old `UCC21520DW` is obsolete. | $2–5 | TI replacement for UCC21520. **A suffix only** if the isolated rails are 12 V. |
| Isolated 12 V DC-DC, 2 W | 2 | [R12P212S](https://www.digikey.com/en/products/detail/recom-power/R12P212S/2256185) Recom 12 V→12 V, 2 W | [R12P212S/X2](https://www.digikey.com/en/products/detail/recom-power/R12P212S-X2/3586187); cheaper 1 W [NME1212SC](https://www.digikey.com/en/products/detail/murata-power-solutions-inc/NME1212SC/1927046) (tight on 8-FET 50 kHz drive). Traco / Murata 12 V 2 W SIP also fine. | $8–17 | One low-side, one high-side. Prefer 2 W over 1 W. 15 V modules are a later option, not required. |
| DC-bus electrolytic | 2→6 | [LGU2A472MELC](https://www.digikey.com/en/products/detail/nichicon/LGU2A472MELC/2540733) 4700 µF **100 V** snap-in (~$8–9) | [LGU1J472MELC](https://www.digikey.com/en/products/detail/nichicon/LGU1J472MELC/2540661) 4700 µF **63 V** (~$7) if you stay strictly ≤60 V and clamp well; Rubycon / Panasonic low-ESR 63–100 V snap-in. Search: `4700uF 100V snap-in low ESR`. | $4–10 | Energy store, **not** the 200 kHz tank. 100 V preferred for resonant rise. Two cans is enough for first shots. |
| Bridge pulse / DC-link film | 4→8 | [B32774D4106K000](https://www.digikey.com/en/products/detail/tdk/B32774D4106K000/3492300) TDK 10 µF 450 V (~$7) | [B32774D4226K000](https://www.digikey.com/en/products/detail/tdk/B32774D4226K000/1884963) 22 µF 450 V; Kemet C4AQ / Vishay MKP1848 10–22 µF 250–450 V. Search: `DC link film 10uF 450V`. | $5–12 | Park these right at the half-bridge legs. |
| HF decouple (C0G ceramic) | 8→16 (factory bag **50**, or ~15 singles) | [C350C104F1G5TA](https://www.digikey.com/en/products/detail/kemet/C350C104F1G5TA/6562499) Kemet GoldMax 0.1 µF **1%** 100 V C0G, **radial**, 10.16 mm lead spacing | Other 100 nF 100 V+ C0G radial (5% `J` suffix is cheaper and electrically the same here). Not 1206 SMD. | $1–3 (1% is spendy) | One at each FET + driver VDDA/VDDB/VCCI. Bulk bag is 50; Digi-Key Bulk still sells singles. Does **not** replace the 10 µF film. |
| Gate resistor | 16 | Search: [`4.7 ohm 0.5W 1% metal film axial`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=4.7+ohm+0.5W+1%25+metal+film+axial) | 10 Ω same family. Buy a 10-pack of each and pick on the bench. | $0.10–0.25 | One per designed FET footprint. 0.5 W preferred (pulse). |
| Gate–source resistor (optional but recommended) | 16 | Search: [`10k 0.25W 1% metal film axial`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=10k+0.25W+1%25+metal+film+axial) | Any 10 kΩ ¼ W. | $0.03–0.10 | Keeps the gate defined when the driver is off. |
| Current sensor (protection / peak) | 1→2 | [ACS772ECB-200B-PFF-T](https://www.digikey.com/en/products/detail/allegro-microsystems/ACS772ECB-200B-PFF-T/9674832) 200 A bidirectional, 200 kHz (~$10.54) | 250 A / 400 A ACS772 siblings; ACS37200. [Family](https://www.digikey.com/en/products/base-product/allegro-microsystems/620/ACS772/300586). | $10–15 | Bandwidth is **at** the launch frequency — good for peak / protect, not a waveform instrument. |
| Bypass relay | 1→2 | [T9AS1D12-12](https://www.digikey.com/en/products/detail/te-connectivity-potter-brumfield-relays/T9AS1D12-12/254519) TE 30 A SPST, 12 V coil (~$6.40) | T9G / T92 30 A; automotive ISO mini 80 A (Amazon / rocker-relay). Coil transistor + flyback diode from the junk box or a 2N7002 / 2N2222 pack. | $4–10 | Rated for preconditioning current (5–20 A class), **not** launch current. Launch path is `L_series` with this open. |
| Manual copper shorting bar | 1 | Cut from the bus-bar copper below | — | (copper stock) | Lowest-inductance bypass for bring-up if the relay is late. |
| Bus / output TVS | 2→4 | [5KP58A](https://www.digikey.com/en/products/detail/littelfuse-inc/5KP58A/556577) or bulk [5KP58A-B](https://www.digikey.com/en/products/detail/littelfuse-inc/5KP58A-B/3427764) — 58 V standoff, ~93.6 V clamp, 5 kW, **P600 axial** (~$1.50–3) | [1.5KE68A-B](https://www.digikey.com/en/products/detail/littelfuse-inc/1-5KE68A-B/714924) 1.5 kW DO-201 if 5KP is empty. `5KP64A` if the pack sits near 58 V full (16s LFP). SMD: [5.0SMDJ58A](https://www.digikey.com/en/products/detail/littelfuse-inc/5-0SMDJ58A/2024341). Bidirectional is `CA`. | $1.50–3 | Unidirectional (`A`) on the DC bus. One on the bus, one across the rail pads. 58 V standoff is right for a 48 V / 13s pack (~55 V full). |
| Freewheel / clamp diode | 2 | [MUR1560G](https://www.digikey.com/en/products/detail/onsemi/MUR1560G/919902) 600 V 15 A ultrafast TO-220 (~$2.50) | Any 150 V+ ultrafast or SiC Schottky in TO-220. Search: `ultrafast diode 200V 15A TO-220`. | $1.50–4 | Shares work with the FET body diodes. |
| Snubber R | 2→4 | Search: [`22 ohm 2W metal oxide axial`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=22+ohm+2W+metal+oxide) | 10–47 Ω pulse-safe. Tune on the bench. | $0.30–1 | One RC per half-bridge leg. |
| Snubber C | 2→4 | Search: [`4.7nF 250V C0G`](https://www.digikey.com/en/products/filter/ceramic-capacitors/60?keywords=4.7nF+250V+C0G) or small pulse film | 1–10 nF 250 V+ film / C0G. | $0.20–1 | Start at a few nF; do not guess a final value from this list. |
| Bleeder | 2→4 | Search: [`1.5k 10W wirewound`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=1.5k+10W+wirewound) or [`2k 10W chassis`](https://www.digikey.com/en/products/filter/chassis-mount-resistors/54?keywords=2k+10W) | Any 1–2 kΩ 5–10 W. Same as v0.1. | $0.80–3 | Size total dissipation for a few-second dump of the electrolytic bus. |
| Charge / inrush limiter | 1 | [HS25 10R J](https://www.digikey.com/en/products/detail/ohmite/HS25-10R-J/5307681) 10 Ω 25 W chassis (~$5.35) | 10–47 Ω 25 W; or an NTC inrush + optional relay. Search: `25W 10 ohm chassis`. | $3–8 | Soft-charges the bank. Bypass it after the bus is up if you want faster recharge. |
| Reverse-polarity (series Schottky) | 1 | [MBR20100CT-E3/4W](https://www.digikey.com/en/products/detail/vishay-general-semiconductor-diodes-division/MBR20100CT-E3-4W/2153208) Vishay 100 V / 20 A dual common-cathode TO-220 (~$3) | [MBR20H100CT](https://www.digikey.com/en/products/detail/taiwan-semiconductor-corporation/MBR20H100CT/7377448); any 100 V 10–20 A TO-220 Schottky. Do **not** pair with a P-FET in series. | $1.50–4 | Pack+ → anode(s), cathode → bus (parallel both anodes if you like). Charge current only; launch does not go through it. ~0.6–0.8 V drop while charging. Skip only if you never swap the battery leads. |
| Temperature sensor | 2 | [TMP36GT9Z](https://www.digikey.com/en/products/detail/analog-devices-inc/TMP36GT9Z/820404) TO-92 (~$1.85) | [NTCLG100E2103JB](https://www.digikey.com/en/products/detail/vishay-beyschlag-draloric-bc-components/NTCLG100E2103JB/773999) 10 k NTC (~$0.70) glued to the FET bar. | $0.70–2 | One on the MOSFET bar, one on board copper near the bus. |
| Charge LED + resistor | 1 set | Search: [`5mm red LED`](https://www.digikey.com/en/products/filter/led-indication-discrete/94?keywords=5mm+red+LED) + [`10k 0.25W`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=10k+0.25W) | Any. | $0.20 | Visible when the bank is charged. |
| Bus / rail voltage divider | 2 sets | Search: [`220k 1% 0.25W metal film`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=220k+1%25+0.25W+metal+film) + [`10k 1% 0.25W metal film`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=10k+1%25+0.25W+metal+film) | [`200k 1% 0.25W`](https://www.digikey.com/en/products/filter/through-hole-resistors/53?keywords=200k+1%25+0.25W+metal+film) + same 10k (less headroom). 0.1% if you care about absolute volts. **Not** 100k/10k unless the ADC is 5 V. | $0.10–0.30 | For a **3.3 V ADC** (typical BTT / STM32): 220k/10k → 48 V≈2.09 V, 60 V≈2.61 V, 65 V≈2.83 V. 200k/10k is 2.29 / 2.86 / 3.10 V. Old 100k/10k is 11:1 and hits ~5.5 V at 60 V. Clamp each tap with the BAT85s below; the ratio must stay under the rail so the diodes only catch spikes. |
| Divider clamp diodes | **10** | [BAT85S-TAP](https://www.digikey.com/en/products/detail/vishay-general-semiconductor-diodes-division/BAT85S-TAP/3104127) Vishay 30 V / 200 mA Schottky, **DO-35 axial** (~$0.20–0.50) | Other axial BAT85 / [1N5819](https://www.digikey.com/en/products/filter/diodes-rectifiers-single/280?keywords=1N5819). Not SOD-523 `BAT54KFILM` (too small to hand-solder). | $0.15–0.50 | Two per divider if you clamp both ways (tap→3.3 V and tap→GND) → 4 for bus + rail sense. Order 10; they are cheap and you will use extras on test points. Cathode band to the MCU rail (or GND for the lower clamp). |
| 5 V / 3.3 V housekeeping | 1 set | Search: [`AMS1117-3.3`](https://www.digikey.com/en/products/filter/voltage-regulators-linear-low-drop-out-ldo-regulators/699?keywords=AMS1117-3.3) + [`L7805CV`](https://www.digikey.com/en/products/filter/voltage-regulators-linear-low-drop-out-ldo-regulators/699?keywords=L7805CV) | Better LDOs (AP2112, AMS1117-5.0) if you already have a favorite. | $0.50–2 | From the 12 V isolated rail or a small aux input. |
| Logic connectors | see proto kit | Breakaway headers in the **Breadboard / proto kit** below | JST-XH later if the BTT harness already uses it. | — | FIRE, PWM, bypass, fault, sense. |
| TO-247 heatsink + hardware | 1 bar or 8 clips | Search: [`TO-247 heatsink`](https://www.digikey.com/en/products/filter/thermal-heat-sinks/219?keywords=TO-247+heatsink) + [`TO-220 insulating pad`](https://www.digikey.com/en/products/filter/thermal-pads-sheets/219?keywords=TO-220+sil-pad) + [`M3 shoulder screw`](https://www.digikey.com/en/products/filter/screws-bolts/562?keywords=M3+socket+cap) | A single aluminum bar drilled for 8 TO-247s is better than 8 tiny sinks. | $10–25 | Isolate tabs from the bar unless all drains are common (they are not — half-bridge). |
| Bus bar / flexible copper | as needed | Metals / McMaster: [copper sheet](https://www.mcmaster.com/products/copper/copper-sheets/) 0.016–0.032″ (0.4–0.8 mm) or thicker | Amazon copper flashing; leftover flexible strip from the v0.1 build. | variable | External high-current path. Also used for the `L_series` pads and shorting bar. |
| Copper spreader washers / plates | 4–8 | Cut from 1–2 mm copper sheet (same McMaster copper family) | — | low | 2-bolt rail clamps **and** `L_series` terminals. |
| Bolts / hardware | assorted | Hardware store or McMaster M5 / M6 stainless + steel washers | — | $5–15 | Same 2-bolt clamp idea as v0.1. |
| PCB | 1 | **Do not order yet.** | JLCPCB / PCBWay 2.0–2.4 mm, 2–3 oz when layout exists. | $15–60 | — |

**Approximate total for a minimal first build** (8 FETs + 4 spares, 2× 100 V electrolytics, 4× 10 µF film, driver + 2 isolated 12 V, ACS772, relay, TVS/diodes, bleeders, copper, heatsink): **$180–300** depending on how much copper/hardware you already have.

Designed-max populate (16 FETs + 6 electrolytics + 8 film) adds roughly another $80–140.

Add **~$25–35** for the dedicated breadboard kit below if you do not already have a good 830-point board and 22 AWG jumpers.

---

## Breadboard / proto kit (order now)

Logic / gate-drive only — matches [`UnifiedResonantSchematic.md`](UnifiedResonantSchematic.md) §9. There is no single Digi-Key kit that includes the board, 22 AWG jumpers, **and** the SOIC adapter. Buy these on the same order as the semiconductors. Skip cheap Amazon “MB-102 + Dupont” kits: sloppy contacts and floppy leads on the UCC21551 / SIP modules.

Do **not** buy clip-on breadboard 3.3/5 V power hats. They fight the isolated 12 V plan and invite mixing the pack into the logic rails.

| Item | Qty | Primary (Digi-Key) | Good alternatives | Approx. | Notes |
|------|-----|--------------------|-------------------|---------|-------|
| Full-size breadboard, 830 point | 1 | [BB830](https://www.digikey.com/en/products/detail/busboard-prototype-systems/BB830/19200392) BusBoard (~$9) | [BB1660](https://www.digikey.com/en/products/detail/busboard-prototype-systems/BB1660/19200358) (~$17) — two 830s side-by-side if you want MCU 3.3 V away from the isolated 12 V SIPs. 3M framed boards (~$85–160) are overkill. | $9–17 | Same layout as the §9 sketch. Better springs than generic white boards. |
| Pre-formed 22 AWG jumpers | 1 kit | [WK-2](https://www.digikey.com/en/products/detail/global-specialties/WK-2/5231341) 140 pcs (~$9) | Twin Industries 140-pc kits. | $7–10 | Solid **22 AWG** is the only gauge that seats reliably. Use these on the board, not Dupont. Fine for 12 V / 5 V / gate-drive; not for launch or 5–20 A preconditioning. |
| SOIC-16 → DIP adapter | 2 | [PA0006](https://www.digikey.com/en/products/detail/chip-quik-inc/PA0006/5014721) Chip Quik, **300 mil** (~$4) | Any 300 mil SOIC-16 breakout. Not 150 mil / “narrow” SOIC-16. | $4 | Matches `UCC21551ADWR` (DW). One working, one spare. |
| Breakaway 0.1″ header | 1 | [PRPC040SAAN-RC](https://www.digikey.com/en/products/detail/sullins-connector-solutions/PRPC040SAAN-RC/2775214) 40-pin (~$1.25) | Any 0.1″ single-row breakaway. | $1–2 | Snap a 16 for the PA0006; leftovers for MCU and gate headers. |
| M–M Dupont (optional) | 1 pack | Search: [`jumper male-male 40 2.54`](https://www.digikey.com/en/products/filter/jumper-wire/640?keywords=jumper+male-male+40+2.54) | — | $3–6 | Only for the BTT/Pi harness **off** the board. Gate header → FET gates: short 22 AWG, not a 20 cm rainbow. |

Splay TO-220 legs (L7805) slightly so they do not wreck the springs. R12P212S SIP modules fit 0.1″ as-is.

---

## `L_series` winding kit (order copper now)

Do **not** buy a catalog ferrite power inductor. It will saturate at launch current.

| Item | Qty | What to buy | Notes |
|------|-----|-------------|-------|
| Coil conductor | 1 lot, enough for 4–5 coils | 10–12 AWG copper (magnet or hookup) **or** 1/4″ / 6 mm copper tube. McMaster / electrical supplier. Search Digi-Key only if you want magnet wire: [`10 AWG magnet wire`](https://www.digikey.com/en/products/filter/magnet-wire/88?keywords=10+AWG+magnet+wire). | Tube is nicer for high pulse current and air cooling. |
| Formers | DIY | PVC pipe or 3D-printed bobbins, ~20–40 mm diameter | Air-core. |
| Target values | 5 | **~50 nH, 150 nH, 500 nH, 1 µH, 2 µH** | Same 2-bolt pad pattern so they swap. A ~100 mm rail pair is already ~50–150 nH plus bus, so the middle of this kit is the useful range. |
| Terminals | with rail hardware | Same copper washers + M5/M6 | Keep the loop tiny. |

Wind after the first `L_rails` estimate if you want; the copper can sit on the shelf until then.

---

## Optional and possibly needed

Called out separately so they are **not** mistaken for the first-order core kit. Buy from this table only if the note matches what you are actually doing.

| Status | Item | When you need it | Candidate (Digi-Key / other) | Approx. |
|--------|------|------------------|------------------------------|---------|
| Optional — later SMD upgrade | 100 V TOLL OptiMOS | After the TO-247 board works and you want lower Qg / more parallel current on a multi-layer PCB | [IPT015N10N5ATMA1](https://www.digikey.com/en/products/detail/infineon-technologies/IPT015N10N5ATMA1/5213939) 100 V, 1.5 mΩ, ~$6.67. Hard to hand-solder. | $7 |
| Optional — 200 V TO-247 | Extra voltage margin | If 150 V still feels tight once you see overshoot | [IRFP4668PBFXKMA1](https://www.digikey.com/en/products/detail/infineon-technologies/IRFP4668PBFXKMA1/16669049) 200 V. Often long lead time. | $7–16 |
| Optional — experimental series tank | Small pulse film 0.47–2.2 µF | Only if you try a true small-C resonant tank instead of a stiff DC bus | [940C10W1K-F](https://www.digikey.com/en/products/detail/cornell-dubilier-knowles/940C10W1K-F/809448) 1 µF 1 kV pulse; [940C6P22K-F](https://www.digikey.com/en/products/detail/cornell-dubilier-knowles/940C6P22K-F/1929440) 0.22 µF. Buy 4. | $5–12 |
| Optional — waveform current sense | Current transformer | If you want to **scope** the ≥200 kHz burst. ACS772 will not resolve the ring well. | Cheap: [CST206-3A](https://www.digikey.com/en/products/detail/triad-magnetics/CST206-3A/242543) 20–200 kHz, 70 A — OK for preconditioning / low-energy shots, will saturate at launch peak. Real instrument: [Pearson 411](https://www.pearsonelectronics.com/products/wideband-current-monitors) (not Digi-Key; expensive). | $7 / $$$ |
| Optional — higher-range Hall | ACS772 400 A class | If first shots clip the 200 A sensor | Search ACS772 family: [ACS772](https://www.digikey.com/en/products/base-product/allegro-microsystems/620/ACS772/300586) | $11–15 |
| Possibly needed | Isolated 48–60 V PSU | If you do not already have a bench / Mean Well-class 48–60 V supply of a few amps | Search: [`Mean Well 48V 5A`](https://www.digikey.com/en/products/filter/ac-dc-converters/922?keywords=Mean+Well+48V+5A) or [`Mean Well 60V`](https://www.digikey.com/en/products/filter/ac-dc-converters/922?keywords=Mean+Well+60V). Must be isolated from the BTT/Pi earth if you keep a common bench ground. | $40–90 |
| Possibly needed | Dummy-load power resistors | Bring-up before a real barrel (schematic §8 steps 3–5) | Search: [`50 ohm 50W chassis`](https://www.digikey.com/en/products/filter/chassis-mount-resistors/54?keywords=50+ohm+50W+chassis) — buy 2–4 to series/parallel. | $5–12 |
| Optional — bootstrap-only fallback | Half-bridge bootstrap driver | If isolated DC-DCs are out of stock. Weaker for a one-shot launch burst. | Search: [`IR2110PBF`](https://www.digikey.com/en/products/filter/gate-drivers/730?keywords=IR2110PBF) + ultrafast bootstrap diode. | $2–4 |
| Optional — 15 V gate rails | Isolated 15 V 2 W | If you want more Vgs margin than 12 V | Search: [`R15P215S`](https://www.digikey.com/en/products/filter/dc-dc-converters/922?keywords=R15P215S) or `isolated 15V 2W SIP`. Must still match driver UVLO (A suffix is fine). | $10–18 |
| Optional — full-bridge later | 2nd driver + 8 more FETs | Only if bipolar / higher effective voltage is justified | Same MOSFETs + a second UCC21551ADWR | ~$70–100 |
| Optional — solid-state bypass | Paralleled MOSFETs or a small contactor | High repetition-rate firing; not rev 1 | Same TO-247 FET family, or a Kilovac-class EV relay (overkill). | $20+ |
| Optional — ignition tick | Separate HV / HF tick generator | Explicitly **not** required for first revision (schematic §2) | Do not buy a Tesla / flyback module for this yet. | — |
| Possibly needed | Interlock switch / E-stop | Shop safety; schematic wants an inhibit | Search: [`emergency stop 22mm NC`](https://www.digikey.com/en/products/filter/configurable-switch-body/196?keywords=emergency+stop+22mm) or a big NC mushroom from the hardware store. | $8–20 |
| Optional — desat / fast OC latch | Comparator + TVS + latch | If you implement discrete desat instead of relying on ACS772 + firmware | Search: [`LM393P`](https://www.digikey.com/en/products/filter/comparators/370?keywords=LM393P) + [`74HC74`](https://www.digikey.com/en/products/filter/logic-flip-flops/705?keywords=74HC74N) + a 10–15 V zener. Fine to wait for schematic. | $2 |
| Optional — fan | Forced air on the FET bar | Long preconditioning runs | Any 12 V 40–60 mm fan. Search: [`12V 40mm fan`](https://www.digikey.com/en/products/filter/dc-brushless-fans-ac-fans-blowers/217?keywords=12V+40mm+fan). | $5–12 |
| Optional — low-drop reverse-polarity | Ideal-diode IC + N-FET, or P-FET | Only if you want to avoid the Schottky’s ~0.7 V charge drop | IC path: [LM74700QDBVRQ1](https://www.mouser.com/ProductDetail/Texas-Instruments/LM74700QDBVRQ1) (often in stock at Mouser when Digi-Key is empty) + [IRFB4110PBF](https://www.digikey.com/en/products/detail/infineon-technologies/IRFB4110PBF/935978). Do **not** use a P-FET (`IRF9540NPBF`) with gate tied straight to pack− — \(V_{GS}\) max is ±20 V on a 48–60 V pack. | $5–8 |

---

## Assumed already owned (do not force-buy)

- BigTreeTech board + Raspberry Pi (or equivalent MCU) for FIRE / PWM / bypass GPIO
- Isolated 48–60 V bench or Mean Well-class PSU (see optional table if you do not have one)
- Scope with a differential probe or two isolated channels — you will need it for 200 kHz bring-up
- Dummy barrel or a pair of thick copper straps for first current tests

---

## Schematic §3 coverage

Every block in [`UnifiedResonantSchematic.md`](UnifiedResonantSchematic.md) §3 has a BOM line, or is called out as already-owned / wait-for-layout:

| Block | Where it lives |
|-------|----------------|
| 3.1 DC input & charging | Reverse-polarity Schottky, TVS, charge resistor, bleeders, bus divider |
| 3.2 Pulse capacitor bank | Electrolytics + bridge film + HF decouple |
| 3.3 Power bridge | TO-247 MOSFETs, snubber RC, clamp diodes, heatsink |
| 3.4 Gate drive | UCC21551A, isolated 12 V × 2, Rg / Rgs |
| 3.5 `L_series` + bypass | Winding kit, T9AS relay, copper shorting bar |
| 3.6 Rail output | Bus bars, copper washers, output TVS, ACS772 |
| 3.7 Sensing | ACS772, dividers, TMP36 / NTC |
| 3.8 Control & MCU interface | Headers; isolation is the gate driver. Exact pin gender waits for layout. |
| 3.9 Auxiliary power | Isolated 12 V + 5 V / 3.3 V LDOs |
| Optional ignition tick | Optional table — not rev 1 |

---

## Two circuit parts (breadboard or later PCB)

Treat the driver as two circuits that only meet at a few well-defined points. This split is the home-build layout, not a temporary hack. It applies to a first solderless-breadboard checkout of the logic and to the eventual simple PCB.

**1. Logic / gate drive / sense** — 12 V isolated supplies, UCC21551, PWM / enable / fault, voltage dividers, TMP36, relay coil, MCU headers.

- Fine on a solderless breadboard for bring-up (SOIC driver needs an adapter), or on a soldered proto / later PCB.
- Prove dead time and isolated 12 V **with no 48 V connected**, using a dummy gate load (spare FET or ~10 nF).
- If you split across two boards, put this side on one and power on the other. Do **not** run long jumper wires for MOSFET gates or the power return; the gate loop must stay as short as the power loop.

**2. High-current pulse path** — battery/bus, electrolytics, pulse film, MOSFET drain/source, `L_series`, bypass, rails, bleeder, ACS772 *current* conductor.

- Never through solderless-breadboard springs (amp-class contacts; extra inductance wrecks ≥200 kHz and spikes the FETs).
- Current rides on short, thick **external** conductors — copper bar, laminated strip, or a few paralleled heavy wires — bolted to wide pads. Board copper only provides landing pads, not the pulse path. “Floating bars” above or beside a simple single-sided board is the intended construction.
- Close the loop *C_tank → half-bridge → L_series / bypass → rails → return* in as small an area as you can physically fold. Wires are acceptable for a first jig if they are short, fat, and laid flat as a go/return pair or sandwich. A long flying lead to the barrel is unbudgeted inductance.
- Bleeder must be hardwired (not a jumper that can fall out). The Hall sensor body can sit next to the logic; its heavy current path stays on the bars.

The two sides touch only at FET gates (and `Rgs`), isolated-supply returns, sense taps, and the bypass-coil drive. That is enough for a later PCB to stay simple: control and landing pads on the board, bus bars for current.

---

## Builder advice

- Order extras of MOSFETs, the isolated driver, and at least two spare film cans. Those are the parts you will stress on first shots.
- Buy the driver, MOSFETs, ACS772, and pulse film from Digi-Key or Mouser. Counterfeit gate-drive optos and Hall sensors are common on marketplaces.
- **Confirm the UCC21551 suffix.** `A` = 6.7 V VDD min (correct for 12 V isolated modules). `C` = 13.5 V min and will sit in UVLO forever on 12 V.
- If any v0.1 `IRFP4568` / isolated 12 V bricks / ACS772 / copper / hardware are already on the shelf, reuse them and subtract from this list.
- Keep a small stock of 1–2 mm copper plate and the custom flexible strip for high-current joints.
- Do not order the PCB, a full-bridge FET set, or an ignition-tick HV box until the half-bridge rings into a dummy load.
