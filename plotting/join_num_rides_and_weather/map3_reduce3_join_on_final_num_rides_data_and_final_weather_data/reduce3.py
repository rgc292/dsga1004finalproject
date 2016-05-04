#!/usr/bin/python

'''
Reducer join the final_weather_data.txt and the final_num_rides_data
'''

import sys

rides = {}
weather = {}

for line in sys.stdin:
	data = line.strip().split('\t')
	size = data[1].strip().split(',')
	
	if (len(size)==1):
	    rides[data[0].strip()]=data[1].strip()
	    
	else:
	    weather[data[0].strip()]=data[1].strip()

march_missing = 0

for i in sorted(weather.items()):
    counter = 0
    for j in sorted(rides.items()):
        if i[0]==j[0]:
            if counter == 0:
                counter += 1
                print i[0],
                print '\t' + j[1] + ',' + i[1].strip()
                
            else:
                pass

        else:
            if counter == 0:
                counter += 1
                if i[0] in ['2015-03-08 02:00:00']:
                    
                    if march_missing < 12:
                        march_missing += 1
                        print i[0],
                        print '\t' + '0' + ',' + i[1].strip()
                elif i[0] in ['2015-03-28 02:00:00']:
                    if march_missing < 12:
                        march_missing += 1
                        print i[0],
                        print '\t' + '0' + ',' + i[1].strip()
                    
                elif i[0] in ['2015-03-28 03:00:00']:
                    if march_missing < 12:
                        march_missing += 1
                        print i[0],
                        print '\t' + '0' + ',' + i[1].strip()

                elif i[0] in ['2015-03-28 04:00:00']:
                    if march_missing < 12:
                        march_missing += 1
                        print i[0],
                        print '\t' + '0' + ',' + i[1].strip()
                elif i[0] in ['2015-03-28 05:00:00']:
                    if march_missing < 12:
                        march_missing += 1
                        print i[0],
                        print '\t' + '0' + ',' + i[1].strip()
                elif i[0] in ['2015-03-28 06:00:00']:
                    if march_missing < 12:
                        march_missing += 1
                        print i[0],
                        print '\t' + '0' + ',' + i[1].strip()
                elif i[0] in ['2015-03-28 07:00:00']:
                    if march_missing < 12:
                        march_missing += 1
                        print i[0],
                        print '\t' + '0' + ',' + i[1].strip()
                elif i[0] in ['2015-03-28 08:00:00']:
                    if march_missing < 12:
                        march_missing += 1
                        print i[0],
                        print '\t' + '0' + ',' + i[1].strip()
                elif i[0] in ['2015-03-28 09:00:00']:
                    if march_missing < 12:
                        march_missing += 1
                        print i[0],
                        print '\t' + '0' + ',' + i[1].strip()
                elif i[0] in ['2015-03-28 10:00:00']:
                    if march_missing < 12:
                        march_missing += 1
                        print i[0],
                        print '\t' + '0' + ',' + i[1].strip()
                elif i[0] in ['2015-03-28 12:00:00']:
                    if march_missing < 12:
                        march_missing += 1
                        print i[0],
                        print '\t' + '0' + ',' + i[1].strip()
                elif i[0] in ['2015-03-28 15:00:00']:
                    if march_missing < 12:
                        march_missing += 1
                        print i[0],
                        print '\t' + '0' + ',' + i[1].strip()
                else:
                    counter = 0

#for i in rides.keys():
    #for j in weather.keys():
        #if i==j:
            #print i,
            #print '\t' + rides[i] + ',' + weather[j].strip()
            #print ',' + weather[j].strip()
    