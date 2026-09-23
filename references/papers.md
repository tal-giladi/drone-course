# Papers

Primary sources behind the models in this course — the places to go when a lesson's simplification
stops being enough.

Each entry says **which lesson** it sits under and **what it gives you that the lesson does not**.
Nothing here is required reading; all of it is the next step if a particular model becomes your
problem rather than your background.

> [!NOTE]
> Titles and authors are given rather than links wherever a stable link does not exist. Several of
> these are standards or textbook chapters rather than journal papers, which is normal for this
> field: most of the useful UAV literature is in standards, theses and firmware source.

## Aerodynamics and propulsion

**Momentum theory and the actuator disk** — any rotorcraft text, e.g. Leishman, *Principles of
Helicopter Aerodynamics*, ch. 2.
*Under [01.06](../01-flight-physics/01.06-momentum-theory.md) and
[FA.02](../optional-foundations/flight-aerodynamics/FA.02-newtons-laws-flight.md).* Gives the factor
of two in the far wake that FA.02 makes explicit, and the assumptions under which induced power is
`T^1.5 / √(2ρA)`.

**Propeller performance databases** — UIUC Propeller Data Site.
*Under [02.05](../02-motors-escs-props/02.05-propellers.md) and
[02.06](../02-motors-escs-props/02.06-prop-motor-matching.md).* Measured thrust and power
coefficients for small propellers, which is the honest version of the curve a manufacturer prints.

**Ground effect for rotors** — Cheeseman & Bennett's correction.
*Under [01.11](../01-flight-physics/01.11-ground-effect.md).* Where the "one rotor diameter" rule of
thumb comes from and how badly it degrades.

## Estimation

**Kalman, R. E. (1960), "A New Approach to Linear Filtering and Prediction Problems"** — the original.
*Under [06.03](../06-state-estimation/06.03-kalman-from-scratch.md).* Short, readable, and worth
seeing once in its own notation.

**Thrun, Burgard & Fox, *Probabilistic Robotics*** — chapters 2–4.
*Under [06.01](../06-state-estimation/06.01-why-estimation.md) to
[06.04](../06-state-estimation/06.04-ekf-nonlinear.md).* The clearest treatment of why an estimator
is a belief rather than a measurement.

**ArduPilot EKF3 source and documentation** — `AP_NavEKF3`.
*Under [06.05](../06-state-estimation/06.05-ekf3-in-ardupilot.md).* The actual filter your aircraft
runs, which is the only one whose behaviour you can check against a log.

## Control

**Mellinger & Kumar (2011), "Minimum Snap Trajectory Generation and Control for Quadrotors"**.
*Under [07.05](../07-control/07.05-velocity-position-and-modes.md) and
[12.02](../12-autonomous-flight/12.02-mission-planning.md).* Why differential flatness makes
quadrotor trajectory generation tractable, and where the course's simpler waypoint model stops.

**Bouabdallah & Siegwart (2005), "Backstepping and Sliding-mode Techniques Applied to an Indoor
Micro Quadrotor"**.
*Under [07.02](../07-control/07.02-cascaded-loops.md).* The comparison that explains why a cascaded
PID remains the practical choice despite better-performing alternatives.

**Ziegler & Nichols (1942), "Optimum Settings for Automatic Controllers"**.
*Under [07.01](../07-control/07.01-pid-for-flight.md).* Mostly of historical interest, and useful
for seeing how old the tuning-by-provocation method is.

## Navigation and GNSS

**Misra & Enge, *Global Positioning System: Signals, Measurements and Performance***.
*Under [13.01](../13-navigation-gnss/13.01-gnss-fundamentals.md) to
[13.03](../13-navigation-gnss/13.03-rtk-and-ppk.md), and
[FGL.04](../optional-foundations/gnss-navigation-math/FGL.04-satellite-geometry-and-error.md).* The
standard reference for the error budget and the geometry matrix FGL.04 builds.

**NGA, *Department of Defense World Geodetic System 1984*** (NGA.STND.0036).
*Under [FGL.01](../optional-foundations/gnss-navigation-math/FGL.01-earth-coordinates-and-datums.md).*
Where `a` and `1/f` come from, and more readable than its title suggests.

**Klobuchar (1987), "Ionospheric Time-Delay Algorithm for Single-Frequency GPS Users"**.
*Under [13.02](../13-navigation-gnss/13.02-error-sources.md).* The broadcast ionospheric model, which
is the one term in the budget your receiver actually tries to remove.

**RTCM SC-104 standard** — differential and RTK correction formats.
*Under [13.03](../13-navigation-gnss/13.03-rtk-and-ppk.md).* What is actually on the correction link.

## Radio

**ITU-R P.526** — propagation by diffraction.
*Under [FRA.02](../optional-foundations/rf-datalink/FRA.02-link-budget-math.md).* The source of the
60 % Fresnel-clearance convention, with the diffraction losses that justify it.

**ITU-R P.525** — free-space propagation.
*Under FRA.02.* The formal version of `(4πd/λ)²`, including the aperture argument FRA.02 stresses.

**Rappaport, *Wireless Communications: Principles and Practice*** — ch. 4.
*Under FRA.02's Level 3.* The two-ray model and its breakpoint, done properly rather than as a floor.

**Semtech, *LoRa Modulation Basics* (AN1200.22)**.
*Under [FRA.01](../optional-foundations/rf-datalink/FRA.01-rf-in-45-minutes.md) and
[FRA.04](../optional-foundations/rf-datalink/FRA.04-protocols-and-bands.md).* How a receiver decodes
6 dB below the noise floor, which FRA.01 uses and does not derive.

## Vision and perception

**Redmon et al. (2016), "You Only Look Once: Unified, Real-Time Object Detection"**.
*Under [14.04](../14-vision-perception/14.04-detection-in-the-air.md).* The architecture family the
course uses, and the paper that made real-time detection on an aircraft plausible.

**Zhang (2000), "A Flexible New Technique for Camera Calibration"**.
*Under [14.02](../14-vision-perception/14.02-field-calibration.md).* The calibration every toolchain
implements.

**Hartley & Zisserman, *Multiple View Geometry in Computer Vision*** — chapters 6 and 9.
*Under [14.05](../14-vision-perception/14.05-tracking-and-geolocation.md).* The projection and ray
intersection behind pixel-to-ground geolocation.

## Safety and operations

**Reason, J. (1990), *Human Error*** — and the error/violation distinction.
*Under [FOP.03](../optional-foundations/civil-ops/FOP.03-debrief-and-aar.md).* The basis for where
blamelessness stops.

**JARUS, *Specific Operations Risk Assessment (SORA)***.
*Under [FOP.02](../optional-foundations/civil-ops/FOP.02-risk-management-bowtie.md) and
[16.05](../16-testing-analysis/16.05-field-protocols-and-the-safety-case.md).* The bowtie turned into
a regulatory method, and the closest thing to a standard shape for a drone safety case.

**NUREG/CR-5485, *Guidelines on Modeling Common-Cause Failures in PRA***.
*Under FOP.02's Level 3.* The beta-factor model, from the industry that had to take it seriously
first.

**Clopper & Pearson (1934), "The Use of Confidence or Fiducial Limits Illustrated in the Case of the
Binomial"**.
*Under [19.05](../19-capstone-hermon-mission/19.05-the-campaign-and-the-report.md).* Where "eight of
ten means 49 % to 94 %" comes from.

## Batteries

**Doyle, Fuller & Newman (1993), "Modeling of Galvanostatic Charge and Discharge of the
Lithium/Polymer/Insertion Cell"**.
*Under [FEL.03](../optional-foundations/drone-electronics-power/FEL.03-lipo-deep-dive.md).* Why the
discharge curve has the shape it does, and why 0.14 V per cell covers 40 % of the energy.

**Peukert's law, and why it barely applies to LiPo**.
*Under [03.09](../03-power-system/03.09-endurance-prediction.md).* Useful as a contrast: the
correction that matters for lead-acid is nearly negligible here, and knowing why is worth ten
minutes.
