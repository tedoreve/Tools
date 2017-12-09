# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:37:38 2017

@author: tedoreve
"""

import random as ran
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

#===============================function=======================================
class pixel(object):
    
    def __init__(self,name,density):            
        self.name   = name
        self.dens   = density
        
    def give_density(self,num):    
        self.dens -= num
        
    def accept_density(self,num):
        self.dens += num
#        self.life   = self.belief*self.pop
#        self.magic  = self.belief/self.pop

def fun(x,p):
    n0,alpha = p
    return n0*x**-alpha
    
def residuals(p, y, z):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return (y - fun(z,p))
#=================================main=========================================
if __name__=='__main__':
    pool    = []
    pix_num = 128*128
    init_d  = 1000
    cycle   = 1000 
    
    for i in range(pix_num):
        pool.append(pixel('id'+str(i),init_d))
        
    for j in range(cycle):
        for i in range(pix_num):
            idnumber = ran.randint(0,pix_num-1)
            if pool[i].dens < 0:
                continue
            else:
                pool[i].give_density(pool[idnumber].dens/init_d)
                pool[idnumber].accept_density(pool[idnumber].dens/init_d)
    
    now_m  = []
    for i in range(pix_num):
        now_m.append(pool[i].dens)
    now_m.sort()   
    n, bins, patches = plt.hist(now_m)
    


#    p0 = [1,100]
#    plsq, pcov, infodict, errmsg, success = leastsq(residuals, p0,args=(n,bins[1:61]),full_output=1, epsfcn=0.0001)
#    x = np.linspace(0,10000,1000)
#    plt.plot(x, fun(x,plsq), 'r--', linewidth=2)
    