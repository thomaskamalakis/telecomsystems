import commlib as cl
import matplotlib.pyplot as plt

pam_map = cl.pam_gray_map(16)
plt.close('all')
cl.plot_map(pam_map, disp_y = 0.05)
plt.ylim([-1, 1])
