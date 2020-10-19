# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:11:47 2020

@author: HP FOLIO 9480M
"""
'''Write a function problem1_7() that computes the area of a trapezoid. Here is the
formula: A = (1/2)(b1+b2)h. '''
def problem1_7():
    b1=float(input("Enter the length of one of the bases:"))

    b2=float(input("Enter the length of the other base:"))

    h=float(input('Enter the height:'))
    A = (1/2)*((b1+b2)*h)

    print('The area of a trapezoid with bases',b1,'and',b2,'and height',h,'is',A)
