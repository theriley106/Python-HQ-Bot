#!/usr/bin/env python
# encoding: utf-8
import csv
import json

def readCSV(csvFile):
	with open(csvFile, 'r') as f:
 		reader = csv.reader(f)
		return list(reader)
listOfAnswers = readCSV('HQTriviaScribe_tweets.csv')

for val in listOfAnswers:
	tempVals = val[2].split("\n")
	question = tempVals[0]
	if '✓' in str(val[2]):
		print 'check'
	print str(val[2])
