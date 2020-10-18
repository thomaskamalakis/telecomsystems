import numpy as np
import matplotlib.pyplot as plt

# Time axis
Npt = 1000                          # number of points in the time axis
T = 1e-9                            # total signal duration [s]
T1 = 0.2e-9                         # pulse "on" duration [s]
t = np.linspace(-T/2, T/2, 1000)    # time axis

# Frequency axis
Npf = 1000                          # number of points in the frequency axis
Fmax = 40e9                         # maximum frequency
f = np.linspace(-Fmax, Fmax, 1000)  # frequency axis

# Time signal
x = np.zeros(t.size)
i = 0

for tm in t:
    if np.abs(tm) <= T1/2.0:
        x[i] = 1
    i = i + 1

X = np.sinc( f * T1 )

plt.close('all')
plt.figure(1)
plt.plot(t, x)
plt.savefig
plt.figure(2)
plt.plot(t, X)

