import numpy as np
import matplotlib.pyplot as plt
import time

## set N from 2 to 512 and do explicit for loop, data stored in "result"

test = 2**np.arange(1,9)
result = []
for N in test:
    AMat = np.random.random([N,N])
    BMat = np.random.random([N,N])
    CMat = np.zeros([N,N],float)
    start = time.time()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                CMat[i,j] = AMat[i,k] * BMat[k,j]
    result.append(time.time()-start)


## set N from 2 to 16384 and do np.dot, data stored in "result2"

test2 = 2**np.arange(1,14)
result2 = []
for N in test2:
    AMat = np.random.random([N,N])
    BMat = np.random.random([N,N])
    CMat = np.zeros([N,N],float)
    start = time.time()
    CMat = np.dot(AMat,BMat)
    result2.append(time.time()-start)


## after finding that the result for small N is far from our prediction, we chose better N where the calculation time is around 1-10s. Do for loop here and result stored in result3

test3 = np.int_(np.round(128*1.1**np.arange(0,12)))
result3 = []
for N in test3:
    AMat = np.random.random([N,N])
    BMat = np.random.random([N,N])
    CMat = np.zeros([N,N],float)
    start = time.time()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                CMat[i,j] = AMat[i,k] * BMat[k,j]
    result3.append(time.time()-start)


## Do np.dot here and result stored in result4

test4 = np.int_(np.round(4096*1.1**np.arange(0,12)))
result4 = []
for N in test4:
    AMat = np.random.random([N,N])
    BMat = np.random.random([N,N])
    CMat = np.zeros([N,N],float)
    start = time.time()
    CMat = np.dot(AMat, BMat)
    result4.append(time.time()-start)

plt.plot(np.log(test),np.log(np.array(result)),"+")
plt.xlabel("ln(N)")
plt.ylabel("ln(operation time/s)")
plt.savefig("1-1.png")

plt.clf()

plt.plot(np.log(test2),np.log(np.array(result2)),"+")
plt.xlabel("ln(N)")
plt.ylabel("ln(operation time/s)")
plt.savefig("1-2.png")

plt.clf()

plt.plot(np.log(test3),np.log(np.array(result3)),"+",np.log(test3),np.polyfit(np.log(test3),np.log(np.array(result3)),1)[0]*np.log(test3)+ np.polyfit(np.log(test3),np.log(np.array(result3)),1)[1],"-")
plt.xlabel("ln(N)")
plt.ylabel("ln(operation time/s)")
plt.text(5.6,1.0,"k = {k}}".format(k = np.polyfit(np.log(test3),np.log(np.array(result3)),1)[0]))
plt.savefig("1-3.png")

plt.clf()

plt.plot(np.log(test3),np.log(np.array(result3)),"+",np.log(test3),np.polyfit(np.log(test3),np.log(np.array(result3)),1)[0]*np.log(test3)+ np.polyfit(np.log(test3),np.log(np.array(result3)),1)[1],"-")
plt.xlabel("ln(N)")
plt.ylabel("ln(operation time/s)")
plt.text(9.2,1.0,"k = {k}}".format(k = np.polyfit(np.log(test3),np.log(np.array(result4)),1)[0]))
plt.savefig("1-4.png")

