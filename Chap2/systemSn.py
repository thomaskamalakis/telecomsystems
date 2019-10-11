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

# frequency response
f3dB=5.0
H=1.0/(1j*f/f3dB+1)

# number of iterations
Nit=1000
YY=np.zeros([N,N])

for m in range(0,Nit):
    x=np.random.randn(N)
    
    # calculate spectrum at input
    Xf=Dt*np.fft.fftshift(np.fft.fft(np.fft.fftshift(x)))
    
    # Multiply with transfer function
    Yf=Xf*H
    
    # Back to the time domain
    y0=1.0/Dt*np.fft.fftshift(np.fft.ifft(np.fft.fftshift(Yf)))
        
    y=np.asmatrix(y0)
    yt=np.transpose(y)
    Y=np.multiply(yt,y)
        
    YY=Y+YY
    
YY=1.0/Nit*YY

    
# calculate autocorrelation
Rnn=np.array(YY[int(N/2)])[0]

# Calculate power spectral density
Sn=Dt*np.fft.fftshift(np.fft.fft(np.fft.fftshift(Rnn)))

plt.figure(1)    
plt.plot(t,np.real(y0))
plt.xlim([-0.5,0.5])
plt.ylabel('$N_k(t)$')
plt.xlabel('$t$')
plt.tight_layout()
plt.savefig('outputsystem.png')

plt.figure(2)    
plt.plot(t,np.real(Rnn))
plt.xlim([-0.5,0.5])
plt.grid()
plt.xlabel('$\\tau$')
plt.ylabel('$R_{NN}( \\tau )$')
plt.tight_layout()
plt.savefig('outputRXX.png')

plt.figure(3)    
plt.plot(f,np.abs(Sn),label='Numerical')
plt.plot(f,Dt*np.abs(H)*np.abs(H),label='Analytical',linewidth=3.0)
plt.xlim([-10.0,10.0])
plt.grid()
plt.xlabel('$f$')
plt.ylabel('$S_{N}(f)$')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.tight_layout()
plt.savefig('outputSn.png')

