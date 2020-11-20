import commlib as cl
import numpy as np
import matplotlib.pyplot as plt

# Time axis
T = 10
TS = 1.0
N = 1024
f0 = 20

# time axis
t = cl.time_axis(-T, T, N)

# PAM constellation
M = 16
c = cl.pam_constellation(M)
Pavg = c.avg_power()

# PAM pulse shape
p = cl.square_pulse(t, TS)
p.calc_spectrum()
f, P = p.get_spectrum()

# baseband PAM power spectral density
SXX = Pavg / TS * np.abs(P) ** 2.0

# Plot psd
plt.close('all')
plt.figure(1)
plt.plot(f, SXX, label = 'baseband')

# SXX callable
SXXc = lambda freq : np.interp(freq, f, SXX)

# PAM bandpass psd
SYY = ( SXXc(f-f0) + SXXc(f+f0) )/4.0
plt.plot(f, SYY, label = 'bandpass')
plt.grid()
plt.xlabel('f')
plt.ylabel('PSD')
plt.legend()


