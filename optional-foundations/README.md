# Optional foundations

<!-- 26 lessons that exist to make a main-path lesson readable, and to carry
     the optional CUX specialisation track. -->

Twenty-six lessons in six tracks. **None of them is required**, and every one of them exists
because a specific main-path lesson assumes something it never taught — or, in the case of CUX,
because you asked for an application the main path does not cover.

Twenty of them are **beginner-level**, 45–75 minutes, and need no hardware. Each one ends on a
number the main path already uses, so you arrive at the main lesson recognising its arithmetic
instead of taking it on trust.

**The six are the exception.** [CUX](#cux--airspace-awareness--self-defence-cux) is
**advanced**, 60–90 minutes, and reuses the stage-2 computer, camera and laser rangefinder rather
than adding hardware. It is still `track: foundations`, so it never gates a module and it stays
out of the dependency chain — it is simply read when you want it, not when you need it.

## How to use them

Do not read this section front to back. Use it the way you would use a reference:

1. Start a main-path lesson.
2. If a number or a unit in it is doing work you cannot follow, check its **Optional
   prerequisites** row — it names the foundation that explains it.
3. Read that one, then come back.

`py course.py why <lesson-id>` prints the same answer from the dependency graph.

## The six tracks

| Track | Lessons | What it removes |
|---|---|---|
| [**FA** — Flight & aerodynamics](flight-aerodynamics/README.md) | 4 | "Where does 3.556 N come from?" |
| [**FEL** — Drone electronics & power](drone-electronics-power/README.md) | 5 | "Why is the pack 6S and why 23.6 minutes?" |
| [**FGL** — GNSS & navigation maths](gnss-navigation-math/README.md) | 4 | "What is a latitude a measurement *against*?" |
| [**FRA** — RF & datalink](rf-datalink/README.md) | 4 | "What is a dBm and why 917 MHz?" |
| [**FOP** — Civil operations fundamentals](civil-ops/README.md) | 3 | "What does a professional do that a hobbyist does not?" |
| [**CUX** — Airspace awareness & self-defence](airspace-awareness/README.md) | 6 | "What is actually in my airspace, and what can I honestly do about it?" |

## Where each track lands

Every track ends on a main-path number, deliberately:

| Track | closes on |
|---|---|
| FA | **23.6 minutes** of endurance, from 88.8 Wh ÷ 226 W |
| FEL | **10.2 A** of hover current, and the calibration that makes it trustworthy |
| FGL | 13.02's **4.50 m UERE** and the DOP that multiplies it |
| FRA | 09.01's **135 dB** budget and **917–920 MHz** |
| FOP | 16.05's residual — **one flight in 1,239**, once every 35 years |
| CUX | 14.04's **32 px floor** applied to a 450 mm aircraft: **41.0 m**, and 1.7 % of VLOS |

## CUX — Airspace awareness & self-defence (CUX)

The one track here that is an **application** rather than a prerequisite. It assumes you have
been through modules 12, 14, 15 and 18 — it is built almost entirely out of their machinery,
re-pointed upward — and it covers what happens when there is a second aircraft in the sky:

```text
CUX.01  detect another aircraft      41 m, and 1.7 % of the volume you may look at
CUX.02  hold a track on it           1.28 m with a rangefinder, 12.0 s to a velocity
CUX.03  identify it                  Remote ID — identity, not intent
CUX.04  report it                    45.5 s at p50, 497.5 s at p99, and the record
CUX.05  deconflict against it        § 107.37(a): you yield, and "well clear" is geometry
CUX.06  and when you cannot          12 s of evasion, and the barrier with no evidence
```

**Hermon is the sensor and the evidence throughout.** Nothing in this track attacks anything,
nothing in it takes an action on a detection without identity and a human, and no lesson supplies
parts that would let it. Two of its six lessons exist specifically to say what the aircraft
**cannot** do: CUX.01 quotes 41 m and 514 false alarms an hour, CUX.05 shows the deconfliction
requirement is 32× what the optics can supply, and CUX.06 closes on 13.05's untested
flow-plus-inertial barrier — the course's longest-standing open item, in the place where it stops
being a footnote.

It also costs nothing to skip. **No stage, no part and no ₪ changes**, because everything it uses
is already bought for module 14.

## The shortest useful path

If you read only five of the twenty foundations, read these:

- [FA.03](flight-aerodynamics/FA.03-work-energy-power.md) — where the flight time comes from
- [FEL.03](drone-electronics-power/FEL.03-lipo-deep-dive.md) — what a pack's label does and does not say
- [FGL.04](gnss-navigation-math/FGL.04-satellite-geometry-and-error.md) — why your position error is a shape
- [FRA.02](rf-datalink/FRA.02-link-budget-math.md) — why the link budget lies, and by how much
- [FOP.02](civil-ops/FOP.02-risk-management-bowtie.md) — how to argue that something is safe

Each one is an hour, and each one changes how a whole module reads.
