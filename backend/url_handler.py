import urllib.request
import re
from pprint import pprint

from bs4 import BeautifulSoup


class UrlHandler(object):
	def __init__(self, url):
		self.url = url

	def load_url(self, url):
		req = urllib.request.Request(url)
		res = urllib.request.urlopen(req)
		return BeautifulSoup(res.read())

	def parse_content(self):
		raise Exception('please implement me')

class AlastraHandler(UrlHandler):
	def __init__(self, type):
		self._base = 'http://recipes2.alastra.com/%s' % type

		self._ignore = ['kg', 'tsp', 'tbsp', 'cup', 'cups', 'l', 'g', 'oz', 'about', '/', '-', 'tablespoon', 'tablespoons', 'lb', 'ml', 'ts', 'tb', 'c']

	def validate(self, url):
		return re.match('[A-z0-9]+\.html', url) != None # I want a boolean

	def parse_recipe(self, url):
		print('Checking \'%s\'' % url)
		cont = self.load_url(url)
		text = cont.find('pre').getText()

		res = []

		
		all_ingredients = re.findall(re.compile(r'^[0-9].*', re.MULTILINE), text)
		for line in all_ingredients:
			if ' or ' in line:
				foo = line.split(' or ')
			else:
				foo = [line]

			for bar in foo:
				words = bar.split(' ')
				out = []
				for w in words:
					if not any(char.isdigit() for char in w) and not w.lower() in self._ignore:
						out.append(w)
				if len(out)>0: res.append(' '.join(out))

		return res

	def parse_content(self):
		cont = self.load_url('%s/default.html' % self._base)
		ret = []

		for cell in cont.find_all('td'):
			res = cell.find_all('a')
			for e in res:
				href = e['href']
				if self.validate(href):
					ret.append(
						self.parse_recipe('%s/%s' % (self._base, href))
					)

			if len(ret) == 3: break
		return ret

if __name__ == '__main__':
	u = AlastraHandler('african')
	pprint(u.parse_content())