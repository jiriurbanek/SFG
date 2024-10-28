import numpy as np
from numba import jit
import math

@jit
def circleOverlap(r1, r2, d):
    assert (r1 > r2)
    assert (r1 > 0.0)
    assert (r2 > 0.0)
    assert (d > 0.0)
    x = 0.0
    y = 0.0
    phi1 = 0.0
    phi2 = 0.0
    A = 0.0
    if (r1 < (r2 + d)) and (d < r1 + r2):
        x = (r1*r1 - r2*r2 + d*d)/(2.0*d)
        y = math.sqrt(r1*r1 - x*x)
        phi1 = 2.0*np.arcsin(y/r1)
        if (x < d):
            phi2 = 2.0*np.arcsin(y/r2)
        if (x > d):
            phi2 = 2.0*np.pi - 2.0*np.arcsin(y/r2)
        if (x == d):
            phi2 = np.pi
        A = (np.pi*r1*r1 - phi1*r1*r1/2 - phi2*r2*r2/2 + d*y) / (np.pi*r1*r1)
    if (r1 >= (d + r2)):
        A = 1.0 - (r2*r2)/(r1*r1)
    if (d >= (r1 + r2)):
        A = 1.0
    return A
@jit
def apparentDistance(m1, m2, G, r, i, time):
    omega = (1.0/r) * math.sqrt(G * (m1+m2)/r)
    xp = r*(m2/(m2+m1)) * np.cos(omega * time)
    yp = -1.0 * r*(m2/(m2+m1)) * np.sin(omega * time) * np.sin(i)
    xs = -1.0 * r*(m1/(m2+m1)) * np.cos(omega * time)
    ys = r*(m1/(m2+m1)) * np.sin(omega * time) * np.sin(i)
    R = math.sqrt((xp - xs)**2 + (yp - ys)**2)
    return R
@jit
def timeFunction(m1, m2, r1, r2, r, i, G, number):
    omega = (1.0/r) * math.sqrt(G * (m1+m2)/r)
    period = (1.0*np.pi)/omega
    itime = period/number
    for j in range (number):
        print(circleOverlap(r1, r2, apparentDistance(m1, m2, G, r, i, j*itime)))
    return 1

timeFunction(8.0, 1.0, 2.0, 1.0, 10.0, 0.1, 1.0, 10000000)
