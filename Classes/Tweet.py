'''
Created on 15-mei-2013

@author: Kevin
'''
import re
from datetime import datetime

class Tweet:
    def __init__(self, _id=0, _tweet="", _date="Mon, 01 January 1900 00:00:00", _user="", _label=0):
        self.id=_id
        self.date=datetime.strptime(_date,"%a, %d %B %Y %H:%M:%S")
        self.user=_user
        self.message=_tweet.rstrip('\n')
        self.label=int(_label)
        
    def setTweet(self, data):
        data = data.split('\t')
        self.id = data[0]
        self.date = datetime.strptime(data[1][:-6],"%a, %d %B %Y %H:%M:%S")
        self.user = data[2]
        #text = data[3].rstrip('\n').lower()
        #self.message = re.sub(r'([a-zA-Z])\1+', r'\1', text)
        self.message = data[3].rstrip('\n')
    
    def getTweetTSV(self, order=['id', 'label', 'date', 'user', 'message', 'trimmedMessage']):
        line = ''
        for part in order:
            if part == 'id':
                line += str(self.id) + '\t'
            elif part == 'label':
                line += str(self.label) + '\t'
            elif part == 'date':
                line += self.getDate() + ' ' + self.getTime() + '\t'
            elif part == 'user':
                line += self.user + '\t'
            elif part == 'message':
                line += self.message
            elif part == 'trimmedMessage':
                #line += re.sub(r'([a-zA-Z])\1+', r'\1', self.message).lower()
                line += self.getTrimmedMessage()
        return line
    
    def getTrimmedMessage(self):
        s = self.message.lower()
        
        badParts = [r'\bhttp[\S]*\b', r'@[\S]*\b']
        for part in badParts:
            s = re.sub(part, '', s, re.IGNORECASE)
            
        #s = re.sub(r'([a-zA-Z])\1+', r'\1', s)
        badChars = ["!", "?", ":", "."]
        for char in badChars:
            s = s.replace(char, "")
        s = " ".join(s.split())
        return s
    
    def removeStopWords(self, stopWords):
        s = self.message
        for word in stopWords:
            self.message = re.sub(r'\b' + word[0] + r'\b', '', self.message, flags = re.IGNORECASE)
        self.message = " ".join(self.message.split())
    
    def containsTag(self, tag):
        if tag in self.message:
            return True
        else:
            return False
    
    # time.struct_time(tm_year=2013, tm_mon=5, tm_mday=2, tm_hour=19, tm_min=14, tm_sec=7, tm_wday=3, tm_yday=122, tm_isdst=-1)
    def getDate(self, trailingZeros=True):
        if (trailingZeros):
            date = self.__trailingZero(self.date['tm_year'], 4)
            date += '/' + self.__trailingZero(self.date['tm_mon'])
            date += '/' + self.__trailingZero(self.date['tm_mday'])
            return date
        else:
            return self.date['tm_year'] + "/" + self.date['tm_mon'] + "/" + self.date['tm_mday']
    
    def getTime(self):
        time = self.__trailingZero(self.date['tm_hour'])
        time += ':' + self.__trailingZero(self.date['tm_min'])
        time += ':' + self.__trailingZero(self.date['tm_sec'])
        return time
    def getHour(self, trailingZeros=True):
        if (trailingZeros):
            return self.__trailingZero(self.date['tm_hour'])
        else:
            return self.date['tm_hour']
    
    def __trailingZero(self, value, digits=2):
        value = str(value)
        while (len(value) < digits):
            value = "0" + value
        return value