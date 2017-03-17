# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 09:28:42 2017

@author: tedoreve
"""

import hashlib
from read import read
from functools import reduce

md5  = hashlib.md5()
name = input('Please input your name:')
md5.update(name.encode('utf-8'))
name = md5.hexdigest()
f    = lambda x: (x[i:i+4] for i in range(29))
leaf = set(f(name))

code = read('code.txt')
code = list(map(str.split,code))
code = list(map(lambda x: list(map(str.lower,x)),code))
root1= list(r[0] for r in code)
root2= list(r[5] for r in code)
root = dict(zip(root1,root2))

radix= list(root.keys() & leaf)
g    = lambda x: (x[i] for i in radix)
virtual_name = list(g(root))

if virtual_name:
    print(reduce(lambda x,y:x+y,virtual_name))
else:
    print('Failed, your name is unique.')
