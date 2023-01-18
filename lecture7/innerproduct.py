import commlib as cl
import numpy as np
import matplotlib.pyplot as plt

f0 = 2.5e9
RS = 40e6
TS = 1/RS

N = 10000
t = np.linspace(-TS, TS, N)
p = cl.square_pulse(t, TS)

c = cl.carrier(t, f0)

plt.close('all')
p.plot()
c.plot()

psamples = p.samples
to_intergrate = p.samples ** 2 * np.sin(4 * np.pi * f0 * t)
plt.figure()
plt.plot(t, to_intergrate)

I = np.trapz( to_intergrate, t )

I0 = np.trapz( psamples ** 2, t)