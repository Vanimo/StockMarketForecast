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

def findHashTags(tweet, tags):    
    tweetTag = []
    for group in tags:
        groupTag = group[0]
        for tag in group:
            if tag in tweet.lower():
                tweetTag.append(groupTag)
    return tweetTag

class NestedDict(dict): #http://ohuiginn.net/mt/2010/07/nested_dictionaries_in_python.html
    def __getitem__(self, key):
        if key in self: return self.get(key)
        return self.setdefault(key, NestedDict())
        

def countTweetTags(sFile):
    twitterFile = open(sFile)
    my_dict = NestedDict()
    searchedTags = [['#ibm'], ['#aapl'], ['#msft', '#microsoft'], ['#facebook']]
    tagHeaders = []
    for tagList in searchedTags:
        tagHeaders.append(tagList[0])
    
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
            
        stamp = str(time[0]) + "-" + addZeroMonth + str(time[1]) + "-" + addZeroDay + str(time[2]) + "_" + addZeroHour + str(time[3])
        tags = findHashTags(parts[3], searchedTags)
        for tag in tags:
            if (tag in my_dict[stamp]):
                my_dict[stamp][tag] += 1
            else:
                my_dict[stamp][tag] = 1
    twitterFile.close()
    return tagHeaders, my_dict