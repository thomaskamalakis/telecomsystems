from numpy.random import normal
import numpy as np
import matplotlib.pyplot as plt

save_path = '/home/thkam/Documents/Presentations/TelecomSystems/lecture3/'
mu = 1
sigma1 = 2
sigma2 = 6
Nsamples = 1000

xn1 = normal(mu, sigma1, Nsamples)
xn2 = normal(mu, sigma2, Nsamples)

plt.close('all')

plt.figure(1)
plt.plot(xn2,'s', label = 'sigma=6')
plt.plot(xn1,'s', label = 'sigma=2')

plt.xlabel('index')
plt.ylabel('sample')
plt.legend()
plt.savefig(save_path + 'demostd.png')
