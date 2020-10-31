import tweepy
import time
import schedule
import random
from datetime import datetime, timedelta

auth = tweepy.OAuthHandler('API Key','API Key Secret')
auth.set_access_token('Access Token','Access Token Secret')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

def retweeter(api, screen_name1):
	tweets = api.user_timeline(screen_name=screen_name1, 
                           # 200 is the maximum allowed count
                           count=5,
                           include_rts = False,
                           # Ensures that tweets over 140 chars are included fully
                           tweet_mode = 'extended'
                           )
	for tweet in tweets:
		#Good for checking and logging
		#print("ID: {}".format(tweet.id))
		#print(tweet.created_at)
		#print(tweet.full_text)

		#if you turn retweets to true or want to avoid retweet replies un comment this section
		#if tweet.in_reply_to_status_id is not None or \
		#	tweet.user.id == api.me().id:
		#	return
		if not tweet.favorited:
			#print('Tweet already liked')
		#else:
			tweet.favorite()
		if not tweet.retweeted:
			#print("already retweeted")
		#else:
			tweet.retweet()
		#print("\n")

def retweeterList():
	MemberList = ['ScreenName1', 'ScreenName2']
	for member in MemberList:
		retweeter(api, member)
		print('checked for new ', member, ' tweets')

schedule.every(10).minutes.do(retweeterList)

while True:
	schedule.run_pending()
	time.sleep(1)
