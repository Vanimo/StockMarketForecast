'''
Created on 8-mei-2013

@author: Floris
'''
import json
import urllib2



def searchTwitter(query):
    url = "https://search.twitter.com/search.json?q=" + str(query)
    text = urllib2.urlopen(url).read()
    JS = json.loads(text)
    tweets = JS['results']
    size = len(JS['results'])
    data = []
    row = [None]*4
    for i in range(0,size-1):
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

print searchTwitterTag("IBM")