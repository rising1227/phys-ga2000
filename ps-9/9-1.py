import numpy as np
import matplotlib.pyplot as plt

omega = 1

def f(r,t):
    x = r[0]
    y = r[1]
    fx = y
    fy = -omega**2 * x
    return np.array([fx,fy],float)

def f1(r,t):
    x = r[0]
    y = r[1]
    fx = y
    fy = -omega**2 * x**3
    return np.array([fx,fy],float)

mu = 1
def f2(r,t):
    x = r[0]
    y = r[1]
    fx = y
    fy = -omega**2 * x + mu * (1-x**2) * y
    return np.array([fx,fy],float)

a = 0
b = 50
N = 100000
h = (b-a)/N
H = 5

tpoint = np.arange(a,b,h)

xdata = np.zeros((N,H))
ydata = np.zeros((N,H))

for s in range(5):
    r = [s+1,0]
    i = 0
    for t in tpoint:
        xdata[i,s] = r[0]
        ydata[i,s] = r[1]
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r = r + (k1+2*k2+2*k3+k4)/6
        i = i + 1

# a
plt.plot(tpoint,xdata[:,0])
plt.xlabel("time/s")
plt.ylabel("x")
plt.savefig("9-6a.png",dpi=600)
plt.clf()

# b
plt.plot(tpoint,xdata[:,0])
plt.plot(tpoint,xdata[:,1])
plt.xlabel("time/s")
plt.ylabel("x")
plt.savefig("9-6b.png",dpi=600)
plt.clf()


a = 0
b = 20
N = 100000
h = (b-a)/N
H = 5
tpoint = np.arange(a,b,h)
xdata1 = np.zeros((N,H))
ydata1 = np.zeros((N,H))
for s in range(5):
    r = [s+1,0]
    i = 0
    for t in tpoint:
        xdata1[i,s] = r[0]
        ydata1[i,s] = r[1]
        k1 = h*f1(r,t)
        k2 = h*f1(r+0.5*k1,t+0.5*h)
        k3 = h*f1(r+0.5*k2,t+0.5*h)
        k4 = h*f1(r+k3,t+h)
        r = r + (k1+2*k2+2*k3+k4)/6
        i = i + 1

# c
plt.plot(tpoint,xdata1[:,0],label="A=1")
plt.plot(tpoint,xdata1[:,1],label="A=2")
plt.plot(tpoint,xdata1[:,2],label="A=3")
plt.legend()
plt.xlabel("time/s")
plt.ylabel("x")
plt.savefig("9-6c.png",dpi=600)
plt.clf()

# d
plt.plot(xdata[:,0],ydata[:,0],label="A=1")
plt.plot(xdata[:,1],ydata[:,1],label="A=2")
plt.plot(xdata[:,2],ydata[:,2],label="A=3")
plt.legend()
plt.xlabel("time/s")
plt.ylabel("x")
plt.savefig("9-6d-1.png",dpi=600)
plt.clf()

plt.plot(xdata1[:,0],ydata1[:,0],label="A=1")
plt.plot(xdata1[:,1],ydata1[:,1],label="A=2")
plt.plot(xdata1[:,2],ydata1[:,2],label="A=3")
plt.legend()
plt.xlabel("time/s")
plt.ylabel("x")
plt.savefig("9-6d-2.png",dpi=600)
plt.clf()


a = 0
b = 20
N = 100000
h = (b-a)/N
xdata2 = np.zeros((N,3))
ydata2 = np.zeros((N,3))
tpoint = np.arange(a,b,h)
for s in range(3):
    mu = 2 ** s
    r = [1,0]
    i = 0
    for t in tpoint:
        xdata2[i,s] = r[0]
        ydata2[i,s] = r[1]
        k1 = h*f2(r,t)
        k2 = h*f2(r+0.5*k1,t+0.5*h)
        k3 = h*f2(r+0.5*k2,t+0.5*h)
        k4 = h*f2(r+k3,t+h)
        r = r + (k1+2*k2+2*k3+k4)/6
        i = i + 1

# e
plt.plot(xdata2[:,0],ydata2[:,0],label="$\mu$=1")
plt.plot(xdata2[:,1],ydata2[:,1],label="$\mu$=2")
plt.plot(xdata2[:,2],ydata2[:,2],label="$\mu$=4")
plt.legend()
plt.xlabel("time/s")
plt.ylabel("x")
plt.savefig("9-6e.png",dpi=600)
plt.clf()