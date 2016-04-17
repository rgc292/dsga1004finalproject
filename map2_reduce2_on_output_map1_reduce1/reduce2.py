#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    data = line.split('\t')
    
    data[0] = data[0].strip()
    data[1] = data[1].strip()
    
    datetime = data[0].split(',')
    
    day = datetime[0][3:5]
    month = datetime[0][0:2]
    year = datetime[0][6:10]
    hour = datetime[1]
    #min = datetime[2]
    
    # Convert time from GMT to EST taking into account difference between EST and EDT
    if month == '12':
        if day == '01':
            if hour == '0':
                day = '30'
                hour = '19'
                month = '11'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                
            elif hour == '1':
                day = '30'
                hour = '20'
                month = '11'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '2':
                day = '30'
                hour = '21'
                month = '11'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '3':
                day = '30'
                hour = '22'
                month = '11' 
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                               
            elif hour == '4':
                day = '30'
                hour = '23'
                month = '11'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
            else:
                h = int(hour)-5
                hour = str(h)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
        else:
            if hour == '0':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '19'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                
            elif hour == '1':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '20'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '2':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '21'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '3':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '22' 
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                               
            elif hour == '4':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '23'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
            else:
                h = int(hour)-5
                hour = str(h)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
    
    elif month == '01':
        if day == '01':
            if hour == '0':
                day = '31'
                hour = '19'
                month = '12'
                year = '2014'
                #print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                
            elif hour == '1':
                day = '31'
                hour = '20'
                month = '12'
                year = '2014'
                #print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '2':
                day = '31'
                hour = '21'
                month = '12'
                year = '2014'
                #print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '3':
                day = '31'
                hour = '22'
                month = '12' 
                year = '2014'
                #print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                               
            elif hour == '4':
                day = '31'
                hour = '23'
                month = '12'
                year = '2014'
                #print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
            else:
                h = int(hour)-5
                hour = str(h)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
        else:
            if hour == '0':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '19'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                
            elif hour == '1':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '20'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '2':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '21'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '3':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '22' 
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                               
            elif hour == '4':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '23'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
            else:
                h = int(hour)-5
                hour = str(h)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
    
    elif month == '02':
        if day == '01':
            if hour == '0':
                day = '31'
                hour = '19'
                month = '01'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                
            elif hour == '1':
                day = '31'
                hour = '20'
                month = '01'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '2':
                day = '31'
                hour = '21'
                month = '01'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '3':
                day = '31'
                hour = '22'
                month = '01' 
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                               
            elif hour == '4':
                day = '31'
                hour = '23'
                month = '01'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
            else:
                h = int(hour)-5
                hour = str(h)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
        else:
            if hour == '0':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '19'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                
            elif hour == '1':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '20'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '2':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '21'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '3':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '22' 
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                               
            elif hour == '4':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '23'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
            else:
                h = int(hour)-5
                hour = str(h)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
    
    elif month in ['04','06','09']:
        if day == '01':
            if hour == '0':
                day = '31'
                hour = '20'
                m = int(month)-1
                month = '0'+str(m)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                
            elif hour == '1':
                day = '31'
                hour = '21'
                m = int(month)-1
                month = '0'+str(m)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '2':
                day = '31'
                hour = '22'
                m = int(month)-1
                month = '0'+str(m)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '3':
                day = '31'
                hour = '23'
                m = int(month)-1
                month = '0'+str(m)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
            else:
                h = int(hour)-4
                hour = str(h)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
        else:
            if hour == '0':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '20'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                
            elif hour == '1':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '21'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '2':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '22'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '3':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '23' 
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
            else:
                h = int(hour)-4
                hour = str(h)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
    
    elif month in ['05','07','08','10']:
        if day == '01':
            if hour == '0':
                if month == '08':
                    day = '31'
                else:
                    day = '30'
                hour = '20'
                m = int(month)-1
                month = '0'+str(m)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                
            elif hour == '1':
                if month == '08':
                    day = '31'
                else:
                    day = '30'
                hour = '21'
                m = int(month)-1
                month = '0'+str(m)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '2':
                if month == '08':
                    day = '31'
                else:
                    day = '30'
                hour = '22'
                m = int(month)-1
                month = '0'+str(m)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '3':
                if month == '08':
                    day = '31'
                else:
                    day = '30'
                hour = '23'
                m = int(month)-1
                month = '0'+str(m)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
            else:
                h = int(hour)-4
                hour = str(h)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
        else:
            if hour == '0':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '20'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                
            elif hour == '1':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '21'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '2':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '22'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
            elif hour == '3':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '23' 
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
            else:
                h = int(hour)-4
                hour = str(h)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
    elif month == '03':
        if int(day) <= 9:
            if int(day) == 1:
                if hour == '0':
                    day = '28'
                    hour = '19'
                    m = int(month)-1
                    month = '0'+str(m)
                    print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

                elif hour == '1':
                    day = '28'
                    hour = '20'
                    m = int(month)-1
                    month = '0'+str(m)
                    print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

                elif hour == '2':
                    day = '28'
                    hour = '21'
                    m = int(month)-1
                    month = '0'+str(m)
                    print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

                elif hour == '3':
                    day = '28'
                    hour = '22'
                    m = int(month)-1
                    month = '0'+str(m)
                    print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

                elif hour == '4':
                    day = '28'
                    hour = '23'
                    m = int(month)-1
                    month = '0'+str(m)
                    print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1]) 
                
                else:
                    h = int(hour)-5
                    hour = str(h)
                    print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])  
                    
            elif int(day) > 1:
                if hour == '0':
                    d = int(day)-1
                    day = '0'+str(d)
                    hour = '19'
                    print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                
                elif hour == '1':
                    d = int(day)-1
                    day = '0'+str(d)
                    hour = '20'
                    print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
                elif hour == '2':
                    d = int(day)-1
                    day = '0'+str(d)
                    hour = '21'
                    print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                                
                elif hour == '3':
                    d = int(day)-1
                    day = '0'+str(d)
                    hour = '22' 
                    print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                                               
                elif hour == '4':
                    d = int(day)-1
                    day = '0'+str(d)
                    hour = '23'
                    print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
                
                else:
                    if int(day) == 9:
                        h = int(hour)-4
                    else:
                        h = int(hour)-5
                    hour = str(h)
                    print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])   

        elif int(day) > 9:
            if hour == '0':
                d = int(day)-1
                if int(day) <= 10:
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '20'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
							
            elif hour == '1':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '21'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
											
            elif hour == '2':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '22'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
											
            elif hour == '3':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '23' 
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])
			
            else:
                h = int(hour)-4
                hour = str(h)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1]) 
                
    elif month == '11':
        if day == '01':
			if hour == '0':
				day = '31'
				hour = '20'
				m = int(month)-1
				month = str(m)
				print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

			elif hour == '1':
				day = '31'
				hour = '21'
				m = int(month)-1
				month = str(m)
				print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

			elif hour == '2':
				day = '31'
				hour = '22'
				m = int(month)-1
				month = str(m)
				print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

			elif hour == '3':
				day = '31'
				hour = '23'
				m = int(month)-1
				month = str(m)
				print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

			elif hour == '4':
				day = '31'
				hour = '23'
				m = int(month)-1
				month = str(m)
				print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1]) 
			
			else:
				h = int(hour)-5
				hour = str(h)
				print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])  

        else:
            if hour == '0':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '19'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

            elif hour == '1':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '20'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

            elif hour == '2':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '21'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

            elif hour == '3':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '22' 
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

            elif hour == '4':
                d = int(day)-1
                if int(day) <= 10: 
                    day = '0'+str(d)
                else:
                    day = str(d)
                hour = '23'
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])

            else:
                h = int(hour)-5
                hour = str(h)
                print '%s/%s/%s,%s\t%s' % (month,day,year,hour,data[1])   