'''
Created on 1-apr.-2013

@author: Kevin
@author: Brecht
'''
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="RoMx5nWeqf902D7mdEJtFQ"
consumer_secret="mRQx1WJ59mrOOZl41JIKfXTxTnoPIt9wkMT7S2cE"
consumer = "test"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token="1346367678-RVCG9By0PvLYaTRz6psz0wsbjEUo0xR1vlI5hU1"
access_token_secret="osV8f570CVdH2Jcwr9OIBeGf3D56AFCcgZL9aaq90"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print api.me().name
class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)    
    stream.filter(track=['economics'])