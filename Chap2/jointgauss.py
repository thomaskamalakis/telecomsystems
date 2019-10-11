# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

import numpy as np
# always begin with the same seed
np.random.seed(0)

# generate a and b
N=1000
a=np.random.randn(N)
b=np.random.randn(N)

X=2*a+b
Y=2*a-b

# range of samples to be taken into account when estimating expectations
R=np.arange(10,1000,10)

mx=np.zeros([len(R),1])
my=np.zeros([len(R),1])
sx=np.zeros([len(R),1])
sy=np.zeros([len(R),1])
rxy=np.zeros([len(R),1])

indx=0

# calculate statistical data
for r in R:
   xr=X[1:r]
   yr=Y[1:r]
   
   mx[indx]=np.mean(xr)
   my[indx]=np.mean(yr)
   sx[indx]=np.mean((xr-mx[indx])**2)
   sy[indx]=np.mean((yr-my[indx])**2)
   rxy[indx]=np.mean((xr-mx[indx])*(yr-my[indx]))/np.sqrt(sx[indx])/np.sqrt(sy[indx])
   indx=indx+1

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}	
plt.rc('font', **font)
   
# Plot Expectations
plt.figure(1)
plt.xlabel('$N$',**font)
plt.ylabel('Expectations')
plt.plot(R,mx,label='$\mu_X$')
plt.plot(R,sx,label='$\sigma_X^2$')
plt.plot(R,rxy,label=r"$\rho$")
plt.legend(bbox_to_anchor=(1.3, 1.05))
plt.tight_layout()
plt.savefig('statistics.png')

