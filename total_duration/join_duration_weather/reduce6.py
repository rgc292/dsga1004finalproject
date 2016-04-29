#!/usr/bin/python

'''
Reducer join the final_weather_data.txt and the final_total_duration data
'''

import sys

duration = {}
weather = {}
id = []

for line in sys.stdin:

	data = line.strip().split('\t')
	size = data[1].strip().split(',')
	
	if ((len(size)!=1)):
	    weather[data[0].strip()]=data[1].strip()
		
	else:
	    duration[data[0].strip()]=data[1].strip()

for j in sorted(duration.items()):
    for i in sorted(weather.items()):

        if i[0].strip()==j[0].strip():
            id.append(j[0].strip())
            print j[0],
            print '\t' + j[1] + ',' + i[1].strip()
                
for key in weather.keys():
    if key.strip() not in id:
        print key.strip()+'\t'+'0'+','+weather[key].strip() 
