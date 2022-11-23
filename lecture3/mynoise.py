#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:25:24 2022

@author: thomas
"""
import numpy as np
import commlib as cl
import matplotlib.pyplot as plt

Tmin = -1
Tmax = 1
N = 1000
T = 0.5
t = cl.time_axis(Tmin, Tmax, N)
x = cl.square(t , T)

plt.close('all')
plt.plot(t, x)

n = np.random.normal(loc = 0.0, scale = 3, size = N)
y = x + n
plt.figure()
plt.plot(y)