from numpy.random import normal
import numpy as np
import matplotlib.pyplot as plt

save_path = '/home/thkam/Documents/Presentations/TelecomSystems/lecture3/'
mu = 1
sigma = 2

Nsamples = np.arange(100, 10000, 100)
expectations = np.zeros( Nsamples.size )

func = lambda x : x ** 2.0

# iterate over different N values
for i, N in enumerate(Nsamples):
    xn = normal(mu, sigma, N)
    expectations[i] = np.mean( func(xn) )
    
    
# Plot expectations
plt.close('all')

plt.figure(1)
plt.plot(Nsamples, expectations)
plt.title('Expectations vs Nsamples')
plt.xlabel('Nsamples')
plt.ylabel('Expected Value')
plt.savefig(save_path + 'convsquare.png')
