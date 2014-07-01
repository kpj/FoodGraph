import json


class FileHandler(object):
	def __init__(self, path):
		self.path = path

	def escape_str(self, string):
		return string.replace(r'"', r'\"')

	def save(self, data, props):
		dat = []
		for k1 in data:
			for k2 in data:
				if k2 in data[k1].keys():
					dat.append([
						self.escape_str(k1),
						self.escape_str(k2),
						float(data[k1][k2]) / props['inum']
					])

		obj = {
			'data': dat,
			'props': props
		}

		with open(self.path, 'w') as fd:
			fd.write('var data = ' + json.dumps(obj))