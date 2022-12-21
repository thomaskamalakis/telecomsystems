#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:25:24 2022

@author: thomas
"""
import numpy as np
import commlib as cl
import matplotlib.pyplot as plt
B = 50

def H(f):
    return cl.square_filter(f , B)
    
Tmin = -1
Tmax = 1
N = 1000
t = cl.time_axis(Tmin, Tmax, N)


n = np.random.normal(loc = 0.0, scale = 3, size = N)
n_out = cl.system_action(t, n, H)

plt.close('all')
plt.figure()
plt.plot(t,n)

plt.figure()
plt.plot(t,n_out)