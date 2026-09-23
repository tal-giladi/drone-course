# Suppliers — Israel

Checked 2026-09-22, or carried over from the robotics course's 2026-09-16 pass where marked.
Confidence labels: **[V]** I opened the page · **[S]** search snippet only · **[E]** estimate.
Full notes and sources:
[`references/research/israel-drone-hardware-2026-09.md`](../references/research/israel-drone-hardware-2026-09.md).

## The short version

> **Israeli drone retail is DJI retail.** The shops that sell "drones" here sell DJI aircraft
> and repair them. The shops that sell drone *parts* sell 5-inch FPV racing parts. **Neither
> stocks what an ArduPilot build needs.** Plan on importing the avionics and buying the
> batteries, wire, tools and the Raspberry Pi locally.

## Batteries, chargers, safety

| Supplier | Where | What | Notes |
|---|---|---|---|
| **Sollan (סולן)** | sollan.co.il · Ra'anana | **6S LiPo packs**, buck converters, 18650 cells | **[V]** HRB 6S 5000 mAh 50C EC5 **₪443**, 2 in stock. Free pickup Sun–Thu 10:00–17:30; post or UPS ₪39; same-day Tel Aviv ₪129. *Their page lists the pack at 225 g, which is wrong — weigh it.* |
| **Dominator** | dominator.co.il | Gens Ace packs, chargers, RC hardware | **[S]** Gens Ace 6S 6800 mAh ₪950, 961 g. |
| **RCBattery** | rcbattery.co.il | Pulse LiPo, the widest Israeli LiPo catalogue | **[S]** 6S line not opened this pass. |
| **RCZone** | rczone.co.il | Balance chargers | **[V, 2026-09-16]** Their verified charger was 2–3S only. **Confirm 6S capability before ordering.** |
| **C-Hobby** | c-hobby.co.il | LiPo safety bags | **[V, 2026-09-16]** 20 × 10 cm bag ≈ ₪35. Buy a larger one for a 6S 5000. |

## Electronics, wire, connectors, sensors

| Supplier | Where | What | Notes |
|---|---|---|---|
| **Hackstore / אלקטרוניכאן** | hackstore.co.il · Rehovot | Wire, fuses, switches, buck converters, INA219/INA226, solder, irons, multimeters, Chinese modules | **[V, 2026-09-16]** The default source for the power tree in [03.04](../03-power-system/03.04-power-distribution.md). |
| **4Project** | 4project.co.il · Yehud | **Pololu / SparkFun / goBILDA distributor**: regulators, XT60, ToF sensors, connectors | **[V, 2026-09-16]** Shows live stock. Pololu's Israeli distributor. |
| **DigiKey Israel** | digikey.co.il | Anything catalogued, **billed in ₪, customs cleared for you** | **[V, 2026-09-16]** 7–10 business days. Worth the premium when you want the customs step to disappear. |
| **Mouser Israel** | mouser.co.il | Same | **[S]** "Free shipping over ₪400". Blocked automated fetch. |

## Raspberry Pi and compute

| Supplier | Where | What | Notes |
|---|---|---|---|
| **Piitel (פייטל)** | piitel.co.il | **Raspberry Pi 5, Pico, cameras, accessories** | **[V, 2026-09-16]** The only Israeli entry on the Raspberry Pi approved-reseller list. Pi 5 4 GB **₪500**, 8 GB **₪800**, Active Cooler ₪30, 27 W PSU ₪70. UPS within 5 business days; pickup by appointment only. |
| **KSP** | ksp.co.il | microSD, hand tools, screwdriver sets | **[V, 2026-09-16]** SanDisk High Endurance 64 GB ₪79. No Pi boards. |

## FPV parts

| Supplier | Where | What | Notes |
|---|---|---|---|
| **Cell-Tec (סלטק)** | cell-tec.co.il | **5-inch FPV racing parts**: motors, AIO flight controllers, cameras, VTX, goggles, props | **[V]** Brands: T-Motor, BrotherHobby, RCinpower, XING, Foxeer, RunCam, RadioMaster, Gemfan. Motors ₪59–124, all 2207/2306 class. Flight controllers are F4 AIO (HGLRC Zeus35 ₪249). **No ArduPilot-class board, no ESC above 35 A, no 3110-class motor.** No stock indicator. Worth a call for 10 in props. |
| **RaceDrones Israel** | race-drones.com | FPV community and information | **[S]** Catalogue not verified. |

## DJI retail and repair — not component sources

**Dronex** (dronex.co.il, ships nationwide in up to 14 business days) · **Bargad**
(bargad.co.il, 100+ models, professional DJI repair workshop) · **DJI Store Israel**
(djistore.benda.co.il, the official importer). **[S]**

Useful if you want a DJI aircraft to fly alongside Hermon, or a repair bench. Not useful for
this build.

## Import sources used by this course

| Source | Good for | Notes |
|---|---|---|
| **Holybro** (holybro.com) | Pixhawk 6C, Tekko32 ESC, M10 GNSS, SiK radios | **[V]** Pixhawk 6C $199, Tekko32 F4 Metal 65 A $94.99. The vendor ArduPilot's own docs assume. |
| **T-Motor** (store.tmotor.com) | MN3110 motors, published thrust curves | **[V]** The thrust data is why the course names this part. |
| **AliExpress** | Frame, props, ELRS, SiK clones, servos, pumps | **[E]** 2–4 weeks. The realistic source for everything cheap. |
| **Matek** (mateksys.com) | H743-SLIM — the budget flight controller | **[S]** |

See [importing-to-israel.md](importing-to-israel.md) before ordering any of them.

## Names that did not check out

Carried from the robotics research: **Kitsat, Elkotec, Nisko, Chip Center, Anodit** — no
resolving store found. **arduino.co.il** redirects to a Google Sites login. **pinum.co.il,
asif-bag.co.il, drivers.org.il** look like machine-translated AliExpress mirrors — avoid.
**Zap.co.il** returns nothing for maker parts.
