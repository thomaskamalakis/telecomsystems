from commlib import psk_simulation, psk_constellation
import matplotlib.pyplot as plt
import numpy as np

SNRbdBs = np.arange(10, 10.5, 0.5)
n = np.arange(1,7,1)
Ms = np.array([4])
Ms = Ms.astype(int)

Pes = np.zeros( [SNRbdBs.size, Ms.size] )
Peb = np.zeros( [SNRbdBs.size, Ms.size] )
Pest = np.zeros( [SNRbdBs.size, Ms.size] )
Pebt = np.zeros( [SNRbdBs.size, Ms.size] )

threshold = 1e-4

for i, SNRbdB in enumerate(SNRbdBs):
    for j, M in enumerate(Ms):
        
        s = psk_simulation(max_iterations = int(1e7), 
                           M = M, SNRbdB = SNRbdB, report_step = 10, 
                           keep_realizations = False, 
                           max_symbol_errors = 100)
        #Pest[i,j] = s.constellation.ser() 
        c = psk_constellation(M = M, SNRbdB = SNRbdB)
        Pest[i,j] = c.ser()
#        s.execute()
#        Pes[i, j] = s.symbol_errors / s.iterations_performed
#        Peb[i, j] = s.bit_errors / s.iterations_performed / np.log2(M)
#        if Pes[i,j] < threshold:
#            break
#        print('M = %d, SNRbdB = %6.2f Pe = %e / %e' % (M,SNRbdB, Pes[i,j], Pest[i,j]))

        print('M = %d, SNRbdB = %6.2f Pe = %e' % (M,SNRbdB, Pest[i,j]))

#plt.close('all')

for j, M in enumerate(Ms):
    plt.figure(1)
    plt.semilogy( SNRbdBs, Pest[:,j], label = 'M = %d' % M)
#    plt.figure(2)
#    plt.semilogy( SNRbdBs, Peb[:,j], label = 'M = %d' % M)
    
plt.figure(1)
plt.xlabel('SNRb [dB]')
plt.ylabel('SER')
plt.legend()
plt.ylim([1e-5, 1])
    
#plt.figure(2)
#plt.xlabel('SNRb [dB]')
#plt.ylabel('BER')
#plt.legend()
#plt.ylim([1e-5, 1])
