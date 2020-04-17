# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 13:47:15 2020

@author: simon
"""

def lessThan4(aList):
    '''
    aList: a list of strings
    
    returns a new list that only contains strings with fewer than 4 characters
    '''
    newList = []    
    for word in aList:
        if len(word) < 4:            
            newList.append(word)  
    
    return newList

def lessThan4a(aList):
    '''
    aList: a list of strings
    
    returns a new list that only contains strings with fewer than 4 characters
    '''    
    return [word for word in aList if len(word) < 4]

# Test The Functions
aList = ['Mike', 'Peter', 'Tom', 'JP']
print(lessThan4(aList))
print(lessThan4a(aList))