# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:37:38 2017

@author: tedoreve
"""

import random as ran
import matplotlib.pyplot as plt

#===============================character======================================
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
#=================================main=========================================
if __name__=='__main__':
    pool    = []
    pix_num = 128*128
    init_d  = 1000
    cycle   = 5000 
    
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
    plt.hist(now_m)
    