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
ra  = np.linspace(-np.pi,np.pi,100)

dec = np.linspace(0,0,100)

c = SkyCoord(ra=ra*u.rad, dec=dec*u.rad, frame='icrs')
l = c.galactic.l.rad
b = c.galactic.b.rad

df = pd.DataFrame({'l':l,'b':b})


for i in range(len(l)):
    if df.l[i] > np.pi:
        df.l[i] -= np.pi*2
        
df=df.sort(columns='l')      
plt.plot(df.l,df.b)

plt.title("Aitoff")
plt.grid(True)

