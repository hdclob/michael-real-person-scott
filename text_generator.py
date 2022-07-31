import requests

def generateText(prompt):
	resp = requests.post('https://api.deepai.org/api/text-generator', headers={
		'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K',
	}, data={
		'text': prompt
	})

	resp = resp.json()
	return resp

