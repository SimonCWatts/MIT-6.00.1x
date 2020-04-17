# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:54:45 2020

@author: simon
"""

# You are given a dictionary aDict that maps integer keys to integer values.
# Write a Python function that returns a list of keys in aDict
# that map to dictionary values that appear exactly once in aDict.

# This function takes in a dictionary and returns a list.
# Return the list of keys in increasing order.
# If aDict does not contain any values appearing exactly once, return an empty list.
# If aDict is empty, return an empty list.
# For example:
# If aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} then your function should return [1, 3, 8]
# If aDict = {1: 1, 2: 1, 3: 1} then your function should return []

Dict1 = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0, 5:99}
Dict2 = {1: 1, 2: 1, 3: 1}
Dict3 = {}

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # count how many times each value occurs
    freqDict = {}
    for k, v in aDict.items():
        if v not in freqDict:
            freqDict[v] = 1
        else:
            freqDict[v] += 1

    # now return a list of unique values
    unique_values = []
    for k, v in freqDict.items():
        if v == 1:
            unique_values.append(k)

    # build a list of keys that correspond to the unique values
    unique_keys = []
    for k, v in aDict.items():
        if v in unique_values:
            unique_keys.append(k)

    # sort and return the list of unique keys
    return sorted(unique_keys)



## TEST CASES ##
print('Dict1 should return [1, 3, 5, 8]', 'Actual return is ', uniqueValues(Dict1))
print('Dict2 should return []', 'Actual return is ', uniqueValues(Dict2))
print('Dict3 should return []', 'Actual return is ', uniqueValues(Dict3))