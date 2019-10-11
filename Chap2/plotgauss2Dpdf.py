#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 12:23:22 2019

@author: thomas
"""
import matplotlib.pyplot as plt

import numpy as np

def gausspdf2D(x,y,r,s2):
    expo=-1.0/2.0/(1-r**2)*(x**2/s2+y**2/s2-2.0*r*x*y/s2)
    pdf = 1.0/2.0/np.sqrt(1-r**2)/np.pi/s2*np.exp(expo)
    return(pdf)
    
dx, dy = 0.1, 0.1

# generate 2 2d grids for the x & y bounds
y, x = np.mgrid[slice(-8, 8 + dy, dy),
                slice(-8, 8 + dx, dx)]
r=3.0/5.0
s2=5
pdf=gausspdf2D(x,y,r,s2)
plt.figure(1)
plt.pcolor(x,y,pdf)
plt.colorbar()
plt.axis('equal')
plt.title('$f_{X,Y}(x,y)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.tight_layout()
plt.savefig('correlatedPDFg.png')

r=0.0
pdf=gausspdf2D(x,y,r,s2)
plt.figure(2)
plt.pcolor(x,y,pdf)
plt.colorbar()
plt.axis('equal')
plt.title('$f_{X,Y}(x,y)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.tight_layout()
plt.savefig('uncorrelatedPDFg.png')
