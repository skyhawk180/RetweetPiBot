#!/usr/bin/env python2

# A Retweet Bot in Python

import sys
import time
from datetime import datetime
from twython import Twython

class bot:
	def __init__(self, c_key, c_secret, a_token, a_token_secret):
		# Create a Twython API instance
		self.api = Twython(c_key, c_secret, a_token, a_token_secret)

		# Make sure we are authenticated correctly
		try:
			self.api.verify_credentials()
		except:
			sys.exit("Authentication Failed")
	
		self.last_ran = datetime.now()

	@staticmethod
	
	def timestr_to_datetime(timestr):
		#Convert datetime
		timestr = "{0} {1}".format(timestr[:19], datetime.now().year)

		#DateTime converted
		return datetime.strptime(timestr, '%a %b %d %H:%M:%S %Y')


	def retweet_task(self, screen_name):
		#RT any tweets we havent seen it from usr
		print "Checking for new tweets from @{0}".format(screen_name)

		#Get a list of users latest tweets
		timeline = self.api.get_user_timeline(screen_name = screen_name)

		#Loop through and check for new tweets
		for t in timeline:
			tweet_time = bot.timestr_to_datetime(t['created_at'])
			if tweet_time > self.last_ran:
				print "Retweeting {0}".format(t['id'])
				self.api.retweet(id = t['id'])

if __name__ == "__main__":
	#OAuth keys from api.twitter.com
	#Readme file for 'HowTo' details
	c_key=""
	c_secret=""

	#API Token from api.twitter.com
	#Readme file for 'HowTo' Instructions
       a_token=""
       a_token_secret=""


	#Create instance of bot class
	twitter = bot(c_key, c_secret, a_token, a_token_secret)

	#Retweet anything new from @github every 5mins
	#Replace with your favorite Twitter handles.
	#Need to extend the code to retweet from multiple sources. Its quite simple.
		while True:
		# Update the time
	        # Only RT new stuff
	        twitter.retweet_task("github")
		    twitter.last_ran = datetime.now()
		    time.sleep(5 * 60)
