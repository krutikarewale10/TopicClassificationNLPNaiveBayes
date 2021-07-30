import tweepy
from tweepy import OAuthHandler
import json
import datetime as dt
import time
import os
import sys

def load_api():
    ''' Function that loads the twitter API after authorizing the user. '''

    consumer_key = 'WKPCn3SeIEyQbIhE7Ix3kUnEg'
    consumer_secret = 'hH3xLHfL7wlZVeDYxO0fZMUmsdFjhtwFABk2EF0cEXcUJUmlVH'
    access_token = '2915309070-tnzqn7HhGynPdekKmIICVvIhqWxEzSpb4MBAtxF'
    access_secret = '1LxniuYCdbS1BDptSdqaLZLIFvZ6rp6uzQ9BhAS1lXq2V'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    # load the twitter API via tweepy
    return tweepy.API(auth)
