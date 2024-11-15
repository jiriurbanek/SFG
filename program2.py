import numpy as np
circle = np.loadtxt(open("circle-i-0.5-pi.txt", "rb"), delimiter=",", skiprows=0)
ellipse = np.loadtxt(open("ellipse-i-0.5-a-1.2-b-1-c-0.8333333.txt", "rb"), delimiter=",", skiprows=0)
output = open("difference.txt", 'w')
for row in range(10000):
    a = (- circle[row][1] + ellipse[row][1])
    output.write(str(row)+","+str(a)+"\n")
output.close()
