#---firstpart
from commlib import psk_simulation, psk_constellation
import matplotlib.pyplot as plt
import numpy as np

SNRbdBs = np.arange(4, 18, 0.5)
M = 16

Pes = np.zeros( SNRbdBs.size )
Peb = np.zeros( SNRbdBs.size )
Pest = np.zeros( SNRbdBs.size )
Pebt = np.zeros( SNRbdBs.size )

threshold = 1e-5

for i, SNRbdB in enumerate(SNRbdBs):
        
    s = psk_simulation(max_iterations = int(1e6), 
                       M = M, SNRbdB = SNRbdB, report_step = 100000, 
                       keep_realizations = False, 
                       max_symbol_errors = 100,
                       report = True)
    Pest[i] = s.constellation.ser() 
    c = psk_constellation(M = M, SNRbdB = SNRbdB)
    Pest[i] = c.ser()
    Pebt[i] = c.ber()    
    s.execute()
    Pes[i] = s.symbol_errors / s.iterations_performed
    Peb[i] = s.bit_errors / s.iterations_performed / np.log2(M)
    if Pes[i] < threshold:
        break
    print('M = %d, SNRbdB = %6.2f Pe = %e / %e' % (M,SNRbdB, Pes[i], Pest[i]))
    print('M = %d, SNRbdB = %6.2f Pe = %e' % (M,SNRbdB, Pest[i]))

#---secondpart
plt.close('all')

plt.figure(1)
plt.semilogy( SNRbdBs, Pest, label = 'theoretical')
plt.semilogy( SNRbdBs, Pes, 'o', label = 'numerical')

plt.figure(2)
plt.semilogy( SNRbdBs, Peb, label = 'theoretical')
plt.semilogy( SNRbdBs, Pebt, 'o', label = 'numerical')
    
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