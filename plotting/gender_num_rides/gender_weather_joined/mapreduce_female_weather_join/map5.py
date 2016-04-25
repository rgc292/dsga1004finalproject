#!/usr/bin/python

'''
Mapper for preparing data to be joined
'''

import sys

for line in sys.stdin:
	data = line.strip().split('\t')	# Splitting the columns of a CSV file
	
	if data[0][-1:] == 'F': # rides
	    print data[0].strip()+'\t'+','+data[1].strip()
	
	else:
	    print data[0].strip()+'\t'+data[1].strip()

	