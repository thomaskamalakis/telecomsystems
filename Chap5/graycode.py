#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:44:54 2019

@author: thomas
"""
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
def graycode(M):

    if (M==1):
        g=['0','1']

    elif (M>1):
        gs=graycode(M-1)
        gsr=gs[::-1]
        gs0=['0'+x for x in gs]
        gs1=['1'+x for x in gsr]
        g=gs0+gs1
    return(g)
    
    
M=2**4                                      # number of levels
gwords=graycode(np.log2(M).astype(int))     # Gray code words
u=np.arange(0,M)
Am = 2*u -  M +1                            # Symbol levels
         
for i,g in enumerate(gwords): 
    print('%d -> %6.2f : %s' %(i,Am[i],g))
    
plt.figure()    
plt.stem(u,Am)
plt.xlabel('$m$')
plt.ylabel('$A_m$')

for n in range(0,M):
    A = Am[n]   
    if A>0:
        y=A+1
    else:
        y=A-2
    plt.text(n-0.5,y,gwords[n]) 

minA=np.min(Am)
maxA=np.max(Am)

plt.ylim(minA-4,maxA+4)    
plt.tight_layout()
plt.savefig('levelspam.png')
