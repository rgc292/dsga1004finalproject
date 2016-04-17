#!/usr/bin/python

import sys

save = {}

datehour = []
min = []
val = []


#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Fill in your reduce code here. To write to output file, use "print"
    line = line.strip()
    data = line
    
    data = line.split('\t')
    
    data[0] = data[0].strip()
    data[1] = data[1].strip()
    
    
    # Get one weather information for each hour per each day. This is the latest data for the specific hour
    if data[0][0:-3] in save.keys():
        if int(data[0][-2:]) > int(save[data[0][0:-3]]['min']):
            save[data[0][0:-3]]['min'] = data[0][-2:]
            save[data[0][0:-3]]['val'] = data[1]
            
    else:
        save[data[0][0:-3]] = {'min': data[0][-2:], 'val': data[1]}
    
           
for i in save:
    print '%s\t%s' % (str(i),str(save[i]['val']))
    
