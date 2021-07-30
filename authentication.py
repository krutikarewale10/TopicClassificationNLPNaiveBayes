import os
import tweepy as tw
import pandas as pd
import json


consumer_key= 'WKPCn3SeIEyQbIhE7Ix3kUnEg'
consumer_secret= 'hH3xLHfL7wlZVeDYxO0fZMUmsdFjhtwFABk2EF0cEXcUJUmlVH'
access_token= '2915309070-tnzqn7HhGynPdekKmIICVvIhqWxEzSpb4MBAtxF'
access_token_secret= '1LxniuYCdbS1BDptSdqaLZLIFvZ6rp6uzQ9BhAS1lXq2V'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "#wildfires"
date_since = "2020-01-01"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)


# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)

print("\n***")

texts = []
for tweet in tweets:
    texts.append(json.dumps(tweet))
with open('tweet.json','w') as fou:
    json.dump(texts,fou)
    
with open('tweet.json','r') as fin:
    texts= json.load(fin)
for txt in texts:
    print(json.loads(txt)['text'])

'''
tweet_text = pd.DataFrame(data=tweets)
print(tweet_text)
'''

'''
def write_tweets(tweets, filename):
     Function that appends tweets to a file. 

    with open(filename, 'a') as f:
        for tweet in tweets:
            json.dump(tweet._json, f)
            f.write('\n')
'''
    
