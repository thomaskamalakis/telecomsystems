import numpy as np
import matplotlib.pyplot as plt
from commlib import Qfunction

def psk_ser4( SNRS ):
    return 2 * Qfunction( np.sqrt(SNRS) ) * (1 - 0.5 * Qfunction( np.sqrt(SNRS) ) )
                         
def psk_ser(M, SNRS):
    rS = SNRS 
    vmax = 100
    Nphi = 1000
    v = np.arange(0, vmax, vmax/Nphi)
    phis = np.arange( np.pi/M, np.pi, np.pi/M/Nphi)
    f = np.zeros(phis.size)
    
    for i, phi in enumerate(phis):
        g = v * np.exp( -0.5 * ( v - np.sqrt(2*rS) * np.cos(phi) ) ** 2.0 )
        f[i] = 1/(2*np.pi) * np.exp( -rS*np.sin(phi) ** 2.0) * np.trapz(g,v)
      
    plt.figure(1)
    plt.plot(phis, f)
    return 2*np.trapz(f, phis)

plt.close('all')
M = 4
SNRbdB=np.arange(10, 10.1, 0.1)
SNRb = 10 ** (SNRbdB/10)
SNRS = SNRb * np.log2(M)
ser = np.zeros(SNRS.size)

for i, snrs in enumerate(SNRS):
    ser[i] = psk_ser(M, snrs)

print(ser)
print(psk_ser4 (SNRS) )