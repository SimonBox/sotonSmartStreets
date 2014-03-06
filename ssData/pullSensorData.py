'''
Created on 6 Mar 2014

@author: simon
'''
import getopt
import sys
import retrieve


def main(argv,dir):
    try:
        opts, args = getopt.getopt(argv, "x:y:", ["Lat=","Lon="])
    except getopt.GetoptError:
        print "Incorrect specification of command line arguments"
        sys.exit(2)
        
    r = retrieve(52.577,-1.827)
    [temp,tDist,tTime] = r.getLatestValidTemperature()
    [level,sDist,sTime] = r.getLatestValidGulleySiltLevel()
    [distance] = r.getNearestPothole()
    print temp,tDist,tTime
    