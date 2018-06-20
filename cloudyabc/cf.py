# -*- coding: utf-8 -*-
"""
Created on Mon May 28 08:03:46 2018

@author: tedoreve
"""

import numpy as np
import matplotlib.pyplot as plt

cooling = np.loadtxt('cooling.dat')
plt.loglog(cooling[:,0],cooling[:,1])



yinterp = np.interp([10,1000,100000], cooling[:,0],cooling[:,1])

plt.loglog([10,1000,100000],yinterp,'o')
plt.show()