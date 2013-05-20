'''
Created on 20 May 2013

@author: Brecht
'''

from Methods import IO
from stemming.porter2 import stem

def getTweetsEmotions_3states(messages):    
    emotions = getEmotions()
    returnValues= [-1] * len(messages)
    
    for i in range(len(messages)):
        for emo in emotions:
            word = emo[0]
            if word in messages[i]:
                returnValues[i] = int(emo[1])
    
    return returnValues

def getTweetEmotion_3states(message, emotions):
    for emo in emotions:
        word = emo[0]
        if word in message:
            return int(emo[1])
    return -1

def getEmotions():
    arr = IO.readData("data/Emotions.txt")
    for index in range(0, len(arr)):
        arr[index][0] = stem(arr[index][0])
    return arr