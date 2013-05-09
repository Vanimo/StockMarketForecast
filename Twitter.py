'''
Created on 8-mei-2013

@author: Brecht Deconinck
@author: Floris Cockaerts

Handles the twitter API for searching tweets
'''
import json
import urllib2
import IO

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
    for i in range(0,size):
        row = [None]*4
        row[0] = tweets[i]['id']
        row[1] = tweets[i]['created_at']
        row[2] = tweets[i]['from_user']
        row[3] = tweets[i]['text']
        data.append(row)
    return data

def searchTwitterFrom(tag,lasttweetid):
    query = "%23" + str(tag) + "%20last_id%3A" + lasttweetid
    return searchTwitter(query)
def searchTwitterTag(tag):
    query = "%23" + str(tag)
    return searchTwitter(query)

if __name__ == '__main__':
    #Get Tweets
    arrTweets = searchTwitterTag("IBM")
    #Write Tweets to File
    IO.writeData("data/Tweets.txt", arrTweets)
    #Read Tweets From File
    tweets = IO.readData("data/Tweets.txt")
    #Show Tweets
    print tweets   
