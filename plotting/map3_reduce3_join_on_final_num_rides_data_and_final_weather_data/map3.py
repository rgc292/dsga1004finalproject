#!/usr/bin/python

'''
Mapper for finding the number of rides for every day during an hour
'''

import sys

for line in sys.stdin:
	data = line.strip().split('\t')	# Splitting the columns of a CSV file
	size = data[1].split(',')
	
	if len(size) == 1: # rides
	    print data[0].strip(),
	    print '\t'+data[1].strip()
	
	else:
	    print data[0].strip(),
	    print '\t'+data[1].strip()

	