# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:59:06 2017

@author: tedoreve
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy import units as un
from astropy import constants as con


def cooling():
    dex  = np.linspace(1,17,17)
    def f(x):
        return 'str' + x
    names = map(f, dex.astype(int).astype(str))
    data = pd.read_table('D:\software\c17.00\source\script.dat',names=names,encoding='gb2312')

    plt.plot(data['str1'],data['str5'])
    plt.plot([17406778.95421341,]*17,dex*1e-23)
    plt.plot(dex*1e6,[2.5e-23,]*17)
    ##plt.xlim(0.52,2.36)
    ##plt.ylim(1e36,1e39)
    plt.xscale('log')
    plt.yscale('log')
    
def sed():
    data = pd.read_table('D:\software\c17.00\source\script.con',encoding='gb2312')
    plt.plot(data['#Cont  nu'],data['total'])
    #e    = (data['nu'].values*con.Ryd).to('keV',equivalencies=un.spectral())
#    plt.ylim(1e-6,1e-2)
    plt.xscale('log')
    plt.yscale('log')
    
#==============================================================================
if __name__ == '__main__':
    cooling()
#    sed()
#==============================================================================
