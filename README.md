# twitter_bot
An automated Twitter bot that likes and retweets from a list of Twitter accounts. Checks every 10 minutes to see if any new tweets by each user on the list, if there is any new tweets it retweets and likes them. It doesn't like or retweet retweets. 

# Setup instructions

1. Sign up or login to https://developer.twitter.com/
2. Create a new stand alone app
3. Make sure the new app has permissions to read and write
4. Replace 'API key', 'API key secret', 'Access Token' and 'Access Token Secret' with your version of each
```
auth = tweepy.OAuthHandler('API Key','API Key Secret')
auth.set_access_token('Access Token','Access Token Secret')
```
5. Replace 'ScreenName1' and "ScreenName2' with the screen names of users you wish to auto retweet and like. Just add to the list if you have more than 2 users you'd like to auto retweet and like their tweets. A twitter accounts stream name is their @ but without the @. For example mine is @BuzzRW, so you would enter 'BuzzRW' in the list.
```
MemberList = ['ScreenName1', 'ScreenName2']
```
6. Run code. If you want it to run 24/7 and don't want to leave your PC on 24/7 you'll have to host it on a sever. I recommend using AWS or Google cloud as you can get a year of hosting for free. If you're not sure how to set up and run the script on a sever here are a couple of good video tutorials. 
[How to Run a Python Script 24/7 for Free (Ubuntu Server on AWS)](https://www.youtube.com/watch?v=BYvKv3kM9pk&ab_channel=CameronCobb)
[Free Hosting for Python Scripts on Google Cloud](https://www.youtube.com/watch?v=5OL7fu2R4M8&t=144s&ab_channel=JayMartMedia)
