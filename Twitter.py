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

def GET_Twitter(query):
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

def searchTwitter(tag,variables):
    query = "%23" + str(tag) + str(variables)
    return GET_Twitter(query)

def twitterUntil(y, m, d):
    # Returns tweets generated before the given date. Date should be formatted as YYYY-MM-DD.
    return "&until=" + str(y) + "-" + str(m) + "-" + str(d)
def twitterSince(y,m,d):
    # Return tweets generated after the given date.
    return "&since=" + str(y) + "-" + str(m) + "-" + str(d)
def twitterSinceID(lastTweetID):
    # Returns results with an ID greater than (that is, more recent than) the specified ID. 
    # There are limits to the number of Tweets which can be accessed through the API. 
    # If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.
    return "&since_id=" + str(lastTweetID)
def twitterMaxID(ID):
    # Returns results with an ID less than (that is, older than) or equal to the specified ID.
    return "&max_id=" + str(ID)
def twitterRPP(rpp):
    #The number of tweets to return per page, up to a max of 100.
    return "&rpp=" + str(rpp)
def twitterPage(page):
    # The page number (starting at 1) to return, up to a max of roughly 1500 results (based on rpp * page).
    return "&page=" + str(page)

def simpleSearch():
    #Get Tweets
    arrTweets = searchTwitter("IBM","")
    #Write Tweets to File
    IO.writeData("data/Tweets.txt", arrTweets)
    #Read Tweets From File
    tweets = IO.readData("data/Tweets.txt")
    #Show Tweets
    print tweets   

def searchTestTwo():
    s = twitterUntil(2013,5,2)
    arrTweets = searchTwitter("IBM",s)
    IO.writeData("data/scrapeTest.txt", arrTweets)
    lastID = arrTweets[0][0]
    go_on = False
    
    while go_on:
        time.sleep(2)
        s = twitterUntil(2013,5,2)
        s += twitterSinceID(lastID)
        queryAnswer = searchTwitter("IBM", s)
        if(len(queryAnswer) < 1):
            go_on = False
        else:
            lastID = queryAnswer[0][0]
            IO.writeData("data/scrapeTest.txt", queryAnswer)
            arrTweets += queryAnswer
        print "Tweets returned: " + str(len(queryAnswer))
               
    IO.writeData("data/Tweets.txt", arrTweets)

def searchTestThree(): #Search between an interval
    s = twitterRPP(100)
    s += twitterSince(2013, 5, 1)
    s += twitterUntil(2013, 5, 8)
    
    i = 1
    go_on = True
    
    tweets = []
    
    while(i <= 10 and go_on):
        q = s + twitterPage(i)
        answer = searchTwitter("IBM", q)
        print len(answer)
        if (len(answer) < 1):
            go_on = False
        else:
            time.sleep(1.4)
            i += 1
        tweets += answer
    IO.writeData("data/Tweets.txt", tweets)
    
if __name__ == '__main__':
    #simpleSearch()
    searchTestThree()
    