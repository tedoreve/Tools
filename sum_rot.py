# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 12:39:55 2018

@author: tedoreve
"""

import numpy as np



a   = np.random.rand(16,16)

l   = len(a)

deg = 5

t   = np.tan(np.deg2rad(deg))

if t < 2/l:
    for i in range(int(l/2)):
        if t < 1/(l-i):
            result              = np.zeros([l+1,l])
            result[0:l,0:l-i]   = a[:,0:l-i]
            result[1:l+1,l-i:l] = a[:,l-i:l]
            final               = result.sum(axis=1)
            print('yes1')
            break

elif t < 1:
    for i in range(int(l/2)):
        p = int(l/2-i)
        if t < 1/p:
            index               = int(np.ceil(l/p)-1)
            result              = np.zeros([l+index,l])
            for n in range(index+1):
                if p*(n+1) <= l:
                    result[n:l+n,p*n:p*(n+1)] = a[:,p*n:p*(n+1)]
                else:
                    result[n:l+n,p*n:l] = a[:,p*n:l]
                      
            final               = result.sum(axis=1)
            print('yes2')
            break