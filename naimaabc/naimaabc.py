import numpy as np
import matplotlib.pyplot as plt

import naima
from naima.models import (ExponentialCutoffPowerLaw, Synchrotron,
                          InverseCompton)
from astropy.constants import c
import astropy.units as u

ECPL = ExponentialCutoffPowerLaw(1e36*u.Unit('1/eV'), 1*u.TeV, 2.1, 13*u.TeV)
SYN = Synchrotron(ECPL, B=100*u.uG)

# Define energy array for synchrotron seed photon field and compute
# Synchroton luminosity by setting distance to 0.
Esy = np.logspace(-6, 6, 100)*u.eV
Lsy = SYN.flux(Esy, distance=0*u.cm)

# Define source radius and compute photon density
R = 2 * u.pc
phn_sy = Lsy / (4 * np.pi * R**2 * c) * 2.26

# Create IC instance with CMB and synchrotron seed photon fields:
IC = InverseCompton(ECPL, seed_photon_fields=['CMB', 'FIR', 'NIR',
                                              ['SSC', Esy, phn_sy]])

# Compute SEDs
spectrum_energy = np.logspace(-1,14,100)*u.eV
sed_IC = IC.sed(spectrum_energy, distance=1.5*u.kpc)
sed_SYN = SYN.sed(spectrum_energy, distance=1.5*u.kpc)

# Plot
plt.figure(figsize=(8,5))
#plt.rc('font', family='sans')
#plt.rc('mathtext', fontset='custom')
ssc = IC.sed(spectrum_energy, seed='SSC', distance=1.5*u.kpc)
plt.loglog(spectrum_energy,ssc,lw=1.5,
        ls='-',label='IC (SSC)',c=naima.plot.color_cycle[2])
for seed, ls in zip(['CMB','FIR','NIR'], ['-','--',':']):
    sed = IC.sed(spectrum_energy, seed=seed, distance=1.5*u.kpc)
    plt.loglog(spectrum_energy,sed,lw=1,
            ls=ls,c='0.25')#,label='IC ({0})'.format(seed))


plt.loglog(spectrum_energy,sed_IC,lw=2,
        label='IC (total)',c=naima.plot.color_cycle[0])
plt.loglog(spectrum_energy,sed_SYN,lw=2,label='Sync',c=naima.plot.color_cycle[1])
plt.xlabel('Photon energy [{0}]'.format(
        spectrum_energy.unit.to_string('latex_inline')))
plt.ylabel('$E^2 dN/dE$ [{0}]'.format(
        sed_SYN.unit.to_string('latex_inline')))
plt.ylim(1e-12, 1e-6)
#plt.ylim(1e-31, 1e-12)
plt.tight_layout()
plt.legend(loc='lower left')