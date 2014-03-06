'''
Created on 6 Mar 2014

@author: simon
'''
#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint
from retrieve import retrieve

##authorization
request = urllib2.Request('http://demo.ckan.org/api/3/action/dashboard_activity_list')
request.add_header('Authorization', '6c05da93-c769-4781-a5cf-40361a8cecfe')
#response_dict = json.loads(urllib2.urlopen(request, '{}').read())

r = retrieve(52.577,-1.827)
[temp,dist,time] = r.getLatestValidTemperature()


data = json.load(urllib2.urlopen('https://smartstreets.sensetecnic.com/wotkit/api/sensors?text=temperature'))
#for item in data:
#    if item["latitude"] <= 50:
#        print "hello"
# Use the json module to dump a dictionary to a string for posting.
#data_string = urllib.quote(json.dumps({'id': 'data-explorer'}))
#data_string = urllib.quote(json.dumps('id'))

# Make the HTTP request.
#response = urllib2.urlopen('http://demo.ckan.org/api/3/action/group_list',data_string)
#assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
#response_dict = json.loads(response.read())

# Check the contents of the response.
#assert response_dict['success'] is True
#result = response_dict['result']
#pprint.pprint(result)
