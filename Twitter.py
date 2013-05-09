'''
Created on 8-mei-2013

@author: Brecht Deconinck
@author: Floris Cockaerts

Handles the twitter API for searching tweets
'''
import json
import urllib2
import IO
import time

def main():
    return

# https://dev.twitter.com/docs/using-search

def searchTwitter(query):
    url = "https://search.twitter.com/search.json?q=" + str(query)
    text = urllib2.urlopen(url).read()
    JS = json.loads(text)
    tweets = JS['results']
    size = len(tweets)
    data = []
    print "Number of tweets in JSON: " + str(len(tweets))
    for i in range(0,size):
        row = [None]*4
        row[0] = tweets[i]['id']
        row[1] = tweets[i]['created_at']
        row[2] = tweets[i]['from_user']
        row[3] = tweets[i]['text']
        data.append(row)
    return data

def searchTwitterFromID(tag,lasttweetid):
    query = "%23" + str(tag) + "%20since_id%3A" + str(lasttweetid)
    return searchTwitter(query)
def searchTwitterFromDate(tag, y, m, d):
    query = "%23" + str(tag) + "%20until%3A" + str(y) + "-" + str(m) + "-" + str(d)
    return searchTwitter(query)
def searchTwitterFromeDateAndID(tag, lastTweetID, y, m, d):
    query = "%23" + str(tag) + "%20until%3A" + str(y) + "-" + str(m) + "-" + str(d) + "%20since_id%3A" + str(lastTweetID)
    return searchTwitter(query)
def searchTwitterTag(tag):
    query = "%23" + str(tag)
    return searchTwitter(query)

def simpleSearch():
    #Get Tweets
    arrTweets = searchTwitterTag("IBM")
    #Write Tweets to File
    IO.writeData("data/Tweets.txt", arrTweets)
    #Read Tweets From File
    tweets = IO.readData("data/Tweets.txt")
    #Show Tweets
    print tweets   

if __name__ == '__main__':
    #simpleSearch()
    arrTweets = searchTwitterFromDate("IBM",2013,5,2)
    IO.writeData("data/scrapeTest.txt", arrTweets)
    lastID = arrTweets[-1][0]
    go_on = True
    
    while go_on:
        time.sleep(2)
        queryAnswer = searchTwitterFromeDateAndID("IBM", lastID, 2013,5,2)
        IO.writeData("data/scrapeTest.txt", queryAnswer)
        arrTweets += queryAnswer
        print "Tweets returned: " + str(len(queryAnswer))
        if(len(queryAnswer) < 1):
            go_on = False        
    IO.writeData("data/Tweets.txt", arrTweets)