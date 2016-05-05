#!/usr/bin/python

'''
Reducer for finding the number of rides for every day during an hour by age group
'''

import sys

current_key = None
count = 0

for line in sys.stdin:
	ride_information = line.strip().split('\t')

	key = ride_information[0]
	value = int(ride_information[1])
	if (current_key != key):
		if current_key:
			print "%s\t%d" % (current_key, count)

		current_key = key
		count = value

	else:
		count += value

print "%s\t%d" % (current_key, count)
