#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:42:23 2019

@author: thomas
"""

from scipy import special
import numpy as np
import matplotlib.pyplot as plt


def Qfunction(x):    
    return 0.5 * special.erfc( x / np.sqrt(2.0) )


def qfunction(Q):
    yy = np.arange(10,1,-0.1)        
    QQ = Qfunction(yy)    
    q = np.interp(Q,QQ,yy)
    return q

def SNRmin(M,Pb):
    q2 = qfunction( Pb * M * np.log2(M) / 2 / (M**2-1) )    
    return ( M**2 - 1 ) / 6 / np.log2(M) * q2 ** 2.0

MM=np.array([4, 8, 16, 32, 64]).astype(int)
n=np.arange(-14,-1,0.1)
Pb=np.array( 10.0** n )

SNRb=np.zeros([Pb.size, MM.size])

plt.close('all')
plt.figure()    
for i, M in enumerate(MM):
    print(i,M)
    SNRb[:,i] = 10.0*np.log10(SNRmin( M, Pb ))
    plt.semilogx(Pb,SNRb[:,i],label='$M='+str(M)+'$')
    
plt.legend()
plt.title('$P_b$ with respect to $\mathrm{SNR}_b^{min}$ (PAM)')
plt.xlabel('$P_b$')
plt.ylabel('$\mathrm{SNR}_b^{min}$ [dB]')
plt.savefig('PbSNRPAM.png')

    


