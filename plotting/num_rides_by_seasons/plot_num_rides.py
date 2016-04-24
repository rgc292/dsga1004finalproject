'''
Code to plot the total number of rides taken during every hour of the day during the 4 seasons - Spring, Summer, Fall, Winter

Author: Varun D N
Project: Big Data

Input: Data directory. Inside the directory there should be 4 files - spring.txt, summer.txt, fall.txt and winter.txt.
	   The names of the files should be exactly the same.

Output: Continuous plot with 4 subplots representing the 4 seasons mentioned above
'''

import sys
import matplotlib.pyplot as plt
import matplotlib
import datetime

# Spring data
spring_dates = []
spring_num_rides = []

# Summer data
summer_dates = []
summer_num_rides = []

# Fall data
fall_dates = []
fall_num_rides = []

# Winter data
winter_dates = []
winter_num_rides = []

plt.close('all')

with open(sys.argv[1] + "/spring.txt", 'r') as f:
	for line in f:
		data = line.strip().split('\t')
		date = data[0]
		rides = data[1]

		spring_dates.append(date)
		spring_num_rides.append(rides)

with open(sys.argv[1] + "/summer.txt", 'r') as f:
	for line in f:
		data = line.strip().split('\t')
		date = data[0]
		rides = data[1]

		summer_dates.append(date)
		summer_num_rides.append(rides)

with open(sys.argv[1] + "/fall.txt", 'r') as f:
	for line in f:
		data = line.strip().split('\t')
		date = data[0]
		rides = data[1]

		fall_dates.append(date)
		fall_num_rides.append(rides)

with open(sys.argv[1] + "/winter.txt", 'r') as f:
	for line in f:
		data = line.strip().split('\t')
		date = data[0]
		rides = data[1]

		winter_dates.append(date)
		winter_num_rides.append(rides)

f, axarr = plt.subplots(2, 2, figsize = (10, 10))

axarr[0, 0].plot(xrange(1, len(spring_num_rides) + 1), spring_num_rides, 'g')	# Green - Spring
axarr[0, 0].set_title('Spring')
axarr[0, 0].set_xlim([1, len(spring_num_rides) + 1])
axarr[0, 0].set_xlabel('Date and Hour')
axarr[0, 0].set_ylabel('Number of rides')

axarr[0, 1].plot(xrange(1, len(summer_num_rides) + 1), summer_num_rides, 'y')	# Yellow - Summer
axarr[0, 1].set_title('Summer')
axarr[0, 1].set_xlim([1, len(summer_num_rides) + 1])
axarr[0, 1].set_xlabel('Date and Hour')
axarr[0, 1].set_ylabel('Number of rides')

axarr[1, 0].plot(xrange(1, len(fall_num_rides) + 1), fall_num_rides, 'brown')	# Fall - Brown
axarr[1, 0].set_title('Fall')
axarr[1, 0].set_xlim([1, len(fall_num_rides) + 1])
axarr[1, 0].set_xlabel('Date and Hour')
axarr[1, 0].set_ylabel('Number of rides')

axarr[1, 1].plot(xrange(1, len(winter_num_rides) + 1), winter_num_rides, 'b')	# Winter - Blue
axarr[1, 1].set_title('Winter')
axarr[1, 1].set_xlim([1, len(winter_num_rides) + 1])
axarr[1, 1].set_xlabel('Date and Hour')
axarr[1, 1].set_ylabel('Number of rides')

f.tight_layout()	# Fits the space
f.subplots_adjust(top=0.88)	# Adjusts the space between the main title and the plots
if len(sys.argv) == 3:
	f.suptitle("Number of rides taken every hour, every day in 2015 - " + sys.argv[2], fontsize = 18)	# Main title for the subplots
else:
	f.suptitle("Number of rides taken every hour, every day in 2015", fontsize = 18)	# Main title for the subplots
plt.show()