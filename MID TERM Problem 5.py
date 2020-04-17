# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 13:59:57 2020

@author: simon
"""

def keysWithValue1(aDict, target):
    '''
    aDict: a dictionary [keys and values are both integers]
    target: an integer
    
    returns a list of keys that correspond to the values that equal 'Target' sorted in increasing order
    if 'target' is not found in the dictionary then -1 is returned
    '''   
    return sorted([k for k, v in aDict.items() if v == target])

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary [keys and values are both integers]
    target: an integer
    
    returns a list of keys that correspond to the values that equal 'Target' sorted in increasing order
    if 'target' is not found in the dictionary then -1 is returned
    '''   
    
    ListOfKeys = []   
    for k, v in aDict.items():
       if v == target:
           ListOfKeys.append(k)   
    return sorted(ListOfKeys)

##### TEST THE FUNCITONS   
aDict = {11: 10, 2: 20, 3: 30, 4: 10, 9: 10, 5: 10}
target = 10

print(keysWithValue(aDict, target))
print(keysWithValue1(aDict, target))