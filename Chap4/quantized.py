#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:00:00 2019

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt

def analogfunction(t):
    f0=10.0e6   
    return np.sin(2.0*np.pi*f0*t)
   
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}	
plt.rc('font', **font)

# sample and hold
def sample(t,x,Ts):
    xs=np.zeros(np.size(t))
    i=0
    told=t[0]
    fold=x[0]
    for tc in t:
        if tc-told>=Ts:
           told=tc
           fold=x[i]
        xs[i]=fold
        i=i+1
    return xs

# quantize samples
def quantize(x,Rmin,Rmax):
    xhat=np.zeros(np.size(x))
    indx=0
    for xc in x:
        i = np.where((Rmin<=xc) & (Rmax>xc))
        xhat[indx]=(Rmin[i]+Rmax[i])/2.0
        indx=indx+1
        
    return(xhat)
    
# analog time axis
Nt=2.0e3
Dt=1.0e-10
t=np.arange(0.0,Nt)*Dt+Dt/2.0

# sample period
Ts=3.0e-9

# analog function
x=analogfunction(t)

# sample
xs=sample(t,x,Ts)

# levels
Rmin=np.arange(-1.05,1.05,0.1)
Rmax=np.arange(-0.95,1.15,0.1)

xq=quantize(xs,Rmin,Rmax)

plt.plot(t/1e-6,x,label='Analog')
plt.plot(t/1e-6,xq,label='Digital')
plt.ylabel('$x(t)$')
plt.xlabel('$t [\mu s]$')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.tight_layout()
plt.savefig('quantized.png')