'''
Created on 8-mei-2013

@author: Brecht Deconinck
'''
import json
import urllib2
import Preprocessor

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
        data.append(row)
    return data

if __name__ == '__main__':
    #Search Twitter
    tweets = searchTwitter("IBM")
    #Write Tweets to File
    Preprocessor.writeTwitterData("Tweets.txt", tweets)
    #Read Tweets From File
    tweets = Preprocessor.readTwitterData("Tweets.txt")
    #Show Tweets
    print tweets   
