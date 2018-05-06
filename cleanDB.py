#!/usr/bin/env python
# encoding: utf-8
import csv
import json
import re
import datetime

letters = ["A", "B", "C", "D"]

DATABASE = []
def readCSV(csvFile):
	with open(csvFile, 'r') as f:
		reader = csv.reader(f)
		return list(reader)

def convertToDateTime(timestamp):
	return datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
listOfAnswers = readCSV('databaseArchive/HQTriviaScribe_tweets.csv')[1:][::-1]
# Reverse list
questionNum = 0
for e, val in enumerate(listOfAnswers):
	tempDict = {}
	tempDict["timestamp"] = val[1]
	try:
		if (convertToDateTime(val[1]) - convertToDateTime(listOfAnswers[e-1][1])).total_seconds() < (60 * 120):
			questionNum += 1
		else:
			questionNum = 1
	except Exception as exp:
		print exp
	tempDict["question_num"] = questionNum
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

with open('DBase.json', 'w') as fp:
	json.dump(DATABASE, fp)
