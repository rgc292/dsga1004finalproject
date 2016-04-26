'''
Visualizes any numerical feature during all four seasons.

Input: Data directory name, Number indicating the index of the variable to be plotted, Variable name

Output: Plots of the feature throughout all the 4 seasons
'''

import sys
import matplotlib.pyplot as plt
import matplotlib
import datetime

# Spring data
spring_data = []

# Summer data
summer_data = []

# Fall data
fall_data = []

# Winter data
winter_data = []

feature = int(sys.argv[2])

plt.close('all')

with open(sys.argv[1] + "/spring.txt", 'r') as f:
	for line in f:
		data = line.strip().split('\t')

		try:
			if data[1].strip().split(',')[feature][0] != '*':		
				spring_data.append(float(data[1].strip().split(',')[feature]))	
			else:
				spring_data.append(0.)
		except IndexError:
			spring_data.append(0.)

with open(sys.argv[1] + "/summer.txt", 'r') as f:
	for line in f:
		data = line.strip().split('\t')
		
		try:
			if data[1].strip().split(',')[feature][0] != '*':		
				summer_data.append(float(data[1].strip().split(',')[feature]))	
			else:
				summer_data.append(0.)
		except IndexError:
			summer_data.append(0.)			

with open(sys.argv[1] + "/fall.txt", 'r') as f:
	for line in f:
		data = line.strip().split('\t')

		try:
			if data[1].strip().split(',')[feature][0] != '*':		
				fall_data.append(float(data[1].strip().split(',')[feature]))	
			else:
				fall_data.append(0.)
		except IndexError:
			fall_data.append(0.)

with open(sys.argv[1] + "/winter.txt", 'r') as f:
	for line in f:
		data = line.strip().split('\t')

		try:
			if data[1].strip().split(',')[feature][0] != '*':		
				winter_data.append(float(data[1].strip().split(',')[feature]))	
			else:
				winter_data.append(0.)
		except IndexError:
			winter_data.append(0.)

f, axarr = plt.subplots(2, 2, figsize = (10, 10))

axarr[0, 0].plot(xrange(1, len(spring_data) + 1), spring_data, 'g')	# Green - Spring
axarr[0, 0].set_title('Spring')
axarr[0, 0].set_xlim([1, len(spring_data) + 1])
axarr[0, 0].set_xlabel('Date and Hour')
axarr[0, 0].set_ylabel(sys.argv[3])

axarr[0, 1].plot(xrange(1, len(summer_data) + 1), summer_data, 'y')	# Yellow - Summer
axarr[0, 1].set_title('Summer')
axarr[0, 1].set_xlim([1, len(summer_data) + 1])
axarr[0, 1].set_xlabel('Date and Hour')
axarr[0, 1].set_ylabel(sys.argv[3])

axarr[1, 0].plot(xrange(1, len(fall_data) + 1), fall_data, 'brown')	# Fall - Brown
axarr[1, 0].set_title('Fall')
axarr[1, 0].set_xlim([1, len(fall_data) + 1])
axarr[1, 0].set_xlabel('Date and Hour')
axarr[1, 0].set_ylabel(sys.argv[3])

axarr[1, 1].plot(xrange(1, len(winter_data) + 1), winter_data, 'b')	# Winter - Blue
axarr[1, 1].set_title('Winter')
axarr[1, 1].set_xlim([1, len(winter_data) + 1])
axarr[1, 1].set_xlabel('Date and Hour')
axarr[1, 1].set_ylabel(sys.argv[3])

f.tight_layout()	# Fits the space
f.subplots_adjust(top=0.88)	# Adjusts the space between the main title and the plots
f.suptitle(sys.argv[3] + " at the end of every hour, every day in 2015", fontsize = 18)	# Main title for the subplots
plt.show()