from dotenv import load_dotenv
from michael_scott import MichaelScott
import os

if __name__ == "__main__":
	load_dotenv()

	MichaelScott({
		'twitter': {
			'api_key': os.environ['TWITTER_API_KEY'],
			'api_key_secret': os.environ['TWITTER_API_KEY_SECRET'],
			'bearer_token': os.environ['TWITTER_BEARER_TOKEN'],
			'access_token': os.environ['TWITTER_ACCESS_TOKEN'],
			'access_token_secret': os.environ['TWITTER_ACCESS_TOKEN_SECRET']
		},
		'giphy': {
			'api_key': os.environ['GIPHY_API_KEY']
		},
	})

