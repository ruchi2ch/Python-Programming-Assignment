# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:57:59 2020

@author: HP FOLIO 9480M
"""
'''Problem 1_5:
Write a function 'problem1_5(age)'. This function should use if-elif-else
statement to print out "Have a glass of milk." for anyone under 7; "Have
a coke." for anyone under 21, and "Have a martini." for anyone 21 or older.
'''
def problem1_5(age):
    if age<7:
        print("Have a glass of milk.") 
    elif age<21:
        print("Have a coke.") 
    else:
        print("Have a martini.")