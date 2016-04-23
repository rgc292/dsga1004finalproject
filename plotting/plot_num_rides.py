'''
Code to plot the total number of rides taken during every hour of the day throughout the year

Author: Varun D N
Project: Big Data

Input: Data File
'''

import sys
import matplotlib.pyplot as plt

num_rides = []

with open(sys.argv[1], 'r') as f:
	for line in f:
		data = line.strip().split('\t')
		date = data[0]
		rides = data[1]

		num_rides.append(rides)

plt.plot(xrange(1, len(num_rides) + 1), num_rides, 'r')
plt.xlabel('Date and Hour')
plt.ylabel('Number of rides')
plt.title("Number of rides taken every hour, every day throughout the year")
plt.show()