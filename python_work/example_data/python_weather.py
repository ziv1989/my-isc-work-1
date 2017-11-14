#!/bin/env python

#Opening and reading weather.csv for ncas-isc

#Doing the whole file in one go
with open('weather.csv','r') as reader:
    data=reader.read()

print data
print "End of part one"
print

#Reading line by line
with open('weather.csv','r') as reader:
    line=reader.readline()
    while line != '':
        print line
	line=reader.readline()
print "It's over."