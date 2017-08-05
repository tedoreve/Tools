# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:03:37 2017

@author: tedoreve
"""

import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
import pandas as pd


dec_low = np.deg2rad(-11)
dec_hig = np.deg2rad(66)

ra  = np.linspace(-np.pi,np.pi,100)

#dec1 = np.linspace(dec_hig,dec_hig,10000)
#dec2 = np.linspace(dec_low,dec_low,10000)

dec  = np.linspace(dec_low,dec_hig,100)

#c1 = SkyCoord(ra=ra*u.rad, dec=dec1*u.rad, frame='icrs')
#c2 = SkyCoord(ra=ra*u.rad, dec=dec2*u.rad, frame='icrs')
#l1 = c1.galactic.l.rad
#b1 = c1.galactic.b.rad
#l2 = c2.galactic.l.rad
#b2 = c2.galactic.b.rad

arr = np.meshgrid(ra,dec)
c   = SkyCoord(ra=arr[0]*u.rad, dec=arr[1]*u.rad, frame='icrs')
l   = c.galactic.l.rad
b   = c.galactic.b.rad
l.reshape(1,l.size)
df = pd.DataFrame({'l':l.reshape(1,l.size)[0].tolist(),'b':b.reshape(1,b.size)[0].tolist()})
#
#
for i in range(len(df.l)):
    if df.l[i] > np.pi:
        df.l[i] -= np.pi*2
##df=df.sort_values('l')
##df=df.sort(columns='l')     
plt.figure()
plt.subplot(111, projection="aitoff")
#plt.subplot(111) 
#plt.plot(l,b,'o',color='r',markeredgecolor='r',markersize=1)
plt.plot(df.l,df.b,'o',color='g',markeredgecolor='g',markersize=9,label='xx')
plt.legend()
##plt.scatter(df.l,df.b,c=0.5, alpha=0.5)
plt.title("Aitoff")
plt.grid(True)

