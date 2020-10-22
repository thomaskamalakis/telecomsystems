import commlib as cl
import matplotlib.pyplot as plt

f0 = 50
T = 1 / f0
Tmin = -T / 2
Tmax = +T / 2
N = 1000
A = 1

t = cl.time_axis(Tmin, Tmax, N)
x = cl.cos_signal(A, f0, t)

# Plot results
plt.close('all')
plt.figure(1)
plt.xlabel('t/T')
plt.ylabel('x(t)')
plt.plot( t/T , x )

print('Power computed using trapezium rule: ', cl.average_power(t, x) )