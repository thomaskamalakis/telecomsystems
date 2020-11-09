import commlib as cl
import numpy as np

N = 1024
TS = 1e-9
T = 20 * TS
sa2 = 1.0

t = cl.time_axis(T, N)
p = cl.square(t, TS)
f = cl.frequency_axis(t)
P = cl.spectrum(t, p)

SX = sa2 / TS * np.abs(P)**2.0

cl.plot_signal(f / 1e9, SX, close_all = True, xlabel = 'f [GHz]', ylabel = 'SX')
 
cl.plot_signal(f * TS, SX / np.max(SX), 
               xlabel = 'f * TS', ylabel = 'SX [normalized]', 
               xlim = [-1, 1], show_grid = True)

SX1 = cl.window(f, SX, -1/TS, +1/TS)
total = np.trapz(SX, f)
total1 = np.trapz(SX1, f)
print('power fraction :', total1/total )



