#!/bin/env python2.7

import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig, ax1 = plt.subplots()

time=[0,1,2,3,4,5,6]
co2=[250,265,272,260,300,320,389]
temp=[14.1,15.5,16.3,18.1,17.3,19.1,20.2]

ax1.plot(time,co2,'r')
ax1.set_ylabel(r'$\rm{CO}_2$ (ppm)')
ax2=ax1.twinx()
ax2.set_ylabel(r'Temp')
ax2.plot(time,temp,'b--')

plt.show()