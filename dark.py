# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 18:00:29 2017

@author: tedoreve
"""

from astropy import constants as con
from astropy import units as un
import numpy as np
import matplotlib.pyplot as plt
from galpy.potential import MWPotential2014
from galpy.potential import plotRotcurve
#import galpy.util.bovy_conversion as conv

class darkMatter(object):
    
    def __init__(self,r,v1,v2,n1,n2,T1,T2):
        self.r  = r
        self.v1 = v1
        self.v2 = v2
        self.n1 = n1
        self.n2 = n2
        self.T1 = T1
        self.T2 = T2
        self._GalacticMass = 7e11*con.M_sun
        
    def rotation_model1(self):
        '''
        prove that pressure can provide force comparable to gravity
        '''
        e1 = con.m_p*self.v1**2
        e2 = 2*con.k_B*self.T1
        print('Centrifugal force: ',e1.to('J'))
        print('Pressure:          ',e2.to('J'))     
        
    def rotation_model2(self):
        '''
        prove that pressure can contribute to the rotation model
        '''
        a1 = self.v1**2/self.r
        a2 = con.G*0.2*self._GalacticMass/self.r**2
        deltaP = (self.n2*self.T2-self.n1*self.T1)*con.k_B/r*10
        a3 = deltaP/(self.n1*con.m_p)
        print('Centrifugal force: ',a1.to('m/s^2'))
        print('Gravity:           ',a2.to('m/s^2'))
        print('Pressure:          ',a3.to('m/s^2'))
        
    def rotation_model_new(self):
        '''
        more accurate quantitative estimation
        '''
        
    def test_model(self,mod):
        '''
        calculate the necessary Pressure gradience curve
        '''
        
        if 'model' in mod:
            plotRotcurve(MWPotential2014,Rrange=[0.01,10.],grid=1001,yrange=[0.,1.2])
            MWPotential2014[0].plotRotcurve(Rrange=[0.01,10.],grid=1001,overplot=True)
            MWPotential2014[1].plotRotcurve(Rrange=[0.01,10.],grid=1001,overplot=True)
            MWPotential2014[2].plotRotcurve(Rrange=[0.01,10.],grid=1001,overplot=True)
        
        if 'obs' in mod: 
            rv_obs = np.loadtxt('../data/rotation_obs.txt')                
            plt.plot(rv_obs[:,0]/24,rv_obs[:,1]/220) #units: 8 kpc, 220 km/s
        
        if 'pre' in mod:
            #let pressure force = dark matter gravity force
            r = [(i+1)/10 for i in range(100)]
#            v0 = [MWPotential2014[0].vcirc((i+1)/10) for i in range(100)] 
#            v1 = [MWPotential2014[1].vcirc((i+1)/10) for i in range(100)] 
            v2 = [MWPotential2014[2].vcirc((i+1)/10) for i in range(100)]
            
            rho0 = [MWPotential2014[0].dens((i+1)/10,0) for i in range(100)] 
            rho1 = [MWPotential2014[1].dens((i+1)/10,0) for i in range(100)] 
#            rho2 = [MWPotential2014[2].dens((i+1)/10,0) for i in range(100)] 
            rho  = np.array(rho0) + np.array(rho1)# + np.array(rho2)
            rho  = rho*un.M_sun/un.pc**3
#            plt.plot(r,rho)
            
#            a0 = (np.array(v0)*220*un.km/un.s)**2/(np.array(r)*8*un.kpc) 
#            a1 = (np.array(v1)*220*un.km/un.s)**2/(np.array(r)*8*un.kpc) 
            a2 = (np.array(v2)*220*un.km/un.s)**2/(np.array(r)*8*un.kpc) 
#            v3 = ((a0+a1+a2)*(np.array(r)*8*un.kpc))**0.5/(220*un.km/un.s)
#            plt.plot(r,v0)
#            plt.plot(r,v1)
#            plt.plot(r,v2)
            
            deltaP = (-a2*rho).to('Pa/kpc')
            deltaT = (deltaP/rho*con.m_p/con.k_B).to('K/kpc')
            plt.plot(r,deltaT)
            
    
            r = np.array(r)*8*un.kpc
            T = [self.T2,]
            for i in range(99):
                T.append((T[i]+deltaT[99-i]*(r[99-i]-r[98-i])))
            
            def get_value(li):
                arr = []
                for i in li:
                    arr.append(i.value)
                return arr
            T.reverse()
            T = get_value(T)
#            plt.plot(r,T)
#            plt.xlim(15,)
                
        
if __name__=='__main__':
    r   = 1e5*un.lyr/2
    v1  = 230*un.km/un.s
    v2  = 180*un.km/un.s
    n1  = 1*un.cm**-3
    n2  = 0.1*un.cm**-3
    T1  = 100*un.K
    T2  = 5e6*un.K 
    dM  = darkMatter(r,v1,v2,n1,n2,T1,T2)
    dM.rotation_model1()
    dM.rotation_model2()
    dM.test_model(['pre'])
