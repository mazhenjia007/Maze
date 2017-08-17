import Maze_ENV
import Maze_AGNT
import numpy as np
import sys
import copy

def clone(V1, V2, n, m):
    for i in range(n):
        for j in range(m):
            V1[i][j] = V2[i][j]

def Maze_Train():
    hENV = Maze_ENV.TM_ENV()
    
    V = np.zeros((hENV.height, hENV.width))
    V_old = np.zeros((hENV.height, hENV.width))
    gamma = 0.95
    alpha = 0.1

    ## while converge()==0:
    nIter = 10000

    sys.stdout.write("\nMain Iteration:...\n")

    for iIter in range(nIter):
        perc = float(iIter) / float(nIter) * 100
        sys.stdout.write("\r%.4f%%" % perc) 

        ps, VUpdate = Maze_AGNT.ExecEpi(V, gamma, hENV)

        ## V_new = copy.deepcopy(V)
        clone(V_old, V, hENV.height, hENV.width)

        for i in range(len(ps)):
            s = ps[i]
            Vup = VUpdate[i]
            V0 = V_old[s.x][s.y]

            V[s.x][s.y] = V0 + alpha*(Vup-V0)

    hFile = open('V.txt', 'w')
    for x in range(hENV.height):
        for y in range(hENV.width):
            hFile.write("%6.4f " % (V[x][y]))
        hFile.write("\n")
    hFile.close()

## def converge():

Maze_Train()
