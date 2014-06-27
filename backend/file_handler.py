class FileHandler(object):
	def __init__(self, path):
		self.path = path

	def save(self, data, num):
		with open(self.path, 'w') as fd:
			fd.write('var data = [')

			for k1 in data:
				for k2 in data:
					if k2 in data[k1].keys():
						perc = float(data[k1][k2]) / num
						ele = '["%s", "%s", %f],\n' % (k1, k2, perc)
						fd.write(ele)

			fd.write(']')