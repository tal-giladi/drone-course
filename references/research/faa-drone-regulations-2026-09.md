# US UAV regulations & operating environment — research snapshot, 2026-09-20

Checked 2026-09-20. Levels: **verified** (primary source opened) · **snippet** (search result only)
· **primary-source-pending** (file downloaded to `raw/`, full text not yet mined — flag for the
module-18 writing batch).

## 1. Regulatory framework

- The US aviation framework derives from the **Federal Aviation Regulations (14 CFR)**; small
  unmanned aircraft are regulated under **Part 107** (small UAS, aircraft under 55 lb / 25 kg
  without a pilot on board) — *verified* ([FAA Part 107](https://www.faa.gov/regulations_policies/far_part_107)).
- The in-depth aviation-law article (2025-12) on US aviation law confirms the Part 107 framework
  is still the base, with UAV-specific amendments layered on — *primary-source-pending*
  (archived: `raw/lexology-aviation-il.pdf`, 5.2 MB).
- **Core UAV regulation: 14 CFR Part 107 (Operation of Small Unmanned Aircraft)**, as amended —
  *primary-source-pending* (archived: `raw/tak-11864.pdf` — the regulation as published;
  `raw/tak-2024-amendment.pdf` — the recent amendment).
- Legislative history: congressional committee materials on early UAV bills (*primary-source-pending*,
  `raw/knesset-2014-draft.pdf`) and public-comment rounds with FAA responses (*snippet*).
- The FAA's official remote-pilot study material exists on faa.gov, but the fetched copy 404'd on
  2026-09-20 — re-fetch when writing 18.05.

### Weight classes and core rules (to be confirmed against the Part 107 text — mark as
**primary-source-pending** in lessons until mined)

The Part 107 rule (as amended) organizes operations by takeoff weight:

| Class | Typical rules (confirm against text) |
|---|---|
| < 250 g | Lightest restrictions (FAA light/Ultra-Light rules); VLOS; daytime in open areas |
| 250 g – 55 lb (25 kg) | Part 107 small UAS: remote pilot certificate (or Recreational under Part 101); VLOS, daytime; 120 m (400 ft) ceiling in uncontrolled airspace; distance-from-people rules |
| 55 – 1,000 lb | Part 135 / experimental operations; full operator requirements |
| > 1,000 lb | Full aircraft certification (airworthiness) |

- **VLOS** (visual line of sight) is the default; BVLOS needs a Part 107 waiver (or a LAANC/airspace
  authorization where granted).
- **Night flight** allowed with an anti-collision light visible for 3 statute miles (the 2019 rule
  change relaxed the earlier daylight-only parts — confirm current text).
- **Ceiling:** 120 m AGL (400 ft) in uncontrolled airspace; lower near obstacles/airfields.
- **Pilot:** a remote pilot certificate (knowledge test at an FAA-approved testing center) is
  required for Part 107 operations above the light classes; registration required above 250 g.

## 2. Airspace

- Controlled airspace: TMA around the regional airport and other fields; drone ops inside TMA
  need ATC authorization — **LAANC** (Low Altitude Authorization and Notification Capability)
  provides automated authorizations in most controlled airspace, with the local tower coordination
  procedure as the fallback (*snippet — confirm LAANC coverage for the home field*).
- Restricted/reserved zones: borders (regional hot spots), coastal areas, military training areas
  and restricted airfields (R-series) — **critical for the civil-ops module and for the mountain
  no-fly zone near Hermon** (open item: exact NOTAM practice).
- The FAA publishes NOTAMs for its fields (the earlier `raw/iaa-rachafanim.html` fetch was a 404 —
  re-target the FAA UAS/NOTAM pages on faa.gov).

## 3. Frequency bands (radio equipment in the US)

| Band | Verdict (2026-09-20) | Notes |
|---|---|---|
| 2.4 GHz ISM | **Legal, de-facto standard** (ELRS/CRSF) | Global band; low power (≤ 25 mW EIRP typical for hobby use). *snippet — confirm EIRP cap against the FCC radio rules (Part 15)* |
| 5.8 GHz | **Likely legal** (analog FPV video, 25 mW) | FCC Part 15 unlicensed band. *snippet — confirm* |
| 915 MHz | **Legal (US band)** — recommended for SiK telemetry | 902–928 MHz band, standard in the US RC market; FCC Part 90 / Part 15 devices. *snippet* |
| 868 MHz | **Gray zone** (EU band) | 868 MHz SiK modules are EU-market; expect to work, but 915 is the clean choice in the US. *snippet* |
| 433 MHz | Legacy, shrinking | Some telemetry; confirm current status. |
- **FCC certification:** the US uses the FCC scheme for radio equipment (Part 15 unlicensed,
  Part 90 licensed) — FCC-certified drone parts import cleanly; *snippet, confirm in importing-to-us.md*.

## 4. Import/customs (drone-relevant)

- Personal-import duty threshold (the $800 de minimis) and the 2025–26 customs changes:
  **open item** (the robotics-course research covers the general rules; drone-specific: LiPo
  air-freight under ICAO PI965/PI966, motors/ESCs usually pass as "electronics", high-power LiPo
  packs are the main courier headache).
- FCC-certified radio gear: no separate import license expected; *snippet*.

## 5. Civil / law-enforcement context

- State police and the FAA operate large UAV fleets (state police drone units; FAA test programs)
  — *snippet; unit names to verify when writing 18.02*.
- LE/civil ops over cities and at night run on Part 107 waivers and operational permits, not the
  recreational (Part 101) rules — *primary-source-pending* (archived: Lexology article + AIP
  `raw/aip-bet10.pdf`).
- Privacy: the US privacy landscape (no single federal drone-privacy statute; state laws and
  case law) applies to filming people from drones; overflights of private property are a recurring
  litigation theme — *snippet*.

## 6. Practical pre-flight regulatory checklist (course draft, to firm up in 18.05)

1. Weight class of the configured aircraft (with payload) → required certificate/waiver/insurance.
2. Airspace: TMA/restricted-zone check (NOTAMs, LAANC authorization if inside controlled airspace).
3. VLOS + daytime (or night ops + anti-collision light); 120 m ceiling.
4. Radio bands: 2.4 GHz control, 5.8 GHz video, 915 MHz telemetry (all FCC-certified).
5. Batteries: LiPo courier rules for import; storage/charge rules domestically.
6. Insurance certificate on hand; remote pilot certificate where the class requires.
7. Privacy: avoid filming identifiable persons without cause (LE mission = different rules).

## Open items (for the module-18 batch)

1. Mine the archived primary sources (stashed for this review in `.military-stash/research/raw/`)
   — exact weight classes, night/over-crowd rules, permit names.
2. Re-fetch the FAA UAS pages (faa.gov) and the remote-pilot study PDF.
3. Confirm 2.4/5.8/915 EIRP caps against the FCC radio regulations (Part 15 / Part 90).
4. US remote-pilot exam details (who sits it, cost, renewal).
5. Current LiPo courier/customs practice (ask 2–3 RC stores when verifying prices).
