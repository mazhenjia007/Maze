import math
import numpy as np
import sys

UNDF = -1
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

class Tp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return (self.x==other.x) and (self.y==other.y)
    def __ne__(self, other):
        return (self.x!=self.x) or (self.y!=self.y)
    def __add__(self, other):
        return Tp(self.x+other.x, self.y+other.y)
    def __sub__(self, other):
        return Tp(self.x-other.x, self.y-other.y)

dps = [Tp(0, -1), Tp(1, 0), Tp(0, 1), Tp(-1, 0)]

class TM_ENV:
    def __init__(self):
        self.height = 0
        self.width = 0
        self.map = np.zeros((1, 1))
        self.start = Tp(0, 0)
        self.goal = Tp(0, 0)

        self.LoadMap()

        ## self.maxStep = self.height*self.width*10
        self.maxStep = 1500

        self.s = Tp(0, 0)
        self.a = UNDF
        self.r = 0
        self.terminal = 0
        self.step = 0

        self.Init()

    def LoadMap(self):
        hFile = open('Maze_MAP.txt', 'r')
        line = hFile.readline()
        arr = line.split(' ')
        a1 = arr[0]
        a2 = arr[1].replace('\n', '')
        self.height = eval(a1)
        self.width = eval(a2)

        self.map = np.zeros((self.height, self.width))

        for x in range(self.height):
            line = hFile.readline()
            for y in range(self.width):
                ch = line[y]
                if ch=='1':
                    self.map[x][y] = 1
                elif ch=='0':
                    self.map[x][y] = 0
                elif ch=='S':
                    self.map[x][y] = 0
                    self.start = Tp(x, y)
                elif ch=='G':
                    self.map[x][y] = 0
                    self.goal = Tp(x, y)

        hFile.close()

    def Init(self):
        self.s = self.start
        self.terminal = 0
        self.a = UNDF
        self.r = 0
        self.step = 0

    def GetState(self):
        return self.s

    def SetAction(self, a):
        self.a = a

    def ProcessDynamic(self):
        s_new = self.s + dps[self.a]
        if self.map[s_new.x][s_new.y]==1:
            self.r = 0
            return 0
        else:
            self.s = s_new
            if self.s==self.goal:
                self.r = 1
                self.terminal = 1
            else:
                self.r = 0

            self.step += 1
            if self.step>self.maxStep:
                self.terminal = 2

            return 1

    def GetReward(self):
        return self.r
