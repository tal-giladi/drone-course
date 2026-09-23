"""Solve the motor-propeller equilibrium for Hermon, to pick the KV."""
import math

RHO = 1.225
D = 10 * 0.0254
D4, D5 = D ** 4, D ** 5
CT = 0.095          # static thrust coefficient, cheap 10x4.5x3 nylon
CP = 0.055          # static power coefficient
CQ = CP / (2 * math.pi)
R_M = 0.09          # ohm, motor resistance
I0 = 0.5            # A, no-load current
V_PACK = 22.2


def thrust_n(n):
    return CT * RHO * n * n * D4


def torque_nm(n):
    return CQ * RHO * n * n * D5


def solve_n(kv, throttle):
    """rpm where the motor's available voltage equals what the prop demands."""
    kt = 9.5493 / kv
    v = V_PACK * throttle
    lo, hi = 1.0, 500.0
    for _ in range(200):
        n = (lo + hi) / 2
        i = torque_nm(n) / kt + I0
        v_need = n * 60 / kv + i * R_M
        if v_need < v:
            lo = n
        else:
            hi = n
    n = (lo + hi) / 2
    i = torque_nm(n) / kt + I0
    return n, i, v * i


HOVER_T = 1.20 * 9.81 / 4
print(f"hover thrust per motor: {HOVER_T:.2f} N")
n_h = math.sqrt(HOVER_T / (CT * RHO * D4))
print(f"hover rpm (from Ct)   : {n_h * 60:.0f} rpm = {n_h:.1f} rev/s")
print(f"blade-pass (3 blades) : {n_h * 3:.0f} Hz")
print(f"tip speed             : {2 * math.pi * n_h * D / 2:.0f} m/s  Mach {2 * math.pi * n_h * D / 2 / 343:.2f}")

print(f"\n{'KV':>5s} {'hover thr%':>11s} {'full rpm':>9s} {'full I':>7s} {'full T/motor':>13s} {'T/W @1.2kg':>11s} {'hover W':>8s}")
for kv in (400, 470, 550, 700, 900):
    # find throttle where thrust == hover thrust
    lo, hi = 0.01, 1.0
    for _ in range(200):
        t = (lo + hi) / 2
        n, i, p = solve_n(kv, t)
        if thrust_n(n) < HOVER_T:
            lo = t
        else:
            hi = t
    t_hover = (lo + hi) / 2
    n_hv, i_hv, p_hv = solve_n(kv, t_hover)
    nf, i_f, p_f = solve_n(kv, 1.0)
    tf = thrust_n(nf)
    print(f"{kv:5d} {t_hover * 100:10.0f}% {nf * 60:9.0f} {i_f:6.1f}A "
          f"{tf / 9.81 * 1000:10.0f} g {4 * tf / (1.2 * 9.81):10.2f} "
          f"{4 * p_hv:7.0f}")

print("\nDetail for KV470:")
for t in (0.3, 0.4, 0.45, 0.5, 0.6, 0.8, 1.0):
    n, i, p = solve_n(470, t)
    print(f"  throttle {t*100:3.0f}% : {n*60:6.0f} rpm  {thrust_n(n)/9.81*1000:6.0f} g  "
          f"{i:5.1f} A  {p:6.1f} W/motor  {4*p+10:6.0f} W total")
