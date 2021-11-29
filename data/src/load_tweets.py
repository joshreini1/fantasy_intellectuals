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
api_key = os.getenv('api_key')
api_key_secret = os.getenv('api_key_secret')
bearer_token = os.getenv('bearer_token')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

#load text file containing twitter user ids
user_ids = pd.read_csv('data\\users\\twitter_users.csv')
user_ids = pd.DataFrame(user_ids)

#pull tweets using tweepy
auth = tw.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
parser=tw.parsers.JSONParser() #get a nice printed json response

twitter_data = []

for i in range(0,len(user_ids)):
    user_id = user_ids['twitter'].values[i]

    print(user_id)
    try:
        tweets = api.user_timeline(screen_name=user_id, 
                                # 200 is the maximum allowed count
                                count=200,
                                include_rts = False,
                                # Necessary to keep full_text 
                                # otherwise only the first 140 words are extracted
                                tweet_mode = 'extended'
                                )
    except Exception:
        pass

    for info in tweets[:3]:
        print("ID: {}".format(info.id))
        print(info.created_at)
        print(info.full_text)
        twitter_data.append({'user_id' : user_id, 'created_at' : info.created_at, 'full_text': info.full_text})
        print("\n")

twitter_data = pd.DataFrame(twitter_data)

twitter_data.to_csv('data\\tweets\\tweets.csv',index=False)