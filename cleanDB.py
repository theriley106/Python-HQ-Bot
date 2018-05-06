#!/usr/bin/env python
# encoding: utf-8
import csv
import json
import re

letters = ["A", "B", "C", "D"]

DATABASE = []
def readCSV(csvFile):
	with open(csvFile, 'r') as f:
 		reader = csv.reader(f)
		return list(reader)
listOfAnswers = readCSV('HQTriviaScribe_tweets.csv')

for val in listOfAnswers:
	tempDict = {}
	tempDict["timestamp"] = val[0]
	tempVals = val[2].split("\n")
	tempDict["question"] = tempVals[0]
	tempDict["answers"] = []
	for i, val in enumerate(tempVals[1:]):
		nestDict = {}
		nestDict["choice"] = letters[i]
		if '✓' in str(val):
			nestDict["correct"] = True
		else:
			nestDict["correct"] = False
		nestDict["text"] = val.replace(" ✓", "").partition(") ")[2]
		tempDict["answers"].append(nestDict)
	DATABASE.append(tempDict)
print DATABASE
