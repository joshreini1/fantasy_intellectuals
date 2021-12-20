'''
Load Tweets
The purpose of this script is to load tweets using the Twitter API and Twitter package

Author: Josh Reini (joshreini1@gmail.com)
'''
#load packages
import pandas as pd
import os
from dotenv import load_dotenv
import tweepy as tw
from tweepy import OAuthHandler

#get twitter api keys from dot env
load_dotenv()
consumerKey = os.getenv('api_key')
consumerSecret = os.getenv('api_key_secret')
bearer_token = os.getenv('bearer_token')
accessToken = os.getenv('access_token')
accessSecret = os.getenv('access_token_secret')

auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)

api = tw.API(auth, wait_on_rate_limit=True)

def stream_tweets(search_term):
    data = [] # empty list to which tweet_details obj will be added
    counter = 0 # counter to keep track of each iteration
    print(counter)
    for tweet in tw.Cursor(api.search_tweets, q='\"{}\" -filter:retweets'.format(search_term), count=100, lang='en', tweet_mode='extended').items():
        tweet_details = {}
        tweet_details['name'] = tweet.user.screen_name
        tweet_details['tweet'] = tweet.full_text
        tweet_details['retweets'] = tweet.retweet_count
        tweet_details['location'] = tweet.user.location
        tweet_details['created'] = tweet.created_at.strftime("%d-%b-%Y")
        tweet_details['followers'] = tweet.user.followers_count
        tweet_details['is_user_verified'] = tweet.user.verified
        print(tweet_details)
        data.append(tweet_details)
        
        counter += 1
        if counter == 1000:
            break
        else:
            pass
    df = pd.DataFrame(data)
    df.to_csv('..\\tweets\\' + search_term + '.csv', index=False)
    print('done!')
    
search_terms = ['climate change','covid']

if __name__ == "__main__":
    print('Starting to stream...')
    for search_term in search_terms:
        stream_tweets(search_term)