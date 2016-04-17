#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    data = line.split('\t')
    
    # Map weather-data dataset having key as (date,time), and values as (DIR,SPD,GUS,TEMP,DEWP,SLP,STP,MAX,MIN,PCP01,PCP06,PCP24,SD)
    print '%s\t%s' % (data[0],data[1])
                    
        