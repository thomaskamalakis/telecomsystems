import numpy as np
from scipy.special import erfc

def Qfunction(x):
    return 0.5 * erfc( x / np.sqrt(2) )

Pt_specified = 1e-6

# beta = 0.1
M = 2
Rb = 10e9 # data rate [b/s]
Tb = 1 / Rb # bit duration [s]
TS = Tb * np.log2(M)
beta = np.sqrt(3 * Pt_specified / (M**2 - 1) )
N0 = 1e-22 #[ W/Hz ]

print('Tb = ', Tb, 's')
print('TS = ', TS, 's')

LdB = -40 # channel loss
L = 10 ** (LdB/10)
print('Channel loss in linear scale = ', L)

Pt = (M ** 2 - 1) * beta ** 2.0 / 3
print('Transmitted power = ', Pt, 'W')

Pr = L * Pt
print('Received power = ', Pr, 'W')

Er = Pr * TS
print('Received energy in one symbol duration = ', Er, 'J')

Eb = Pr * Tb
print('Received energy in one bit duration = ', Eb, 'J')

SNRb = Eb / N0
print('Signal-to-noise per bit = ', SNRb)

SNRbdB = 10 * np.log10(SNRb)
print('Signal-to-noise per bit = ', SNRbdB)
q = np.sqrt( 6 * SNRb * np.log2(M) / (M**2 - 1) )
Pb = 2 * (M-1) / (M * np.log2(M) ) * Qfunction(q)

print('Error probability : %e' %Pb)

B = 1 / TS
print('Bandwidth : ', B, 'Hz')
print('Bandwidth : ', B/1e9, 'GHz')








