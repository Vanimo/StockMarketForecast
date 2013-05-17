'''
Created on 8-mei-2013

@author: Brecht Deconinck
'''
import Methods.IO as IO
from Classes import Tweet
from stemming.porter2 import stem
from datetime import datetime, timedelta
from decimal import *

def main():
    classifyTweetsDJIA(1)
    
def classifyTweetsDJIA(offset = 3):
    # TODO: Read last line of classified tweets
    
    history = priceHistoryDJIA()
    tweetFile = open("data/scrapeDJIA.txt")
    tweets = []    
    for line in IO.readData_by_line(tweetFile):
        tweet = Tweet.Tweet()
        tweet.setTweet(line)
        tweet.label = history[tweet.date.date()]
        tweets.append(tweet)        
    IO.writeTweets("data/ClassifiedDJIA", tweets, ['label', 'message'])

def priceHistoryDJIA():
    data = IO.readData("data/DJIA.csv")
    prices = {}
    first = True
    date = datetime.today()
    lastDate = date
    
    for line in data:
        lastDate = datetime.strptime(line[0], "%b %d, %Y")
        if first:
            date = lastDate
            first = False
        prices[lastDate] = Decimal(line[1])
        
    priceChanges = {}
    priceChange = 0
    while (date > lastDate):
        nextDay = date + timedelta(days=-1)
        if date in prices:            
            while nextDay not in prices:
                nextDay = nextDay + timedelta(days=-1)            
            if (prices[date] - prices[nextDay] >= 0):
                priceChange = 1
            else:
                priceChange = 0
        priceChanges[date.date()] = priceChange
        date = date + timedelta(days=-1)
    return priceChanges
    
def setTweetsEmotion():
    #Get Emotions
    arrEmo = getEmotions()
    #Analyse Tweet Emotion
    data = open("data/scrapeCompanies.txt")    
    #Read every tweet
    for line in IO.readData_by_line(data):
        tweet = Tweet.Tweet()
        tweet.setTweet(line)
        #Check every emotion
        value = 0
        for emo in arrEmo:
            word = emo[0]
            if word in tweet.message:
                #Update value by emotion
                if emo[1] == "1":
                    value = 1
                else:
                    value = -1
                if(value != 0):
                    break
            tweet.label = value
        print tweet.label, " " ,tweet.message

def getEmotions():
    arr = IO.readData("data/Emotions.txt")
    for index in range(0, len(arr)):
        arr[index][0] = stem(arr[index][0])
    return arr

if __name__ == '__main__':
    main()