# Stage 3 — precision positioning (optional)

**No lesson in this course requires this stage.**
[13.03](../13-navigation-gnss/13.03-rtk-and-ppk.md) teaches carrier-phase positioning, integer
ambiguity resolution and the PPK workflow without any of it. Buy this only if you have a
reason — a survey client who needs centimetre ground control, or an interest in the topic.

## When it is actually worth it

| Your situation | Verdict |
|---|---|
| Learning the theory | Skip. 13.03 uses public RINEX data and a simulator |
| Precision landing on a pad | Skip — that is Stage 5's IR beacon, which is both cheaper and more reliable indoors and at night |
| Photogrammetry for a paying client | Buy, or subscribe to NTRIP |
| Mapping without ground control points | Buy — this is the case that pays for itself |

## The list

| # | Item | Reference part | ≈ price | Conf. |
|---|---|---|---|---|
| 1 | RTK rover (on the aircraft) | Holybro H-RTK F9P Helical, or an ArduSimple simpleRTK2B | $250–400 | [S] |
| 2 | RTK base | A second F9P board + a survey tripod and a ground plane | $250–350 | [S] |
| 2b | — or, instead of a base | An **NTRIP subscription** to a commercial Israeli CORS network | subscription | [E] |
| 3 | Correction link | The existing telemetry radio, or a phone hotspot to the ground station | — | — |

**≈ ₪2,000** for a base-and-rover pair at 2026 prices, converted and with VAT. **[E]**

## The Israeli specifics

- **The correction link is the hard part, not the receiver.** RTK needs a continuous stream of
  corrections from a base within a few tens of kilometres. If you run your own base, the
  corrections go over Hermon's telemetry link and compete with MAVLink for the 917–920 MHz
  window's bandwidth — which is narrow. The realistic setup is corrections over a phone
  hotspot to the ground station, then up the telemetry link.
- **NTRIP over a CORS network** is the lower-effort path. Israel has commercial and academic
  CORS coverage; confirm the provider, the cost and the mount points before buying a base.
  This is an open item in
  [the research file](../references/research/israel-drone-hardware-2026-09.md#6-open-items-for-the-next-research-pass).
- **A rover with no corrections is just an expensive GNSS receiver.** A dual-frequency F9P
  in standalone mode is better than an M10, but not by enough to justify the price. Budget
  for the corrections or do not buy the rover.

## What it unlocks

[13.03](../13-navigation-gnss/13.03-rtk-and-ppk.md) only — and it makes that lesson's
practical exercise real rather than simulated.
