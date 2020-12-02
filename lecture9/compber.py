#---firstpart
from commlib import pam_constellation, psk_constellation, qam_constellation
import matplotlib.pyplot as plt
import numpy as np

SNRbdBs = np.arange(4, 30, 0.5)
Ms = np.array([16, 64])
Ms = Ms.astype(int)

Pest = {}
Pebt = {}
for key in ['pam','psk','qam']:
    Pest[key] = np.zeros( [SNRbdBs.size, Ms.size] )
    Pebt[key] = np.zeros( [SNRbdBs.size, Ms.size] )

for i, SNRbdB in enumerate(SNRbdBs):
    for j, M in enumerate(Ms):
        cpam = pam_constellation(M = M, SNRbdB = SNRbdB)
        Pest['pam'][i,j] = cpam.ser()
        Pebt['pam'][i,j] = cpam.ber()
        cpsk = psk_constellation(M = M, SNRbdB = SNRbdB)
        Pest['psk'][i,j] = cpsk.ser()
        Pebt['psk'][i,j] = cpsk.ber()        
        cqam = qam_constellation(M = M, SNRbdB = SNRbdB)
        Pest['qam'][i,j] = cqam.ser()
        Pebt['qam'][i,j] = cqam.ber()
        print('M = %d, SNRbdB = %6.2f' % (M, SNRbdB) )

#---secondpart
plt.close('all')

for j, M in enumerate(Ms):
    plt.figure(1)
    plt.semilogy( SNRbdBs, Pest['pam'][:,j], '-d', label = 'PAM M = %d' % M)
    plt.semilogy( SNRbdBs, Pest['psk'][:,j], '-o', label = 'PSK M = %d' % M)
    plt.semilogy( SNRbdBs, Pest['qam'][:,j], '-s', label = 'QAM M = %d' % M)
    plt.figure(2)
    plt.semilogy( SNRbdBs, Pebt['pam'][:,j], '-d', label = 'PAM M = %d' % M)
    plt.semilogy( SNRbdBs, Pebt['psk'][:,j], '-o', label = 'PSK M = %d' % M)
    plt.semilogy( SNRbdBs, Pebt['qam'][:,j], '-s', label = 'QAM M = %d' % M)
    plt.figure(2)
    
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
#---thirdpart
