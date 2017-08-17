import numpy as np
import Maze_AGNT
import Maze_ENV
import Maze_Train
import math
import sys

"""
V = np.zeros((12, 12))
gamma = 0.95

ps, UV = Maze_AGNT.ExecEpi(V, gamma, 1)

sys.stdout.write("%d\n" % len(ps))

cnt = np.zeros((12, 12))
for i in range(len(ps)):
    x = ps[i].x
    y = ps[i].y
    cnt[x][y] += 1

for x in range(12):
    for y in range(12):
        sys.stdout.write("%4d " % cnt[x][y])
    sys.stdout.write("\n")
"""

V = Maze_Train.Maze_Train()

sys.stdout.write("\n")

for x in range(12):
    for y in range(12):
        sys.stdout.write("%6.4f " % V[x][y])
    sys.stdout.write("\n")
