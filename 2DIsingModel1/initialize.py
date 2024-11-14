import numpy as np

def IsingGeneration(m,B,random=False):
    """
    Generate a initial spin lattice for the calculation. m is the size of the system.
    Random = false: Generate an initial paramagnets for zero temperature.
    Random = True: Generate an initial random spin lattice for very high temperature.
    """
    if random == False:
        S = np.ones((m,m),dtype=bool)
        for i in range(m):
            for j in range(m):          
                if B[i][j] < 0:
                    S[i][j] = False
        return S
    else:
        mat = np.random.uniform(0,1,(m,m))
        S = np.bool_(mat*2//1)
        return S
    
def IsingGenerationint(m,B,random=False):
    """
    Generate a initial spin lattice for the calculation. m is the size of the system.
    Random = false: Generate an initial paramagnets for zero temperature.
    Random = True: Generate an initial random spin lattice for very high temperature.
    """
    if random == False:
        S = np.ones((m,m),dtype=np.int8)
        for i in range(m):
            for j in range(m):          
                if B[i][j] < 0:
                    S[i][j] = np.int8(-1)
        return S
    else:
        mat = np.random.uniform(0,2,(m,m))
        S = (mat//1)*2 - 1
        return np.int8(S)


def CalculateEnergy(S,B):
    """
    Calculate the energy of the system with ising interaction and external field
    """
    Spinsystem = np.int_(S)*2-1
    E1 = (Spinsystem * B).sum()
    Sleft = np.roll(S,-1,axis=1)
    Sright = np.roll(S,1,axis=1)
    Sup = np.roll(S,-1,axis=0)
    Sdown = np.roll(S,1,axis=0)
    E2 = (S != Sleft).sum() *2 + (S != Sright).sum() *2 + (S != Sup).sum() *2 + (S != Sdown).sum() * 2
    return E1 + E2/2

def CalculateEnergyint(S,B):
    """
    Calculate the energy of the system with ising interaction and external field
    """

    E1 = (S * B).sum()
    Sleft = np.roll(S,-1,axis=1)
    Sright = np.roll(S,1,axis=1)
    Sup = np.roll(S,-1,axis=0)
    Sdown = np.roll(S,1,axis=0)
    E2 = -((S*Sleft - 1).sum() + (S*Sright - 1).sum() + (S*Sup - 1).sum() + (S*Sdown - 1).sum())
    return E1 + E2/2