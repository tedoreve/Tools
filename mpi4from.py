# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 12:17:34 2018

@author: tedoreve
"""
import numpy as np
import pyPLUTO as pp
import plot_flux as pf

if __name__ == '__main__':
    t      = 4 
    sigma  = 1.0
    vindex = 0.0
    i      = 2
    
    wdir = './'
    nlinf = pp.nlast_info(w_dir=wdir)
    
#==============================================================================
    D = pp.pload(t,w_dir=wdir)   
    xlabel = 'x (pc)'
    ylabel = 'y (pc)'
    name   = 't'+str(t)+'_xy.eps'
    print(D.rho.shape,D.bx1.shape)
    b = np.fromfile("filename.bin",dtype = 'float64')
    b.shape = D.rho.shape
    pf.plot(i,b,xlabel,ylabel,name,sigma)

    