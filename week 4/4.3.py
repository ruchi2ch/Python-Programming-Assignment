# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:17:23 2020

@author: HP FOLIO 9480M
"""
'''Problem 4_3:
Write a function problem4_3(product, cost) so that you can enter the product
and its cost and it will print out nicely. Specifically, allow 25 characters
for the product name and left-justify it in that space; allow 6 characters for
the cost and right justify it in that space with 2 decimal places. Precede the
cost with a dollar-sign. There should be no other spaces in the output.
'''

def problem4_3(product, cost):
    print('{0:<25}${1:>6.2f}'.format(product,cost))