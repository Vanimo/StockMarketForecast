'''
Created on 8-mei-2013

@author: Brecht Deconinck
@author: Floris Cockaerts

Handles the twitter API for searching tweets
'''
import json
import urllib2
import Preprocessor

def main():
    return

# https://dev.twitter.com/docs/using-search

def searchTwitter(query):
    url = "https://search.twitter.com/search.json?q=" + str(query)
    text = urllib2.urlopen(url).read()
    JS = json.loads(text)
    tweets = JS['results']
    size = len(JS['results'])
    data = []
    row = [None]*4
    for i in range(0,size-1):
        row[0] = tweets[i]['created_at']
        row[1] = tweets[i]['from_user']
        row[2] = tweets[i]['text']
        data.append(row)
    return data

def searchTwitterFrom(tag,lasttweetid):
    query = "%23" + str(tag) + "%20last_id%3A" + lasttweetid
    return searchTwitter(query)
def searchTwitterTag(tag):
    query = "%23" + str(tag)
    return searchTwitter(query)

def writeTweets():
    try:
        f = open("Tweets.txt", "w")
        for i in range(0, len(arrTweets)):
            #datum, user, text
            row = arrTweets[i][0] + "\t" + arrTweets[i][1] + "\t" + arrTweets[i][2] + "\n"
            f.write(row)
    except IOError:
        print 'Error: writing tweets'
    finally:
        f.close()
        print "Write Complete"

if __name__ == '__main__':
    #Get Tweets
    arrTweets = searchTwitterTag("IBM")
    #Write Tweets to File
    from IO import writeData
    writeData("data/Tweets.txt", arrTweets)
    #Read Tweets From File
    tweets = Preprocessor.readTwitterData("data/Tweets.txt")
    #Show Tweets
    print tweets   
