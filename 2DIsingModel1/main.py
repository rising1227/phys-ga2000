import numpy as np
import matplotlib.pyplot as plt
from initialize import IsingGeneration, CalculateEnergy, IsingGenerationint
from Metropolis import transferfunction, metropolis
import multiprocessing
import time
import sys
m = 100
align = True

# generating data for different m: reading m from argv parameter
if len(sys.argv) > 1:
    m = np.int_(sys.argv[1])
    align = bool(int(sys.argv[2]))

# initialization
B = np.zeros((m,m))
S = IsingGenerationint(m,B,False,align)
E0 = CalculateEnergy(S,B)
M0 = (np.int_(S)*2-1).sum()

# temperature range
Tfinal = 5
section = 100

# our data, each element of EnergyT and MagneticT is an array for different temparature
EnergyT = [0,0,0,0,0,0,0]
MagneticT = [0,0,0,0,0,0,0]
for i in range(7):
    EnergyT[i] = np.zeros(section)
    MagneticT[i] = np.zeros(section)

# calculating theoretical value
mas = np.linspace(0.01,5,1000)
def TheoryMag(T):
    z = np.e**(-4/T)
    if (1-6*z+z**2) > 0:
        return (1+z)**(0.25) * (1-6*z+z**2)**(0.125) * (1-z)**(-0.5)
    else:
        return 0

TheoryMag = np.vectorize(TheoryMag)

# defining iteration for different temperature
def iteration(T,B):
    if B == 0:
        if T > 2.1 and T < 2.4:
            return 200000000
        elif T < 1.2:
            return 200000
        elif T < 2.8:
            return 2000000
        else:
            return 2000000
    else:
        if T > 2.1 and T < 2.4:
            return 8000000
        elif T < 1.2:
            return 200000
        elif T < 2.8:
            return 2000000
        else:
            return 2000000    

B0range = [-0.5,-0.25,-0.1,0,0.1,0.25,0.5]

nowtime = time.time()


# funcion to do main calculation
def DoBcalculation(queue,j):
    # initialize
    B0 = B0range[j]
    # get in track of simulation process
    print("simulating magnetic field:", B0range[j])
    B = np.ones((m,m)) * B0
    S = IsingGeneration(m,B,False)
    E0 = CalculateEnergy(S,B)
    M0 = (np.int_(S)*2-1).sum()
    i = 0
    # performing metropolis algorithm for each temperature
    for T in np.linspace(0.001,Tfinal,section):
        print("calculating step:", i)
        print("current time used:", time.time()-nowtime)
        EnergyT[j][i],MagneticT[j][i] = metropolis(m,T,S,B,M0,E0,iteration(T,B0))
        i = i + 1
        E0 = CalculateEnergy(S,B)
        M0 = (np.int_(S)*2-1).sum()
    # parallelism
    queue.put((EnergyT[j],MagneticT[j],j))
    # if j == 0:
    #     plt.plot(np.linspace(0.001,Tfinal,section),EnergyT[j],"+")
    #     plt.savefig("testphoto.png")
    #     plt.clf()


if __name__ == "__main__":
    # perform main calculation in many cores
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

# saving the data into binary files
np.save("E-T({s}).npy".format(s=m),EnergyT)
np.save("B-T({s}).npy".format(s=m),MagneticT)


