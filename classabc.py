# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:43:44 2017

@author: tedoreve
"""

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests