'''
Created on 8-mei-2013

@author: Floris
'''
import json
import urllib2

def searchTwitter(tag):
    url = "https://search.twitter.com/search.json?q=%23" + str(tag)
    text = urllib2.urlopen(url)
    JS = json.loads(text)
    size = len(JS['results'])
    data = []
    row = [None]*3
    for i in range(0,size-1):
        row[0] = JS[i]['created_at']
        row[1] = JS[i]['from_user']
        row[2] = JS[i]['text']
        data.append(row)
    return data

def searchTwitterFrom(tag,lasttweetid):
    url = "https://search.twitter.com/search.json?q=%23" + str(tag) + "%20last_id%3A" + lasttweetid
    text = urllib2.urlopen(url)
    JS = json.loads(text)
    size = len(JS['results'])
    data = []
    row = [None]*3
    for i in range(0,size-1):
        row[0] = JS[i]['created_at']
        row[1] = JS[i]['from_user']
        row[2] = JS[i]['text']
        data.append(row)
    return data