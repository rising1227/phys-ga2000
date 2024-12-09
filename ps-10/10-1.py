import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# define parameters 
dt = 10**(-18)
N = 1000
L = 10**(-8)
m = 9.109*10**(-31)
a = L/N
hbar = 1.05457*10**(-34)

# define initial wave function
global phi0
phi0 = np.zeros(N-1,dtype=complex)
phi1 = np.zeros(N-1,dtype=complex)

sigma = 10**(-10)
kappa = 5*10**(10)
x0 = L/2
def init(x):
    return np.e**(-((x-x0)**2)/(2*sigma**2))*np.e**(kappa*x*(0+1j))
pos = np.linspace(L/N,L-L/N,N-1)

phi0 = init(pos)

# define the matrice A and B
s = dt * hbar * (0+1j)/(4*m*a**2)
a1 = 1+s*2
a2 = -s
b1 = 1-s*2
b2 = s
A = np.zeros((N-1,N-1),dtype=complex)
B = np.zeros((N-1,N-1),dtype=complex)


for i in range(N-1):
    for j in range(N-1):
        if i == j:
            A[i,j] = a1
        if i == j+1 or i == j-1:
            A[i,j] = a2
        # A[0,-1] = a2
        # A[-1,0] = a2

for i in range(N-1):
    for j in range(N-1):
        if i == j:
            B[i,j] = b1
        if i == j+1 or i == j-1:
            B[i,j] = b2
        # B[0,-1] = b2
        # B[-1,0] = b2

Aprime = np.linalg.inv(A)

# Animation and evolution

fig, ax = plt.subplots()
line = ax.plot(pos,np.real(phi1))
ax.set_ylim(-1,1)
ax.set_xlabel("position/m")
ax.set_ylabel("re(psi)")

def animate(t):
    global phi0
    phi0 = np.dot(Aprime,np.dot(B,phi0))
    line[0].set_ydata(np.real(phi0))
    return line


anim = FuncAnimation(
    fig,
    animate,
    interval = 50/30,
    blit = True
)

plt.show()


