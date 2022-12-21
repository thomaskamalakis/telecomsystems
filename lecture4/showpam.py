import commlib as cl
import numpy as np
import matplotlib.pyplot as plt
TS = 1e-9                   # Symbol duration

# symbols
ak = np.array([0.5, 0.25, 1.0, 0.5])

plt.close('all')

t, x = cl.pam_waveform1(ak, TS)
plt.figure()
cl.plot_signal(t, x, plot_type = '-o', close_all = True)


