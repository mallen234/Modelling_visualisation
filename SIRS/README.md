#SIRS 

This is a statistical physics model of the spread of infection within a population of people based on three parameters and three different states. The population cycle through the states based on the statistical chance they surroundings and a statistical uncertainty modelled through monte carlo simulation
S - susceptible
I - infected
R - recovered
S - susceptible again


To run: simply cd into the SIRS repo and run main.py. It should prompt you to either display the animation or run the experiment - the experiment will produce a lot of graphs showing the phase transitions between the different parameters. You have to give it the Lattice size and three probabilities which represent the chances of going from one state to the next.
For interesting wave like behaviour you can try p1,p2,p3 = 0.8,0.1,0.01 
