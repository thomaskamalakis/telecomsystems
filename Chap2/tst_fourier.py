#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:41:07 2019

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt

N=1024
n=np.arange(-N/2.0,N/2.0,1)
x=np.zeros(N)
x[N/2]=1
plt.figure(1)
plt.plot(x)
X=np.fft.fftshift(np.fft.fft(np.fft.fftshift(x)))
plt.figure(2)
plt.plot(X)

