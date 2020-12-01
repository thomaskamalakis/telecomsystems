from commlib import pam_constellation, psk_constellation
import matplotlib.pyplot as plt
import numpy as np

SNRbdBs = np.arange(4, 25, 1)
M = 4

PesPAM = np.zeros( SNRbdBs.size )
PebPAM = np.zeros( SNRbdBs.size )
PesPSK = np.zeros( SNRbdBs.size )
PebPSK = np.zeros( SNRbdBs.size )

for i, SNRbdB in enumerate(SNRbdBs):

    cpsk = psk_constellation(M, SNRbdB = SNRbdB)
    cpam = pam_constellation(M, SNRbdB = SNRbdB)
    
    PesPAM[i] = cpam.ser()
    PesPSK[i] = cpsk.ser()
    PebPAM[i] = cpam.ber()
    PebPSK[i] = cpsk.ber()
    
plt.close('all')

plt.figure(1)
plt.semilogy( SNRbdBs, PesPAM, label = '%d-PAM' %M)
plt.semilogy( SNRbdBs, PesPSK, label = '%d-PSK' %M)
plt.xlabel('SNRb [dB]')
plt.ylabel('SER')
plt.legend()
plt.title('PSK vs PAM SER for M=%d' %M)
plt.ylim([1e-6, 1])

plt.figure(2)
plt.semilogy( SNRbdBs, PebPAM, label = '%d-PAM' %M)
plt.semilogy( SNRbdBs, PebPSK, label = '%d-PSK' %M)
plt.xlabel('SNRb [dB]')
plt.ylabel('BER')
plt.legend()
plt.title('PSK vs PAM BER for M=%d' %M)
plt.ylim([1e-6, 1])
