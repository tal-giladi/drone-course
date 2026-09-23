# Stage 1 — first flight (Hermon's core)

**Order at module 02. Fly at module 11.** The eight modules in between are theory, simulation
and SITL — they are what covers the 2–4 weeks of shipping.

Target aircraft: 1.45 kg, 450 mm, 6S, 10 × 4.5 × 3 props, 226 W hover, 22 min.
Full specification: [`references/hermon-numbers.md`](../references/hermon-numbers.md).

> [!IMPORTANT]
> Two lines on this list are **not** what an online build guide will tell you to buy.
> Read [§why](#why-two-parts-differ-from-every-tutorial) before you order.

## The list

Israeli lines are ₪ including VAT. Import lines are the vendor's USD list price; add shipping
and 18 % VAT above the $75 threshold. Confidence labels are explained in
[the research file](../references/research/israel-drone-hardware-2026-09.md).

### Airframe and powertrain — import

| # | Item | Reference part | Substitute spec | ≈ price | Conf. |
|---|---|---|---|---|---|
| 1 | Frame, 450-class | S500 or F450-class, glass-fibre centre plates, carbon arms | 400–500 mm wheelbase, ≥ 8 mm arm, integrated PDB acceptable | $35 | [E] |
| 2 | **Motors ×4 (+1 spare)** | **T-Motor MN3110 KV470** — 80 g, 15 A cont., 3–6S | **3110-class stator, 420–520 KV, ≥ 15 A continuous, 6S-rated, M3 mounting** | $32 ea | [S] |
| 3 | ESC, 4-in-1 | Holybro Tekko32 F4 Metal 65 A (AM32) | 4-in-1, ≥ 50 A continuous, 4–6S, DShot600, current sensor, 30.5 × 30.5 mm | **$94.99** | [V] |
| 4 | Propellers ×6 sets | Gemfan or HQProp 10 × 4.5, 3-blade | 10 in diameter exactly, 4.0–5.0 in pitch, 3-blade, M5 bore | $4/set | [E] |

### Avionics — import

| # | Item | Reference part | Substitute spec | ≈ price | Conf. |
|---|---|---|---|---|---|
| 5 | Flight controller | **Holybro Pixhawk 6C** | STM32H743 or F765, ≥ 5 UARTs, dual IMU, baro, SD card slot, ArduPilot target exists | **$199.00** | [V] |
| 5b | — budget substitute | Matek H743-SLIM | same spec, one IMU | $85 | [S] |
| 6 | GNSS + compass | Holybro M10 | u-blox M10 or M9, with a magnetometer, UART | $55 | [S] |
| 7 | Control link TX | RadioMaster Pocket (ELRS 2.4 GHz) | Any ELRS 2.4 GHz transmitter, ≥ 4 channels + 2 switches | $65–120 | [S] |
| 8 | Control link RX ×2 | ELRS 2.4 GHz receiver | CRSF output, diversity optional | $12 ea | [S] |
| 9 | **Telemetry pair** | **SiK v3 900 MHz** (Holybro or a clone) | **900 MHz-class hardware** — see §why | $25–40/pair | [S] |

### Power and the parts you buy in Israel

| # | Item | Reference part | ≈ ₪ | Where | Conf. |
|---|---|---|---|---|---|
| 10 | **Battery ×2** | HRB 6S 5000 mAh 50C, EC5 | **443 ea** | **Sollan, Ra'anana** | **[V]** |
| 11 | Balance charger | ≥ 100 W, 6S, with a storage-charge mode | 350 | Dominator, RCZone | [E] |
| 12 | LiPo safety bag (large) | Fits 155 × 50 × 50 mm | 50 | C-Hobby | [S] |
| 13 | XT60 pairs ×4 | — | 40 | Hackstore, 4Project | [E] |
| 14 | Silicone wire | 12 AWG red/black, 2 m each | 60 | Hackstore | [E] |
| 15 | **Anti-spark XT90-S** (in place of a trunk fuse) | 60 A+, anti-spark | 35 | Hackstore | [E] |
| 16 | Connector set | 3.5 mm bullets or direct-solder, servo leads, JST | 40 | 4Project | [E] |

### Totals

| Path | Import (USD) | Israel (₪) | All-in ≈ ₪ |
|---|---|---|---|
| Cheapest (Matek H743, SiK clone, 1 spare motor, 1 battery) | ≈ $390 | ≈ 1,050 | **≈ 3,200** |
| Recommended (Pixhawk 6C, Holybro SiK, spare motor + spare ESC, 2 batteries) | ≈ $530 | ≈ 1,550 | **≈ 4,300** |

Neither figure includes shipping. Both include 18 % VAT on the import value above $75.

## Why two parts differ from every tutorial

### The motors are 470 KV, not 1700 KV

KV is free-spin revolutions per volt. On 6S (22.2 V) a 1700 KV motor wants ~37,700 rpm. A
10 in propeller makes Hermon's 363 g of hover thrust at about **5,060 rpm** and reaches its
limits near 10,000 — past that, the blade is outside its design envelope and the current is
outside the motor's. **Propeller diameter sets the rpm; rpm, pack voltage and the target hover
throttle set the KV.** Hover should sit at 40–60 % throttle, which puts 10 in on 6S near
470 KV, on a 3110-sized stator big enough to make torque at that speed.
[02.02](../02-motors-escs-props/02.02-kv-torque-curve.md) derives it,
[02.06](../02-motors-escs-props/02.06-prop-motor-matching.md) matches it,
[02.07](../02-motors-escs-props/02.07-static-thrust-test.md) makes you measure it.

If you buy 2207/1700 KV motors because a 5-inch build guide said so, they will not turn 10 in
props, and a 5-inch aircraft cannot hover for 22 minutes.

### The telemetry radio must be reconfigured before you transmit

Israel's licence-exempt sub-GHz window is **917–920 MHz**. A radio sold as "915 MHz" ships
configured for the US 902–928 MHz band; a radio sold as "868 MHz" is built for the European
863–870 MHz band. **Neither default is inside the Israeli window.**

Buy the **900 MHz-class** hardware — the "915 MHz" SKU — and constrain it in the SiK firmware
before the first transmission:

```text
ATS8=917000      # MIN_FREQ in kHz
ATS9=920000      # MAX_FREQ in kHz
ATS10=10         # NUM_CHANNELS — 10 hops inside the 3 MHz window
RTS8=917000      # and the SAME on the REMOTE radio, or they never meet
RTS9=920000
RTS10=10
AT&W             # write
ATZ              # reboot
```

Do not buy the 868 MHz SKU: its radio front end is filtered for 863–870 MHz and will not
perform at 918 MHz. Do not buy a 433 MHz radio at all — 430–440 MHz is the amateur service
here, not a licence-exempt SRD band.
[09.04](../09-telemetry-datalink/09.04-telemetry-917.md) sets it up,
[09.05](../09-telemetry-datalink/09.05-spectrum-and-regulation.md) covers the law.

## What this stage unlocks

[02.07](../02-motors-escs-props/02.07-static-thrust-test.md) ·
[03.04](../03-power-system/03.04-power-distribution.md)–[03.10](../03-power-system/03.10-lipo-in-israel.md) ·
all of module 04 · module 05 · [07.07](../07-control/07.07-filtering-and-methodic-tuning.md) ·
module 08 · module 09 · module 11 · module 12 · module 16 ·
projects [P01](../projects/P01-first-hover.md), [P02](../projects/P02-tuned-cascade.md),
[P04](../projects/P04-datalink-range.md), [P05](../projects/P05-first-mission.md).

## Before you click buy

- [ ] Check the import-VAT threshold today. It was $75 → $150 → $130 → $75 inside twelve months.
- [ ] Confirm the frame's arm length gives ≥ 30 mm of tip clearance for a 10 in prop.
- [ ] Confirm the FC has a free UART for each of: GNSS, ELRS, SiK, and (later) the companion computer.
- [ ] Confirm the ESC's current sensor is supported by ArduPilot's `BATT_MONITOR` options.
- [ ] Order one spare motor and one spare set of props with the first order, not after the first crash.
- [ ] Buy the batteries **locally** and on a day you can collect them. They will not come by post.
