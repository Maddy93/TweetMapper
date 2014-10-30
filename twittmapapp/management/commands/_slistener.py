'''
Created on 26 Oct 2014

@author: Jack The Ripper
'''
from tweepy import StreamListener
import json, time, sys
import os, re
import pymysql
import datetime
track = ['halloween','ebola','obama','google']

class SListener(StreamListener):

    def __init__(self, api = None):
        self.conn = pymysql.connect(host='twittdb.cb13za9cehdr.us-west-2.rds.amazonaws.com', user='cloud123', passwd='cloud123', db='twittdb')
        self.start_time = datetime.datetime.now();
        self.conn.autocommit(1)
        self.cur=self.conn.cursor()
        self.api = api or API()
        self.delout  = open('delete.txt', 'a')

    def on_data(self, data):
        if  'in_reply_to_status' in data:
            time=datetime.datetime.now()
            diff=time-self.start_time;
            if(diff < datetime.timedelta(minutes=10)):
                self.on_status(data)
            else:
                sys.exit()
            self.on_status(data)
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
        print 'before'
        if status:
            json_data = json.loads(status)
            id_str=json_data['id_str']
            location=re.escape(json_data['user']['location'])
           
            coordinates=json_data['coordinates']
            if coordinates:
                coordinates_list=coordinates.items()
                longitude=coordinates_list[1][1][0]
                latitude=coordinates_list[1][1][1]
            if not location:
                location=""
            location_ascii =  ''.join([i if ord(i) < 128 else ' ' for i in location])
            category = ""
            for substring in track:
                if substring in status.lower():
                    category = substring
                    break
            if id_str and coordinates and category:
                sql='insert ignore into twittmapapp_tweetdata (id_str,location,category,longitude,latitude) values ("'+id_str+'","'+location_ascii+'","'+category+'",'+str(longitude)+','+str(latitude)+');'
                t=self.cur.execute(sql)   
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