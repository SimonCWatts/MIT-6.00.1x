# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:56:32 2020

@author: simon
"""
# Write a function is_triangular that meets the specification below.
# A triangular number is a number obtained by the continued summation of integers starting from 1.
# For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.


def gen_tri(n):
    '''
    n, a positive integer
    returns the sum of integers between 1 and n
    '''
    triangle = 0
    for i in range(1, n+1):
        triangle += i
    return triangle


print('n:', 1, 'tri:', gen_tri(1))

print('n:', 2, 'tri:', gen_tri(2))

print('n:', 3, 'tri:',gen_tri(3))

print('n:', 4, 'tri:',gen_tri(4))

print('n:', 5, 'tri:',gen_tri(5))



def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #YOUR CODE HERE
    def gen_tri(n):
        '''
        n, a positive integer
        returns the sum of integers between 1 and n
        '''
        tri = 0
        for i in range(1, n+1):
            tri += i
        return tri

    list_of_triangles = []

    for i in range(int(k/2) + 1):
        list_of_triangles.append(gen_tri(i))

    if k == 1 or k == 3:
        return True
    else:
        return k in list_of_triangles
