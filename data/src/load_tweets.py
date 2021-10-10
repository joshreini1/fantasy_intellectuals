'''
Load Tweets
The purpose of this script is to load tweets using the Twitter API and tweepy package.

Author: Josh Reini (joshreini1@gmail.com)
'''

#load packages
import os
from dotenv import load_dotenv
import tweepy as tw
import pandas as pd

#get twitter api keys from dot env
load_dotenv()
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')


#load text file containing twitter user ids
user_ids = pd.read_csv('..\\users\\twitter_users.csv')
user_ids = pd.DataFrame(user_ids)

#pull tweets using tweepy
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
parser=tw.parsers.JSONParser() #get a nice printed json response

for user in len(user_ids):
    user_id = user_ids['twitter'].values[user]
    user = api.get_user(user_id)

    tweets = api.user_timeline(screen_name=user_id, 
                            # 200 is the maximum allowed count
                            count=200,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )

    for info in tweets[:3]:
        print("ID: {}".format(info.id))
        print(info.created_at)
        print(info.full_text)
        print("\n")