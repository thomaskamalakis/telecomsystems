#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:00:49 2019

@author: thomas
"""

import numpy as np
PS=np.matrix('0.1 0.3 0.1; 0.2 0.2 0.3; 0.7 0.5 0.6')

ny=len(PS)
S=PS-np.eye(ny)

S[ny-1]=np.matrix('1 1 1')
b=np.matrix('0; 0; 1')
p=np.linalg.inv(S)*b
H=0
for i in range(0,2):
    for j in range(0,2):
        H=H-p[i,0]*np.log2(PS[i,j])
print(H)