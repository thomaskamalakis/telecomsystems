#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:44:54 2019

@author: thomas
"""
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import special

def Qfunction(x):    
    return 0.5 * special.erfc( x / np.sqrt(2.0) )

def pam_symbol(m,M):
    return 2.0 * m - M + 1.0
    
def random_symbols(Q,M):    
    indxs = [random.randint(0,M-1) for i in range(int(Q))]
    indxs = np.array(indxs)
    symbols = pam_symbol(indxs,M)
    return symbols

def shortest_distance(symbols,constellation):
    
    decoded_symbols = np.zeros(symbols.size)
    
    for i,symbol in enumerate(symbols):
        d = np.abs(symbol - constellation)
        p = np.argmin(d)
        decoded_symbols[i] = constellation[p]
    
    return(decoded_symbols)

def count_errors(symbols1,symbols2):
    e = (np.abs(symbols2 - symbols1) > 0 ).astype(int)
    return np.sum(e)
            
Q = 1e6
SNRsperbitdB = np.arange(7.0,18.0,1.0)
M = 4

SNRperbits = 10.0 ** (SNRsperbitdB / 10.0)
SNRs = SNRperbits * np.log2(M)
signal_power = (M**2.0-1.0) / 3.0
noise_powers = signal_power / SNRs / 2

errors = np.zeros(SNRs.size)
Ps = np.zeros(SNRs.size)

constellation = pam_symbol(np.arange(M),M)
Ns = noise_powers.size

for i,noise_power in enumerate(noise_powers):
    symbols = random_symbols(Q,M)
    noise = np.sqrt(noise_power) * np.random.randn(int(Q))
    received_samples = symbols + noise
    received_symbols = shortest_distance(received_samples,constellation)
    errors[i] = count_errors(received_symbols,symbols)
    Ps[i] = errors[i] / Q
    print('Starting iteration for %d /%d errors = %d' %(i+1, Ns, errors[i] ) )

g = 6.0 * np.log2(M) / ( M**2-1 ) * SNRperbits
Pb = Ps / np.log2(M)

Ps_an = 2.0 * (M - 1) / M *Qfunction( np.sqrt(g) )
Pb_an = Ps_an / np.log2(M)
  
plt.close('all')
plt.figure()    
plt.semilogy(SNRsperbitdB,Ps,'ro',label='numerical')
plt.semilogy(SNRsperbitdB,Ps_an,label='analytical')
plt.xlabel('$\mathrm{SNR}_\mathrm{S} [dB]$')
plt.ylabel('$P_\mathrm{s}$')
plt.legend()
plt.savefig('PsPAM.png')

plt.figure()    
plt.semilogy(SNRsperbitdB,Pb,'ro',label='numerical')
plt.semilogy(SNRsperbitdB,Pb_an,label='analytical')
plt.xlabel('$\mathrm{SNR}_\mathrm{b} [dB]$')
plt.ylabel('$P_\mathrm{b}$')
plt.legend()
plt.savefig('PbPAM.png')
    
    
    

