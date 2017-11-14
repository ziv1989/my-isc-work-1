#!/bin/env python

#Exercise 3 from ncas-isc reading and writing files in python

#Open the file and extract just the last rainfall values from the csv file
with open('/home/user01/my-isc-work/python_work/example_data/weather.csv', 'r') as reader:
    first_line=reader.readline()
    rain=[]
    for line in reader:
	line=line.strip()
	rain.append(float(line.split(",")[-1]))

print rain

with open('myrain.txt','w') as writer:
    for i in rain:
        writer.write(str(i)+'\n')