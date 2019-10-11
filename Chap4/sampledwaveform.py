#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:00:00 2019

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt

# function to create the square pulse
def pulse(t,T):
    f=np.zeros(np.size(t))
    i=0
    for t0 in t:
       if (t0<T/2.0) and (t0>=-T/2.0):
           f[i]=1           
       else:
           f[i]=0
       i=i+1
    return f

def analogfunction(t):
    f0=10.0e6   
    return np.sin(2.0*np.pi*f0*t)
   
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}	
plt.rc('font', **font)

# analog time axis
Nt=2.0e3
Dt=1.0e-10
t=np.arange(0.0,Nt)*Dt+Dt/2.0

# analog function
x=analogfunction(t)

# sample waveform
kmin=0
kmax=20
xs=np.zeros([int(Nt)])
Ts=1.0e-8

for k in np.arange(kmin,kmax):
    xs=xs+analogfunction(k*Ts)*pulse(t-k*Ts,Ts)

    
plt.plot(t/1e-6,x,label='Analog')
plt.plot(t/1e-6,xs,label='Digital')
plt.ylabel('$x(t)$')
plt.xlabel('$t [\mu s]$')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.tight_layout()
plt.savefig('analogdigital.png')