'''
Created on 10 May 2013

@author: Floris
'''
import matplotlib.pyplot as plt
import Methods.PreProcessing as prpr
import csv

# Main
def main():
    allTweets()
    perTag()
    return

# Version two
def perTag():
    tags, tweet_dict = prpr.countTweetTags("data/scrapeCompanies.txt","byDay")
    keylist = tweet_dict.keys()
    keylist.sort()   
    with open("data/frequency3.csv", "wb") as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Year-month-day_hour'] + tags)
        for key in keylist:
            values = []
            for tag in tags:
                if tag in tweet_dict[key]:
                    values.append(tweet_dict[key][tag])
                else:
                    values.append("0")
            writer.writerow([key]+values)        
        
# Version one
def allTweets(showGraph=False):
    tweet_dict = prpr.countAllTweets("data/scrapeDJIA.txt")
    keylist = tweet_dict.keys()
    keylist.sort()
    
    # Write csv file
    with open("data/frequency.csv", "wb") as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Year-month-day_hour', 'tweetcount'])
        for key in keylist:
            writer.writerow([key, tweet_dict[key]])
        csvfile.close()                         
    if(showGraph):
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
    
if __name__ == '__main__':
    main()
