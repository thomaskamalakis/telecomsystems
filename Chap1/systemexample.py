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

# system parameters
a=1

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

# input signal in the time domain
x=square(t,T)

# input signal in the frequency domain
X=Dt*np.fft.fftshift(np.fft.fft(np.fft.fftshift(x)))

# transfer function
H=1.0/(1j*2*np.pi*a*f+1)

# output spectrum
Y=H*X

# inverse fourier transform
y=N*Df*np.fft.fftshift(np.fft.ifft(np.fft.fftshift(Y)))

# Plot in frequency domain
plt.figure(1)
plt.xlabel('$f$ [kHz]',**font)
plt.ylabel('Fourier Transform')
plt.plot(f,abs(X),label='$|X(f)|$')
plt.plot(f,abs(Y),label='$|Y(f)|$')
plt.plot(f,abs(H),'--',label='$|H(f)|$')
plt.xlim(-0.5,0.5)
plt.legend(bbox_to_anchor=(1.3, 1.05))
plt.tight_layout()
plt.savefig('spectrasystem.png')

plt.figure(2)
plt.xlabel('$t$ [ms]',**font)
plt.ylabel('Signal')
plt.plot(t,np.real(x),label='$x(t)$')
plt.plot(t,np.real(y),label='$y(t)$')
plt.legend(bbox_to_anchor=(1.3, 1.05))
plt.xlim(-6,6)
plt.tight_layout()
plt.savefig('signalsystem.png')
