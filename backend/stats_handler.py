class StatsHandler(object):
	def __init__(self):
		self._core = {}
		self.ingredient_num = 0

	def add_entry(self, ingredients):
		self.ingredient_num += len(ingredients)

		for entry in ingredients:
			if not entry in self._core.keys():
				self._core[entry] = {}

			for e in ingredients:
				if entry == e:
					continue
				if not e in self._core[entry].keys():
					self._core[entry][e] = 0

				self._core[entry][e] += 1

	def info(self):
		try:
			from pprint import pprint
		except:
			pass
		pprint(self._core)
		print(self.ingredient_num)