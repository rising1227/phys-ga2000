import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab

def funccv(x):
    return x**4 * np.e**x /((np.e**x-1)**2)

def cv(x):
    xp, wp = gaussxwab(50,0,428/x)
    xp = np.array(xp)
    wp = np.array(wp)
    inte = (funccv(xp) * wp).sum()
    return 9*0.001*6.022*1.38*100000*(x/428)**3 * inte
cv1 = np.vectorize(cv)

def cv300(N):
    xp, wp = gaussxwab(N,0,428/300)
    xp = np.array(xp)
    wp = np.array(wp)
    inte = (funccv(xp) * wp).sum()
    return 9*0.001*6.022*1.38*100000*(300/428)**3 * inte

plt.plot(np.arange(5,500,5),cv1(np.arange(5,500,5)),"+-")
plt.xlabel("Temperature(K)")
plt.ylabel("Heat Capacity(J/K)")

plt.savefig("ps4-1-2.png")

print("convergence test, the numerical gaussian integration at 300K result from N=10, 20 to 70")
print(np.vectorize(cv300)(np.arange(10,70,10)))
