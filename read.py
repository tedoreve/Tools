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
    text = ['txt','dat','md','gitignore','sh']
    
    #read and return data
    if ext in text:
        with open(filename,'r') as f:
            data = f.readlines()
            
    
    return data
            