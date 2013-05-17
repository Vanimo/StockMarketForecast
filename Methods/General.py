'''
Created on 17 May 2013

@author: Floris
'''


# Return the ID and date of the most recent tweet saved in the data
def getLastTweetID(sFile):
    from Methods.IO import readLastLine
    line = readLastLine(sFile)
    line = line.split('\t')
    return line[0], line[1]