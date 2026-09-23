# Stage 5 — precision landing & the final aircraft

Two separate purchases at two different times:

- **The IR beacon** — buy at [12.05](../12-autonomous-flight/12.05-auto-takeoff-land-precision.md),
  because precision landing is taught there and the capstone depends on it.
- **The spares and the case** — buy before module 19, because a capstone campaign is ten
  flights in a day and a broken prop should not end it.

## The precision-landing set

| # | Item | Reference part | Substitute spec | ≈ price | Conf. |
|---|---|---|---|---|---|
| 1 | IR beacon (on the pad) | IR-LOCK MarkOne beacon | Any modulated-IR beacon the sensor is matched to | $100 | [S] |
| 2 | IR sensor (on the aircraft) | IR-LOCK sensor (Pixy-based) | Must emit ArduPilot's `LANDING_TARGET` MAVLink message | $150 | [S] |
| 2b | — cheaper substitute | The Stage 2 camera + an ArUco marker, processed on the Pi | Software only; you write it in [14.05](../14-vision-perception/14.05-tracking-and-geolocation.md) | ₪0 | [E] |
| 3 | Landing pad | 75 cm folding pad, or a painted plywood square | Contrasting, flat, and heavy enough not to blow away | ₪80 | [E] |

> The **cheap substitute is a real option and a better lesson.** You already have a camera, a
> companion computer and the geolocation maths from module 14. An ArUco marker on a pad plus a
> `LANDING_TARGET` publisher gets you to roughly 0.2–0.4 m in daylight — the same figure the
> IR set achieves, and you understand every line of it. The IR set wins at night, in sun glare,
> and when you want it to work without the Pi booting. Decide in
> [12.05](../12-autonomous-flight/12.05-auto-takeoff-land-precision.md).

## The spares set

Buy these **before** the capstone campaign, not after the first failure.

| # | Item | Quantity | ≈ ₪ | Why |
|---|---|---|---|---|
| 1 | Propellers | 4 sets | 100 | A prop strike is the most common damage and props are consumables |
| 2 | Motor | 1 | 100 | A bent shaft ends a flying day; a spare motor is 15 minutes |
| 3 | ESC (4-in-1) | 1 | 300 | Only if you are running the campaign to a deadline |
| 4 | XT60 pair + 12 AWG wire | 1 m | 40 | Battery leads chafe |
| 5 | Landing gear / arm | 1 set | 60 | The parts that hit the ground first |
| 6 | Flight case or a padded toolbox | 1 | 200–400 | Ten flights means transporting a built aircraft repeatedly |
| 7 | Third battery | 1 | 443 | Ten missions is ~4 hours of flying; two packs means constant waiting |

**Cheapest path ≈ ₪400** (props, one motor, wire, a padded box).
**Recommended ≈ ₪1,100** (all of the above, including the third battery).

## What this stage unlocks

[12.05](../12-autonomous-flight/12.05-auto-takeoff-land-precision.md) ·
[19.04](../19-capstone-hermon-mission/19.04-phase-3-delivery-and-precision-rtl.md) ·
[19.05](../19-capstone-hermon-mission/19.05-the-campaign-and-the-report.md) ·
project [P08](../projects/P08-hermons-mission.md).
