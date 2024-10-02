import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab

def V(x):
    return x**4

def Tperiod(x):
    xp, wp = gaussxwab(20,0,x)
    xp = np.array(xp)
    wp = np.array(wp)
    inte = ((lambda y,z:1/(np.sqrt(V(y)-V(z))))(x,xp) * wp).sum()
    return inte * np.sqrt(8)

plt.plot(np.arange(0.05,2,0.05),np.vectorize(Tperiod)(np.arange(0.05,2,0.05)),"+-")
plt.xlabel("Initial Position")
plt.ylabel("Periodicity")

plt.savefig("ps4-2-2")