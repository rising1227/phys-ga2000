import numpy as np
import matplotlib.pyplot as plt

R = 0.08
rho = 1.22
C = 0.47
m = 1
def motion(r,t):
    x = r[0]
    xdot = r[1]
    y = r[2]
    ydot = r[3]
    fx = xdot
    fxdot = (-0.5*np.pi* R**2 * rho * C / m) * xdot*np.sqrt(xdot**2 + ydot**2)
    fy = ydot
    fydot = (-0.5*np.pi* R**2 * rho * C / m) * ydot*np.sqrt(xdot**2 + ydot**2) - 9.8
    return np.array([fx,fxdot,fy,fydot],float)

a = 0
b = 20
N = 100000
h = (b-a)/N
tpoint = np.arange(a,b,h)
xdata = np.zeros(N)
xdotdata = np.zeros(N)
ydata = np.zeros(N)
ydotdata = np.zeros(N)


r = np.array([0,50*np.sqrt(3),0,50])
i = 0
for t in tpoint:
    xdata[i] = r[0]
    xdotdata[i] = r[1]
    ydata[i] = r[2]
    ydotdata[i] = r[3]
    k1 = h*motion(r,t)
    k2 = h*motion(r+0.5*k1,t+0.5*h)
    k3 = h*motion(r+0.5*k2,t+0.5*h)
    k4 = h*motion(r+k3,t+h)
    r = r + (k1+2*k2+2*k3+k4)/6
    i = i + 1

# b
plt.plot(xdata,ydata)
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.savefig("9-7b.png",dpi=600)
plt.clf()


r = np.array([0,50*np.sqrt(3),0,50])
i = 0
a = 0
b = 20
N = 100000
h = (b-a)/N
tpoint = np.arange(a,b,h)
xdata1 = np.zeros((N,5))
xdotdata1 = np.zeros((N,5))
ydata1 = np.zeros((N,5))
ydotdata1 = np.zeros((N,5))
s = 0
for m in [0.1,0.5,1,5,10]:
    r = np.array([0,50*np.sqrt(3),0,50])
    i = 0
    for t in tpoint:
        xdata1[i,s] = r[0]
        xdotdata1[i,s] = r[1]
        ydata1[i,s] = r[2]
        ydotdata1[i,s] = r[3]
        k1 = h*motion(r,t)
        k2 = h*motion(r+0.5*k1,t+0.5*h)
        k3 = h*motion(r+0.5*k2,t+0.5*h)
        k4 = h*motion(r+k3,t+h)
        r = r + (k1+2*k2+2*k3+k4)/6
        i = i + 1
    s = s + 1

# c
plt.plot(xdata1[:,0],ydata1[:,0],label="m=0.1")
plt.plot(xdata1[:,1],ydata1[:,1],label="m=0.5")
plt.plot(xdata1[:,2],ydata1[:,2],label="m=1")
plt.plot(xdata1[:,3],ydata1[:,3],label="m=5")
plt.plot(xdata1[:,4],ydata1[:,4],label="m=10")
plt.legend()
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.savefig("9-7c.png",dpi=600)
plt.clf()