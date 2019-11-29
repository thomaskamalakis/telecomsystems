#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:44:47 2019

@author: thomas
"""

import numpy as np
import matplotlib.pyplot as plt

def graycode(M):

    if (M==1):
        g=['0','1']

    elif (M>1):
        gs=graycode(M-1)
        gsr=gs[::-1]
        gs0=['0'+x for x in gs]
        gs1=['1'+x for x in gsr]
        g=gs0+gs1
    return(g)

def psk_symbol(m,M):    
    theta = 2 * np.pi * (m-1) / M
    s = np.array([np.cos(theta), -np.sin(theta)])
    return(s)

def psk_symbols(M):
    syms = np.zeros([M,2])
    for m in range(0,M):
        syms[m] = psk_symbol(m,M)    
    return syms    


M=16
plt.close('all')
code_words = graycode(np.log2(M))
symbols = psk_symbols(M)
for i,code_word in enumerate(code_words):
    x = symbols[i,0]
    y = symbols[i,1]
    
    plt.plot(x,y,'ro')    
    plt.text(x,y+0.1,code_word,horizontalalignment='center')
    plt.axis('equal')
    plt.xlim([-1.3,1.3])
    plt.ylim([-1.3,1.3])
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    cname = str(M) + '-PSK' 
    plt.title(cname)
    
name = 'PSK' + str(M) + '.png'
plt.savefig(name)