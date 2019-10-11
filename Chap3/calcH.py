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

p1=np.arange(0.001,1.0,0.001)
p0=1.0-p1
H=-p1*np.log2(p1)-p0*np.log2(p0)
plt.figure(1)    
plt.plot(p1,H)
    
plt.ylabel('$H$')
plt.xlabel('$p_1$')
plt.grid()
plt.tight_layout()
plt.savefig('calcH.png')
