'''
Created on 11-May.-2013

@author: Kevin
'''

from datetime import datetime

class TweatReader:
    # read TSV file quick and dirty
    @staticmethod
    def readTsvFile(name):
        file_to_read=open(name,'r')
        list_of_tweets=[]
        for line in file_to_read:
            split_tabs=line.split('\t')
            if len(split_tabs)>=4:
                list_of_tweets.append(Tweet(split_tabs[0], split_tabs[3],_date=split_tabs[1][:-6],_user=split_tabs[2]))
        return list_of_tweets
    
    @staticmethod
    def preprocessTweets(list_of_tweets):
        stopWords = getStopWords("StopWords.txt")
        goodFeelings, badFeelings = getEmotionWords("Emotions.txt")
        
    @staticmethod
    def getStopWords(link): #De stopwoorden uit het document halen.
        SWs = []
        f = open(link, 'rU')
        for line in f:
            SWs.append(line.rstrip('\n'))
            return SWs
        
    @staticmethod
    def getEmotionWords(link): #De stopwoorden uit het document halen.
        badFeelings = []
        goodFeelings = []  
        f = open(link, 'rU')  
        for line in f:
            split_tabs=line.split('\t')
            if len(split_tabs)>=2:
                if split_tabs[1]==1:
                    goodFeelings.append(split_tabs[0])
                else:
                    badFeelings.append(split_tabs[0])
        return goodFeelings, badFeelings

class Tweet:
    def __init__(self, _id, _tweet,_date="Mon, 01 January 1900 00:00:00", _user="",_label=0):
        self.id=_id
        self.date=datetime.strptime(_date,"%a, %d %B %Y %H:%M:%S")
        self.user=_user
        self.tweet=_tweet.rstrip('\n')
        self.label=int(_label)