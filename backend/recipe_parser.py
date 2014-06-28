import re

from helper import ignore_char


class RecipeParser(object):
	def parse(self, content):
		raise Exception('please implement me')

class AlastraParser(RecipeParser):
	@staticmethod
	def parse(text):
		res = []
		all_ingredients = re.findall(re.compile(r'^[0-9].*', re.MULTILINE), text)
		
		for line in all_ingredients:
			if ' or ' in line:
				foo = line.split(' or ')
			else:
				foo = [line]

			for bar in foo:
				words = re.findall(r"[\w']+", bar)
				out = []
				for w in words:
					if not any(char.isdigit() for char in w) and not w.lower().strip(' .()[]{}') in ignore_char:
						out.append(w)
				if len(out)>0: res.append(' '.join(out).strip(' \t\n\r'))

		return res