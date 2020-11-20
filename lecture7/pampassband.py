import matplotlib.pyplot as plt
import commlib as cl
import numpy as np

# Parameters
TS = 1e-9
samples_per_symbol = 40
tguard = 1 * TS
f0 = 1 / TS
N0 = 1e-10
B = 2e9
f0 = 2e9
tinitial = 3/ f0 /4

# system transfer function
H = lambda f : np.exp( -f**2.0 / f0 ** 2.0 / 2)

# Signal constellation
c = cl.pam_constellation(16, title = '16-PAM')

# Plot PAM constellation
plt.close('all')
c.plot()
c.plot_map()

# set bits to be transmitted
bits = cl.random_bits(32)

# build input waveform and plot
x = cl.digital_signal(TS = TS, samples_per_symbol = samples_per_symbol, 
                      tinitial = tinitial, tguard = tguard, constellation = c,
                      fcarrier = f0)
x0 = cl.digital_signal(TS = TS, samples_per_symbol = samples_per_symbol, 
                      tinitial = tinitial, tguard = tguard, constellation = c,
                      fcarrier = 0)

x.modulate_from_bits( bits, constellation = c )
x0.modulate_from_bits( bits, constellation = c )

plt.close('all')
plt.figure(1)
plt.plot(x.t, x.samples, 'r', label = 'passband PAM')
plt.plot(x0.t, x0.samples, 'b--', label = 'baseband PAM')
plt.legend()