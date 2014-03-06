'''
Created on 6 Mar 2014

@author: simon
'''
#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint
import math

class retrieve(object):
    '''
    classdocs
    '''


    def __init__(self,lat,lon):
        '''
        Constructor
        '''
        self.lat = lat
        self.lon = lon
        self.request = urllib2.Request('http://demo.ckan.org/api/3/action/dashboard_activity_list')
        self.request.add_header('Authorization', '6c05da93-c769-4781-a5cf-40361a8cecfe')
        
    def getNearestSensorOLD(self,exclude,type):
        distance = 999999999999
        sensorID = 0
        tempData = json.load(urllib2.urlopen('https://smartstreets.sensetecnic.com/wotkit/api/sensors?text=%s' % type))
        for item in tempData:
            if not self.isIdBanned(exclude,item["id"]):
                sLat = item["latitude"]
                sLon = item["longitude"]
                sDist = self.calculateDistance(sLat, sLon)
                if sDist<distance:
                    distance = sDist
                    sensorID = item["id"]
                
        return [sensorID,distance]
    
    def getNearestSensor(self,exclude,type):
        distance = 999999999999
        sensorID = 0
        request = urllib2.Request('https://smartstreets.sensetecnic.com/wotkit/api/sensors?text=%s' % type)
        request.add_header('x-api-key', '6c05da93-c769-4781-a5cf-40361a8cecfe')
        tempData = json.load(urllib2.urlopen(request))
        for item in tempData:
            if not self.isIdBanned(exclude,item["id"]):
                sLat = item["latitude"]
                sLon = item["longitude"]
                sDist = self.calculateDistance(sLat, sLon)
                if sDist<distance:
                    distance = sDist
                    sensorID = item["id"]
                
        return [sensorID,distance]
    
    
    def getNearestTemperatureSensor(self,exclude):
        [sensorID,distance] = self.getNearestSensor(exclude, "temperature")
        return [sensorID,distance] 
    
    def getNearestGullySensor(self,exclude):
        [sensorID,distance] = self.getNearestSensor(exclude, "Gully")
        return [sensorID,distance] 
    
    def getNearestPothole(self):
        [sensorID,distance] = self.getNearestSensor([], "Pothole")
        return [distance]
    
    def getLatestTempAtID(self,sensorID):
        request = urllib2.Request("https://smartstreets.sensetecnic.com/wotkit/api/sensors/%d/data?beforeE=5" % sensorID)
        request.add_header('x-api-key', '6c05da93-c769-4781-a5cf-40361a8cecfe')
        tempData = json.load(urllib2.urlopen(request))
        intTimeStamp = 0
        friendlyTimeStamp = '1979-02-14T00:00:00Z'
        temperatureReading = 99
        for item in tempData:
            if item["timestamp"]>=intTimeStamp:
                intTimeStamp = item["timestamp"]
                temperatureReading = item["value"]
                friendlyTimeStamp = item["timestamp_readable"]
        return[temperatureReading,friendlyTimeStamp]
        
    def getLatestGullySiltLevelAtID(self,sensorID):
        request = urllib2.Request("https://smartstreets.sensetecnic.com/wotkit/api/sensors/%d/data?beforeE=5" % sensorID)
        request.add_header('x-api-key', '6c05da93-c769-4781-a5cf-40361a8cecfe')
        tempData = json.load(urllib2.urlopen(request))
        intTimeStamp = 0
        friendlyTimeStamp = '1979-02-14T00:00:00Z'
        siltReading = 200
        for item in tempData:
            if item["timestamp"]>=intTimeStamp:
                intTimeStamp = item["timestamp"]
                siltReading = item["siltLevel"]
                friendlyTimeStamp = item["timestamp_readable"]
        return[siltReading,friendlyTimeStamp]
        
        
        
    def getLatestValidTemperature(self):
        exclude=[]
        while True:
            [senID,dist] = self.getNearestTemperatureSensor(exclude)
            [temp,time] = self.getLatestTempAtID(senID)
            if temp != 99:
                break
            else:
                exclude.append(senID)
        return [temp,dist,time]
    
    def getLatestValidGulleySiltLevel(self):
        exclude=[]
        while True:
            [senID,dist] = self.getNearestGullySensor(exclude)
            [level,time] = self.getLatestGullySiltLevelAtID(senID)
            if level != 200:
                break
            else:
                exclude.append(senID)
        return [level,dist,time]               
                
    def calculateDistance(self,lat,lon):
        #dlat = self.lat-lat
        #dlon = self.lon-lon
        #return math.sqrt(math.pow(dlat,2)+math.pow(dlon,2))
        return self.haversineDistance([self.lat,self.lon], [lat,lon])
    
    def haversineDistance(self,origin, destination):
        lat1, lon1 = origin
        lat2, lon2 = destination
        radius = 6371 # km

        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c
    
        return d
    
    def isIdBanned(self,excluded,test):
        for sid in excluded:
            if test==sid:
                return True
        return False