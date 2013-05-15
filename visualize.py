from Methods.TweetReader import TweetReader
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from Classes import Tweet

def readAndShow(sFile):
    #tweets=TweetReader.readTsvFile('data/Tweets.txt')
    tweets=TweetReader.readTsvFile(sFile)
    
    # enter start date of game
    start_date=datetime.strptime("Thu, 02 May 2013 09:50:00","%a, %d %B %Y %H:%M:%S")
    # we set the duration of the game to 2 hours
    end_date=datetime.strptime("Thu, 09 May 2013 10:50:00","%a, %d %B %Y %H:%M:%S")
    
    #initialize list
    N_points = (end_date-start_date).seconds / 3600 + (end_date-start_date).days * 24 #per uur 
    points_of_graph=[0]*N_points
    
    
    for tweet in tweets:
        if tweet.date<start_date or tweet.date >= end_date:
            continue 
        # compute difference of dates, in seconds
        time_delta=tweet.date-start_date
        hour = time_delta.seconds / 3600 + time_delta.days * 24
        
        # increase per hour count
        points_of_graph[hour]+=1
    
    plt.plot(range(N_points) ,points_of_graph)
    plt.ylabel('Tweet volume')
    plt.xlabel('Hour')
    plt.show()

def createGraph(dataDict):
    keylist = dataDict.keys()
    keylist.sort()
    
    #initialize list
    N_points = len(keylist) #per uur 
    points_of_graph=[0]*N_points
    i = 0
    
    for key in keylist:
        points_of_graph[i] = dataDict[key]
        i += 1
    plt.plot(range(N_points) ,points_of_graph)
    plt.ylabel('Tweet volume')
    plt.xlabel('Hour')
    plt.show()