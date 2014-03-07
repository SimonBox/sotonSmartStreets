'''
Created on 6 Mar 2014

@author: simon
'''
#!/usr/bin/env python
from retrieve import retrieve
import sys
import json

# Sorry, slight change!
def getSensorData(latitude, longitude):
  #r = retrieve(float(sys.argv[1]),float(sys.argv[2]))
  r = retrieve(latitude,longitude)
  [temp,tDist,tTime] = r.getLatestValidTemperature()
  #print temp, tDist, tTime
  [level,sDist,sTime] = r.getLatestValidGulleySiltLevel()
  #print level, sDist, sTime
  [distance] = r.getNearestPothole()
  return json.dumps({"temperature(C)":temp, "thermometerDistance(km)":tDist, "thermometerTime":tTime, "siltLevel(%)":level, "siltSensorDistance(km)":sDist, "siltSensorTime":sTime, "nearestPotholeDistance(km)":distance},indent=4, separators=(',', ': '))



