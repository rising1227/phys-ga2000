import numpy as np
import random
import matplotlib.pyplot as plt


# legacy version with bool type
def transferfunction(m,S,E,M,B,T):
    if T == 0:
        beta = 1000000000000000
        # print("zero temperature, only true ground state")
    else:
        beta = 1/T
    i = random.randint(0,m-1)
    j = random.randint(0,m-1)

    deltaE = (np.int_(S[i,j] == S[(i+1)%m,j]) + np.int_(S[i,j] == S[i-1,j]) + np.int_(S[i,j] == S[i,(j+1)%m]) + np.int_(S[i,j] == S[i,j-1]))*4 - 8 + 2 * B[i,j] * (np.int_(S[i,j])*2 - 1)
    deltaM = (np.int_(S[i,j])*2 - 1) * -2
    if deltaE <= 0:
        S[i,j] = (S[i,j] != True)
        return E+deltaE, M+deltaM
    else:
        if random.random() < np.e**(-deltaE*beta):
            S[i,j] = (S[i,j] != True)
            return E+deltaE, M+deltaM
        else:
            return E,M


# for performing one step in the markov chain
def transferfunctionint(m,S,E,M,B,T):
    if T == 0:
        beta = 1000000000000000
        # print("zero temperature, only true ground state")
    else:
        beta = 1/T
    i = random.randint(0,m-1)
    j = random.randint(0,m-1)

    deltaE = (S[(i+1)%m,j] + S[i-1,j] + S[i,(j+1)%m] + S[i,j-1])*S[i,j] * 2 + 2 * B[i,j] * S[i,j]
    deltaM = -2 * S[i,j]
    if deltaE <= 0:
        S[i,j] = -S[i,j]
        return E+deltaE, M+deltaM
    else:
        if random.random() < np.e**(-deltaE*beta):
            S[i,j] = -S[i,j]
            return E+deltaE, M+deltaM
        else:
            return E,M


# legacy version with bool type
def metropolis(m,T,S,B,M,E,iteration,func=transferfunction):
    energy = np.zeros(iteration)
    magnetic = np.zeros(iteration)
    for i in range(iteration):
        E, M = func(m,S,E,M,B,T)
        energy[i] = E
        magnetic[i] = M
    # plt.plot(energy)
    # plt.plot(magnetic)
    return np.average(energy[-iteration//10:-1]),np.average(magnetic[-iteration//10:-1])


# reiterating "transferfunctionint" and perform a markov chain for a certain temperature
def metropolisint(m,T,S,B,M,E,iteration,func=transferfunctionint):
    energy = np.zeros(iteration)
    magnetic = np.zeros(iteration)
    for i in range(iteration):
        E, M = func(m,S,E,M,B,T)
        energy[i] = E
        magnetic[i] = M
    # plt.plot(energy)
    plt.plot(magnetic)
    print(np.std(energy[-iteration//10:-1])/np.average(energy[-iteration//10:-1]))
    return np.average(energy[-iteration//10:-1]),np.average(magnetic[-iteration//10:-1])

        