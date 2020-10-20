# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 01:13:05 2020

@author: HP FOLIO 9480M
"""
'''Problem 2_3:
Write a function problem2_3() that should have a 'for' loop that steps
through the list below and prints the name of the state and the number of
letters in the state's name. You may use the len() function.'''
def problem2_3(ne):
    for i in range(0,len(ne)):
        print(ne[i],'has',len(ne[i]),'letters.')
        
        