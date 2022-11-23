#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:34:49 2022

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000000
x = np.random.randint(1, high = 7, size = N)
Ex = np.mean(x)
Ex2 = np.mean(x**2)
Ex3 = np.mean(x**3)

y = np.random.uniform(low = 0, high = 1, size = N)
Ey = np.mean(y)
Ey2 = np.mean(y ** 2)

m1 = 1
m2 = 2
z1 = np.random.normal(loc = m1, scale = 2, size = N)
z2 = np.random.normal(loc = m2, scale = 4, size = N)

plt.close('all')
plt.plot(z1)
plt.plot(z2)

plt.figure()
plt.plot(z1-m1)
plt.plot(z2-m2)

plt.figure()
plt.plot( (z1-m1) ** 2 )
plt.plot( (z2-m2) ** 2 )

s1 = np.mean( (z1-m1) ** 2)
s2 = np.mean( (z2-m2) ** 2)

