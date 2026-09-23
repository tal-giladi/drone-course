# Software/simulation stack — version check, 2026-09-20

Checked 2026-09-20. "verified" = release page/feed opened; "snippet" = seen only in search
results. The course baseline is ArduPilot + Ubuntu 24.04 (WSL2) + ROS 2 Jazzy (shared with the
robotics course).

| Item | Version | Date | Status | Evidence |
|---|---|---|---|---|
| ArduPilot (stable) | **4.7.0** | stable tree live on firmware.ardupilot.org | verified | [firmware.ardupilot.org stable-4.7.0](https://firmware.ardupilot.org/Plane/stable-4.7.0/Pixhawk6C/), [GitHub releases](https://github.com/ArduPilot/ardupilot/releases) |
| ArduPilot (dev) | master | continuous | snippet | [ReleaseNotes.txt](https://github.com/ArduPilot/ardupilot/blob/master/ArduCopter/ReleaseNotes.txt) |
| QGroundControl | **5.1.4** (5.1.x line, docs "Stable_V5.1") | 2026 | verified | [newreleases v5.1.4](https://newreleases.io/project/github/mavlink/qgroundcontrol/release/v5.1.4), [QGC docs Stable_V5.1](https://docs.qgroundcontrol.com/Stable_V5.1/zh/qgc-user-guide/getting_started/download_and_install.html) |
| Mission Planner | **1.3.83** (latest stable, 2025-09-10); dev builds active 2026-09-17 | 2025-09 / 2026-09 | verified | [GitHub releases atom feed](https://github.com/ArduPilot/MissionPlanner/releases.atom) |
| ExpressLRS | **4.1.0** (4.x line; 3.6.4 also maintained) | 2026 | verified | [ExpressLRS 4.1.0](https://newreleases.io/project/github/ExpressLRS/ExpressLRS/release/4.1.0#1#1), [3.6.4](https://newreleases.io/project/github/ExpressLRS/ExpressLRS/release/3.6.4) |
| ultralytics YOLO | **YOLO26** (2026 line; "edge-first", PyTorch 2.x) | 2026 | snippet | [Ultralytics press release](https://www.ultralytics.com/news/ultralytics-redefines-state-of-the-art-vision-ai-with-yolo26#1), [YOLO26 blog](https://www.ultralytics.com/blog/ultralytics-yolo26-the-new-standard-for-edge-first-vision-ai#1) |
| JMAVSim | community-supported, still in PX4 + ArduPilot SITL docs | 2025–26 | snippet | [PX4 sim_jmavsim docs](https://github.com/PX4/PX4-Autopilot/blob/d31c6923475eb10dac21c27e33adc4d23b77e63c/PX4-Autopilot/docs/en/sim_jmavsim/index.md?plain=1#1), [community simulators list](https://raw.githubusercontent.com/PX4/PX4-user_guide/921bbdfc48592f195deb34b8fd0552075769b635/en/simulation/community_supported_simulators.md#1) |
| ROS 2 ↔ ArduPilot bridge | **MAVROS** (mavlink/mavros) is the active gateway; ArduPilot ships `ardupilot_gazebo` for Gazebo; `mavlink2ros` = legacy | 2026 | snippet | [mavlink/mavros](https://github.com/mavlink/mavros#1), [mavros on index.ros.org](https://index.ros.org/r/mavros/#foxy), [community ROS2 Humble + MAVROS + ArduPilot framework](https://github.com/sidharthmohannair/ros2-ardupilot-sitl-hardware#1) |
| Gazebo | Harmonic (ROS 2 Jazzy pairing, EOL 2029-05) — same as robotics course | — | verified (robotics course 2026-09-16) | `robotics-course/curriculum/versions.yaml` |
| Aeroflight / AirSim / Unity | not re-checked this pass — mark **pending** before module 10 | — | pending | — |
| uavlog | active, part of ArduPilot Methodic Tuning workflow — **pending** exact release | — | pending | — |
| mavsdk / pymavlink | latest 2026 releases — **pending** | — | pending | — |

## Surprises (course-relevant)

1. **QGC is on the 5.x line** (5.1.4) — the robotics-era assumption of "QGC 2.x/3.x" is stale;
   QGC 5.1 UI/docs links must be used in lessons 08.06, 12.02.
2. **Mission Planner stable is a year old (1.3.83, 2025-09)** but dev builds ship weekly
   (2026-09-17). Lesson 08.06 should pin "stable 1.3.83, dev available" and prefer stable.
3. **ELRS 4.1** is current — lessons 09.02/09.03 should reference 4.x firmware and note the 3.6.x
   long-term line for older hardware.
4. **YOLO26** is the current Ultralytics release — lesson 14.05 must not pin YOLO11; use
   "YOLO26 (current), 11 as fallback".
5. **ROS 2 bridge:** MAVROS remains the practical ArduPilot↔ROS 2 gateway on Jazzy; the course
   pattern (SITL → hardware with the same MAVROS nodes) is proven by community projects.

## Open items before module 10/15 lessons are written

- Exact current uavlog tag, mavsdk/pymavlink versions (one fetch pass).
- Aeroflight status/pricing; AirSim maintenance status (for 10.08 and 18.08).
- ArduPilot 4.7 release-notes highlights (breaking changes vs 4.5/4.6) — fetch
  ArduCopter/ReleaseNotes.txt head when writing 08.01/08.11.
