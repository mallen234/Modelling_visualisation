import numpy as np
import scipy
from numpy.random import rand
from matplotlib import pyplot as plt
from matplotlib import animation
import sys

def primarystate_oscillator(N):
    #PRIMARY STATE FOR A OSCILLATOR
    Lattice = np.zeros([N,N])
    a = int(N/2)
    Lattice[a-2:a+1,a] = 1
    print(Lattice)
    return Lattice    

def primarystate_pentomino(N):
    #PRIMARY STATE FOR A PENTOMINO
    Lattice = np.zeros([N,N])
    Lattice[25,26:28] = 1
    Lattice[26,25:27] = 1
    Lattice[27,26] = 1
    return Lattice

def primarystate_glider(N):
    #PRIMARY STATE FOR A GLIDER
    
    Lattice = np.zeros([N,N])
    
    Lattice[1,0] = 1
    Lattice[1,2] = 1
    Lattice[0,2] = 1
    Lattice[2,1:3] = 1

    return Lattice

def primarystate_spaceship(N):
    Lattice = np.zeros([N,N])

    Lattice[1:4,0] = 1
    Lattice[0,1] = 1
    Lattice[3,1] = 1
    Lattice[3,2:4] = 1
    Lattice[0,4] = 1
    Lattice[2,4] = 1
    return Lattice

def primarystate(N):
    #PRIMARY STATE FOR A RANDOM CONFIG
    Lattice = np.random.randint(2, size=(N,N))
    return Lattice

class Lattice:
    def __init__(self,N,primaryState):
        self.N = N
        self.lattice = primaryState(N)

    def step_func(self,Lattice,N):
        New_Lattice = Lattice.copy()
        for i in range(N):
            for j in range(N):
                #print("latticeconfig",i,j)
                
                if (Lattice[i,j] == 0):
                    a = neighbours(Lattice,i,j,N)
                    #print(a)
                    if (a ==3):
                        New_Lattice[i,j] = 1

                else:
                    a = neighbours(Lattice,i,j,N)
                    #print("a",a)
                    if (a < 2) or (a > 3):
                        New_Lattice[i,j] = 0
        
        self.lattice = New_Lattice