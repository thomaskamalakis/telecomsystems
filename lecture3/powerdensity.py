import commlib as cl
import matplotlib.pyplot as plt
import numpy as np

T = 10
T1 = 1
N = 1000

t = cl.time_axis(-T, T, N)
x = cl.square(t, T1)
f = cl.frequency_axis(t)
Sx = cl.power_density(t, x)

plt.close('all')
cl.plot_signal(t, x, xlabel = 't',
               ylabel = 'x', figure_no = 1)
   
cl.plot_signal(f, Sx, xlabel = 'f',
               ylabel = 'Sx', figure_no = 2)

# calculate average power
T = np.max(t) - np.min(t)
Et = cl.energy(t, x) / T
Ef = np.trapz(Sx, f)

print('Average power :', Et)
print('Average power from power density :', Ef)
        