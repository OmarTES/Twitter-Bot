#reference: https://youtu.be/W0wWwglE1Vc by CS Dojo
#Title: twitterBot
#Author: Omar El-Shaarawi
#Date: 30/12/2020
#Describtion: Create a Twitter bot that will tweet.

import tweepy

print('Automated Message')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id) + ' - ' + mention.text)
    
#to be continued