#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 07:48:06 2019

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt

# function to create the square pulse
def square(t,T):
    
    f=(t<=T/2.0) * (t>=-T/2.0)
    return(f)
    
  
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}	
plt.rc('font', **font)

# time axis
T=4;
Tmax=30.0
N=1024
n=np.arange(-N/2.0,N/2.0,1)
Dt=2*Tmax/N
t = n*Dt

# frequency axis
Df=1.0/2.0/Tmax
f=n*Df

# signal in the time domain
x=square(t,T)

# signal in the frequency domain
X=Dt*np.fft.fftshift(np.fft.fft(np.fft.fftshift(x)))

# Analytical expression for the spectrum
X2=T*np.sinc(f*T)

# Plot results
plt.figure(1)
plt.xlabel('$t$ [msec]',**font)
plt.ylabel('$x(t)$ [V]')
plt.tight_layout()
plt.plot(t,x)
plt.savefig('square2.png')

plt.figure(2)
plt.plot(t,np.real(X2),t,X,'o')
plt.xlim(-3,3)
plt.legend(['analytical','numerical'])
plt.xlabel('$f$ [kHz]',**font)
plt.ylabel('$X(f)$')
plt.tight_layout()
plt.savefig('fftcomp.png')