import numpy as np
import solvers
import scipy as sp

def ellipseSegment(x1, y1, x2, y2, A, B, h, k, phi):
    x1Prime = np.cos(phi) * (x1 - h) + np.sin(phi) * (y1 - k)
    x2Prime = np.cos(phi) * (x2 - h) + np.sin(phi) * (y2 - k)
    y1Prime = -1*np.sin(phi) * (x1 - h) + np.cos(phi) * (y1 - k)
    y2Prime = -1*np.sin(phi) * (x2 - h) + np.cos(phi) * (y2 - k)
    Phi1 = 0.0
    Phi2 = 0.0
    Phi1Roof = 0.0
    if y1Prime >= 0:
        Phi1 = np.arccos(x1Prime / A)
    if y2Prime < 0:
        Phi1 = 2*np.pi - np.arccos(x1Prime / A)
    if y2Prime >= 0:
        Phi2 = np.arccos(x2Prime / A)
    if y2Prime < 0:
        Phi2 = 2*np.pi - np.arccos(x2Prime / A)
    if Phi1 <= Phi2:
        Phi1Roof = Phi1
    if Phi1 > Phi2:
        Phi1Roof = Phi1 - 2*np.pi
    area = ((Phi2 - Phi1Roof) * A * B / 2) + (np.sign(Phi2 - Phi1Roof - np.pi) / 2) * np.abs(x1 * y2 - x2 * y1)
    print(Phi1Roof)
    return area

def ellipseCase(AA1, BB1, CC1, DD1, EE1, FF1, AA2, BB2, CC2, DD2, EE2, FF2):
    A = np.array([[AA1, BB1/2, DD1/2,], [BB1/2, CC1, EE1/2], [DD1/2, EE1/2, FF1]])
    B = np.array([[AA2, BB2/2, DD2/2,], [BB2/2, CC2, EE2/2], [DD2/2, EE2/2, FF2]])

    d = AA1 * (CC1 * FF1 - EE1 * EE1) - (CC1 * DD1 * DD1 - 2*BB1 * DD1* EE1 + FF1 * BB1 * BB1)
    a = 1/d* (AA1 * (CC1 * FF2 - 2*EE1 * EE2 + FF1 * CC2) + 2*BB1 * (EE1 * DD2 - FF1 * BB2 + DD1* EE2) + 2*DD1 * (EE1 * BB2 - CC1 * DD2) - (BB1 * BB1 * FF2 + DD1 * DD1 * CC2 + EE1 * EE1 * AA2) + (CC1 * FF1 * AA2))
    b = 1/d* (AA1 * (CC2 * FF2 - EE2 * EE2) + 2*BB1 * (EE2 * DD2 - FF2 * BB2) + 2*DD1* (EE2 * BB2 - CC2 * DD2) + CC1 * (AA2 * FF2 - DD2 * DD2) + 2*EE1 * (BB2 * DD2 - AA2 * EE2) + FF1 * (AA2 * CC2 - BB2 * BB2))
    c = 1/d* (AA2 * (CC2 * FF2 - EE2 * EE2) - (BB2 * BB2 - FF2 - 2*BB2 * DD2 * EE2 + DD2 * DD2 * CC2))
    s = solvers.solve_cubic(a, b, c)
    s1 = s[0]
    s2 = s[1]
    s3 = s[2]
    s4 = -27*c**3 + 18*c*a*b + a*a*b*b - 4*a**3*c - 4*b**3
