'''
Created on 8-mei-2013

@author: Brecht Deconinck
@author: Floris Cockaerts

Handles the twitter API for searching tweets
'''
import json
import urllib2
import time
import Methods.IO as IO

# Main
def main():
    searchTwitter("DJIA", "scrapeDJIA")
    searchTwitter(["Alcoa", "AmericanExpress", "AT%26T", "Pfizer", "Caterpillar", "HPQ", "HP", "McD", "McDo"], "scrapeDJIA_Companies")
    searchTwitter(["IBM", "AAPL", "MSFT", "Microsoft", "Facebook"], "scrapeCompanies")
    return

# https://dev.twitter.com/docs/using-search
# https://dev.twitter.com/docs/api/1/get/search

def searchTwitter(tags, fileName):    
    print "Start Twitter scraping for " + str(tags)
    j=1
    fileName = "data/" + fileName
    fileExt = ".txt"
    sOptions = twitterRPP(100)
    sQuery = twitterBuildTagString(tags)
    
    # If data file exists, read latest tweet, otherwise skip
    from os.path import exists
    if (exists(fileName+fileExt)):
        lastID, lastTime = getLastTweetID(fileName+fileExt)
        print "Last tweet ID: " + lastID + " at time: " + lastTime
        sOptions += twitterSinceID(lastID) # Manual assignment of the newest tweet we scraped so far
    else:
        print "No file " + fileName + fileExt + " found, searching without maxID"
    
    # Initial search
    tweets = getTweets(sQuery + sOptions)
    if (len(tweets) < 2):
        print "No search results"
        return
    
    # Continue searching from oldest tweet found in every message
    oldestID = tweets[-1][0] # Get ID of the oldest tweet for the next query
    go_on = True
    i=1    
    
    while(go_on):        
        sOptions2 = sOptions + twitterMaxID(oldestID)
        results = getTweets(sQuery + sOptions2, i)
        
        if (len(results) < 2): # Catch empty results, errors and sleep if we'll continue
            go_on = False            
        else:
            time.sleep(1.1) # Sleep a bit so twitter doesn't throw us out
            i += 1
            oldestID = results[-1][0] # Get ID of the oldest tweet for the next query
            
        tweets += results[1:] # First result is tweet with "oldestID", so drop it
        
        if (i>=250): # Backup data if we acquire a lot
            IO.writeData(fileName + "_P" + str(j) + fileExt, tweets, overWrite=True)
            j += 1
            tweets = []
            i = 0
    
    # Save data, if buffer has been used, read buffer files in reversed order
    if (j==1):
        IO.writeData(fileName+fileExt, tweets, True, False)
    else:
        IO.writeData(fileName+fileExt, tweets, True, False)
        j -= 1
        while (j>=1):
            bfr = IO.readData(fileName + "_P" + str(j) + fileExt)            
            IO.writeData(fileName+fileExt, bfr, True, False)
            IO.deleteFile(fileName + "_P" + str(j) + fileExt) # Remove temporary file
            j -= 1
    print "Finished Twitter scrape"

# HTTP GET request and read the answer
def GET_Twitter(FetchAddress):
    attempts = 0
    while attempts < 2:
        try:
            response = urllib2.urlopen(FetchAddress)
            message= response.read()
        except urllib2.HTTPError, e:
            print 'The server didn\'t do the request.'
            print 'Error code: ', str(e.code) + "  address: " + FetchAddress
            time.sleep(4)
            attempts += 1
        except urllib2.URLError, e:
            print 'Failed to reach the server.'
            print 'Reason: ', str(e.code) + "  address: " + FetchAddress
            time.sleep(4)
            attempts += 1
        except Exception, e:
            print 'Something bad happened while grabbing and/or reading a page.'
            print 'Reason: ', str(e.code) + "  address: " + FetchAddress
            time.sleep(4)
            attempts += 1
        else:
            return message
    return []

# Builds the twitter URL and converts the JSON reply
def getTweets(query, ID=0):
    url = "https://search.twitter.com/search.json?q=" + str(query)
    
    text = GET_Twitter(url)
    JS = json.loads(text)
    tweets = JS['results']
    
    size = len(tweets)
    if (size <= 1):
        return []
    data = []
    first = tweets[0]['created_at']
    last = tweets[-1]['created_at']
    print str(ID) + "\t JSON count: " + str(len(tweets)) + "  \tFirst: " + str(first) + "\tLast: " + str(last)
    for i in range(0,size):
        row = [None]*4
        row[0] = tweets[i]['id']
        row[1] = tweets[i]['created_at']
        row[2] = tweets[i]['from_user']
        row[3] = tweets[i]['text']
        data.append(row)
    return data

# Return the ID and date of the most recent tweet saved in the data
def getLastTweetID(sFile):
    line = IO.readLastLine(sFile)
    line = line.split('\t')
    return line[0], line[1]
 
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
def twitterBuildTagString(tags):
    sQuery = "%23"
    firstTag = True
    if(isinstance(tags, (str, unicode))):
        sQuery += tags
    elif(isinstance(tags, (list))):
        for tag in tags:
            if (firstTag):
                sQuery += tag
                firstTag = False
            else:
                sQuery += twitterConcatTags(tag)
    return sQuery
def twitterConcatTags(tag):
    return "%20OR%20%23" + str(tag)

if __name__ == '__main__':
    main()

#def searchTwitter(tag,variables):
    #    query = "%23" + str(tag) + str(variables)
    #    return getTweets(query)
# def simpleSearch():
#     #Get Tweets
#     arrTweets = searchTwitter("IBM","")
#     #Write Tweets to File
#     IO.writeData("data/Tweets.txt", arrTweets)
#     #Read Tweets From File
#     tweets = IO.readData("data/Tweets.txt")
#     #Show Tweets
#     print tweets   
# 
# def searchTestTwo():
#     s = twitterUntil(2013,5,2)
#     arrTweets = searchTwitter("IBM",s)
#     IO.writeData("data/scrapeTest.txt", arrTweets)
#     lastID = arrTweets[0][0]
#     go_on = False
#     
#     while go_on:
#         time.sleep(2)
#         s = twitterUntil(2013,5,2)
#         s += twitterSinceID(lastID)
#         queryAnswer = searchTwitter("IBM", s)
#         if(len(queryAnswer) < 1):
#             go_on = False
#         else:
#             lastID = queryAnswer[0][0]
#             IO.writeData("data/scrapeTest.txt", queryAnswer)
#             arrTweets += queryAnswer
#         print "Tweets returned: " + str(len(queryAnswer))
#                
#     IO.writeData("data/Tweets.txt", arrTweets)
# 
# def searchTestThree(): #Search between an interval
#     s = twitterRPP(100)
#     s += twitterSince(2013, 5, 1)
#     s += twitterUntil(2013, 5, 8)
#     
#     i = 1
#     go_on = True
#     
#     tweets = []
#     
#     while(i <= 14 and go_on):
#         q = s + twitterPage(i)
#         answer = searchTwitter("IBM", q)
#         if (len(answer) < 1):
#             go_on = False
#         else:
#             time.sleep(1.4)
#             i += 1
#         tweets += answer
#     IO.writeData("data/Tweets.txt", tweets)
#def searchTestFour(): #Search backwards in time :o
#    j=1
#    fileName = "data/scrapeDJIA"
#    fileExt = ".txt"
#    s = twitterRPP(100)
#    #lastID = getLastTweetID(fileName+fileExt)
#    #print "Last tweet ID: " + lastID
#    #s += twitterSinceID(lastID) # Manual assignment of the newest tweet we scraped so far
#    
#    #tag = "IBM" # %20 is a space sign
#    ##tag += twitterConcatTags("Apple")
#    #tag += twitterConcatTags("AAPL")
#    #tag += twitterConcatTags("MSFT")
#    #tag += twitterConcatTags("Microsoft")
#    ##tag += twitterConcatTags("FB")
#    #tag += twitterConcatTags("Facebook")
#    tag = "djia"
#    
#    tweets = searchTwitter(tag, s)
#    if (len(tweets) < 2):
#        print "No search results"
#        return
#    
#    oldestID = tweets[-1][0] # Get ID of the oldest tweet for the next query
#    go_on = True
#    i=1
#    
#    
#    while(go_on):        
#        q = s + twitterMaxID(oldestID)
#        results = searchTwitter(tag, q)
#        
#        if (len(results) < 2): # Catch empty results, errors and sleep if we'll continue
#            go_on = False            
#        else:
#            time.sleep(1.1) # Sleep a bit so twitter doesn't throw us out
#            i += 1
#            oldestID = results[-1][0] # Get ID of the oldest tweet for the next query
#            
#        tweets += results[1:] # First result is tweet with "oldestID", so drop it
#        
#        if (i>=250): # Backup data if we acquire a lot
#            IO.writeData(fileName + "_P" + str(j) + fileExt, tweets, overWrite=True)
#            j += 1
#            tweets = []
#            i = 0
#    if (j==1):
#        IO.writeData(fileName+fileExt, tweets, True, False)
#    else:
#        IO.writeData(fileName+fileExt, tweets, True, False)
#        j -= 1
#        while (j>=1):
#            bfr = IO.readData(fileName + "_P" + str(j) + fileExt)            
#            IO.writeData(fileName+fileExt, bfr, True, False)
#            IO.deleteFile(fileName + "_P" + str(j) + fileExt) # Remove temporary file
#            j -= 1  