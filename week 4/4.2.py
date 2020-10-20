# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:17:22 2020

@author: HP FOLIO 9480M
"""
'''Problem 4_2:
Write a function that will compute and print the mean and standard deviation
of a list of real numbers '''
import random
numList = []
random.seed(150)
for i in range(0,25):
    numList.append(round(100*random.random(),1))

import statistics    
def problem4_2(ran_list):
    print(statistics.mean(ran_list))
    print(statistics.stdev(ran_list))
    