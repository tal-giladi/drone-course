# Glossary

Terms as this course uses them, with the lesson that defines each one and — where there is one —
**Hermon's number**.

Definitions here are deliberately short. The lesson is the definition; this is the index.

## Notation used throughout

| Marker | Means |
|---|---|
| **[V]** | verified — computed, measured, or checked against a primary source |
| **[S]** | from a search snippet or a secondary source; check before relying on it |
| **[E]** | an estimate, stated so you can argue with it |
| **Version-sensitive** | this will age; the lesson says what to re-check |

---

## A

**AAR** — after-action review. Four questions in order: planned, happened, why, one change.
[FOP.03](../optional-foundations/civil-ops/FOP.03-debrief-and-aar.md)

**Ampacity** — the current at which a wire reaches a chosen temperature rise. **14 AWG = 29.4 A** at
40 K. On a drone it decides the gauge, not voltage drop.
[FEL.05](../optional-foundations/drone-electronics-power/FEL.05-wiring-fuses-and-measurement.md)

**Attitude** — roll, pitch and yaw relative to a ground frame. Readable by eye out to **242 m**.
[19.02](../19-capstone-hermon-mission/19.02-phase-1-preflight-and-launch.md)

## B

**Barrier** — something that stops a threat reaching a hazard (preventive) or stops a hazard
reaching a consequence (recovery). **Without evidence it is a belief.**
[FOP.02](../optional-foundations/civil-ops/FOP.02-risk-management-bowtie.md)

**β (beta factor)** — the fraction of failures that defeat every barrier at once. At **β = 0.3**, six
barriers are only 3.3× better than one. FOP.02

**Bowtie** — hazard in the middle, threats left, consequences right, barriers on both sides.
Hermon's residual: **8.1e−4 per flight**.
[16.05](../16-testing-analysis/16.05-field-protocols-and-the-safety-case.md)

## C

**CEP** — circular error probable; the radius containing half the fixes. **0.75 × drms.** Not the
same as R95 or 2drms, which are 1.73× and 2×.
[FGL.04](../optional-foundations/gnss-navigation-math/FGL.04-satellite-geometry-and-error.md)

**CRSF** — the ExpressLRS control protocol. Worst-case stick age **7.29 ms** at 150 Hz.
[FRA.04](../optional-foundations/rf-datalink/FRA.04-protocols-and-bands.md)

## D

**Datum** — an ellipsoid pinned to the Earth. The wrong one is **245 m** of perfectly repeatable
error. [FGL.01](../optional-foundations/gnss-navigation-math/FGL.01-earth-coordinates-and-datums.md)

**dB / dBm / dBi** — a ratio, a power referenced to 1 mW, and a gain referenced to an isotropic
radiator. **dB + dBm = dBm; dBm + dBm is nonsense.**
[FRA.01](../optional-foundations/rf-datalink/FRA.01-rf-in-45-minutes.md)

**DOP** — dilution of precision. `(GᵀG)⁻¹` read off the diagonal; dimensionless, and containing no
measurement. **Position error = DOP × UERE.** FGL.04

**drms** — `HDOP × UERE`; the 1σ radial position error. FGL.04

## E

**EIRP** — `Ptx + Gtx − losses`. **What the regulator measures**, so a 9 dBi antenna on a legal
100 mW radio is 631 mW. FRA.01

**EKF origin** — set once at the first good fix and never moved. **Not the same as home**, and RTL
flies to home. [FGL.02](../optional-foundations/gnss-navigation-math/FGL.02-local-frames-enu.md)

**Ellipsoidal height** — height above the WGS84 ellipsoid; what a receiver computes. Differs from
orthometric height by **N ≈ 17 m** here. FGL.01

**ENU / NED** — east-north-up and north-east-down. The matrix between them has **determinant +1**: a
genuine 180° rotation, and the missing sign is **60 m in the wrong direction**. FGL.02

## F

**Fresnel zone** — the ellipsoid a radio link actually travels through. Needs **60 % clear**; at a
2 km span at 917 MHz that is **7.7 m**, measured at the **midpoint**.
[FRA.02](../optional-foundations/rf-datalink/FRA.02-link-budget-math.md)

**FSPL** — free-space path loss, `(4πd/λ)²`. **The frequency term is the receiving antenna, not the
propagation** — 8.5 dB between 917 and 2440 MHz, constant at every distance. FRA.02

## G

**Geoid** — the surface water would settle on; mean sea level. Separation **N ≈ 17 m** in northern
Israel. It cancels in relative altitude and does **not** cancel between two databases. FGL.01

**GSD** — ground sample distance. Images go as **1/GSD²**: 55 at 4 cm, 2,291 at 0.5 cm.
[18.01](../18-civil-ops/18.01-uav-missions.md)

## H

**HDOP** — √(Qee + Qnn). 8 satellites, well spread: **≈ 1.06**. [13.02](../13-navigation-gnss/13.02-error-sources.md)

**Hermon** — this course's aircraft. **1.450 kg**, 45 cm, 6S 5000 mAh, 10 in props, T_hover
**3.556 N** per motor, **226 W** hover, **88.8 Wh** usable, **23.6 min**.
[`hermon-numbers.md`](hermon-numbers.md)

## K

**KV** — motor rpm per volt of back-EMF. **470 KV** on 6S. KV and cell count are **one decision**:
470 KV on 3S cannot hover.
[FEL.04](../optional-foundations/drone-electronics-power/FEL.04-bldc-from-zero.md)

## L

**LAANC** — automated airspace authorisation. **2 minutes** versus 30 days for a manual one.
[18.04](../18-civil-ops/18.04-airspace-in-operations.md)

## M

**MAVLink** — a **message bus**, not a control protocol. Never fly an aircraft on MAVLink sticks.
FRA.04

**Multipath** — a reflected signal arriving late. **A bias, not a noise**: it never averages out.
13.02

## N

**Noise floor** — `−174 dBm + 10 log₁₀(BW)`. A physical constant; **bandwidth is the only lever you
own**. FRA.01

**Null** — the direction an antenna does not radiate. A dipole's is **off the tip**, 15.2 dB down at
10° off axis, and on a drone it points **straight up and down**.
[FRA.03](../optional-foundations/rf-datalink/FRA.03-antennas-and-polarisation.md)

## O

**Objective** — a **state** the world will be in, testable by someone who was not there. Only about
**42 %** of a realistic plan's lines qualify.
[FOP.01](../optional-foundations/civil-ops/FOP.01-mission-planning-process.md)

**Orthometric height** — height above the geoid; what maps and DEMs mean by "altitude". FGL.01

## P

**Part 107** — the FAA small-UAS certificate this course teaches. 55 lb limit; Hermon is **6.8 %** of
it. [18.05](../18-civil-ops/18.05-part-107-and-the-legal-path.md)

**Polarisation** — the plane a field oscillates in. Coupling goes as `cos²`: **1.2 dB at 30° of
bank**, ~25 dB crossed. Circular costs a fixed 3 dB and removes that 25. FRA.03

## R

**Remote ID** — a broadcast identifying the aircraft **and where the operator is standing**. The only
link whose failure is legal rather than technical. 18.04, FRA.04

**RTK** — carrier-phase corrections giving centimetres — **from a datum**. A ₪50 printed sheet and a
₪2,000 RTK receiver bought the same 100 % in
[19.04](../19-capstone-hermon-mission/19.04-phase-3-delivery-and-precision-rtl.md).

## S

**SBUS** — an inverted 100 kbaud control protocol. Worst-case stick age **17.01 ms**, inside which
the 400 Hz rate loop runs **seven times**. FRA.04

**Shunt** — a small precise resistor whose voltage drop is the current. 0.5 mΩ gives **5.09 mV at
hover** and wastes 0.02 % of the power. FEL.05

**SWR** — standing wave ratio. **SWR 3 costs only 1.25 dB** of signal; it matters because the
reflected power goes back into the amplifier. FRA.03

## U

**UERE** — user equivalent range error: the six-source budget, root-sum-squared to **4.50 m**. The
ionosphere is **79 % of the variance**. 13.02, FGL.04

**UTM** — a projection with `k₀ = 0.9996` **by design**. A UTM metre is not a metre: 97 cm over a
2.4 km baseline and **0.08 % of every area, as a bias**.
[FGL.03](../optional-foundations/gnss-navigation-math/FGL.03-geodesy-distance-and-bearing.md)

## V

**VDOP** — √(Quu). Always worse than HDOP — **1.30×** in a good sky — because every satellite is
above you. FGL.04

**VLOS** — visual line of sight. Hermon is a **dot at 2,420 m** and its attitude is unreadable past
**242 m**; the second number is the operational one. 19.02

## W

**Watchdog** — the thing that decides nobody is driving. A crashed process is easy to see; **a
process that is alive and silent is the real failure mode**.
[15.05](../15-onboard-autonomy/15.05-behaviour-trees-and-watchdogs.md)

**WGS84** — the global datum: `a` = 6,378,137 m, 1/f = 298.257223563. Geocentric, which is what
satellites made possible. FGL.01

---

## The Israeli specifics, in one place

| | |
|---|---|
| licence-exempt sub-GHz band | **917–920 MHz** only — 8.7× narrower than the US 902–928 |
| personal-import VAT exemption | **$75** |
| VAT | **18 %** |
| exchange rate used throughout | **1 USD = ₪3.033** |
| magnetic declination **[S]** | ≈ **4.5°**, worth 190 m over a VLOS leg |
| geoid separation **[S]** | ≈ **+17 m** |
