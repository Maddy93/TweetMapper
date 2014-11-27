'''
Created on 26 Oct 2014

@author: Jack The Ripper
'''
from tweepy import StreamListener
import json, time, sys
import os, re
import pymysql
import datetime
from boto.sqs.message import Message
# from alchemyapi import AlchemyAPI
import boto.sqs
# import boto.sns

track = ['thanksgiving','ebola','winter','christmas','ferguson']

class SListener(StreamListener):

    def __init__(self, api = None):
        self.conn = pymysql.connect(host='', user='', passwd='', db='twittdb')
#         print self.conn
#         self.alchemyapi = AlchemyAPI()
#         self.sns = boto.sns.connect_to_region('us-west-2')
#         self.topic="arn:aws:sns:us-west-2:410402614078:test"
#         self.subject="Sentiment"
#         self.sns = boto.connect_sns()
        self.t=datetime.datetime.now()
        self.counter=0
        self.conn.autocommit(1)
        self.cur=self.conn.cursor()
        self.api = api or API()
        self.filesize = 0
#         self.fprefix = fprefix
        self.delout  = open('delete.txt', 'a')
        self.connboto = boto.sqs.connect_to_region("us-west-2")
        self.q = self.connboto.create_queue('myqueue1')
        

    def on_data(self, data):
        if  'in_reply_to_status' in data:
            time=datetime.datetime.now()
            diff=time-self.t
            if(diff < datetime.timedelta(hours=10)):
                self.on_status(data)
            else:
                print 'exit'
                sys.exit()
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print warning['message']
            return False

    def on_status(self, status):
        if status:
            json_data = json.loads(status)
            id_str=json_data['id_str']
            location=re.escape(json_data['user']['location'])
           
            coordinates=json_data['coordinates']
            text=json_data['text']
            if coordinates:
                coordinates_list=coordinates.items()
                longitude=coordinates_list[1][1][0]
                latitude=coordinates_list[1][1][1]
            if not location:
                location=""
            location_ascii =  ''.join([i if ord(i) < 128 else ' ' for i in location])
            text_ascii =  ''.join([j if ord(j) < 128 else ' ' for j in text])
            category = ""
            for substring in track:
                if substring in status.lower():
                    category = substring
                    break
            if id_str and coordinates and category:
                sql='insert ignore into twittmapapp_tweetdata (id_str,location,category,longitude,latitude) values ("'+id_str+'","'+location_ascii+'","'+category+'",'+str(longitude)+','+str(latitude)+');'
                t=self.cur.execute(sql)  
                m = Message()
                m.set_body("This message contains text,id,latitude and longitude")
                m.message_attributes = {"text":{"data_type": "String","string_value":text_ascii}, "id":{"data_type": "String","string_value":id_str},"category":{"data_type": "String","string_value":category},"longitude":{"data_type": "String","string_value":str(longitude)},"latitude":{"data_type": "String","string_value":str(latitude)}}
                self.q.write(m)  
#                 print "hi"
#                 response = self.alchemyapi.sentiment("text", text_ascii) 
#                 if response['status']!="ERROR":
#                     print "Sentiment: ", response["docSentiment"]["type"]
#                     self.sns.publish(self.topic, response["docSentiment"]["type"], self.subject);
        return

    def on_delete(self, status_id, user_id):
        self.delout.write( str(status_id) + "\n")
        return

    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return 