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

# always begin with the same seed
np.random.seed(0)

# create many random samples
N=1000
s = 2
m = 1
n=s* np.random.randn( N ) + m

# range of samples to be taken into account when estimating expectations
R=np.arange(10,1000,10)

mvs=np.zeros([len(R),1])
svs=np.zeros([len(R),1])
indx=0

for r in R:
   nr=n[1:r]
   mm=np.mean(nr)
   ss=np.mean((mm-nr)**2)
   mvs[indx]=mm
   svs[indx]=ss
   indx=indx+1
   
      
# Plot Expectations
plt.figure(1)
plt.xlabel('$N$',**font)
plt.ylabel('Expectations')
plt.plot(R,mvs,label='$\mu$')
plt.plot(R,svs,label='$\sigma^2$')
plt.legend(bbox_to_anchor=(1.3, 1.05))
plt.tight_layout()
plt.savefig('expectations.png')