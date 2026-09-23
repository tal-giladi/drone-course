import math, random
RHO = 1.225
D = 10 * 0.0254
D4, D5 = D**4, D**5
CT, CP = 0.0985, 0.045
ETA = 0.80
random.seed(7)
print("MEASURED = [")
print("    # thr%   rpm   grams   amps   volts")
for thr, rpm in ((20, 2010), (30, 3020), (40, 4010), (50, 5030), (60, 5980),
                 (70, 6960), (80, 7890), (90, 8820), (100, 9740)):
    n = rpm / 60
    t_n = CT * RHO * n * n * D4
    grams = t_n / 9.81 * 1000
    p_shaft = CP * RHO * n**3 * D5
    p_elec = p_shaft / ETA
    # pack sag: 25.0 V open circuit, 0.04 ohm x 4 motors sharing
    for _ in range(30):
        i_total = 4 * p_elec / (25.0 - 0.0)
    v = 25.0
    for _ in range(40):
        i = p_elec / v
        v = 25.0 - 0.04 * (i * 4) - 0.0
    i = p_elec / v + 0.5  # no-load current
    grams_m = round(grams * random.uniform(0.985, 1.015))
    i_m = round(i * random.uniform(0.98, 1.02), 1)
    print(f"    ({thr:3d}, {rpm:6d}, {grams_m:6d}, {i_m:5.1f}, {v:5.2f}),")
print("]")
