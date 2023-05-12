import numpy as np
import scipy
from numpy.random import rand
from matplotlib import pyplot as plt
from matplotlib import animation
import sys
import subprocess
from lattice import Lattice

# p1,p2,p3 = 0.8,0.1,0.01     THIS IS FOR WAVES
# p1,p2,p3 = 0.5,0.5,0.5
# p1,p2,p3 = 0.1,0.7,0.1

def main():
    print("Would you like to show animation or run experiment?")
    first_input = input("Type 1 for animation and 2 for experiment: ")
    try:
        if (str(first_input) == "1"):
            N = int(input("Input size of Lattice: "))
            p1 = float(input("Input p1: "))
            p2 = float(input("Input p2: "))
            p3 = float(input("Input p3: "))

        elif (str(first_input) == "2"):
            N = input("Input size of Lattice")
            subprocess.run(["python", "experiment.py"])
            exit(0)
        
        else:
            print("Error: please type 1 or 2")
            exit(0)
    except IndexError:
        raise IndexError("Please hand 4 arguments at the command line: Size of Lattice, p1,p2,p3 ")

    except ValueError:
        raise ValueError(" Please give an integer then 3 floats")

    sweeps = 1000
    lattice_inst = Lattice(N,p1,p2,p3,sweeps)
    Lattice.sim(lattice_inst)

main()