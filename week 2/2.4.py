# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:20:57 2020

@author: HP FOLIO 9480M
"""
'''Problem 2_4:
random.random() generates pseudo-random real numbers between 0 and 1. Write a program to use only random.random()
to generate a list of random reals between 30 and 35.'''
import random
def problem2_4():
    listt=[]
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(70)
    for i in range(0,10):
        listt.append(30+5*random.random())
    print(listt)
        