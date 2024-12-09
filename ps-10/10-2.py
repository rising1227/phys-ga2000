import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dst,idst
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

# fourier transformation


re = dst(np.real(phi0))
im = dst(np.imag(phi0))
alpha = np.pi**2*hbar*dt/(2*m*L**2)
kmat = np.zeros(N-1)
for i in range(N-1):
    kmat[i] = (i+1)**2

numb = 100
plt.plot(pos,idst(np.real(re*np.cos(kmat*numb*alpha) + im*np.sin(kmat*numb*alpha))))
plt.xlabel("position/m")
plt.ylabel("re(psi)")
plt.savefig("7.png",dpi=500)
plt.clf()





# Animation and evolution

fig, ax = plt.subplots()
line = ax.plot(pos,np.real(phi1))
ax.set_ylim(-1,1)
ax.set_xlabel("position/m")
ax.set_ylabel("re(psi)")

def animate(numb):
    factorsin = np.sin(kmat*numb*alpha)
    factorcos = np.cos(kmat*numb*alpha)
    phire = idst(np.real(re*factorcos + im*factorsin))
    line[0].set_ydata(phire)
    return line


anim = FuncAnimation(
    fig,
    animate,
    interval = 50/30,
    blit = True
)

plt.show()