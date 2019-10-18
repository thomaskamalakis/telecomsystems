#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 07:48:06 2019

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}	
plt.rc('font', **font)

x=np.arange(-3.0,3.0,0.1)
m=0
s=1.5

f=1 / (s*np.sqrt(2*np.pi) ) * np.exp( -(x - m) ** 2 / 2.0 / s**2.0 )

plt.close('all')   
plt.figure(1)
plt.xlabel('$x$',**font)
plt.ylabel('f')
plt.plot(x,f)