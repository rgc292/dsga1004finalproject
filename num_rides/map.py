#!/usr/bin/python

'''
Mapper for finding the number of rides for every day during an hour
'''

import sys

for line in sys.stdin:
	trip_details = line.strip().split(',')	# Splitting the columns of a CSV file

	if 'tripduration' not in trip_details:	# Ignoring the row containing column names
		start_time = trip_details[1]	# Start time. Eg: "1/1/2015 11:01"

		if start_time[0] == '"':	# Some rows have the dates encoded in quotes (")
			start_time = start_time[1:-1]

		time_information = start_time.strip().split(' ')
		date = time_information[0]	# Extracting date - MM/DD/YYYY
		hour = int(time_information[1].strip().split(':')[0])	# Hour : 0-23

		print "%s,%d\t%d" % (date, hour, 1)	# Output of map phase
