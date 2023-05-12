import numpy as np
import scipy
from numpy.random import rand
from matplotlib import pyplot as plt
from matplotlib import animation
import sys

def main():
    global N
    
    if (sys.argv[1] == "run_exp"):
        N = int(sys.argv[2])
        experiment(N)
        exit(1)

    elif (sys.argv[1] == "velocity_exp"):
        N = int(sys.argv[2])
        velocity_experiment(N)
        exit(1)

    try:
        N = int(sys.argv[1])
        Timestep = int(sys.argv[2])
        primary = str(sys.argv[3])
    
    except IndexError:
        raise IndexError("Please hand 3 arguments at the command line: Size of Lattice, Timesteps, initialstate ")

    except ValueError:
        raise ValueError(" Please give two integers then a string")
    
    Method_dict = {"O":gol.primarystate_oscillator,"G":gol.primarystate_glider,"R":gol.primarystate,"P":gol.primarystate_pentomino}
    State = Method_dict[sys.argv[3]](N)


    for i in range(Timestep):

        plt.cla()
        im=plt.imshow(State,cmap = "bwr",vmin=-1,vmax = +1)
        plt.draw()
        plt.pause(0.0002)
        #print(total_alive(State))

        State = gol.step_func(State,N)

main()