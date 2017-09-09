# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 22:17:27 2017

@author: tedoreve
"""

#import numpy as np
#from astropy import constants as con
from astropy import units as un

d = 6*un.kpc
r1 = 33*un.pc
r2 = 44*un.pc
width = (2.36-0.52)*un.keV
print(width.to('Hz',equivalencies=un.spectral()).value)

T = 0.29*un.keV
lam = 4e-23*un.erg*un.cm**3/un.s
Fx  = 2e-9*un.erg/un.cm**2/un.s
c   = 1.2*r2*r2*r1/(r2*r2*2+r2*r1*4)
n_H = (Fx/c/lam)**0.5
print(T.to('K',equivalencies=un.temperature_energy()).value)
#n_e = 0.29*un.cm**-3
#n_h = n_e/12*10
#n_he= n_e/12
#V   = r1*r2*r2*4/3*np.pi
#m   = n_h*con.m_p*V+n_he*con.m_p*2*V+n_e*con.m_e*V
#print(m.to(con.M_sun).value)
#N_e = n_e*V
#N_h = n_h*V
#N_he= n_he*V
#E   = (N_e+N_h+N_he)*T
#print(E.to('erg'))

