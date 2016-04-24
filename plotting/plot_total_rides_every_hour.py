'''
Program to aggreagate the total rides taken every hour during each season and plot a bar graph of it.

Input: Directory name containing the data files, Optional argument to make the plot title descriptive (eg: 'Weedays', 'Weekends')
Output: Bar chart of the total number of rides taken during every hour 
'''

import sys
import matplotlib.pyplot as plt
import matplotlib
import datetime
import numpy as np

spring_num_rides = [0] * 24	# Spring data
summer_num_rides = [0] * 24 	# Summer data
fall_num_rides = [0] * 24 	# Fall data
winter_num_rides = [0] * 24	# Winter data

plt.close('all')

with open(sys.argv[1] + "/spring.txt", 'r') as f:
	for line in f:
		data = line.strip().split('\t')
		hour = int(data[0].strip().split(' ')[1][:2])
		rides = int(data[1].strip().split(',')[0])

		spring_num_rides[hour] += rides

with open(sys.argv[1] + "/summer.txt", 'r') as f:
	for line in f:
		data = line.strip().split('\t')
		hour = int(data[0].strip().split(' ')[1][:2])
		rides = int(data[1].strip().split(',')[0])

		summer_num_rides[hour] += rides

with open(sys.argv[1] + "/fall.txt", 'r') as f:
	for line in f:
		data = line.strip().split('\t')
		hour = int(data[0].strip().split(' ')[1][:2])		
		rides = int(data[1].strip().split(',')[0])

		fall_num_rides[hour] += rides

with open(sys.argv[1] + "/winter.txt", 'r') as f:
	for line in f:
		data = line.strip().split('\t')
		hour = int(data[0].strip().split(' ')[1][:2])		
		rides = int(data[1].strip().split(',')[0])

		winter_num_rides[hour] += rides



f, axarr = plt.subplots(2, 2, figsize = (10, 10))

width = 0.75
ind = np.arange(1, len(spring_num_rides) + 1)

axarr[0, 0].bar(ind, spring_num_rides, width, color = 'g')	# Green - Spring
axarr[0, 0].set_title('Spring')
axarr[0, 0].set_xlim([1, len(spring_num_rides) + 1])
axarr[0, 0].set_xticks(ind + 0.75 / 2)
axarr[0, 0].set_xticklabels(tuple([str(i) for i in ind]))
axarr[0, 0].set_xlabel('Hour')
axarr[0, 0].set_ylabel('Total number of rides')

axarr[0, 1].bar(ind, summer_num_rides, width, color = 'y')	# Yellow - Summer
axarr[0, 1].set_title('Summer')
axarr[0, 1].set_xlim([1, len(summer_num_rides) + 1])
axarr[0, 1].set_xticks(ind + 0.75 / 2)
axarr[0, 1].set_xticklabels(tuple([str(i) for i in ind]))
axarr[0, 1].set_xlabel('Hour')
axarr[0, 1].set_ylabel('Total number of rides')

axarr[1, 0].bar(xrange(1, len(fall_num_rides) + 1), fall_num_rides, width, color = 'brown')	# Fall - Brown
axarr[1, 0].set_title('Fall')
axarr[1, 0].set_xlim([1, len(fall_num_rides) + 1])
axarr[1, 0].set_xticks(ind + 0.75 / 2)
axarr[1, 0].set_xticklabels(tuple([str(i) for i in ind]))
axarr[1, 0].set_xlabel('Hour')
axarr[1, 0].set_ylabel('Total number of rides')

axarr[1, 1].bar(xrange(1, len(winter_num_rides) + 1), winter_num_rides, width, color = 'b')	# Winter - Blue
axarr[1, 1].set_title('Winter')
axarr[1, 1].set_xlim([1, len(winter_num_rides) + 1])
axarr[1, 1].set_xticks(ind + 0.75 / 2)
axarr[1, 1].set_xticklabels(tuple([str(i) for i in ind]))
axarr[1, 1].set_xlabel('Hour')
axarr[1, 1].set_ylabel('Total number of rides')

f.tight_layout()	# Fits the space
f.subplots_adjust(top=0.88)	# Adjusts the space between the main title and the plots
if len(sys.argv) == 3:
	f.suptitle("Number of rides taken every hour, every day in 2015 - " + sys.argv[2], fontsize = 18)	# Main title for the subplots
else:
	f.suptitle("Number of rides taken every hour, every day in 2015", fontsize = 18)	# Main title for the subplots
plt.show()
