#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 01:06:26 2018

@author: marwansalama
"""
r = 0.04
portion_down_payment = 0.25
semi_annual_raise = 0.07
total_cost = 1000000
annual_salary = float(input("Enter the starting salary:​ "))
number_of_months = 36
allowed_deviation = 100
upper_bound = 10000
lower_bound = 0
current_savings = 0.0
number_of_iterations = 0
best_rate = -1.0

while lower_bound < upper_bound and (upper_bound-lower_bound) > 1:
    number_of_iterations += 1
    salary = annual_salary
    print("upper_bound: ",upper_bound, "lower_bound: ", lower_bound,"ratio= ",((upper_bound+lower_bound)/2)/10000)
    for month in range(number_of_months+1):
       
        if month%6 == 0 and month > 0:
            salary = annual_salary + annual_salary*semi_annual_raise
        current_savings = current_savings + (current_savings*r/12) + (salary/12)* (((upper_bound+lower_bound)/2)/10000)
        
    if abs(current_savings-total_cost*portion_down_payment) <= allowed_deviation:
        best_rate = ((upper_bound - lower_bound)/2)/100
        print("current_savings: ", current_savings )
        break
    elif current_savings < (total_cost * portion_down_payment):
        lower_bound = int((upper_bound + lower_bound)/2)
    else:
        upper_bound = int((upper_bound + lower_bound)/2)
    print("current_savings: ", current_savings )
    current_savings = 0

if best_rate != -1.0:
    print("Best savings rate: "+str(best_rate))
    print("Steps in bisection search: "+str(number_of_iterations))
else:
    print("It is not possible to pay the down payment in three years.")