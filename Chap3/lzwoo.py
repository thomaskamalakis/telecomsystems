#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:42:19 2019

@author: thomas
"""

class lzwdict:
    binreps=[]          # list to hold the binary representations of the messages
    decreps=[]          # list to hold the decimal representations
    msgs=[]             # list to hold the messages
    max_so_far=127
    
    # pre-encode initial phrases in dictionary
    def encode_ascii(self,ir):
        for i in ir:
            binrep=bin(i)[2:].zfill(7)
            print(binrep,i,chr(i))
            self.decreps.append(i)
            self.binreps.append(binrep)
            self.msgs.append(chr(i))
    
    def output_code(self,w,binmsg):
        i=self.msgs.index(w)
        binrep=self.binreps[i]
        print(binrep)
        binmsg=binrep+binmsg
        return(binmsg)

    def add_entry(self,wc):
        self.max_so_far=self.max_so_far+1
        binrep=bin(self.max_so_far)[2:]
        self.msgs.append(wc)
        self.decreps.append(self.max_so_far)
        self.binreps.append(binrep)
                
    def contains(self,wc):
        return(wc in self.msgs)
        
# initialize dictionary
dictionary=lzwdict()

# read file
with open('across-the-universe.txt', 'r') as myfile:
    S=myfile.read()

# message to transmit    
binmsg=''

# Original dictionary - ASCII characters
ir=range(1,128)
dictionary.encode_ascii(ir)

# phrase read so far
w=''

# for every character in S
for c in S:
    if dictionary.contains(w+c):
        w=w+c
    else:
        # output code for w
        binmsg=dictionary.output_code(w,binmsg)
        
        # add entry for w+c
        dictionary.add_entry(w+c)
        w=c

# output code for w
binmsg=dictionary.output_code(w,binmsg)

print(binmsg)        
ratio=len(binmsg)/len(S)/7
print('\nCompression ratio: %6.2f' % ratio)