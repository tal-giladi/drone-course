# Resources

Places worth going back to. Everything here is referenced from at least one lesson, and the reason
it is here is stated — a bare link list is not a resource.

> [!NOTE]
> **Version-sensitive.** Firmware documentation, regulatory pages and supplier catalogues all move.
> Re-check anything with a version number in it before relying on it, and see
> [`research/software-versions-2026-09.md`](research/software-versions-2026-09.md) for what was
> current when the course was written.

## Firmware and autopilot

| | |
|---|---|
| [ArduPilot documentation](https://ardupilot.org/copter/) | The primary reference for every parameter this course sets. The Copter section is the one you want. |
| [ArduPilot parameter list](https://ardupilot.org/copter/docs/parameters.html) | Searchable, versioned, and the authority when a lesson and a build disagree |
| [ArduPilot SITL](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html) | Module 10 and P03 live here |
| [ArduPilot developer docs](https://ardupilot.org/dev/) | For module 15's offboard work and anything involving the code itself |
| [PX4 documentation](https://docs.px4.io/) | Not this course's firmware, but the second opinion is often the clearest explanation |

## Protocols and ground stations

| | |
|---|---|
| [MAVLink common message set](https://mavlink.io/en/messages/common.html) | FRA.04's point about `relative_alt` being **up** and `*_NED` being **down** is visible right in the spec |
| [QGroundControl](https://docs.qgroundcontrol.com/) | The ground station used throughout |
| [ExpressLRS](https://www.expresslrs.org/) | Packet rates, link quality and the sensitivity figures FRA.01 derives |
| [ROS 2 documentation](https://docs.ros.org/) | Module 15 |
| [REP-103](https://www.ros.org/reps/rep-0103.html) | Why half of robotics is ENU and half of aviation is NED |

## Navigation and GNSS

| | |
|---|---|
| [ESA Navipedia](https://gssc.esa.int/navipedia/) | The best free treatment of pseudoranges, DOP and error budgets |
| [GPS performance standards](https://gssc.esa.int/navipedia/index.php/GPS_Performances) | Defines which accuracy metric a published figure actually is |
| [EPSG registry](https://epsg.org/home.html) | Every datum and transformation. Check FGL.01's `[S]` numbers here |
| [NOAA geoid models](https://geodesy.noaa.gov/GEOID/) | Your own N, for FGL.01's Level 4 |
| [NOAA magnetic field calculators](https://www.ncei.noaa.gov/products/world-magnetic-model) | Declination and its annual drift — FGL.03's 190 m |
| [Movable Type: lat/long formulas](https://www.movable-type.co.uk/scripts/latlong.html) | Haversine, rhumb lines and destination, with derivations |
| [GNSS planning](https://www.gnssplanning.com/) | Predict DOP at a site before you drive there |

## Radio

| | |
|---|---|
| [ARRL Handbook reference](https://www.arrl.org/arrl-handbook-reference) | Decibels, antennas, noise — the standard treatment |
| [ITU P.526](https://www.itu.int/rec/R-REC-P.526/en) | Where the 60 % Fresnel-clearance convention comes from |
| [ITU national frequency allocations](https://www.itu.int/en/ITU-R/terrestrial/fmd/Pages/default.aspx) | The authority for FRA.04's band figures, including Israel's |
| [TI current-sense monitors](https://www.ti.com/amplifier-circuit/current-sense/overview.html) | FEL.05's amplifier and its error sources |

## Regulation

| | |
|---|---|
| [FAA Part 107](https://www.faa.gov/uas/commercial_operators) | The certificate this course teaches |
| [FAA airspace and LAANC](https://www.faa.gov/uas/getting_started/laanc) | 18.04's 2-minutes-versus-30-days |
| [Israeli Civil Aviation Authority](https://www.gov.il/en/departments/civil_aviation_authority) | The rules that actually apply where you fly |
| [`research/faa-drone-regulations-2026-09.md`](research/faa-drone-regulations-2026-09.md) | What was current when the course was written |

## Safety and operations

| | |
|---|---|
| [SKYbrary](https://skybrary.aero/) | Bowties, CRM, errors versus violations — FOP.02 and FOP.03's sources |
| [EASA SORA](https://www.easa.europa.eu/en/domains/civil-drones) | The bowtie formalised into a regulatory route |
| [Google SRE: postmortem culture](https://sre.google/sre-book/postmortem-culture/) | FOP.03's blamelessness arithmetic, from software operations |

## Buying, in Israel

| | |
|---|---|
| [HARDWARE.md](../HARDWARE.md) | What to buy, when, from whom, in ₪ including VAT |
| [`hardware/suppliers-israel.md`](../hardware/suppliers-israel.md) | The supplier list itself |
| [`hardware/importing-to-israel.md`](../hardware/importing-to-israel.md) | The $75 exemption, 18 % VAT, and what not to ship by air |
| [`research/israel-drone-hardware-2026-09.md`](research/israel-drone-hardware-2026-09.md) | The survey the prices came from |

## Books worth owning

| | |
|---|---|
| *Small Unmanned Aircraft: Theory and Practice* — Beard & McLain | The standard text for modules 06, 07 and 12. Free draft chapters are online. |
| *Introduction to Multicopter Design and Control* — Quan Quan | Closer to this course's shape: build, model, control, fly |
| *Probabilistic Robotics* — Thrun, Burgard & Fox | Module 06's estimation, done properly |
| *The ARRL Handbook* | Everything in FRA, and a lifetime of the rest |

## The parallel course

| | |
|---|---|
| [Robotics course](https://github.com/tal-giladi/robotics-course) | Shared fundamentals are cross-referenced rather than re-taught; [00.05](../00-orientation/00.05-relationship-robotics-course.md) maps which is which |
