import numpy as np
import matplotlib.pyplot as plt

# plotting: you can look at title and figure name for information

Tfinal = 5
section = 100
import sys
m = 100
if len(sys.argv) > 1:
    m = np.int_(sys.argv[1])

# calculating theoretical value
mas = np.linspace(0.01,5,1000)
def TheoryMag(T):
    z = np.e**(-4/T)
    if (1-6*z+z**2) > 0:
        return (1+z)**(0.25) * (1-6*z+z**2)**(0.125) * (1-z)**(-0.5)
    else:
        return 0

TheoryMag = np.vectorize(TheoryMag)

# reading external data
EnergyT = np.load("E-T({asd}).npy".format(asd=m))
MagneticT = np.load("B-T({asd}).npy".format(asd=m))
B0range = [-0.5,-0.25,-0.1,0,0.1,0.25,0.5]

for s in [3,4,6]:
    plt.plot(np.linspace(0.001,Tfinal,section),EnergyT[s],"+",label="B={asd}".format(asd=B0range[s]))
plt.xlabel("$T'$")
plt.ylabel("$E'/J$")
plt.legend()
plt.title("${asd}\\times{asd}$ Ising model".format(asd=m))
plt.savefig("plots/E-T_withB_diagram(latest,{asd})".format(asd=m))
plt.clf()

for s in [0,2,3,4,6]:
    plt.plot(np.linspace(0.001,Tfinal,section),EnergyT[s],"+",label="B={asd}".format(asd=B0range[s]))
plt.xlabel("$T'$")
plt.ylabel("$E'$/J")
plt.legend()
plt.title("${asd}*\\times{asd}$ Ising model".format(asd=m))
plt.savefig("plots/E-T_withB_diagram(latest,{asd})(with negative B)".format(asd=m))
plt.clf()

for s in [0,2,3,4,6]:
    plt.plot(np.linspace(0.001,Tfinal,section),MagneticT[s]/m**2,"+",label="B={asd}".format(asd=B0range[s]))
plt.plot(mas,TheoryMag(mas),"-",label="theoretical")
plt.legend()
plt.xlabel("$T'$")
plt.ylabel("$M$")
plt.title("${asd}\\times{asd}$ Ising model".format(asd=m))
plt.savefig("plots/M-T_withB_diagram(latest,{asd})".format(asd=m))
plt.clf()