# Hardware — what to buy, when, and where

Hermon's parts list for a student **living in Israel**. The detailed per-stage pages are in
[`hardware/`](hardware/README.md); the aircraft's frozen specification is
[`references/hermon-numbers.md`](references/hermon-numbers.md).

> [!IMPORTANT]
> **Prices read 2026-09-22.** Israeli shop prices include 18 % VAT. Import lines are the
> vendor's list price in USD and **exclude shipping and the VAT you owe above $75**.
> 1 USD = ₪3.033. Stock and prices move weekly and the import-VAT threshold changed three
> times in 2025–26: **check before you order.**
> Evidence and confidence labels: [`references/research/israel-drone-hardware-2026-09.md`](references/research/israel-drone-hardware-2026-09.md).

> [!CAUTION]
> Stage 1 brings a 6S lithium-polymer pack into your home. Read [SAFETY.md](SAFETY.md) before
> the parts arrive: charge only on a non-flammable surface or in a LiPo bag, never unattended,
> never above 4.20 V/cell, and store at 3.80 V/cell. **Buy packs in Israel** — lithium is
> effectively not air-freighted to private addresses.

## The three things that make this list different from every online tutorial

1. **The flight electronics are import-only.** Israeli drone retail is DJI retail; the FPV
   shops stock 5-inch racing parts. Nothing here carries ArduPilot-class boards, low-KV
   3110 motors, 65 A 6S ESCs or SiK radios. Plan for 2–4 weeks of post.
2. **The telemetry radio must be reconfigured before you transmit.** Israel's licence-exempt
   sub-GHz window is **917–920 MHz**. You buy the 900 MHz-class radio and constrain it in
   firmware. The "868 MHz" SKU is the wrong band for Israel; the "915 MHz" SKU is the right
   hardware with the wrong default. [09.04](09-telemetry-datalink/09.04-telemetry-917.md)
   does it properly.
3. **The motors are 470 KV, not 1700 KV.** Hermon turns 10-inch propellers on 6S at about
   5,060 rpm. A 5-inch racing motor cannot do that — see
   [`hermon-numbers.md` §2](references/hermon-numbers.md#2-the-powertrain).

## The buying philosophy: don't buy everything at once

1. **Buy per stage, when the lessons need it.** Everything before a stage runs on your laptop
   or in simulation — roughly 60 h of the course happens before Stage 1 has to arrive.
2. **Order Stage 1 at module 02, fly it at module 11.** That is deliberate: the shipping time
   is covered by the eight modules of theory, simulation and SITL in between.
3. **Buy locally when the gap is small** (batteries, chargers, wire, tools, the Pi). Import
   when there is no local seller — which for this build is most of the avionics.
4. **Keep spares of what beginners break:** one motor, one ESC, two sets of props, a spare
   XT60 pair.
5. **Stage 3 is optional.** No lesson requires RTK.

## Stages at a glance

| Stage | Buy when | What it adds | Unlocks |
|---|---|---|---|
| **Tools** ([tools.md](hardware/tools.md)) | before module 04 | 80 W iron, solder, flux, strippers, cutters, hex drivers, heat-shrink, multimeter, LiPo bag, safety glasses | 02.07, 03.04, all of module 04 |
| **1 — First flight** ([stage-1](hardware/stage-1-first-flight.md)) | **order at module 02**, fly at module 11 | 450-class frame; 4× 3110/470 KV motors; 65 A 4-in-1 ESC; H743-class FC; M10 GNSS; ELRS 2.4 GHz TX + 2 RX; SiK 900 MHz pair; 2× 6S 5000 mAh + charger + bag; 10×4.5×3 props; power tree | 02.07, 03.04–03.10, module 04, 05, 08, 09, 11, 12; projects P01, P02, P04, P05 |
| **2 — Computer & vision** ([stage-2](hardware/stage-2-computer-and-vision.md)) | module 14 | Raspberry Pi 5 8 GB + cooler + storage + UPS HAT; camera + gimbal; laser rangefinder; cabling | 05.05, 13.05, module 14, module 15; projects P06, P07 |
| **3 — Precision positioning** *(optional)* ([stage-3](hardware/stage-3-precision-positioning.md)) | module 13, only if you want it | RTK base + rover, or an NTRIP subscription | 13.03 only |
| **4 — Payload & delivery pod** ([stage-4](hardware/stage-4-payload.md)) | module 17 | Servo or EPM release; 3D-printed 250 g practice pods; small spray kit | module 17, capstone |
| **5 — Precision landing & final** ([stage-5](hardware/stage-5-precision-landing.md)) | module 12 (beacon), module 19 (spares) | IR landing beacon + receiver; spares set; flight case | 12.05, module 19; project P08 |

## Cost per stage

Estimates. Israeli lines are ₪ including VAT; import lines are converted at ₪3.033/$ **with**
18 % VAT added but **without** shipping.

| Stage | Cheapest path ≈ ₪ | Recommended path ≈ ₪ |
|---|---|---|
| Tools | 600 | 900 |
| 1 — First flight | **3,200** | **4,300** |
| 2 — Computer & vision | 1,400 | 2,600 |
| 3 — Precision positioning (optional) | 0 (skip) | 2,000 |
| 4 — Payload & delivery pod | 250 | 600 |
| 5 — Precision landing & final | 400 | 1,100 |
| **Core course (tools + 1 + 2)** | **≈ 5,200** | **≈ 7,800** |
| **Everything except stage 3** | **≈ 5,850** | **≈ 9,500** |

## Cheapest path vs recommended path

| Decision | Cheapest | Recommended | Why the recommendation |
|---|---|---|---|
| Flight controller | Matek H743-SLIM ≈ $85 | Holybro Pixhawk 6C $199 | Dual IMU, separate bootloader, a case, and the board the ArduPilot docs assume. The Matek flies the same firmware and is a legitimate choice if the budget is tight |
| ESC | 4× discrete 40 A | Holybro Tekko32 F4 Metal 65 A 4-in-1 $95 | One board, one current sensor, one set of solder joints, and the current headroom for a 40 A punch-out |
| Motors | AliExpress 3110-class 470 KV clone | T-Motor MN3110 KV470 | Published thrust curves, which [02.06](02-motors-escs-props/02.06-prop-motor-matching.md) needs. Buy one spare either way |
| Batteries | 1 × 6S 5000 mAh (₪443) | 2 × 6S 5000 mAh | One pack means one flight per session and a long drive home. Two is the difference between a training day and a training hour |
| Charger | 50 W 6S balance charger | ≥ 100 W with a storage-charge mode | [03.07](03-power-system/03.07-charging-balancing-storage.md) uses the storage mode every session |
| Companion computer | Pi 5 4 GB ₪500 | Pi 5 8 GB ₪800 | Headroom for a detector and ROS 2 at once (module 15) |
| Telemetry | SiK clone pair ≈ $25 | Holybro SiK v3 ≈ $40 | The clone works; the Holybro has the better antenna and the documented firmware. **Both need the 917–920 MHz reconfiguration** |
| RTK (stage 3) | Skip | Skip unless a client needs it | No lesson requires it; 13.03 teaches the theory without the hardware |

## Where to buy

| Kind of part | Go to |
|---|---|
| 6S LiPo packs, chargers, safety bags | **Sollan** (Ra'anana), **Dominator**, **RCBattery**, **C-Hobby** |
| Wire, fuses, XT60, switches, current sensors, solder | **Hackstore** (Rehovot), **4Project** (Yehud) |
| Raspberry Pi 5 and accessories | **Piitel** — the Israeli Raspberry Pi approved reseller |
| microSD, hand tools | **KSP** |
| Connectors and anything catalogued, billed in ₪ with customs handled | **DigiKey Israel** |
| Props and small FPV hardware | **Cell-Tec** (confirm they carry 10 in, their catalogue is 5 in) |
| **Everything else — FC, ESC, motors, GNSS, ELRS, SiK, gimbal, rangefinder** | **Import.** See [importing-to-israel.md](hardware/importing-to-israel.md) |

Full supplier notes, addresses and confidence labels:
[`hardware/suppliers-israel.md`](hardware/suppliers-israel.md).
