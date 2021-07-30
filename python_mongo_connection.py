# importing pymongo
import os
import tweepy as tw
import pandas as pd
import json
from pymongo import MongoClient
import pymongo
import bson
from bson.raw_bson import RawBSONDocument

# create a database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
print(myclient.list_database_names())

# list of database
dblist = myclient.list_database_names()

# ceated database exists or not

if "mydatabase" in dblist:
  print("The database exists.")
else:
    print("Not exist")

# create collection
mycol = mydb["tweets"]

# check collection exists
collist = mydb.list_collection_names()
if "tweets" in collist:
  print("The collection exists.")


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
              since=date_since).items(10)
print(tweets)
print(type(tweets))



# Iterate and print tweets
txts = []
for tweet in tweets:
    print(tweet.text)
    txts.append(tweet.text)
    #print(txts)

#print(type(txts))
docs = [{'_id':1}, RawBSONDocument(bson.BSON.encode({'docs':txts}))]
   
x = mycol.insert_many(docs,ordered=False)







