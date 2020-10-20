# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 01:01:30 2020

@author: HP FOLIO 9480M
"""
'''Problem 2_2:
Write a function 'problem2_2()' that takes a list and does the following to it.
0) print the whole list (this doesn't require a while or for loop)
1) print the item with index 0
2) print the last item in the list
3) print the items with indexes 3 through 5 but not including 5
4) print the items up to the one with index 3 but not including item 3
5) print the items starting at index 3 and going through the end.
6) print the length of the list ( use len() )
7) Use the append() method of a list to append the letter "z" onto a list.
 Print the list with z appended.
'''
def problem2_2(my_list):
    print(my_list)
    print(my_list[0])
    print(my_list[-1])
    print(my_list[3:5]) 
    print(my_list[:3])
    print(my_list[3:])
    print(len(my_list))
    my_list.append('z')
    print(my_list)