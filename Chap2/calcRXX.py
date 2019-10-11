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

# signal amplitude and frequency
A=1
f0=1

# number of iterations
Nit=100
XX=np.zeros([N,N])

plt.figure(1)    
for n in range(0,Nit):
    phi=2*np.pi*np.random.rand()
    x=A*np.sin(2.0*np.pi*f0*t+phi)
    plt.plot(t,x)
    x=np.asmatrix(x)
    xt=np.transpose(x)
    X=np.multiply(xt,x)
    XX=X+XX
    
XX=1.0/Nit*XX
plt.xlim([-0.5,0.5])
plt.ylabel('$X_n(t)$')
plt.xlabel('$t$')
plt.tight_layout()
plt.savefig('Xtphi.png')

plt.figure(2)    
plt.plot(t,XX[:,(np.int) (N/2)])
plt.xlim([-0.5,0.5])
plt.grid()
plt.xlabel('$\\tau$')
plt.ylabel('$R_{XX}( \\tau )$')
plt.tight_layout()
plt.savefig('RXX.png')
