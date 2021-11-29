'''
Score Tweets
The purpose of this script is to score tweets.

Author: Josh Reini (joshreini1@gmail.com)
'''

import pandas as pd
import nltk
from ntlk.corpus import stopwords

stopwords = stopwords.words('english')

twitter_data = pd.read_csv('data\\tweets\\tweets.csv')
twitter_data['tokenized_tweet'] = twitter_data.\
    apply(lambda row: nltk.word_tokenize(row['full_text']), axis=1)

twitter_data.to_csv('data\\tweets\\token_tweets.csv')