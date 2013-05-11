from TweetReader import Tweet,TweatReader
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

tweets=TweatReader.readTsvFile('data/Tweets.txt')

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
    hour = time_delta.seconds / 3600
    
    # increase per hour count
    points_of_graph[hour]+=1

plt.plot(range(N_points) ,points_of_graph)
plt.ylabel('Tweet volume')
plt.xlabel('Hour')
plt.show()
