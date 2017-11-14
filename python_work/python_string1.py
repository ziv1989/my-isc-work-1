#!/bin/env python
#Script from the second exercise about strings from ncas-isc

s = "I love to write python"
split_s=s.split()

#>=0 is required because word in split_s returns -1 is false
#and 'if -1' returns true
for word in split_s:
    if word.lower().find('i')>=0:
	print "I found 'i' in: '{0}'".format(word)    
