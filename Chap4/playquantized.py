#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 07:32:21 2019

@author: thomas
"""

    
import numpy as np
import sounddevice as sd

from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# quantize samples
def quantize(x,Rmin,Rmax):
    xhat=np.zeros(np.size(x))
    indx=0
    for xc in x:
        i = np.where((Rmin<=xc) & (Rmax>xc))
        xhat[indx]=(Rmin[i]+Rmax[i])/2.0
        indx=indx+1
        
    return(xhat)

minv=-32767
maxv=+32768
Dv=4096
R=np.arange(minv,maxv,Dv)
Rmin=R[0:len(R)-1]
Rmax=R[1:len(R)]

# read audio samples
input_data = read("/usr/share/sounds/alsa/Rear_Center.wav","rb")
audio = input_data[1]
audio = np.array(audio)
rate = input_data[0]

# quantize audio
audio_q=quantize(audio,Rmin,Rmax)
audio_q=np.array(audio_q,dtype=np.int16)

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}	
plt.rc('font', **font)

plt.plot(audio_q)
plt.ylim(-32767,+32768)
plt.ylabel('$\hat{x_i}$')
plt.xlabel('$i$')
plt.tight_layout()
plt.savefig('sampledsound4096.png')

sd.play(audio_q, rate)