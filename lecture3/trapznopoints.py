import commlib as cl
import matplotlib.pyplot as plt
import numpy as np

f0 = 50
T = 1 / f0
Tmin = -T / 2
Tmax = +T / 2
A = 1

# number of points considered in each simulation
Ns = np.arange(10, 1000, 10)
Ps = np.zeros( Ns.size )

for i, N in enumerate(Ns):
    t = cl.time_axis(Tmin, Tmax, N)
    x = cl.cos_signal(A, f0, t)
    Ps[ i ] = cl.average_power(t, x)
    print('Power computed using trapezium rule using ', 
           N, ' points is : ', Ps[ i ] )
    
plt.close('all')
plt.plot(Ns, Ps)
plt.xlabel('N')
plt.ylabel('P')
        
    