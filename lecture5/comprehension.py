#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:28:45 2022

@author: thomas
"""

l = [1, 2 , 3, 4]

l2 = [x**2 for x in l]

lstr = ['Alice', 'Bob', 'Eve']
l3 = [y + '0' for y in lstr]
print(l3)