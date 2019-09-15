import tweepy
import os
from dotenv import load_dotenv


DEBUG = True

# GWt settings from .env file
load_dotenv(verbose=DEBUG)

# Tweeter API access
consumer_key = os.getenv('TWEETER_CONSUMER_KEY')
consumer_secret = os.getenv('TWEETER_CONSUMER_SECRET')
access_token = os.getenv('TWEETER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWEETER_ACCESS_TOKEN_SECRET')



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# import ipdb; ipdb.set_trace()

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# count = 0
# for status in tweepy.Cursor(api.user_timeline).items(100):
#     # process status here
#     count += 1
#     print(count)

#API.retweeters(id)


root_id = os.getenv('ROOT_STATUS_ID')
if not root_id:
    root_id = input('Root tweet status id: ')

root_status = api.get_status(root_id)

print(root_status.lang)