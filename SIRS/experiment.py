import numpy as np
import scipy
from numpy.random import rand
from matplotlib import pyplot as plt
from matplotlib import animation
import sys
from Lattice import Lattice

def main():
    p2 = 0.5
    p1 = np.linspace(0,1,21)
    p3 = np.linspace(0,1,21)

    aveInfected = np.zeros([21,21])
    aveVariance = np.zeros([21,21])
    
    sweeps = 10
    Lattice = primary_state(N)

    for i in range(11):       #TWO FOR LOOPS TO GO OVER FULL MATRIX OF P1,P3 VALUES
        print(i)
        for j in range(11):
            print(j)
            b=1
            Infected = []
            Variance = []

            for k in range(sweeps): #LOOP TO DO THE TOTAL NUMBER OF SWEEPS
                for l in range(N*N):  #LOOP THAT DOES A FULL LOOP
                    Lattice = step_func(Lattice,N,p1[i],p2,p3[j])

                if (k>1):
                    a = average_infected(Lattice,N)
                    Infected.append(a)

                    if  (a==0):
                        b=0
                        break
                
            if b == 0:
                aveVariance[i,j] = 0
                aveInfected[i,j] = 0
            
            Infected = np.asarray(Infected)
            
            meanInfect = np.mean(Infected)
            varInfect = np.mean(Infected**2) - meanInfect**2
            

            aveVariance[i,j] = varInfect/N
            aveInfected[i,j] = meanInfect/N

    X,Y = np.meshgrid(p1,p3)
    fig,ax=plt.subplots(1,1)
    cp = ax.contourf(X, Y, aveInfected)
    fig.colorbar(cp)
    plt.savefig("SIRS_PHASE_DIAGRAM.png")
    plt.show()
