#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:42:19 2019

@author: thomas
"""

with open('across-the-universe.txt', 'r') as myfile:
    S=myfile.read()
    
binreps=[]
decreps=[]
msgs=[]
binmsg=''

# Original dictionary - ASCII characters
for i in range(1,128):
    binrep=bin(i)[2:].zfill(7)
    print(binrep,i,chr(i))
    decreps.append(i)
    binreps.append(binrep)
    msgs.append(chr(i))

max_so_far=127

w=''

# for every character in S
for c in S:
    if w+c in msgs:
        w=w+c
    else:
        
        # output code for w
        i=msgs.index(w)
        decrep=decreps[i]
        binrep=binreps[i]
        print(binrep)
        binmsg=binrep+binmsg
        
        # add entry for w+c
        max_so_far=max_so_far+1
        binrep=bin(max_so_far)[2:]
        msgs.append(w+c)
        decreps.append(max_so_far)
        binreps.append(binrep)
        w=c

# output code for w
i=msgs.index(w)
decrep=decreps[i]
binrep=binreps[i]
print(binrep)
binmsg=binrep+binmsg

print(binmsg)        
ratio=len(binmsg)/len(S)/7
print('\nCompression ratio: %6.2f' % ratio)