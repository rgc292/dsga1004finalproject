#!/usr/bin/python

'''
Mapper for preparing data to be joined
'''

import sys

for line in sys.stdin:
	data = line.strip().split('\t')	# Splitting the columns of a CSV file
	size = data[1].split(',')
	
	if len(size) == 1: # rides
	    date_gender = data[0].strip().split(',')
	    print date_gender[0].strip()+','+date_gender[1].strip()+'\t'+','+data[1].strip()
	
	else:
	    print data[0].strip()+'\t'+data[1].strip()

	