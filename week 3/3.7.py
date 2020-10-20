# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:18:47 2020

@author: HP FOLIO 9480M
"""
'''Problem 3_7:
Write a function that would read a CSV file that looks like this, flowers.csv:
petunia,5.95
alyssum,3.95
begonia,5.95
sunflower,5.95
coelius,4.95
and look up the price of a flower and print out that price.'''
import csv
def problem3_7(csv_pricefile,flower):
    with open(csv_pricefile, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for r in reader:
               if flower in r:
                   print(r[1])