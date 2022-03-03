# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:31:23 2022

@author: Nilo Farfan
"""

#Assignment 1: Income Tax Calculator 

gross_income = float(input("Enter the gross income: "))
number_of_children = float(input("Enter the number of dependents:"))
standard_deduction = 10000
deduction_per_child = 3000
total_deductions = standard_deduction + deduction_per_child*number_of_children

taxable_income = gross_income - total_deductions
total_tax = taxable_income*0.20

print("\nThe income tax is:"+ "$",total_tax)
input("Press enter to submit to the I.R.S")
