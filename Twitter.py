'''
Created on 8-mei-2013

@author: Brecht Deconinck
'''
def main():
    return

def getTweets():
    print "Receiving Tweets"
    return [["Tweet 1","Tweet 2","Tweet 3","Tweet 4","Tweet 5"],["a","b","c","d","e"]]

def writeTweets():
    try:
        f = open("Tweets.txt", "w")
        for i in range(0, len(arrTweets[0])):
            row = arrTweets[0][i] + "\t" + arrTweets[1][i] + "\n"
            f.write(row)
    except IOError:
        print 'Error: writing tweets'
    finally:
        f.close()
        print "Write Complete"

if __name__ == '__main__':
    #Get Tweets
    arrTweets = getTweets()
    #Write Tweets to File
    writeTweets()
    
    
