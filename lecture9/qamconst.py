import commlib as cl
import numpy as np
import matplotlib.pyplot as plt

M = 16
c = cl.qam_constellation(M)
plt.close('all')
c.plot_map(rotation = 0)

TS = 1e-9
Nsymbols = 10
samples_per_symbol = 100
Nbits = int( np.log2(M) * Nsymbols )
bits = cl.random_bits(Nbits)
fcarrier = 2 / TS

s = cl.digital_signal(constellation = c, 
                      fcarrier = fcarrier, 
                      TS = TS, samples_per_symbol = samples_per_symbol,
                      phi0 = np.pi/2.0)

s.modulate_from_bits(bits)
s.plot()