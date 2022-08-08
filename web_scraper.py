import requests, os, time
from bs4 import BeautifulSoup

def scrape_script(url, filename):
	resp = requests.get(url)

	soup = BeautifulSoup(resp.content, 'html.parser')

	lines = soup.find('div', {'class': 'postbody'}).find_all('p')

	for line in lines:
		if not line.text:
			continue

		strong = line.find('strong')
		if strong is None:
			continue

		strong.decompose()
		
		with open(filename, 'a') as f:
			f.write(line.text[2:])
			f.write('\n')

def scrape(url):
	resp = requests.get(url)

	soup = BeautifulSoup(resp.content, 'html.parser')

	rows = soup.find('table', class_='tablebg').find_all('tr')
	rows = rows[4:]

	for row in rows:
		link = row.find('a')
		if link is None:
			continue

		idx = link.text.find('-')
		text = link.text
		if idx != -1:
			text = link.text[:idx]
		
		text = text.strip()
		idx = text.find('x')
		folder_path = 'scripts/season-{0}'.format(text[:idx])
		file_path = '{0}/episode-{1}.txt'.format(folder_path, text[idx + 1:].replace('/', '-'))

		if not os.path.exists(folder_path):
			os.makedirs(folder_path)

		scrape_script('https://transcripts.foreverdreaming.org' + link.get('href')[1:], file_path)
		time.sleep(1)

	new_link = soup.find('div', class_='box extra-content control-box top').find_all('a')[-1]
	if new_link.text == '»':
		new_url = 'https://transcripts.foreverdreaming.org' + new_link.get('href')[1:]
		return scrape(new_url)

if __name__ == "__main__":
	scrape('https://transcripts.foreverdreaming.org/viewforum.php?f=574')