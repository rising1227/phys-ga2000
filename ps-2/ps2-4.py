import numpy as np
import matplotlib.pyplot as plt

N = 2000

real2 = np.arange(-2,2,4/N)
real = np.arange(2,-2,-4/N)
complex = 0+1j

result_table = real.reshape([N,1])*complex + real2.reshape([1,N])

def determine_func(a):
    hini = 0
    for i in range(100):
        hini = hini**2 + a
        if np.abs(hini) >= 2:
            return False
            break
    return True
vectorized_function = np.vectorize(determine_func)

resultfinal = np.vectorize(int)(vectorized_function(result_table))


step=200

# Set the ticks on the x-axis and y-axis with a step
x_ticks = np.arange(0, N, step)
y_ticks = np.arange(0, N, step)

# Create corresponding labels ranging from -2 to 2, formatted to 2 decimal places
x_labels = [f"{label:.2f}" for label in np.linspace(-2, 2, N)[::step]]
y_labels = [f"{label:.2f}" for label in np.linspace(2, -2, N)[::step]]

plt.xticks(ticks=x_ticks, labels=x_labels)
plt.yticks(ticks=y_ticks, labels=y_labels)
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.imshow(resultfinal, cmap='gray', interpolation='nearest')
plt.show()