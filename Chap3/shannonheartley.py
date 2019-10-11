#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:00:00 2019

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}	
plt.rc('font', **font)

SNRdB = np.arange(0.0,40.0,1)
SNR=10.0**(SNRdB/10.0)
CB=np.log2(1.0+SNR)
plt.figure(1)
plt.plot(SNRdB, CB)
plt.xlabel('SNR [dB]')
plt.ylabel('$C/B$ [bits/s/Hz]')
plt.tight_layout()
plt.savefig('CB.png')
