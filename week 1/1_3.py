# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:40:12 2020

@author: HP FOLIO 9480M
"""
'''Problem 1_3:
Write a function problem1_3(n) that adds up the numbers 1 through n and
prints out the result.
'''
def problem1_3(n):
    my_sum=0
    i=1
    while i<=n :  
        my_sum +=i
        i+=1
    print(my_sum)