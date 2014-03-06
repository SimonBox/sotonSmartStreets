'''
Created on 6 Mar 2014

@author: simon
'''
#!/usr/bin/env python
from retrieve import retrieve
import sys

r = retrieve(sys.argv[1],sys.argv[2])
[temp,tDist,tTime] = r.getLatestValidTemperature()
print temp, tDist, tTime
[level,sDist,sTime] = r.getLatestValidGulleySiltLevel()
print level, sDist, sTime
[distance] = r.getNearestPothole()
print distance


