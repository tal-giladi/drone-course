# Optional foundations

<!-- 20 lessons that exist to make a main-path lesson readable. -->

Twenty lessons in five tracks. **None of them is required**, and every one of them exists
because a specific main-path lesson assumes something it never taught.

They are **beginner-level**, 45–75 minutes, and need no hardware. Each one ends on a number the
main path already uses, so you arrive at the main lesson recognising its arithmetic instead of
taking it on trust.

## How to use them

Do not read this section front to back. Use it the way you would use a reference:

1. Start a main-path lesson.
2. If a number or a unit in it is doing work you cannot follow, check its **Optional
   prerequisites** row — it names the foundation that explains it.
3. Read that one, then come back.

`py course.py why <lesson-id>` prints the same answer from the dependency graph.

## The five tracks

| Track | Lessons | What it removes |
|---|---|---|
| [**FA** — Flight & aerodynamics](flight-aerodynamics/README.md) | 4 | "Where does 3.556 N come from?" |
| [**FEL** — Drone electronics & power](drone-electronics-power/README.md) | 5 | "Why is the pack 6S and why 23.6 minutes?" |
| [**FGL** — GNSS & navigation maths](gnss-navigation-math/README.md) | 4 | "What is a latitude a measurement *against*?" |
| [**FRA** — RF & datalink](rf-datalink/README.md) | 4 | "What is a dBm and why 917 MHz?" |
| [**FOP** — Civil operations fundamentals](civil-ops/README.md) | 3 | "What does a professional do that a hobbyist does not?" |

## Where each track lands

Every track ends on a main-path number, deliberately:

| Track | closes on |
|---|---|
| FA | **23.6 minutes** of endurance, from 88.8 Wh ÷ 226 W |
| FEL | **10.2 A** of hover current, and the calibration that makes it trustworthy |
| FGL | 13.02's **4.50 m UERE** and the DOP that multiplies it |
| FRA | 09.01's **135 dB** budget and **917–920 MHz** |
| FOP | 16.05's residual — **one flight in 1,239**, once every 35 years |

## The shortest useful path

If you read only five of the twenty, read these:

- [FA.03](flight-aerodynamics/FA.03-work-energy-power.md) — where the flight time comes from
- [FEL.03](drone-electronics-power/FEL.03-lipo-deep-dive.md) — what a pack's label does and does not say
- [FGL.04](gnss-navigation-math/FGL.04-satellite-geometry-and-error.md) — why your position error is a shape
- [FRA.02](rf-datalink/FRA.02-link-budget-math.md) — why the link budget lies, and by how much
- [FOP.02](civil-ops/FOP.02-risk-management-bowtie.md) — how to argue that something is safe

Each one is an hour, and each one changes how a whole module reads.
