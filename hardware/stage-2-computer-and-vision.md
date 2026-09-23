# Stage 2 — companion computer & vision

**Buy at module 14.** Nothing before module 14 needs it; modules 05–13 run on the Stage 1
aircraft and your laptop.

This is the stage where Hermon stops being a radio-controlled aircraft and starts being a
robot that carries a computer.

## The list

| # | Item | Reference part | Substitute spec | ≈ price | Where | Conf. |
|---|---|---|---|---|---|---|
| 1 | Companion computer | **Raspberry Pi 5, 8 GB** | 4 GB works; 8 GB gives headroom for a detector and ROS 2 together | **₪800** (4 GB ₪500) | **Piitel** | [V] |
| 2 | Active cooler | Official Pi 5 Active Cooler | Any Pi 5 cooler. The Pi throttles under YOLO without one | **₪30** | Piitel | [V] |
| 3 | Storage | NVMe HAT + 256 GB SSD, or a 128 GB A2 microSD | A2-class card minimum; video writes kill cheap cards | ₪140–400 | KSP, Piitel | [V] |
| 4 | Power for the Pi | 5 V 5 A BEC from the 6S pack, **not** a USB power bank | ≥ 5 A continuous, 6S input, with its own ground return | ₪170 | 4Project, Hackstore | [E] |
| 5 | Camera | Raspberry Pi Camera Module 3 (wide) or a USB global-shutter camera | **Global shutter strongly preferred** — see below | ₪180–400 | Piitel | [S] |
| 6 | Gimbal | 2-axis brushless gimbal for a ~40 g camera | Must accept PWM or MAVLink mount control | $70–150 | Import | [E] |
| 7 | Laser rangefinder | Benewake TF-Luna or TFmini-S (12 m) / TF02-Pro (40 m) | I²C or UART, ArduPilot `RNGFND` driver exists | $25–90 | Import | [S] |
| 8 | Cabling & mounts | UART cables, USB-C right-angle, 3D-printed camera tray, vibration grommets | — | ₪100 | Local / print | [E] |

**Cheapest path ≈ ₪1,400** (Pi 5 4 GB, microSD, Pi Camera 3, TF-Luna, no gimbal).
**Recommended ≈ ₪2,600** (Pi 5 8 GB, NVMe, global-shutter camera, 2-axis gimbal, TF02-Pro).

## The one decision that matters: rolling shutter vs global shutter

A rolling-shutter sensor reads the image one row at a time. On a vibrating, translating
aircraft, straight lines come out bent and a 10 m/s survey smears. The Pi Camera Module 3 is
rolling shutter; it is fine for learning and for slow survey work, and it is what most people
start with. A global-shutter camera (the Pi Global Shutter Camera, or an OV9281-class USB
module) costs more and has a smaller sensor, but it is the right answer if your detections
matter at speed. [14.01](../14-vision-perception/14.01-cameras-for-uavs.md) measures the
difference; buy the cheap one first if you are unsure, and upgrade when you have seen the
artefact with your own eyes.

## Why the Pi is powered from a BEC and not a power bank

A USB power bank adds 200–400 g, cannot be monitored by the flight controller, and will cut
out under the Pi 5's inrush. Hermon's power tree
([03.04](../03-power-system/03.04-power-distribution.md)) gives the Pi a dedicated 5 V 5 A
regulator off the 6S pack, with its own return path so the Pi's current does not modulate the
flight controller's ground reference.
[15.01](../15-onboard-autonomy/15.01-companion-architecture.md) covers the isolation rules.

## What this stage unlocks

[05.05](../05-sensors/05.05-flow-and-rangefinders.md) ·
[13.05](../13-navigation-gnss/13.05-degraded-denied-and-spoofed.md) ·
all of module 14 · all of module 15 · module 19 ·
projects [P06](../projects/P06-detection-in-the-air.md),
[P07](../projects/P07-offboard-autonomy.md), [P08](../projects/P08-hermons-mission.md).

## Mass budget warning

Stage 2 adds roughly **250–350 g** to a 1.45 kg aircraft. That is the same order as the
delivery pod. Do the arithmetic in
[04.02](../04-frame-and-assembly/04.02-mass-and-center-of-mass.md) *before* you buy, and check
it against the thrust margin in
[`hermon-numbers.md`](../references/hermon-numbers.md#2-the-powertrain). If Stage 2 and Stage 4
are both fitted, Hermon is near 1.8 kg and the endurance is roughly halved — which is exactly
what [17.01](../17-payloads-delivery/17.01-payload-mass-and-com.md) makes you compute.
