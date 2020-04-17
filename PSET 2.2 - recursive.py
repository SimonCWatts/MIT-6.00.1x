# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:53:23 2020

@author: simon
"""

balance = 510000 # the outstanding balance on the credit card
annualInterestRate = 0.02 # annual interest rate as a decimal

# guess a value for the payment amt as 1/12 the original balance (rounded to units of 10)
monthlyPaymentAmt = round(balance / 120, -1)    

# convert to monthly values
monthlyInterestRate = annualInterestRate / 12

# define a function that computes the balance after 12months
def EndBal(balance, monthlyInterestRate, monthlyPaymentAmt):
    '''
    Return: [float] the balance after 12 months of interest and repayments
    balance: [int] starting balance
    monthlyInterestRate: [float] monthly interest rate as a decimal
    monthlyPaymentAmt: [int] monthly payment amount
    '''
    for i in range(120):
        balance = (1 + monthlyInterestRate) * (balance - monthlyPaymentAmt)
    return balance

# define a recursive function to compute the min mthly payment    
def PayOff(balance, monthlyInterestRate, monthlyPaymentAmt):
    '''
    Return: [int] the minimum monthly payment amount to cover the balance in 12 months
    balance: [int] starting balance
    monthlyInterestRate: [float] monthly interest rate as a decimal
    monthlyPaymentAmt: [int] monthly payment amount
    '''
    # if the end balance is less or equal to zero then the monthlyPaymentAmt is sufficient to cover the balance
    if EndBal(balance, monthlyInterestRate, monthlyPaymentAmt) <= 0:
        return monthlyPaymentAmt
    else:
        return PayOff(balance, monthlyInterestRate, monthlyPaymentAmt + 10)

print('Lowest Payment:', round( PayOff(balance, monthlyInterestRate, monthlyPaymentAmt) ) )        