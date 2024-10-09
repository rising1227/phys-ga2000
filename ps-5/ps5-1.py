import numpy as np
import matplotlib.pyplot as plt
import jax.numpy as jnp
from jax import grad
import math

h = 10**(-8)

def f(x):
    return 1 + 0.5 * np.tanh(2*x)
def fprime(x):
    return (f(x+h/2) - f(x-h/2))/h
def fprimethe(x):
    return 1/np.cosh(2*x)**2
A = np.arange(-2,2,0.05)

plt.plot(A,np.vectorize(fprimethe)(A),"-",label="analytical")
plt.plot(A,np.vectorize(fprime)(A),"+",label="numerical")
plt.legend()
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.savefig("ps5-1-1.png")
plt.clf()

def f1(x):
    return 1 + 0.5 * jnp.tanh(2*x)

A1 = jnp.arange(-2,2,0.05)
fprimejax = grad(f1)

plt.plot(A1,np.vectorize(fprimejax)(A1),"-",label="jax calculation")
plt.plot(A,np.vectorize(fprime)(A),"+",label="numerical")
plt.legend()
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.savefig("ps5-1-2.png")
plt.clf()
