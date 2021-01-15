import numpy as np
import matplotlib.pyplot as plt

p = np.arange(0.001, 0.999, 0.001)
H = - p * np.log2(p) - (1 - p) * np.log2(1-p)

plt.close('all')
plt.figure(1)
plt.plot(p, H)
plt.xlabel('p')
plt.ylabel('H')

