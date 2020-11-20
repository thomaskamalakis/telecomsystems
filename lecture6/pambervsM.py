from commlib import pam_constellation
import matplotlib.pyplot as plt
import numpy as np

SNRbdBs = np.arange(5, 40, 0.1)
n = np.arange(1,7,1)
Ms = 2 ** n
Ms = Ms.astype(int)

Pes = np.zeros( [SNRbdBs.size, Ms.size] )
Peb = np.zeros( [SNRbdBs.size, Ms.size] )

for i, SNRbdB in enumerate(SNRbdBs):
    for j, M in enumerate(Ms):
        
        c = pam_constellation( M = M, SNRbdB = SNRbdB )
        Pes[i, j] = c.ser()
        Peb[i, j] = c.ber()
        

plt.close('all')

for j, M in enumerate(Ms):
    plt.figure(1)
    plt.semilogy( SNRbdBs, Pes[:,j], label = 'M = %d' % M)
    plt.figure(2)
    plt.semilogy( SNRbdBs, Peb[:,j], label = 'M = %d' % M)
    
plt.figure(1)
plt.xlabel('SNRb [dB]')
plt.ylabel('SER')
plt.legend()
plt.ylim([1e-12, 1])
    
plt.figure(2)
plt.xlabel('SNRb [dB]')
plt.ylabel('BER')
plt.legend()
plt.ylim([1e-12, 1])
