import argparse

import tweepy

auth = tweepy.OAuthHandler(consumer_key='yE7vJQaPOx4NzYdDGdGj2z0Mu',
  consumer_secret='O6ziWt24NtwoowEuIE0ikJTuTuwDwkhlHPngz6AI1cutfCG4ZV')
auth.set_access_token('2916610206-J6yEm9PlkymrpztHx1URt9hJ5K4djgYw3UTns9r',
	'O7keZ627dBQv1Cpbxh0BHGjBCS7VgKghwWkJG3iYsU4l0')
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
