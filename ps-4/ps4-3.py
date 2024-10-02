import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab
import math
from scipy.special import roots_hermite

array = np.zeros([50,50])
array[0,0]=1
array[1,1]=2

for i in np.arange(2,50,1):
    for j in range(50):
        array[i,j] = 2 * array[i-1,j-1] - 2*(i-1)*array[i-2,j]

def H(n,x):
    array1 = np.arange(0,50,1)
    return (x**array1 * array[n]).sum()

def phi(n,x):
    return H(n,x)*np.e**(-0.5*x**2)/np.sqrt(math.factorial(n)*np.sqrt(np.pi)*2**n)
phi1 = np.vectorize(phi)

plt.plot(np.arange(-4,4,0.04),phi1(0,np.arange(-4,4,0.04)),label="n=0")
plt.plot(np.arange(-4,4,0.04),phi1(1,np.arange(-4,4,0.04)),label="n=1")
plt.plot(np.arange(-4,4,0.04),phi1(2,np.arange(-4,4,0.04)),label="n=2")
plt.plot(np.arange(-4,4,0.04),phi1(3,np.arange(-4,4,0.04)),label="n=3")
plt.legend()
plt.xlabel("x")
plt.ylabel("wave function value")
plt.savefig("ps4-3-1.png")

plt.clf()

plt.plot(np.arange(-10,10,0.01),phi1(30,np.arange(-10,10,0.01)),"-")
plt.xlabel("x")
plt.ylabel("wave function value for n=10")
plt.savefig("ps4-3-2.png")

plt.clf()

def uncertainty(n):
    xp, wp = gaussxwab(100,-10,10)
    xp = np.array(xp)
    wp = np.array(wp)
    return (xp**2 * np.vectorize(phi1)(n,xp)**2 * wp).sum()

print("The uncertainty for n=5 with Gaussian Quadrature is: ",np.sqrt(uncertainty(5)))

def phi2(n,x):
    return H(n,x)/np.sqrt(math.factorial(n)*np.sqrt(np.pi)*2**n)
phi3 = np.vectorize(phi2)

def uncertaintyH(n):
    xp, wp = roots_hermite(n+3,mu=False)
    xp = np.array(xp)
    wp = np.array(wp)
    return (xp**2 * np.vectorize(phi3)(n,xp)**2 * wp).sum()

print("The uncertainty for n=5 with Gauss-Hermite method is: ",np.sqrt(uncertaintyH(5)))