import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('signal.dat',dtype=float,delimiter='|')
signal = data[1:,1:-1]
time = signal[:,0]/10**9
result = signal[:,1]

# 1
plt.plot(time,result,"+")
plt.xlabel('t')
plt.ylabel('signal')
plt.savefig("ps5-3-1.png",dpi=600)
plt.clf()

# 2
A = np.zeros((1000,4))
A[:,0] = 1
A[:,1] = time
A[:,2] = time**2
A[:,3] = time**3
(u, w, vt) = np.linalg.svd(A, full_matrices=False)
ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = ainv.dot(result)
bm = A.dot(x)
plt.plot(time, result, '.', label='data')
plt.plot(time, bm, '.', label='model')
plt.xlabel('t/10^9')
plt.ylabel('signal')
plt.legend()
plt.savefig("ps5-3-2.png",dpi=600)
plt.clf()

# 3
print("the number of observation point inside one sigma is {a}".format(a=np.int_(np.abs(bm - result) < 2).sum()))

# 4

for k in [10,20]:
    A1 = np.zeros((1000,k))
    for i in range(k):
        A1[:,i] = time**i
    (u1, w1, vt1) = np.linalg.svd(A1, full_matrices=False)
    ainv1 = vt1.transpose().dot(np.diag(1. / w1)).dot(u1.transpose())
    x1 = ainv1.dot(result)
    bm1 = A1.dot(x1)
    plt.plot(time, result, '.', label='data')
    plt.plot(time, bm1, '.', label='model')
    plt.xlabel('t/10^9')
    plt.ylabel('signal')
    plt.legend()
    plt.savefig("ps5-3-4-{h}.png".format(h=k),dpi=600)
    plt.clf()
    print("The condition number for k equals {h} is {r}".format(h=k,r=w1.max()/w1.min()))


# 5
# for frequency from 2Hz to 

A1 = np.zeros((1000,39))
for i in range(20,39):
    A1[:,i] = np.sin(2*(2+(1+i/4.0))*np.pi*time)
A1[:,0] = 1
for i in range(1,20):
    A1[:,i] = np.cos(2*(2+(1+i/4.0))*np.pi*time)
(u1, w1, vt1) = np.linalg.svd(A1, full_matrices=False)
ainv1 = vt1.transpose().dot(np.diag(1. / w1)).dot(u1.transpose())
x1 = ainv1.dot(result)
bm1 = A1.dot(x1)
plt.plot(time, result, '.', label='data')
plt.plot(time, bm1, '.', label='model')
plt.xlabel('t/10^9')
plt.ylabel('signal')
plt.legend()
plt.savefig("ps5-3-55.png")
plt.clf()
print("the number of observation point inside one sigma is {a}".format(a=np.int_(np.abs(bm1 - result) < 2).sum()))