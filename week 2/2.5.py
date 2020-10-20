# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:31:35 2020

@author: HP FOLIO 9480M
"""
'''Problem 2_5:
Let's do a small simulation. Suppose that you rolled a die repeatedly. Each
time that you roll the die you get a integer from 1 to 6, the number of pips
on the die. Use random.randint(a,b) to simulate rolling a die 10 times and
printout the 10 outcomes. The function random.randint(a,b) will
generate an integer (whole number) between the integers a and b inclusive.
Remember each outcome is 1, 2, 3, 4, 5, or 6, so make sure that you can get
all of these outcomes and none other. Print the list, one item to a line so that
there are 10 lines as in the example run. Make sure that it has 10 items
and they are all in the range 1 through 6. '''
import random

def problem2_5():
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(171)
    for i in range(0,10):
        print(random.randint(1,6))