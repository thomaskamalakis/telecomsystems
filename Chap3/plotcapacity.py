#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:00:00 2019

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}	
plt.rc('font', **font)

T=4;
pe = np.arange(0.01, 1, 0.01)
Rmax=1.0+pe*np.log2(pe)+(1.0-pe)*np.log2(1.0-pe)
plt.figure(1)
plt.plot(pe, Rmax)
plt.xlabel('$p_\mathrm{e}$')
plt.ylabel('$R_\mathrm{max}$')
plt.tight_layout()
plt.savefig('Rmax.png')
