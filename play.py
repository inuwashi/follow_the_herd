import tweepy
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests

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

print(f'Getting data for status {root_id}')
root_status = api.get_status(root_id)

url = f"https://twitter.com/{root_status.user.screen_name}/status/{root_status.id}"
print(url)

print(f'Getting retwitters for status {root_id}')
root_retweeters = api.retweeters(root_id)

print(f'Getting likes for status {root_id}')
page = requests.get(f'{url}/likes')
likes_soup = BeautifulSoup(page.content, 'html.parser')





like_url  = (
    'https://api.twitter.com/2/timeline/liked_by.json?'
    'include_profile_interstitial_type=1&'
    'include_blocking=1&'
    'include_blocked_by=1&'
    'include_followed_by=1&'
    'include_want_retweets=1&'
    'include_mute_edge=1&'
    'include_can_dm=1&'
    'include_can_media_tag=1&'
    'skip_status=1&'
    'cards_platform=Web-12&'
    'include_cards=1&'
    'include_composer_source=true&'
    'include_ext_alt_text=true&'
    'include_reply_count=1&'
    'tweet_mode=extended&'
    'include_entities=true&'
    'include_user_entities=true&'
    'include_ext_media_color=true&'
    'include_ext_media_availability=true&'
    'send_error_codes=true&'
    'tweet_id=1172875481915346949&
    'count=80&'
    'ext=mediaStats%2ChighlightedLabel%2CcameraMoment




import ipdb; ipdb.set_trace()