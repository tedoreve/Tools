# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 12:17:34 2018

@author: tedoreve
"""
import numpy as np

b = np.fromfile("./a.bin",dtype = 'float64')
b.shape = [4,4,4,2]
print(b)
