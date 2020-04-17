# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:53:23 2020

@author: simon
"""
# set the three inputs
balance = 484 # the outstanding balance on the credit card
annualInterestRate = 0.2 # annual interest rate as a decimal
monthlyPaymentRate = .04  # minimum monthly payment rate as a decimal

def 
# convert to monthly values
monthlyInterestRate = annualInterestRate / 12

for i in range(12):
    # first subtract payments from the balance
    monthlyPaymentAmt = monthlyPaymentRate * balance
    balance -= monthlyPaymentAmt
    
    # second add the interest on the balance 
    balance += monthlyInterestRate * balance

print('Remaining balance:', round(balance, 2))