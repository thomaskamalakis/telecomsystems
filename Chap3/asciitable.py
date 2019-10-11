#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:49:58 2019

@author: thomas
"""

for a in range(32,48):
    print(str(a)+' $\leftarrow$ '+chr(a)+' & '+str(a+16)+' $\leftarrow$ '+chr(a+16)+' & '
          +str(a+32)+' $\leftarrow$ '+chr(a+32)+' & '
          +str(a+48)+' $\leftarrow$ '+chr(a+48)+' \\\\')
    