# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 20:15:38 2017

@author: tedoreve
"""

import random as ran
import matplotlib.pyplot as plt

#===============================character======================================
class character(object):
    
    def __init__(self,name,money):            
        self.name   = name
        self.money  = money
        
    def give_money(self):    
        self.money -= 1
        
    def accept_money(self):
        self.money += 1
#        self.life   = self.belief*self.pop
#        self.magic  = self.belief/self.pop
#=================================main=========================================
if __name__=='__main__':
    pool   = []
    people = 45
    init_m = 45
    cycle  = 5000 
    
    for i in range(people):
        pool.append(character('id'+str(i),init_m))
        
    for j in range(50):
        for i in range(people):
            idnumber = ran.randint(0,people-1)
            pool[i].give_money()
            pool[idnumber].accept_money()
    
    now_m  = []
    for i in range(people):
        now_m.append(pool[i].money)
    now_m.sort()   
    plt.plot(now_m)
    