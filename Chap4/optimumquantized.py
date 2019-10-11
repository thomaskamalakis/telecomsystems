#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 07:32:21 2019

@author: thomas
"""

    
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# quantize samples
def quantize(x,xhat):
    
    xhat=np.sort(xhat)
    
    # Quantized version
    Qx=np.zeros([x.size])
    
    # optimal intervals
    a=np.zeros([xhat.size-1])
    for i in range(0,xhat.size-1):
        a[i]=0.5*(xhat[i+1]+xhat[i])
    
    # quantize signal
    for q in range(0,x.size-1):
        
        xc=x[q]
        if xc<a[0]:
            Qx[q]=xhat[0]
        elif xc>a[xhat.size-2]:
            Qx[q]=xhat[xhat.size-1]
        else:
            pos=np.argmin(np.abs(xc-xhat))
            Qx[q]=xhat[pos]
        
    return(Qx)

def metric(x,xhat,fX):
    D=np.sum( (quantize(x,xhat)-x)**2.0*fX)
    return(D)

xhat=np.arange(1,3,1)    
# analog time axis
Nt=1000.0
Dt=0.005
x=np.arange(0,Nt-1,1)*Dt
fX=1.0/np.sqrt(2.0*np.pi)*np.exp(-x**2/2.0)
metricD= lambda xhat : metric(x,np.concatenate([[0.0],xhat]),fX)
Qx=quantize(x,xhat)
plt.plot(x,fX)
res = minimize(metricD, xhat, method='nelder-mead', options={'maxiter' : 1e6,'maxfev' : 1e6,'xtol': 1e-4, 'disp': True})
print(res.x)