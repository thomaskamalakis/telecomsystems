import matplotlib.pyplot as plt
import commlibv2 as cl

T = 0.1
T1 = 0.01
N = 1024
f0 = 20

t = cl.time_axis(-T, T, N)
#carrier = cl.carrier(t, f0)
#carrier.plot(close_all = True)
#
#pulse = cl.square_pulse(t, T1)
#pulse.plot()
#pulse.calc_spectrum()
#pulse.plot(what = 'spectrum')
#
#w = carrier.windowed(-T/2, T/2)
#w.plot()
#
#

plt.close('all')
c = cl.pam_constellation(16, title = '16-PAM')
c.plot()
c.plot_map()

bits = cl.random_bits(32)
#symbols = c.bits_to_symbols( bits )
z = cl.digital_signal(TS = 1e-6, samples_per_symbol = 10, 
                      tinitial = 0, tguard = 0.0, constellation = c)
z.modulate_from_bits( bits, constellation = c )
z.plot()