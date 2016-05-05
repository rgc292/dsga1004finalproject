#!/usr/bin/python

'''
Mapper for finding the number of rides for every day during an hour by age group
'''

import sys

for line in sys.stdin:
	trip_details = line.strip().split(',')

	if 'tripduration' not in trip_details:
		start_time = trip_details[1]

		if start_time[0] == '"':
			start_time = start_time[1:-1]

		time_information = start_time.strip().split(' ')
		date = time_information[0]
		hour = int(time_information[1].strip().split(':')[0])
		
		age = trip_details[-2]
		
		if '"' in trip_details[-2]:
			age = trip_details[-2][1:-1]
		
		#print "%s" % (age)
		if age:
			if int(age) >= 1994: #age <= 20 
				print "%s,%s,%d\t%d" % (date,str(20),hour, 1)
			
			elif (int(age) < 1994) and (int(age) >= 1979): # 20 > age <= 35
				print "%s,%s,%d\t%d" % (date,str(35),hour, 1)
		
			elif (int(age) < 1979) and (int(age) >= 1964): # 35 > age <= 50
				print "%s,%s,%d\t%d" % (date,str(50),hour, 1)
		
			elif (int(age) < 1964): # age > 50
				print "%s,%s,%d\t%d" % (date,str(99),hour, 1)
		