# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:53:23 2020

@author: simon
"""

balance = 999999 # the outstanding balance on the credit card
annualInterestRate = 0.18 # annual interest rate as a decimal

# convert to monthly value
monthlyInterestRate = annualInterestRate / 12
monthlyPayUpper = (balance * ((1 + monthlyInterestRate) ** 12)) / 12
monthlyPayLower = balance / 12


# define a function that computes the balance after 12months
def EndBal(balance, monthlyInterestRate, monthlyPaymentAmt):
    '''
    Return: [float] the balance after 12 months of interest and repayments
    balance: [int] starting balance
    monthlyInterestRate: [float] monthly interest rate as a decimal
    monthlyPaymentAmt: [int] monthly payment amount
    '''
    for i in range(12):
        balance = (1 + monthlyInterestRate) * (balance - monthlyPaymentAmt)
    return balance

# define a recursive function to compute the min mthly payment    
def PayOff(balance, monthlyInterestRate, monthlyPayUpper, monthlyPayLower):
    '''
    Return: [int] the minimum monthly payment amount to cover the balance in 12 months
    balance: [int] starting balance
    monthlyInterestRate: [float] monthly interest rate as a decimal
    monthlyPaymentAmt: [int] monthly payment amount
    '''
    monthlyPaymentAmt = (monthlyPayUpper + monthlyPayLower) / 2
    EndBalance = round(EndBal(balance, monthlyInterestRate, monthlyPaymentAmt), 2)

    if EndBalance > 0:
        print('Payments:', monthlyPaymentAmt,'Balance:', EndBalance)  
        return PayOff(balance, monthlyInterestRate, monthlyPayUpper, monthlyPaymentAmt)
    elif EndBalance < 0:
        print('Payments:', monthlyPaymentAmt,'Balance:', EndBalance)
        return PayOff(balance, monthlyInterestRate, monthlyPaymentAmt, monthlyPayLower)
    else:
        print('Payments:', monthlyPaymentAmt,'Balance:', EndBalance)
        return monthlyPaymentAmt    
    
print('Lowest Payment:', round( PayOff(balance, monthlyInterestRate, monthlyPayUpper, monthlyPayLower), 2 ) )        