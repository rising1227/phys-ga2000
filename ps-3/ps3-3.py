import numpy as np
import matplotlib.pyplot as plt


tau = 3.053*60
z = np.random.random(1000)
t = -tau * np.log2(1-z)

a = np.sort(t)
result = np.zeros(1000)

for i in range(1000):
    result[i] = np.int_(a>i).sum()

plt.plot(np.arange(1000),result)
plt.xlabel("time/s")
plt.ylabel("number of particle not decayed")
plt.savefig("ps3-3.png",dpi=600)