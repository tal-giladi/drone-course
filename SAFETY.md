# Safety

Read this before the Stage 1 parts arrive. Re-read the relevant section before each stage.

This course has three hazards that can seriously injure you, and one that can burn your house
down. None of them are exotic and all of them are managed by procedure rather than by luck.

| # | Hazard | Where it appears | Worst realistic outcome |
|---|---|---|---|
| 1 | **Spinning propellers** | [02.07](02-motors-escs-props/02.07-static-thrust-test.md), module 04 onward, every flight | Deep lacerations, tendon damage, eye loss |
| 2 | **Lithium-polymer packs** | [03.01](03-power-system/03.01-lipo-chemistry.md) onward, permanently | House fire |
| 3 | **A falling aircraft** | Module 11 onward | Head injury to a bystander |
| 4 | **A released payload** | Module 17, module 19 | Injury to whatever is below |

---

## The five standing rules

These apply from the moment you own a propeller until you stop flying. They are not
stage-specific and there is no situation in this course that justifies breaking one.

1. **Props off for anything that is not a flight.** Configuration, parameter changes, firmware
   flashing, motor-direction tests, first power-up after any wiring change — propellers come
   off. Every one of them can spin a motor.
2. **Safety glasses whenever a propeller can turn.** Including on the bench. Including for
   "just a second".
3. **Never charge a lithium pack unattended, and never on a flammable surface.** LiPo bag,
   concrete floor or a metal tin. Not on the desk, not overnight, not "while I pop out".
4. **Know where the disarm is before you arm.** Physically — which switch, which hand. If you
   have to look for it, you will not find it in time.
5. **Nobody is in the plane of a propeller disc.** Not you, not a bystander, not a pet. Stand
   behind or above, never level with it.

---

## 1. Propellers

A 10-inch propeller at Hermon's full throttle has tips moving at **130 m/s** — 470 km/h. It
will go through skin, tendon and bone before you have registered that it moved.

### What actually causes propeller injuries

Almost never a crash. The three real causes, in order:

1. **An unexpected arm.** A stray transmitter input, a failsafe recovering, a flight controller
   rebooting mid-configuration. This is why rule 1 exists.
2. **Reaching for a moving aircraft.** A drone that is about to tip over is a drone you let tip
   over. It costs ₪100 of parts. Your hand costs more.
3. **Being in the disc plane during a bench test.** See
   [02.07](02-motors-escs-props/02.07-static-thrust-test.md).

### Bench-test procedure

Written out in full in [02.07](02-motors-escs-props/02.07-static-thrust-test.md). The short
version:

- Rig **clamped or bolted** to the bench, never held or weighted.
- Propeller at least **3 diameters (750 mm)** from every surface.
- A **physical barrier** between you and the disc — polycarbonate, plywood, or a doorway.
- **Check the prop nut** before every run: torque, direction, and no cracks.
- Battery and disarm **within reach**, and you know which is which.
- **Outdoors or in a garage.** Not in a room with things you care about.
- Return to idle between test points; do not dwell above 80 % throttle for more than ~10 s.

### Propeller condition

Replace a propeller that has: a visible crack, a chip out of a leading edge, a bent blade, or
any contact with a hard surface at speed. They cost ₪15 a set. A blade that sheds at 9,800 rpm
is an unguided projectile and also an instant, violent imbalance that can tear a motor off an
arm.

### Arming discipline

- Arm only when you intend to fly, standing where you intend to stand.
- Announce it out loud if anyone else is present: **"arming"**.
- Disarm the instant the aircraft is on the ground and you are walking towards it.
- Never walk towards an armed aircraft. Ever.

---

## 2. Lithium-polymer packs

Hermon's pack is **6S 5000 mAh — 111 Wh**. That is roughly the energy of 25 g of TNT, stored in
a soft foil bag with no mechanical protection, capable of releasing it in about thirty seconds
as a 600 °C fire that supplies its own oxygen.

A LiPo fire cannot be smothered and water makes it worse in the short term. **You do not put a
LiPo fire out; you contain it and let it finish.**

### The rules

| Rule | Why |
|---|---|
| **Charge in a LiPo bag, on concrete or in a metal container** | Containment when, not if |
| **Never unattended** | The window between "puffing" and "fire" is about a minute |
| **Never above 4.20 V per cell** | Over-charge is the single most common cause of failure |
| **Never below 3.30 V per cell** | Over-discharge causes internal copper shunts that fail later, in the air |
| **Store at 3.80 V per cell** | A pack left full loses capacity fast and swells |
| **Never charge a pack that is puffed, hot, or has been crashed** | Internal damage may already be in progress |
| **Never charge a pack below 5 °C or above 45 °C** | Lithium plating at low temperature; runaway risk at high |
| **Balance-charge every time** | A cell drifting out of balance is the failure mode you can actually see coming |

### After a crash

Any crash hard enough to break something is hard enough to damage a pack internally.

1. **Do not** put it straight in the car.
2. Disconnect it, inspect it, and put it somewhere fireproof and visible.
3. **Watch it for 30 minutes.** Most post-crash failures happen inside that window.
4. If it is puffed, warm, or smells sweet — it is finished. Discharge it fully through a
   resistive load and dispose of it properly.

### The Israeli summer

A car interior in Tel Aviv in August reaches 60–70 °C. That is above the safe storage
temperature for a LiPo and well above the temperature at which a marginal pack fails.

**Never leave a pack in a parked car.** Carry it in, or plan the flying day around it.
[03.10](03-power-system/03.10-lipo-in-israel.md) covers storage and transport here properly.

### Disposal

Discharge to 0 V through a resistive load (a 12 V car bulb works), then take it to an
electronics-recycling point. Never in household waste.

---

## 3. Flying

### Site selection

Before every flight:

- **A clear area** with a radius of at least 30 m, or the maximum planned altitude, whichever is
  greater.
- **No people** who have not consented to be there, and no people at all downwind or under the
  planned track.
- **No roads, railways, power lines, or livestock** within the fence.
- **Airspace checked.** Module 18 teaches this properly; before then, fly somewhere obviously
  uncontrolled and well away from any airfield.
- **The wind is below your limit.** Hermon's is 6 m/s
  ([`hermon-numbers.md`](references/hermon-numbers.md)). Measure it; do not estimate it.

### Pre-flight

The full checklist is built in
[04.06](04-frame-and-assembly/04.06-preflight-and-airworthiness.md). It is not optional and it
is not from memory — you read it off a card, every time, including the hundredth time.

### The abort

**Write down your abort criteria before you arm**, every flight. They are the conditions under
which you will cut the throttle and accept a broken aircraft. Typical ones: the aircraft leaves
the fence, a motor note changes, the link warning appears, anything approaches the site.

An aircraft is ₪3,000. Deciding in the moment is how people hesitate.

### Failsafes

Configured in [09.03](09-telemetry-datalink/09.03-failsafe-when-the-link-drops.md) and
[12.04](12-autonomous-flight/12.04-rtl-and-the-failsafe-tree.md), and **physically tested**
before they are trusted. A failsafe you have not triggered on purpose is a hypothesis.

---

## 4. Payloads

From module 17, Hermon carries and releases 250 g.

- **The release must be physically incapable of firing while disarmed.** Configure it, then
  prove it by power-cycling with a loaded pod over a padded surface.
- **Never fly a loaded pod over anything you would mind hitting**, including during the tests
  where you are deliberately checking the release.
- **The drop zone is cleared and observed** before every release.
- A released 250 g object from 30 m arrives at about 24 m/s. Treat the area under the aircraft
  as part of the aircraft.
- The spray payload is a **moving mass**: see
  [17.03](17-payloads-delivery/17.03-spray-and-irrigation.md) for why a half-full tank changes
  the handling.

---

## 5. Electrical

- **Solder with ventilation**, and never with the battery connected.
- **Fuse the pack.** Hermon's power tree ([03.04](03-power-system/03.04-power-distribution.md))
  has an inline fuse for exactly one reason: a shorted ESC across a 50 C pack is a 250 A arc.
- **Check polarity twice before the first connection of anything.** Reverse polarity on a 6S
  pack destroys everything downstream instantly.
- **Use an XT60 with an anti-spark resistor, or expect a spark** on every connection. The spark
  is the capacitor bank charging; it is normal, and it slowly erodes the connector.
- **Never work on a powered aircraft.** Disconnect, then work.

---

## When something goes wrong

1. **Stop.** Do not try to save the situation with a faster reaction.
2. **Make it safe**: disarm, disconnect, step back.
3. **Do not touch anything for thirty seconds.** Especially a crashed pack.
4. **Write down what happened while you remember it.** Module 16 turns this into a discipline
   ([16.05](16-testing-analysis/16.05-field-protocols-and-the-safety-case.md)) and module 18
   turns it into an after-action review
   ([18.03](18-civil-ops/18.03-mission-planning-process.md)).

The point of writing it down is not paperwork. It is that the second time something surprises
you, you should already know what it was.
