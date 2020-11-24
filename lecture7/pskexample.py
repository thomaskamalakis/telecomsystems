import commlib as cl
import matplotlib.pyplot as plt

M = 16
c = cl.psk_constellation(M)
plt.close('all')
c.plot_map(rotation = 0)