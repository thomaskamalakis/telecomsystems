import numpy as np
import matplotlib.pyplot as plt

sigma = 1
x = np.linspace(-8, 8, 10000)

f = 1 / np.sqrt(2*np.pi) / sigma * np.exp( -x ** 2.0 / 2 / sigma ** 2)

plt.close('all')
plt.figure()
plt.plot(x, f)

I = np.trapz(f, x)
print('I = ', I)