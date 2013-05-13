'''
Created on 10 May 2013

@author: Floris
'''
import matplotlib.pyplot as plt

import Methods.PreProcessing as prpr

tweet_dict = prpr.countAllTweets("data/scrapeTest2.txt")
keylist = tweet_dict.keys()
keylist.sort()

# Write csv file
import csv
with open("data/frequency.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Year-month-day_hour', 'tweetcount'])
    for key in keylist:
        writer.writerow([key, tweet_dict[key]])
    csvfile.close()                         

#initialize list
N_points = len(keylist) #per uur 
points_of_graph=[0]*N_points
i = 0

for key in keylist:
    points_of_graph[i] = tweet_dict[key]
    i += 1
plt.plot(range(N_points) ,points_of_graph)
plt.ylabel('Tweet volume')
plt.xlabel('Hour')
plt.show()
