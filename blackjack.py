# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:32:54 2017

@author: tedoreve
"""

#import numpy as np

pool = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
hand = []
while True:
    try:
        card = input('please input your card number: ')
        card = int(card)
    except:
        break
    hand.append(card)
    pool.remove(card)
    rest = 21 - sum(hand)
    add  = [x for x in pool if x <= rest]
    if len(add) < len(pool) - len(add):
        print('stop')
    else:
        print('go on')



