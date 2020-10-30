import matplotlib.pyplot as plt
import numpy as np
from commlib import time_axis, frequency_axis, square, spectrum

# time axis
T = 4
Tmax = 30.0
N = 1024

t = time_axis( Tmax, N)
f = frequency_axis(t)
x = square(t, T)
X = spectrum(t, x)

# Analytical expression for the spectrum
X2= T * np.sinc( f * T ) 

plt.close('all')

# Plot results
plt.figure(1)
plt.xlabel('t [msec]')
plt.ylabel('x(t)')
plt.plot(t,x)
plt.figure(2)

plt.plot(f, X2, f, X, 'o')
plt.xlim([-0.5, 0.5])
plt.legend(['analytical','numerical'])
plt.xlabel('f [kHz]')
plt.ylabel('X(f)')