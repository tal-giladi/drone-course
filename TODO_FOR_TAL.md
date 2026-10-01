# TODO for Tal

Things the build could not decide without you. Nothing here blocks reading or flying the course —
all 167 files are written and validate `--strict`. **Item 6 is new and is the most consequential
one** — read it before planning an Academy import.

## 1. A stale directory: `17-payloads-targeting/`

It contains one file, `README.md`, generated from an **older syllabus** that had an 11-lesson module
on darts, gel blasters, nets, seekers and laser designation. That module no longer exists — it was
replaced by `17-payloads-delivery/` (6 lessons: payload mass, release mechanisms, spray/irrigation,
release dynamics, drop-point maths, building the pod).

Nothing links to it and `validate.py` does not see it, but it would ship with the site and it
contradicts the syllabus. **I did not delete it** — it describes content that may have been removed
deliberately, and deleting is yours to decide.

```bash
rm -r "17-payloads-targeting"
```

## 2. Three external URLs the link checker cannot reach

```
ERROR: TimeoutError: https://www.st.com/...stm32h743-753.html   (08.02)
ERROR: TimeoutError: https://www.st.com/en/...stm32h743-753.html (08.02)
ERROR: URLError:    https://m-selig.ae.illinois.edu/props/propDB.html  (02.06, 02.07, 02.11)
```

`st.com` times out for **every** URL on the domain from an automated checker, including its own
series landing page, while other sites answer instantly. That is bot protection, not a dead link —
it works in a browser. **Do not replace it**; it is the canonical ST product page.

The UIUC **propDB** host is intermittent — it answered on some runs and raised a bare `URLError`
on others, and it is a genuinely useful reference for module 02's thrust numbers. Re-run
`py tools/validate.py --external` before touching it; if it is ever truly gone, the measured
coefficients in [`references/hermon-numbers.md`](references/hermon-numbers.md) do not depend on
it.

Everything else resolves. 38 dead ones were replaced during the final pass of batch 25, and the
**five found while adding CUX** (four ArduPilot/FAA URLs I had picked, plus a pre-existing SKYbrary
link in FOP.03) were replaced or de-linked this session. The FOP.03 citation now names Reason's
1990 book directly instead of guessing at a URL.

## 3. Numbers marked **[S]** that are worth confirming before you rely on them

These came from search snippets rather than from a primary source. Each is labelled `[S]` in the
lesson, and each would change a conclusion if it were wrong:

| number | where | why it matters |
|---|---|---|
| Palestine 1923 → WGS84 shift: dX −275.72, dY +94.78, dZ +340.89 m | FGL.01 | gives the 245 m datum error; check against the EPSG registry |
| geoid separation N ≈ +17 m, northern Israel | FGL.01, FGL.03 | the DEM-versus-receiver hazard |
| magnetic declination ≈ 4.5° | FGL.03 | 190 m of cross-track over a VLOS leg |
| Israel's licence-exempt sub-GHz window 917–920 MHz | FRA.04, 09.05 | the whole telemetry design rests on it |
| ETSI 868 MHz 1 % duty cycle | FRA.04 | the argument for not using the European band |
| ELRS sensitivities −117 / −108 / −105 dBm | FRA.01, FRA.02 | the link budget's range figures |

## 4. Two conventions I chose without asking

**Ten flights, not nineteen.** P08 asks for ten capstone missions because 19.05's arithmetic says
ten pins the bias to 9 cm but leaves the CEP at ±22 %, and **nineteen** would be needed to
distinguish 48 % from 88 %. Ten is a compromise between statistics and batteries; the stretch goal
says so.

**FOP.02's worked bowtie is its own example**, not 16.05's seventeen-barrier one. It reproduces
16.05's *findings* (β makes the best-protected threat worse; a barrier without evidence is a belief)
on a four-threat example you can hold in your head, then checks itself against 16.05's published
residual. If you would rather it re-derived the full seventeen, that is a rewrite of one section.

## 5. The course's own open item, deliberately left open

**16.05's flow-plus-inertial fallback barrier still has no evidence.** It was identified in 16.05,
not tested in module 17, not tested in module 18, and 19.05 closes the course still not having tested
it. FOP.03 then names this explicitly: *a finding that survives three debriefs is not a finding any
more, it is an undocumented decision.*

That is intentional — it is the course's best worked example of an honest safety case. P08's
milestone 8 and its stretch goals are where a student closes it. **If you would rather the course
closed it itself**, that is a new lesson or a substantial addition to 13.05, and it is the one
outstanding content decision in the whole build.

## 6. NEW — this course does **not** match the Academy import format

Found while adding the CUX track. It is not caused by that work and nothing is broken, but it
must be settled **before** the course is imported.

`CLAUDE.md` points at `C:\Users\TalGiladi\OneDrive\repos\tals-academy\docs\new-course-instructions.md`
as binding. That file prescribes a layout this repo does not use:

| | `new-course-instructions.md` | this repo |
|---|---|---|
| Layout | `lessons/module-NN/lesson-MM.md` | `NN-name/NN.NN-slug.md` |
| Front-matter | `id`, `module`, `minutes`, `prerequisites`, `objectives`, `volatility`, `last_verified` | **none, in any of the 167 files** |
| Quizzes | a separate `.quiz.yaml` per lesson, 4 options, one correct | 153 files exist, but in the **old fingerprint format** (see below) |
| Module quizzes | `assessments/module-NN-quiz.yaml`, 8–10 questions | none |
| Sidebar | `- **Module N — Title**` | docsify tree generated by `build.py` |
| Source of truth | the markdown | `curriculum/syllabus.yaml` |

**The 153 existing quizzes may all be dropped on import.** They use the format your commit
`2b183d3` introduced:

```yaml
- source: 06d89b7abb3a
  question: ...
  options: [...]
  correct: 0
```

§5 says: *"No `source:` field (that is the old fingerprint format for retrofitted courses)"* and
*"A quiz entry that breaks any rule above is dropped on import."* It also **requires** an
`explanation`, which none of the 153 have. On a literal reading of §5 that is **153 files and
~1,026 questions that import as nothing** — the exact failure the guidelines cite for *baking* and
*pen-tester*.

**The CUX quizzes are the exception:** the six written today use the §5 format (`id`, `question`,
`options`, `correct`, `explanation`, no `source`). I did not reproduce the fingerprint because it
cannot be computed honestly — it is not a plain hash of the question, and a random 12-hex value
would silently break the drift detection it exists for.

**So there is a decision, and it is a mechanical one:** either the 153 are converted to §5
(add `explanation` from each lesson's `<details>` answer, drop `source`, add `id`), or the importer
is taught to accept the fingerprint format. CUX is already on the §5 side.

**The rest of item 6 stands:**

**The scale of the full migration:** 167 lessons needing front-matter and heading restructuring,
~24 module quizzes, and the layout change. That is a separate project, not a task.

**What was done about it here:** nothing, deliberately. The CUX track was written in the repo's
**existing** format so that `tools/validate.py` stays the single authority and 167 files stay
green. Writing six lessons in a foreign format would have broken `--strict` and left the tree
incoherent. **The decision is yours:** migrate the whole course to the Academy format before
import, or import it as-is and accept that it does not conform.

**Also undecided:** `curriculum/course-details.md` (course slug, free or paid, risk notice) and
`PUBLISHING_WARNING.md` both belong to that migration and do not exist yet.
