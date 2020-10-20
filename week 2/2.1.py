# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 00:56:55 2020

@author: HP FOLIO 9480M
"""
'''Problem 2_1:
Write a function 'problem2_1()' that sets a variable lis = list(range(20,30)) and
does all of the following, each on a separate line:
(a) print the element of lis with the index 3
(b) print lis itself
(c) write a 'for' loop that prints out every element of lis.'''
def problem2_1():
    lis = list(range(20,30))
    print(lis[3])
    print(lis)
    for i in range(0,len(lis)):
        print(lis[i],end=" ")