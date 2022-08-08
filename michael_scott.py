import os, tweepy, time, random, string
from giphy import Giphy
from tweet_generator import TweetGenerator
from urllib import request

class MichaelScott:
	def __init__(self, config):
		self.config = {
			'twitter': {
				'api_key': 'xxx',
				'api_key_secret': 'xxx',
				'bearer_token': 'xxx',
				'access_token': 'xxx',
				'access_token_secret': 'xxx'
			},
			'giphy': {
				'api_key': 'xxx'
			},
		}
		self.config.update(config)

		self.post_gif = True

		self.__load_twitter()
		self.__load_giphy()
		self.__load_tweet_generator()
		self.start()

	def __load_twitter(self):
		# V1
		self.twitter = tweepy.API(tweepy.OAuth1UserHandler(
			self.config['twitter']['api_key'],
			self.config['twitter']['api_key_secret'],
			self.config['twitter']['access_token'],
			self.config['twitter']['access_token_secret']
		))

		# V2
		# self.twitter = tweepy.Client(
		# 	consumer_key=self.config['twitter']['api_key'],
		# 	consumer_secret=self.config['twitter']['api_key_secret'],
		# 	access_token=self.config['twitter']['access_token'],
		# 	access_token_secret=self.config['twitter']['access_token_secret'],
		# )

	def __load_giphy(self):
		self.giphy = Giphy(self.config['giphy']['api_key'])

	def __load_tweet_generator(self):
		self.tweet_generator = TweetGenerator()

	def __download_random_gif(self):
		resp = self.giphy.search_gifs('michael scott')

		total_count = resp['pagination']['total_count']

		resp = self.giphy.search_gifs('michael scott', random.randint(0, total_count - 1))

		request.urlretrieve(resp['data'][0]['images']['downsized']['url'], 'temp.gif')

	def start(self):
		self.__download_random_gif()
		# self.twitter.update_status_with_media('', 'temp.gif')

		print('Michael Scott just tweeted a stupid GIF')
		try:
			while True:
				self.post_gif = bool(random.randint(0, 1))
				try:
					if self.post_gif:
						self.__download_random_gif()
						self.twitter.update_status_with_media('', 'temp.gif')

						print('Michael Scott just tweeted a stupid GIF')
					else:
						text = self.tweet_generator.generate()
						self.twitter.update_status(text)

						print('Michael Scott just tweeted something stupid')
				except:
					continue

				time.sleep(random.randint(10, 60) * 60)
		except KeyboardInterrupt:
			print('Michael Scott has stopped running (God bless his soul)')
