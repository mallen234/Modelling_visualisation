import numpy as np
import scipy
from numpy.random import rand
from matplotlib import pyplot as plt
from matplotlib import animation
import sys

class Lattice:
    def __init__(self,N,p1,p2,p3,sweeps):
        self.N = N
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.sweeps = sweeps
        self.lattice = np.random.randint(3,size=(self.N,self.N)) -1


    def average_infected(self):
        a = self.N - np.count_nonzero(np.abs(self.lattice))
        return a
    
    def neighbours(self,i,j):
        neighbours_set = np.array([self.lattice[(i+1)%self.N,j], self.lattice[i,(j+1)%self.N]\
        ,self.lattice[(i-1),j],self.lattice[i,(j-1)]])

        if 0 in neighbours_set:
            return True

        else:
            return False

    def step_func(self):

        rand1 = np.random.randint(self.N) # define random numbers for monte carlo
        rand2 = np.random.randint(self.N)

        if (self.lattice[rand1,rand2] == -1) and self.neighbours(rand1,rand2):
            if np.random.rand() <=  self.p1:
                self.lattice[rand1,rand2] = 0

        elif self.lattice[rand1,rand2] == 0:
            if np.random.rand() <=  self.p2:
                self.lattice[rand1,rand2] = 1

        elif self.lattice[rand1,rand2] == 1:
            if np.random.rand() <=  self.p3:
                self.lattice[rand1,rand2] = -1

    # static method to run simulation
    def sim(Lattice):
        for i in range(Lattice.sweeps):
            for i in range(Lattice.N*Lattice.N):
                Lattice.step_func()
            
            plt.cla()
            im=plt.imshow(Lattice.lattice,vmin=-1,vmax = +1)
            plt.draw()
            plt.pause(0.00002)