
# Importing Libraries
import os
import tweepy as tw
import pandas as pd
import json
from pymongo import MongoClient
import pymongo
import bson
from bson.raw_bson import RawBSONDocument

consumer_key= 'WKPCn3SeIEyQbIhE7Ix3kUnEg'
consumer_secret= 'hH3xLHfL7wlZVeDYxO0fZMUmsdFjhtwFABk2EF0cEXcUJUmlVH'
access_token= '2915309070-tnzqn7HhGynPdekKmIICVvIhqWxEzSpb4MBAtxF'
access_token_secret= '1LxniuYCdbS1BDptSdqaLZLIFvZ6rp6uzQ9BhAS1lXq2V'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "Health"
date_since = "2020-10-02"
date_until = "2020-10-03"

mongo_docs = []
tweets = tw.Cursor(api.search,
                   q=search_words,
                   lang="en",
                   since=date_since,
                   until=date_until,
                   result_type="recent"
                   ).items(5000)


for tweet in tweets:
    docs = {}
    docs['tweet'] = tweet.text
    docs['user_id'] = str(tweet.id)
    mongo_docs += [docs]

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["health"]

mycol.insert_many( mongo_docs )
#Iterate and print tweets
'''
txts = []
for tweet in tweets:
    print(tweet.text)
    txts.append(tweet.text )
    #print(txts)

print("\n*")
print(docs[txts])

# Fetching tweet id
user_id =[]
for tweet in tw.Cursor(api.user_timeline, screen_name="@IBM", since=date_since, until=date_until).items(5):
    print("ID TWEET: " + str(tweet.id))
    user_id.append(str(tweet.id))



#print(type(txts))
#docs = [{'_id':1}, RawBSONDocument(bson.BSON.encode({'docs':txts}))]
   
#x = mycol.insert_many(docs,ordered=False)



docs = [{'_id': 1}, RawBSONDocument(bson.BSON.encode({'docs':txts}))]
print("\n*")
x = mycol.insert_many(docs,ordered=False)
'''

