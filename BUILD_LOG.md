# Build log — read this first after a crash

This file is the **single source of truth for where the build stopped**. Every batch updates
it *before* moving on. If a session dies mid-batch, start again at the first batch whose
status is not `done`.

- **Course:** Practical UAV — Hermon (see [README.md](README.md), [ARCHITECTURE.md](ARCHITECTURE.md))
- **Student:** software/AI engineer **living in Israel**, studying for **FAA Part 107**
- **Last updated:** 2026-09-23 — **THE COURSE IS COMPLETE.** 161/161 files, `validate.py --links --final --strict` clean, 1 external URL unreachable (bot-walled).

---

## Standing decisions (2026-09-22, confirmed by Tal)

| # | Decision | Consequence |
|---|---|---|
| D1 | **Parts are sourced in Israel; certification content stays FAA Part 107.** | `HARDWARE.md`, `hardware/*`, all prices in ₪ (+ USD), Israeli shops first, import path second. Module 18 and FOP keep the Part 107 syllabus. |
| D2 | **Anything not legally buyable/usable in Israel is swapped for an equivalent that is.** | **Corrected in batch 2:** Israel's licence-exempt sub-GHz window is **917–920 MHz**, not 868 and not the full US 902–928. Hermon buys the 900 MHz SiK hardware and constrains it in firmware. The batch-1 guess of "use 868" was wrong and has been replaced everywhere. |
| D3 | **Lessons 02.03–03.07 are rewritten**, not kept. | They were generated in a degenerate possessive style ("the 03.06's monitor's the 03.04's power tree's measurement's layer"). Numbers, tables and code are correct and are preserved; only the prose is rewritten in the clean style of modules 00–01. |
| D4 | **The curriculum is trimmed from 259 items to 161** (133 main lessons + 20 foundations + 8 projects). | Nothing on the build/fly critical path is cut. The trim merges theory lessons and shortens the target length to ~350–450 lines per lesson. |
| D5 | **Module 17 is civil payload engineering**, not munitions. | The old plan (bombs, grenades, fuzing, seekers, laser designation, target lead) is replaced by mass/CoM, release mechanisms, spray & irrigation, release dynamics, drop-point ballistics and the Hermon pod build. This matches the course's stated civil/Part 107 goal and the "irrigation payload" in the README. |
| D6 | **Work runs batch by batch across sessions without check-ins.** | Each batch ends with: files written → `py tools/build.py` → `py tools/validate.py` → this log updated. |
| D7 | **Hermon's motor is a 3110-class 470 KV, not a 2207/1700 KV.** | The original spec was physically impossible: a 1700 KV motor free-spins at ~37,700 rpm on 6S and cannot turn a 10 in propeller. Corrected in batch 2 to 700 KV, then **corrected again in batch 3 to 470 KV** once 02.06's motor–propeller equilibrium was actually solved: a 10×4.5×3 makes 300 g at ~4,700 rpm, and hover must land at 40–60 % throttle, so KV ≈ 4700/(22.2 × 0.46) ≈ 470. Derived numbers frozen in `references/hermon-numbers.md` — see the batch-3 journal entry for the full table. Everything else survived untouched: 1.20 kg, 450 mm, 6S 5000 mAh, 10×4.5×3, 194 W, 25 min. |
| D8 | **(batch 2) `references/hermon-numbers.md` is the single source of truth for the aircraft.** | No lesson invents a number about Hermon. It quotes that file or derives its value from it. |

---

## Quality bar for every lesson

Copy the shape of [`01-flight-physics/01.05-drag.md`](01-flight-physics/01.05-drag.md) — that is
the reference lesson. Required sections are enforced by `tools/validate.py`:

`What you will learn` · `Why it matters` · `Prerequisites` · `Concept` · `Technical explanation`
(Levels 1–4) · `Diagram` · `Code` · `Exercise` · `Expected result` · `Troubleshooting` ·
`Common mistakes` · `Knowledge check` · `Practical challenge` · `You can skip this if` ·
`Go deeper` · `Progress checkpoint`

Rules that the broken lessons violated and that must not come back:

1. **Write sentences, not possessive chains.** Never `the 03.04's PDB's ADC's the 6 cells's`.
   A cross-reference is a markdown link — `[03.04](03-power-system/03.04-power-distribution.md)` —
   used once, in a normal sentence.
2. **Every number is either derived in the lesson or cited.** Hermon's numbers are fixed in
   [`references/hermon-numbers.md`](references/hermon-numbers.md); use those, do not invent new ones.
3. **Code runs.** Standard library unless the lesson's `software:` field says otherwise. The
   `Expected result` block must be the *actual* output of the code as written.
4. **Target 350–450 lines.** Dense, not padded. Module 02's rewrites came out at 450–700 lines;
   that is acceptable where the density is real, but do not pad to reach it.
5. **RUN THE CODE.** Use `scratchpad/runcode.py <lesson.md>` (see below). Paste the *real*
   stdout into the `Expected result` block. In batch 3 this caught **four** lessons where the
   hand-written output was wrong, and in two cases the wrong output was hiding a wrong
   *physical model* — not a formatting slip.

### The build-time helper scripts

Four helpers live in `tools/` (copied out of the session scratchpad at the end of batch 3 so
they survive). They are **build tools, not course content** — students never run them.

| Script | Does |
|---|---|
| `tools/runcode.py <lesson.md>` | Extracts the ```python block under `## Code` and runs it. **Use this on every lesson.** |
| `tools/gendata.py` | Generates physically consistent thrust-stand sample data from $C_T$/$C_P$, with no-load current and pack sag |
| `tools/match.py` | The motor–propeller equilibrium solver (the one that found the 470 KV answer) |
| `tools/fixlinks.py [--write]` | Remaps every lesson cross-link onto current ids after a syllabus change. Its `ABSORBED` dict records which trimmed lesson absorbed which |
| `tools/paste.py <lesson.md> ...` | Runs the lesson's code block and **splices the real stdout** into the ```text block after `Output:`. The other half of the runcode loop |
| `tools/paths.py [prefix]` | Prints every lesson id and its path from `graph.json`. **Use it before linking to an unwritten lesson** instead of guessing the slug |

```bash
py tools/runcode.py 02-motors-escs-props/02.06-prop-motor-matching.md
```

---

## Batch plan and status

Legend: ☐ not started · ◐ in progress · ☑ done

| # | Batch | Files | Status | Notes |
|---|---|---|---|---|
| 1 | Re-plan: trimmed `curriculum/syllabus.yaml`, README/ARCHITECTURE reframed for Israel sourcing + Part 107, this log | syllabus.yaml, README.md, ARCHITECTURE.md, BUILD_LOG.md | ☑ | 161 items locked; `build.py` + `validate.py` green |
| 2 | Israel hardware research → the Hermon BOM that can actually be bought here | `references/research/israel-drone-hardware-2026-09.md`, `references/hermon-numbers.md`, `HARDWARE.md`, `hardware/*` (8 files) | ☑ | Settled D2 (917–920 MHz) **and** caught a physics error in the original motor choice — see D7 |
| 3 | Rewrite 02.03–02.11 | 9 files | ☑ | All nine rewritten. Every code block **executed** and its real output pasted back. `validate.py --strict` clean |
| 4 | Rewrite 03.01–03.07, write 03.08–03.10 | 10 files | ☑ | All ten written, code executed, `validate.py --strict` clean. Forward-flight power model built and back-propagated into 03.05 and 02.08 |
| 4b | **Mass revision 2 (D9): 1.20 → 1.45 kg** — reconcile module 02 + 03 | 21 | ☑ | Global numeric pass, all code re-run and re-spliced, prose reconciled, `validate --strict` clean |
| 4c | **Reconcile modules 00 and 01** against `hermon-numbers.md` rev 2 | 19 | ☑ | 00.03 and 01.03 rewritten; 01.01/01.02/01.04/01.05/01.06/01.07/01.11/01.12/00.04/00.06 reconciled. Three broken models found and fixed on the way — see the journal |
| 5 | Module 04 — frame & assembly | 6 | ☑ | All six written, code run, output spliced, validated. Plus a module-02 rpm reconciliation (4,637/9,785 → 5,060/9,836) |
| 6 | Module 05 — sensors | 6 | ☑ | All six written, code run, output spliced, validated |
| 7 | Module 06 — state estimation | 6 | ☑ | All six written, code run, output spliced, validated |
| 8 | Module 07 — control | 7 | ☑ | All seven written, code run, output spliced, validated |
| 9 | Module 08 — flight controller | 7 | ☑ | All seven written, code run, output spliced, validated |
| 10 | Module 09 — telemetry & datalink | 5 | ☑ | All five written, code run, output spliced, validated. Plus a real SiK register fix (S1/S2/S3 → S8/S9/S10) across four files |
| 11 | Module 10 — simulation | 5 | ☑ | All five written, code run, output spliced, validated |
| 12 | Module 11 — first flights | 6 | ☑ | All six written, code run, output spliced, validated |
| 13 | Module 12 — autonomous flight | 6 | ☑ | 12.01–12.06, all validated |
| 14 | Module 13 — navigation & GNSS | 5 | ☑ | 13.01–13.05, all validated. EGNOS, not WAAS |
| 15 | Module 14 — vision & perception | 6 | ☑ | 14.01–14.06, all validated |
| 16 | Module 15 — onboard autonomy | 6 | ☑ | 15.01–15.06, all validated |
| 17 | Module 16 — testing & analysis | 5 | ☑ | 16.01–16.05, all validated |
| 18 | Module 17 — payloads & delivery | 6 | ☑ | 17.01–17.06, all validated |
| 19 | Module 18 — civil ops (Part 107) | 6 | ☑ | 18.01–18.06, all validated |
| 20 | Module 19 — capstone | 5 | ☑ | 19.01–19.05, all validated. MAIN PATH DONE |
| 21 | Foundations FA (4) + FEL (5) | 9 | ☑ | FA.01–04, FEL.01–05, all validated `--strict` |
| 22 | Foundations FGL (4) + FRA (4) + FOP (3) | 11 | ☑ | All 20 foundation lessons now validate `--strict` |
| 23 | Projects P01–P08 | 8 | ☑ | All eight written and validated |
| 24 | Non-node files | 9 | ☑ | Module READMEs were already generated; the 9 the sidebar wanted are written |
| 25 | Final pass | — | ☑ | Links final-strict clean; 38 dead external URLs replaced; `index.html` and `README.md` corrected |

---

## Per-batch procedure

```bash
py tools/build.py && py tools/validate.py --strict
```

Then edit the row above to ☑ and add one line to the journal.

### D9 — Hermon's all-up mass is 1.45 kg, not 1.20 kg

**1.20 kg was never achievable.** Four 3110-class motors (352 g) plus a 6S 5000 mAh pack (720 g)
is **1,072 g before the frame, propellers, ESC, flight controller, radios, wiring or fasteners**.
1.20 kg left 480 g for all of that. It was caught while writing module 04's mass budget, which is
the first lesson that itemises the aircraft.

**The new frozen set is in `references/hermon-numbers.md` §8**, which lists exactly what moved and
what did not. Headlines:

| | Rev 1 | **Rev 2** |
|---|---|---|
| All-up mass, clean | 1.20 kg | **1.45 kg** (730 g dry + 720 g pack) |
| With pod | 1.45 kg | **1.70 kg** |
| Hover thrust / motor | 2.94 N | **3.56 N (363 g)** |
| Hover rpm | 4,700 | **5,060** |
| Hover throttle | 46 % | **48 %** |
| Blade-pass | 234 Hz | **253 Hz** — the 07.07 notch centre |
| Thrust-to-weight | 4.56 : 1 | **3.78 : 1** (3.22 with pod) |
| Figure of merit | 0.43 | **0.49** — a *separate* correction, see below |
| Hover power | 194 W | **226 W** (216 W propulsion + 10 W avionics) |
| Hover current | 8.7 A | **10.2 A** (2.0 C) |
| Endurance | 27.4 / published 25 min | **23.6 / published 22 min** |
| Best endurance speed | 7.7 m/s | **8.6 m/s** (200 W, 26.6 min) |
| Cruise 10 m/s | 181 W | **202 W**, 26.4 min, 15.8 km |
| Best range | 16.1 m/s, 21.6 km | **16.8 m/s, 20.4 km** |
| Radius at 6 m/s wind | 5.7 km | **5.1 km** (×0.8 → 4.1 km planning) |
| Mass exchange rate | 0.242 W/g | **0.223 W/g**, 100 g = **2.2 min** |
| $k_{install}$ | 1.113 | **1.121** |
| **Motor KV** | **470** | **470 — unchanged** |

**The KV surviving is the reassuring part**: hover thrust and hover throttle moved together, so
$KV = 5060/(22.2 \times 0.485) = 470$ still. Also unchanged: the pack, the propeller, the
wheelbase, full-throttle figures (9,836 rpm, 1,369 g, 57 A), the failsafes, the radio bands.

**The second, independent correction: FM 0.43 → 0.49.** 02.08 used
$FM = C_T^{3/2}/(C_P\sqrt2)$, which is the *rotor* coefficient convention. In the **propeller**
convention this course uses ($C_T = T/\rho n^2 D^4$), it is
$FM = C_T^{3/2}\sqrt{2/\pi}/C_P = 0.49$. The two routes to shaft power (via FM, and via $C_P$
directly) now agree to 0.2 %; before, they disagreed by 14 %.

**How it was applied:** `scratchpad/mass.py` — an ordered protect / replace / restore pass with
digit-boundary guards, 42 files, ~800 substitutions — then every code block re-run and re-spliced
with `tools/paste.py`. A rev-1 backup sits in `scratchpad/backup_rev1/`.

**What it exposed, and this is the bigger finding:** modules 00 and 01 were never built on
`hermon-numbers.md` at all. They assume **4 N per motor of maximum thrust** (58 occurrences),
a **0.15 kg battery**, `P_MOTORS_HOVER = 180 W` and a thrust-to-weight of 1.36 : 1. That is a
different, much weaker aircraft, and no amount of numeric substitution fixes the reasoning built
on top of it. Hence **batch 4c**.

## Where to pick up

**THE COURSE IS FINISHED.** There is nothing to pick up. What follows is what was done and what is
left for a human to decide.

```
161 nodes, 161 files present, 0 missing
161 files checked, 0 errors, 0 warnings      (validate.py --links --final --strict)
161 files checked, 1 errors, 0 warnings      (validate.py --external — see below)
```

| | |
|---|---|
| main-path lessons | **133** |
| optional foundation lessons | **20** (FA 4 · FEL 5 · FGL 4 · FRA 4 · FOP 3) |
| projects | **8** |
| **total** | **161** |

### What batches 23–25 did

**Batch 23 — the eight projects.** P01 first hover · P02 tuned cascade · P03 SITL harness ·
P04 datalink measured · P05 five clean missions · P06 detection from the air · P07 offboard
autonomy · P08 the capstone campaign. Every one states a goal with a number in it, tests two or
three of the course's own predictions in a table, writes acceptance criteria as **states** with an
evidence column, and ends on the portfolio artefact.

**Batch 24 — the nine files `_sidebar.md` wanted and nothing had written:** `PROGRESS.md`
(generated by `course.py render`), `MAINTAINING.md`, `references/glossary.md`,
`references/papers.md`, `references/resources.md`, `references/troubleshooting/README.md`,
`labs/README.md`, `projects/README.md`, `optional-foundations/README.md`. The module READMEs were
already generated by `build.py` and needed nothing.

**Batch 25 — the final pass.** `--links --final --strict` is clean. `README.md`'s status block
was stale ("37 of 161 lessons written") and is now correct. `index.html` was named
*Practical Robotics* and linked the **robotics** course's repo — the name is fixed and the repo now
points at `tal-giladi/drone-course`. **38 dead external URLs were found by `--external` and replaced with probed,
live ones** across 42 files: nine ArduPilot doc pages that had been renamed, eleven Wikipedia links
(wrong titles, or titles whose parentheses break a markdown link), and eighteen others.

### The one remaining external error, and why it is not a regression

```
ERROR: TimeoutError: https://www.st.com/...stm32h743-753.html  (08.02)
```

`st.com` times out for **every** URL on the domain from an automated checker, including its own
series landing page, while Wikipedia's STM32 page answers instantly. That is bot protection, not a
dead link. **Do not "fix" it by replacing the URL** — it is the canonical ST product page and it
works in a browser.

### Decisions left to a human

[TODO_FOR_TAL.md](TODO_FOR_TAL.md) has five. The repo URL was the first and it is now settled:
the course lives at `tal-giladi/drone-course` and `index.html` links it. What is left:

1. **`17-payloads-targeting/`** is a stale directory holding one generated README from an older
   syllabus (darts, gel blasters, seekers, laser designation — a module that no longer exists).
   Nothing links to it and `validate.py` cannot see it. **It was not deleted**, because removing
   content that may have been cut deliberately is not the build's call.

The rest are `[S]`-marked numbers worth confirming, two conventions chosen without asking, and the
course's own deliberately-open item (below).

### The thing the course leaves open on purpose

**16.05's flow-plus-inertial barrier still has no evidence.** Identified in 16.05, untested through
modules 17 and 18, and 19.05 closes the course still not having tested it. FOP.03 then names it
explicitly: *a finding that survives three debriefs is not a finding any more, it is an undocumented
decision.*

That is the course's best worked example of an honest safety case, and P08's milestone 8 is where a
student closes it. It is the one outstanding **content** decision.

### If you are editing this course

Read [MAINTAINING.md](MAINTAINING.md). It has the syllabus-is-truth rule, the tool list, both
heading schemas (16 for a lesson, 12 for a project), the house style, the gotchas that cost time
during the build, and the release checklist.

```bash
py tools/build.py && py tools/validate.py --links --final --strict && py course.py render
```

### The per-lesson loop, kept for reference

```
write the lesson with empty glance/prereqs markers, an empty ```text after Output:, and @@CODE@@
run the model standalone first, READ the output, fix the prose against the real numbers
substitute the code into @@CODE@@, then paste.py, build.py, validate.py --strict
```

It caught modelling errors rather than typos in every batch, and several of those failures produced
better teaching material than the intended result — 17.02's rejected EPM, 18.03's abort margin
breaching 12.03's, 19.02's VLOS halving, FGL.04's mask that can never pay, FOP.01's contingency pair
that fits by six seconds.

---

## Historical: the batch-by-batch fact tables

Everything below is a record of how the build proceeded. It is kept for the fact
tables, which are the per-module summaries of what each module established. Any
forward-looking statement in it has been overtaken — the course is finished.


**Batch 22 is complete. ALL 20 OPTIONAL FOUNDATION LESSONS ARE DONE** — FA (4), FEL (5),
FGL (4), FRA (4), FOP (3) = 20 lessons. **153 of 161 files**, all validating `--strict`.

**PROJECT FILE FORMAT, now confirmed by writing five of them.** `validate.py` requires for `kind == project`: an H1 starting with the id (`# P06 — Title`), a `<!-- glance:start -->` block, and these **12 headings in order** — `Goal` · `Why this project` · `Prerequisites` · `Hardware and software` · `Architecture` · `Milestones` · `Acceptance criteria` · `Safety` · `Troubleshooting` · `Stretch goals` · `Evidence to keep` · `Progress checkpoint`. **NO prereqs markers, NO exercises, NO knowledge check, NO code block, NO word minimum, and the `[!WARNING]` is not enforced** — but P01–P05 all carry one anyway, plus a `[!CAUTION]`, and the next three should match. Links ARE checked, and the `Search for` warning still applies.

**The house style established across P01–P05, worth matching:** the Goal is one bold sentence with a number in it; `Why this project` names 2–3 course predictions the project TESTS, in a table with `where` and `what you will measure`; `Architecture` is a mermaid flowchart of the WORKFLOW, not of the software; every `Acceptance criteria` row is a **state** with an **evidence** column (FOP.01's Level 2 rule applied to the course itself); `Evidence to keep` always ends on the portfolio artefact. Recurring cross-links: FOP.01 (plan), FOP.02 (barriers/evidence), FOP.03 (one change, one artefact), 18.02 (₪2,084 a day), 19.05 (a rate with an interval).

**Original note on batch 23 — projects P01–P08 (8 files).** The project entries live at the BOTTOM of
`curriculum/syllabus.yaml`, under a top-level `projects:` key (not inside a module). Run
`py tools/paths.py P0` for the slugs and read each entry before writing. Do not guess a slug.

**PROJECTS ARE A THIRD KIND OF FILE** — not a main-path lesson and not a foundation. Check what
`validate.py` actually requires of them before writing the first one (the 16 headings may or may
not apply; `tools/validate.py` is the authority, and `py tools/validate.py --paths projects/*.md
--strict` on a first draft is the fastest way to find out). Their character:

- They produce **EVIDENCE**, not understanding. P01 is "hover 30 s with drift ≤ 0.5 m **and the
  log + video to prove it**".
- They have `hardware: [stage1]` or higher, so a **`[!WARNING]` or `[!CAUTION]` IS REQUIRED**.
- Every acceptance criterion should be a **measurable state** — FOP.01's Level 2 test, applied to
  the course's own projects.
- Each one should name the **artefact** it produces (FOP.03's rule): a log, a video, a parameter
  file, a report.

**What the foundations established** (batch 21's FA/FEL table is above; here is batch 22's):

| Fact | Where |
|---|---|
| The Earth is **21,385 m** fatter than tall; geodetic vs geocentric latitude is **19 km** at our site | FGL.01 |
| A degree of longitude here is **85 %** of a degree of latitude — a square in degrees is 1000 × 847 | FGL.01 |
| `1e-7` deg = **1.11 cm**, **406× finer than 13.02's 4.50 m UERE**; float32 is 23 cm | FGL.01 |
| A datum error is **245 m** — **54× the whole GNSS budget** — and RTK does not touch it | FGL.01 |
| Geoid N ≈ **17 m**, and it CANCELS in every relative altitude — until you mix a DEM with a receiver: **30 m of clearance becomes 13** | FGL.01 |
| In ECEF **one metre is the 8th significant digit** — that is why local frames exist | FGL.02 |
| ENU↔NED has **determinant +1**: a real 180° rotation, and the missing sign is **60 m, exactly twice, every time** | FGL.02 |
| Euler angles are a **recipe with an order**: Z-Y-X vs X-Y-Z is **14.7°** apart | FGL.02 |
| A flat Earth is wrong by **46 cm at 19.02's 2,420 m** and first matters at **7.6 km**, which the aircraft cannot reach | FGL.02 |
| **The EKF origin is not HOME**, and 12.04's RTL flies to HOME | FGL.02 |
| Corrected flat-Earth distance is **10 microns** out at VLOS range; **the cosine is the bug, not the curvature** | FGL.03 |
| And the cosine bug is **0 % due north, 18.6 % due east** — which is how it survives testing | FGL.03 |
| Bearing convergence over a VLOS leg is **0.0139°**; **declination is 325× that** and puts you **190 m off** | FGL.03 |
| A rhumb line and a great circle differ by **16 microns** at VLOS range | FGL.03 |
| A **UTM metre is 0.9996** of one: 97 cm over a VLOS leg and **0.08 % of every area, as a BIAS** | FGL.03 |
| **Variances add, errors do not**: 6 sources → 4.50 m, not 8.2; perfecting the smallest buys **0.4 %** vs the largest' **54 %** (**137 : 1**) | FGL.04 |
| DOP is **(G'G)⁻¹ read off the diagonal** — DIMENSIONLESS, containing no measurement | FGL.04 |
| **VDOP beats HDOP by 1.30×** because every satellite is above you | FGL.04 |
| **A mask ONLY EVER COSTS GEOMETRY** (125 % / 239 % at 30°). It is a MULTIPATH setting, and in the open it cannot pay | FGL.04 |
| CEP/drms/R95/2drms differ by **2.7×**; R95 is **0.7× the mission CEP and 19× 12.05's landing criterion** | FGL.04 |
| **An antenna is a LENGTH**: 8.2 cm at 917 MHz, 3.1 cm at 2440 | FRA.01 |
| dB + dBm = dBm; **dBm + dBm is nonsense**. dBi is AIM, and the regulator measures **EIRP** | FRA.01 |
| **-174 dBm/Hz + 10log(BW) + NF + SNR = -112 dBm**, 09.01's SiK sensitivity DERIVED | FRA.01 |
| **Slowing down is the cheapest decibel in radio** — 12 dB, for latency only | FRA.01 |
| **The frequency term in FSPL is the RECEIVING ANTENNA, not propagation** — 8.5 dB, constant at every distance | FRA.02 |
| 135 dB → **146 km**, correct and useless. Range goes as **√power** | FRA.02 |
| Fresnel needs **7.7 m at 2 km**, and the height is the **MIDPOINT** — an aircraft at 10 m is OBSTRUCTED with 135 dB spare | FRA.02 |
| Beyond `4h₁h₂/λ` loss goes as d⁴: **146 km becomes 21** | FRA.02 |
| **STATE A MARGIN, NOT A RANGE**: 36 dB at 2,420 m, 7× the Fresnel clearance. **ALTITUDE IS THE LINK BUDGET** | FRA.02 |
| A dipole **nulls off the tip**: 15.2 dB down at 10°. A monopole with no ground plane makes one from the coax | FRA.03 |
| **Both vertical whips aim their nulls UP AND DOWN**, so the margin is worst DIRECTLY OVERHEAD: **12 dB vs 36 dB at 2,420 m** | FRA.03 |
| Polarisation is cos²: **1.2 dB at 30° of bank**, ~25 dB crossed. **Circular costs a fixed 3 and removes that 25** | FRA.03 |
| **SWR 3 costs only 1.25 dB** — it matters because the power goes BACK INTO THE PA. A dummy load reads 1.0 | FRA.03 |
| SBUS worst-case stick age is **17.0 ms** and **07.03's loop runs 7× inside it** — that is why the cascade exists | FRA.04 |
| Hopping turns a catastrophic failure into a gradual one; **CRSF at 50 % loss still beats SBUS at none, at 75 % it does not** | FRA.04 |
| **Routine telemetry is 22× ETSI's 1 % duty cycle** — 868 MHz could not carry it even where legal | FRA.04 |
| **Israel's 917–920 MHz is 8.7× narrower** than the US band: 6 hop channels vs 52. SURVEY THE SITE | FRA.04 |
| Six radio links, **only CONTROL is required to keep flying**; **Remote ID is the only LEGAL failure** | FRA.04 |
| A question costs **1 at the desk, 50 on site, 100 after delivery**. All eight cost ₪333 | FOP.01 |
| **An objective is a STATE, not an activity** — only 42 % of a realistic plan qualifies. A state can be REACHED ANOTHER WAY | FOP.01 |
| Five paragraphs, and **the aborts go in COMMAND AND SIGNALS** — including the 2 rows ANYBODY may call. The test is the **READ-BACK** | FOP.01 |
| **A margin holds exactly ONE contingency**: 1 pair of 10 fits, by 6 seconds. Fit it, abort on it, shrink it, **or SPLIT it** | FOP.01 |
| **L × S destroys the remedy**: four hazards score 6 and need four incompatible treatments | FOP.02 |
| On the recovery side almost every row names **the same barrier, and it is a DISTANCE** | FOP.02 |
| `P = ((1-β)p)ⁿ + βp`: at β = 0.3, **six barriers are 3.3× one**, and the penalty is **worst where you worked hardest** | FOP.02 |
| **The only barrier with β = 0 is the one with no aircraft in it** | FOP.02 |
| **A barrier without evidence is a belief** — one untested barrier of eight moved a residual **63 %** | FOP.02 |
| 16.05's 8.1e-4 = one flight in **1,239** = **once every 35 years** — so you will never learn it by flying | FOP.02 |
| Without a written plan, **58 % of what you observed is unusable** | FOP.03 |
| **Blame is arithmetic**: reporting 0.90 → 0.25 under-counts **3.6×**, and 35 years becomes **10** | FOP.03 |
| Eight agreed actions: expected 1.6, **P(all) = 0.000003**. ONE change | FOP.03 |
| **A change is only real if it modifies an ARTEFACT** — checklist, parameter, or manual. 4 of 8 proposals are intentions | FOP.03 |
| **All three of 19.05's course-level findings were type B** — the hazards were right, THE NUMBERS WERE OPTIMISTIC | FOP.03 |
| A finding surviving three debriefs **is a DECISION, not a finding** | FOP.03 |

**The capstone's closing numbers, which every remaining file should stay consistent with:**

| Fact | Where |
|---|---|
| The mission is **10:01 of 11:12 usable** — 1:11 of margin — so TWO FLIGHTS | 19.01 |
| 13 abort rows: **5 the aircraft's, 6 the PIC's, 2 anybody's** | 19.01 |
| Setup: site 11:00 once + aircraft **15:12** per flight + 393 s of free waits. Flight 2 is **6:12** | 19.02 |
| VLOS: a dot at **2,420 m**, attitude only to **242 m** — 18.05's 500 m was **2× optimistic** | 19.02 |
| **7 of 10 systems checks fail silently** | 19.02 |
| **3 of 11 within 2.8 m: one false confirmation in 303 flights, 88 % recall** | 19.03 |
| **Precision landing acquires only 55 % of the time on GPS** | 19.04 |
| **A ₪50 printed sheet and a ₪2,000 RTK buy the same 100 %** | 19.04 |
| The mission is **4.8 clean flights in 10**, and **8.8 with the sheet** | 19.04 |
| **8 of 10 means 49 % to 94 %**; separating 48 % from 88 % needs **19 flights** | 19.05 |
| **16.05's barrier STILL has no evidence** after three modules | 19.05 |
| Hermon: **1.450 kg**, T_hover **3.556 N**/motor, **88.8 Wh**, **226 W**, **23.6 min** | `references/hermon-numbers.md` |

**Per-lesson loop (unchanged — follow it exactly):**

```
write the lesson with empty glance/prereqs markers, an empty ```text after Output:, and @@CODE@@
run the model standalone first, READ the output, fix the prose against the real numbers
substitute the code into @@CODE@@, then paste.py, build.py, validate.py --strict
```

Remember the **## Prerequisites** heading with its empty markers, and a `[!WARNING]`/`[!CAUTION]`
whenever the syllabus entry has non-empty `hardware` — **which every project has.**
`py tools/paths.py <prefix>` before linking to anything; never guess a slug. `validate.py --paths`
takes a **glob, not a directory**, and in bash the glob must be **unquoted**. Two globs that work:
`optional-foundations/*/*.md` and `18-civil-ops/*.md`.

**Standing gotchas, all of which have cost time at least once:**

- `%%` only survives inside a string that actually has a `%` operator applied to it. In a plain
  `print("...")` it prints as `%%`.
- Prefer the Write tool for any patch script with backslashes or longer than ~50 lines; bash
  heredocs eat backslashes and apostrophes.
- `validate.py` warns on the phrase "Search for" in a lesson. Reword.
- When a model prints a table and the prose then summarises it, **re-read the table**: four of the
  errors caught in batches 21–22 were a summary contradicting its own table.
