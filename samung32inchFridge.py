#!/usr/bin/env python
import sys, os, time
import tweepy
keys = dict(
consumer_key='',
consumer_secret='',
access_token='', 
access_token_secret=''
)

user = "@YOUR_HANDLE"

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

def tweet():
	message=input("tweet: ")
	api.update_status(message)
	print('tweet sent successfully!')
if __name__ == "__main__":
	while 1:
		tweet()
