# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:33:10 2020

@author: HP FOLIO 9480M
"""
'''Problem 2_6:
Let's continue with our simulation of dice by rolling two of them. This time
each die can come up with a number from 1 to 6, but you have two of them. The
result or outcome is taken to be the sum of the pips on the two dice. Write a
program that will roll 2 dice and produce the outcome. This time let's roll
the two dice 100 times. Print the outcomes one outcome per line.
"""
'''
import random
def problem2_6():
    s=0
    random.seed(431)
    for i in range(0,100):
        d1, d2 = (random.randint(1,6), random.randint(1,6))
        s= d1 + d2 
        print(s)
        s=0   