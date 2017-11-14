#!/bin/env python
#for the Tuples Exercise from ncas-isc

my_list = [23,'fifty',7.344]

for item in enumerate(my_list):
    count, element =item
    print count, element

first,middle,last=my_list
print first
print middle
print last

first, middle, last = middle, last, first
print first
print middle
print last


