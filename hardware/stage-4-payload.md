# Stage 4 — payload & delivery pod

**Buy at module 17.** Most of this stage is 3D printed, bought at a hardware shop, or already
in your parts bin — it is the cheapest stage in the course and the one you build the most of
yourself.

Hermon's payload is **250 g**, released from a pod under the centre plate. Everything about
what that does to the aircraft is derived in
[17.01](../17-payloads-delivery/17.01-payload-mass-and-com.md) and
[17.04](../17-payloads-delivery/17.04-release-dynamics.md).

## The release mechanism

Pick one. The course builds the servo version in
[17.06](../17-payloads-delivery/17.06-building-hermons-pod.md) and tests the others on the bench.

| Option | Part | Hold force | Release time | ≈ price | Verdict |
|---|---|---|---|---|---|
| **Servo latch** (built in 17.06) | Metal-gear micro servo (MG90S class) + printed latch | 1–2 kg with a proper over-centre geometry | 60–120 ms | ₪40 | **Recommended.** Cheap, obvious, inspectable, fails closed |
| Electro-permanent magnet | EPM v3 or similar | 3–5 kg | < 20 ms | $45 | Fastest and cleanest, but needs a steel plate on the payload and its own power |
| Pin puller | Solenoid + printed pin | 2 kg | 30 ms | ₪80 | Jams if the load side is pre-tensioned; a good lesson in why |

## The list

| # | Item | Spec | ≈ ₪ | Where | Conf. |
|---|---|---|---|---|---|
| 1 | Micro servo, metal gear | MG90S or better, 5 V from the FC's servo rail | 40 | Hackstore, AliExpress | [E] |
| 2 | Printed pod + latch + practice payloads | PLA or PETG. Print 4 pods so you can fly four sorties per print run | 60 (filament) | Print at home, a print farm, or a makerspace | [E] |
| 3 | Payload mass | 250 g of something inert and cheap — sand, water, steel shot | 0 | — | — |
| 4 | Mounting hardware | M3 standoffs, nylon screws (they shear instead of bending the frame) | 30 | 4Project | [E] |
| 5 | Servo extension + signal wire to an AUX output | — | 20 | Hackstore | [E] |
| **Spray option** | | | | | |
| 6 | Diaphragm pump, 5–12 V | 1–2 L/min, self-priming | 80 | AliExpress | [E] |
| 7 | Tank | 500 mL bottle with a baffle. **A baffle is not optional** — see below | 20 | — | [E] |
| 8 | Nozzle | Hollow-cone, 0.3–0.5 mm, or a pair of flat-fan nozzles on a short boom | 40 | Agricultural supply | [E] |
| 9 | Tubing + fittings | 4 mm silicone | 25 | Hardware shop | [E] |

**Cheapest path ≈ ₪250** (servo release + printed pods only).
**Recommended ≈ ₪600** (release + spray kit + a spare servo + a second pod set).

## Two warnings the lessons will repeat

**The tank needs a baffle.** A half-full 500 mL tank in a banked turn is 250 g of mass sliding
to one side at exactly the moment the controller is trying to hold an angle. It shows up as a
low-frequency attitude wobble that no amount of PID tuning fixes.
[17.03](../17-payloads-delivery/17.03-spray-and-irrigation.md) shows the log signature.

**The release must be physically incapable of firing while disarmed.** A servo latch that
opens when the flight controller boots, or when a stray PWM frame arrives, will drop 250 g on
whatever is under the aircraft in the workshop. ArduPilot's servo output parameters give you
a safe disarmed position; use it, and then test it by power-cycling with a loaded pod over a
padded surface. [17.02](../17-payloads-delivery/17.02-release-mechanisms.md) is where that
gets designed properly.

## Printing it

If you do not own a printer, the robotics course's Israeli print options apply: a local print
farm charges ₪8–13 for small parts, and community makerspaces are free.
A Bambu Lab A1 mini is ≈ ₪900 if you decide you want one — it is optional for this course
and useful for the rest of your life.

## What this stage unlocks

All of [module 17](../17-payloads-delivery/README.md) ·
[19.04](../19-capstone-hermon-mission/19.04-phase-3-delivery-and-precision-rtl.md) ·
project [P08](../projects/P08-hermons-mission.md).
