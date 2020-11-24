import commlib as cl
import matplotlib.pyplot as plt

M = 4
s = cl.psk_simulation(M = M, SNRbdB = 20, keep_realizations = True, max_iterations = 10000,
                      max_symbol_errors = 10000)
s.execute()
plt.close('all')
s.plot_constellation()

s = cl.psk_simulation(M = 16, SNRbdB = 30, keep_realizations = True, max_iterations = 10000,
                      max_symbol_errors = 10000)
s.execute()
s.plot_constellation()


