'''
Program to convert dates in string format to date objects and sort according to the time

Author: Varun D N
Project: Big Data
'''

'''
Input: File name

To use this program specifically for the purpose stated above, run the following command:
		python sort_by_time.py num_rides_data.txt | sort > formated_num_rides.txt
'''

import datetime
import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		data = line.strip().split('\t')

		formated_date = datetime.datetime.strptime(data[0], "%m/%d/%Y,%H")

		print formated_date,
		print '\t' + data[1]

