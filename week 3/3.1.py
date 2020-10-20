# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:06:59 2020

@author: HP FOLIO 9480M
"""
'''Problem 3_1:
Write a function that reads a text file and counts the number of characters in
it. Print both the text file and the number of characters.'''
def problem3_1(txtfilename):
    """ Opens file and prints its contents line by line. """
    infile = open(txtfilename)

    sum = 0

    for line in infile:
        sum = sum + len(line)
        print(line, end="") # the file has "\n" at the end of each line already

    print("\n\nThere are", sum, "letters in the file.")

    infile.close()