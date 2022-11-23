import numpy as np
import matplotlib.pyplot as plt
import commlib as cl

T = 4;
Tmax = 30.0
N = 1024
Fmax = 2.0/T
m = 10
# def Hc(f):
#     return cl.square_filter(f, Fmax)
def pulse(t, T, m):
    return np.exp( -t**(2*m) / T ** (2*m) )

def Hc(f):
    return np.exp( -f**2 / Fmax**2.0)
t = cl.time_axis(Tmax, N)         # time axis
x = pulse(t, T, m)
#x = cl.square(t,T)                        # input signal

# Hc = lambda f : cl.square_filter(f, Fmax) # filter callable

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

plt.figure()
X = cl.spectrum(t, x)
Y = cl.spectrum(t, y)
f = cl.frequency_axis(t)
H = Hc(f)

plt.plot(f, np.real(X) / np.max(np.real(X)) )
plt.plot(f, np.real(Y) / np.max(np.real(Y)) )
plt.plot(f, H )


















