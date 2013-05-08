'''
Created on 8-mei-2013

@author: Brecht Deconinck
'''
import json
import urllib2

def main():
    return

def searchTwitter(tag):
    url = "https://search.twitter.com/search.json?q=%23" + str(tag)
    text = urllib2.urlopen(url).read()
    JS = json.loads(text)
    tweets = JS['results']
    size = len(tweets)
    data = []
    row = [None]*3
    for i in range(0,size-1):
        row[0] = tweets[i]['created_at']
        row[1] = tweets[i]['from_user']
        row[2] = tweets[i]['text']
        #print row
        data.append(row)
    return data

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
    arrTweets = searchTwitter("IBM")
    #Write Tweets to File
    writeTweets()
    
    
