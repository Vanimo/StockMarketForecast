'''
Created on 9 May 2013

@author: Floris
'''
def readData(sFile):
    tweets = []
    try:
        print "Read Data"
        f = open(sFile, "r")
        data = f.readlines()
        for line in data:
            #strip line from \n and \t
            row = line.strip().split("\t")
            #add row to tweets
            tweets.append([row[0],row[1],row[2]])
        print "Read Complete"
    except IOError:
        print 'Error: reading tweets'
    finally:
        f.close()
    return tweets
    
def writeData(sFile, arr):
    try:
        print "Write Start"
        f = open(sFile, "w")
        for i in range(0, len(arr)):
            #datum, user, text
            row = arr[i][0] + "\t" + arr[i][1] + "\t" + arr[i][2] + "\n"
            f.write(row)
        print "Write Complete"
    except IOError:
        print 'Error: writing tweets'
    finally:
        f.close()