import matplotlib.pyplot as plt
import commlib as cl

# time axis
T = 4;
Tmax = 30.0
N = 1024

t = cl.time_axis( −Tmax, +Tmax, N)
f = cl.frequency_axis(t)
x = cl.square(t, T)
X = cl.spectrum(t, x)

# Analytical expression for the spectrum
X2= T ∗ np.sinc( f ∗ T )

plt.close(’all’)

# Plot results
plt.figure(1)
plt.xlabel(’t [msec]’)
plt.ylabel(’x(t)’)
plt.plot(t,x)
plt.figure(2)
plt.plot(t,np.real(X2),t,X,’o’)
plt.xlim(−3,3)
plt.legend([’analytical’,’numerical’])
plt.xlabel(’f [kHz]’)
plt.ylabel(’X(f)’)