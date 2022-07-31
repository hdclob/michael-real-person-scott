import requests

class Giphy:
	def __init__(self, api_key):
		self.url = 'https://api.giphy.com'
		self.api_key = api_key

	def search_gifs(self, q, offset = 0):
		endpoint = self.url + '/v1/gifs/search'

		resp = requests.get(endpoint, params={
			'api_key': self.api_key,
			'q': q,
			'offset': offset,
			'limit': 1
		})

		resp = resp.json()

		return resp
