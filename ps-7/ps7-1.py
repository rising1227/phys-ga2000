import numpy as np
import matplotlib.pyplot as plt

def f(m,r):
    return (1+m)*r**3*(1-r)**2 - (1-r)**2 + m*r**2

def derf(m,r):
    return 3*(1+m)*r**2*(1-r)**2 + (-2)*(1+m)*r**3*(1-r)**1 - (-2)*(1-r)**1 + 2*m*r**1

mmoon = 7.34767309 * 10**22
mearth = 5.97219 * 10**24
mjupyter = 1.89813 * 10**27
msun = 1.989 * 10**30



x = 1
m1 = mjupyter/msun
while(1):
    if np.abs(f(m1,x)) < 1e-10:
        print("the final solution is ",x)
        break
    x = x - f(m1,x)/derf(m1,x)