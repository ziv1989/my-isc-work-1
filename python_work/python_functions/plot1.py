#!/bin/env python2.7

import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

time=[0,1,2,3,4,5,6]
co2=[250,265,272,260,300,320,389]
temp=[14.1,15.5,16.3,18.1,17.3,19.1,20.2]

plt.plot(time,co2,'b--',time,temp,'r')
plt.title(r'Chemistry Data')
plt.xlabel(r'\rm{Time (s)}')
plt.ylabel(r'$\rm{CO}_2$ (ppm)')
plt.legend()


plt.show()