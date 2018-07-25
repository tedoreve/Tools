# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 12:11:24 2018

@author: tedoreve
"""

import matplotlib.pyplot as plt
import numpy as np
import astropy.constants as con
import astropy.units as un


def maxwell(T,m,v):
    a = np.sqrt(con.k_B*T/con.m_e)
    print('a=',a.to('km/s'))
    return np.sqrt(2/np.pi)*v**2/a**3 * np.exp(-v**2/2/a**2)
    
def ptotal(v):
    dv = v[1]-v[0]
    p  = maxwell(T,con.m_e,v).to('s/km')*dv
    return np.sum(p)
    
def accelerator(p,n,v):
    fin = np.zeros(len(v))
    for i in range(len(v)):
        fin[i] = maxwell(T,con.m_e,v[i])*(1-p) + fin[i-1]*p
    return fin
    
if __name__ == '__main__': 
    
    T = 50*un.K #ISM temperature before shock wave arrival
    p = 0.5      #possibility that the particle remain within the accelerator after each cycle
    n = 1        #the cycle times
    dv= 1        #speed addition after each cycle
    
    fig, ax = plt.subplots(1, 1)
    
    v = np.linspace(0,200, (201-0)/dv)*un.km/un.s
    
    ax.plot(v, maxwell(T,con.m_e,v).to('s/km'),'r-', lw=5, alpha=0.6, label='maxwell pdf')
    
    ax.set_xlabel('v (km/s)')
    ax.set_ylabel('pdf (possibility per km/s)')
    ax.set_title('Maxwell Speed Distribution')
    plt.legend()