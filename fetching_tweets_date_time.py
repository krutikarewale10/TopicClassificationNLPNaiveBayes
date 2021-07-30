import tweepy
import csv
import codecs
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Access tokens
auth = tweepy.auth.OAuthHandler('WKPCn3SeIEyQbIhE7Ix3kUnEg', 'hH3xLHfL7wlZVeDYxO0fZMUmsdFjhtwFABk2EF0cEXcUJUmlVH')
auth.set_access_token('2915309070-tnzqn7HhGynPdekKmIICVvIhqWxEzSpb4MBAtxF', '1LxniuYCdbS1BDptSdqaLZLIFvZ6rp6uzQ9BhAS1lXq2V')
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('result1234.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
#e=csvFile.encode('abc.csv')
f = codecs.open('abc.csv',encoding='utf-8', mode='a')
for tweet in tweepy.Cursor(api.search,
q="cool",
since="2020-09-28",
until="2015-09-29",
lang="en").items(100):
#Write a row to the csv file/ I use encode utf-8
    print(tweet);
    csvWriter.writerow([tweet])

