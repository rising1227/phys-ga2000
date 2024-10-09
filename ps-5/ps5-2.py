import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab

y1 = lambda x:x**1*np.e**(-x)
y2 = lambda x:x**2*np.e**(-x)
y3 = lambda x:x**3*np.e**(-x)
a = np.arange(0,5,0.025)

plt.plot(a,y1(a),label="a=2")
plt.plot(a,y2(a),label="a=3")
plt.plot(a,y3(a),label="a=4")
plt.legend()
plt.xlabel("x")
plt.ylabel("Gamma_a(x)")
plt.savefig("ps5-2-1.png")
plt.clf()

def func(a,x):
    return (a-1)/(1-x)**2 * np.e**(-(a-1)*x/(1-x) + (a-1)*np.log((a-1)*x/(1-x)))
func = np.vectorize(func)

xp, wp = gaussxwab(100,0,1)
xp = np.array(xp)
wp = np.array(wp)

for i in [1.5,3,6,10]:
    print("Calculation of Gamma[{asd}] is {sd}".format(asd=i,sd=(func(i,xp) * wp).sum()))

