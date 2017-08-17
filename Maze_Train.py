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
    ## alpha = 0.1

    ## while converge()==0:
    nIter = 10000

    sys.stdout.write("\nMain Iteration:...\n")

    eps = 1
    Anneal = 200
    rate = 0.1
    iA = 0

    alpha = 0.25
    Anl2 = 500
    r2 = 0.05
    iA2 = 0
    
    Vs = np.zeros(nIter)

    for iIter in range(nIter):
        perc = float(iIter) / float(nIter) * 100
        sys.stdout.write("\r%.4f%%" % perc)

        ps, VUpdate = Maze_AGNT.ExecEpi(V, gamma, eps, hENV)
        """
        for i in range(len(ps)):
            sys.stdout.write("(%2d, %2d) %6.4f\n" 
                             % (ps[i].x, ps[i].y, VUpdate[i]))
        """
        ## V_new = copy.deepcopy(V)
        clone(V_old, V, hENV.height, hENV.width)
        ## """
        for i in range(len(ps)):
            s = ps[i]
            Vup = VUpdate[i]
            V0 = V_old[s.x][s.y]

            V[s.x][s.y] = V0 + alpha*(Vup-V0)
        """
        s_nxt = hENV.goal
        for i in range(len(ps))[::-1]:
            s = ps[i]
            V0 = V[s.x][s.y]

            V[s.x][s.y] = V0 + alpha*(Vup-V0)
        """
        iA += 1
        if iA == Anneal:
            eps = eps * rate
            iA = 0

        iA2 += 1
        if iA2 == Anl2:
            alpha = alpha * r2
            iA2 = 0
        
        V00 = V[hENV.start.x][hENV.start.y]
        Vs[iIter] = V00

        """
        sys.stdout.write("\n")

        for x in range(12):
            for y in range(12):
                sys.stdout.write("%6.4f " % V[x][y])
            sys.stdout.write("\n")
        """

    hFile = open('V.txt', 'w')
    for x in range(hENV.height):
        for y in range(hENV.width):
            hFile.write("%6.4f " % (V[x][y]))
        hFile.write("\n")
    hFile.close()

    hFile = open('Vs.txt', 'w')
    for i in range(nIter):
        hFile.write("%7.4f\n" % Vs[i])
    hFile.close()

    return V

## def converge():

## Maze_Train()
