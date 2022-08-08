import requests, os, random

class TweetGenerator:
	def __get_random_episode(self):
		seasons = os.listdir('scripts')
		season = seasons[random.randint(0, len(seasons) - 1)]

		episodes = os.listdir('scripts/{0}'.format(season))
		episode = episodes[random.randint(0, len(episodes) - 1)]

		filepath = 'scripts/{0}/{1}'.format(season, episode)

		with open(filepath, 'r') as file:
			lines = file.readlines()

		return lines

	def generate(self):
		lines = self.__get_random_episode()
		break_loop = False
		tries = 0
		max_tries = len(lines)
		found_match = False
		mixable_lines = []
		while not break_loop:
			line = lines[random.randint(0, len(lines) - 1)]
			if len(line) > 280 or len(line) < 140:
				tries += 1
				break_loop = False
				found_match = False
			else:
				mixable_lines.append(line)

			if len(mixable_lines) == 2:
				break_loop = True
				found_match = True
			
			if tries >= max_tries:
				break_loop = True

		if not found_match:
			return self.generate()

		split_fl = mixable_lines[0].split()
		split_sl = mixable_lines[1].split()

		fp_idx = int(len(split_fl) / 2)
		if fp_idx == 0:
			fp_idx = 1
		sp_idx = int(len(split_sl) / 2)
		fp = ' '.join(split_fl[:fp_idx])
		sp = ' '.join(split_sl[sp_idx:])

		fp[0].upper()
		if fp.endswith(('.', '!', '?', '. ', '! ', '? ')):
			sp[0].upper()
		text = '{0} {1}'.format(fp, sp)

		return text


