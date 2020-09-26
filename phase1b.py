# Phase1(b): Google NLP
# Write test programs to exercise different Google BLP APIs.  Focus on Sentiment analysis.
# All your programs should be on GitHub including a README file explaining your tests and results.

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def getAverageSentiment(sentiments):
	'''Takes in a list of sentiments and returns the average score and mangnitude'''
	totalScore, totalMagnitude = 0, 0

	for sentiment in sentiments:
		totalScore += sentiment.score
		totalMagnitude += sentiment.magnitude

	return totalScore/len(sentiments), totalMagnitude/len(sentiments)

# Instantiates a client
client = language.LanguageServiceClient()

# Creates lists for individual texts to anaylze and semtiment resuls
texts = []
sentiments = []

# The texts to analyze
texts.append(u'Hello, world!')
texts.append(u'Goodbye, world!')

# Create a document for each of the texts and analyze it for sentiment
for text in texts:
	document = types.Document(
	    content=text,
	    type=enums.Document.Type.PLAIN_TEXT)

	# Detects the sentiment of the text
	sentiments.append(client.analyze_sentiment(document=document).document_sentiment)

# Print out the sentiment for each of the texts
for i in range(len(texts)):
	print('Text: {}'.format(texts[i]))
	print('Sentiment: {}, {}'.format(sentiments[i].score, sentiments[i].magnitude))

averageScore, averageMagnitude = getAverageSentiment(sentiments)


# Print the average sentiment for each of the texts
print('Average Sentiment: {}, {}'.format(averageScore, averageMagnitude))

