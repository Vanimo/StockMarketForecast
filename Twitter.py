'''
Created on 8-mei-2013

@author: Brecht Deconinck
'''
import json
import urllib2
import Preprocessor

def main():
    return

def searchTwitter(query):
    url = "https://search.twitter.com/search.json?q=" + str(query)
    text = urllib2.urlopen(url).read()
    JS = json.loads(text)
    tweets = JS['results']
    size = len(JS['results'])
    data = []
    row = [None]*4
    for i in range(0,size-1):
<<<<<<< HEAD
        row[0] = tweets[i]['created_at']
        row[1] = tweets[i]['from_user']
        row[2] = tweets[i]['text']
        data.append(row)
    return data

if __name__ == '__main__':
    #Search Twitter
    tweets = searchTwitter("IBM")
=======
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
>>>>>>> cedd9fe575ce837832d0dd90c3654dde398ef60f
    #Write Tweets to File
    Preprocessor.writeTwitterData("Tweets.txt", tweets)
    #Read Tweets From File
    tweets = Preprocessor.readTwitterData("Tweets.txt")
    #Show Tweets
    print tweets   
