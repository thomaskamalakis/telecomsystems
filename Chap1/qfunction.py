#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:03:19 2019

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import special
    
x = np.arange(0,8,0.01)
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}	
plt.rc('font', **font)

# Plot Q function
plt.figure(num=1,figsize=(10,8))
plt.xlabel('$x$',**font)
plt.ylabel('$Q(x)$')
plt.semilogy(x,0.5*special.erfc(x/np.sqrt(2.0)))
plt.legend(bbox_to_anchor=(1.3, 1.05))
plt.tight_layout()
plt.grid()
plt.savefig('Qfunction.png')
    
