import Maze_ENV
import math
import numpy as np
import sys
import copy

def ExecEpi(V, gamma, eps, hENV=None):
    if hENV==None:
        hENV = Maze_ENV.TM_ENV()
    else:
        hENV.Init()

    ## eps = 0.1

    ps = []
    VUpdate = []

    while hENV.terminal==0:
        s = hENV.GetState()
        ## draw an action a
        a, V_new = TD0(V, gamma, eps, hENV)
        
        ps.append(s)
        VUpdate.append(V_new)

        hENV.SetAction(a)
        hENV.ProcessDynamic()

    return (ps, VUpdate)

def TD0(V, gamma, eps, hENV):
    s = hENV.GetState()

    LegalMove = []
    Vs = []
    maxMove = -1
    maxV = -1
    for dir in range(4):
        hTMP = copy.deepcopy(hENV)
        hTMP.SetAction(dir)
        
        if hTMP.ProcessDynamic()==1:
            s_next = hTMP.GetState()
            V_new = hTMP.r + gamma*V[s_next.x][s_next.y]

            LegalMove.append(dir)
            Vs.append(V_new)
            
            if maxMove==-1:
                maxMove = dir
                maxV = V_new
            elif V_new > maxV:
                maxMove = dir
                maxV = V_new

    if np.random.rand() < 1-eps:
        return (maxMove, maxV)
    else:
        index = math.floor(np.random.rand()*len(LegalMove))
        return (LegalMove[index], Vs[index])
