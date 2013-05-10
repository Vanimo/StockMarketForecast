'''
Created on 10 May 2013

@author: Floris
'''
import IO
from time import strptime

twitterFile = open("data/scrapeTest2.txt")
for tweet in IO.readData_by_line(twitterFile):
    parts = tweet.strip().split('\t')
    time = strptime(parts[1][5:-6], "%d %B %Y %H:%M:%S")
    """02 May 2013 19:14:07
    time.struct_time(tm_year=2013, tm_mon=5, tm_mday=2, tm_hour=19, tm_min=14, tm_sec=7, tm_wday=3, tm_yday=122, tm_isdst=-1)
    """
    print time
    break
twitterFile.close()