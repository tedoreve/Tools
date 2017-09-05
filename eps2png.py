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
        plt.subplots_adjust(top=1.0,bottom=0.0,left=0.0,right=1.0)
#        plt.savefig(name.replace('.eps','.png'))
        plt.show()
