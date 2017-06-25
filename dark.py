# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 18:00:29 2017

@author: tedoreve
"""

from astropy import constants as con
from astropy import units as un
#import numpy as np

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
        prove that pressure can provide force at same magnitude comparing 
        with gravity
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
        
    def rotation_model3(self):
        '''
        more accurate quantitative estimation
        '''
        
        
        
if __name__=='__main__':
    r  = 1e5*un.lyr/2
    v1 = 230*un.km/un.s
    v2 = 180*un.km/un.s
    n1  = 1*un.cm**-3
    n2  = 0.1*un.cm**-3
    T1  = 100*un.K
    T2  = 1e6*un.K 
    instance = darkMatter(r,v1,v2,n1,n2,T1,T2)
    instance.rotation_model1()
    instance.rotation_model2()