# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:01:49 2020

@author: simon
"""

s = input("provide a string: ") 
#s = 'azcbobobegghakl'
substring = ''
longest = ''

for idx in range(len(s)):
    if s[idx - 1] <= s[idx]:
        substring += s[idx]
    else:
        substring = s[idx]
        
    if len(substring) > len(longest):
        longest = substring
    
print("Longest substring in alphabetical order is:", longest)