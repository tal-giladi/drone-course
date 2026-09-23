# Buying Hermon's parts in Israel — research snapshot, 2026-09-22

Scope: every component of the Hermon build (a 1.45 kg, 450 mm, 6S quadcopter on 10 in props),
sourced for a student **living in Israel**. Prices were read on the named page on the date
given. Israeli shop prices include 18 % VAT.

**Exchange rate used: 1 USD = ₪3.033** (Bank of Israel representative rate, 2026-09-16, carried
over from the robotics course's research —
`robotics-course/references/research/israel-hardware-stage1-2026-09.md`).

Confidence labels, same convention as the robotics course:

- **[V] verified** — I opened the page and read the price, stock or spec.
- **[S] search snippet** — a search-engine summary or a listing, not a page I opened.
- **[E] estimate** — my engineering estimate, not checked against a source in this session.

> [!WARNING]
> **What is still unverified after this pass.** Israeli drone retail is DJI retail. No Israeli
> shop I found stocks ArduPilot-class flight controllers, 3110-class motors, 65 A 6S 4-in-1
> ESCs, M10 GNSS modules or SiK radios. Those lines are marked **[S]/[E] import** below and
> need a live basket check before you order. Do not treat the import prices as quotes.

---

## 1. The headline findings

1. **Flight electronics are import-only.** Israeli hobby retail splits into DJI dealers
   (Dronex, Bargad, DJI Store Israel) and 5-inch FPV racing shops (Cell-Tec, RaceDrones).
   Neither carries the ArduPilot-class parts this build needs. Everything in §4 comes in by
   post.
2. **Batteries and chargers are bought locally and that is not optional.** Lithium packs are
   effectively not air-freighted to private addresses. Sollan, Dominator, RCBattery and RCZone
   all stock 6S packs and balance chargers. **[V]**
3. **The telemetry band is the one true blocker, and the common answer is wrong.** Israel's
   licence-exempt sub-GHz window is **917–920 MHz**. A US "915 MHz" SiK radio defaults to
   902–928 MHz and a European "868 MHz" radio to 863–870 MHz — **neither default sits inside
   the Israeli window.** Buy the 900 MHz-class radio and constrain it in firmware (§3).
4. **The personal-import VAT exemption is $75**, and it moved three times in 2025–26. Above
   $75 you owe 18 % VAT; above $500 duty and purchase tax may apply. **[V, carried over]**
5. **The motor in the original Hermon spec was wrong** and this research is what caught it.
   A 2207 / 1700 KV motor cannot turn a 10 in propeller on 6S. Corrected to a **3110-class,
   470 KV** motor — the value that puts hover at 48 % throttle on 6S. See
   `references/hermon-numbers.md` §2 and the equilibrium solved in
   `02-motors-escs-props/02.06-prop-motor-matching.md`.

---

## 2. Israeli suppliers, checked

| Supplier | URL | Good for | Notes |
|---|---|---|---|
| **Sollan (סולן)** | https://www.sollan.co.il/ | **6S LiPo packs**, buck converters, cells | **[V] HRB 6S 5000 mAh 50C, EC5 plug: ₪443, 2 in stock (2026-09-22).** Pickup in Ra'anana (Sun–Thu 10:00–17:30) is free; registered post or UPS ₪39; same-day Tel Aviv ₪129. The page states 225 g for the pack, which is wrong — a 6S 5000 mAh is ~700–750 g. Weigh it yourself. |
| **Dominator** | https://www.dominator.co.il/ | Gens Ace packs, chargers, RC hardware | **[S]** Gens Ace 6S 6800 mAh ₪950, listed at 961 g, 157×49×60 mm. |
| **RCBattery** | https://rcbattery.co.il/ | LiPo packs (Pulse), the widest Israeli LiPo catalogue | **[S]** 6S line not opened; 2S/3S 5000 mAh pages verified to exist. |
| **RCZone** | https://rczone.co.il/ | **Balance chargers** | **[V, carried over 2026-09-16]** RCToolkit C3 (2–3S only — *not enough for Hermon*, you need a 6S-capable charger). Check their 6S range before ordering. |
| **C-Hobby** | https://c-hobby.co.il/ | **LiPo safety bags** | **[V, carried over]** 20×10 cm fire-resistant bag ≈ ₪35. Buy a larger one for a 6S 5000. |
| **Cell-Tec (סלטק)** | https://www.cell-tec.co.il/ | **Props, 5 in FPV parts, small hardware** | **[V]** Deep 5 in racing catalogue: BrotherHobby, T-Motor, RCinpower, XING, Foxeer, RunCam, RadioMaster. Motors are all 2207/2306 class, ₪59–124. Flight controllers are F4 AIO boards (HGLRC Zeus35 AIO ₪249, SucceX Micro F4 ₪109) — **no ArduPilot-class board, no ESC above 35 A, no 3110-class motor.** No stock indicator on the pages. |
| **Piitel (פייטל)** | https://piitel.co.il/ | **Raspberry Pi 5** (official reseller) — stage 2 | **[V, carried over]** Pi 5 4 GB ₪500, 8 GB ₪800, Active Cooler ₪30, 27 W PSU ₪70. UPS in up to 5 business days. |
| **4Project** | https://www.4project.co.il/ | Pololu/SparkFun distributor: regulators, XT60, connectors, ToF sensors | **[V, carried over]** Shows live stock. Warehouse in Yehud. |
| **Hackstore** | https://hackstore.co.il/ | Wire, fuses, switches, buck converters, INA219/INA226, solder, multimeters | **[V, carried over]** Rehovot. Good for the power-tree parts of [03.04](../../03-power-system/03.04-power-distribution.md). |
| **KSP** | https://ksp.co.il/ | microSD cards, screwdriver sets, hot-glue guns | **[V, carried over]** SanDisk High Endurance 64 GB ₪79; precision screwdriver kit ₪59. |
| **DigiKey Israel** | https://www.digikey.co.il/ | Anything catalogued, billed in ₪, customs handled | **[V, carried over]** ₪ orders arrive in 7–10 business days with DigiKey clearing customs. |
| Dronex / Bargad / DJI Store Israel | dronex.co.il, bargad.co.il, djistore.benda.co.il | **DJI retail and repair only** | **[S]** Not component sources. Useful if you ever want a DJI aircraft for comparison, or a repair bench. |
| RaceDrones Israel | https://race-drones.com/ | FPV community, 5 in builds | **[S]** Informational; catalogue not verified. |

### What no Israeli shop was found to stock

ArduPilot-class flight controllers (Pixhawk / H743) · 2810–3110-class low-KV motors ·
45 A+ 6S 4-in-1 ESCs · u-blox M10 GNSS modules · SiK telemetry radios · ExpressLRS
transmitters and receivers · UAV laser rangefinders · IR precision-landing beacons.
**All of these are import lines.**

---

## 3. Spectrum: what Hermon may legally transmit

| Band | Israeli status | Hermon's use |
|---|---|---|
| 2400–2483.5 MHz | Licence-exempt, ≤ 100 mW e.i.r.p. for the Bluetooth/ANT+ class of device named in the regulations **[V]** | **ExpressLRS control link.** Keep the TX at a legal power setting; a 1 W module is sold but 100 mW-class output is what the exemption contemplates |
| **917–920 MHz** | **Licence-exempt.** The Ministry of Communications opened 917–920 MHz for LoRaWAN-class use (decree reported 2021-05-11); an earlier pilot allocation was 915–917 MHz. The LoRa Alliance published the **AS923-4** regional profile for Israel **[V]** | **MAVLink telemetry.** Buy a 900 MHz-class SiK radio and set `ATS8=917000`, `ATS9=920000`, `ATS10=10` (and the same as `RTS8/9/10` on the remote radio) so all hopping stays inside the window |
| 863–870 MHz (EU SRD) | **Not an Israeli allocation.** Do not buy the "868 MHz" SKU | — |
| 902–928 MHz (US ISM) | Only the 917–920 MHz slice is exempt here. The "915 MHz" SKU is the right *hardware*, with the wrong *default configuration* | Reconfigure before first transmit |
| 433 MHz | 430–440 MHz is amateur-service in the Israeli table (Class A/B, 250 W); it is **not** a general licence-exempt SRD band the way LPD433 is in Europe **[V, amateur table]** | Avoid. Do not buy a 433 MHz telemetry radio |
| 5725–5875 MHz | Moved from prohibited to permit-based in the December 2020 draft regulations **[S]** | The course does not require an FPV video link. If you fit one, check the permit first |

**Type approval.** Israel's Wireless Telegraph regulations run three tracks: licensing,
conformity approval (אישור התאמה), and exemption. Radio equipment you import for personal use
generally needs to fall under an exemption or carry a conformity approval. CE-marked equipment
under the EU Radio Equipment Directive (2014/53/EU) is recognised in the regulations' framing
of the exemption path. **[V, regulation text]** This is the honest summary; it is not legal
advice, and lesson
[09.05](../../09-telemetry-datalink/09.05-spectrum-and-regulation.md) says so too.

**Sources.**
`https://www.nevo.co.il/law_html/law01/502_470.htm` (תקנות הטלגרף האלחוטי (פטור מרישוי)) **[V]** ·
`https://resources.lora-alliance.org/home/the-lorawan-standard-is-open-for-business-in-israel` **[V]** ·
`https://www.iarc.org/wp-content/uploads/2024/12/Frequency-table-Israel-2022.pdf` (amateur allocations) **[V]**

---

## 4. The Stage-1 bill of materials

Reference parts and the substitute spec. **Import prices are list prices in USD, read on the
vendor's own store page unless marked [S]; they exclude shipping and the 18 % VAT you will owe
above the $75 threshold.**

| # | Item | Reference part | Price | Where | Conf. |
|---|---|---|---|---|---|
| 1 | Frame, 450-class | S500 / F450-class glass-fibre + carbon arms | ≈ $35 | AliExpress | [E] |
| 2 | Motors ×4, 3110-class 470 KV, 6S | T-Motor MN3110 KV470 (80 g, 15 A cont., 3–6S) | ≈ $32 ea | T-Motor store / AliExpress | [S] |
| 3 | ESC, 4-in-1, 65 A, 4–6S, DShot600 | Holybro Tekko32 F4 Metal 65 A (AM32) | **$94.99** | holybro.com | [V] |
| 4 | Flight controller, H743-class | Holybro Pixhawk 6C | **$199.00** | holybro.com | [V] |
| 4b | — cheaper substitute | Matek H743-SLIM | ≈ $85 | mateksys / AliExpress | [S] |
| 5 | GNSS, u-blox M10 + compass | Holybro M10 | ≈ $55 | holybro.com | [S] |
| 6 | Control link TX | RadioMaster Pocket / Boxer, ELRS 2.4 GHz | ≈ $65–120 | AliExpress / Cell-Tec | [S] |
| 7 | Control link RX ×2 | ELRS 2.4 GHz receiver | ≈ $12 ea | AliExpress | [S] |
| 8 | Telemetry pair | SiK v3 900 MHz (Holybro or clone) — **reconfigure to 917–920 MHz** | ≈ $40/pair | Holybro / AliExpress | [S] |
| 9 | Propellers, 10×4.5×3, ×6 sets | Gemfan / HQProp 10 in 3-blade | ≈ $4/set | Cell-Tec or AliExpress | [E] |
| 10 | **Battery ×2, 6S 5000 mAh 50C** | HRB 6S 5000 mAh EC5 | **₪443 ea** | **Sollan (Ra'anana)** | **[V]** |
| 11 | **Balance charger, 6S-capable** | ISDT / SkyRC class, ≥ 100 W | ≈ ₪350 | Dominator / RCZone | [E] |
| 12 | **LiPo safety bag** (large) | Fire-resistant, fits a 6S 5000 | ≈ ₪50 | C-Hobby | [S] |
| 13 | Power tree: XT60 pairs, 12 AWG silicone wire, fuse, switch | — | ≈ ₪120 | Hackstore / 4Project | [E] |
| 14 | Bench tools: 80 W iron, solder, flux, strippers, cutters, hex drivers, heat-shrink | — | ≈ ₪600 | Hackstore / KSP | [V, carried over] |

**Stage 1, cheapest path:** frame + motors + Matek H743 + Tekko32 + M10 + ELRS Pocket + 2 RX +
SiK pair + props ≈ **$400 import**, plus ≈ ₪1,500 of Israeli lines (2 packs, charger, bag,
wire, tools). With 18 % VAT on the import, call it **≈ ₪3,200 all-in [E]**.

**Stage 1, recommended path** (Pixhawk 6C instead of the Matek, a better charger, a spare motor
and a spare ESC) ≈ **₪4,300 [E]**.

---

## 5. Import rules that actually bite

Carried over from the robotics-course research, still current on 2026-09-22 unless noted:

- **Personal-import VAT exemption: $75.** Raised to $150 in December 2025, revoked; set to
  $130 in February 2026, revoked on 1 June 2026; **back to $75 from 2 June 2026.** Between $75
  and $500 you owe 18 % VAT; above $500 customs duty and purchase tax may also apply. **[V]**
  *This has changed three times in a year — check it before you place a large order.*
- **Lithium batteries do not fly to private addresses.** Buy packs in Israel. This is why
  items 10–12 above are the only mandatory local lines in Stage 1.
- **Radio transmitters** (items 6, 7, 8) are the import lines most likely to be questioned.
  CE-marked gear is the safer paperwork; see §3.
- **DigiKey Israel bills in ₪ and clears customs for you** (7–10 business days) — worth the
  premium for connectors, wire and anything catalogued, because it removes the customs step.
- **AliExpress** is the realistic source for the frame, motors, props and radios. 2–4 weeks.
  Split orders to stay under thresholds only if that is genuinely cheaper *after* shipping.

---

## 6. Open items for the next research pass

| # | Question | Why it matters |
|---|---|---|
| 1 | Live basket price for the Stage-1 import list, including shipping to Israel | The ≈ ₪3,200 figure is an estimate built from list prices |
| 2 | Does any Israeli shop stock a 6S-capable balance charger, and at what price | Item 11 is [E] |
| 3 | Does Cell-Tec stock 10 in 3-blade props, or is it 5 in only | Item 9 is [E] |
| 4 | T-Motor MN3110 KV470 thrust data **at 22.2 V with a 10 in prop** — the manufacturer only publishes 11.1 V, 14.8 V and larger-propeller rows | The 1,313 g figure in `hermon-numbers.md` is **derived from assumed thrust and power coefficients** ($C_T = 0.095$, $C_P = 0.055$), not read off a table. [02.07](../../02-motors-escs-props/02.07-static-thrust-test.md) is where you measure it, and that is the whole point of that lesson |
| 5 | Current MoC position on 5.8 GHz video permits | Only matters if you fit FPV video |
| 6 | Stage 2–5 sourcing (Pi 5 accessories, gimbal, rangefinder, IR beacon, servo release) | Not needed until module 14 |

---

## Sources

- [Cell-Tec — FPV motors](https://www.cell-tec.co.il/category/מנועים-לרחפני-fpv)
- [Cell-Tec — ESCs and flight controllers](https://www.cell-tec.co.il/category/בקרי-מהירות--טיסה-ל--fpv)
- [Sollan — HRB 6S 5000 mAh](https://www.sollan.co.il/product/%D7%A1%D7%95%D7%9C%D7%9C%D7%AA-%D7%9C%D7%99%D7%A4%D7%95-%D7%A4%D7%95%D7%9C%D7%99%D7%9E%D7%A8-hrb-6s-5000mah-lipo-battery-ec5-plug-50c-22-2v/)
- [Dominator — Gens Ace 6S 6800 mAh](https://www.dominator.co.il/product/%D7%91%D7%98%D7%A8%D7%99%D7%94-%D7%9C%D7%99%D7%A4%D7%95-6-%D7%AA%D7%90%D7%99%D7%9D-gens-ace-6800mah)
- [RCBattery Israel](https://rcbattery.co.il/)
- [Dronex](https://www.dronex.co.il/) · [Bargad](https://bargad.co.il/) · [DJI Store Israel](https://www.djistore.benda.co.il/)
- [Holybro — Pixhawk 6C](https://holybro.com/products/pixhawk-6c)
- [Holybro — Tekko32 F4 Metal 65 A ESC](https://holybro.com/products/tekko32-f4-metal-4in1-65a-esc-65a)
- [T-Motor — MN3110 Navigator](https://store.tmotor.com/product/mn3110-motor-navigator-type.html)
- [LoRa Alliance — the LoRaWAN standard is open for business in Israel (917–920 MHz)](https://resources.lora-alliance.org/home/the-lorawan-standard-is-open-for-business-in-israel)
- [תקנות הטלגרף האלחוטי (פטור מרישוי), תשפ״א-2021](https://www.nevo.co.il/law_html/law01/502_470.htm)
- [Frequency allocations for amateur radio use in Israel, 2022](https://www.iarc.org/wp-content/uploads/2024/12/Frequency-table-Israel-2022.pdf)
- Robotics course: `references/research/israel-hardware-stage1-2026-09.md` (suppliers, import rules, FX rate)
