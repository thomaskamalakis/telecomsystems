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

Pbmin=1e-6
Rb = 100e6
n=np.arange(1,9)
MM = 2**n
PavN0 = np.zeros(MM.size)
Pav = np.zeros(MM.size)
B = Rb / np.log2(MM) / 2.0

N0=1e-15

for i,M in enumerate(MM):
    SNRb = SNRmin(M,Pbmin)
    PavN0[i] = SNRb * Rb
    Pav[i] = 10* np.log10( N0 * PavN0[i] / 1e-3 )

plt.close('all')
plt.figure()   
ax = plt.gca()
ax.set_xscale('log') 
plt.stem(MM,Pav)
plt.xlabel('$M$')
plt.ylabel('$P_\mathrm{av}$ [dBm]')
plt.ylim([-35,10])
for i,M in enumerate(MM):
    if Pav[i] < 0:
        plt.text(4*M/5,Pav[i]-2,'$M$='+str(M))
    else:
        plt.text(4*M/5,Pav[i]+2,'$M$='+str(M))

plt.savefig('PavPAM.png')
plt.figure()   
ax = plt.gca()
ax.set_xscale('log') 
plt.stem(MM,B/1e6)
plt.xlabel('$M$')
plt.ylim([0,60])

plt.ylabel('$B$ [MHz]')
for i,M in enumerate(MM):
    plt.text(4*M/5,B[i]/1e6+2,'$M$='+str(M))
plt.savefig('BPAM.png')
    
