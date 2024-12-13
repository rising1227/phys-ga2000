# 2D Ising Model Simulation Code
This is a code to perform simulation for 2D Ising model. We utilize metropolis algorithm to calculation expectation energy and magnetization of the system.

### to generate data
run: python3 main.py m
m states for the size of your 2D Ising model you would like to simulate.
I would suggest you choose m <= 500. For larger system, you might need to increase the number of iteration step manually(in the iteration(T,B) function in main.py)

### to plot
run: python3 plot.py m
m stands for the size of 2D ising model you'd like to plot the result
This generates standard diagram(M-T', E'-T' diagram for different external magnetization).

### for special diagrams in our report
simply run: python3 specialplot.py