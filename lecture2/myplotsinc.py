import numpy as np
import matplotlib.pyplot as plt

# Time axis 
Npt = 1000          # number of points in the time axis
T = 1e-9            # second
T1 = 0.2e-9         # second

# Build time axis 
t = np.linspace(-T/2, T/2, Npt )

# Calculate signal in the time domain
x = np.zeros( t.size )
i = 0

# for loop to estimate the signal
for tm in t:
    if (tm >= -T1/2) and (tm <= T1/2):
        x[ i ] = 1
    
    i += 1

# plot signal in the time domain
plt.close('all')
plt.figure(1)
plt.plot(t, x)

        
    



 

