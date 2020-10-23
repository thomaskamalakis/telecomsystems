import numpy as np
import matplotlib.pyplot as plt

# Time axis 
Npt = 1000          # number of points in the time axis
T = 1e-9            # second
T1 = 0.1e-9         # second

# Frequency axis
Npf = 1000
Fmax = 40e9

# Build time axis 
t = np.linspace(-T/2, T/2, Npt )

# Build frequency axis
f = np.linspace(-Fmax, Fmax, Npf )

# Calculate signal in the time domain
x = np.zeros( t.size )

# for loop to estimate the signal
x = np.logical_and(t >= -T1/2, t <= T1/2).astype(float)

# signal spectrum
X = T1 * np.sinc( f * T1 )

# plot signal in the time domain
plt.close('all')
plt.figure(1)
plt.plot(t, x)

# plot signal spectrum 
plt.figure(2)
plt.plot(f, X)
        
    



 

