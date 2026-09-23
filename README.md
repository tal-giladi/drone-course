# Practical UAV — from software engineer to civil drone operator (FAA Part 107)

A hands-on UAV course for an experienced software/AI engineer who wants to **design, build,
program, test and operate a civil quadcopter** — and end up job-ready as a civil drone
operator.

**Parts are bought in Israel.** Every component in the build has an Israeli supplier, an
₪ price, and a substitute spec; where a part is not legally usable here it has been swapped
for one that is (the telemetry radio is constrained to 917-920 MHz). The certification half of the
course teaches the **FAA Part 107** syllabus.

> [!NOTE]
> **Status: complete.** All **161 of 161** files are written and validate `--strict`: 20 modules,
> **133 main-path lessons**, **20 optional foundation lessons** and **8 projects**, defined in
> [ARCHITECTURE.md](ARCHITECTURE.md) and declared in
> [`curriculum/syllabus.yaml`](curriculum/syllabus.yaml).
> Build history and per-module fact tables: [BUILD_LOG.md](BUILD_LOG.md).
> To change anything: [MAINTAINING.md](MAINTAINING.md).

## The build vehicle

**Hermon** — a ~1.45 kg, 45 cm, 6S quadcopter on 10–12 in props. You size its powertrain,
budget its power, build it, tune it, fly it, instrument it, fit it with a 250 g delivery pod,
and certify it for a full autonomous **survey → detect → deliver → precision-RTL** mission
(the capstone, module 19).

## How to study this course

- The course site: open `index.html` in a browser (docsify).
- Progress: `py course.py status` / `py course.py next` (standard library only).
- Prerequisite readiness: `py course.py why <lesson-id>` — tells you exactly what to learn
  before a lesson, and whether the
  [robotics course](https://github.com/tal-giladi/robotics-course) already covered it.

## Key documents

| File | What it is |
|---|---|
| [BUILD_LOG.md](BUILD_LOG.md) | **Start here after a break** — decisions, batch plan, and where the build stopped |
| [ARCHITECTURE.md](ARCHITECTURE.md) | The 11 architecture deliverables (curriculum map, prerequisites, hours, hardware, Israeli purchasing, software stack, textbooks, assessment, capstone, repo structure, progress tracking) |
| [COURSE_MAP.md](COURSE_MAP.md) | The whole course on one page |
| [HARDWARE.md](HARDWARE.md) | What to buy, when, and from which Israeli supplier (₪, incl. VAT) |
| [SAFETY.md](SAFETY.md) | Standing rules + hazards by stage |
| [drone-course.md](drone-course.md) | The original instructions |
