from numpy.random import normal, uniform
import matplotlib.pyplot as plt

save_path = '/home/thkam/Documents/Presentations/TelecomSystems/lecture3/'
mu = 1
sigma = 2
a = 1
b = 2

Nsamples = 1000

# normal distribution
xn = normal(mu, sigma, Nsamples)

# uniform distribution
xu = uniform(a, b, Nsamples)

# Plot samples
plt.close('all')

plt.figure(1)
plt.plot(xn,'s')
plt.title('Normal distribution')
plt.savefig(save_path + 'normalsamples.png')

plt.figure(2)
plt.plot(xu,'s')
plt.title('Uniform distribution')
plt.savefig(save_path + 'uniformsamples.png')
