import tweepy

api_key = 'kpXXI89WorsuuRR8lRSaRZ54I'
api_key_secret = 'DvtBuY2J3udg0omEInJeQJm9mbmUUVOEEGU5dMcRBO9FuSveAW'
access_token = '750243721-yBeLXfNlVi1ChORd5yHTyTlNGzKEsQoOqfWAbL74'
access_token_secret = 'v8DZ5G2zS0uG52j4D3CBiBHf5NXNn2IEqtYFSY7j9D0JW'

auth = tweepy.OAuth1UserHandler(
	api_key, api_key_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)