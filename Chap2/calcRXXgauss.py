#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 12:23:22 2019

@author: thomas
"""
import matplotlib.pyplot as plt

import numpy as np

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}	
plt.rc('font', **font)

# time axis
Tmax=3.0
N=1024
n=np.arange(-N/2.0,N/2.0,1)
Dt=2*Tmax/N
t = n*Dt

# frequency axis
Df=1.0/2.0/Tmax
f=n*Df

# number of iterations
Nit=10000
XX=np.zeros([N,N])

plt.figure(1)    
for m in range(0,Nit):
    x=np.random.randn(N)
    plt.plot(t,x)
    x=np.asmatrix(x)
    xt=np.transpose(x)
    X=np.multiply(xt,x)
    XX=X+XX
    
XX=1.0/Nit*XX

# calculate autocorrelation
Rnn=np.array(XX[N/2])[0]

# Calculate power spectral density
Sn=Dt*np.fft.fftshift(np.fft.fft(np.fft.fftshift(Rnn)))

plt.xlim([-0.5,0.5])
plt.ylabel('$X_n(t)$')
plt.xlabel('$t$')
plt.tight_layout()
plt.savefig('gaussnt.png')

plt.figure(2)    
plt.plot(t,Rnn)
plt.xlim([-0.5,0.5])
plt.grid()
plt.xlabel('$\\tau$')
plt.ylabel('$R_{nn}( \\tau )$')
plt.tight_layout()
plt.savefig('gaussRXX.png')

plt.figure(3)    
plt.plot(f,np.abs(Sn))
plt.grid()
plt.xlabel('$f$')
plt.ylabel('$S_{n}(f)$')
plt.tight_layout()
plt.savefig('gaussSn.png')

