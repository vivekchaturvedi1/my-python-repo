#stdlib
import argparse
import os

#3rd party lib
import tweepy
import yaml


#project modules
from log import  writeLog

#with context manager
with open("config/user_data.yml", 'r') as ymlfile:
  cfg = yaml.load(ymlfile)

auth = tweepy.OAuthHandler(cfg['CONSUMER_KEY'], cfg['CONSUMER_SECRET'])
auth.set_access_token(cfg['ACCESS_TOKEN'], cfg['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', dest='userName',
	help='The user_name of any authenticated tweeter user',
	default=cfg['DEFAULT_USER_NAME'])
parser.add_argument('-c', '--count', dest='count', type=int,
	help='The no of last tweets on the user account', default=5)

try:
	os.mkdir("users_log")
except os.error:
	print 'The users_log directory is already present!'

namespace=parser.parse_args()
timeline = api.user_timeline(screen_name=namespace.userName,
	count=namespace.count)
tweet_user=namespace.userName
os.chdir("users_log")

try:
	os.mkdir("%s" %tweet_user)
except os.error:
	print ('The %s directory is already present!' %tweet_user)

os.chdir("%s" %tweet_user)
for tweet in timeline:
	tweet_time=str(tweet.created_at).replace(' ','-').replace(':','-')
	writeLog(tweet_time, tweet.text)
