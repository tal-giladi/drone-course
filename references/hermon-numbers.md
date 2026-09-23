# Hermon: the frozen numbers

Every lesson in this course quotes Hermon's numbers. They are defined **here, once**. If a
lesson needs a number about the aircraft, it comes from this page or is derived in the lesson
from numbers on this page — it is never invented.

If you change a number here, run `py tools/validate.py` and grep the course for the old value.

- **Frozen:** 2026-09-22
- **Revision 2 (2026-09-22):** the all-up mass was corrected from 1.20 kg to **1.45 kg**. See
  §8 — 1.20 kg was not achievable with a 450 mm frame, four 3110-class motors and a 720 g 6S
  pack, and every number downstream of mass moved with it.
- **Design authority:** modules 01–04 derive these; module 02.07 and 11.05 *measure* them.

---

## 1. The airframe

| Quantity | Value | Where it comes from |
|---|---|---|
| **Dry mass** (everything except the pack) | **730 g** | The mass budget in [04.02](../04-frame-and-assembly/04.02-mass-and-center-of-mass.md) |
| **All-up mass, clean** | **1.45 kg** | 730 g dry + 720 g pack |
| All-up mass, with delivery pod | **1.70 kg** | 1.45 kg + 250 g pod (module 17) |
| Maximum takeoff mass | **2.0 kg** | Thrust margin limit; also keeps Hermon under the 2 kg line that several rule sets use |
| Wheelbase (motor-to-motor diagonal) | **450 mm** | 450-class frame; fits 10 in props with 32 mm tip clearance between adjacent discs |
| Configuration | Quadcopter, X | Decision 4 in [ARCHITECTURE.md](../ARCHITECTURE.md) |
| Arm length (centre to motor shaft) | 225 mm | 450 / 2 |

**Prop clearance check.** Adjacent motors on a 450 mm X quad sit 450/√2 = 318 mm apart. Two
10 in (254 mm) discs side by side need 254 mm. Clearance = 318 − 254 = **64 mm**, i.e. 32 mm
per side. A 12 in (305 mm) prop would leave 13 mm — too little. **10 in is the frame's limit;
that is why Hermon is a 10 in aircraft.**

## 2. The powertrain

| Quantity | Value | Where it comes from |
|---|---|---|
| Propeller | **10 × 4.5 × 3** (254 mm, 3-blade) | [02.05](../02-motors-escs-props/02.05-propellers.md), [02.06](../02-motors-escs-props/02.06-prop-motor-matching.md) |
| Motor | **3110-class, 470 KV, 6S-rated** | [02.11](../02-motors-escs-props/02.11-hermon-powertrain-design.md). Reference part: T-Motor MN3110 KV470 |
| Motor mass | 80 g bare, ~88 g with leads | Manufacturer data |
| Motor continuous current | ≥ 15 A | Reference part: 15 A for 180 s. Full throttle draws 14.1 A — **full throttle is a burst condition, not a cruise** |
| Required static thrust per motor | **≥ 1,100 g at 10 × 4.5, 6S, full throttle** | Predicted 1,369 g in [02.06](../02-motors-escs-props/02.06-prop-motor-matching.md); **measured** in [02.07](../02-motors-escs-props/02.07-static-thrust-test.md) |
| Hover thrust per motor, clean | **3.56 N (363 g)** | 1.45 kg × 9.81 / 4 |
| Hover thrust per motor, with pod | **4.17 N (425 g)** | 1.70 kg × 9.81 / 4 |
| Hover rpm | **≈ 5,060 rpm** (84.4 rev/s) | $n=\sqrt{T/(C_T\rho D^4)}$ with the **measured** $C_T = 0.098$ from [02.07](../02-motors-escs-props/02.07-static-thrust-test.md). [02.06](../02-motors-escs-props/02.06-prop-motor-matching.md) predicts 5,141 rpm from its *assumed* $C_T = 0.095$ — a 1.5 % design margin, which is the point of measuring |
| Hover throttle | **≈ 48 %** | The 40–60 % band that [02.06](../02-motors-escs-props/02.06-prop-motor-matching.md) targets |
| Blade-pass frequency at hover | **253 Hz** | 84.4 rev/s × 3 blades — the harmonic notch centre in [07.07](../07-control/07.07-filtering-and-methodic-tuning.md) |
| Thrust-to-weight, clean | **≈ 3.78 : 1** | 4 × 1,369 g / 1,450 g |
| Thrust-to-weight, with pod | **≈ 3.22 : 1** | 4 × 1,369 g / 1,700 g |
| Measured coefficients | $C_T = 0.098$, $C_P = 0.050$, **FM 0.49** | [02.07](../02-motors-escs-props/02.07-static-thrust-test.md). $FM = C_T^{3/2}\sqrt{2/\pi}/C_P$ in the propeller convention |
| ESC | **4-in-1, ≥ 45 A, 4–6S, DShot600** | [02.03](../02-motors-escs-props/02.03-esc-basics.md), [02.04](../02-motors-escs-props/02.04-esc-firmware.md). Reference part: Holybro Tekko32 F4 Metal **65 A** — headroom, because ESC ratings are optimistic |

> [!IMPORTANT]
> **Why 470 KV and not the 1700 KV you see on every 5 in build.**
> KV is revolutions per volt with no load. On 6S (22.2 V) a 1700 KV motor free-spins at
> ~37,700 rpm. A 10 in propeller makes Hermon's 363 g of hover thrust at about **5,060 rpm**
> and reaches its limits near 10,000; at 37,700 rpm the blade would be destroyed and the motor
> would draw a current no 5 in motor can survive. **Prop diameter sets rpm; rpm, pack voltage
> and the target hover throttle set KV.** Hover should land at 40–60 % throttle, so
> $KV \approx 5060 / (22.2 \times 0.485) \approx 470$.
> [02.02](../02-motors-escs-props/02.02-kv-torque-curve.md) derives it;
> [02.06](../02-motors-escs-props/02.06-prop-motor-matching.md) solves the equilibrium.

## 3. Power and energy

| Quantity | Value | Where it comes from |
|---|---|---|
| Pack | **6S1P, 5000 mAh LiPo**, 50 C | [03.02](../03-power-system/03.02-pack-configuration.md) |
| Nominal pack voltage | **22.2 V** | 6 × 3.7 V |
| Full / storage / empty (per cell) | 4.20 V / 3.80 V / 3.30 V | [03.01](../03-power-system/03.01-lipo-chemistry.md) |
| Pack energy, nameplate | **111 Wh** | 22.2 V × 5.0 Ah |
| Usable energy at 80 % DoD | **88.8 Wh** | The reserve policy in [03.09](../03-power-system/03.09-endurance-prediction.md) |
| Pack mass | **720 g** | Measured on the real pack; it is the single heaviest item, 50 % of the aircraft |
| Pack internal resistance | ~0.040 Ω (6.7 mΩ per cell) | [03.03](../03-power-system/03.03-c-rating-voltage-sag.md) |
| **Hover power, clean (the design budget)** | **226 W** | [03.05](../03-power-system/03.05-power-budget.md), [03.09](../03-power-system/03.09-endurance-prediction.md) |
| Propulsion line at hover | **216 W** (54 W per motor) | 226 − 10 |
| **Hover current at 22.2 V** | **10.2 A** (2.0 C) | 226 W / 22.2 V |
| Hover efficiency | **6.4 g/W** | 1,450 g / 226 W |
| Avionics load (FC, GNSS, radios) | ~10 W | [03.05](../03-power-system/03.05-power-budget.md) |
| Burst current (punch-out) | **40 A** | [03.03](../03-power-system/03.03-c-rating-voltage-sag.md) |
| Full-throttle pack current | **57 A** (14.1 A per motor) | [02.06](../02-motors-escs-props/02.06-prop-motor-matching.md) |
| Installed-power factor $k_{install}$ | **1.12** | [03.09](../03-power-system/03.09-endurance-prediction.md) — airframe download + interference |
| Hover endurance at 80 % DoD | **23.6 min** | 88.8 Wh / 226 W |
| **Published endurance spec** | **22 min** | 23.6 min with a margin for wind and pack ageing |
| Failsafe thresholds (per cell) | warn 3.60 V · low 3.50 V → RTL · min 3.30 V → land | [03.06](../03-power-system/03.06-battery-monitoring.md) |

> The 226 W figure is a **budget**, not a best case. Momentum theory for 363 g on a 10 in disc
> gives 19.0 W of induced power per motor; the propeller's figure of merit (0.49) takes that to
> 38.8 W of shaft power, the electrical chain to 48.2 W, and $k_{install} = 1.12$ to 54.0 W per
> motor. [01.06](../01-flight-physics/01.06-momentum-theory.md) does the ideal calculation,
> [11.05](../11-first-flights/11.05-battery-discipline.md) measures the real one, and you are
> expected to land inside ±15 % of the budget.

## 3a. Performance

From the forward-flight model in
[03.09](../03-power-system/03.09-endurance-prediction.md), at 1.45 kg, ISA, 88.8 Wh usable.

| Condition | Speed | Power | Current | Endurance | Range |
|---|---|---|---|---|---|
| Hover | 0 | **226 W** | 10.2 A | **23.6 min** | — |
| Best endurance | **8.6 m/s** | 200 W | 9.0 A | **26.6 min** | 13.7 km |
| **Cruise (spec)** | **10 m/s** | **202 W** | 9.1 A | **26.4 min** | **15.8 km** |
| Best range | **16.8 m/s** | 265 W | 11.9 A | 20.2 min | **20.4 km** |
| Hover, with pod | 0 | 284 W | 12.8 A | 18.7 min | — |
| Hover, stage 2 (+Pi) | 0 | 281 W | 12.6 A | 19.0 min | — |

**Round-trip radius at 10 m/s airspeed**, before the ×0.8 planning factor:

| Headwind | 0 | 3 m/s | 6 m/s | 9 m/s |
|---|---|---|---|---|
| Radius | **7.9 km** | 7.2 km | **5.1 km** | 1.5 km |

**The mass exchange rate:** 1 g costs **0.223 W** of hover power; 100 g costs **2.2 minutes**
(9.3 %) of endurance. A payload drawing less than **0.22 W per gram** costs more in mass than in
watts.

## 4. Avionics

| Item | Spec | Notes |
|---|---|---|
| Flight controller | STM32H743-class, ≥ 5 UARTs, dual IMU, baro, SD | Reference parts: Holybro Pixhawk 6C, Matek H743-SLIM |
| GNSS | u-blox M10, with compass | [05.04](../05-sensors/05.04-gnss-receiver.md) |
| Control link | ExpressLRS **2.4 GHz** | Legal in Israel under the 2400–2483.5 MHz exemption |
| Telemetry link | SiK v3 900 MHz radio, **constrained to 917–920 MHz** | See §6. This is not the radio's default |
| Companion computer (stage 2) | Raspberry Pi 5, 8 GB | Same board as the robotics course. +130 g, +25 W |
| Main pack connector | **EC5** | What Israeli-stock packs ship with; see [03.10](../03-power-system/03.10-lipo-in-israel.md) |

## 5. Flight envelope

| Limit | Value | Set by |
|---|---|---|
| Maximum wind for a training flight | 6 m/s | [11.04](../11-first-flights/11.04-flying-in-wind.md) |
| Maximum wind for a capstone mission | 6 m/s | [19.01](../19-capstone-hermon-mission/19.01-the-brief.md) |
| Cruise speed (mission) | 10 m/s | [12.02](../12-autonomous-flight/12.02-mission-planning.md) |
| Planning radius at the wind limit | **4.1 km** (5.1 × 0.8) | [03.09](../03-power-system/03.09-endurance-prediction.md) |
| Survey altitude | 40 m AGL | [19.01](../19-capstone-hermon-mission/19.01-the-brief.md) |
| Minimum GNSS to arm in an auto mode | 3-D fix, ≥ 10 satellites, HDOP ≤ 1.2 | [05.04](../05-sensors/05.04-gnss-receiver.md) |
| Landing accuracy, precision landing | ≤ 0.3 m mean offset | [12.05](../12-autonomous-flight/12.05-auto-takeoff-land-precision.md) |

## 6. Radio bands — the Israeli constraint

This is the one place where Hermon's parts list differs from every tutorial you will read
online, and it is a legal difference, not a preference.

| Link | Band Hermon uses | Why |
|---|---|---|
| Control (ExpressLRS) | 2400–2483.5 MHz | Licence-exempt in Israel; the ExpressLRS 2.4 GHz hardware is the same everywhere |
| Telemetry (SiK / MAVLink) | **917–920 MHz only** | Israel's Ministry of Communications opened **917–920 MHz** for licence-exempt sub-GHz use. A US "915 MHz" radio ships configured for 902–928 MHz and a European "868 MHz" radio for 863–870 MHz — **neither default is inside the Israeli window.** You buy the 900 MHz-class radio and constrain its hopping range in the SiK firmware |
| Video (if fitted) | 5725–5875 MHz, permit-based | Check before you transmit; the course does not require an FPV video link |

The SiK parameters that do it (taught in
[09.04](../09-telemetry-datalink/09.04-telemetry-917.md)):

```text
ATS8=917000      # MIN_FREQ, kHz
ATS9=920000      # MAX_FREQ, kHz
ATS10=10         # NUM_CHANNELS — 10 × 300 kHz hops inside the 3 MHz window
RTS8=917000      # and the SAME on the REMOTE radio
RTS9=920000
RTS10=10
```

Sources and the rest of the spectrum story:
[`references/research/israel-drone-hardware-2026-09.md`](research/israel-drone-hardware-2026-09.md).

## 7. What is measured, not assumed

Three of the numbers above are **predictions that the course makes you verify**. Write your
measured value next to the predicted one; a gap is a finding, not a failure.

| Number | Predicted | You measure it in | Acceptance |
|---|---|---|---|
| Static thrust per motor | 1,369 g at full throttle | [02.07](../02-motors-escs-props/02.07-static-thrust-test.md) on your own rig | Within 15 % of the prediction |
| **All-up mass** | **1.45 kg** | [04.02](../04-frame-and-assembly/04.02-mass-and-center-of-mass.md) on a scale | Within 100 g, or re-derive §3 |
| Hover power | 226 W | [11.05](../11-first-flights/11.05-battery-discipline.md) from a real hover | Within 15 % of the budget |
| Hover endurance | 22 min | [11.05](../11-first-flights/11.05-battery-discipline.md) | ≥ 18 min to 80 % DoD, or the budget is wrong |

## 8. Revision 2 — why the mass changed

**Revision 1 froze the all-up mass at 1.20 kg. It is not achievable.** Writing the mass budget
for module 04 forced the itemisation, and the arithmetic does not close:

| Item | Mass |
|---|---|
| 4 × 3110-class motor with leads | 352 g |
| 6S 5000 mAh pack | 720 g |
| **Those two alone** | **1,072 g** |
| 450 mm carbon frame | 180–210 g |
| 4 × 10 × 4.5 × 3 propeller | 48–56 g |
| ESC, FC, GNSS, two radios, wiring, hardware | 160–200 g |
| **Realistic total** | **1.45–1.60 kg** |

1.20 kg would have left **480 g** for everything except the pack, and the motors alone are 352 g
of that. **1.45 kg is the target for a carefully built, light-part-selection aircraft**; a first
build typically lands at 1.50–1.60 kg, which costs about a minute of endurance per 50 g.

**What moved, and what did not:**

| Moved | Did not move |
|---|---|
| Hover thrust 2.94 → **3.56 N** per motor | **Motor KV: still 470** — hover thrust and hover throttle moved together |
| Hover rpm 4,700 → **5,060** | Propeller: 10 × 4.5 × 3 |
| Hover throttle 46 → **48 %** | Pack: 6S 5000, 111 Wh, 88.8 Wh usable, 720 g, 0.040 Ω |
| Blade-pass 234 → **253 Hz** | Full throttle: 9,836 rpm, 1,369 g, 57 A |
| Thrust-to-weight 4.56 → **3.78 : 1** | Failsafes: 3.60 / 3.50 / 3.30 V |
| Hover power 194 → **226 W** | Wheelbase 450 mm, X quad |
| Hover current 8.7 → **10.2 A** | Radio bands |
| Endurance 27.4 → **23.6 min**, published 25 → **22 min** | MTOM 2.0 kg |
| Figure of merit 0.43 → **0.49** (a *separate* correction: the propeller-convention formula is $C_T^{3/2}\sqrt{2/\pi}/C_P$, not $C_T^{3/2}/(C_P\sqrt2)$) | $C_T = 0.098$, $C_P = 0.050$ |

**That the KV survived unchanged is the reassuring part**: it says the powertrain choice was
driven by the propeller and the pack voltage, which did not move, rather than by a mass estimate,
which did.
