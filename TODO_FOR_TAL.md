# TODO for Tal

Things the build could not decide without you. Nothing here blocks reading or flying the course —
all 161 files are written and validate `--strict`.

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

## 2. One external URL the link checker cannot reach

```
ERROR: TimeoutError: https://www.st.com/...stm32h743-753.html   (08.02)
```

`st.com` times out for **every** URL on the domain from an automated checker, including its own
series landing page, while other sites answer instantly. That is bot protection, not a dead link —
it works in a browser. **Do not replace it**; it is the canonical ST product page.

Every other external URL in the course now resolves. 38 dead ones were found and replaced during
the final pass: nine ArduPilot doc pages that had been renamed, eleven Wikipedia links (wrong
titles, or titles whose parentheses break a markdown link), and eighteen others.

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
