# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:01:49 2020

@author: simon
"""

s = input("provide a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowelsInS = [v for v in s if v in vowels]

print("Number of vowels: ", len(vowelsInS))