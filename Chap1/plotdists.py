#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:23:37 2019

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt

# function to create the uniform distribution
def uniform(x,a,b):
    
    f=(x>=a) * (x<=b)
    f=1.0/(b-a)*f
    return(f)
 
def gauss(x,mu,s):
    
    f=1.0/np.sqrt(2*np.pi)/s*np.exp(- np.power(x-mu,2)/2/np.power(s,2) )
    return(f)
    
x = np.arange(-5, 6, 0.01)
a=-2.0
b=+2.0
mu=1.0
s=2.0

fg=gauss(x,mu,s)
fs=uniform(x,a,b)

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}	
plt.rc('font', **font)

# Plot in frequency domain
plt.figure(1)
plt.xlabel('$x$',**font)
plt.ylabel('Distribution')
plt.plot(x,abs(fg),label='Gaussian')
plt.plot(x,abs(fs),label='uniform')
plt.xlim(-5.0,6.0)
plt.legend(bbox_to_anchor=(1.3, 1.05))
plt.tight_layout()
plt.savefig('pdfs.png')
    
