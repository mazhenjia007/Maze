import math
import numpy as np
import sys

V = np.zeros((12, 12))

hFile = open('V.txt', 'r')
for x in range(12):
    line = hFile.readline()
    arr = line.split(' ')
    arr[len(arr)-1] = arr[len(arr)-1].replace('\n', '')

    for y in range(12):
        V[x][y] = eval(arr[y])

hFile.close()

hFile = open('step.txt', 'w')
for x in range(12):
    for y in range(12):
        if V[x][y]==0:
            sys.stdout.write("***** ")
        else:
            res = math.log(V[x][y]) / math.log(0.95)
            sys.stdout.write("%5.2f " % (res))
    sys.stdout.write("\n")
hFile.close()
