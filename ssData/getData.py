'''
Created on 6 Mar 2014

@author: simon
'''
#!/usr/bin/env python
from retrieve import retrieve
import sys
import json

r = retrieve(float(sys.argv[1]),float(sys.argv[2]))
[temp,tDist,tTime] = r.getLatestValidTemperature()
#print temp, tDist, tTime
[level,sDist,sTime] = r.getLatestValidGulleySiltLevel()
#print level, sDist, sTime
[distance] = r.getNearestPothole()
print json.dumps({"temperature(C)":temp, "thermometerDistance(km)":tDist, "thermometerTime":tTime, "siltLevel(%)":level, "siltSensorDistance(km)":sDist, "siltSensorTime":sTime, "nearestPotholeDistance(km)":distance},indent=4, separators=(',', ': '))




