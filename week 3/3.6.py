# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:39:14 2020

@author: HP FOLIO 9480M
"""
'''Problem 3_6:
Write a program (not just a function, but a stand alone program or script) that
reads through a file and writes another file that gives the length of each line
in the first file. If line is the line that you've read into your program, use
line.strip("\n") to strip away the invisible newline character at the end of
each line. Otherwise, your count will be one higher than the autograder's.'''
    
import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]

infile = open(inputfile)
outfile = open(outputfile,'w')

for line in infile:
    lin= line.strip("\n")
    outfile.write(str(len(lin))+"\n")

infile.close()
outfile.close()