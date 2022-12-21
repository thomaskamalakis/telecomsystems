import matplotlib.pyplot as plt
import commlib as cl
import numpy as np

# Parameters
TS = 1e-9
samples_per_symbol = 20
tinitial = 0
tguard = 10 * TS
f0 = 10 / TS
N0 = 1e-10
B = 3e9
Nbits = 32

# system transfer function
H = lambda f : np.exp( -f**2.0 / f0 ** 2.0 / 2)

# Signal constellation
c = cl.pam_constellation(4, title = '4-PAM')

# Plot PAM constellation
plt.close('all')
c.plot()
c.plot_map()

# set bits to be transmitted
bits = cl.random_bits(Nbits)

# build input waveform and plot
x = cl.digital_signal(TS = TS, samples_per_symbol = samples_per_symbol, 
                      tinitial = tinitial, tguard = tguard, constellation = c)

x.modulate_from_bits( bits, constellation = c )
x.plot()

# create channel system and apply
#s = cl.system(input_signal = x, transfer_function = H)
#s.apply()

# get output signal and plot
#y = s.get_output()
#y.plot()

n = cl.white_noise(N0 = N0, B = B, t = x.t)
n.plot()

z = x + n
z.plot()