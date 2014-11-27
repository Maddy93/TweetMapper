'''
Created on 26 Oct 2014

@author: Jack The Ripper
'''

from slistener import SListener
from slistener import track
import time, tweepy, sys
import json
import re

consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def main():
    
    listen = SListener(api)
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."
    global track
    try: 
        stream.filter(track = track)
    except:
        stream.disconnect()

if __name__ == '__main__':
    main()
