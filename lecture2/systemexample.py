import numpy as np
import matplotlib.pyplot as plt
import commlib as cl

T = 4;
Tmax = 30.0
N = 1024
Fmax = 5.0/T

t = cl.time_axis(Tmax, N)         # time axis
x = cl.square(t,T)                        # input signal

Hc = lambda f : cl.square_filter(f, Fmax) # filter callable

y = cl.system_action(t, x, Hc)


plt.close('all')
plt.figure(1)
plt.title('Fmax * T =' + str(Fmax*T))
plt.xlabel('t [ms]')
plt.ylabel('Signal')
plt.plot(t, np.real(x), label='x(t)')
plt.plot(t, np.real(y), label='y(t)')
plt.legend()
plt.xlim(-6,6)
