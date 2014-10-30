from django.core.management.base import BaseCommand, CommandError
from _slistener import SListener
from _slistener import track
import datetime
import time, tweepy, sys
import json
import re


class Command(BaseCommand):
    def handle(self, *args, **options):
        consumer_key='qpUR91PwjvChszV0VFgrc4Hje'
        consumer_secret='q9mPUZE2OsFbaqKUF32ZsY1ry4anZ1k8pNSne56wc3HInmERFu'
        access_token='2845943577-R0g6YRlrdEqSFb2mKy5HXuByQPdpq4TLGrPkmSs'
        access_token_secret='ed5emUSxHENLtqN8nLYvGkbipKAEemFd0fgjsXNPC8GED'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)    
        
        listen = SListener(api)
        stream = tweepy.Stream(auth, listen)
        print "Streaming started..."
        global track 
        try:
            stream.filter(track = track)
        except:
            stream.disconnect()
