import numpy as np
import matplotlib.pyplot as plt
import commlib as cl

T = 4;
Tmax = 30.0
N = 1024
Fmax = 20.0/T

t = cl.time_axis(-Tmax, +Tmax, N)         # time axis
x = cl.square(t,T)                        # input signal
Hc = lambda f : cl.square_filter(f, Fmax) # filter callable

y = cl.system_action(t, x, Hc)

f = cl.frequency_axis(t)
X = cl.spectrum(t,x)
Y = cl.spectrum(t,y)

plt.close('all')
plt.figure(1)
plt.title('Fmax * T =' + str(Fmax*T))
plt.xlabel('f [kHz]')
plt.ylabel('Spectrum')
plt.plot(t, np.abs(X), '--', label='|X(f)|')
plt.plot(t, np.abs(Y), label='|Y(f)|')
plt.xlim([-10, 10])
plt.legend()
