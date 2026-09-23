# Maintaining the course

How to change this course without breaking it.

Everything here is enforced by `tools/validate.py`, which is the authority whenever this document and
the tool disagree.

## The one rule

> **`curriculum/syllabus.yaml` is the single source of truth.**

Module structure, lesson ids, slugs, titles, difficulty, time, prerequisites, hardware, software,
`teaches` and `skip_if` all live there. Nothing else declares them, and the generated blocks in every
lesson come from it.

Edit the syllabus, then run `tools/build.py`. Never edit a generated block by hand.

## The tools

| | |
|---|---|
| `py tools/build.py` | regenerates `curriculum/graph.json`, `_sidebar.md`, `COURSE_MAP.md`, module READMEs, and the `glance` / `prereqs` blocks in every lesson |
| `py tools/paths.py <prefix>` | prints canonical file paths for ids. **Run this before writing any link.** |
| `py tools/paste.py <file.md>` | runs the lesson's `python` block and splices real stdout into the following ```text block |
| `py tools/validate.py` | structure, headings, exercises, links |
| `py course.py render` | regenerates `PROGRESS.md` from `progress/progress.json` |

## Validation

```bash
py tools/validate.py --strict
```

```bash
py tools/validate.py --links --final --strict
```

`--paths` takes a **glob, not a directory**, and in bash the glob must be **unquoted** so the shell
expands it:

```bash
py tools/validate.py --paths optional-foundations/*/*.md --strict
```

`--external` checks every outbound URL over the network. It is slow and it is the right thing to run
before a release.

## Adding a lesson

1. Add the entry to `curriculum/syllabus.yaml` — id, slug, title, difficulty, time, requires,
   optional, hardware, software, teaches, skip_if.
2. Run `py tools/paths.py <id>` to get the canonical path. **Do not invent a slug.**
3. Write the file with:
   - an H1 starting with the id
   - empty `<!-- glance:start --><!-- glance:end -->` markers
   - a `## Prerequisites` heading with empty `<!-- prereqs:start --><!-- prereqs:end -->` markers
   - a ```python block with `@@CODE@@` as a placeholder
   - an `Output:` line followed by an **empty** ```text block
4. Write and run the model **standalone first**, read its output, and fix the prose against the real
   numbers.
5. Substitute the code, then `paste.py`, then `build.py`, then `validate.py --strict`.

### The 16 lesson headings, in order

What you will learn · Why it matters · Prerequisites · Concept · Technical explanation · Diagram ·
Code · Exercise · Expected result · Troubleshooting · Common mistakes · Knowledge check ·
Practical challenge · You can skip this if · Go deeper · Progress checkpoint

Also required: exercise headings of the form
`### Exercise <id>-E<n> — title \`[tag]\``, at least **5** `<details>` answers in Knowledge check,
at least **2** external URLs in Go deeper, a diagram, an "Ask your teacher" tip, and **≥ 900 words**.
A `[!WARNING]` or `[!CAUTION]` is required when the syllabus entry has non-empty `hardware`.

### The 12 project headings, in order

Goal · Why this project · Prerequisites · Hardware and software · Architecture · Milestones ·
Acceptance criteria · Safety · Troubleshooting · Stretch goals · Evidence to keep ·
Progress checkpoint

Projects need **no** prereqs markers, no exercises, no knowledge check, no code block and no word
minimum — but every one in this course carries a `[!WARNING]` and a `[!CAUTION]` anyway, and new
ones should match.

## House style

These are conventions rather than checks, and they are what makes the course consistent.

**Every number is derived, and every model runs.** Code blocks are pure-standard-library Python, no
numpy, deterministic, and runnable standalone. The output in the ```text block is **real stdout**,
spliced by `paste.py` — never typed by hand.

**Confidence markers.** **[V]** verified, **[S]** from a search snippet, **[E]** an estimate. Use
them on any number you did not compute yourself.

**Aircraft numbers come from one place.** [`references/hermon-numbers.md`](references/hermon-numbers.md)
is frozen. A lesson that needs the mass or the hover thrust reads it from there; it does not restate
it from memory.

**Israeli constraints are not optional.** Prices in ₪ including 18 % VAT; the licence-exempt sub-GHz
band is **917–920 MHz** and nothing else; the personal-import VAT exemption is **$75**; 1 USD =
**₪3.033**.

**Certification content stays FAA Part 107.** Hardware is sourced in Israel; the certificate taught
is American, deliberately.

**Lessons close on a number the course already uses.** Especially the optional foundations — their
whole purpose is to make a main-path number recognisable.

**Cross-references are honest.** If a lesson contradicts an earlier one, say so and give both
numbers. Three of module 19's findings are the course correcting itself, and that is a feature.

## Gotchas that have cost time

- **`%%` only survives** inside a string that actually has a `%` operator applied to it. In a plain
  `print("...")` it renders as `%%`.
- **Re-read the table before believing the prose.** Several errors caught during the build were a
  summary contradicting the table directly above it.
- **`validate.py` warns on the phrase "Search for"**. Reword it.
- **Prefer writing patch scripts to a file** over bash heredocs; heredocs eat backslashes and
  apostrophes.
- **Never guess a slug.** `tools/paths.py` exists for this and every link error during the build was
  a guessed slug.

## Changing a frozen number

If Hermon's mass, thrust or endurance ever changes:

1. Change `references/hermon-numbers.md`.
2. Find every lesson that uses the number — search, do not rely on memory.
3. **Re-run every affected model** and re-splice with `paste.py`. The outputs are real; they must be
   regenerated, not edited.
4. Re-read the prose around each one. A substituted number with unchanged reasoning is the most
   dangerous kind of error, because it validates cleanly.

This has happened twice in the course's history and both times the reasoning, not the arithmetic, was
the expensive part.

## Release checklist

```bash
py tools/build.py && py tools/validate.py --links --final --strict && py course.py render
```

Then check by hand:

- `README.md`'s lesson count is current
- `COURSE_MAP.md` and `_sidebar.md` were regenerated
- `index.html` still loads the sidebar
- `py tools/validate.py --external` passes, or every failure is understood
- `BUILD_LOG.md` says where things actually stand

## Where the build history is

[BUILD_LOG.md](BUILD_LOG.md) — the batch table, the decisions, and the per-module fact tables. It is
the first thing to read after a break, and it is kept current deliberately so that a session which
ends unexpectedly loses nothing.
