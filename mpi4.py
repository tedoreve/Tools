import numpy as np
from mpi4py import MPI
import time
import pyPLUTO as pp

import naima
from multiprocessing import Pool
from naima.models import (ExponentialCutoffPowerLaw, Synchrotron,
                          InverseCompton)
from astropy.constants import c
import astropy.units as u
#==============================================================================
def f(rho, B):
    ECPL = ExponentialCutoffPowerLaw(1e36*rho*u.Unit('1/eV'), 1*u.TeV, 2.0, 13*u.TeV)
    SYN = Synchrotron(ECPL, B=1000*B*u.uG)
    
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
    spectrum_energy = np.logspace(13,14,1)*u.eV
    sed_IC = IC.sed(spectrum_energy, distance=1.5*u.kpc)
    
    return sed_IC.value
#==============================================================================

    

#==============================================================================
#n = 1 * u.cm**-3
#l = 1 * u.pc
#print((n*l**3).to('')) 
#==============================================================================
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
    
    rho_vol, B_vol = D.rho,(D.bx1**2+D.bx2**2)**0.5
    flux_vol = np.zeros([rho_vol.shape[2],rho_vol.shape[1],rho_vol.shape[0]])


#==============================================================================
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    per = rho_vol.shape[2]//size
    
    comm.Barrier()
    start_time = time.time()
    
    for i in range(per * rank, per * (rank+1)):
        for j in range(rho_vol.shape[1]):
            for k in range(rho_vol.shape[0]):
                flux_vol[i,j,k] = f(rho_vol[i,j,k], B_vol[i,j,k])
    
    
    if rank == 0:
        total = np.zeros([rho_vol.shape[2],rho_vol.shape[1],rho_vol.shape[0]])
    else:
        total = None
    
    comm.Barrier()
    #collect the partial results and add to the total sum
    comm.Reduce(flux_vol, total, op=MPI.SUM, root=0)
    
    stop_time = time.time()
    
    if rank == 0:
        print ("The sum of numbers from 1 to 1 000 000: ", total)
        print ("time spent with ", size, " threads in milliseconds")
        print ("-----", (stop_time-start_time)*1000, "-----")
        total.tofile("a.bin")
        
    