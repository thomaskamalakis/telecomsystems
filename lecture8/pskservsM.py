from commlib import psk_constellation
import matplotlib.pyplot as plt
import numpy as np

SNRbdBs = np.arange(0.5, 25, 0.5)
n = np.arange(1,7,1)
Ms = np.array([2, 4, 8, 16, 32])
Ms = Ms.astype(int)

Pest = np.zeros( [SNRbdBs.size, Ms.size] )
Pebt = np.zeros( [SNRbdBs.size, Ms.size] )

threshold = 1e-4

for i, SNRbdB in enumerate(SNRbdBs):
    for j, M in enumerate(Ms):
        c = psk_constellation(M = M, SNRbdB = SNRbdB)
        Pest[i,j] = c.ser()
        Pebt[i,j] = c.ber()
        print('M = %d, SNRbdB = %6.2f Pe = %e' % (M,SNRbdB, Pest[i,j]))

plt.close('all')

for j, M in enumerate(Ms):
    plt.figure(1)
    plt.semilogy( SNRbdBs, Pest[:,j], label = 'M = %d' % M)
    plt.figure(2)
    plt.semilogy( SNRbdBs, Pebt[:,j], label = 'M = %d' % M)
    
plt.figure(1)
plt.xlabel('SNRb [dB]')
plt.ylabel('SER')
plt.legend()
plt.ylim([1e-5, 1])
    
plt.figure(2)
plt.xlabel('SNRb [dB]')
plt.ylabel('BER')
plt.legend()
plt.ylim([1e-5, 1])
