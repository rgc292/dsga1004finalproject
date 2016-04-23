#!/usr/bin/python

'''
Mapper for finding the number of rides for every day during an hour
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

		if trip_details[-1][0] == '"':
			gender_field = trip_details[-1][1:-1]
		else:
			gender_field = trip_details[-1]

		if int(gender_field) == 1:	# Male
			gender = 'M'
		
		elif int(gender_field) == 2:	# Female
			gender = 'F'

		else:				# Unknown
			gender = 'U'

		print "%s,%d,%s\t%d" % (date, hour, gender, 1)
