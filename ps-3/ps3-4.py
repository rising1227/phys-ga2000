import numpy as np
import matplotlib.pyplot as plt
import scipy

N = 1000
M = 100000



for N in [1,10,100,1000]:
    y = np.random.exponential(1,[N,M]).sum(0)/N
    plt.hist(y,100)
    plt.xlabel("y")
    plt.ylabel("number of variable")
    plt.savefig("ps3-4{asd}.png".format(asd = N))
    plt.clf()


asert = 2**np.arange(0,14)
mean = []
variance = []
skewness = []
kurtosis = []
for N in asert:
    y = np.random.exponential(1,[N,M]).sum(0)/N
    mean.append(y.sum()/M)
    variance.append(np.var(y))
    skewness.append(scipy.stats.skew(y))
    kurtosis.append(scipy.stats.kurtosis(y))

plt.plot(np.arange(0,14),mean,"+",np.arange(0,14),np.zeros(14)+1,"-")
plt.xlabel("log2(N)")
plt.ylabel("mean of the distribution")
plt.savefig("ps3-4-21.png")
plt.clf()


plt.plot(np.arange(0,14),1/(2**np.arange(0,14)),"-",np.arange(0,14),variance,"x")
plt.xlabel("log2(N)")
plt.ylabel("variance of the distribution")
plt.savefig("ps3-4-22.png")
plt.clf()

plt.plot(np.arange(0,14),skewness,"+-")
plt.xlabel("log2(N)")
plt.ylabel("skewness of the distribution")
plt.savefig("ps3-4-23.png")
plt.clf()

plt.plot(np.arange(0,14),kurtosis,"+-")
plt.xlabel("log2(N)")
plt.ylabel("kurtosis of the distribution")
plt.savefig("ps3-4-24.png")
plt.clf()
