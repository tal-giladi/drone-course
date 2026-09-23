# Troubleshooting index

Symptoms, sorted by what you observed rather than by what is wrong. Each row names the lesson that
has the full diagnosis.

Every lesson in this course has its own **Troubleshooting** section; this page is the way in when you
do not yet know which lesson to open.

## The ordering rule

Before using this page, apply the rule from
[16.03](../../16-testing-analysis/16.03-reading-flight-logs.md): **open the log in a fixed order**,
because the first thing you look at determines what you suspect. Mode changes, then errors, then the
subsystem you think is at fault — in that order, every time.

And note the sizes from [FGL.01](../../optional-foundations/gnss-navigation-math/FGL.01-earth-coordinates-and-datums.md)
and [FGL.02](../../optional-foundations/gnss-navigation-math/FGL.02-local-frames-enu.md): **an error's
magnitude usually names its cause.**

| the error is about | the cause is almost always |
|---|---|
| **~20 km** | geodetic versus geocentric latitude |
| **~250 m** | the wrong datum |
| **~60 m, exactly twice your command** | a sign, ENU versus NED |
| **~17 m, in altitude only** | the geoid — a DEM mixed with a receiver |
| **~15 %, east-west only** | a missing `cos(latitude)` |

## It will not arm

| symptom | where |
|---|---|
| pre-arm check fails, message unclear | [11.01](../../11-first-flights/11.01-first-flight.md) |
| compass inconsistent | [05.03](../../05-sensors/05.03-compass-and-baro.md) |
| EKF not happy / position unavailable | [06.06](../../06-state-estimation/06.06-ekf-health-and-logs.md) |
| GNSS fix but poor HDOP | [13.02](../../13-navigation-gnss/13.02-error-sources.md) |
| battery failsafe at full charge | [03.06](../../03-power-system/03.06-battery-monitoring.md) |

## It flies badly

| symptom | where |
|---|---|
| leans hard on lift-off | [P01](../../projects/P01-first-hover.md) — motor order or direction |
| fast, high-pitched oscillation | [07.07](../../07-control/07.07-filtering-and-methodic-tuning.md) — D fighting noise |
| slow oscillation that builds | [07.03](../../07-control/07.03-rate-loops.md) — P too high |
| motors hot after a short flight | [02.09](../../02-motors-escs-props/02.09-heat-vibration-noise.md), and 07.07 |
| roll fine, pitch not | [P02](../../projects/P02-tuned-cascade.md) — different inertia, separate loops |
| drifts consistently one way | [11.04](../../11-first-flights/11.04-flying-in-wind.md) or [05.06](../../05-sensors/05.06-noise-bias-and-calibration.md) |
| altitude wanders | [05.03](../../05-sensors/05.03-compass-and-baro.md), then 06.06 |
| worse after a battery change | [FEL.03](../../optional-foundations/drone-electronics-power/FEL.03-lipo-deep-dive.md) — sag changes the system gain |

## Power and endurance

| symptom | where |
|---|---|
| flight time far below prediction | [03.09](../../03-power-system/03.09-endurance-prediction.md) |
| hover current rises through the flight | [FEL.01](../../optional-foundations/drone-electronics-power/FEL.01-electricity-refresher.md) — expected: 8.97 → 10.76 A |
| logged mAh disagrees with the charger | [FEL.05](../../optional-foundations/drone-electronics-power/FEL.05-wiring-fuses-and-measurement.md) — calibrate against the charger |
| a connector runs hot | FEL.05 — watts per m², and replace it |
| one cell always lowest | FEL.03 — and at 0.60 V of drift the alarm stops protecting it |
| pack puffed | [03.08](../../03-power-system/03.08-battery-safety.md) — stop using it |

## Radio and telemetry

| symptom | where |
|---|---|
| telemetry stutters on the pad, fine at range | [FRA.03](../../optional-foundations/rf-datalink/FRA.03-antennas-and-polarisation.md) — **the overhead null** |
| range far below the budget | [FRA.02](../../optional-foundations/rf-datalink/FRA.02-link-budget-math.md) — Fresnel, then the two-ray floor |
| link drops at short range, fine far away | FRA.02 — ground-reflection nulls below the breakpoint |
| poor in one direction only | FRA.03 — something conductive is shadowing the antenna |
| failsafe fires with strong RSSI | [09.03](../../09-telemetry-datalink/09.03-failsafe-when-the-link-drops.md) — read link quality, not signal strength |
| SWR perfect, range terrible | FRA.03 — a dummy load reads 1.0 |
| imported radio will not work here | [09.05](../../09-telemetry-datalink/09.05-spectrum-and-regulation.md) — it shipped on 902–928; Israel is 917–920 |

## Navigation

| symptom | where |
|---|---|
| position jumps near a building | 13.02 — multipath, which is a **bias** |
| altitude worse than horizontal | [FGL.04](../../optional-foundations/gnss-navigation-math/FGL.04-satellite-geometry-and-error.md) — VDOP, and unfixable |
| raising the elevation mask made it worse | FGL.04 — a mask only ever costs geometry |
| the fence triggers at the wrong radius | FGL.02 — the EKF origin is not home |
| RTL goes somewhere unexpected | [12.04](../../12-autonomous-flight/12.04-rtl-and-the-failsafe-tree.md) — RTL flies to **home** |
| heading off by a few degrees | [FGL.03](../../optional-foundations/gnss-navigation-math/FGL.03-geodesy-distance-and-bearing.md) — declination, 190 m over a VLOS leg |

## Autonomy and software

| symptom | where |
|---|---|
| mission flies an unexpected first leg | [P05](../../projects/P05-first-mission.md) — the missing takeoff command |
| waypoint overshoot | [07.05](../../07-control/07.05-velocity-position-and-modes.md) |
| offboard mode rejected | [15.04](../../15-onboard-autonomy/15.04-offboard-control.md) — setpoints must already be streaming |
| the service starts on the bench, not on boot | [15.06](../../15-onboard-autonomy/15.06-deployment-and-first-autonomous-flight.md) |
| a hung process is not detected | [15.05](../../15-onboard-autonomy/15.05-behaviour-trees-and-watchdogs.md) — watch **data**, not the process |
| SITL hangs instead of exiting | [P03](../../projects/P03-sitl-harness.md) — kill the process group |
| passes in SITL, fails in the air | P03 — that is a model error, and worth writing down |

## Vision

| symptom | where |
|---|---|
| recall collapses with altitude | [18.01](../../18-civil-ops/18.01-uav-missions.md) — GSD, and images go as 1/GSD² |
| detections good, position metres out | [14.05](../../14-vision-perception/14.05-tracking-and-geolocation.md) — attitude timing first |
| averaging fixes does not help | [19.03](../../19-capstone-hermon-mission/19.03-phase-2-survey-and-detect.md) — 0.27 %, because the terms are biases |
| false positives everywhere | [14.04](../../14-vision-perception/14.04-detection-in-the-air.md) — the base rate, not the model |
| latency fine on the bench, bad in flight | [14.06](../../14-vision-perception/14.06-edge-compute-and-latency.md) — thermal throttling |

## When the symptom is not here

Three questions, in order, and they resolve most of what this page does not:

1. **What changed?** A parameter, a battery, a prop, a firmware version, a site.
2. **What size is the error?** Use the table at the top; magnitudes name causes.
3. **What does the log say, in the fixed order?** 16.03. Not the order your suspicion suggests.

And if you find something this page should contain, add it — that is
[FOP.03](../../optional-foundations/civil-ops/FOP.03-debrief-and-aar.md)'s rule: a change is only
real when it modifies an artefact, and this file is one.
