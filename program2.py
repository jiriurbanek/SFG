import subprocess
import numpy as np
subprocess.run(["./overlap", "100000-ellipses.txt", "choice", "2"])
subprocess.run(["sed", "-i", r"s/ \+/,/g", "results.txt"])
import numpy as np
array = np.loadtxt(open("results.txt", "rb"), delimiter=",", skiprows=1)
output = open("results2.txt", 'w')
for row in range(len(array)):
    a = (array[row][1] - array[row][4])/array[row][1]
    output.write(str(row)+","+str(a)+"\n")
output.close()
