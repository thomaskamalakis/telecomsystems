#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:30:06 2022

@author: thomas
"""
import numpy as np
import matplotlib.pyplot as plt

from commlib import Qfunction
x = np.linspace(0, 5, 100)
Q = Qfunction(x)
plt.close('all')
plt.plot(x, Q)
plt.xlabel('x')
plt.ylabel('Q(x)')

plt.figure(2)
plt.semilogy(x, Q)
plt.xlabel('x')
plt.ylabel('Q(x)')
