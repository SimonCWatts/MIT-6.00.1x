# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:01:49 2020

@author: simon
"""

s = input("provide a string: ") 

bobCount = len([1 for i in range(len(s)) if s[i : i + 3] == 'bob'])

print("Number of bobs:", bobCount)