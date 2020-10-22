import commlib as cl
import matplotlib.pyplot as plt

T = 10
T1 = 1
N = 1000

t = cl.time_axis(-T, T, N)
x = cl.square(t, T1)
f = cl.frequency_axis(t)
X = cl.spectrum(t, x)

plt.close('all')
cl.plot_signal(t, x, xlabel = 't',
               ylabel = 'x', figure_no = 1)
   
cl.plot_signal(f, X, xlabel = 'f',
               ylabel = 'X', figure_no = 2)

Et = cl.energy(t, x)
Ef = cl.energy(f, X)

print('Energy in the time domain :', Et)
print('Energy in the frequency domain :', Ef)
    