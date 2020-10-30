#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:58:53 2020

@author: thkam
"""

import numpy as np
from scipy import special
import matplotlib.pyplot as plt
 
def qfunction(x):
    return 0.5*special.erfc(x/np.sqrt(2))

x = np.linspace(0.0, 10.0, 100)
Q = qfunction(x)

plt.close('all')
plt.figure(1)
plt.semilogy(x, Q)
plt.xlabel('x')
plt.ylabel('Q')





