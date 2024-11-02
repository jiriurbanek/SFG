import numpy as np
import math
from numba import jit
def shapeCase(a, b, c):
# returns 1 if planet is spherical
    assert a > 0
    assert b > 0
    assert c > 0
    if a == b and b == c:
        return 1
    else:
        return 0
def relativePositions(m1, m2, G, r, i, time):
# returns coordinates of the system in time, 1 is star and 2 is planet, G is gravitational
# constant, r is relative distance, i is inclination such that for i = 0 no transit is
# to be seen and for i = 0.5*pi the planet transits across the star's center
# time is the time interval that has passed
    omega = (1.0/r)* math.sqrt(G * (m1+m2)/r)
    k = r*m1/(m2+m1)
    x1 = -k*np.cos(omega*time)
    y1 = k*np.cos(i)*np.sin(omega*time)
    x2 = k*np.cos(omega*time)
    y2 = -k*np.cos(i)*np.sin(omega*time)
    return x1, y1, x2, y2

def ellipseParameters(a, b, c, i, omega, time, phasezero):
# Takes semi axes, inclination, orbital velocity, time passed and phase as parameters
# and outputs transformed axes and angle between y-axis.
    if shapeCase(a, b, c):
        return a, a, 0
    alpha = phasezero + omega*time - 0.5*np.pi
    A = (np.sin(alpha)/a)**2 + (np.cos(alpha)/b)**2
    B = (np.cos(alpha)*np.cos(i)/a)**2 + (np.sin(alpha)*np.cos(i)/b)**2 + (np.sin(i)/c)**2
    C = ((1/a)**2 - (1/b)**2)*np.sin(2*alpha)*np.cos(i)
    aprime = -(math.sqrt(-2*(C**2 - 4*A*B)*(A + B - math.sqrt((A - B)**2 + C**2))))/(C**2-4*A*B)
    bprime = -(math.sqrt(-2*(C**2 - 4*A*B)*(A + B + math.sqrt((A - B)**2 + C**2))))/(C**2-4*A*B)
    phi = 0.5*np.arctan2(-C, B-A)
    return aprime, bprime, phi

def circleOverlap(r1, r2, x1, y1, x2, y2):
    x = 0.0
    y = 0.0
    phi1 = 0.0
    phi2 = 0.0
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
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


def timePosition(m1, r1, m2, a, b, c, phasezero, i, r, G, number):
# This function takes mass and radius of star m1 and r1, mass and semi-axes of planet
# m2, a, b, and c, its rotation phase at zero orbital phase phasezero, inclination of
# orbit i, distance between star and planet r, gravitational constant G and number of
# iterations number
    omega = (1/r)*math.sqrt(G * (m1+m2)/r)
    period = (1*np.pi)/omega # so that we don't have to model the transit curve behind
# the star and we only calculate half of it
    itime = period/number # this is iteration time
    output = open('output-ellipse.txt', 'w')
    for j in range (number):
# Count only ids with nonzero overlap, for zeros plot 4ish points
        X1, Y1, X2, Y2 = (relativePositions(m1, m2, G, r, i, j*itime))
        A, B, Phi = (ellipseParameters(a, b, c, i, omega, j*itime, phasezero))
        text = j, r1, r1, X1, Y1, 0.0, A, B, X2, Y2, Phi, "\n"
        output.write(" ".join(map(str, text)))
    output.close()

timePosition(8, 2, 1, 1, 1.5, 0.3, 0, 0, 10, 1, 100)
