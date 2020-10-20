# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:55:12 2020

@author: HP FOLIO 9480M
"""
'''Problem 4_1:
Write a function that will sort an alphabetic list (or list of words) into
alphabetical order. '''
firstline = ["Happy", "families", "are", "all", "alike;", "every", \
              "unhappy", "family", "is", "unhappy", "in", "its", "own", \
              "way.", "Leo Tolstoy", "Anna Karenina"] 
def problem4_1(wordlist):
    print(wordlist)
    print(sorted(wordlist,key=str.lower))