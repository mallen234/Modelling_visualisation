import numpy as np
import scipy
from numpy.random import rand
from matplotlib import pyplot as plt
from matplotlib import animation
import sys
import gol_functions as gol
from scipy.stats import linregress as linregress


def experiment(N):
    average_equil = []
    L = 200
    length = np.linspace(1,L,L)
    #print(length)
    for i in range(L):
        
        #print(i)
        TotAlive = []
        State = gol.primarystate(N)
        for j in range(100000):
            TotAlive.append(gol.total_alive(State))
            State = gol.step_func(State,N)
            if (j > 3):
                if (TotAlive[j] == TotAlive[j-1] and TotAlive[j] == TotAlive[j-2] \
                    and TotAlive[j] == TotAlive[j-3] and TotAlive[j] == TotAlive[j-4]):
                    average_equil.append(j-4)
                    break
        # print(average_equil[i])
    gol.plotting_func(average_equil,length)

def velocity_experiment(N):
    com_list_x = []
    com_list_y = []
    T = 1000
    time_list = []
    Lattice = gol.primarystate_glider(N)

    print(Lattice)
    for i in range(T):
        com_stuff = gol.com_glider(Lattice,N)
        #print(com_stuff)
        if (com_stuff != None):
            com_list_x.append(com_stuff[0])
            com_list_y.append(com_stuff[1])
            time_list.append(i)
        #print (com_list_x[i])
        #print(com_list_y[i])

        # plt.cla()
        # im=plt.imshow(Lattice,cmap = "bwr",vmin=-1,vmax = +1)
        # plt.draw()
        # plt.pause(0.0002)
        #print(total_alive(State))

        Lattice = gol.step_func(Lattice,N)

    com_list_x = np.asarray(com_list_x)
    com_list_y = np.asarray(com_list_y)

    #print(com_list_y,com_list_x)

    r_list = np.sqrt((com_list_x**2)+(com_list_y**2))
    plt.show()
    #print(r_list)
    #print(time_list)

    plt.scatter(time_list,r_list,s=2)
    
    time_list = np.asarray(time_list)

    slope, intercept, r_value, p_value, std_error = linregress(time_list[:150],r_list[:150])

    theoretical = slope*time_list + intercept

    plt.plot(time_list[:150],theoretical[:150],color = "red")
    plt.xlabel("Generations")
    plt.ylabel("Position")
    plt.savefig("velocity_glider.png")
    plt.show()
    print(f'\nthe speed IS {np.abs(slope)} places per generation')

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