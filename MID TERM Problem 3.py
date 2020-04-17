# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:56:15 2020

@author: simon
"""



def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    y = 0  
    while x >= b ** y:
        y += 1   
  
    return y-1 


# Test
x = 10
b = 1.001

print('program says', myLog(x, b))

import math
print('answer is', math.log(x, b))