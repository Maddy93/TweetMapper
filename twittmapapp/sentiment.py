'''
Created on 26 Nov 2014

@author: Jack The Ripper
'''
import boto
import boto.sqs
from alchemyapi import AlchemyAPI
from boto.sqs.message import Message
from alchemyapi import AlchemyAPI
import boto.sqs
import boto.sns
import json

conn = boto.sqs.connect_to_region("us-west-2")
my_queue = conn.get_queue('myqueue1')
sns = boto.sns.connect_to_region('us-west-2')
topic="arn:aws:sns:us-west-2:410402614078:test"
subject="Sentiment"
alchemyapi = AlchemyAPI()
while 1:
    rs = my_queue.get_messages(message_attributes=['text','latitude','longitude','category']) 
    if rs:
        text_str=rs[0].message_attributes['text']['string_value']
#         print text_str
        latitude_str=rs[0].message_attributes['latitude']['string_value']
        longitude_str=rs[0].message_attributes['longitude']['string_value']
        category_str=rs[0].message_attributes['category']['string_value']
#         print latitude_str
#         print longitude_str
#         print category_str 

        response = alchemyapi.sentiment('text', text_str)
#         print response
        my_queue.delete_message(rs[0])
        if response['status']!="ERROR" and response["docSentiment"]["type"]!='neutral' :
            print "sasd"
            sentiment=response["docSentiment"]["type"]
            sentiment_score=response["docSentiment"]["score"]
#             print response
#             print type(str(sentiment))
            print "Sentiment: ",sentiment
            final_str=str(sentiment)+"#"+latitude_str+"#"+longitude_str+"#"+category_str+"#"+sentiment_score;
#             print final_str
#             js = {}
#             js['sentiment'] = str(sentiment)
#             js['latitude'] = latitude_str
#             js['longitude'] = longitude_str
#             json_str="{\"sentiment\":\""+str(sentiment)+"\",\"latitude\":\""+latitude_str+"\",\"longitude\":\""+longitude_str+"\"}"
            sns.publish(topic,final_str,subject);
