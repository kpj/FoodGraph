class FileHandler(object):
	def __init__(self, path):
		self.path = path

	def escape_str(self, string):
		return string.replace(r'"', r'\"')

	def save(self, data, num):
		cont = 'var data = ['

		for k1 in data:
			for k2 in data:
				if k2 in data[k1].keys():
					perc = float(data[k1][k2]) / num
					ele = '["%s", "%s", %f],\n' % (self.escape_str(k1), self.escape_str(k2), perc)
					cont += ele

		# remove last ',\n' to make valid json
		cont = cont[:-2]

		with open(self.path, 'w') as fd:
			fd.write(cont)
			fd.write(']')