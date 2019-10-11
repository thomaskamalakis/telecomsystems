#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:42:19 2019

@author: thomas
"""

import numpy as np

#S='AABABBBABAABABBBABBABB'
S='ABABABABABABABABABABAB'
w=''
d=['']
msgs=[]
tosend=[]

for c in S:
    if w+c in d:
        w=w+c
    else:
        print(d.index(w),c)
        msgs.append([d.index(w),c])
        d.append(w+c)
        w=''

# convert to binary
nbits=0
reps=[]
print('\n')

for msg in msgs:
    i=msg[0]
    c=msg[1]
    # number of bits required for representation
    
    print(i,nbits,2**(nbits-1)+1)
    
    if (i==0) and (nbits==0):
        bc=''
        nbits=nbits+1
    else:
        if i>=2**(nbits-1)+1:
            nbits=nbits+1
        bc=bin(i)[2:].zfill(nbits)
        
    if c=='A':
       ac='0'
    else:
       ac='1'
   
    reps.append(bc+','+ac+'|')
    
    