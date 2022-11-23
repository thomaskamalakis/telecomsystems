import numpy as np
import matplotlib.pyplot as plt

# function to create the square pulse
def square(t , T):    
    f = np.logical_and( t <= T / 2.0 , t >= -T/2.0 )
    return f.astype('float')

N = 1024
n = np.arange(-N / 2.0, N / 2.0, 1)  

# time axis
T = 4;
Tmax = 30.0
Dt = 2 * Tmax / N
t = n * Dt

# frequency axis
Df = 1.0 / (N * Dt)
f = n * Df

# signal in the time domain
x = square(t,T)

# signal in the frequency domain
X = Dt * np.fft.fftshift( np.fft.fft( np.fft.fftshift(x) ) )

# Analytical expression for the spectrum
X2= T * np.sinc( f * T ) 

# Plot results
plt.figure(1)
plt.xlabel('t [msec]')
plt.ylabel('x(t)')
plt.plot(t,x)

plt.figure(2)
plt.plot(t, X2, t, X, 'o')
plt.xlim(-3,3)
plt.legend(['analytical','numerical'])
plt.xlabel('f [kHz]')
plt.ylabel('X(f)')
