# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 22:17:27 2017

@author: tedoreve
"""

import numpy as np
from astropy import constants as con
from astropy import units as un

d = 6*un.kpc
r1 = 9*un.pc
r2 = 3*un.pc
V1 = 4/3*np.pi*r1**3
V2 = 4/3*np.pi*r2**3
#width = (2.36-0.52)*un.keV
#print(width.to('Hz',equivalencies=un.spectral()).value)

T = 0.5*un.keV
print(T.to('K',equivalencies=un.temperature_energy()).value)
lam1 = 3.5e-23*un.erg*un.cm**3/un.s
lam2 = 3.4e-23*un.erg*un.cm**3/un.s
lam3 = 2.5e-23*un.erg*un.cm**3/un.s
Fx1  = 1.4**2*2.2e35*un.erg/un.s
Fx2  = 1.4**2*2.7e34*un.erg/un.s
Fx3  = 1.4**2*1.1e34*un.erg/un.s
c    = 1.2*(V1-V2)
n_H  = (Fx2/c/lam2)**0.5
print(n_H.to('cm^-3').value)
mh   = con.m_p*n_H*(V1-V2)
mhe  = 2*con.m_p*n_H*0.1*(V1-V2)
eh   = con.k_B*T.to('K',equivalencies=un.temperature_energy())*n_H*(V1-V2)
ehe  = con.k_B*T.to('K',equivalencies=un.temperature_energy())*n_H*0.1*(V1-V2)

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

