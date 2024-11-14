import numpy as np
import matplotlib.pyplot as plt
from initialize import IsingGeneration, CalculateEnergy
from Metropolis import transferfunction, metropolis
import multiprocessing
import time

m = 1000
B = np.zeros((m,m))
S = IsingGeneration(m,B,False)
E0 = CalculateEnergy(S,B)
M0 = (np.int_(S)*2-1).sum()


Tfinal = 5
section = 400

EnergyT = [0,0,0,0,0,0,0]
MagneticT = [0,0,0,0,0,0,0]
for i in range(7):
    EnergyT[i] = np.zeros(section)
    MagneticT[i] = np.zeros(section)

# theoretical value
mas = np.linspace(0.01,5,1000)
def TheoryMag(T):
    z = np.e**(-4/T)
    if (1-6*z+z**2) > 0:
        return (1+z)**(0.25) * (1-6*z+z**2)**(0.125) * (1-z)**(-0.5)
    else:
        return 0

TheoryMag = np.vectorize(TheoryMag)

def iteration(T):
    if T < 1.2:
        return 3000000
    elif T < 2.26:
        return 6000000 + np.int64((TheoryMag(T-Tfinal/section) -TheoryMag(T))*700000000)
    else:
        return 9000000

B0range = [-0.5,-0.25,-0.1,0,0.1,0.25,0.5]

nowtime = time.time()

def DoBcalculation(queue,j):
    B0 = B0range[j]
    print("simulating magnetic field:", B0range[j])
    B = np.ones((m,m)) * B0
    S = IsingGeneration(m,B,False)
    E0 = CalculateEnergy(S,B)
    M0 = (np.int_(S)*2-1).sum()
    i = 0
    for T in np.linspace(0.001,Tfinal,section):
        print("calculating step:", i)
        print("current time used:", time.time()-nowtime)
        EnergyT[j][i],MagneticT[j][i] = metropolis(m,T,S,B,M0,E0,iteration(T))
        i = i + 1
        E0 = CalculateEnergy(S,B)
        M0 = (np.int_(S)*2-1).sum()
    queue.put((EnergyT[j],MagneticT[j],j))
    # if j == 0:
    #     plt.plot(np.linspace(0.001,Tfinal,section),EnergyT[j],"+")
    #     plt.savefig("testphoto.png")
    #     plt.clf()


if __name__ == "__main__":
    # creating processes
    p = [0,0,0,0,0,0,0]
    queue = multiprocessing.Queue()
    for i in range(7):
        p[i] = multiprocessing.Process(target=DoBcalculation, args=(queue,i))
    for i in range(7):
        p[i].start()
    for i in range(7):
        p[i].join()
    for i in range(7):
        a,b,count = queue.get()
        EnergyT[count] = a
        MagneticT[count] = b

    # both processes finished
    print("Done!")


for s in np.arange(3,7):
    plt.plot(np.linspace(0.001,Tfinal,section),EnergyT[s],"+",label="B={asd}".format(asd=B0range[s]))
plt.xlabel("T")
plt.ylabel("E/J")
plt.legend()
plt.title("1000*1000 Ising model:E-T diagram")
plt.savefig("E-T_withB_diagram(latest)")
plt.clf()

for s in range(7):
    plt.plot(np.linspace(0.001,Tfinal,section),EnergyT[s],"+",label="B={asd}".format(asd=B0range[s]))
plt.xlabel("T")
plt.ylabel("E/J")
plt.legend()
plt.title("1000*1000 Ising model:E-T diagram")
plt.savefig("E-T_withB_diagram(latest)(with negative B)")
plt.clf()

for s in range(7):
    plt.plot(np.linspace(0.001,Tfinal,section),MagneticT[s]/m**2,"+",label="B={asd}".format(asd=B0range[s]))
plt.plot(mas,TheoryMag(mas),"-",label="theoretical")
plt.legend()
plt.xlabel("T")
plt.ylabel("M")
plt.title("1000*1000 Ising model:M-T diagram")
plt.savefig("M-T_withB_diagram(latest)")
plt.clf()