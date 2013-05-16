'''
Created on 16-mei-2013

@author: Brecht Deconinck
'''
from Methods.IO import readData_by_line, readData
from Classes import Tweet
from stemming.porter2 import stem

def main():
    #Get Emotions
    arrEmo = getEmotions()
    #Analyse Tweet Emotion
    data = open("data/scrapeCompanies.txt")
    tweet = Tweet.Tweet()
    #Read every tweet
    for line in readData_by_line(data):
        tweet.setTweet(line)
        #Check every emotion
        value = 0
        for emo in arrEmo:
            word = emo[0]
            if word in tweet.tweet:
                #Update value by emotion
                if emo[1] == "1":
                    value = 1
                else:
                    value = -1
            if(value != 0):
                break
        tweet.label = value
        print tweet.label, " " ,tweet.tweet

def getEmotions():
    arr = readData("data/Emotions.txt")
    for index in range(0, len(arr)):
        arr[index][0] = stem(arr[index][0])
    return arr

if __name__ == '__main__':
    main()
