import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft,irfft

datapiano = np.loadtxt("piano.txt")
datatrumpet = np.loadtxt("trumpet.txt")



plt.plot(datapiano)
plt.xlabel("datapoint")
plt.ylabel("waveform")
plt.savefig("8-2-1.png")
plt.clf()


plt.plot(datatrumpet)
plt.xlabel("datapoint")
plt.ylabel("waveform")
plt.savefig("8-2-2.png")
plt.clf()

plt.plot(np.arange(5000,7000),datapiano[5000:7000])
plt.xlabel("datapoint")
plt.ylabel("waveform")
plt.savefig("8-2-3.png")
plt.clf()


plt.plot(np.arange(5000,7000),datatrumpet[5000:7000])
plt.xlabel("datapoint")
plt.ylabel("waveform")
plt.savefig("8-2-4.png")
plt.clf()

a = rfft(datapiano)
b = rfft(datatrumpet)

plt.plot(np.abs(a)[0:10000])
plt.xlabel("Fourier coefficient")
plt.ylabel("value for fourier coefficient")
plt.savefig("8-2-5.png")
plt.clf()

plt.plot(np.abs(b)[0:10000])
plt.xlabel("Fourier coefficient")
plt.ylabel("value for fourier coefficient")
plt.savefig("8-2-6.png")
plt.clf()