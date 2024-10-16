import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import time

hdu_list = fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data

# 1

for k in range(5):
    plt.axvline(1240/(13.6*(1/4 - 1/9)))
    plt.axvline(1240/(13.6*(1/4 - 1/16)))
    plt.axvline(1240/(13.6*(1/4 - 1/25)))
    plt.plot(10**logwave/10,flux[k],"g")
    plt.xlabel("lambda/nm")
    plt.ylabel("flux")
    plt.savefig("7-1-{wqe}.png".format(wqe=k))
    plt.clf()

# 2

Normalization = flux.sum(1)
normalizeflux = np.zeros((9713,4001))
for i in range(9713):
    normalizeflux[i] = flux[i] / Normalization[i]

# 3

Res = normalizeflux.sum(0)
residualflux = np.zeros((9713,4001))
for i in range(4001):
    residualflux[:,i] = normalizeflux[:,i] - Res[i]/9713

# 4

starttime = time.time()

C = np.dot(residualflux.T,residualflux)/9713
lamba, hU = np.linalg.eig(C)

print("time comsumption for diagonalization is",time.time()-starttime)

for k in range(5):
    plt.plot(10**logwave/10,hU.T[k])
    plt.xlabel("lambda/nm")
    plt.ylabel("flux")
    plt.savefig("7-4-{wqe}.png".format(wqe=k))
    plt.clf()

# 5

starttime = time.time()

Q,S,VT = np.linalg.svd(residualflux)

print("time comsumption for SVD is",time.time()-starttime)

print("The cosine of the angle between two vectors(from SVD method and PCA diagonialization method) is",np.dot(hU.T[0],-VT[0])/np.sqrt(np.dot(hU.T[0],hU.T[0])*np.dot(-VT[0],-VT[0])))


# 6

print("condition number for SVD:",S.max()/S.min())

print("condition number for PCA diagonialization:",lamba.max()/lamba.min())

# 7

coeffmatrice = np.dot(hU.T,residualflux.T)

for k in range(5):
    approx = (np.dot(coeffmatrice.T[:,0:5],hU.T[0:5])[k] + Res/9713)* Normalization[k]
    plt.plot(10**logwave/10,approx,label="approx")
    plt.plot(10**logwave/10,flux[k],label="real data")
    plt.legend()
    plt.xlabel("lambda/nm")
    plt.ylabel("flux")
    plt.savefig("7-7-{wqe}.png".format(wqe=k))
    plt.clf()

# 8

plt.plot(coeffmatrice[1,:],coeffmatrice[0,:],"+")
plt.xlabel("c1")
plt.ylabel("c0")
plt.savefig("7-8-1.png")
plt.clf()

plt.plot(coeffmatrice[2,:],coeffmatrice[1,:],"+")
plt.xlabel("c2")
plt.ylabel("c1")
plt.savefig("7-8-2.png")
plt.clf()

# 9

sd = []
for s in range(20):
    approx = (np.dot(coeffmatrice.T[:,0:s],hU.T[0:s])[0] + Res/9713)* Normalization[0]
    error = ((approx - flux[0])**2).sum()
    sd.append(error)
plt.plot(sd)
plt.xlabel("Nc")
plt.ylabel("Error for approximation")
plt.savefig("7-9.png")
plt.clf()










