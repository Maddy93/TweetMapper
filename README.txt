Twitter_Map Assignment 2
UNI : hv2174 & mk3700
Introduction
The assignment has been done in Python on Django framework.
Software used
1. Python
2. Django
3. tweepy- Twitter API
4. Google Maps JavaScript API
5. pymysql
6. python-crontab1.8.1
7. Amazon RDS
8. Amazon Elastic Beanstalk
9. Used Load Balancing Service in EBS
10. Google Maps HeatMap API
11. Amazon EC2
12. Amazon SQS
13. Amazon SNS
14. AlchemyAPI
15. Amazon Worker environmetns
How the application works
1. tweets.py and slistener.py work in collecting the tweets using Streamlistener API of twitter and collect Realtime tweets . The tweets are based on the the keywords given in slistener.py. The tweets are stored and given to a queue. The sentiment.py file reads from queue, calculates sentiment and publishes it to SNS. The tweet collection and sentiment calculations are done in separate workers which interact with each other and the main application through SQS and SNS. 
2. The tweet collection is in run where a cronjob is set to collect tweets periodically. (period can be modified)
3. The tweets are stored dynamically into an Amazon RDS database.
4. The Twittmappapp is deployed in the ElasticBeanStalk(EBS) environment.
5. In the application URL, one can choose the keywords to see the map plotting for.
6. The  map shows the Heatmap of the tweets based on the HeatMap API by Google.
7. The heatmap has a toggle button which can be used to switch the views between positive twets and negative tweets
8. We also display the overall sentiment of the tweets in real-time as we get more tweets

Steps to run the application
1. Go to the URL to run the application
2. Choose keywords for which you want to see the the tweet heat map.

GITHUB URL : https://github.com/Maddy93/cloud
Application URL: http://cloud-env-6efgknpfxp.elasticbeanstalk.com/
