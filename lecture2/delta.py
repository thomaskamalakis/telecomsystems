import numpy as np
import matplotlib.pyplot as plt

def delta(t, Dt):
    x = np.zeros(t.size)

    for i, tm in enumerate(t):
        if -Dt/2.0 <= tm <= Dt/2.0:
            x[i] = 1.0/Dt
            
    return x

Dts = np.array([0.1, 0.05, 0.025, 0.01])
t = np.arange(-0.2, 0.2, 0.001)

plt.close('all')
plt.figure(1)

for Dt in Dts:
    x = delta(t,Dt)
    label = 'Dt=' + str(Dt)
    plt.plot(t, x, label = label)

plt.legend()
