import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft,irfft

datadow = np.loadtxt("dow.txt")
plt.plot(datadow)

c = rfft(datadow)
plt.xlabel("t/day")
plt.ylabel("dow jones industurial average")
plt.savefig("8-3-1.png")
plt.clf()

for i in range(c.shape[0]):
    if i > c.shape[0]*0.1:
        c[i] = 0
dow1 = irfft(c)

plt.plot(datadow,label="original")
plt.plot(dow1,label="smoothed")
plt.xlabel("t/day")
plt.ylabel("dow jones industurial average")
plt.legend()
plt.savefig("8-3-2.png")
plt.clf()


d = rfft(datadow)
for i in range(d.shape[0]):
    if i > d.shape[0]*0.02:
        d[i] = 0
dow2 = irfft(d)

plt.plot(datadow,label="original")
plt.plot(dow2,label="smoothed")
plt.xlabel("t/day")
plt.ylabel("dow jones industurial average")
plt.legend()
plt.savefig("8-3-3.png")
plt.clf()