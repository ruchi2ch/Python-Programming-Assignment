# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:18:24 2020
7/17/2016

@author: HP FOLIO 9480M
"""
'''Problem 3_4:
Write a function that is complementary to the one in the previous problem that
will convert a date such as June 17, 2016 into the format 6/17/2016. '''
def problem3_4(mon, day, year):
    months = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"Septemper":9,"October":10,"November":11,"December":12}
    #for x in months:
    if mon=="January":
        print(str(months["January"])+'/'+str(day)+'/'+str(year))
    elif mon=="February":
        print(str(months["February"])+'/'+str(day)+'/'+str(year))
    elif mon=="March":
        print(str(months["March"])+'/'+str(day)+'/'+str(year))
    elif mon=="April":
        print(str(months["April"])+'/'+str(day)+'/'+str(year))
    elif mon=="May":
        print(str(months["May"])+'/'+str(day)+'/'+str(year))
    elif mon=="June":
        print(str(months["June"])+'/'+str(day)+'/'+str(year))
    elif mon=="July":
        print(str(months["July"])+'/'+str(day)+'/'+str(year))
    elif mon=="August":
        print(str(months["August"])+'/'+str(day)+'/'+str(year))
    elif mon=="September":
        print(str(months["September"])+'/'+str(day)+'/'+str(year))
    elif mon=="October":
        print(str(months["October"])+'/'+str(day)+'/'+str(year))
    elif mon=="November":
        print(str(months["November"])+'/'+str(day)+'/'+str(year))
    elif mon=="December":
        print(str(months["December"])+'/'+str(day)+'/'+str(year))