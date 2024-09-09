import numpy as np
import matplotlib.pyplot as plt

def gaussian(sigma,dev,x):
    return (1/(sigma*np.sqrt(2*np.pi))) * np.e**(-0.5*(x-dev)**2/sigma**2)


x = np.linspace(-10,10,100)
y = gaussian(3,0,x)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Gaussian Function with zero mean and standard derivation of 3")
plt.plot(x,y)

plt.savefig('gaussian.png')