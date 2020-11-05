# Phase 2: Build Your Own Social Media Analyzer

import sys

# Import libraries for twitter analysis
import tweepy
import csv

# Imports the Google Cloud client library
from google.cloud import language_v1

def getAverageSentiment(sentiments):
	'''Takes in a list of sentiments and returns the average score and mangnitude'''
	totalScore, totalMagnitude = 0, 0

	for sentiment in sentiments:
		totalScore += sentiment.score
		totalMagnitude += sentiment.magnitude

	return totalScore/len(sentiments), totalMagnitude/len(sentiments)

def getTweets():
	'''Asks user for hastag, fetches related tweets, and stores to CSV file'''
	csvFile = open('mytweets.csv', 'w')
	csvWriter = csv.writer(csvFile)

	numTweets = 100

	hashtag = ''

	while len(hashtag) < 2 or hashtag[0] != '#':
		hashtag = input('Enter the hastag you would like to analyze sentiment for: ')
		if len(hashtag) >= 1:
			if hashtag[0] != '#':
				print("Note: The first character must be a #")

	for tweet in tweepy.Cursor(api.search,q=hashtag,count=100, lang="en", since="2020-09-28").items(numTweets):
		if verbose:
			print(tweet.created_at, tweet.text)
		csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

	csvFile.close()

def analyzeSentiment():
	'''Analyzes the sentiment for different tweets stored in a CSV file'''
	# Instantiates a client
	client = language_v1.LanguageServiceClient()

	# Creates lists for individual texts to anaylze and semtiment resuls
	texts = []
	sentiments = []

	# Create the text to analyze from the CSV file
	csvFile = open('mytweets.csv', 'r')
	twitterData = csv.reader(csvFile, delimiter = ',')
	for row in twitterData:
		texts.append(row[1])
		if verbose:
			print(row[1])
			print('')

	# Create a document for each of the texts and analyze it for sentiment
	for text in texts:
		document = language_v1.Document(
			content=text,
			type_=language_v1.Document.Type.PLAIN_TEXT)

		# Detects the sentiment of the text
		sentiments.append(client.analyze_sentiment(request={'document' : document}).document_sentiment)

	# Print out the sentiment for each of the texts
	for i in range(len(texts)):
		if verbose:
			print('Text: {}'.format(texts[i]))
			print('Sentiment: {}, {}'.format(sentiments[i].score, sentiments[i].magnitude))

	averageScore, averageMagnitude = getAverageSentiment(sentiments)

	# Print the average sentiment for each of the texts
	print('Average Sentiment Score: {}'.format(averageScore))
	print('Average Sentiment Magnitude: {}'.format(averageMagnitude))


if __name__ == "__main__":
	# Import file with twitter keys
	import twitter_keys
	
	# Setup for Twitter API
	auth = tweepy.OAuthHandler(twitter_keys.API_key, twitter_keys.API_secret_key)
	auth.set_access_token(twitter_keys.Access_token, twitter_keys.Access_token_secret)
	api = tweepy.API(auth)

	verbose = False			#flag used for debug output

	if len(sys.argv) > 1:
		if sys.argv[1] == "-v":
			verbose = True

	getTweets()
	analyzeSentiment()
