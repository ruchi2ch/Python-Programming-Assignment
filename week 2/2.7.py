# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 01:44:18 2020

@author: HP FOLIO 9480M
"""
'''Problem 2_7:
Heron's formula for computing the area of a triangle with sides a, b, and c is
as follows. Let s = .5(a + b + c) --- that is, 1/2 of the perimeter of the
triangle. Then the area is the square root of s(s-a)(s-b)(s-c). You can compute
the square root of x by x**.5 (raise x to the 1/2 power). Use an input
statement to get the length of the sides. Don't forget to convert this input
to a real number using float().'''

def problem2_7():
    one=float(input('Enter length of side one: '))
    two=float(input('Enter length of side two: '))
    three=float(input('Enter length of side three: '))
    s=0.5*(one+two+three)
    a=s*(s-one)*(s-two)*(s-three)
    ar=a**0.5
    print('Area of a triangle with sides',float(one),float(two),float(three),'is',float(ar))
    