# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:18:39 2017

@author: tedoreve
"""
import re

def read(filename):
    
    #get the extension name
    ext = re.match(r'^.*\.([a-zA-Z][0-9a-zA-Z]*)$',filename).group(1)
    
    #classify the extension name for different file types
    text1 = ['txt','dat','md','gitignore','sh','reg']
    text2 = ['html','tex','rdb','csv','ecsv','hdf5','xml']
    text3 = ['png','PNG','jpg','JPG','jpeg','JPEG','pdf','eps','bmp','svg']
    text4 = []
    
    #read and return data
    if ext in text1:
        with open(filename,'r') as f:
            data = f.readlines()
    elif ext in text2:
        from astropy.table import Table
        data = Table.read(filename)
    elif ext == 'fits':
        from astropy.io import fits
        data = fits.open(filename)
    elif ext in text3:
        import matplotlib.image as mp
        data = mp.imread(filename)
    return data
            