import numpy as np
import matplotlib.pyplot as plt

Tmax = 100
T = 10
f0 = 0.5

t = np.arange(0, Tmax, 0.01)
g = np.exp( -(t - Tmax/2.0) ** 2.0 / T ** 2.0)
c = np.cos(2 * np.pi * f0 * t )

plt.close('all')
plt.figure(1)
plt.plot(t,g)

plt.figure(2)
plt.plot(t,c)

plt.figure(3)
plt.plot(t, g * c )

plt.figure(4)
plt.plot(t, g * c **2.0 )

I1 = np.trapz( g, t )

I2 = np.trapz( g * c , t )

I3 = np.trapz( g * c ** 2.0, t )

print('Pulse integral : %e' % I1)
print('Pulse times carrier integral : %e' % I2)
print('Pulse times carrier squared integral : %e' % I3)
