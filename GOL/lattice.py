import numpy as np
import scipy
from numpy.random import rand
from matplotlib import pyplot as plt
from matplotlib import animation
import sys

def step_func(Lattice,N):
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
    
    return New_Lattice