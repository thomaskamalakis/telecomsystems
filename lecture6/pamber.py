#---pamber1
from commlib import pam_simulation, Qfunction
import matplotlib.pyplot as plt
import numpy as np

SNRbdBs = np.arange(12, 20, 0.5)
max_iterations = 100000
report_step = 100
max_symbol_errors = 1000
M = 16
Pes = np.zeros( SNRbdBs.size )
Pes2 = np.zeros( SNRbdBs.size )
Peb = np.zeros( SNRbdBs.size )
Peb2= np.zeros( SNRbdBs.size )

for i, SNRbdB in enumerate(SNRbdBs):
    SNRb = 10 ** (SNRbdB / 10)
    q = 6 * SNRb * np.log2(M) / (M ** 2.0 - 1)
    Pes[i] = 2 * (M-1) / M * Qfunction ( np.sqrt(q) )
    Peb[i] = 2 * (M-1) / M * Qfunction ( np.sqrt(q) ) / np.log2(M)
    
    s = pam_simulation(M = M, SNRbdB = SNRbdB, 
                       max_iterations = max_iterations, 
                       report_step = report_step,
                       max_symbol_errors = max_symbol_errors) 
    s.execute()

    Pes2[i] = s.symbol_errors / s.iterations_performed
    Peb2[i] = s.bit_errors / s.iterations_performed / s.m

#---pamber2
    print('\nSymbol error ratio')
    print('Analytical result : %e' %Pes[i])
    print('Numerical  result : %e' %Pes2[i])
    
    print('\nBit error ratio')
    print('Analytical result : %e' %Peb[i])
    print('Numerical  result : %e' %Peb2[i])

plt.close('all')
plt.figure(1)
plt.semilogy(SNRbdBs, Pes)
plt.semilogy(SNRbdBs, Pes2,'o')
plt.xlabel('SNRb [dB]')
plt.ylabel('Symbol error ratio')
plt.title('M = %d' %M)

plt.figure(2)
plt.semilogy(SNRbdBs, Peb)
plt.semilogy(SNRbdBs, Peb2,'o')
plt.xlabel('SNRb [dB]')
plt.ylabel('Bit error ratio')
plt.title('M = %d' %M)


