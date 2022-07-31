from random import random
import tweepy, config, random
from giphy import Giphy
from urllib import request
import text_generator

def main():
	# twitter_api = tweepy.API(tweepy.OAuth1UserHandler(
	# 	config.TWITTER_API_KEY, config.TWITTER_API_KEY_SECRET, config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET
	# ))

	# giphy = Giphy(config.GIPHY_API_KEY)

	# resp = giphy.search_gifs('michael scott')

	# total_count = resp['pagination']['total_count']

	# resp = giphy.search_gifs('michael scott', random.randint(0, total_count - 1))

	# request.urlretrieve(resp['data'][0]['images']['original']['url'], 'temp.gif')

	print(text_generator.generateText('jesus'))

if __name__ == "__main__":
    main()

