#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    data = line
    
    # Map weather-data dataset having key as (date,time), and values as (DIR,SPD,GUS,TEMP,DEWP,SLP,STP,MAX,MIN,PCP01,PCP06,PCP24,SD)
    if data[0:6] != "USUSAF":
        if data[21:23] == "00":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(0).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "01":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(1).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "02":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(2).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "03":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(3).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "04":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(4).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "05":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(5).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "06":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(6).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "07":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(7).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "08":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(8).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
                
        if data[21:23] == "09":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(9).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
                
        if data[21:23] == "10":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(10).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "11":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(11).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "12":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(12).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "13":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(13).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "14":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(14).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "15":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(15).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "16":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(16).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "17":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(17).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "18":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(18).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "19":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(19).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "20":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(20).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "21":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(21).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "22":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(22).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
            
        if data[21:23] == "23":
            print '%s/%s/%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (data[17:19].strip(),data[19:21].strip(),data[13:17].strip(),str(23).strip(),data[23:25].strip(),data[26:29].strip(),data[30:33].strip(),data[34:37].strip(),data[42:45].strip(),data[83:86].strip(),data[89:92].strip(),data[93:99].strip(),data[106:112].strip(),data[113:116].strip(),data[117:120].strip(),data[121:126].strip(),data[127:132].strip(),data[133:138].strip(),data[145:147].strip())
