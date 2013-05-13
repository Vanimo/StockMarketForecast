'''
Created on 13 May 2013

@author: Floris
'''

import IO
from time import strptime

def countAllTweets(sFile):
    twitterFile = open(sFile)
    my_dict = dict()
    for tweet in IO.readData_by_line(twitterFile):
        parts = tweet.strip().split('\t')
        time = strptime(parts[1][5:-6], "%d %B %Y %H:%M:%S")
        """02 May 2013 19:14:07
        time.struct_time(tm_year=2013, tm_mon=5, tm_mday=2, tm_hour=19, tm_min=14, tm_sec=7, tm_wday=3, tm_yday=122, tm_isdst=-1)
        """
        addZeroHour = ''
        addZeroDay = ''
        addZeroMonth = ''
        if (int(time[3]) < 10):
            addZeroHour = '0'
        if (int(time[2]) < 10):
            addZeroDay = '0'
        if (int(time[1]) < 10):
            addZeroMonth = '0'
            
        tag = str(time[0]) + "-" + addZeroMonth + str(time[1]) + "-" + addZeroDay + str(time[2]) + "_" + addZeroHour + str(time[3])
        if (tag in my_dict):
            my_dict[tag] += 1
        else:
            my_dict[tag] = 1
    twitterFile.close()
    return my_dict