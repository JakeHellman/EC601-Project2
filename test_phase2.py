# Project 4
# Write Unit tests for Project 2
# 	- Learn how to use Actions
# 	- Learn how to use Python Unit Tests

import phase2 as p2
from pytest import approx

class Sentiment:
	def __init__(self, score, magnitude):
		self.score = score
		self.magnitude = magnitude

def test_getAverageSentiment_TC1():
	sentiments = []
	a = Sentiment(1,-.8)
	sentiments.append(a)
	b = Sentiment(0,0)
	sentiments.append(b)
	c = Sentiment(-0.5,-0.2)
	sentiments.append(c)

	assert p2.getAverageSentiment(sentiments)[0] == approx(0.5/3)
	assert p2.getAverageSentiment(sentiments)[1] == approx(-1/3)

def test_getAverageSentiment_TC2():
	sentiments = []
	a = Sentiment(0.1,-1)
	sentiments.append(a)
	b = Sentiment(0.2,-1)
	sentiments.append(b)
	c = Sentiment(0.3,-1)
	sentiments.append(c)

	assert p2.getAverageSentiment(sentiments)[0] == approx(0.2)
	assert p2.getAverageSentiment(sentiments)[1] == approx(-1)
	