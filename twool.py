import argparse

import yaml

import tweepy

with open("config/user_data.yml", 'r') as ymlfile:
  cfg = yaml.load(ymlfile)

auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
api = tweepy.API(auth)

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', dest='user_name',
	help='The user_name of any authenticated tweeter user')
parser.add_argument('-c', '--count', dest='count', type=int,
	help='The no of last tweets on the user account', default=5)

namespace=parser.parse_args()

if (namespace.user_name):
	timeline = api.user_timeline(screen_name=namespace.user_name,
	count=namespace.count)
	for tweet in timeline:
		print (tweet.text)
else:
	print 'Invalid user name is passed!'
