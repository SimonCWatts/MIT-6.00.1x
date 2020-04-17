# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:57:20 2020

@author: simon
"""

# Write a Python function that creates and returns a list of prime numbers between 2 and N, inclusive,
# sorted in increasing order. A prime number is a number that is divisible only by 1 and itself.
# This function takes in an integer and returns a list of integers.

def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers between 2 and N, inclusive.
    List is sorted in increasing order
    '''
    # a function to generate prime numbers
    def genPrimes():
        '''
        A generator function that yields prime numbers.
        guess: current guess [int]
        p: list of all previously determined prime numbers.
        yield: next prime number
        '''
        x = 1                     #'x' is the current guess for a prime number
        p = []                    # 'p' is the list of all previous correct prime number
        while True:
            x += 1
            for prime in p:
                if x % prime == 0:
                    break         # if x is not prime, then move onto the next guess
            else:
                p.append(x)
                yield p

    prime = genPrimes()
    list_of_primes = prime.__next__()

    # generate a list of prime numbers until the largest value exceeds N
    while list_of_primes[-1] <= N:
        prime.__next__()

    # return the list of primes minus the final value
    return list_of_primes[:-1]




##################################################################
def genPrimes():
    '''
    A generator function that yields prime numbers.
    guess: current guess [int]
    p: list of all previously determined prime numbers.
    yield: next prime number
    '''
    x = 1                     #'x' is the current guess for a prime number
    p = []                    # 'p' is the list of all previous correct prime number
    while True:
        x += 1
        for prime in p:
            if x % prime == 0:
                break         # if x is not prime, then move onto the next guess
        else:
            p.append(x)
            yield x, p
####################################################################