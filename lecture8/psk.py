import commlib as cl
import matplotlib.pyplot as plt

M = 4
TS = 1e-9
samples_per_symbol = 200
f0 = 2e9
Nbits = 8

c = cl.psk_constellation( M = M )
x = cl.digital_signal( TS = TS, samples_per_symbol = samples_per_symbol,
                      constellation = c, fcarrier = f0 ) 
bits = cl.random_bits( Nbits )
x.modulate_from_bits( bits )
x.plot( close_all = True )
plt.grid()
