import commlib as cl
import numpy as np
import matplotlib.pyplot as plt

def inner_product( f, g, t):
    return np.trapz( f * g, t)

def psk_symbols(i, M):
    return i * 2 * np.pi / M

f0 = 2.5e9
RS = 40e6
TS = 1/RS

N = 10000
M = 4
Nsymbols = 1000

t = np.linspace(-TS, TS, N)
p = cl.square_pulse(t, TS)

Ep = p.energy()

p1 =   np.sqrt(2/Ep) * np.cos(2 * np.pi * f0 * t) * p.samples
p2 = - np.sqrt(2/Ep) * np.sin(2 * np.pi * f0 * t) * p.samples

norm1 = inner_product(p1, p1, t)
norm2 = inner_product(p2, p2, t)
inner = inner_product(p1, p2, t)


fq = np.linspace(0, 2*np.pi, M + 1)
x = np.sqrt(Ep/2) * np.cos( fq )
y = np.sqrt(Ep/2) * np.sin( fq )

plt.close('all')
plt.plot(x, y, 'o')
plt.axis('equal')

i_tr = np.random.randint(0, M, Nsymbols)
phase_tr = psk_symbols(i_tr, M)
x_tr = np.cos( phase_tr )
y_tr = np.sin( phase_tr )
plt.figure()
plt.plot(x_tr, y_tr, 'o')
plt.axis('equal')

x_rx = x_tr + np.random.randn( x_tr.size ) * 0.4
y_rx = y_tr + np.random.randn( y_tr.size ) * 0.4

plt.figure()
plt.plot(x_rx, y_rx, 'o')
plt.axis('equal')









