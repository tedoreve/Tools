# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:48:27 2017

@author: tedoreve
"""

#import sys
import os
import matplotlib.image as mp
import matplotlib.pyplot as plt
#print(sys.argv[1])
filename = os.listdir('./')
for name in filename:
    if '.eps' in name:
        data = mp.imread(name)
        plt.axis("off")
        plt.imshow(data)
        plt.savefig(name.replace('.eps','.png'))
