import numpy as np
import matplotlib.pyplot as plt


Tfinal = 5
section = 100

mas = np.linspace(0.01,5,1000)
def TheoryMag(T):
    z = np.e**(-4/T)
    if (1-6*z+z**2) > 0:
        return (1+z)**(0.25) * (1-6*z+z**2)**(0.125) * (1-z)**(-0.5)
    else:
        return 0

TheoryMag = np.vectorize(TheoryMag)

B0range = [-0.5,-0.25,-0.1,0,0.1,0.25,0.5]

# read the data
EnergyT1 = np.load("E-T(100).npy")
MagneticT1 = np.load("B-T(100).npy")/100**2
EnergyT2 = np.load("E-T(200).npy")
MagneticT2 = np.load("B-T(200).npy")/200**2
EnergyT3 = np.load("E-T(300).npy")
MagneticT3 = np.load("B-T(300).npy")/300**2
EnergyT4 = np.load("E-T(500).npy")
MagneticT4 = np.load("B-T(500).npy")/500**2


# without external field: compare with theoretical value
plt.plot(np.linspace(0.001,Tfinal,section),MagneticT1[3],"+",label="N=100")
plt.plot(np.linspace(0.001,Tfinal,section),MagneticT2[3],"+",label="N=200")
plt.plot(np.linspace(0.001,Tfinal,section),MagneticT3[3],"+",label="N=300")
# plt.plot(np.linspace(0.001,Tfinal,section),MagneticT4[3],"+",label="N=500")
plt.plot(mas,TheoryMag(mas),"-",label="Theory")
plt.xlabel("$T'$")
plt.ylabel("$M$")
plt.legend()
plt.title("2D Ising model:$M-T'$ diagram without external field")
plt.savefig("plots/2D Ising model without external field.png",dpi=500)
plt.clf()


m = 100
for s in [3,4,6]:
    plt.plot(np.linspace(0.001,Tfinal,section),(EnergyT1[s]-2*m**2)/10000,"+",label="H'={asd}".format(asd=B0range[s]))
plt.xlabel("$T$'")
plt.ylabel("$E'$/$10^4$")
plt.legend()
plt.title("${asd}\\times{asd}$ Ising model".format(asd=m))
plt.savefig("plots/E-T_withB_diagram(latest,100).png",dpi=500)
plt.clf()


m = 200
for s in [3,4,6]:
    plt.plot(np.linspace(0.001,Tfinal,section),(EnergyT2[s]-2*m**2)/10000,"+",label="H'={asd}".format(asd=B0range[s]))
plt.xlabel("$T'$")
plt.ylabel("$E'$/$10^4$")
plt.legend()
plt.title("${asd}\\times{asd}$ Ising model".format(asd=m))
plt.savefig("plots/E-T_withB_diagram(latest,200).png",dpi=500)
plt.clf()


m = 300
for s in [3,4,6]:
    plt.plot(np.linspace(0.001,Tfinal,section),(EnergyT3[s]-2*m**2)/10000,"+",label="H'={asd}".format(asd=B0range[s]))
plt.xlabel("$T'$")
plt.ylabel("$E'$/$10^4$")
plt.legend()
plt.title("${asd}\\times{asd}$ Ising model".format(asd=m))
plt.savefig("plots/E-T_withB_diagram(latest,300).png",dpi=500)
plt.clf()


m = 100
for s in [0,2,3,4,6]:
    plt.plot(np.linspace(0.001,Tfinal,section),MagneticT1[s],"+",label="H'={asd}".format(asd=B0range[s]))
plt.plot(mas,TheoryMag(mas),"-",label="Theory")
plt.xlabel("$T'$")
plt.ylabel("$M$")
plt.legend()
plt.title("${asd}\\times{asd}$ Ising model".format(asd=m))
plt.savefig("plots/M-T_withB_diagram(latest,100).png",dpi=500)
plt.clf()


m = 200
for s in [0,2,3,4,6]:
    plt.plot(np.linspace(0.001,Tfinal,section),MagneticT2[s],"+",label="H'={asd}".format(asd=B0range[s]))
plt.plot(mas,TheoryMag(mas),"-",label="Theory")
plt.xlabel("$T'$")
plt.ylabel("$M$")
plt.legend()
plt.title("${asd}\\times{asd}$ Ising model".format(asd=m))
plt.savefig("plots/M-T_withB_diagram(latest,200).png",dpi=500)
plt.clf()


m = 300
for s in [0,2,3,4,6]:
    plt.plot(np.linspace(0.001,Tfinal,section),MagneticT3[s],"+",label="H'={asd}".format(asd=B0range[s]))
plt.plot(mas,TheoryMag(mas),"-",label="Theory")
plt.xlabel("$T'$")
plt.ylabel("$M$")
plt.legend()
plt.title("${asd}\\times{asd}$ Ising model".format(asd=m))
plt.savefig("plots/M-T_withB_diagram(latest,300).png",dpi=500)
plt.clf()


plt.plot(np.linspace(0.001,Tfinal,section),(MagneticT3[1]+MagneticT3[5])/MagneticT3[1],"o",label="N=300")
plt.plot(np.linspace(0.001,Tfinal,section),(MagneticT2[1]+MagneticT2[5])/MagneticT2[1],"o",label="N=200")
plt.plot(np.linspace(0.001,Tfinal,section),(MagneticT1[1]+MagneticT1[5])/MagneticT1[1],"o",label="N=100")
plt.xlabel("$T'$")
plt.ylabel("$\\alpha_M$")
plt.legend()
plt.title("2D Ising model:$\\alpha_M-T'$ diagram without opposite external field $H'=\pm 0.25$")
plt.savefig("plots/alphaM-T.png",dpi=500)
plt.clf()


plt.plot((EnergyT1[1]-EnergyT1[5])/EnergyT1[1],"o",label="N=100")
plt.plot((EnergyT2[1]-EnergyT2[5])/EnergyT2[1],"o",label="N=200")
plt.plot((EnergyT3[1]-EnergyT3[5])/EnergyT3[1],"o",label="N=300")
plt.xlabel("$T'$")
plt.ylabel("$\\alpha_E$")
plt.legend()
plt.title("2D Ising model:$\\alpha_E-T'$ diagram without opposite external field $H'=\pm 0.25$")
plt.savefig("plots/alphaE-T.png",dpi=500)
plt.clf()