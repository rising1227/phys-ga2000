import numpy as np
import matplotlib.pyplot as plt

bi213 = np.zeros(10000) + 1
ti209 = np.zeros(10000)
pb209 = np.zeros(10000)
bi209 = np.zeros(10000)
pb = 1-2**(-1/(46*60))
pt = 1-2**(-1/(2.2*60))
pp = 1-2**(-1/(3.3*60))
bi213number = np.zeros(20000)
ti209number = np.zeros(20000)
pb209number = np.zeros(20000)
bi209number = np.zeros(20000)


for i in range(20000):
    ap = np.int_(np.random.random(10000) > pp)
    at = np.int_(np.random.random(10000) > pt)
    ab = np.int_(np.random.random(10000) > pb)
    s = np.int_(np.random.random(10000) > 0.0209)
    ab1t = np.int_((ap + s)>=1)
    ab1p = np.int_((ap + (1-s))>=1)
    
    bi209 = bi209 + pb209 - pb209 * ab
    pb209 = pb209 * ab
    
    pb209 = pb209 + ti209 - ti209 * at
    ti209 = ti209 * at
    
    ti209 = ti209 + bi213 - bi213 * ab1t
    bi213 = bi213 * ab1t
    
    pb209 = pb209 + bi213 - bi213 * ab1p
    bi213 = bi213 * ab1p

    bi213number[i] = bi213.sum()
    ti209number[i] = ti209.sum()
    pb209number[i] = pb209.sum()
    bi209number[i] = bi209.sum()




plt.plot(np.arange(20000),bi213number,"-",label="Bi213",linewidth = 0.7)
plt.plot(np.arange(20000),pb209number,"-",label="Pb209",linewidth = 0.7)
plt.plot(np.arange(20000),ti209number,"-",label="Ti209",linewidth = 0.7)
plt.plot(np.arange(20000),bi209number,"-",label="Bi209",linewidth = 0.7)
plt.xlabel("time/s")
plt.ylabel("particle number")
plt.legend()
plt.savefig("ps3-2.png",dpi=600)