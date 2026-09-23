# Labs

Short, self-contained bench exercises. **Not** projects, and **not** lessons.

A lab is something you can do at a table in under an hour, usually with the aircraft powered down,
that answers one question with a measurement. They exist because some numbers in this course are far
more convincing when you have seen them on your own meter than when you have read them.

## Where the labs actually live

Every lab in this course is embedded in the lesson that needs it — under **Practical challenge**, or
as a `[build]`-tagged exercise. This page is the index, so you can find a bench session without
re-reading a module.

## Power and electronics

| Lab | In | Measures | Why it is worth an hour |
|---|---|---|---|
| Static thrust test | [02.07](../02-motors-escs-props/02.07-static-thrust-test.md) | thrust vs throttle vs current | your motor's real curve, not the datasheet's |
| Pack capacity, honestly | [03.07](../03-power-system/03.07-charging-balancing-storage.md) | delivered Wh vs the label | the label is a best case at a low current |
| Cell drift under load | [FEL.03](../optional-foundations/drone-electronics-power/FEL.03-lipo-deep-dive.md) | per-cell voltage | at 0.60 V of drift the pack alarm stops protecting the weakest cell |
| BEC efficiency | [FEL.02](../optional-foundations/drone-electronics-power/FEL.02-dc-power-math.md) | watts in vs watts out | a linear BEC wastes 38.8 W where a switcher wastes 2.0 |
| Connector temperature | [FEL.05](../optional-foundations/drone-electronics-power/FEL.05-wiring-fuses-and-measurement.md) | ΔT at a known current | 16 % of the watts, 2.3× the temperature |
| Current-sensor calibration | [FEL.05](../optional-foundations/drone-electronics-power/FEL.05-wiring-fuses-and-measurement.md) | logged mAh vs charger mAh | a 10 % error here is 10 % on every endurance figure you quote |

## Sensors and estimation

| Lab | In | Measures |
|---|---|---|
| Gyro and accelerometer noise | [05.02](../05-sensors/05.02-imu.md) | the noise floor your D term has to live with |
| Compass interference | [05.03](../05-sensors/05.03-compass-and-baro.md) | how far current draw moves your heading |
| Vibration survey | [04.04](../04-frame-and-assembly/04.04-mounting-and-vibration.md) | where the resonances are, before you fly |
| GNSS cold and warm start | [05.04](../05-sensors/05.04-gnss-receiver.md) | time to first fix, in your own sky |
| Calibration, proven | [05.06](../05-sensors/05.06-noise-bias-and-calibration.md) | that each calibration improved something measurable |

## Radio

| Lab | In | Measures |
|---|---|---|
| Antenna identification | [FRA.01](../optional-foundations/rf-datalink/FRA.01-rf-in-45-minutes.md) | what band a mystery whip is cut for |
| EIRP arithmetic | [FRA.01](../optional-foundations/rf-datalink/FRA.01-rf-in-45-minutes.md) | whether your setup is legal |
| SWR in flight configuration | [FRA.03](../optional-foundations/rf-datalink/FRA.03-antennas-and-polarisation.md) | not on the bench — the ground is part of the antenna |
| Spectrum survey | [09.05](../09-telemetry-datalink/09.05-spectrum-and-regulation.md) | what else is transmitting at your site |

## Mechanical

| Lab | In | Measures |
|---|---|---|
| Mass budget and centre of mass | [04.02](../04-frame-and-assembly/04.02-mass-and-center-of-mass.md) | the knife-edge check |
| Pod mount load test | [17.06](../17-payloads-delivery/17.06-building-hermons-pod.md) | the landing case: 40 N, 16× hover thrust |
| Release-mechanism cycling | [17.02](../17-payloads-delivery/17.02-release-mechanisms.md) | whether it still releases after 500 cycles |

## Software, no hardware

| Lab | In | Measures |
|---|---|---|
| A quad simulator in Python | [10.02](../10-simulation/10.02-quad-sim-in-python.md) | your own model, before ArduPilot's |
| SITL failure injection | [16.04](../16-testing-analysis/16.04-failure-injection-and-ci.md) | that the failsafe you configured is the one that fires |
| Log forensics | [16.03](../16-testing-analysis/16.03-reading-flight-logs.md) | the fixed order in which to open a log |

## Bench safety

> [!WARNING]
> Two things on this page will hurt you: **a spinning propeller** and **a lithium pack**. Props come
> off for every bench lab that does not specifically need them, and they go back on last. Packs are
> never charged or tested unattended, never outside a fire-resistant container, and never near
> anything you would mind losing. [SAFETY.md](../SAFETY.md) has the standing rules, and they apply at
> a table exactly as they do at a field.

> [!CAUTION]
> Never power a transmitter with its antenna disconnected. FRA.03's Level 4: with no antenna, 100 %
> of the output returns into the amplifier, and the result is a dead radio rather than a weak signal.

## Keeping lab results

Lab results are evidence, and the same rule applies as to projects: **write down the conditions**. A
thrust curve without its battery voltage, or a noise floor without the frame it was measured on, is a
number you cannot use again.
