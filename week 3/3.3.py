# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:21:02 2020June 17, 2016


@author: HP FOLIO 9480M
"""
'''Problem 3_3:
Write a function that will convert a date from one format to another.
Specifically, 06/10/2016 should convert to June 17, 2016. Actually, you
will input the 6, the 17, and the 2016 as separate integers (numbers) and
the function will assemble and print the date as June 17, 2016. I suggest
that you create a tuple months = ("January", "February", "March", ...) to
store the names of the months. Then it is easy to access the name February
as months[1] and so on.
'''

def problem3_3(month, day, year):
    months=("January","February","March","April","May","June","July","August","Septemper","October","November","December") 
    if month==1:
        print(months[0]+' '+str(day)+', '+str(year))
    elif month==2:
        print(months[1]+' '+str(day)+', '+str(year))
    elif month==3:
        print(months[2]+' '+str(day)+', '+str(year))
    elif month==4:
        print(months[3]+' '+str(day)+', '+str(year))
    elif month==5:
        print(months[4]+' '+str(day)+', '+str(year))
    elif month==6:
        print(months[5]+' '+str(day)+', '+str(year))
    elif month==7:
        print(months[6]+' '+str(day)+', '+str(year))
    elif month==8:
        print(months[7]+' '+str(day)+', '+str(year))
    elif month==9:
        print(months[8]+' '+str(day)+', '+str(year))
    elif month==10:
        print(months[9]+' '+str(day)+', '+str(year))
    elif month==11:
        print(months[10]+' '+str(day)+', '+str(year))
    else:
        print(months[11]+' '+str(day)+', '+str(year))