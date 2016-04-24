'''
Program to convert dates in string format to date objects. This code is specifically for sorting the gender data.

Author: Varun D N
Project: Big Data
'''

'''
Input: File name

To use this program specifically for the purpose stated above, run the following command:
		python sort_by_time_gender.py num_rides_data.txt | sort > formated_num_rides.txt
'''

import datetime
import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		data = line.strip().split('\t')
		key = data[0].strip().split(',')

		formated_date = datetime.datetime.strptime(key[0] + ',' + key[1], "%m/%d/%Y,%H")

		print formated_date,
		print ',' + key[2], 
		print '\t' + data[1]

