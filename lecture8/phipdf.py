import matplotlib.pyplot as plt
import numpy as np
import commlib as cl

M = 4
rSs = np.array([1,2,4,10])
plt.close('all')

for rS in rSs:
    SNRbdB = 10 * np.log10(rS / np.log2(M) )    
    s = cl.psk_constellation(M, SNRbdB = SNRbdB)
    phi = np.arange(-2*np.pi, 2*np.pi, 0.01)
    f = s.fphi(phi)
    
    plt.figure(1)
    plt.plot(phi, f, label = "$r_S = %d$" % rS)
    plt.xlabel('$\phi/\pi$')
    plt.ylabel('$f$')

plt.legend()