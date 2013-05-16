'''
Created on 13 May 2013

@author: Floris
'''

import IO
from Classes import Tweet

def countAllTweets(sFile):
    twitterFile = open(sFile)
    my_dict = dict()
    for line in IO.readData_by_line(twitterFile):        
        tweet = Tweet.Tweet()
        tweet.setTweet(line)
        
        tag = tweet.getDate() + "_" + tweet.getHour()

        if (tag in my_dict):
            my_dict[tag] += 1
        else:
            my_dict[tag] = 1
    twitterFile.close()
    return my_dict

def countTweetTags(sFile, method="byDay"):
    twitterFile = open(sFile)
    my_dict = NestedDict()
    searchedTags = [['#ibm'], ['#aapl'], ['#msft', '#microsoft'], ['#facebook']]
    tagHeaders = []
    for tagList in searchedTags:
        tagHeaders.append(tagList[0])
    
    for line in IO.readData_by_line(twitterFile):
        tweet = Tweet.Tweet()
        tweet.setTweet(line)
               
        stamp = tweet.getDate()
        tags = findHashTags(tweet.message, searchedTags)
        for tag in tags:
            if (tag in my_dict[stamp]):
                my_dict[stamp][tag] += 1
            else:
                my_dict[stamp][tag] = 1
    twitterFile.close()
    return tagHeaders, my_dict


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