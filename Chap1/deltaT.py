#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:03:19 2019

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt
    
x = np.arange(0,8,0.01)
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}	
plt.rc('font', **font)

# function to create the square pulse
def deltaT(t,T):
    
    f=1.0/T * (t<=T/2.0) * (t>=-T/2.0)
    return(f)

# Axis for plot
TT=[0.25, 0.5, 1]
plt.figure(1)
plt.ylabel('$\delta_T$',**font)
plt.xlabel('$t$')

# time axis
t=np.arange(-1.5,1.5,0.01)

for T in TT:
    plt.plot(t,deltaT(t,T),label='$T='+str(T)+'$')
             
plt.legend(bbox_to_anchor=(1.3, 1.05))
plt.tight_layout()
plt.savefig('deltaT.png')
    
