'''
Program to segregate the days into weekdays and weekends. 
Before this program is run, create two directories named - 'weekdays' and 'weekends'.

Assumption: This program assumes that there are 24 lines pertaining to each day. This logic is used in deciding whether 
			a day is a weekday or a weekend.

Author: Varun D N
Project: Big Data

Input: Input data file name, Number between 1-7 (1 - Sunday) indicating the day of the first line, name of the output file

Output: The respective output file will be in the weekdays and weekends directories.
'''

import sys

input_data = sys.argv[1]
starting_day = int(sys.argv[2])
output_file_name = sys.argv[3]

weekdays = []
weekends = []

hour_counter = 1
day_number = starting_day

with open(input_data, 'r') as ip:
	for line in ip:
		if day_number == 1 or day_number == 7:
			weekends.append(line)

		else:
			weekdays.append(line)

		if hour_counter == 24:
			day_number = (day_number % 7) + 1

		hour_counter = (hour_counter % 24) + 1

weekdays_file = open('weekdays/' + output_file_name, 'a')

for w in weekdays:
	weekdays_file.write(w)

weekdays_file.close()

weekends_file = open('weekends/' + output_file_name, 'a')

for w in weekends:
	weekends_file.write(w)

weekends_file.close()