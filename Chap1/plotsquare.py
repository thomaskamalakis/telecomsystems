#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:42:28 2019

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

T=4;
t = np.arange(-5, 5, 0.01)
plt.figure(1)
plt.plot(t, square(t,T))
plt.xlabel('$t$ [msec]',**font)
plt.ylabel('$x(t)$ [V]')
plt.tight_layout()
plt.savefig('square.png')

# Plot sinc spectrum
Df=1.0/T/100.0
f=np.arange(-6.0/T,6.0/T,Df)
X=T*np.sinc(f*T)
plt.figure(2)
plt.plot(f, X)
plt.xlabel('$f$ [kHz]',**font)
plt.ylabel('$X(f)$')
plt.tight_layout()
plt.savefig('sinc.png')

