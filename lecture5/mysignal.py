#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:07:38 2022

@author: thomas
"""
import numpy as np
from commlibv2 import signal

def s_callable( t ):
    return np.exp(-t ** 2 / 2)

N = 1024
Tmax = 10
t = np.linspace(-Tmax, Tmax, N)
s = signal(t = t, signal_callable = s_callable )
s.plot()
s.calc_spectrum()
s.plot(what = 'spec')