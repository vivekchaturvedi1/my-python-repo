import argparse

import tweepy

auth = tweepy.OAuthHandler(consumer_key='Ip7MXjdkqh8kxzMAhjc4sJMvH',
  consumer_secret='sNZmiwh7RORAaWMyAIIEmc3GH3ELV2Jt3FL9T0JoQry22TLdwa')
auth.set_access_token('2588044008-zqSBbDhlbyfqt7xYN8cJERuvvDfRIn3ppuEEAuZ',
	'TrszDLxkH2Weo7mUKKQT1orjvw84BEtbuB4bcXjtEf86a')
api = tweepy.API(auth)

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', dest='user_name',
	help='The user_name of any authenticated tweeter user', required=True)
parser.add_argument('-c', '--count', dest='count', type=int,
	help='The no of last tweets on the user account', default=5, required=True)

namespace=parser.parse_args()

if (namespace.user_name):
	timeline = api.user_timeline(screen_name=namespace.user_name,
	count=namespace.count)
	for tweet in timeline:
		print (tweet.text)
else:
	print 'Invalid user name is passed!'
