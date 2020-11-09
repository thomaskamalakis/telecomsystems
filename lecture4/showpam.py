import commlib as cl
import numpy as np

TS = 1e-3                   # Symbol duration

# symbols
ak = np.array([0.5, 0.25, 1.0, 0.5])

t, x = cl.pam_waveform1(ak, TS)
cl.plot_signal(t, x, plot_type = '-o', close_all = True)


