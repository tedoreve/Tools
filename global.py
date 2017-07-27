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

plt.figure()
plt.subplot(111, projection="aitoff")
#plt.subplot(111)
dec_low = np.deg2rad(-11)
dec_hig = np.deg2rad(66)

ra  = np.linspace(-np.pi,np.pi,10000)

dec = np.linspace(dec_hig,dec_hig,10000)

c = SkyCoord(ra=ra*u.rad, dec=dec*u.rad, frame='icrs')
l = c.galactic.l.rad
b = c.galactic.b.rad

df = pd.DataFrame({'l':l,'b':b})


for i in range(len(l)):
    if df.l[i] > np.pi:
        df.l[i] -= np.pi*2
df=df.sort_values('l')
#df=df.sort(columns='l')      
plt.plot(df.l,df.b,'o',color='r',markeredgecolor='r',markersize=1)

#plt.scatter(df.l,df.b,c=0.5, alpha=0.5)
plt.title("Aitoff")
plt.grid(True)

