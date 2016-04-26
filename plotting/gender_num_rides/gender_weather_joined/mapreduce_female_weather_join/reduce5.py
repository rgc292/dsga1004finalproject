#!/usr/bin/python

'''
Reducer join the final_weather_data.txt and the final_rides_by_gender data
'''

import sys

rides = {}
weather = {}
id = []

for line in sys.stdin:

	data = line.strip().split('\t')
	
	if (data[0][-1:] != 'F'):
	    weather[data[0].strip()]=data[1].strip()
		
	else:
	    rides[data[0].strip()]=data[1].strip()
	    print data[0]+'\t'+data[1]


'''for j in sorted(rides.items()):
    for i in sorted(weather.items()):

        if i[0].strip()==j[0][0:-2].strip():
            id.append(j[0][0:-2].strip())
            print j[0],
            print '\t' + j[1][1:] + ',' + i[1].strip()'''
              
for i in rides.keys():
    id.append(i[0:-2])
  
for key in weather.keys():
    if key.strip() not in id:
        print key.strip()+','+'F'+'\t'+'0'+','+weather[key].strip()
