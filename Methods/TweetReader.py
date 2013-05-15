'''
Created on 11-May.-2013

@author: Kevin
'''

from datetime import datetime
from Classes import Tweet

class TweetReader:
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
    
    @staticmethod
    def preprocessTweets(list_of_tweets):
        import os.path
        path = os.path.abspath(os.path.join(os.pardir, "data"))
        #stopWords = self.getStopWords(path + "\\StopWords.txt")
        #goodFeelings, badFeelings = self.getEmotionWords(path + "\\Emotions.txt")