# Phase 1(a): Twitter APIs
# Write test programs to exercise different twitter APIs.
# For example, retrieving tweets, searching per time, hashtags, etc.
# All your programs should be on GitHub including a README file explaining your tests and results.

import twitter_keys

import tweepy
import csv

auth = tweepy.OAuthHandler(twitter_keys.API_key, twitter_keys.API_secret_key)
auth.set_access_token(twitter_keys.Access_token, twitter_keys.Access_token_secret)
api = tweepy.API(auth)

csvFile = open('mytweets.csv', 'w')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#Celtics",count=100, lang="en", since="2020-09-28").items():
	print(tweet.created_at, tweet.text)
	csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])