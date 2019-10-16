#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 23:34:06 2018

@author: marwansalama
"""
r = 0.04
current_savings = 0.0
portion_down_payment = 0.25
number_of_months = 0
annual_salary = float(input("Enter your annual salary:​ "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
down_payment_required = portion_down_payment*total_cost

while current_savings < portion_down_payment*total_cost:
    current_savings = current_savings+(current_savings*r/12) + (annual_salary/12)*portion_saved
    number_of_months = number_of_months + 1
    
print("Number of months:​ "+str(number_of_months))