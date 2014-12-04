#stdlib
import os

def writeLog(tweet_time, tweet_text):
	with open(tweet_time, 'w+') as logFile:
		logFile.write(tweet_text)
